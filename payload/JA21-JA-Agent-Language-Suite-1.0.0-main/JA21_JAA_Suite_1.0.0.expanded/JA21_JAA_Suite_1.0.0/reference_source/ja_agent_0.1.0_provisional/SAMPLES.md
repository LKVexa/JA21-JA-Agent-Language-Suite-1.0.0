# JA Agent Language — Corpus Samples



Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## 8S Coupled Mechanics Integration

This document is normalized to the **Smithson 8S Coupled Mechanics v1.0** framework. Candidate \(S^3\) fibers occupy latent penteract centers
\[
\mathbf c_n=\ell\mathbf n,\qquad \mathbf n\in\mathbb Z^5,\qquad \|\mathbf n\|_1\le M.
\]
The fifth coordinate \(t_8\) is an elucidation axis and is admitted only when
\[
\mathbf e_\perp=(I-C_4C_4^+)\mathbf e,\qquad
\eta_{\mathrm{ind}}=\frac{\|\mathbf e_\perp\|_2^2}{\|\mathbf e\|_2^2+\varepsilon}\ge\varepsilon_{\mathrm{ind}},
\]
and the held-out efficacy gain satisfies \(\Delta_{8S}=\operatorname{Score}(\mathcal M_8)-\operatorname{Score}(\mathcal M_7)>\varepsilon_{\mathrm{gain}}\).

Sparse geometric-semantic coupling and selective triadic escalation use
\[
W_{ij}=A_{ij}\exp\!\left[-\frac{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}{2\sigma_c^2}-\frac{d_J(i,j)^2}{2\sigma_J^2}\right],
\]
\[
\dot\theta_i=\omega_i+K_2\sum_jW_{ij}\sin(\theta_j-\theta_i)+K_3\sum_{j,k}H_{ijk}\sin(\theta_j+\theta_k-2\theta_i).
\]
Activation, effective support, and radius are
\[
p_i=\sigma(h_i),\qquad
s_i=p_i\kappa_i(1-\chi_i)(1-\zeta_i)v(\omega_i),\qquad
r_i=r_{\max}B_{5,\infty}(\mathbf c_i)^\alpha s_i^{1/3}.
\]
Each active site carries
\[
F_i=S^3_{r_i}=\{\mathbf y\in\mathbb R^4:\|\mathbf y\|_2=r_i\},
\]
so the noncollapsed total space is locally \(5+3=8\) dimensional.

Relation testing remains independent across latent geometry, product-state separation, visible projection, and judgement space:
\[
g^{(5)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)}-(\lambda_i+\lambda_j),
\]
\[
\delta^{(8)}_{ij}=\sqrt{(\mathbf c_i-\mathbf c_j)^TG_5(\mathbf c_i-\mathbf c_j)+(r_i-r_j)^2},
\]
\[
g^{(3)}_{ij}=\|\Pi_5\mathbf c_i-\Pi_5\mathbf c_j\|_2-(\widehat r_i+\widehat r_j),
\qquad
g^{(J)}_{ij}=d_J(\mathfrak J_i,\mathfrak J_j)-\theta_J.
\]
R12 must retain the fifth-coordinate meaning, \(\eta_{\mathrm{ind}}\), \(W\), optional \(H\), phase, activation/support, \(g^{(5)}\), \(\delta^{(8)}\), \(g^{(3)}\), \(g^{(J)}\), projection version, uncertainty, relation class, interaction order, \(\Delta_{8S}\), provenance, and limitations.

**Example:** If \(g^{(5)}>\mathrm{tol}_5\) but \(g^{(3)}\le\mathrm{tol}_3\), record `PROJECTION_ONLY`; do not replace latent structure with visible appearance.

**Claim boundary:** this is a proposed penteract–\(S^3\) computational framework. The local dimension count is eight where the fiber is noncollapsed, but the construction is not proclaimed to be the standard sphere \(S^8\) without a separate topological proof.
## JAA-00001 — observation

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00001
use Agent
policy no_network

agent JAA_00001 {
    identity "jaa_00001"
    role "audited-coordinator"
    goal complete_task_3 when confidence >= 0.80
    memory session retention 1h
    budget steps 13 tools 4
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00001.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-caa7a77c1522da7029f0",
  "meaning": "Demonstrates observation at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {model.infer} ⊢ node-e81439854f52d620f15e : AgentPlan ! {ledger.append} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "model.infer"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-e81439854f52d620f15e",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "0814ab78e12c1c7b41ceaa76f42d397e860e2e079d5015e5c0bc3d2c0511f0cb",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "observation",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "model.infer"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-e12686b9792f69e1161c",
  "mcrt_reference": "mcrt-f2f9c4555905fffd3f42",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-3adf0493c9bdbd659217",
      "kind": "observation"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-e12686b9792f69e1161c",
    "statement_identity": "JAA-00001",
    "node_identity": "node-e81439854f52d620f15e",
    "language_profile": "ja.agent",
    "semantic_operator": "authorize",
    "sequence": 1,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "model.infer"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "0814ab78e12c1c7b41ceaa76f42d397e860e2e079d5015e5c0bc3d2c0511f0cb"
    ],
    "output_hashes": [
      "857262e009c7bfa3c6272562215f86ec514ef5fb226467f8b390e6723917d412"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00001",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-f2f9c4555905fffd3f42",
    "canonical_tuple": "<v00001, phi_ja_agent, s00001, d0, rho:ja.agent.record_00001, operator:authorize, OMEGA_JAA_authorize, state:integrated, error0, theta00001, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00001.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00001:observation:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "model.infer"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-f2f9c4555905fffd3f42",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "0814ab78e12c1c7b41ceaa76f42d397e860e2e079d5015e5c0bc3d2c0511f0cb",
    "ast_node": "node-e81439854f52d620f15e",
    "semantic_judgment": "sem-caa7a77c1522da7029f0",
    "r12_record": "r12-e12686b9792f69e1161c",
    "sequence": 1,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00001 vector=v00001 category=ja-agent op=authorize key=ja.agent.record_00001 value=\"observation:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates observation at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `authorize`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00002 — retrieval

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00002
use Agent
policy no_network

agent JAA_00002 {
    identity "jaa_00002"
    role "audited-coordinator"
    goal complete_task_4 when confidence >= 0.80
    memory session retention 1h
    budget steps 14 tools 5
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00002.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-580034d1803ed113a29a",
  "meaning": "Demonstrates retrieval at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-cac3381c37bbe3604f63 : AgentPlan ! {network.connect} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "network.connect"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-cac3381c37bbe3604f63",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "f45845b8f378306b76b69327426b47fa4e7d588ee5b18624fa21f8d332187e26",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "retrieval",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "network.connect"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-c4a24c4668c879c0baf5",
  "mcrt_reference": "mcrt-203474ef59c2133487b2",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-73e714fdd518676706e3",
      "kind": "retrieval"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-c4a24c4668c879c0baf5",
    "statement_identity": "JAA-00002",
    "node_identity": "node-cac3381c37bbe3604f63",
    "language_profile": "ja.agent",
    "semantic_operator": "agent_declare",
    "sequence": 2,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "network.connect"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "f45845b8f378306b76b69327426b47fa4e7d588ee5b18624fa21f8d332187e26"
    ],
    "output_hashes": [
      "01b725cb73b9d5511af712faf1d0e89c926386c4e7367e3d69eca182dfb97cce"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00002",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-203474ef59c2133487b2",
    "canonical_tuple": "<v00002, phi_ja_agent, s00002, d0, rho:ja.agent.record_00002, operator:agent_declare, OMEGA_JAA_agent_declare, state:integrated, error0, theta00002, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00002.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00002:retrieval:complete",
  "effects_observed": [
    "network.connect"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-203474ef59c2133487b2",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "f45845b8f378306b76b69327426b47fa4e7d588ee5b18624fa21f8d332187e26",
    "ast_node": "node-cac3381c37bbe3604f63",
    "semantic_judgment": "sem-580034d1803ed113a29a",
    "r12_record": "r12-c4a24c4668c879c0baf5",
    "sequence": 2,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00002 vector=v00002 category=ja-agent op=agent_declare key=ja.agent.record_00002 value=\"retrieval:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates retrieval at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `agent_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00003 — confidence

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00003
use Agent
policy no_network

agent JAA_00003 {
    identity "jaa_00003"
    role "audited-coordinator"
    goal complete_task_5 when confidence >= 0.80
    memory session retention 1h
    budget steps 15 tools 6
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        require human_approval before InspectRepo
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00003.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-e5e690e551e749e1c074",
  "meaning": "Demonstrates confidence at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {memory.write:scoped} ⊢ node-4766fe434c968d105bc7 : AgentPlan ! {agent.delegate} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "agent.delegate"
  ],
  "capabilities": [
    "memory.write:scoped"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-4766fe434c968d105bc7",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "2afcd4229350c742771bd40639c7430d3092bf50d1c7a7da21f1b7d3171f1f42",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "confidence",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "agent.delegate"
  ],
  "capability_requirements": [
    "memory.write:scoped"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-5e3e9834669f9df57d41",
  "mcrt_reference": "mcrt-d1ed44c4c662dab583f8",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-0a1ddfb0f069311e5cbb",
      "kind": "confidence"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-5e3e9834669f9df57d41",
    "statement_identity": "JAA-00003",
    "node_identity": "node-4766fe434c968d105bc7",
    "language_profile": "ja.agent",
    "semantic_operator": "recover",
    "sequence": 3,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "agent.delegate"
    ],
    "capabilities": [
      "memory.write:scoped"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "2afcd4229350c742771bd40639c7430d3092bf50d1c7a7da21f1b7d3171f1f42"
    ],
    "output_hashes": [
      "f36b9899438e25dca308dffb44722818c2003729d527843c8a93f2995f020e18"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00003",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-d1ed44c4c662dab583f8",
    "canonical_tuple": "<v00003, phi_ja_agent, s00003, d0, rho:ja.agent.record_00003, operator:recover, OMEGA_JAA_recover, state:integrated, error0, theta00003, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00003.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00003:confidence:complete",
  "effects_observed": [
    "agent.delegate"
  ],
  "capabilities_consumed": [
    "memory.write:scoped"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-d1ed44c4c662dab583f8",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "2afcd4229350c742771bd40639c7430d3092bf50d1c7a7da21f1b7d3171f1f42",
    "ast_node": "node-4766fe434c968d105bc7",
    "semantic_judgment": "sem-e5e690e551e749e1c074",
    "r12_record": "r12-5e3e9834669f9df57d41",
    "sequence": 3,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00003 vector=v00003 category=ja-agent op=recover key=ja.agent.record_00003 value=\"confidence:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates confidence at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `recover`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00004 — prompt_injection_defense

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00004
use Agent
policy no_network

agent JAA_00004 {
    identity "jaa_00004"
    role "audited-coordinator"
    goal complete_task_6 when confidence >= 0.80
    memory session retention 1h
    budget steps 16 tools 7
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00004.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-d2d2768389cfbd99003d",
  "meaning": "Demonstrates prompt injection defense at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {memory.read:scoped} ⊢ node-159db749e964931863f9 : AgentPlan ! {model.infer} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "model.infer"
  ],
  "capabilities": [
    "memory.read:scoped"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-159db749e964931863f9",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "b00d18193a8d2f1c7d362edbbc30eb1e95ba0772702397047bd88a674001b467",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "prompt_injection_defense",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "model.infer"
  ],
  "capability_requirements": [
    "memory.read:scoped"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-6b8f436e8ebaa9800414",
  "mcrt_reference": "mcrt-86612fffb6890dde2c1e",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-56bfee109bddaf07ce09",
      "kind": "prompt_injection_defense"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-6b8f436e8ebaa9800414",
    "statement_identity": "JAA-00004",
    "node_identity": "node-159db749e964931863f9",
    "language_profile": "ja.agent",
    "semantic_operator": "tool_call",
    "sequence": 4,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "model.infer"
    ],
    "capabilities": [
      "memory.read:scoped"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "b00d18193a8d2f1c7d362edbbc30eb1e95ba0772702397047bd88a674001b467"
    ],
    "output_hashes": [
      "2169d37cfb92274fb441f409f5afeef47a8c670cb6a540b95cab4505cb34b7b3"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00004",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-86612fffb6890dde2c1e",
    "canonical_tuple": "<v00004, phi_ja_agent, s00004, d0, rho:ja.agent.record_00004, operator:tool_call, OMEGA_JAA_tool_call, state:integrated, error0, theta00004, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00004.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00004:prompt_injection_defense:complete",
  "effects_observed": [
    "model.infer"
  ],
  "capabilities_consumed": [
    "memory.read:scoped"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-86612fffb6890dde2c1e",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "b00d18193a8d2f1c7d362edbbc30eb1e95ba0772702397047bd88a674001b467",
    "ast_node": "node-159db749e964931863f9",
    "semantic_judgment": "sem-d2d2768389cfbd99003d",
    "r12_record": "r12-6b8f436e8ebaa9800414",
    "sequence": 4,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00004 vector=v00004 category=ja-agent op=tool_call key=ja.agent.record_00004 value=\"prompt_injection_defense:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates prompt injection defense at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `tool_call`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00005 — goal

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00005
use Agent
policy no_network

agent JAA_00005 {
    identity "jaa_00005"
    role "audited-coordinator"
    goal complete_task_7 when confidence >= 0.80
    memory session retention 1h
    budget steps 17 tools 8
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00005.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-a4137c3a0beee6e566e7",
  "meaning": "Demonstrates goal at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {tool.invoke:approved} ⊢ node-8b7e7b7d102f7b608d1a : AgentPlan ! {state.write} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "tool.invoke:approved"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-8b7e7b7d102f7b608d1a",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "08bd8dcffb79c184d93822cb7c2d7ffd0184c27cf46d90264ed4f1467a2b47df",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "goal",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "tool.invoke:approved"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-a5bacc4c3ab60a9f6bd9",
  "mcrt_reference": "mcrt-6889730d73cb375c8285",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-adfe86e341bc3292bdf6",
      "kind": "goal"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-a5bacc4c3ab60a9f6bd9",
    "statement_identity": "JAA-00005",
    "node_identity": "node-8b7e7b7d102f7b608d1a",
    "language_profile": "ja.agent",
    "semantic_operator": "observe",
    "sequence": 5,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "tool.invoke:approved"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "08bd8dcffb79c184d93822cb7c2d7ffd0184c27cf46d90264ed4f1467a2b47df"
    ],
    "output_hashes": [
      "02c35baafd52f1989f2653bbe23b13a49861dd8cba87a505b1e0edee68e8fece"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00005",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-6889730d73cb375c8285",
    "canonical_tuple": "<v00005, phi_ja_agent, s00005, d0, rho:ja.agent.record_00005, operator:observe, OMEGA_JAA_observe, state:integrated, error0, theta00005, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00005.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00005:goal:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "tool.invoke:approved"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-6889730d73cb375c8285",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "08bd8dcffb79c184d93822cb7c2d7ffd0184c27cf46d90264ed4f1467a2b47df",
    "ast_node": "node-8b7e7b7d102f7b608d1a",
    "semantic_judgment": "sem-a4137c3a0beee6e566e7",
    "r12_record": "r12-a5bacc4c3ab60a9f6bd9",
    "sequence": 5,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00005 vector=v00005 category=ja-agent op=observe key=ja.agent.record_00005 value=\"goal:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates goal at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `observe`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00006 — tool_call

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00006
use Agent
policy no_network

agent JAA_00006 {
    identity "jaa_00006"
    role "audited-coordinator"
    goal complete_task_8 when confidence >= 0.80
    memory session retention 1h
    budget steps 18 tools 9
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        require human_approval before InspectRepo
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00006.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-f88361b65e2dc99069fa",
  "meaning": "Demonstrates tool call at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {agent.delegate:bounded} ⊢ node-ae92261306b55ad12f6e : AgentPlan ! {state.read} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "agent.delegate:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-ae92261306b55ad12f6e",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "f71e51a3425658937795ada880292bb653ad4eb078f9539f04628c870429b2ac",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "tool_call",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "agent.delegate:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-57725fae2fa7b1ad8faf",
  "mcrt_reference": "mcrt-edf49cc0c00e80704f8f",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-cb2e8c8cb5f5e300d92d",
      "kind": "tool_call"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-57725fae2fa7b1ad8faf",
    "statement_identity": "JAA-00006",
    "node_identity": "node-ae92261306b55ad12f6e",
    "language_profile": "ja.agent",
    "semantic_operator": "approve",
    "sequence": 6,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "agent.delegate:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "f71e51a3425658937795ada880292bb653ad4eb078f9539f04628c870429b2ac"
    ],
    "output_hashes": [
      "b8170962e95a41eb03efc554108d12c4e3c1bf9143a73579eaf57c813536acc3"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00006",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-edf49cc0c00e80704f8f",
    "canonical_tuple": "<v00006, phi_ja_agent, s00006, d0, rho:ja.agent.record_00006, operator:approve, OMEGA_JAA_approve, state:integrated, error0, theta00006, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00006.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00006:tool_call:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "agent.delegate:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-edf49cc0c00e80704f8f",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "f71e51a3425658937795ada880292bb653ad4eb078f9539f04628c870429b2ac",
    "ast_node": "node-ae92261306b55ad12f6e",
    "semantic_judgment": "sem-f88361b65e2dc99069fa",
    "r12_record": "r12-57725fae2fa7b1ad8faf",
    "sequence": 6,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00006 vector=v00006 category=ja-agent op=approve key=ja.agent.record_00006 value=\"tool_call:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates tool call at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `approve`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00007 — budget

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00007
use Agent
policy no_network

agent JAA_00007 {
    identity "jaa_00007"
    role "audited-coordinator"
    goal complete_task_9 when confidence >= 0.80
    memory session retention 1h
    budget steps 19 tools 10
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00007.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-cc4581d11c8607b1d288",
  "meaning": "Demonstrates budget at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {model.infer} ⊢ node-86d38c06d42e3a285e6f : AgentPlan ! {ledger.append} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "ledger.append"
  ],
  "capabilities": [
    "model.infer"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-86d38c06d42e3a285e6f",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "ee762eb73bb0d839aa546448c0caa29abd50469d25f6c7c5efd9b4ad3d6e8d69",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "budget",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "ledger.append"
  ],
  "capability_requirements": [
    "model.infer"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-4bba2cc40ad5a4793f4c",
  "mcrt_reference": "mcrt-50a7e94a57afe7e4bf14",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-4652ecf54a80d61d449f",
      "kind": "budget"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-4bba2cc40ad5a4793f4c",
    "statement_identity": "JAA-00007",
    "node_identity": "node-86d38c06d42e3a285e6f",
    "language_profile": "ja.agent",
    "semantic_operator": "delegate",
    "sequence": 7,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "ledger.append"
    ],
    "capabilities": [
      "model.infer"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "ee762eb73bb0d839aa546448c0caa29abd50469d25f6c7c5efd9b4ad3d6e8d69"
    ],
    "output_hashes": [
      "f0213305151e82c26ad3dd086b0db87e85fdecf92e162510f12a11186fabae2a"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00007",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-50a7e94a57afe7e4bf14",
    "canonical_tuple": "<v00007, phi_ja_agent, s00007, d0, rho:ja.agent.record_00007, operator:delegate, OMEGA_JAA_delegate, state:integrated, error0, theta00007, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00007.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00007:budget:complete",
  "effects_observed": [
    "ledger.append"
  ],
  "capabilities_consumed": [
    "model.infer"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-50a7e94a57afe7e4bf14",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "ee762eb73bb0d839aa546448c0caa29abd50469d25f6c7c5efd9b4ad3d6e8d69",
    "ast_node": "node-86d38c06d42e3a285e6f",
    "semantic_judgment": "sem-cc4581d11c8607b1d288",
    "r12_record": "r12-4bba2cc40ad5a4793f4c",
    "sequence": 7,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00007 vector=v00007 category=ja-agent op=delegate key=ja.agent.record_00007 value=\"budget:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates budget at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `delegate`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00008 — failure_recovery

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00008
use Agent
policy no_network

agent JAA_00008 {
    identity "jaa_00008"
    role "audited-coordinator"
    goal complete_task_10 when confidence >= 0.80
    memory session retention 1h
    budget steps 20 tools 11
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00008.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-1d0811064d52bb8aab45",
  "meaning": "Demonstrates failure recovery at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {ledger.append} ⊢ node-1a28f4da0439a6c540e6 : AgentPlan ! {network.connect} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "network.connect"
  ],
  "capabilities": [
    "ledger.append"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-1a28f4da0439a6c540e6",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "662acd885b0866a9974d2122294453b3cac0e783b93703ae3dcc696122d959d3",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "failure_recovery",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "network.connect"
  ],
  "capability_requirements": [
    "ledger.append"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-123d2d272d34b40b6ffa",
  "mcrt_reference": "mcrt-76fa25e534261e1e273c",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-58301ce85bd2797301cd",
      "kind": "failure_recovery"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-123d2d272d34b40b6ffa",
    "statement_identity": "JAA-00008",
    "node_identity": "node-1a28f4da0439a6c540e6",
    "language_profile": "ja.agent",
    "semantic_operator": "plan",
    "sequence": 8,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "network.connect"
    ],
    "capabilities": [
      "ledger.append"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "662acd885b0866a9974d2122294453b3cac0e783b93703ae3dcc696122d959d3"
    ],
    "output_hashes": [
      "89d8f98e24ba3ef76f245fffca61c201aeadd89e2da541ec5e985f4a6c25bab9"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00008",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-76fa25e534261e1e273c",
    "canonical_tuple": "<v00008, phi_ja_agent, s00008, d0, rho:ja.agent.record_00008, operator:plan, OMEGA_JAA_plan, state:integrated, error0, theta00008, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00008.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00008:failure_recovery:complete",
  "effects_observed": [
    "network.connect"
  ],
  "capabilities_consumed": [
    "ledger.append"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-76fa25e534261e1e273c",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "662acd885b0866a9974d2122294453b3cac0e783b93703ae3dcc696122d959d3",
    "ast_node": "node-1a28f4da0439a6c540e6",
    "semantic_judgment": "sem-1d0811064d52bb8aab45",
    "r12_record": "r12-123d2d272d34b40b6ffa",
    "sequence": 8,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00008 vector=v00008 category=ja-agent op=plan key=ja.agent.record_00008 value=\"failure_recovery:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates failure recovery at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `plan`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00009 — policy_escalation

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00009
use Agent
policy no_network

agent JAA_00009 {
    identity "jaa_00009"
    role "audited-coordinator"
    goal complete_task_11 when confidence >= 0.80
    memory session retention 1h
    budget steps 21 tools 12
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        require human_approval before InspectRepo
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00009.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-8408e6cdf47c1ad54264",
  "meaning": "Demonstrates policy escalation at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {memory.write:scoped} ⊢ node-a18a0e8f35f128ebe1c6 : AgentPlan ! {agent.delegate} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "agent.delegate"
  ],
  "capabilities": [
    "memory.write:scoped"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-a18a0e8f35f128ebe1c6",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-6195ec3e37fb4f39",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "a68e777af911ce4eb74f1e6d698a6d594fd17b1779743baa4df798c595742f3f",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "policy_escalation",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "agent.delegate"
  ],
  "capability_requirements": [
    "memory.write:scoped"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-1a21c50eb5848e50bb7d",
  "mcrt_reference": "mcrt-5a03d01fd4c1d1ae64f9",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-4d9e47d9a3462fee58ae",
      "kind": "policy_escalation"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-1a21c50eb5848e50bb7d",
    "statement_identity": "JAA-00009",
    "node_identity": "node-a18a0e8f35f128ebe1c6",
    "language_profile": "ja.agent",
    "semantic_operator": "terminate",
    "sequence": 9,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "agent.delegate"
    ],
    "capabilities": [
      "memory.write:scoped"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "a68e777af911ce4eb74f1e6d698a6d594fd17b1779743baa4df798c595742f3f"
    ],
    "output_hashes": [
      "e0f53c555da72a686c79abda2a84d83420a06fb75c024715d4ca066409048596"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00009",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-5a03d01fd4c1d1ae64f9",
    "canonical_tuple": "<v00009, phi_ja_agent, s00009, d0, rho:ja.agent.record_00009, operator:terminate, OMEGA_JAA_terminate, state:integrated, error0, theta00009, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00009.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00009:policy_escalation:complete",
  "effects_observed": [
    "agent.delegate"
  ],
  "capabilities_consumed": [
    "memory.write:scoped"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-5a03d01fd4c1d1ae64f9",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "a68e777af911ce4eb74f1e6d698a6d594fd17b1779743baa4df798c595742f3f",
    "ast_node": "node-a18a0e8f35f128ebe1c6",
    "semantic_judgment": "sem-8408e6cdf47c1ad54264",
    "r12_record": "r12-1a21c50eb5848e50bb7d",
    "sequence": 9,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00009 vector=v00009 category=ja-agent op=terminate key=ja.agent.record_00009 value=\"policy_escalation:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates policy escalation at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `terminate`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00010 — subplan

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00010
use Agent
policy no_network

agent JAA_00010 {
    identity "jaa_00010"
    role "audited-coordinator"
    goal complete_task_12 when confidence >= 0.80
    memory session retention 1h
    budget steps 22 tools 13
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00010.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-6587d05f6d1dcbd2ff81",
  "meaning": "Demonstrates subplan at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {memory.read:scoped} ⊢ node-0e2a65ece05ea26c8222 : AgentPlan ! {model.infer} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "model.infer"
  ],
  "capabilities": [
    "memory.read:scoped"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-0e2a65ece05ea26c8222",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-caa7a77c1522da70",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "7af31bf469cb1d75b0d35eaecb1b10d75539630b9bb2e13b602d4e149f38d285",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "subplan",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "model.infer"
  ],
  "capability_requirements": [
    "memory.read:scoped"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-f13056166b102b3484b2",
  "mcrt_reference": "mcrt-3a639f6cefb11279ca69",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-ccd328b8f2ae0c17b40e",
      "kind": "subplan"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-f13056166b102b3484b2",
    "statement_identity": "JAA-00010",
    "node_identity": "node-0e2a65ece05ea26c8222",
    "language_profile": "ja.agent",
    "semantic_operator": "remember",
    "sequence": 10,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "model.infer"
    ],
    "capabilities": [
      "memory.read:scoped"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "7af31bf469cb1d75b0d35eaecb1b10d75539630b9bb2e13b602d4e149f38d285"
    ],
    "output_hashes": [
      "898f29eba5c595c747a065a5c381b6dc8ef93d161a6006ce49aea2e19d95b806"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00010",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-3a639f6cefb11279ca69",
    "canonical_tuple": "<v00010, phi_ja_agent, s00010, d0, rho:ja.agent.record_00010, operator:remember, OMEGA_JAA_remember, state:integrated, error0, theta00010, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00010.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00010:subplan:complete",
  "effects_observed": [
    "model.infer"
  ],
  "capabilities_consumed": [
    "memory.read:scoped"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-3a639f6cefb11279ca69",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "7af31bf469cb1d75b0d35eaecb1b10d75539630b9bb2e13b602d4e149f38d285",
    "ast_node": "node-0e2a65ece05ea26c8222",
    "semantic_judgment": "sem-6587d05f6d1dcbd2ff81",
    "r12_record": "r12-f13056166b102b3484b2",
    "sequence": 10,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00010 vector=v00010 category=ja-agent op=remember key=ja.agent.record_00010 value=\"subplan:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates subplan at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `remember`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00011 — knowledge_source

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00011
use Agent
policy no_network

agent JAA_00011 {
    identity "jaa_00011"
    role "audited-coordinator"
    goal complete_task_13 when confidence >= 0.80
    memory session retention 1h
    budget steps 23 tools 14
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        continue when policy_allows
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00011.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-9c294edb61ab17f9cd74",
  "meaning": "Demonstrates knowledge source at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {tool.invoke:approved} ⊢ node-2ca471e9c1d509145b31 : AgentPlan ! {state.write} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "state.write"
  ],
  "capabilities": [
    "tool.invoke:approved"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-2ca471e9c1d509145b31",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-caa7a77c1522da70",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "608758244bdc922e20a64bf66a68689170022553688b372d79e4e98570e041b9",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "knowledge_source",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "state.write"
  ],
  "capability_requirements": [
    "tool.invoke:approved"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-0797681a576b3bc89f28",
  "mcrt_reference": "mcrt-2dd397ab72ee8ef65fb8",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-3a01a9684d5ede0546e3",
      "kind": "knowledge_source"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-0797681a576b3bc89f28",
    "statement_identity": "JAA-00011",
    "node_identity": "node-2ca471e9c1d509145b31",
    "language_profile": "ja.agent",
    "semantic_operator": "authorize",
    "sequence": 11,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "state.write"
    ],
    "capabilities": [
      "tool.invoke:approved"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "608758244bdc922e20a64bf66a68689170022553688b372d79e4e98570e041b9"
    ],
    "output_hashes": [
      "c8e9d8ed5974d49ea805ef713cc090ed09bf60b3ded8811222033cb370b2bcac"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00011",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-2dd397ab72ee8ef65fb8",
    "canonical_tuple": "<v00011, phi_ja_agent, s00011, d0, rho:ja.agent.record_00011, operator:authorize, OMEGA_JAA_authorize, state:integrated, error0, theta00011, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00011.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00011:knowledge_source:complete",
  "effects_observed": [
    "state.write"
  ],
  "capabilities_consumed": [
    "tool.invoke:approved"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-2dd397ab72ee8ef65fb8",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "608758244bdc922e20a64bf66a68689170022553688b372d79e4e98570e041b9",
    "ast_node": "node-2ca471e9c1d509145b31",
    "semantic_judgment": "sem-9c294edb61ab17f9cd74",
    "r12_record": "r12-0797681a576b3bc89f28",
    "sequence": 11,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00011 vector=v00011 category=ja-agent op=authorize key=ja.agent.record_00011 value=\"knowledge_source:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates knowledge source at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `authorize`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

## JAA-00012 — retry

- Level: `beginner`
- Validation class: `positive`
- Expected status: `pass`


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Source
```jaa
ja source 0.3
module corpus.ja_agent.example_00012
use Agent
policy no_network

agent JAA_00012 {
    identity "jaa_00012"
    role "audited-coordinator"
    goal complete_task_14 when confidence >= 0.80
    memory session retention 1h
    budget steps 24 tools 15
    tool InspectRepo(input: Path) -> Report requires tool.invoke:approved
    plan Main {
        observe workspace
        authorize InspectRepo
        require human_approval before InspectRepo
        execute InspectRepo("workspace")
        record mcrt
        terminate when goal.satisfied
    }
}
assert agent.capability_boundary.valid == true
emit mcrt "JAA_00012.mcrt"
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Semantic interpretation
```json
{
  "semantic_id": "sem-624ba0a067723bdca5e1",
  "meaning": "Demonstrates retry at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts.",
  "judgment": "Environment; Policy; {agent.delegate:bounded} ⊢ node-60b03bf9568c806f8d12 : AgentPlan ! {state.read} ⇒ validated",
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effects": [
    "state.read"
  ],
  "capabilities": [
    "agent.delegate:bounded"
  ],
  "policy_decision": "allow",
  "proof_obligations": []
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### AST
```json
{
  "node_id": "node-60b03bf9568c806f8d12",
  "node_kind": "AgentDecl",
  "language_id": "ja.agent",
  "module_id": "module-caa7a77c1522da70",
  "source_span": {
    "line_start": 1,
    "column_start": 1,
    "line_end": 23,
    "column_end": 1
  },
  "origin_hash": "cb16904715c5abe92c4e696b6508210db607e54e64f8d34cc3cef8dcc3146416",
  "attributes": {
    "level": "beginner",
    "validation_class": "positive",
    "feature": "retry",
    "corpus_version": "0.1.0-provisional"
  },
  "declared_type": "AgentPlan",
  "inferred_type": "AgentPlan",
  "effect_set": [
    "state.read"
  ],
  "capability_requirements": [
    "agent.delegate:bounded"
  ],
  "semantic_status": "validated",
  "r12_reference": "r12-c6a7ce7d4c35c0375b04",
  "mcrt_reference": "mcrt-ef681fd776792d62c1a3",
  "children": [
    {
      "role": "domain_construct",
      "node_id": "node-93abf6da969deed6845f",
      "kind": "retry"
    }
  ]
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Compiler representation
```json
{
  "frontend_status": "accepted",
  "diagnostics": [],
  "r12": {
    "record_id": "r12-c6a7ce7d4c35c0375b04",
    "statement_identity": "JAA-00012",
    "node_identity": "node-60b03bf9568c806f8d12",
    "language_profile": "ja.agent",
    "semantic_operator": "agent_declare",
    "sequence": 12,
    "dependencies": [],
    "type": "AgentPlan",
    "effects": [
      "state.read"
    ],
    "capabilities": [
      "agent.delegate:bounded"
    ],
    "policy_decision": "allow",
    "input_hashes": [
      "cb16904715c5abe92c4e696b6508210db607e54e64f8d34cc3cef8dcc3146416"
    ],
    "output_hashes": [
      "03aa3d08b45a421d3a3df68e619d2c3d3ced728376fc91c7e5c9d6b508cbd72d"
    ],
    "state": "lowered",
    "error_status": "error0",
    "confidence": 1.0,
    "proof_status": "satisfied",
    "source_location": {
      "record_id": "JAA-00012",
      "line": 1,
      "column": 1
    },
    "mcrt_reference": "mcrt-ef681fd776792d62c1a3",
    "canonical_tuple": "<v00012, phi_ja_agent, s00012, d0, rho:ja.agent.record_00012, operator:agent_declare, OMEGA_JAA_agent_declare, state:integrated, error0, theta00012, confidence1.0000, status:stable>"
  },
  "artifact": "JAA-00012.jaa.artifact"
}
```


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Runtime representation
```json
{
  "runtime": "JA Agent Scheduler",
  "execution_mode": "deterministic-test",
  "result": "success",
  "expected_output": "JAA-00012:retry:complete",
  "effects_observed": [
    "state.read"
  ],
  "capabilities_consumed": [
    "agent.delegate:bounded"
  ],
  "sandbox": {
    "network": "explicit-only",
    "unknown_code_execution": false,
    "secret_redaction": true
  },
  "mcrt": {
    "record_id": "mcrt-ef681fd776792d62c1a3",
    "record_type": "LEARN_R12",
    "schema_version": "mcrt-0.3",
    "profile": "ja.agent",
    "source_hash": "cb16904715c5abe92c4e696b6508210db607e54e64f8d34cc3cef8dcc3146416",
    "ast_node": "node-60b03bf9568c806f8d12",
    "semantic_judgment": "sem-624ba0a067723bdca5e1",
    "r12_record": "r12-c6a7ce7d4c35c0375b04",
    "sequence": 12,
    "causal_parents": [],
    "determinism_class": "R3-Deterministic",
    "policy_status": "allowed",
    "confidence": 1.0,
    "certification_status": "pass",
    "canonical_record": "LEARN_R12 id=00012 vector=v00012 category=ja-agent op=agent_declare key=ja.agent.record_00012 value=\"retry:positive:deterministic-static-no-hidden-network\" depth=0 confidence=1.0000 status=stable"
  }
}
```


Example: Recalculate q_n(τ), p_n(τ), and r_n(τ) after each phase-integration step, then record the wrapped synchronization error in κ.

### Technical explanation
Demonstrates retry at the beginner level for JA Agent Language. The example is classified as positive and is expected to satisfy the shared JA type, effect, capability, policy, R12, and MCRT contracts. The record follows the JA technical-suite pattern of explicit source, semantic judgment, R12 lowering, MCRT provenance, deterministic behavior, stable identity, and no hidden network execution.


Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.

### Validation result
```json
{
  "expected_status": "pass",
  "actual_status": "modeled_not_executed",
  "class": "positive",
  "diagnostic_code": null,
  "checks": {
    "source_present": true,
    "semantic_interpretation_present": true,
    "ast_contract_complete": true,
    "r12_present": true,
    "mcrt_present": true,
    "capability_path_explicit": true,
    "secret_redaction_required": true,
    "determinism_declared": true
  },
  "note": "Expected validation result generated from the corpus specification; no production compiler was available for execution."
}
```


Example: A two-fiber replay passes when penetration is at most 2% of the smaller radius, wrapped phase error is ≤10⁻⁶ rad, and the tuple hash is identical.

### Optimization notes
- Preserve semantic equivalence for operator `agent_declare`.
- Do not remove capability checks or policy decisions.
- Retain stable node, R12, and MCRT identities after canonicalization.

Example: Apply the coupling mechanics by computing latent geometry first, projected geometry second, and recording both outcomes without forcing tolerance-band cases into a stronger class.
