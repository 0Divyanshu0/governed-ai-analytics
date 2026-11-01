# Build roadmap

## Phase 0 — bootstrap
- [x] Name, purpose, non-proprietary boundary
- [x] FastAPI shell and checks
- [x] Basic CI and documentation

## Phase 1 — synthetic dataset and semantics
- [ ] PostgreSQL Docker Compose service with synthetic commerce tables
- [ ] Curated domain, relation, column, relationship and metric definitions
- [ ] Explicit data grain and freshness fields
- [ ] Migration mechanism and read-only role

## Phase 2 — safe question answering
- [ ] Model adapter and structured query-plan output
- [ ] Scoped catalog retrieval
- [ ] Complete AST validator, role-based relation/column controls
- [ ] Deterministic read-only executor, query timeout and row/byte limits
- [ ] Grounded response with SQL/query provenance

## Phase 3 — evaluations
- [ ] Gold-question dataset and query correctness tests
- [ ] Negative tests for unauthorized columns, invalid joins, injection, ambiguous metrics
- [ ] Latency, cost and failure metrics without sensitive logging

## Phase 4 — product UX
- [ ] React/TypeScript conversational interface
- [ ] Explain SQL and source metric definitions
- [ ] Visual summaries and shareable demo
- [ ] Optional multi-step planner with bounded tools
