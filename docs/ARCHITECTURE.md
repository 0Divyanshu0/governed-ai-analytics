# Architecture (proposed)

## Design constraints

1. The LLM never has database credentials or direct database connectivity.
2. Backend policy is authoritative; prompts are not security controls.
3. Every business metric must have approved grain, filters, and definition.
4. Join paths require verified semantic relationships.
5. A request sees only relevant approved schema metadata.
6. SQL queries use a dedicated read-only database role, transaction timeouts, bounded result sizes and audit-safe logs.
7. Undefined or ambiguous questions should be declined or clarified, not guessed.

## Components

- **API/router:** validates requests and chooses the workflow.
- **Semantic catalog:** domain, entity, column, relationship, metric and policy metadata; versioned changes.
- **Planner:** LLM adapter producing a proposed query only.
- **Policy engine:** independently parses and validates query AST, against a question-scoped allowlist.
- **Executor:** parameterized, read-only database transactions with server-side resource limits.
- **Answer composer:** reports computed results with provenance, limitations, and exact metric definitions.
- **Evaluation harness:** fixtures for correct queries, invalid joins, sensitive fields, unknown metrics, prompt injection and timeouts.

## Data flow

Synthetic dataset -> restricted role / approved schema -> semantic context -> LLM proposal -> policy validation -> read-only execution -> bounded result -> grounded answer.

## Current status

Only a FastAPI shell and prototype policy checks are implemented. The SQL policy is deliberately incomplete and must not be treated as a production security boundary. There are no database or LLM calls in Phase 0.
