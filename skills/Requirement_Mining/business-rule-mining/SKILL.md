---
name: business-rule-mining
description: "Stack-neutral enterprise legacy modernization skill: Business Rule Mining. Conditional applicability."
---

# Business Rule Mining

## Purpose
Perform **Business Rule Mining** as one reusable capability of enterprise application discovery, migration, and validation. Do not assume the legacy language, application domain, destination runtime, or architecture.

## Applicability
Activate only when this capability helps address a discovered requirement or an explicit user objective.
Do not treat the skill name as proof that this technology exists in the current project. For technology-specific skills, mark **not applicable** when the selected stack differs, and choose an equivalent skill or tool instead.

**Mandatory shared discovery artifact:** Capture relevant data definitions, file layouts, interfaces, contracts, source mappings and evidence in `docs/current-state/data-structure-and-interface-analysis.md` (DSI-01) before target code generation. Mark irrelevant subareas N/A with source justification; update findings during modernization.

## Execution
1. Read `AGENTS.md`, `golden template/AZURE_MODERNIZATION_GOLDEN_TEMPLATE.md` (authoritative embedded JSON User Architecture Contract), `docs/discovery/technology-inventory.md`, and the applicable project acceptance criteria. Verify inputs against real workspace files.
2. Identify the specific source files, dependencies, business rules, interfaces, and runtime behavior relevant to **Business Rule Mining**. Include source file/line references where available.
3. Determine whether this capability applies to the selected source and target stack; if not, document `N/A` and stop this skill cleanly.
4. Create an incremental, reversible, source-traceable change. Preserve observable behavior, data precision, security constraints, and interface contracts unless a change has been explicitly approved.
5. Generate appropriate documentation and tests in the target stack, preferring established framework conventions over imposed patterns.
6. Execute available build, static checks and tests. Record command, exit code, and evidence. If environment or dependencies prevent execution, mark `NOT RUN`; never report simulated success.
7. Update the source-to-target traceability map, assumptions/risks, and completion evidence.

## Guardrails
- `legacy-source-app/` is read-only. Generated results belong in `modernization-output/` or `docs/`.
- No invented business rules, endpoints, schemas, credentials, passing tests, or quality metrics.
- No mandatory DDD, CQRS, microservices, REST, React, .NET, or a specific cloud resource absent evidence and architectural approval.
- Non-applicable specialized skills must not change the implementation.
- For Azure-targeted deployment, apply `Rules/azure-deployment.md` and choose services based on actual workload characteristics.

## Expected output
Files changed; source references; decisions and tradeoffs; test/build/security results; open gaps; updated traceability.
