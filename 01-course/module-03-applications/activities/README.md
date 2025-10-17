# Module 3: Practice Activities

Complete these hands-on activities to master SDLC prompt engineering.

---

## 📚 Activity Overview

| Activity | Topic | Time | Difficulty | Prerequisites |
|----------|-------|------|------------|---------------|
| [3.2](./activity-3.2-code-review.md) | Build Code Review Template | 30-40 min | ⭐⭐⭐ | `3.2-code-review-automation.ipynb` complete |
| [3.3](./activity-3.3-test-generation.md) | Build Test Generation Template | 30-40 min | ⭐⭐⭐ | `3.3-test-generation-automation.ipynb` complete |

---

## 🎯 How to Complete Activities

### Step 1: Open the Activity File
Each activity is a separate markdown file. Open it in your editor alongside the notebook.

### Step 2: Follow the 3-Step Process
Each activity uses the same proven workflow:

1. **RESEARCH** (10-15 min) - Study real-world patterns from AWS
2. **DESIGN** (10-15 min) - Answer planning questions before coding
3. **BUILD** (15-20 min) - Create your template between the markers

### Step 3: Edit the Template
Work directly in the activity file between these markers:
```markdown
<!-- TEMPLATE START -->
[Your template goes here]
<!-- TEMPLATE END -->
```

### Step 4: Test Your Template
Use the helper functions in the notebooks to test your templates:

```python
# In 3.2-code-review-automation.ipynb
test_activity_3_2(test_code="...", variables={...})

# In 3.3-test-generation-automation.ipynb
test_activity_3_3(test_code="...", variables={...})
```

**Results auto-save back to your activity file!** ✨

### Step 5: Compare with Solution
Check your work against the official solution in `solutions/`

**Pro Tip:** Solutions are also testable! Run them to see expected output:

```python
from setup_utils import test_activity

# Test the solution to see what "good" looks like
test_activity(
    'solutions/activity-3.2-code-review-solution.md',
    test_code="...",
    variables={...}
)
```

---

## 💡 Tips for Success

### Before You Start
- ✅ Complete the corresponding notebook section first
- ✅ Read the activity instructions carefully
- ✅ Study the AWS patterns linked in each activity

### While Working
- 🔄 **Iterate quickly** - Test early, test often
- 📝 **Take notes** - Capture insights in the Learning Notes section
- 🎯 **Focus on understanding** - Don't just copy patterns, understand why they work
- 🤔 **Think about edge cases** - What could go wrong?

### Testing Tips
- Start with the provided test cases
- Try multiple test scenarios
- Check if results meet all success criteria
- Compare output quality with examples in notebooks

### If You Get Stuck
1. Review the notebook examples
2. Study the AWS pattern more carefully
3. Check the "Common Issues" section in the activity
4. Compare with the solution (but try yourself first!)

---

## 🔧 Using the Testing Functions

### Quick Testing
```python
# Simplest usage
test_activity_3_2()  # Uses defaults
```

### With Custom Test Code
```python
# Test with your own code
test_code = """
def vulnerable_function():
    # your code here
"""

test_activity_3_2(test_code=test_code)
```

### With Template Variables
```python
# Customize template variables
test_activity_3_2(
    test_code=my_code,
    variables={
        'tech_stack': 'Python/Django',
        'repo_name': 'my-project',
        'service_name': 'api-service'
    }
)
```

### Test Solutions for Reference
```python
# Test the solution to see expected output
from setup_utils import test_activity

# Activity 3.2 solution
test_activity(
    'solutions/activity-3.2-code-review-solution.md',
    test_code=vulnerable_code,
    variables={'tech_stack': 'Python', 'repo_name': 'auth-service'}
)

# Activity 3.3 solution
test_activity(
    'solutions/activity-3.3-test-generation-solution.md',
    test_code=requirements,
    variables={'domain': 'E-commerce', 'tech_stack': 'Python/pytest'}
)
```

**Why test solutions?**
- See what "good" output looks like
- Compare your results to expert templates
- Learn from production-ready examples

---

## 📊 Track Your Progress

- [ ] **Setup** (`3.1-setup-and-introduction.ipynb`)
  - [ ] Install dependencies
  - [ ] Test AI connection
  - [ ] Understand module structure

- [ ] **Activity 3.2: Code Review Template** (30-40 min)
  - [ ] Complete: `3.2-code-review-automation.ipynb`
  - [ ] Research: AWS code review pattern
  - [ ] Design: Answer planning questions in `activity-3.2-code-review.md`
  - [ ] Build: Create template between `<!-- TEMPLATE START/END -->` markers
  - [ ] Test: Run `test_activity_3_2()` with authentication code
  - [ ] Compare: Test solution file to see expected output
  - [ ] Iterate: Improve based on comparison

- [ ] **Activity 3.3: Test Generation Template** (30-40 min)
  - [ ] Complete: `3.3-test-generation-automation.ipynb`
  - [ ] Research: AWS test generation pattern
  - [ ] Design: Answer planning questions in `activity-3.3-test-generation.md`
  - [ ] Build: Create template between markers
  - [ ] Test: Run `test_activity_3_3()` with discount system
  - [ ] Compare: Test solution file to see expected output
  - [ ] Iterate: Improve based on comparison

- [ ] **Optional: LLM-as-Judge** (`3.4-llm-as-judge-evaluation.ipynb`)
  - [ ] Learn evaluation patterns
  - [ ] Understand rubric design
  - [ ] See quality validation examples

**🎊 Completed all activities?** You've mastered SDLC prompt engineering fundamentals!

---

## 🎓 What You'll Learn

### Activity 3.2: Code Review
- ✅ How to structure comprehensive review prompts
- ✅ Defining clear severity levels and categories
- ✅ Reviewing across multiple dimensions (security, performance, quality)
- ✅ Generating actionable feedback with code examples
- ✅ Combining multiple tactics (role, context, chain-of-thought)
- ✅ Real-world pattern application from AWS

### Activity 3.3: Test Generation
- ✅ How to identify ambiguities in vague requirements
- ✅ Generating comprehensive edge cases systematically
- ✅ Separating unit tests from integration tests
- ✅ Creating complete test specifications
- ✅ Recommending test infrastructure needs

---

## 🔗 Quick Links

- [Notebook 1: Setup & Introduction](../3.1-setup-and-introduction.ipynb)
- [Notebook 2: Code Review Automation](../3.2-code-review-automation.ipynb)
- [Notebook 3: Test Generation Automation](../3.3-test-generation-automation.ipynb)
- [Notebook 4: LLM-as-Judge Evaluation](../3.4-llm-as-judge-evaluation.ipynb)
- [View Solutions](../solutions/) (now testable!)
- [Module 3 README](../README.md)

---

## 🤝 Getting Help

**Questions?**
- Check the "Common Issues" table in each activity
- Review the notebook examples
- Study the AWS patterns more carefully
- Compare with solutions (after attempting yourself!)

**Found a bug or have suggestions?**
- Open an issue in the repository
- Share feedback with your instructor

---

## 📈 Success Metrics

You'll know you've mastered these skills when you can:

1. ✅ Identify which prompt tactics to combine for different SDLC tasks
2. ✅ Design templates that produce consistent, high-quality outputs
3. ✅ Adapt templates to your specific project context
4. ✅ Test and iterate on prompts systematically
5. ✅ Explain design decisions and trade-offs

**Ready to start?** Open [Activity 3.2](./activity-3.2-code-review.md) and begin! 🚀
