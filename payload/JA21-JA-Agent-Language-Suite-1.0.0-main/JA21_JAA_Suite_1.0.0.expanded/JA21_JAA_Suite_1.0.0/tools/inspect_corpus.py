#!/usr/bin/env python3
import argparse,gzip,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('--id'); p.add_argument('--feature'); p.add_argument('--level'); p.add_argument('--class-name'); p.add_argument('--limit',type=int,default=10); a=p.parse_args()
path=ROOT/'corpus/technical/JA21_JAA_TECHNICAL_CORPUS_10000.jsonl.gz'; n=0
with gzip.open(path,'rt',encoding='utf-8') as f:
    for line in f:
        r=json.loads(line); i=r['identity']; e=r['pedagogy']
        if a.id and i['record_id']!=a.id: continue
        if a.feature and e['feature']!=a.feature: continue
        if a.level and e['level']!=a.level: continue
        if a.class_name and e['validation_class']!=a.class_name: continue
        print(json.dumps(r,indent=2,ensure_ascii=False)); n+=1
        if n>=a.limit: break
