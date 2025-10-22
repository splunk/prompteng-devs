# Module 3: Practice Activities

Complete these hands-on activities to master SDLC prompt engineering.

---

## 📚 Activities

### Core Activities (Complete First)
| # | Topic | Time | Difficulty |
|---|-------|------|------------|
| [3.2](./activity-3.2-code-review.md) | Code Review Template | 30-40 min | ⭐⭐⭐ |
| [3.3](./activity-3.3-test-generation.md) | Test Generation Template | 30-40 min | ⭐⭐⭐ |

### Advanced Activity (Optional)
| # | Topic | Time | Difficulty |
|---|-------|------|------------|
| [3.4](./activity-3.4-llm-as-judge-evaluation.md) | LLM-as-Judge Template ⭐ | 30-40 min | ⭐⭐⭐⭐ Advanced |

> **💡 New to this?** Master 3.2 and 3.3 first before attempting the advanced judge evaluation.

---

## 🎯 How to Complete

### 1. Open Activity File
Each activity is in `activities/activity-X.X-name.md`

### 2. Edit Template
Replace `TODO` comments between:
```markdown
<!-- TEMPLATE START -->
[Your work here]
<!-- TEMPLATE END -->
```

### 3. Test in Notebook
```python
# Activity 3.2 & 3.3
test_activity_3_2(test_code="...", variables={...})
test_activity_3_3(test_code="...", variables={...})

# Activity 3.4
from setup_utils import test_activity_3_4, get_refactor_judge_scenario
test_activity_3_4(variables=get_refactor_judge_scenario())
```

### 4. Compare Solution
```python
# Test solutions to see expected output
test_activity_3_2_solution(...)
test_activity_3_3_solution(...)
test_activity_3_4_solution(variables=get_refactor_judge_scenario())
```

---

## 💡 Tips

**Before starting:**
- ✅ Complete corresponding notebook first
- ✅ Read activity instructions fully

**While working:**
- Test early and often
- Try multiple scenarios
- Compare with solution only after attempting

**If stuck:**
- Review notebook examples
- Check activity "Common Issues" section
- Study patterns more carefully

---

## 📊 Progress Checklist

### Core Activities

#### Activity 3.2: Code Review (30-40 min)
- [ ] Complete `3.2-code-review-automation.ipynb`
- [ ] Study AWS code review pattern
- [ ] Edit template in `activity-3.2-code-review.md`
- [ ] Test with `test_activity_3_2()`
- [ ] Compare with solution

### Activity 3.3: Test Generation (30-40 min)
- [ ] Complete `3.3-test-generation-automation.ipynb`
- [ ] Study AWS test generation pattern
- [ ] Edit template in `activity-3.3-test-generation.md`
- [ ] Test with `test_activity_3_3()`
- [ ] Compare with solution

### Advanced Activity (Optional)

#### Activity 3.4: LLM-as-Judge ⭐ (30-40 min)
- [ ] Complete `3.4-llm-as-judge-evaluation.ipynb`
- [ ] Edit judge template in `activity-3.4-llm-as-judge-evaluation.md`
- [ ] Test with `test_activity_3_4(variables=get_refactor_judge_scenario())`
- [ ] Review "Why Evals Matter" section
- [ ] Compare with solution

---

## 🎓 Learning Goals

**Activity 3.2:** Multi-dimensional code review, severity levels, actionable feedback

**Activity 3.3:** Ambiguity detection, edge case generation, test separation

**Activity 3.4:** Weighted rubrics, score scales, automated decisions, systematic evals

---

## 🔗 Quick Links

- [Notebook 2: Code Review](../3.2-code-review-automation.ipynb)
- [Notebook 3: Test Generation](../3.3-test-generation-automation.ipynb)
- [Notebook 4: LLM-as-Judge](../3.4-llm-as-judge-evaluation.ipynb)
- [View Solutions](../solutions/)
- [Module 3 README](../README.md)

---

**Ready?** Open [Activity 3.2](./activity-3.2-code-review.md) to start! 🚀
