# Prompt Engineering for Developers

A comprehensive learning resource for mastering prompt engineering techniques specifically designed for software developers. This course provides structured tutorials, hands-on exercises, and real-world implementation examples to help you integrate AI assistants effectively into your development workflow.

## Course Structure

Following the proven structure of AWS educational resources, this course is organized into three main sections:

### 📚 [01-tutorials/](./01-tutorials/) - Fundamentals & Learning
Complete tutorials teaching prompt engineering from foundations to advanced integration:
- **Module 1**: Course introduction, environment setup, and prompt anatomy
- **Module 2**: Core techniques - clear instructions, personas, delimiters, reasoning  
- **Module 3**: Software engineering applications - code quality, testing, debugging, APIs
- **Module 4**: Custom command integration for AI code assistants

### 🛠️ [02-exercises/](./02-exercises/) - Hands-On Practice
Interactive exercises and assessments to reinforce learning:
- **hands-on/**: Guided practice activities for each module
- **solutions/**: Complete reference implementations with detailed explanations

### 🎯 [03-examples/](./03-examples/) - Real-World Use Cases  
Production-ready patterns and implementation examples:
- **code-quality/**: Refactoring, modernization, and quality improvement workflows
- **debugging/**: Incident investigation, root cause analysis, and resolution patterns
- **api-integration/**: Client generation, error handling, and robust integration patterns
- **custom-commands/**: Reusable command templates and team adoption strategies

## Quick Start Guide

### Learning Path
1. **🎯 Start Here**: [01-tutorials/module-01-foundations/](./01-tutorials/module-01-foundations/) for environment setup
2. **📖 Learn**: Progress through tutorials in order (modules 1-4)  
3. **🛠️ Practice**: Complete exercises in [02-exercises/hands-on/](./02-exercises/hands-on/)
4. **🎯 Apply**: Implement patterns from [03-examples/](./03-examples/) in real projects

### Prerequisites
- **Python 3.8+** and package manager (uv recommended)
- **IDE** with notebook support (VS Code or Cursor)
- **API Access** to one of:
  - GitHub Copilot (recommended)
  - CircuIT APIs
  - OpenAI API key

### Environment Setup

Use uv to manage dependencies:

#### Using uv (Required)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Alternative: Install using pip
pip install uv

# Setup and install dependencies
cd prompteng-devs
uv venv .venv
source .venv/bin/activate
uv pip install --upgrade pip
uv sync -r requirements.txt
```

- **Configure environment variables**:

```bash
cp .env-default .env
$EDITOR .env
```

Rename `.env-default` to `.env` and edit the values to match your environment (e.g., API keys or tokens required by your workflow). Ensure `.env` is present before running notebooks that depend on environment variables.

- **Launch the notebook (Optional)**:

```bash
jupyter lab
# or
jupyter notebook
```

You can also open the folder directly in VS Code or Cursor and use their built-in notebook support. When prompted for a kernel, select the interpreter from `.venv`.

## Navigation & Usage

### Directory Structure Overview
```
prompt-eng-for-devs/
├── 01-tutorials/           # Complete learning modules
│   ├── module-01-foundations/
│   ├── module-02-fundamentals/  
│   ├── module-03-applications/
│   ├── module-04-integration/
│   └── prompt-engineering-for-developers.ipynb  # Complete course
├── 02-exercises/           # Hands-on practice
│   ├── hands-on/          # Exercise notebooks  
│   └── solutions/         # Reference solutions
├── 03-examples/           # Real-world patterns
│   ├── code-quality/
│   ├── debugging/
│   ├── api-integration/
│   └── custom-commands/
└── GitHub-Copilot-2-API/  # GitHub Copilot proxy setup
```

### Using the Notebooks
- **Kernel**: Select the `.venv` Python interpreter as the notebook kernel
- **Execution**: Run cells top-to-bottom initially, then iterate as needed  
- **Experimentation**: Create new cells for testing; preserve original examples
- **IDE Integration**: VS Code/Cursor built-in notebook support recommended

### Course Timing
- **Total Duration**: ~90 minutes
- **Session Options**: 
  - Single 90-minute session, or
  - Three 30-minute focused sessions, or  
  - Self-paced over multiple days

## Target Audience

This course is designed for:
- **Software Engineers** looking to integrate AI assistants into their workflow
- **Technical Leads** wanting to establish team prompt engineering standards
- **DevOps Engineers** seeking to automate development workflows with AI
- **Engineering Managers** planning AI-assisted development adoption

## What You'll Build

By course completion, you'll have:
- ✅ **Working Development Environment** with AI assistant integration
- ✅ **Prompt Engineering Toolkit** with reusable patterns and commands  
- ✅ **Production-Ready Workflows** for code quality, debugging, and API integration

## Contributing

Issues and pull requests welcome! Please ensure:
- Examples are minimal, reproducible, and well-documented
- New patterns include both implementation and usage guidance
- Educational content follows the established progression structure


