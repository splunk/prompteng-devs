# Prompt Engineering for Developers

Master prompting techniques for software development with structured tutorials, hands-on exercises, and real-world examples.

## 🚀 Get Started

**1. Clone the repository:**
```bash
git clone git@github.com:splunk/prompteng-devs.git
cd prompteng-devs
```

**2. Begin learning:**
- **[Start Module 1: Foundations](./01-tutorials/module-01-foundations/)** ← Begin learning immediately
- **[View All Modules](./01-tutorials/)** ← Browse the complete course
- **[Practice Exercises](./02-exercises/hands-on/)** ← Complete after each module
- **[Real Examples](./03-examples/)** ← Production patterns

---

## 📚 Learning Path

### Recommended Workflow
1. **Complete each module** → **Practice exercises** → **Self-assess** → **Next module**
2. **Track your progress** using the competency matrix in each module
3. **Apply skills** with real-world examples after completing all modules

### 1. **Tutorials** - Learn the fundamentals
- **[Module 1: Foundations](./01-tutorials/module-01-foundations/)** - Environment setup & prompt anatomy (20 min)
- **[Module 2: Core Techniques](./01-tutorials/module-02-fundamentals/)** - Instructions, personas, reasoning (30 min)  
- **[Module 3: Applications](./01-tutorials/module-03-applications/)** - Code quality, testing, debugging (30 min)
- **[Module 4: Integration](./01-tutorials/module-04-integration/)** - Custom commands & AI assistants (10 min)

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

**Notebook Usage**: Select `.venv` Python interpreter as kernel, run cells top-to-bottom, experiment in new cells.

---

## 🤝 Contributing

Issues and pull requests welcome! Ensure examples are minimal, reproducible, and well-documented.