# JA21 JA Agent Language Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies bounded plans, tool authority, approvals, memory and termination. Its import boundary is: Reinfer capabilities from actual source; prevent delegated privilege amplification.

## Source and coverage

Original input: `JA21-JA-Agent-Language-Suite-1.0.0-main.zip`. Source SHA 256: `b6941a03799d6509db2a37b36d74de461e98d83f359fa74670b188be2f96b7f2`. The source archive is preserved in the parent folder. All 1,068 original leaf files were read and hashed; 31,008 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### JA-01 High priority

JAA-00001 declares tool.invoke:approved while modeled capability metadata lists model.infer. 8,750 source records have a lexical requirement absent from modeled capability metadata.

Status: **mitigated_by_explicit_evidence_qualification**. Current records are qualified as modeled expectations; source hash and lexical requirement consistency recorded.

Evidence: `JA21_JAA_Suite_1.0.0/corpus/technical/JA21_JAA_TECHNICAL_CORPUS_10000.jsonl.gz | JA21_JAA_Suite_1.0.0/specifications/LANGUAGE_SPECIFICATION.md`.

Remaining gate: A complete versioned profile parser, semantic inference and target/runtime conformance are needed before native admission.

### BASE-08 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Reinfer capabilities from actual source; prevent delegated privilege amplification.

## Contribution to the new fabric language

Profile owner: `ja.agent`. Bounded plans, tool authority, approvals, memory and termination. Reinfer capabilities from actual source; prevent delegated privilege amplification.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
