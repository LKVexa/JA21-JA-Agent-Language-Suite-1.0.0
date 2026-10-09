# JA21 JA Agent Language
## A Technical Textbook for Auditable Agents, Governed Tools, and Deterministic Replay

**Suite edition:** 1.0.0  
**Language profile:** `ja.agent`  
**Primary extension:** `.jaa`  
**Corpus scale:** 10,000 technical records  
**Example pack:** 1,000 curated scripts

> An agent is not trustworthy because it is fluent. It is trustworthy only to the extent that its identity, authority, evidence, uncertainty, actions, and stopping conditions remain inspectable.

## Preface

This textbook turns the uploaded JA Agent corpus into a standalone, teachable language suite. It is intended for language designers, compiler and runtime engineers, agent-tool authors, safety reviewers, instructors, and advanced students. Every worked program is source-faithful to the supplied corpus.

The corpus specifies expected outcomes but does not include a native production compiler or scheduler. Accordingly, the book distinguishes specified behavior from executed evidence.

## Contents

1. [The JA Agent Language as a Full Suite](#chapter-1-the-ja-agent-language-as-a-full-suite)
2. [Agent Declarations and Stable Identity](#chapter-2-agent-declarations-and-stable-identity)
3. [Roles, Goals, and Success Criteria](#chapter-3-roles-goals-and-success-criteria)
4. [Observation, Knowledge Sources, and Retrieval](#chapter-4-observation-knowledge-sources-and-retrieval)
5. [Plans, Subplans, and Delegation](#chapter-5-plans-subplans-and-delegation)
6. [Tool Schemas and Tool Calls](#chapter-6-tool-schemas-and-tool-calls)
7. [Capability Boundaries and Authorization](#chapter-7-capability-boundaries-and-authorization)
8. [Budgets, Quotas, and Timeouts](#chapter-8-budgets-quotas-and-timeouts)
9. [Memory Scope and Retention](#chapter-9-memory-scope-and-retention)
10. [Confidence, Uncertainty, and Evidence](#chapter-10-confidence-uncertainty-and-evidence)
11. [Events and Multi-Agent Messages](#chapter-11-events-and-multi-agent-messages)
12. [Supervision, Approval, and Policy Escalation](#chapter-12-supervision-approval-and-policy-escalation)
13. [Failure Recovery, Retry, and Termination](#chapter-13-failure-recovery-retry-and-termination)
14. [Prompt-Injection Defense and Secret Handling](#chapter-14-prompt-injection-defense-and-secret-handling)
15. [Audit History and Deterministic Replay](#chapter-15-audit-history-and-deterministic-replay)
16. [Compiler Frontend, AST, Types, Effects, and Capabilities](#chapter-16-compiler-frontend-ast-types-effects-and-capabilities)
17. [R12 and MCRT Lowering](#chapter-17-r12-and-mcrt-lowering)
18. [Scheduler, Sandboxing, and Runtime Evidence](#chapter-18-scheduler-sandboxing-and-runtime-evidence)
19. [Optimization Without Governance Loss](#chapter-19-optimization-without-governance-loss)
20. [Interoperability, Deployment, and Air-Gapped Operation](#chapter-20-interoperability-deployment-and-air-gapped-operation)
21. [Conformance, Certification, and Smithson 8S Coupled Mechanics](#chapter-21-conformance-certification-and-smithson-8s-coupled-mechanics)
22. [Capstone: A Standalone JA Agent Toolchain](#chapter-22-capstone-a-standalone-ja-agent-toolchain)

---

# Chapter 1: The JA Agent Language as a Full Suite

## Learning objectives

- Explain the purpose of `agent_declaration`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

The language treats an agent as a bounded program with identity, authority, evidence, and stopping rules. The full suite connects corpus records, scripts, language contracts, teaching material, and validation tools.

### Agent Declaration

Defines the bounded agent as an auditable language object rather than an implicit process. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00032` · `beginner` · `positive` · `agent_declaration`

```jaa
ja source 0.3
module corpus.ja_agent.example_00032
use Agent
policy no_network

agent JAA_00032 {
    identity "jaa_00032"
    role "audited-coordinator"
    goal complete_task_34 when confidence >= 0.80
    memory session retention 1h
    budget steps 44 tools 4
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
emit mcrt "JAA_00032.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-8bef3ce5427d4e33535f : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `agent_declare`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `agent_declaration` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `agent_declaration`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 2: Agent Declarations and Stable Identity

## Learning objectives

- Explain the purpose of `agent_declaration`, `identity`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Stable identity supports audit, delegation, replay, and responsibility. An identity must survive formatting and optimization while remaining distinct from role, session, and tool identity.

### Agent Declaration

Defines the bounded agent as an auditable language object rather than an implicit process. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Identity

Gives the agent a stable identity that survives lowering and replay. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00032` · `beginner` · `positive` · `agent_declaration`

```jaa
ja source 0.3
module corpus.ja_agent.example_00032
use Agent
policy no_network

agent JAA_00032 {
    identity "jaa_00032"
    role "audited-coordinator"
    goal complete_task_34 when confidence >= 0.80
    memory session retention 1h
    budget steps 44 tools 4
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
emit mcrt "JAA_00032.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-8bef3ce5427d4e33535f : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `agent_declare`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `agent_declaration`, `identity` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `agent_declaration`, `identity`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 3: Roles, Goals, and Success Criteria

## Learning objectives

- Explain the purpose of `role`, `goal`, `success_criteria`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Roles constrain responsibility; goals state desired terminal conditions; success criteria define evidence. Conflating these produces agents that can sound complete without being complete.

### Role

Limits the agent to a declared responsibility and authority surface. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Goal

Expresses the desired terminal condition and its confidence threshold. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Success Criteria

Separates verifiable completion evidence from persuasive narrative. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00005` · `beginner` · `positive` · `goal`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {tool.invoke:approved} ⊢ node-8b7e7b7d102f7b608d1a : AgentPlan ! {state.write} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `observe`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `role`, `goal`, `success_criteria` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `role`, `goal`, `success_criteria`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 4: Observation, Knowledge Sources, and Retrieval

## Learning objectives

- Explain the purpose of `observation`, `knowledge_source`, `retrieval`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Observation is a claim about perceived state. Knowledge sources and retrieval define provenance, admissibility, ranking, and policy. Retrieved text remains untrusted data.

### Observation

Records what the agent perceived, when, and from which environment boundary. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Knowledge Source

Declares admissible local or approved sources and their provenance. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Retrieval

Constrains search, ranking, citation, and no-network behavior. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00011` · `beginner` · `positive` · `knowledge_source`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {tool.invoke:approved} ⊢ node-2ca471e9c1d509145b31 : AgentPlan ! {state.write} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `authorize`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `observation`, `knowledge_source`, `retrieval` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `observation`, `knowledge_source`, `retrieval`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 5: Plans, Subplans, and Delegation

## Learning objectives

- Explain the purpose of `plan`, `subplan`, `delegation`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Plans make causal order inspectable. Subplans bound complexity. Delegation transfers a named task, not unlimited authority, and must preserve confidence, evidence, and return contracts.

### Plan

Defines an ordered, inspectable sequence of guarded actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Subplan

Encapsulates a bounded plan fragment with explicit inputs, outputs, and exit conditions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Delegation

Transfers a named responsibility without silently transferring unrestricted authority. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00025` · `beginner` · `positive` · `delegation`

```jaa
ja source 0.3
module corpus.ja_agent.example_00025
use Agent
policy no_network

agent JAA_00025 {
    identity "jaa_00025"
    role "audited-coordinator"
    goal complete_task_27 when confidence >= 0.80
    memory session retention 1h
    budget steps 37 tools 28
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
emit mcrt "JAA_00025.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {model.infer} ⊢ node-f3685feb975f6f83c14c : AgentPlan ! {ledger.append} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `observe`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `plan`, `subplan`, `delegation` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `plan`, `subplan`, `delegation`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 6: Tool Schemas and Tool Calls

## Learning objectives

- Explain the purpose of `tool_schema`, `tool_call`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

A tool is safe only when its schema, effects, capabilities, inputs, outputs, and failure modes are explicit. A tool call is a governed state transition, not free-form function invocation.

### Tool Schema

Defines tool arguments, return types, effects, capabilities, and policy requirements. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Tool Call

Executes a declared tool only after schema, capability, and policy checks. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00006` · `beginner` · `positive` · `tool_call`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {agent.delegate:bounded} ⊢ node-ae92261306b55ad12f6e : AgentPlan ! {state.read} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `approve`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `tool_schema`, `tool_call` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `tool_schema`, `tool_call`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 7: Capability Boundaries and Authorization

## Learning objectives

- Explain the purpose of `capability_boundary`, `human_approval`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Capability boundaries separate language from authority. Human approval creates a durable gate; authorization must be scoped to a tool, operation, arguments, time, and evidence state.

### Capability Boundary

Separates what an agent can describe, request, authorize, and execute. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Human Approval

Creates a durable approval gate for sensitive or irreversible actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00013` · `beginner` · `positive` · `capability_boundary`

```jaa
ja source 0.3
module corpus.ja_agent.example_00013
use Agent
policy no_network

agent JAA_00013 {
    identity "jaa_00013"
    role "audited-coordinator"
    goal complete_task_15 when confidence >= 0.80
    memory session retention 1h
    budget steps 25 tools 16
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
emit mcrt "JAA_00013.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {model.infer} ⊢ node-b6c10b3413cc69cd4c78 : AgentPlan ! {ledger.append} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `recover`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `capability_boundary`, `human_approval` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `capability_boundary`, `human_approval`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 8: Budgets, Quotas, and Timeouts

## Learning objectives

- Explain the purpose of `budget`, `quota`, `timeout`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Budgets and quotas make resource use part of semantics. Timeouts need explicit expiry behavior so they do not become hidden infinite waits or accidental retries.

### Budget

Bounds steps, tools, tokens, compute, or other declared resources. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Quota

Limits repeated use across a window and prevents invisible resource drift. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Timeout

Defines a deterministic deadline and an explicit response to expiry. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00007` · `beginner` · `positive` · `budget`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {model.infer} ⊢ node-86d38c06d42e3a285e6f : AgentPlan ! {ledger.append} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `delegate`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `budget`, `quota`, `timeout` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `budget`, `quota`, `timeout`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 9: Memory Scope and Retention

## Learning objectives

- Explain the purpose of `memory_scope`, `memory_retention`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Memory scope defines what can be remembered; retention defines how long. Both must be enforced independently of convenience, model context length, or previous success.

### Memory Scope

Restricts which information an agent may retain or retrieve. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Memory Retention

Defines how long memory survives and how it is expired. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00020` · `beginner` · `positive` · `memory_retention`

```jaa
ja source 0.3
module corpus.ja_agent.example_00020
use Agent
policy no_network

agent JAA_00020 {
    identity "jaa_00020"
    role "audited-coordinator"
    goal complete_task_22 when confidence >= 0.80
    memory session retention 1h
    budget steps 32 tools 23
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
emit mcrt "JAA_00020.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-23ba0e6481fb57f12bbc : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `remember`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `memory_scope`, `memory_retention` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `memory_scope`, `memory_retention`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 10: Confidence, Uncertainty, and Evidence

## Learning objectives

- Explain the purpose of `confidence`, `uncertainty`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Confidence is a calibrated estimate. Uncertainty records missing evidence, disagreement, and tolerance bands. Neither should be replaced by polished prose or majority vote.

### Confidence

Declares calibrated belief rather than implying certainty. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Uncertainty

Preserves ambiguity, missing evidence, and tolerance-band conditions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00003` · `beginner` · `positive` · `confidence`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {memory.write:scoped} ⊢ node-4766fe434c968d105bc7 : AgentPlan ! {agent.delegate} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `recover`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `confidence`, `uncertainty` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `confidence`, `uncertainty`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 11: Events and Multi-Agent Messages

## Learning objectives

- Explain the purpose of `event`, `multi_agent_message`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Events activate bounded transitions. Multi-agent messages need typed intent, sender identity, causal parents, confidence, and policy so coordination remains auditable.

### Event

Represents a typed state transition or external observation that may activate a plan. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Multi Agent Message

Carries typed intent, provenance, confidence, and causal identity between agents. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00024` · `beginner` · `positive` · `event`

```jaa
ja source 0.3
module corpus.ja_agent.example_00024
use Agent
policy no_network

agent JAA_00024 {
    identity "jaa_00024"
    role "audited-coordinator"
    goal complete_task_26 when confidence >= 0.80
    memory session retention 1h
    budget steps 36 tools 27
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
emit mcrt "JAA_00024.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {agent.delegate:bounded} ⊢ node-79877d82f0278d197647 : AgentPlan ! {state.read} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `tool_call`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `event`, `multi_agent_message` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `event`, `multi_agent_message`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 12: Supervision, Approval, and Policy Escalation

## Learning objectives

- Explain the purpose of `supervision`, `human_approval`, `policy_escalation`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Supervision defines intervention rights. Approval authorizes a bounded action. Escalation transfers unresolved judgement to a stronger authority without erasing the original uncertainty.

### Supervision

Makes oversight state, intervention rights, and escalation behavior explicit. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Human Approval

Creates a durable approval gate for sensitive or irreversible actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Policy Escalation

Routes unresolved or high-risk decisions to a stronger authority. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00017` · `beginner` · `positive` · `human_approval`

```jaa
ja source 0.3
module corpus.ja_agent.example_00017
use Agent
policy no_network

agent JAA_00017 {
    identity "jaa_00017"
    role "audited-coordinator"
    goal complete_task_19 when confidence >= 0.80
    memory session retention 1h
    budget steps 29 tools 20
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
emit mcrt "JAA_00017.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {tool.invoke:approved} ⊢ node-71be84e3d2d4fa7608e6 : AgentPlan ! {state.write} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `delegate`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `supervision`, `human_approval`, `policy_escalation` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `supervision`, `human_approval`, `policy_escalation`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 13: Failure Recovery, Retry, and Termination

## Learning objectives

- Explain the purpose of `failure_recovery`, `retry`, `termination`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Recovery restores a safe state; retry repeats under a reasoned limit; termination guarantees a stop. These are different constructs and should never be inferred from one another.

### Failure Recovery

Defines safe restoration or degraded-mode behavior after a failed action. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Retry

Constrains repetition with reason, limit, backoff, and idempotence. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Termination

Guarantees an explicit stop condition and prevents unbounded continuation. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00008` · `beginner` · `positive` · `failure_recovery`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-1a28f4da0439a6c540e6 : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `plan`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `failure_recovery`, `retry`, `termination` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `failure_recovery`, `retry`, `termination`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 14: Prompt-Injection Defense and Secret Handling

## Learning objectives

- Explain the purpose of `prompt_injection_defense`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Prompt injection exploits confusion between data and instruction. The language must preserve instruction hierarchy, isolate retrieved text, redact secrets, and deny authority amplification.

### Prompt Injection Defense

Treats retrieved or tool-provided text as untrusted data unless policy authorizes instruction status. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00004` · `beginner` · `positive` · `prompt_injection_defense`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {memory.read:scoped} ⊢ node-159db749e964931863f9 : AgentPlan ! {model.infer} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `tool_call`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `prompt_injection_defense` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `prompt_injection_defense`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 15: Audit History and Deterministic Replay

## Learning objectives

- Explain the purpose of `audit_history`, `deterministic_replay`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Audit history records causal evidence; deterministic replay tests whether the same stable inputs and policy state reproduce the bounded path. Replay must include approvals, tool versions, and failures.

### Audit History

Preserves causal, policy, tool, and decision evidence. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Deterministic Replay

Reconstructs the same bounded decision path from stable inputs and identities. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00018` · `beginner` · `positive` · `audit_history`

```jaa
ja source 0.3
module corpus.ja_agent.example_00018
use Agent
policy no_network

agent JAA_00018 {
    identity "jaa_00018"
    role "audited-coordinator"
    goal complete_task_20 when confidence >= 0.80
    memory session retention 1h
    budget steps 30 tools 21
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
emit mcrt "JAA_00018.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {agent.delegate:bounded} ⊢ node-d8779129e8eee471bd7b : AgentPlan ! {state.read} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `plan`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `audit_history`, `deterministic_replay` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `audit_history`, `deterministic_replay`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 16: Compiler Frontend, AST, Types, Effects, and Capabilities

## Learning objectives

- Explain the purpose of `agent_declaration`, `tool_schema`, `capability_boundary`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

The compiler translates source into a typed, effect-aware, capability-aware AST. Diagnostics should identify the earliest responsible phase and retain source spans and proof obligations.

### Agent Declaration

Defines the bounded agent as an auditable language object rather than an implicit process. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Tool Schema

Defines tool arguments, return types, effects, capabilities, and policy requirements. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Capability Boundary

Separates what an agent can describe, request, authorize, and execute. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00032` · `beginner` · `positive` · `agent_declaration`

```jaa
ja source 0.3
module corpus.ja_agent.example_00032
use Agent
policy no_network

agent JAA_00032 {
    identity "jaa_00032"
    role "audited-coordinator"
    goal complete_task_34 when confidence >= 0.80
    memory session retention 1h
    budget steps 44 tools 4
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
emit mcrt "JAA_00032.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-8bef3ce5427d4e33535f : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `agent_declare`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `agent_declaration`, `tool_schema`, `capability_boundary` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `agent_declaration`, `tool_schema`, `capability_boundary`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 17: R12 and MCRT Lowering

## Learning objectives

- Explain the purpose of `audit_history`, `deterministic_replay`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

R12 records stable semantic relations; MCRT records runtime causality and provenance. Lowering must not collapse confidence, policy, authority, uncertainty, or interaction order.

### Audit History

Preserves causal, policy, tool, and decision evidence. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Deterministic Replay

Reconstructs the same bounded decision path from stable inputs and identities. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00018` · `beginner` · `positive` · `audit_history`

```jaa
ja source 0.3
module corpus.ja_agent.example_00018
use Agent
policy no_network

agent JAA_00018 {
    identity "jaa_00018"
    role "audited-coordinator"
    goal complete_task_20 when confidence >= 0.80
    memory session retention 1h
    budget steps 30 tools 21
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
emit mcrt "JAA_00018.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {agent.delegate:bounded} ⊢ node-d8779129e8eee471bd7b : AgentPlan ! {state.read} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `plan`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `audit_history`, `deterministic_replay` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `audit_history`, `deterministic_replay`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 18: Scheduler, Sandboxing, and Runtime Evidence

## Learning objectives

- Explain the purpose of `tool_call`, `budget`, `termination`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

The scheduler enforces policy, schemas, budgets, memory, approval, and termination while recording evidence. Sandboxing is a runtime property, not a promise made in source comments.

### Tool Call

Executes a declared tool only after schema, capability, and policy checks. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Budget

Bounds steps, tools, tokens, compute, or other declared resources. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Termination

Guarantees an explicit stop condition and prevents unbounded continuation. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00007` · `beginner` · `positive` · `budget`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {model.infer} ⊢ node-86d38c06d42e3a285e6f : AgentPlan ! {ledger.append} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `delegate`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `tool_call`, `budget`, `termination` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `tool_call`, `budget`, `termination`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 19: Optimization Without Governance Loss

## Learning objectives

- Explain the purpose of `plan`, `confidence`, `human_approval`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Optimization may shorten plans or cache retrieval, but only with proof that authority, causal order, confidence, budgets, approvals, and replay identities remain equivalent.

### Plan

Defines an ordered, inspectable sequence of guarded actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Confidence

Declares calibrated belief rather than implying certainty. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Human Approval

Creates a durable approval gate for sensitive or irreversible actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00003` · `beginner` · `positive` · `confidence`

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

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {memory.write:scoped} ⊢ node-4766fe434c968d105bc7 : AgentPlan ! {agent.delegate} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `recover`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `plan`, `confidence`, `human_approval` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `plan`, `confidence`, `human_approval`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 20: Interoperability, Deployment, and Air-Gapped Operation

## Learning objectives

- Explain the purpose of `multi_agent_message`, `tool_schema`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Interoperability requires stable schemas and provenance across agents and hosts. Deployment preserves no-network defaults, explicit capabilities, local tooling, and reproducible manifests.

### Multi Agent Message

Carries typed intent, provenance, confidence, and causal identity between agents. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Tool Schema

Defines tool arguments, return types, effects, capabilities, and policy requirements. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00016` · `beginner` · `positive` · `multi_agent_message`

```jaa
ja source 0.3
module corpus.ja_agent.example_00016
use Agent
policy no_network

agent JAA_00016 {
    identity "jaa_00016"
    role "audited-coordinator"
    goal complete_task_18 when confidence >= 0.80
    memory session retention 1h
    budget steps 28 tools 19
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
emit mcrt "JAA_00016.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {memory.read:scoped} ⊢ node-265c5f77856d8255a956 : AgentPlan ! {model.infer} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `approve`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `multi_agent_message`, `tool_schema` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `multi_agent_message`, `tool_schema`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 21: Conformance, Certification, and Smithson 8S Coupled Mechanics

## Learning objectives

- Explain the purpose of `uncertainty`, `deterministic_replay`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

Conformance separates modeled expectations from native evidence. The 8S profile is preserved as a proposed computational framework with explicit claim boundaries and independent latent, projected, semantic, and provenance tests.

### Uncertainty

Preserves ambiguity, missing evidence, and tolerance-band conditions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Deterministic Replay

Reconstructs the same bounded decision path from stable inputs and identities. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00027` · `beginner` · `positive` · `deterministic_replay`

```jaa
ja source 0.3
module corpus.ja_agent.example_00027
use Agent
policy no_network

agent JAA_00027 {
    identity "jaa_00027"
    role "audited-coordinator"
    goal complete_task_29 when confidence >= 0.80
    memory session retention 1h
    budget steps 39 tools 30
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
emit mcrt "JAA_00027.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {memory.write:scoped} ⊢ node-86a9937689a2581bde9a : AgentPlan ! {agent.delegate} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `delegate`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `uncertainty`, `deterministic_replay` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `uncertainty`, `deterministic_replay`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Chapter 22: Capstone: A Standalone JA Agent Toolchain

## Learning objectives

- Explain the purpose of `agent_declaration`, `plan`, `tool_call`, `audit_history`.
- Trace the construct from source through semantic judgment, AST, R12, MCRT, and validation evidence.
- Identify policy, capability, confidence, replay, and failure obligations.
- Design a structural test and a native-execution test without confusing the two.

The capstone joins parser, semantic checker, policy engine, R12 lowering, scheduler, tool host, MCRT ledger, replay verifier, and certification harness into one bounded toolchain.

### Agent Declaration

Defines the bounded agent as an auditable language object rather than an implicit process. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Plan

Defines an ordered, inspectable sequence of guarded actions. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Tool Call

Executes a declared tool only after schema, capability, and policy checks. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

### Audit History

Preserves causal, policy, tool, and decision evidence. In a conforming implementation, this meaning must remain visible after parsing, optimization, lowering, scheduling, and replay. The implementation should reject any transformation that silently widens authority, deletes evidence, or changes a bounded condition.

## Worked corpus example

**Corpus anchor:** `JAA-00032` · `beginner` · `positive` · `agent_declaration`

```jaa
ja source 0.3
module corpus.ja_agent.example_00032
use Agent
policy no_network

agent JAA_00032 {
    identity "jaa_00032"
    role "audited-coordinator"
    goal complete_task_34 when confidence >= 0.80
    memory session retention 1h
    budget steps 44 tools 4
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
emit mcrt "JAA_00032.mcrt"
```

### Evidence trace

- **Semantic judgment:** `Environment; Policy; {ledger.append} ⊢ node-8bef3ce5427d4e33535f : AgentPlan ! {network.connect} ⇒ validated`
- **Policy decision:** `allow`
- **R12 operator:** `agent_declare`
- **Runtime result:** `success`
- **Expected validation:** `pass`
- **Native status:** `modeled_not_executed`

## Review lenses

| Lens | Review question |
|---|---|
| SOPHIA | Does meaning, confidence, uncertainty, and claim scope remain truthful? |
| CHARLOTTE | Is the construct named, indexed, and connected coherently to the suite? |
| LANDON | Are compiler, runtime, policy, replay, and diagnostic contracts enforceable? |
| Professor | Can a learner explain, test, and repair the construct? |
| Podium | Is the evidence legible, navigable, and publication-ready? |

## Engineering checklist

- Stable source, semantic, AST, R12, and MCRT identities are linked.
- Tool and policy authority is explicit and least-privileged.
- Confidence and uncertainty are preserved rather than cosmetically resolved.
- Budgets, memory, retries, timeouts, and termination remain bounded.
- Expected structural behavior and native execution evidence are reported separately.

## Laboratory

Locate three additional scripts for `agent_declaration`, `plan`, `tool_call`, `audit_history` in `catalogs/SCRIPT_CATALOG.csv`. Compare one positive, one expected-fail, and one boundary or integration case. Produce an evidence packet containing the source, AST node, capability set, policy decision, diagnostic or proof obligation, R12 identity, MCRT identity, and a proposed native test.

## Review questions

1. What semantic mistake is most likely when implementing `agent_declaration`, `plan`, `tool_call`, `audit_history`?
2. Which evidence must survive optimization?
3. What should fail at compile time, and what must remain a runtime check?
4. How would a replay verifier detect authority or causal drift?

---

# Glossary

**Agent plan:** A typed, bounded sequence of observations, decisions, approvals, tool actions, records, and termination conditions.  
**Capability:** A named authority required for an effectful operation.  
**Policy decision:** An allow, deny, or escalation result attached to a specific evidence state.  
**R12:** The suite’s stable semantic-relation representation.  
**MCRT:** The runtime provenance and causal-record representation.  
**Modeled not executed:** Expected behavior encoded by the corpus but not demonstrated by a native implementation.  
**Deterministic replay:** Reproduction of a bounded execution path from stable inputs, identities, versions, approvals, and policy state.
