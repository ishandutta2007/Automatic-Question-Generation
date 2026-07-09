# The Distributed Context Padding

Imbalance in GPU clusters.

## Diagram
```mermaid
flowchart TD
  A[Context Blocks] --> B[Length Sorter]
  B --> C[GPU Buckets]
```

[Back to README](../README.md)
