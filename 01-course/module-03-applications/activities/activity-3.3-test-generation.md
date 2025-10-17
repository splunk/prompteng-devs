# Activity 3.3: Build Your Own Test Generation Template

**⏱️ Time Required:** 30-40 minutes  
**🎯 Difficulty:** Intermediate  
**📚 Prerequisites:** Complete Section 2 of `3.3-test-generation-automation.ipynb`

---

## 🎯 Your Mission

Build a production-ready **command-style** test generation prompt template that analyzes requirements, spots ambiguities, and produces reusable specs for an e-commerce discount system. You will research, design, and assemble the four building blocks—`<command_summary>`, `<system_inputs>`, `<reasoning_checklist>`, and `<output_contract>`—so the model delivers consistent, automation-friendly test plans.

---

## 📋 Success Criteria

Your finished template should:
- ✅ Capture intent, success signals, and consumers inside `<command_summary>`
- ✅ Bundle all context (project overview, functional requirements, existing tests) inside `<system_inputs>`
- ✅ Force deliberate thinking about coverage gaps via `<reasoning_checklist>`
- ✅ Emit a predictable test specification inside `<output_contract>`
- ✅ Separate unit vs integration tests and call out infrastructure needs

---

## 🔍 Scenario Snapshot

You are supporting a shopping cart discount system with intentionally vague requirements:
- Users can apply discount codes (percentage or fixed amount)
- Codes have expiration dates and usage limits
- Cart total must stay positive after discounts
- Business rule: only one discount per order

Your template must highlight unclear requirements, invent edge cases, and document the tests your QA team needs.

---

## 📝 Working Plan

### Step 1 — Research the Pattern (10-15 minutes)
1. Read the [AWS Anthropic Test Generation Command](https://github.com/aws-samples/anthropic-on-aws/blob/main/advanced-claude-code-patterns/commands/generate-tests.md).
2. Note how they phrase the command summary, organize inputs, guide reasoning, and structure the output.

Use the space below for quick notes:
```
Command summary ingredients:
- 

Inputs to carry over:
- 

Reasoning checklist prompts I like:
- 

Output elements worth keeping:
- 
```

### Step 2 — Blueprint Your Command Template (10-15 minutes)
Answer these prompts before editing the template:
```
Command summary focus (mission, consumers, success signals):
- 

System inputs to include (project context, requirements, coverage snapshot):
- 

Reasoning checklist questions that surface gaps:
1. 
2. 
3. 
4. 

Output contract sections and formatting rules:
- 

Reusable {{variables}} I plan to support:
- 
```
> Tip: Tune the four tags to match the test case you are targeting. Updating the command summary, inputs, checklist, and output contract is the fastest way to adapt the template to a new feature.

### Step 3 — Build & Test (15-20 minutes)
1. Scroll to the editable template block below.
2. Modify only the content between `<!-- TEMPLATE START -->` and `<!-- TEMPLATE END -->`.
3. Replace the TODO comments with your command summary, system inputs, reasoning checklist, and output contract.
4. Keep the XML shell, `{{variables}}`, and HTML comments so the testing helper can extract your work.
5. Save the file and run `test_activity_3_3()` in the notebook when you are ready.

✅ **Do:** update the four tags to optimise the prompt for the discount system (or any feature you target).  
❌ **Don’t:** remove the XML tags, change the code fence, or delete the comment markers—those are required for automated testing.

<details>
<summary>❓ Why keep the HTML comment markers?</summary>

The `<!-- TEMPLATE START -->` and `<!-- TEMPLATE END -->` markers tell the `test_activity_3_3()` helper exactly where your template begins and ends. They disappear in rendered Markdown but are essential for automation.

</details>

---

## 👇 YOUR EDITABLE TEMPLATE IS BELOW 👇

```xml
/*******************************************************************************
 *  ✏️  EDIT YOUR TEMPLATE BETWEEN THE COMMENT BLOCKS
 *  
 *  The test function extracts everything between:
 *  <!-- TEMPLATE START --> and <!-- TEMPLATE END -->
 *  
 *  Instructions:
 *  1. Replace TODO comments with your content
 *  2. Focus on coverage gaps, ambiguity detection, and reusable output
 *  3. Keep the four command sections intact
 *  4. Use {{variables}} for parameterisation
 ******************************************************************************/

<!-- TEMPLATE START -->
<command_summary>
<!-- TODO: Summarise the mission, consumers, and success signals for this test plan. -->
Command: TODO - Replace with when and why the team runs this command.
Primary Objective: TODO - Define the goal for coverage or decision-making.
Success Signals:
- TODO - What confirms coverage is sufficient?
- TODO - What ambiguities must be surfaced?
- TODO - How should output stay automation-ready?
</command_summary>

<system_inputs>
<!-- TODO: Bundle every piece of context the model needs to read once. -->
<ProjectOverview>
<!-- EDITING NOT REQUIRED: these project context fields are provided by the function call variables -->
{{project_context}}
</ProjectOverview>
<FunctionalRequirements>
<!-- EDITING NOT REQUIRED: these functional requirement fields are provided by the function call variables -->
{{functional_requirements}}
</FunctionalRequirements>
<ExistingTests>
<!-- EDITING NOT REQUIRED: these existing test fields are provided by the function call variables -->
{{existing_tests}}
</ExistingTests>
</system_inputs>

<reasoning_checklist>
<!-- TODO: Guide the model through deliberate analysis before it writes specs. -->
1. TODO - Anchor context in one or two bullets.
2. TODO - Compare requirements to existing tests and log risk themes.
3. TODO - Capture ambiguities or missing business rules that block automation.
4. TODO - Expand uncovered scenarios into test specs (unit/integration) with setup, steps, and expected results before drafting the final answer.
</reasoning_checklist>

<output_contract>
<!-- TODO: Define the exact Markdown layout for the test plan. -->
## Summary
- [Product goal]
- [High-risk areas or notable gaps]

## Ambiguities & Follow-ups
- **Question:** [Open question]
  **Why it matters:** [Impact if unanswered]
  **Assumption (if unclarified):** [Temporary assumption]

## Coverage Map
| Theme | Risk Level | Missing Scenario |
| --- | --- | --- |

## Unit Tests
### Test: [Name]
**Goal:** [Purpose]
**Setup:** [Data, mocks]
**Steps:**
1. ...
2. ...
**Expected:** [...]
**Priority:** [P0/P1/P2]

## Integration Tests
### Test: [Name]
**Goal:** [Purpose]
**Setup:** [Services, data]
**Steps:**
1. ...
2. ...
**Expected:** [...]
**Priority:** [P0/P1/P2]

## Test Data & Tooling
- Mocks/Stubs: [...]
- Fixtures: [...]
- Environments: [...]
</output_contract>
<!-- TEMPLATE END -->

/*******************************************************************************
 *  YOUR TEMPLATE ENDS HERE
 *  
 *  Next step: Test it!
 *  Go to: 3.3-test-generation-automation.ipynb
 *  Run: test_activity_3_3(test_code="...", variables={...})
 ******************************************************************************/
```

---

### Step 4 — Test Your Template

**🧪 Try it in the notebook:**

Open `3.3-test-generation-automation.ipynb` and run:

```python
# Shopping Cart Discount System requirements (intentionally vague!)
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

test_activity_3_3(
    test_code=discount_requirements,
    variables={
        'project_context': project_context,
        'functional_requirements': discount_requirements,
        'existing_tests': existing_tests
    }
)
```

**Your template's output:**
<!-- TEST RESULT -->
```
[Results will be automatically saved here when you test]
```
<!-- TEST RESULT END -->

**Self-Check:**
- [ ] Did `<command_summary>` make the mission and success signals explicit?
- [ ] Did `<system_inputs>` capture everything the model needs in one scan?
- [ ] Did `<reasoning_checklist>` surface ambiguities and risk themes?
- [ ] Did `<output_contract>` separate unit vs integration tests with full specs?
- [ ] Did you call out infrastructure needs and priorities?

---

## 🧪 Extra Experiments

After your first run, iterate:
- Swap in a new `{{project_context}}` for a different domain (e.g., SaaS billing).
- Feed altered requirements (e.g., stackable discounts) and confirm ambiguities change.
- Trim success signals to see how the output shifts, then refine them.

---

## ✅ Completion Checklist

- [ ] Template highlights intent, inputs, reasoning, and deliverables clearly
- [ ] Ambiguities and coverage gaps are called out before test specs
- [ ] Unit and integration tests are separated with reusable formatting
- [ ] Test infrastructure needs are listed (mocks, data, environments)
- [ ] Template uses `{{variables}}` for easy reuse
- [ ] Tested with the helper function and reviewed the output

---

## 🚀 Next Steps

- Compare with the reference solution: [`solutions/activity-3.3-test-generation-solution.md`](../solutions/activity-3.3-test-generation-solution.md)
- Reflect on what you learned:
```
1. 
2. 
3. 
```
- Ready for more? Continue to `3.4-llm-as-judge-evaluation.ipynb` for model-based evaluation patterns.

---

## 💡 Need Help?

Drop a note in your team's channel or revisit the AWS pattern for inspiration. Small tweaks to the four tags go a long way—focus on clarity over volume.
