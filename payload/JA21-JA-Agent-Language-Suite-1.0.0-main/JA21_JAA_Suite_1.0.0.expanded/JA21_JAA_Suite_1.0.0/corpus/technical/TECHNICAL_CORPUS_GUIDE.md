# JA Agent Language Technical Corpus

## Purpose

This directory is the normalized technical heart of the standalone JA21 JA Agent Language Suite. It turns the uploaded seven-document wrapper into an indexed evidence system without discarding source, semantic judgments, AST identity, compiler/R12 evidence, runtime/MCRT evidence, policy decisions, validation expectations, optimization constraints, or Smithson 8S annotations.

## Corpus profile

| Measure | Value |
|---|---:|
| Technical records | 10,000 |
| Agent-language features | 32 |
| Proficiency levels | 10 |
| Validation classes | 10 |
| Expected pass records | 7,500 |
| Expected-fail records | 2,500 |

## Contents

- `JA21_JAA_TECHNICAL_CORPUS_10000.jsonl.gz` — normalized master corpus.
- `jaa_01.jsonl.gz` through `jaa_20.jsonl.gz` — twenty 500-record shards.
- `DOCUMENT_METADATA.json` — preserved document-level coupling-mechanics profile.
- `../schema/` — source and normalized schemas.
- `../index/technical_corpus_index.csv` — compact navigation and analysis index.

## Evidence discipline

Agent output is not accepted merely because it looks helpful. Identity, role, goal, success criteria, observation provenance, retrieval boundaries, tool schemas, capabilities, approvals, budgets, memory retention, confidence, uncertainty, retries, termination, audit history, deterministic replay, and policy decisions remain explicit. R12 and MCRT identities connect source meaning to replay evidence.

## Native-evidence boundary

The records model expected compiler and runtime behavior. No production JA Agent compiler, scheduler, tool host, or native R12/MCRT runtime was supplied. The suite therefore validates structure and provenance, not real tool execution or autonomous deployment.
