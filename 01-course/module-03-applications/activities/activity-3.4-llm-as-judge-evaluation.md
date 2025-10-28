# Activity 3.4: Create an LLM-as-Judge Evaluation Template

**⏱️ Time Required:** 30-40 minutes  
**🎯 Difficulty:** Advanced  
**📚 Prerequisites:** Complete Sections 3.2–3.4

---

## 🎯 Your Mission

Create an automated judge template that evaluates AI-generated refactored code against a weighted rubric. Your template will assess correctness, design quality, safety, and test coverage—then output an **Accept / Revise / Block** verdict that a pipeline can act on.

## 📋 What You'll Build

A judge template that:
- ✅ Scores **4 weighted criteria**: correctness (35%), design quality (25%), safety/performance (20%), test coverage (20%)
- ✅ Forces the LLM to provide rationale before scoring
- ✅ Calculates a weighted total and recommends **Accept / Revise / Block**
- ✅ Returns a structured report your pipeline can parse

## 🔍 The Scenario

An AI assistant refactored a cache helper function. Your judge must evaluate whether:
- The refactored code preserves the original behaviour (cache hits/misses/writes stats must remain identical)
- Design improved (eviction logic extracted cleanly into a helper function)
- No safety issues introduced (eviction threshold guards remain intact)
- Tests exist or are proposed for the changes

**Your judge template will be tested with this scenario in the notebook.**

## 📝 How to Complete This Activity

### Step 1: Edit the Template Below (20-25 minutes)

1. Scroll down to **"Your Editable Judge Template"**
2. Replace all `TODO` comments between `<!-- TEMPLATE START -->` and `<!-- TEMPLATE END -->`
3. Define what scores 5, 3, and 1 mean for each criterion
4. Specify failure triggers and escalation conditions
5. Keep all `{{variable}}` placeholders—they'll be filled in when testing

**Key template sections to complete:**
- **Judge Profile**: Define the role and focus areas
- **Rubric**: Fill in score guides (5/3/1) for all 4 criteria
- **Scoring Protocol**: Describe the evaluation steps
- **Decision Rules**: Map weighted scores to Accept/Revise/Block
- **Report Format**: Structure the output

### Step 2: Test Your Template (10-15 minutes)

1. Open `3.4-llm-as-judge-evaluation.ipynb`
2. Run the **"Test Your Judge Template"** cell with `test_activity_3_4(variables=get_refactor_judge_scenario())`
3. Review the judge's verdict for the cache refactor scenario
4. Iterate: If scores don't match expectations, refine your template and re-run

**Testing tip:** The `test_activity_3_4()` function uses `get_refactor_judge_scenario()` to provide a complete cache refactor scenario—you just need to complete your template.

**💡 Optional: Use a different model for judging**

To avoid the AI model judging its own output (which can lead to bias), you can switch to a different provider/model for evaluation. Add this to your notebook test cell:

```python
import setup_utils

# Switch to a different provider for judging
original_provider = setup_utils.PROVIDER
try:
    setup_utils.PROVIDER = 'openai'  # or 'claude' if you were using 'openai'
    judge_preview = test_activity_3_4(variables=get_refactor_judge_scenario())
finally:
    setup_utils.PROVIDER = original_provider  # restore original
```

This ensures the judge evaluates independently from the model that generated the refactor.

---

## 👇 Your Editable Judge Template 👇

````xml
/*******************************************************************************
 *  ✏️  EDIT YOUR TEMPLATE BETWEEN THE COMMENT BLOCKS
 *  
 *  The test function extracts everything between:
 *  <!-- TEMPLATE START --> and <!-- TEMPLATE END -->
 *  
 *  Instructions:
 *  1. Preserve the XML structure for automated extraction
 *  2. Replace `TODO` comments with your content
 *  3. Define clear score guides: what does 5, 3, and 1 mean for each criterion?
 *  4. Keep `{{variable}}` placeholders—they'll be substituted when testing
 ******************************************************************************/
<!-- TEMPLATE START -->
<judge_profile>
Role: TODO — Define your judge's role (e.g., "Principal Refactoring Engineer for {{service_name}}")
FocusAreas:
- TODO — What behaviour must be preserved? (e.g., cache stats, side effects)
- TODO — What design patterns to enforce? (e.g., single responsibility, clear naming)
- TODO — What observability to protect? (e.g., logging, metrics)
</judge_profile>

<evaluation_context>
<artifact_brief>
{{refactor_brief}}
</artifact_brief>
<pre_refactor_snippet>
{{code_before}}
</pre_refactor_snippet>
<post_refactor_snippet>
{{code_after}}
</post_refactor_snippet>
<refactor_metadata>
CommandIntent: {{refactor_goal}}
TestStatus: {{test_summary}}
StaticAnalysis: {{analysis_findings}}
</refactor_metadata>
</evaluation_context>

<rubric>
<criterion id="correctness" weight="0.35">
Goal: Verify behaviour parity and backward compatibility.
ScoreGuide:
- 5 → TODO — What indicates perfect preservation? (e.g., counters match, tests confirm parity)
- 3 → TODO — What's acceptable risk? (e.g., minor logging reordered, fixable)
- 1 → TODO — What's a failure? (e.g., stats dropped, contract broken)
FailureTriggers:
- TODO — When should you immediately BLOCK? (check {{critical_regression}})
</criterion>

<criterion id="design_quality" weight="0.25">
Goal: Confirm the refactor improves structure and readability.
ScoreGuide:
- 5 → TODO — What's excellent design? (e.g., helper extracted, names clear)
- 3 → TODO — What's adequate? (e.g., some improvement, debt remains)
- 1 → TODO — What's poor? (e.g., added complexity, unclear intent)
Checklist:
- TODO — Design rules to enforce (e.g., single responsibility, docstrings)
</criterion>

<criterion id="safety_performance" weight="0.20">
Goal: Assess security, resource usage, and failure handling.
ScoreGuide:
- 5 → TODO — Safe and efficient? (e.g., bounds enforced, no blocking calls)
- 3 → TODO — Minor gap? (e.g., slight inefficiency, log missing)
- 1 → TODO — Dangerous? (e.g., unbounded growth, removed guards)
RedFlags:
- TODO — When to escalate? (check {{security_findings}})
</criterion>

<criterion id="test_strategy" weight="0.20">
Goal: Ensure regression tests exist or new coverage is proposed.
ScoreGuide:
- 5 → TODO — Strong coverage? (e.g., tests named, gaps addressed)
- 3 → TODO — Acknowledged gaps? (e.g., plan vague but mentioned)
- 1 → TODO — No coverage? (e.g., claims unnecessary or omits tests)
EscalateIf:
- TODO — When do missing tests force escalation?
</criterion>
</rubric>

<scoring_protocol>
1. TODO — How to compare code? (e.g., line-by-line diff, check counters/side effects)
2. TODO — What to cross-check? (e.g., {{refactor_goal}}, {{test_summary}}, {{analysis_findings}})
3. TODO — How to score? (e.g., assign scores with evidence, compute weighted total)
4. TODO — When to provide guidance? (e.g., score ≤ 3 or triggers fire)
</scoring_protocol>

<decision_rules>
- Accept → TODO — When is it safe? (e.g., weighted_total ≥ ?, no triggers)
- Revise → TODO — Fixable issues? (e.g., ? ≤ weighted_total < ?, what needs work)
- Block → TODO — Unacceptable? (e.g., weighted_total < ? or triggers fire)
- TODO — Remind: cite specific lines, tests, or evidence
</decision_rules>

<report_format>
## Judge Summary
- Verdict: TODO — How to show Accept/Revise/Block?
- Weighted total: TODO — Format (e.g., X.X/5.0)?
- Key signals: TODO — What to highlight? (counters, tests, etc.)

## Score Breakdown
| Criterion | Weight | Score (1-5) | Evidence | Adjustments |
| --- | --- | --- | --- | --- |
TODO — One row per criterion with rationale

## Required Actions
- Owner: TODO — Who fixes this?
- Task: TODO — What to do?
- Why: TODO — What's the risk?
- Due: TODO — When or trigger?

## Escalation Log
- Triggered?: TODO — Yes/No format?
- Channel: {{escalation_channel}}
- Notes: TODO — What context to include?
</report_format>
<!-- TEMPLATE END -->
/*******************************************************************************
 *  YOUR TEMPLATE ENDS HERE
 *  
 *  Next step: Test it!
 *  Go to: 3.4-llm-as-judge-evaluation.ipynb
 *  Run: test_activity_3_4(variables=get_refactor_judge_scenario())
 ******************************************************************************/
````

---

## 🧪 Test Your Template in the Notebook

Once you've filled in the template above:

1. Open `3.4-llm-as-judge-evaluation.ipynb`
2. Navigate to the cell with `test_activity_3_4(variables=get_refactor_judge_scenario())`
3. Run the cell to evaluate a sample refactor with your judge
4. Review the output—does it match your expectations?
5. Return here to refine your template if needed

**What `get_refactor_judge_scenario()` provides:**
- Complete cache refactor scenario (code_before, code_after)
- AI-generated refactor rationale and analysis
- Test results, static analysis findings, and metadata
- All `{{variables}}` automatically filled in for you

---

## 🔄 Reflection Questions

After testing your template:

- Did your judge catch the critical regression (eviction stats missing)?
- Which criterion needed the most calibration to get accurate scores?
- What threshold works best for Accept vs. Revise vs. Block?
- How would you integrate this into your CI/CD pipeline?

---

## 📚 Next Steps

- **Compare solutions**: Review `solutions/activity-3.4-llm-as-judge-evaluation-solution.md` for the reference implementation
- **Build an eval dataset**: Collect 10-20 refactors with known good/bad patterns to test your judge
- **Try platform evals**: Use OpenAI Dashboard or Anthropic Console to run systematic evaluations
- **Iterate & measure**: Track judge performance over time—adjust weights/thresholds based on metrics, not intuition
