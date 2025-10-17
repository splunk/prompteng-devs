# Activity 3.3 Solution: Test Generation for E-Commerce

**⏱️ Completion Time:** Reference solution  
**🎯 Focus:** Command-style coverage planning, ambiguity detection, reusable specs  
**📚 Ready to Test:** Use `test_activity_3_3_solution()` with this file path

---

## 🎯 Complete Working Solution

This reference solution delivers a production-ready test generation command composed of four sections: `<command_summary>`, `<system_inputs>`, `<reasoning_checklist>`, and `<output_contract>`. It follows the AWS pattern while tailoring success signals, inputs, and output structure for the shopping cart discount system.

### How to Test This Solution

```python
# In 3.3-test-generation-automation.ipynb
from setup_utils import test_activity

discount_requirements = """
Feature: Shopping Cart Discount System

Requirements:
1. Users can apply discount codes at checkout
2. Discount types: percentage (10%, 25%, etc.) or fixed amount ($5, $20, etc.)
3. Each discount code has an expiration date
4. Usage limits: one-time use OR unlimited
5. Business rule: Discounts cannot be combined (one per order)
6. Cart total must be > 0 after discount applied
7. Fixed discounts cannot exceed cart total
"""

existing_tests = """
Current test suite (minimal coverage):
- test_apply_percentage_discount() - 10% off $100 cart
- test_fixed_amount_discount() - $5 off $50 cart
"""

project_context = """
Domain: E-commerce platform
Project: Shopping Cart Discount Service
Primary test framework: pytest
Tech stack: Python/Flask
"""

test_activity(
    'solutions/activity-3.3-test-generation-solution.md',
    test_code=discount_requirements,
    variables={
        'project_context': project_context,
        'functional_requirements': discount_requirements,
        'existing_tests': existing_tests
    }
)
```

---

## 👇 COMPLETE WORKING TEMPLATE BELOW 👇

```xml
/*******************************************************************************
 *  SOLUTION TEMPLATE FOR ACTIVITY 3.3
 *  
 *  This command-style template:
 *  - Sets intent and success signals in <command_summary>
 *  - Packages all context in <system_inputs>
 *  - Forces deliberate analysis via <reasoning_checklist>
 *  - Produces automation-ready specs in <output_contract>
 ******************************************************************************/

<!-- TEMPLATE START -->
<command_summary>
Command: Generate a coverage-first test plan for the Shopping Cart Discount Service before sprint planning.
Primary Objective: Expose untested scenarios, ambiguities, and infrastructure needs so QA can prioritise automation work.
Success Signals:
- Every critical flow (happy path, edge case, error path) has at least one unit or integration test candidate with priority.
- Ambiguities and policy questions are captured with temporary assumptions and follow-up owners.
- Output remains markdown with summary, coverage map, separated test specs, and infrastructure checklist to drop into QA tooling.
</command_summary>

<system_inputs>
<ProjectOverview>
{{project_context}}
</ProjectOverview>
<FunctionalRequirements>
{{functional_requirements}}
</FunctionalRequirements>
<ExistingTests>
{{existing_tests}}
</ExistingTests>
</system_inputs>

<reasoning_checklist>
1. Summarise the product slice in two bullets (business goal + technical scope) to anchor the test strategy.
2. Compare each requirement against the existing tests and label risk themes (happy path, boundary, error handling, policy, security).
3. Record ambiguities, unstated rules, or data dependencies that could block automation; assign provisional assumptions if clarification is pending.
4. For every uncovered scenario, outline a test specification (unit or integration) including setup, steps, expected result, and priority before drafting the final markdown output.
5. Note any infrastructure, data, or tooling gaps (mocks, fixtures, clock control) needed to implement the plan.
</reasoning_checklist>

<output_contract>
## Summary
- Product goal: [One-sentence mission]
- High-risk areas: [Top 2-3 risk themes surfaced]

## Ambiguities & Follow-ups
- **Question:** [What's unclear?]
  **Why it matters:** [Potential impact]
  **Owner / Next step:** [Who clarifies]
  **Assumption (until resolved):** [Working assumption]

## Coverage Map
| Theme | Risk Level | Missing Scenario | Notes |
| --- | --- | --- | --- |

## Unit Tests
### Test: [Descriptive name]
**Goal:** [Behaviour or rule validated]
**Setup:** [Data, fixtures, mocks]
**Steps:**
1. ...
2. ...
**Expected:** [...]
**Priority:** [P0/P1/P2]
**Why it matters:** [Business/tech impact]

[Repeat subsection for each unit test]

## Integration Tests
### Test: [Descriptive name]
**Goal:** [Workflow validated]
**Setup:** [Services, data, sequencing]
**Steps:**
1. ...
2. ...
**Expected:** [...]
**Priority:** [P0/P1/P2]
**Why it matters:** [Business/tech impact]

[Repeat subsection for each integration test]

## Test Data & Tooling
- Mocks/Stubs: [Payment gateway, clock, notification service, etc.]
- Fixtures: [Discount codes by status, carts at boundary totals, user segments]
- Environments: [Local, staging, feature flags]
- Observability: [Logs/metrics needed for validation]

## Implementation Roadmap
- P0 (Critical): [Tests to ship first]
- P1 (High): [Next wave]
- P2 (Medium): [Follow-up scenarios]

## Success Checklist
- [ ] P0 coverage implemented and passing
- [ ] Ambiguities resolved or tracked
- [ ] Test data & tooling available in CI
- [ ] Regression criteria documented
</output_contract>
<!-- TEMPLATE END -->

/*******************************************************************************
 *  SOLUTION TEMPLATE ENDS HERE
 ******************************************************************************/
```

---

## ✅ Why This Solution Works

- **Clear Intent:** `<command_summary>` states when to use the template, what success looks like, and who consumes the output.
- **Single-Pass Inputs:** `<system_inputs>` groups project overview, requirements, and existing tests so the model never loses context.
- **Deliberate Reasoning:** `<reasoning_checklist>` pushes the model to analyse before writing specs, mirroring risk reviews in real teams.
- **Automation-Ready Output:** `<output_contract>` mirrors the markdown structure used in the notebooks and CI tooling (summary, ambiguities, coverage map, test specs, infrastructure, roadmap).
- **Prioritisation:** Including a roadmap and success checklist helps teams plan implementation effort, not just enumerate tests.

Use this file to benchmark your own template, then iterate to match your team's domain or tooling needs.
