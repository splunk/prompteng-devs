# Activity 3.4 Solution: LLM-as-Judge Evaluation Template

**⏱️ Completion Time:** 30-40 minutes (reference implementation)  
**🎯 Focus:** Evaluating AI-generated refactored code with a weighted rubric  
**📚 Ready to Test:** Use `test_activity_3_4_solution(variables=get_refactor_judge_scenario())` from `setup_utils`

---

## 🎯 Solution Overview

This solution demonstrates a complete judge template that evaluates AI refactors against 4 weighted criteria:
- **Correctness (35%)**: Behaviour parity and backward compatibility
- **Design Quality (25%)**: Structure and readability improvements
- **Safety/Performance (20%)**: Security, resource usage, failure handling
- **Test Strategy (20%)**: Regression tests and coverage

The judge outputs an **Accept / Revise / Block** verdict based on weighted scoring.

### How to Test This Solution

```python
# In 3.4-llm-as-judge-evaluation.ipynb
from setup_utils import test_activity_3_4_solution, get_refactor_judge_scenario

# Test with the provided scenario
judge_response = test_activity_3_4_solution(variables=get_refactor_judge_scenario())
print(judge_response)
```

**What the test does:**
- Loads the solution template from this file
- Applies it to a cache refactor scenario (code_before, code_after, AI rationale)
- Returns the judge's verdict with scores and recommendation

> Tip: Compare this solution with your own template to see different approaches to defining score guides and decision thresholds.

---

## 💡 Key Design Decisions

### Weighted Criteria (Totals 100%)
- **Correctness (35%)**: Highest weight—behaviour regressions are unacceptable
- **Design Quality (25%)**: Second priority—refactors should improve, not complicate
- **Safety/Performance (20%)**: Protect resource usage and security invariants
- **Test Strategy (20%)**: Coverage gaps must be acknowledged and addressed

### Score Scale (1-5)
- **5**: Exceeds expectations with clear evidence
- **3**: Meets minimum bar, minor fixable issues
- **1**: Fails to meet standards, serious gaps

### Decision Thresholds
- **Accept**: weighted_total ≥ 3.6 and no hard failures
- **Revise**: 2.8 ≤ weighted_total < 3.6 or single criterion ≤ 2
- **Block**: weighted_total < 2.8 or any hard trigger fires

### Failure Triggers
- Critical regression detected (from metadata)
- Stats counters altered or removed
- Security findings present
- Behaviour changes without test coverage

---

## 👇 COMPLETE JUDGE TEMPLATE 👇

````xml
/*******************************************************************************
 *  SOLUTION TEMPLATE FOR ACTIVITY 3.4
 *  
 *  Judges AI-generated refactors of the cache session helper before merge.
 *  Focus: behaviour parity, design quality, safety/performance, test strategy.
 ******************************************************************************/

<!-- TEMPLATE START -->
<judge_profile>
Role: Principal Refactoring Engineer for {{service_name}} platform services
FocusAreas:
- Guard cache invariants (hits/misses/writes, eviction thresholds, lazy load semantics)
- Enforce modular design: single-responsibility helpers, descriptive naming, docstrings
- Preserve observability hooks: structured logging, metrics, and PagerDuty annotations
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
- 5 → Counters, eviction triggers, and side effects match original behaviour; regressions ruled out with evidence/tests.
- 3 → Minor risk noted (e.g., logging reordered) with clear fix or mitigation.
- 1 → Behavioural regression, missing counter update, or altered contract detected.
 FailureTriggers:
- Block immediately if {{critical_regression}} is present or eviction stats/logging are removed.
</criterion>

<criterion id="design_quality" weight="0.25">
Goal: Confirm the refactor improves structure and readability.
ScoreGuide:
- 5 → Helper extraction reduces duplication, names clarify intent, docstrings explain policy.
- 3 → Some structure improved but leftover duplication or naming debt persists.
- 1 → New complexity, nested branching, or unclear helper responsibilities.
Checklist:
- Reference the refactor style guide (single exit points, helper docstrings, typing updates).
</criterion>

<criterion id="safety_performance" weight="0.20">
Goal: Assess security, resource usage, and failure handling.
ScoreGuide:
- 5 → No new blocking calls; eviction helper enforces capacity limits and error paths.
- 3 → Slight inefficiency or missing instrumentation but no severe risk.
- 1 → Removes safeguards, introduces unbounded growth, or weakens error handling.
RedFlags:
- Escalate if {{security_findings}} include leaked secrets or if retry/backoff logic disappears.
</criterion>

<criterion id="test_strategy" weight="0.20">
Goal: Ensure regression tests exist or new coverage is proposed.
ScoreGuide:
- 5 → Names specific unit/integration tests and outlines contract coverage.
- 3 → Acknowledges gaps but leaves ownership or timing vague.
- 1 → Claims tests are unnecessary or omits mitigation entirely.
EscalateIf:
- Trigger escalation when behaviour shifts without a committed test or alert update.
</criterion>
</rubric>

<scoring_protocol>
1. Compare pre/post code line-by-line; list any changed side effects or counters.
2. Cross-check findings against {{refactor_goal}}, {{test_summary}}, and {{analysis_findings}}; note mismatches.
3. Assign criterion scores with bullet evidence, compute weighted_total, and note triggered Failure/RedFlag conditions.
4. Document improvement guidance whenever a score ≤ 3 or escalation fires, including owners and next steps.
</scoring_protocol>

<decision_rules>
- Accept when weighted_total ≥ 3.6 and no FailureTriggers/RedFlags fire.
- Revise when 2.8 ≤ weighted_total < 3.6 or any single criterion ≤ 2 with recoverable fixes.
- Block when weighted_total < 2.8 or any hard trigger fires; require human review before merge.
- In all cases cite specific lines/tests/logs that justify the verdict and next actions.
</decision_rules>

<report_format>
## Judge Summary
- Verdict: <ACCEPT | REVISE | BLOCK>
- Weighted total: <score>/5
- Key signals reviewed: counters, eviction policy, observability, tests.

## Score Breakdown
| Criterion | Weight | Score (1-5) | Evidence | Adjustments |
| --- | --- | --- | --- | --- |

## Required Actions
- **Owner:** <name or role>
- **Task:** <concrete fix or follow-up>
- **Why it matters:** <risk if skipped>
- **Due:** <deadline or trigger>

## Escalation Log
- Triggered? <Yes/No>
- Channel: {{escalation_channel}}
- Notes: <summary of escalation and next steps>
</report_format>
<!-- TEMPLATE END -->

/*******************************************************************************
 *  END OF SOLUTION TEMPLATE
 *  Use after you attempt the activity on your own.
 ******************************************************************************/
````

---

## 🔄 Using This Template

### In Your Workflow

1. **Generate refactor**: AI assistant refactors code and provides rationale
2. **Run judge**: `test_activity_3_4_solution(variables={...})` with your scenario
3. **Review verdict**: Check scores and recommendation
4. **Take action**: Accept (merge), Revise (iterate), or Block (escalate)

### Customizing for Your Needs

**Adjust weights** based on your priorities:
- Safety-critical systems: Increase safety/performance weight to 30%
- Legacy codebases: Increase test strategy weight to 30%
- Greenfield projects: Increase design quality weight to 35%

**Modify thresholds** based on team tolerance:
- Strict teams: Raise Accept threshold to ≥ 4.0
- Fast-moving teams: Lower Block threshold to < 2.5

**Add custom triggers** for your domain:
- Performance regressions (response time, memory)
- Compliance requirements (audit logging, data retention)
- API contract changes (breaking changes require review)

### Integration Ideas

- **CI/CD**: Run judge after refactor agent, fail build on BLOCK
- **PR Comments**: Post judge report as PR comment for reviewers
- **Metrics**: Track judge scores over time to measure refactor quality
- **Alerts**: Page on-call when critical regression detected
