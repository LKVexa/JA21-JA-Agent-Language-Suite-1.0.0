# JA Agent Language Architecture

```text
Identity + role + goal + success criteria
                │
                ▼
Observation ─ knowledge source ─ retrieval
                │
                ▼
Plan ─ subplan ─ delegation ─ events/messages
                │
                ▼
Tool schema ─ capability gate ─ approval/supervision
                │
                ▼
Budget ─ quota ─ timeout ─ retry/recovery
                │
                ▼
Memory scope ─ audit history ─ deterministic replay
                │
                ▼
R12 lowering ─ MCRT evidence ─ bounded scheduler
```

The architecture rejects the idea that an agent is merely a prompt plus a tool list. It is a typed, policy-governed, evidence-bearing program whose authority and stopping conditions are part of its meaning.
