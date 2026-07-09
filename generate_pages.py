import os

os.makedirs('pages', exist_ok=True)

items = [
    ('The Hand-Crafted Heuristic & Syntax Transformation Era', 'hand-crafted-heuristic.md', 'Deterministic text rules.', 'flowchart TD\n  A[Input Text] --> B[Parse Tree]\n  B --> C[Rule Applier]\n  C --> D[Question]'),
    ('The Neural Sequence-to-Sequence Era', 'neural-seq2seq.md', 'Encoder-Decoder architectures.', 'flowchart TD\n  A[Input Tokens] --> B[Encoder]\n  B --> C[Decoder]\n  C --> D[Question]'),
    ('The Large-Scale Autoregressive Prompting Era', 'autoregressive-prompting.md', 'Few-shot prompting with LLMs.', 'flowchart TD\n  A[Prompt Context] --> B[LLM]\n  B --> C[Question Generation]'),
    ('The Verifiable Self-Play & Alignment Era', 'verifiable-self-play.md', 'RLVR and verifiers.', 'flowchart TD\n  A[LLM Generator] --> B[Sandboxed Verifier]\n  B -->|Pass| C[Dataset]\n  B -->|Fail| A'),
    ('Factoid Question Generation', 'factoid-qg.md', 'Low-level retrieval.', 'flowchart TD\n  A[Text] --> B[NER Extraction]\n  B --> C[Question Template]'),
    ('Deep Cognitive QG', 'deep-cognitive-qg.md', 'High-order logic and reasoning.', 'flowchart TD\n  A[Text] --> B[Macro Theme Analysis]\n  B --> C[CoT Generation]\n  C --> D[Deep Question]'),
    ('Answer-Conditioned vs. Agnostic', 'answer-conditioned-agnostic.md', 'Providing vs not providing target answer.', 'flowchart TD\n  A[Text] --> B{Answer Provided?}\n  B -->|Yes| C[Answer-Conditioned QG]\n  B -->|No| D[Answer-Agnostic QG]'),
    ('Visual Question Generation (VQG)', 'visual-qg.md', 'Cross-modal image to question.', 'flowchart TD\n  A[Image] --> B[Visual Encoder]\n  B --> C[VLM]\n  C --> D[Visual Question]'),
    ('Process-Supervised Step Auditors (PRMs)', 'process-supervised-prms.md', 'Step-by-step verification.', 'flowchart TD\n  A[Step 1] --> B[PRM Score]\n  B --> C[Step 2]\n  C --> D[PRM Score]'),
    ('Vector Database Deduplication Blocks', 'vector-deduplication.md', 'Semantic similarity search to prune duplicates.', 'flowchart TD\n  A[New Question] --> B[Dense Encoder]\n  B --> C[Vector DB Search]\n  C -->|Sim > Threshold| D[Discard]\n  C -->|Sim < Threshold| E[Keep]'),
    ('The Hallucination Cascade', 'hallucination-cascade.md', 'Model collapse due to synthetic errors.', 'flowchart TD\n  A[LLM Output] --> B[RAG Check]\n  B -->|Verified| C[Safe Data]\n  B -->|Hallucination| D[Reject]'),
    ('The Distributed Context Padding', 'distributed-context-padding.md', 'Imbalance in GPU clusters.', 'flowchart TD\n  A[Context Blocks] --> B[Length Sorter]\n  B --> C[GPU Buckets]'),
    ('Automated Educational Assessment', 'educational-assessment.md', 'Adaptive learning systems.', 'flowchart TD\n  A[Student Profile] --> B[AQG System]\n  B --> C[Tailored Quiz]'),
    ('Web-Scale Synthetic Datasets', 'synthetic-datasets.md', 'Self-instruct LLM training.', 'flowchart TD\n  A[Seed Prompts] --> B[LLM Expansion]\n  B --> C[Verification]\n  C --> D[Synthetic Dataset]'),
    ('Enterprise Knowledge Auditing', 'enterprise-auditing.md', 'Stress-testing RAG pipelines.', 'flowchart TD\n  A[Corporate Docs] --> B[AQG Module]\n  B --> C[Synthetic Queries]\n  C --> D[RAG Eval]'),
]

for title, filename, desc, diagram in items:
    content = f'''# {title}\n\n{desc}\n\n## Diagram\n```mermaid\n{diagram}\n```\n\n[Back to README](../README.md)\n'''
    with open(os.path.join('pages', filename), 'w', encoding='utf-8') as f:
        f.write(content)

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

for title, filename, _, _ in items:
    text = text.replace(f'**{title}**', f'**[{title}](pages/{filename})**')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
