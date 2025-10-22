# Module 3: Applications

## Apply Prompt Engineering to SDLC Workflows

Put advanced prompting tactics into practice by automating code review, test planning, and quality evaluation tasks across the software development lifecycle.

### Learning Objectives
By completing the **core sections** (3.1-3.3), you will be able to:

- ✅ Implement prompts that catch defects and gaps during code review and testing
- ✅ Design reusable templates parameterized for different services, stacks, and teams
- ✅ Validate and iterate on prompt templates using test scenarios

**Optional advanced learning** (Section 3.4):
- ✅ Evaluate prompt output with weighted rubrics and automated decision thresholds
- ✅ Scale manual judging to systematic evaluations with production eval platforms

### Getting Started

**First time here?**  
- If you haven't set up your development environment yet, follow the [Quick Setup guide](../../README.md#-quick-setup) in the main README first  
- **New to Jupyter notebooks?** Read [About Jupyter Notebooks](../../README.md#-about-jupyter-notebooks) to understand how notebooks work and where code executes

**Ready to start?**
1. **Open Section 3.1**: Start with [3.1-setup-and-introduction.ipynb](./3.1-setup-and-introduction.ipynb) to configure your environment and preview the module
2. **Install dependencies**: Run the "Install Required Dependencies" cell in the notebook or `pip install -r requirements.txt`
3. **Follow the notebook**: Work through each cell sequentially—the notebook walks you through setup and exercises
4. **Complete exercises**: Build and test prompts alongside the guided labs and activity files

> **Note:** Unlike Modules 1 and 2, Module 3 is organized as four linked sections. Work through them in order:

### Core Sections (Complete These First)
- **[Section 3.1](./3.1-setup-and-introduction.ipynb)** – Environment setup, provider validation, and module orientation
- **[Section 3.2](./3.2-code-review-automation.ipynb)** – Code review automation patterns with parameterized templates
- **[Section 3.3](./3.3-test-generation-automation.ipynb)** – Test generation automation for translating requirements into suites

### Advanced Section (Optional)
- **[Section 3.4](./3.4-llm-as-judge-evaluation.ipynb)** ⭐ **Advanced (Optional)** – LLM-as-judge evaluation, rubric design, and systematic evals

> **💡 Recommended Path:** Complete core sections 3.1-3.3 first (95 minutes) for essential SDLC automation skills. Section 3.4 is optional—return to it when you need production-grade quality gates and systematic evaluation.

### Module Contents

**Core Notebooks:**
- **[3.1-setup-and-introduction.ipynb](./3.1-setup-and-introduction.ipynb)** – Environment checks and provider validation
- **[3.2-code-review-automation.ipynb](./3.2-code-review-automation.ipynb)** – Comprehensive code review workflows
- **[3.3-test-generation-automation.ipynb](./3.3-test-generation-automation.ipynb)** – Requirement-to-test prompt patterns

**Advanced (Optional):**
- **[3.4-llm-as-judge-evaluation.ipynb](./3.4-llm-as-judge-evaluation.ipynb)** ⭐ – Rubrics and automated quality gates

**Supporting Materials:**
- **[activities/](./activities/)** – Practice briefs and instructions (`activities/README.md`)
- **[solutions/](./solutions/)** – Reference templates with deep-dive explanations
- **setup_utils.py** – Shared helpers for configuring AI providers and testing templates

### Time Required
**Core sections (3.1-3.3):** 95 minutes (~1.5 hours)  
**With optional advanced section (3.4):** 135 minutes (~2.25 hours)

### Prerequisites
- Python 3.8+ installed
- IDE with notebook support (VS Code or Cursor recommended)
- API access to GitHub Copilot, CircuIT, or OpenAI

### Next Steps

**After completing core sections (3.1-3.3):**
1. Apply your templates to real project code
2. Compare your work with the solutions directory to identify improvement ideas
3. Continue to **[Module 4: Integration](../module-04-integration/)** to integrate templates into GitHub Copilot, OpenAI Codex, and Claude Code

**Want more advanced skills?**
- Complete **[Section 3.4: LLM-as-Judge](./3.4-llm-as-judge-evaluation.ipynb)** to learn production-grade evaluation with weighted rubrics and systematic testing
