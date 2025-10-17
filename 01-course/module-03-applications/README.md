# Module 3: Applications

## Apply Prompt Engineering to SDLC Workflows

Put advanced prompting tactics into practice by automating code review, test planning, and quality evaluation tasks across the software development lifecycle.

### Learning Objectives
By completing this module, you will be able to:

- ✅ Implement prompts that catch defects and gaps during code review, testing, and release gates
- ✅ Design reusable templates parameterized for different services, stacks, and teams
- ✅ Evaluate prompt output with judge rubrics and close the loop with iterative improvements
- ✅ Integrate prompt workflows with CI/CD, quality assurance, and engineering rituals

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

This module’s sections build on one another:
- **[Section 3.1](./3.1-setup-and-introduction.ipynb)** – Environment setup, provider validation, and module orientation
- **[Section 3.2](./3.2-code-review-automation.ipynb)** – Code review automation patterns with parameterized templates
- **[Section 3.3](./3.3-test-generation-automation.ipynb)** – Test generation automation for translating requirements into suites
- **[Section 3.4](./3.4-llm-as-judge-evaluation.ipynb)** – LLM-as-judge evaluation, rubric design, and automated quality gates

### Module Contents
- **[3.1-setup-and-introduction.ipynb](./3.1-setup-and-introduction.ipynb)** – Environment checks and provider validation
- **[3.2-code-review-automation.ipynb](./3.2-code-review-automation.ipynb)** – Comprehensive code review workflows
- **[3.3-test-generation-automation.ipynb](./3.3-test-generation-automation.ipynb)** – Requirement-to-test prompt patterns
- **[3.4-llm-as-judge-evaluation.ipynb](./3.4-llm-as-judge-evaluation.ipynb)** – Rubrics and automated quality gates
- **[activities/](./activities/)** – Practice briefs and instructions (`activities/README.md`)
- **[solutions/](./solutions/)** – Reference templates with deep-dive explanations
- **setup_utils.py** – Shared helpers for configuring AI providers and testing templates

### Time Required
Approximately 120-150 minutes (2-2.5 hours)

### Prerequisites
- Python 3.8+ installed
- IDE with notebook support (VS Code or Cursor recommended)
- API access to GitHub Copilot, CircuIT, or OpenAI

### Next Steps
After completing this module:
1. Refine and version your prompt templates using the testing helpers in `setup_utils.py`
2. Compare your work with the solutions directory to identify improvement ideas
3. Continue to [Module 4: Integration](../module-04-integration/) to operationalize prompt engineering across your organization
