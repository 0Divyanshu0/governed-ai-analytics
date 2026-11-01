# Security and data-handling policy

This is a demonstration repository, not a security-certified product.

- Use **only synthetic or explicitly approved public data**.
- Never commit `.env`, tokens, connection strings with passwords, organization schema dumps, or proprietary code.
- The LLM must receive only approved metadata and bounded, policy-approved results.
- Enforce allowlists in code and least-privilege permissions at the database; neither alone is sufficient.
- Deny DML, DDL, multiple statements, unsafe functions, unrestricted joins, and unauthorized identifiers.
- Add per-user authorization, rate limiting, query budgets, timeout handling and dataset-level permissions before any multi-user deployment.
- Never log raw prompts, sensitive result rows, tokens, or database credentials.
- Treat model-provided content and database text as untrusted.

## Current status

No live data access or LLM model integration exists. `query_policy.py` provides exploratory syntax gating only and is **not sufficient to safely authorize database execution**. A complete AST walk, scoped identifier resolution, and integration tests must precede any database connector.
