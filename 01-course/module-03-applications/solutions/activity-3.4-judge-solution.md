# Activity 3.4 Solution: Quality Evaluation with LLM-as-Judge

## ✅ What Makes This Solution Follow Best Practices

### 1. Intentionally Low-Quality Input

```xml
<description>Function could be improved</description>
<evidence>The code is not optimal</evidence>
<recommendation>Make it better</recommendation>
```

**Why this matters:**
- Tests the judge's ability to catch poor quality outputs
- Demonstrates what NOT to accept in production
- Realistic: Some AI outputs will be vague or unhelpful
- Validates that the quality gate actually works

### 2. Context-Specific Rubric

```xml
<rubric>
1. Specificity (40%): Are issues concrete with exact evidence?
2. Actionability (30%): Can developer immediately act?
3. Technical Accuracy (20%): Are issues technically sound?
4. Completeness (10%): Are major categories covered?
</rubric>
```

**Why this matters:**
- Weights match your team's priorities (example shows CI/CD context)
- Different contexts need different weightings
- CI/CD needs high specificity (automated posting)
- Documentation review might weight Communication higher

### 3. Explicit Scoring Scale

```
- 5: Excellent - Ready for production
- 4: Good - Minor improvements needed
- 3: Acceptable - Meets minimum bar
- 2: Poor - Significant issues, needs revision
- 1: Unacceptable - Reject and regenerate
```

**Why this matters:**
- Clear definitions prevent ambiguity and inconsistent scoring
- Maps to actionable decisions (not subjective "good/bad")
- Consistent across evaluations (same criteria every time)
- Enables metric tracking over time

### 4. Actionable Thresholds

```
- ACCEPT (≥4.0): Post to PR
- REVISE (2.5-3.9): Regenerate with specific guidance
- REJECT (<2.5): Discard, use different approach
```

**Why this matters:**
- Clear decision points enable automation
- Each outcome has a defined action
- Can be implemented as: `if score >= 4.0: post_to_pr()`
- Middle tier (REVISE) triggers improvement loop instead of failure

### 5. Improvement Feedback Required

```xml
<improvement_needed></improvement_needed>
```

**Why this matters:**
- Not just score, but HOW to improve
- Enables iterative refinement
- Feeds back into prompt improvement process
- Creates a learning loop

## 📊 Expected Judge Evaluation

### Detailed Scoring Breakdown

#### Specificity Score: 1/5 ❌

**Rationale:**
- "Function could be improved" is completely vague
- "The code is not optimal" provides zero evidence
- No line numbers cited
- No specific issues identified
- No code snippets shown

**Improvement Needed:**
```
Replace with: "Line 2: Missing input validation allows negative discount_percent values"
Include: Exact line numbers, quoted code, specific issue description
```

#### Actionability Score: 1/5 ❌

**Rationale:**
- "Make it better" is not actionable
- Developer has no idea WHAT to change
- No code examples provided
- No specific steps given
- Cannot implement without additional research

**Improvement Needed:**
```
Replace with: "Add validation before calculation:
if not 0 <= discount_percent <= 100:
    raise ValueError('Discount must be between 0 and 100%')"
Include: Exact code changes, why they're needed, examples
```

#### Technical Accuracy Score: 2/5 ⚠️

**Rationale:**
- "medium severity" seems reasonable but no justification provided
- Can't verify if assessment is technically correct
- No explanation of WHY it's medium vs high/low
- Might be inaccurate but impossible to tell

**Improvement Needed:**
```
Include reasoning: "Severity: major - Input validation missing can lead to 
runtime errors (negative prices, divide by zero if used in calculations), 
affecting production reliability"
```

#### Completeness Score: 2/5 ⚠️

**Rationale:**
- Only one vague issue found (likely incomplete)
- No security analysis (SQL injection? XSS?)
- No performance considerations
- No maintainability checks (type hints, docstrings)
- No correctness verification

**Improvement Needed:**
```
Systematic check required:
✓ Security issues
✓ Performance concerns  
✓ Correctness bugs
✓ Maintainability improvements
✓ Error handling
```

### Weighted Score Calculation

```python
# Calculate weighted score
specificity_score = 1
actionability_score = 1
technical_accuracy_score = 2
completeness_score = 2

weighted_total = (
    (specificity_score * 0.40) +      # 0.40
    (actionability_score * 0.30) +    # 0.30
    (technical_accuracy_score * 0.20) + # 0.40
    (completeness_score * 0.10)       # 0.20
)
# Total: 1.3
```

### Decision: REJECT (<2.5) 🚫

**Feedback for Improvement:**

```markdown
This review fails to meet minimum quality standards and must be rejected.

Critical Issues:
1. ❌ Vague descriptions lack specificity
   - Current: "Function could be improved"
   - Required: "Line 2: Function lacks input validation for discount_percent parameter"

2. ❌ Recommendations not actionable
   - Current: "Make it better"
   - Required: "Add validation: if not 0 <= discount_percent <= 100: raise ValueError(...)"

3. ❌ No evidence provided
   - Current: "The code is not optimal"
   - Required: Quote exact code, cite line numbers, explain WHY it's an issue

4. ❌ Incomplete coverage
   - Only 1 issue found, likely missing critical problems
   - Should cover: security, performance, correctness, maintainability

Example of Acceptable Quality:
<issue>
  <severity>major</severity>
  <description>Missing input validation allows invalid discount percentages</description>
  <evidence>Line 2: Function accepts any numeric value for discount_percent. 
  Values > 100 result in negative prices. Values < 0 increase price.</evidence>
  <recommendation>Add validation before calculation:
  
  if not 0 <= discount_percent <= 100:
      raise ValueError(f"Discount must be between 0-100%, got {discount_percent}%")
      
  This prevents invalid inputs and provides clear error messages.</recommendation>
</issue>

DO NOT POST THIS REVIEW. Regenerate with specific, actionable feedback.
```

## 💻 Production Implementation

### Complete Automated Quality Gate

```python
from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class JudgeResult:
    """Structured judge evaluation result"""
    specificity_score: float
    actionability_score: float
    technical_accuracy_score: float
    completeness_score: float
    weighted_total: float
    decision: str  # ACCEPT, REVISE, REJECT
    feedback: str

def parse_judge_output(judge_response: str) -> JudgeResult:
    """Parse judge XML/text response into structured result"""
    # In production, use proper XML parsing
    # This is simplified for demonstration
    
    # Extract scores using regex (production should use XML parser)
    specificity = float(re.search(r'Specificity.*?(\d+)/5', judge_response).group(1))
    actionability = float(re.search(r'Actionability.*?(\d+)/5', judge_response).group(1))
    technical = float(re.search(r'Technical.*?(\d+)/5', judge_response).group(1))
    completeness = float(re.search(r'Completeness.*?(\d+)/5', judge_response).group(1))
    
    # Calculate weighted score
    weighted = (
        (specificity * 0.40) +
        (actionability * 0.30) +
        (technical * 0.20) +
        (completeness * 0.10)
    )
    
    # Determine decision
    if weighted >= 4.0:
        decision = "ACCEPT"
    elif weighted >= 2.5:
        decision = "REVISE"
    else:
        decision = "REJECT"
    
    # Extract feedback
    feedback = re.search(r'<feedback>(.*?)</feedback>', judge_response, re.DOTALL).group(1)
    
    return JudgeResult(
        specificity_score=specificity,
        actionability_score=actionability,
        technical_accuracy_score=technical,
        completeness_score=completeness,
        weighted_total=weighted,
        decision=decision,
        feedback=feedback
    )

def automated_quality_gate(ai_review: str, max_retries: int = 2) -> dict:
    """
    Complete quality gate with retry logic.
    
    Returns:
        dict with 'status', 'review', 'score', 'attempts'
    """
    
    for attempt in range(max_retries + 1):
        # Evaluate with judge
        judge_result = evaluate_with_judge(ai_review)
        score = judge_result.weighted_total
        
        # Log attempt
        log_metric(f"judge_score_attempt_{attempt}", score)
        
        if score >= 4.0:
            # HIGH QUALITY - Accept and post
            post_to_pr(ai_review)
            log_metric("ai_review_accepted", score)
            
            return {
                "status": "POSTED",
                "review": ai_review,
                "score": score,
                "attempts": attempt + 1
            }
        
        elif score >= 2.5 and attempt < max_retries:
            # MEDIUM QUALITY - Regenerate with feedback
            print(f"⚠️ Score {score} < 4.0. Regenerating with feedback...")
            
            # Regenerate with specific improvements
            ai_review = regenerate_with_feedback(
                original=ai_review,
                feedback=judge_result.feedback,
                attempt=attempt
            )
            
            # Continue to next iteration
            continue
        
        elif score < 2.5:
            # LOW QUALITY - Reject and fallback to human
            log_metric("ai_review_rejected", score)
            flag_for_human_review(reason=judge_result.feedback)
            
            return {
                "status": "HUMAN_REVIEW_REQUIRED",
                "review": None,
                "score": score,
                "attempts": attempt + 1
            }
        
        else:
            # MAX RETRIES REACHED
            log_metric("ai_review_max_retries", score)
            flag_for_human_review(reason="Max retries exceeded")
            
            return {
                "status": "NEEDS_HUMAN",
                "review": ai_review,
                "score": score,
                "attempts": attempt + 1
            }
    
    return {"status": "FAILED", "review": None, "score": 0, "attempts": max_retries + 1}


# Example usage in CI/CD
def ci_cd_review_workflow(pr_diff: str):
    """Complete CI/CD workflow with quality gate"""
    
    # Step 1: Generate review
    ai_review = generate_code_review(pr_diff)
    
    # Step 2: Quality gate with retry
    result = automated_quality_gate(ai_review, max_retries=2)
    
    # Step 3: Handle outcome
    if result['status'] == 'POSTED':
        print(f"✅ AI review posted (score: {result['score']}, attempts: {result['attempts']})")
        
    elif result['status'] == 'NEEDS_HUMAN':
        print(f"⚠️ AI review quality insufficient. Human review requested.")
        send_slack_notification(
            channel="#code-reviews",
            message=f"PR requires human review. AI score: {result['score']}"
        )
    
    elif result['status'] == 'HUMAN_REVIEW_REQUIRED':
        print(f"❌ AI review rejected. Flagging for human review.")
        add_pr_label("needs-human-review")
```

### Monitoring Dashboard

```python
def generate_quality_dashboard():
    """Track LLM-as-Judge metrics over time"""
    
    metrics = {
        "acceptance_rate": count_accepted() / count_total(),
        "average_score": mean(all_scores()),
        "score_distribution": histogram(all_scores()),
        "retry_rate": count_retries() / count_total(),
        "human_fallback_rate": count_human_reviews() / count_total(),
        
        # By score component
        "specificity_trend": timeseries("specificity"),
        "actionability_trend": timeseries("actionability"),
        
        # Efficiency metrics
        "avg_attempts_per_review": mean(attempts_per_review()),
        "cost_per_accepted_review": calculate_cost(),
    }
    
    return metrics

# Example output:
# Acceptance Rate: 76% (↑ from 68% last week)
# Average Score: 4.1 / 5.0
# Score Distribution: [5★: 23%, 4★: 53%, 3★: 18%, 2★: 5%, 1★: 1%]
# Human Fallback: 6% (target < 10%)
# Avg Cost: $0.08 per accepted review
```

## 🎯 Key Takeaway

LLM-as-Judge isn't just scoring - it's a **complete quality assurance system**:

1. **Automated QA** - Catches poor outputs before they reach users
2. **Feedback Loop** - Provides actionable improvement guidance
3. **Decision Automation** - Enables if/else logic: accept/revise/reject
4. **Continuous Improvement** - Metrics guide prompt refinement
5. **Cost Control** - Prevents wasting human time on low-quality AI outputs
6. **Trust Building** - Teams gain confidence in AI-assisted workflows

### Success Metrics to Track

- **Acceptance Rate**: % of AI outputs that pass quality gate (target: >70%)
- **Average Score**: Mean judge score (target: >4.0)
- **Human Fallback Rate**: % requiring human review (target: <10%)
- **Cost per Review**: Including retries (target: <$0.10)
- **Score Trend**: Improving over time as prompts are refined

---

**Remember**: The judge is only as good as its rubric. Invest time in defining evaluation criteria that match your team's standards and priorities.

