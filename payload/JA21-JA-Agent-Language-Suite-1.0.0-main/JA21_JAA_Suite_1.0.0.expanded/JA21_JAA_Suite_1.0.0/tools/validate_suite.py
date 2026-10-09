#!/usr/bin/env python3
import csv,gzip,json,pathlib,hashlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]; errors=[]
corpus=ROOT/'corpus/technical/JA21_JAA_TECHNICAL_CORPUS_10000.jsonl.gz'; ids=set(); n=0; features=set(); levels=set(); classes=set()
with gzip.open(corpus,'rt',encoding='utf-8') as f:
    for line in f:
        n+=1
        try:r=json.loads(line)
        except Exception as e: errors.append(f'corpus line {n}: {e}'); continue
        rid=r.get('identity',{}).get('record_id')
        if rid in ids: errors.append(f'duplicate record id: {rid}')
        ids.add(rid); features.add(r['pedagogy']['feature']); levels.add(r['pedagogy']['level']); classes.add(r['pedagogy']['validation_class'])
        for key in ['source','semantic_interpretation','ast','compiler_representation','runtime_representation','validation_result']:
            if key not in r: errors.append(f'{rid}: missing {key}')
if n!=10000: errors.append(f'expected 10000 records, found {n}')
scripts=list((ROOT/'scripts').rglob('*.jaa'))
if len(scripts)!=1000: errors.append(f'expected 1000 scripts, found {len(scripts)}')
with (ROOT/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
if len(rows)!=1000: errors.append(f'expected 1000 catalog rows, found {len(rows)}')
for row in rows:
    p=ROOT/row['script_path']
    if not p.exists(): errors.append(f'missing script: {row["script_path"]}'); continue
    text=p.read_text(encoding='utf-8')
    for token in ['ja source 0.3','module ','use Agent','policy no_network','agent ','identity ','role ','goal ','memory ','budget ','tool ','plan ','record mcrt','terminate when','assert agent.capability_boundary.valid','emit mcrt']:
        if token not in text: errors.append(f'{row["record_id"]}: missing {token!r}')
    if text.count('{')!=text.count('}'): errors.append(f'{row["record_id"]}: unbalanced braces')
    if hashlib.sha256(p.read_bytes()).hexdigest()!=row['source_sha256']: errors.append(f'{row["record_id"]}: script hash mismatch')
if len(features)!=32: errors.append(f'expected 32 features, found {len(features)}')
if len(levels)!=10: errors.append(f'expected 10 levels, found {len(levels)}')
if len(classes)!=10: errors.append(f'expected 10 classes, found {len(classes)}')
maxpath=max(len(str(p.relative_to(ROOT))) for p in ROOT.rglob('*'))
if maxpath>180: errors.append(f'max path exceeds 180: {maxpath}')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print(json.dumps({'status':'PASS','technical_records':n,'unique_record_ids':len(ids),'features':len(features),'levels':len(levels),'validation_classes':len(classes),'scripts':len(scripts),'catalog_rows':len(rows),'max_relative_path':maxpath},indent=2))
