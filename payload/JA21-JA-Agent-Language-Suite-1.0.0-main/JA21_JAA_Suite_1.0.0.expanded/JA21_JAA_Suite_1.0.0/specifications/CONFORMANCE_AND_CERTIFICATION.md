# Conformance and Certification

## Test strata

1. Positive acceptance
2. Negative rejection
3. Boundary behavior
4. Integration behavior
5. Security enforcement
6. Performance invariants
7. Deterministic replay
8. Interoperability
9. Recovery
10. Certification holdouts

The corpus contains 250 certification records; the teaching pack includes 25. Certification cases should remain withheld from implementation tuning.

## Minimum conformance evidence

- parser and source-span report;
- typed/effect/capability AST;
- policy and approval decision log;
- tool-schema validation evidence;
- budget, quota, timeout, retry, and termination accounting;
- prompt-injection and secret-handling evidence;
- R12 canonical tuple and MCRT causal record;
- deterministic replay comparison;
- diagnostic identity for expected-fail cases;
- declared limitations and native-execution boundary.
