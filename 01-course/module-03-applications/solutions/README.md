# Module 3 Solutions

Reference implementations for all practice activities.

---

## 📁 Solutions

### [Activity 3.2: Code Review](activity-3.2-code-review-solution.md)
Multi-dimensional review template with severity classification and CI/CD integration

```python
test_activity_3_2_solution(test_code=code, variables={'tech_stack': 'Python'})
```

### [Activity 3.3: Test Generation](activity-3.3-test-generation-solution.md)
Ambiguity detection, edge cases, unit/integration test separation

```python
test_activity_3_3_solution(test_code=requirements, variables={'domain': 'E-commerce'})
```

### [Activity 3.4: LLM-as-Judge](activity-3.4-llm-as-judge-evaluation-solution.md)
Weighted rubric template with Accept/Revise/Block verdicts

```python
from setup_utils import test_activity_3_4_solution, get_refactor_judge_scenario
test_activity_3_4_solution(variables=get_refactor_judge_scenario())
```

**Design:** Correctness (35%), Design (25%), Safety (20%), Tests (20%)

---

## 🎯 Using Solutions

1. **Try first** - Attempt activity without looking
2. **Test yours** - Run your template
3. **Compare** - Check solution for patterns
4. **Test solution** - See expected output
5. **Iterate** - Refine based on insights

---

## 📊 Best Practice Markers

Each solution demonstrates:
- ✅ Domain-specific roles and terminology
- ✅ Measurable criteria with evidence requirements
- ✅ Actionable output with WHY explanations
- ✅ Production patterns (CI/CD, automation)
- ✅ Parameterized and reusable templates


---

## 🧪 Test All Solutions

```python
from setup_utils import (
    test_activity_3_2_solution,
    test_activity_3_3_solution, 
    test_activity_3_4_solution,
    get_refactor_judge_scenario
)

# Code review
test_activity_3_2_solution(
    test_code="def auth(user): query = f'SELECT * FROM users WHERE name={user}'",
    variables={'tech_stack': 'Python'}
)

# Test generation
test_activity_3_3_solution(
    test_code="Build discount calculator with percentage discounts and edge cases",
    variables={'domain': 'E-commerce'}
)

# LLM-as-Judge
test_activity_3_4_solution(variables=get_refactor_judge_scenario())
```

---

## 📚 Next Steps

1. **Implement** - Start with one template in your project
2. **Customize** - Adapt for your domain/stack
3. **Measure** - Track detection rate, time saved
4. **Build evals** - Collect datasets for Activity 3.4 judge
5. **Share** - Version control and document for team

---

**Questions?** Open an issue or submit a PR with variations!
