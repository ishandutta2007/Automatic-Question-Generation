# The Verifiable Self-Play & Alignment Era

RLVR and verifiers.

## Diagram
```mermaid
flowchart TD
  A[LLM Generator] --> B[Sandboxed Verifier]
  B -->|Pass| C[Dataset]
  B -->|Fail| A
```

[Back to README](../README.md)
