# Prompt Engineering for Developers

Master prompting techniques for software development with structured tutorials, hands-on exercises, and real-world examples.

## 🚀 Get Started

**1. Clone the repository:**
```bash
git clone git@github.com:splunk/prompteng-devs.git
cd prompteng-devs
```

**2. Begin learning:**
- **[Start Module 1: Foundations](./01-course/module-01-foundations/)** ← Read README.md, then open the `.ipynb` notebook
- **[View All Modules](./01-course/)** ← Browse the complete course
- **[Implementation Examples](./02-implementation-examples/)** ← Production patterns

---

## 🎯 Recommended Learning Workflow

> **📚 For Each Module:**

#### **Step 1: 📖 Read the Module**
- Open the module's `README.md` file to understand learning objectives and prerequisites

#### **Step 2: 🚀 Launch the Notebook** 
- Open the `.ipynb` notebook file to begin the interactive tutorial

#### **Step 3: 💻 Complete All Cells**
- Run through each cell sequentially from top to bottom

#### **Step 4: 🏃‍♀️ Practice Exercises**
- Complete the hands-on exercises to reinforce learning

#### **Step 5: 📊 Self-Assess**
- Use the competency matrix in the notebook to track your progress

#### **Step 6: ➡️ Next Module**
- Move to the next module and repeat the process

**📈 Track Progress**: Use the competency matrix in each notebook  
**🚀 Apply Skills**: Use real-world examples after completing all modules

💡 **Tip**: Each module directory contains a `README.md` file explaining what you'll learn and how to get started.

---

## ⚡ Quick Setup

**Prerequisites**: Python 3.8+, IDE with notebook support, API access (GitHub Copilot/CircuIT/OpenAI)

```bash
# 1. Clone the repository
git clone git@github.com:splunk/prompteng-devs.git
cd prompteng-devs

# 2. Install dependencies
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --seed
source .venv/bin/activate
uv pip install ipykernel

# 3. Configure environment
cp .env-example .env
# Edit .env with your API keys
```

**Splunk users**: Run `okta-artifactory-login -t pypi` before installing dependencies.

---

## 📚 Learning Path

### 1. **Interactive Course** - Learn the fundamentals
- **[Module 1: Foundations](./01-course/module-01-foundations/)** - Interactive notebook (`.ipynb`) with environment setup & prompt anatomy (20 min)
- **[Module 2: Core Techniques](./01-course/module-02-fundamentals/)** - Interactive notebook (`.ipynb`) with instructions, personas, reasoning (30 min)  
- **[Module 3: Applications](./01-course/module-03-applications/)** - Interactive notebook (`.ipynb`) with code quality, testing, debugging (30 min)
- **[Module 4: Integration](./01-course/module-04-integration/)** - Interactive notebook (`.ipynb`) with custom commands & AI assistants (10 min)

### 2. **Practice** - Reinforce learning
- **Hands-on Exercises** - Integrated into each module to reinforce concepts
- **Self-Assessment** - Use the competency matrix in each module to track your progress

### 3. **Apply** - Real-world patterns
- **[Code Quality](./02-implementation-examples/code-quality/)** - Refactoring & modernization
- **[Debugging](./02-implementation-examples/debugging/)** - Incident investigation & resolution
- **[API Integration](./02-implementation-examples/api-integration/)** - Client generation & error handling
- **[Custom Commands](./02-implementation-examples/custom-commands/)** - Reusable templates


## 🎯 What You'll Build

- ✅ **Working Development Environment** with AI assistant integration
- ✅ **Prompt Engineering Toolkit** with reusable patterns and commands  
- ✅ **Production-Ready Workflows** for code quality, debugging, and API integration

**Total Time**: ~90 minutes (can be split into 3×30min sessions)

---

## 📁 Project Structure

```
prompteng-devs/
├── 01-course/                    # Learning modules
├── 02-implementation-examples/   # Real-world patterns
└── GitHub-Copilot-2-API/         # Copilot setup
```

**Notebook Usage**: Each module IS an interactive notebook (`.ipynb` files). Select `.venv` Python interpreter as kernel, run cells top-to-bottom, experiment in new cells.

---

## 🤝 Contributing

Issues and pull requests welcome! Ensure examples are minimal, reproducible, and well-documented.