# Prompt Engineering for Developers

Master prompting techniques for software development with structured tutorials, hands-on exercises, and real-world examples.

## 🚀 Get Started

**1. Clone the repository:**
```bash
git clone git@github.com:splunk/prompteng-devs.git
cd prompteng-devs
```

**2. Begin learning:**
- **[Start Module 1: Foundations](./01-tutorials/module-01-foundations/)** ← Read README.md, then open the `.ipynb` notebook
- **[View All Modules](./01-tutorials/)** ← Browse the complete course
- **[Practice Exercises](./02-exercises/hands-on/)** ← Complete after each module
- **[Real Examples](./03-examples/)** ← Production patterns

---

## 📚 Learning Path

### 🎯 Recommended Learning Workflow

<div style="background:#f8f9fa; border-radius:8px; padding:18px 22px; margin-bottom:18px; border:1px solid #e0e0e0; box-shadow:0 1px 4px #0001">

<div style="font-weight:700; font-size:1.2em; color:#1a202c; margin-bottom:16px">📚 For Each Module:</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#3b82f6; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">1</span>
<span style="font-weight:600; color:#1a202c">Read the module's <code style="background:#e2e8f0; color:#2d3748; padding:3px 8px; border-radius:4px; font-weight:600">README.md</code></span>
</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#10b981; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">2</span>
<span style="font-weight:600; color:#1a202c">Open the <code style="background:#e2e8f0; color:#2d3748; padding:3px 8px; border-radius:4px; font-weight:600">.ipynb</code> notebook</span>
</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#f59e0b; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">3</span>
<span style="font-weight:600; color:#1a202c">Complete all cells</span>
</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#8b5cf6; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">4</span>
<span style="font-weight:600; color:#1a202c">Practice exercises</span>
</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#ef4444; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">5</span>
<span style="font-weight:600; color:#1a202c">Self-assess with competency matrix</span>
</div>

<div style="display:flex; align-items:center; margin:10px 0; font-size:1em">
<span style="background:#6b7280; color:white; padding:6px 10px; border-radius:12px; font-weight:700; margin-right:14px; font-size:0.9em">6</span>
<span style="font-weight:600; color:#1a202c">Move to next module</span>
</div>

</div>

**📈 Track Progress**: Use the competency matrix in each notebook  
**🚀 Apply Skills**: Use real-world examples after completing all modules

💡 **Tip**: Each module directory contains a `README.md` file explaining what you'll learn and how to get started.

### 1. **Interactive Tutorials** - Learn the fundamentals
- **[Module 1: Foundations](./01-tutorials/module-01-foundations/)** - Interactive notebook (`.ipynb`) with environment setup & prompt anatomy (20 min)
- **[Module 2: Core Techniques](./01-tutorials/module-02-fundamentals/)** - Interactive notebook (`.ipynb`) with instructions, personas, reasoning (30 min)  
- **[Module 3: Applications](./01-tutorials/module-03-applications/)** - Interactive notebook (`.ipynb`) with code quality, testing, debugging (30 min)
- **[Module 4: Integration](./01-tutorials/module-04-integration/)** - Interactive notebook (`.ipynb`) with custom commands & AI assistants (10 min)

### 2. **Practice** - Reinforce learning
- **[Hands-on Exercises](./02-exercises/hands-on/)** - Complete after each module to reinforce concepts
- **[Solutions](./02-exercises/solutions/)** - Reference implementations
- **Self-Assessment** - Use the competency matrix in each module to track your progress

### 3. **Apply** - Real-world patterns
- **[Code Quality](./03-examples/code-quality/)** - Refactoring & modernization
- **[Debugging](./03-examples/debugging/)** - Incident investigation & resolution
- **[API Integration](./03-examples/api-integration/)** - Client generation & error handling
- **[Custom Commands](./03-examples/custom-commands/)** - Reusable templates

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

## 🎯 What You'll Build

- ✅ **Working Development Environment** with AI assistant integration
- ✅ **Prompt Engineering Toolkit** with reusable patterns and commands  
- ✅ **Production-Ready Workflows** for code quality, debugging, and API integration

**Total Time**: ~90 minutes (can be split into 3×30min sessions)

---

## 📁 Project Structure

```
prompteng-devs/
├── 01-tutorials/           # Learning modules
├── 02-exercises/           # Practice activities  
├── 03-examples/           # Real-world patterns
└── GitHub-Copilot-2-API/  # Copilot setup
```

**Notebook Usage**: Each module IS an interactive notebook (`.ipynb` files). Select `.venv` Python interpreter as kernel, run cells top-to-bottom, experiment in new cells.

---

## 🤝 Contributing

Issues and pull requests welcome! Ensure examples are minimal, reproducible, and well-documented.