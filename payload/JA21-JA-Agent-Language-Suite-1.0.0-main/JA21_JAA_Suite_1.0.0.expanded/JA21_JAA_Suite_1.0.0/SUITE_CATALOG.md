# Suite Catalog

## Primary deliverables

| Deliverable | Location | Contents |
|---|---|---|
| Technical corpus | `corpus/technical/` | 10,000 normalized records plus twenty shards and document metadata |
| Corpus index | `corpus/index/technical_corpus_index.csv` | Record-to-feature, source hash, semantic, AST, R12, and MCRT map |
| Script example pack | `scripts/` | 1,000 `.jaa` programs, exactly balanced at one-tenth of every level/class stratum |
| Script catalog | `catalogs/SCRIPT_CATALOG.csv` | Searchable explanation and provenance for every program |
| Textbook | `textbook/JA21_JA_AGENT_LANGUAGE_TEXTBOOK.md` | Twenty-two chapters, worked examples, laboratories, review questions, glossary |
| Education pack | `education/` | Twelve-week curriculum, student workbook, instructor guide |
| Language contracts | `specifications/` | EBNF, language, compiler, runtime, R12/MCRT, conformance |
| Publication system | `design/` | Air-gap-safe visual and information hierarchy |
| Offline tools | `tools/` | Corpus inspection and structural validation |
| Evidence | `manifests/` | Machine-readable inventory and SHA-256 checksums |

## Script pack by validation class

| Validation class | Corpus | Script pack |
|---|---:|---:|
| Positive | 4,000 | 400 |
| Negative | 1,500 | 150 |
| Boundary | 1,000 | 100 |
| Integration | 1,000 | 100 |
| Security | 750 | 75 |
| Performance | 500 | 50 |
| Determinism | 500 | 50 |
| Interoperability | 250 | 25 |
| Recovery | 250 | 25 |
| Certification | 250 | 25 |

## Feature coverage

| Feature | Learning track | Corpus | Script pack |
|---|---|---:|---:|
| `agent_declaration` | Foundations & identity | 312 | 104 |
| `audit_history` | Memory & evidence | 312 | 103 |
| `budget` | Resources & timing | 312 | 98 |
| `capability_boundary` | Tools & authority | 312 | 89 |
| `confidence` | Reliability & safety | 313 | 81 |
| `delegation` | Planning & coordination | 312 | 60 |
| `deterministic_replay` | Memory & evidence | 313 | 60 |
| `event` | Planning & coordination | 312 | 55 |
| `failure_recovery` | Reliability & safety | 313 | 40 |
| `goal` | Foundations & identity | 312 | 40 |
| `human_approval` | Tools & authority | 312 | 20 |
| `identity` | Foundations & identity | 312 | 20 |
| `knowledge_source` | Perception & knowledge | 312 | 20 |
| `memory_retention` | Memory & evidence | 312 | 20 |
| `memory_scope` | Memory & evidence | 313 | 20 |
| `multi_agent_message` | Planning & coordination | 313 | 10 |
| `observation` | Perception & knowledge | 313 | 10 |
| `plan` | Planning & coordination | 312 | 10 |
| `policy_escalation` | Tools & authority | 313 | 10 |
| `prompt_injection_defense` | Reliability & safety | 312 | 10 |
| `quota` | Resources & timing | 312 | 10 |
| `retrieval` | Perception & knowledge | 314 | 10 |
| `retry` | Reliability & safety | 312 | 10 |
| `role` | Foundations & identity | 313 | 10 |
| `subplan` | Planning & coordination | 312 | 10 |
| `success_criteria` | Foundations & identity | 314 | 10 |
| `supervision` | Tools & authority | 312 | 10 |
| `termination` | Reliability & safety | 313 | 10 |
| `timeout` | Resources & timing | 313 | 10 |
| `tool_call` | Tools & authority | 312 | 10 |
| `tool_schema` | Tools & authority | 314 | 10 |
| `uncertainty` | Reliability & safety | 312 | 10 |

## Navigation guidance

Use the textbook for sequential learning, the feature atlas for concept lookup, the script catalog for concrete programs and failure modes, the technical corpus for compiler/evaluator/retrieval workflows, and the specifications for implementation and certification.
