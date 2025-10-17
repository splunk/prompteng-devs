# Activity 3.2: Build Your Own Code Review Template

**⏱️ Time Required:** 30-40 minutes  
**🎯 Difficulty:** Intermediate  
**📚 Prerequisites:** Complete `Section 1` of `3.2-code-review-automation.ipynb`

---

## 🎯 Your Mission

Create a reusable code review prompt template. You will research an industry pattern, adapt it to your needs, and make sure it catches issues across security, performance, maintainability, and overall code quality.

---

## 📋 Success Criteria

Your template should:
- ✅ Review code across security, performance, maintainability, and best practices
- ✅ Call out high-impact issues with line references and severity
- ✅ Suggest clear, actionable fixes
- ✅ Produce a tidy, repeatable review format

---

## 🔍 Scenario Snapshot

The team maintains a user authentication service. Recent reviews surfaced:
- SQL injection and weak password hashing
- Inefficient database access patterns
- Thin validation and error handling

Your template must consistently catch issues like these.

---

## 📝 Working Plan

### Step 1 — Research (10-15 minutes)
1. Read the [AWS Anthropic Code Review Pattern](https://github.com/aws-samples/anthropic-on-aws/blob/main/advanced-claude-code-patterns/commands/code-review.md).
2. Jot down how they structure the prompt, the review dimensions they insist on, how severity is defined, and what their output looks like.

Use the space below for quick notes:
```
Dimensions to copy or adapt:
- Security:
- Performance:
- Maintainability / Quality:
- Other:

What keeps feedback actionable?
-
```

### Step 2 — Blueprint Your Template (10-15 minutes)
Fill in these prompts before you touch the template block (we show XML by default, but you can swap in Markdown later if you prefer):
```
Role (who is reviewing?):

Essential context to provide:

Must-have review dimensions:

Output shape (sections, severity labels, etc.):

Any reusable {{variables}} you want:
```

### Step 3 — Build & Test (15-20 minutes)
1. Scroll to the template block below and edit only the content between `<!-- TEMPLATE START -->` and `<!-- TEMPLATE END -->`.
2. Replace placeholder text with your own role, guidelines, tasks, and output format.
3. Stick with the XML shell shown, or switch the code fence (e.g., to ````markdown) and rewrite it in structured Markdown—the tester will capture everything between the markers either way.
4. Save the file, then open `3.2-code-review-automation.ipynb` and run `test_activity_3_2()` to check your work.

**Helpful reminders**
- Leave the HTML comments (`<!-- TEMPLATE START/END -->`) in place so the tester can find your template.
- If you keep the XML version, reuse the existing tags (`<role>`, `<context>`, etc.) and keep `{{variables}}` for portability.
- If you switch to Markdown, keep the sections clearly labeled (headings or bold labels work well) and leave `{{variables}}` wherever you need substitution.
- Make severity labels and categories meaningful for your team. Think “CRITICAL/MAJOR/MINOR/INFO” or similar.

<details>
<summary>❓ Why do I need those HTML comment markers? (Click to expand)</summary>

The `<!-- TEMPLATE START -->` and `<!-- TEMPLATE END -->` markers tell the `test_activity_3_2()` function where your template begins and ends. They're invisible when markdown is rendered but essential for the auto-testing feature!

</details>

---

## 👇 YOUR EDITABLE TEMPLATE IS BELOW 👇

````xml
/*******************************************************************************
 *  ✏️  EDIT YOUR TEMPLATE BETWEEN THE COMMENT BLOCKS
 *  
 *  The test function extracts everything between:
 *  <!-- TEMPLATE START --> and <!-- TEMPLATE END -->
 *  
 *  Instructions:
 *  1. Replace TODO comments with your content
 *  2. Customize guidelines, tasks, and output format
 *  3. Keep the structure clear (XML tags or well-labeled Markdown)
 *  4. Use {{variables}} for parameterization
 *  
 *  Tip: If you convert this to Markdown, change the opening ````xml fence accordingly.
 ******************************************************************************/

<!-- TEMPLATE START -->
<role>
<!-- TODO: Define the reviewer persona (e.g., Senior {{tech_stack}} Engineer) and list the areas of expertise you want the model to emphasise. -->
</role>

<context>
<!-- EDITING NOT REQUIRED: these context fields are provided by the function call variables -->
Repository: {{repo_name}}
Service: {{service_name}}
Purpose: {{change_purpose}}
</context>

<code_diff>
{{code_diff}}
</code_diff>

<review_guidelines>
<!-- TODO: List the review dimensions (Security, Performance, Error Handling, Code Quality, Correctness, Best Practices, etc.). -->
<!-- TODO: For each dimension, describe what to look for and how to report issues (line refs, impact, fix). -->
</review_guidelines>

<tasks>
<!-- TODO: Break the workflow into numbered steps (e.g., Step 1 - Think, Step 2 - Assess, Step 3 - Suggest, Step 4 - Verdict). -->
<!-- TODO: Under each step, include bullet prompts that guide the model's reasoning and outputs. -->
</tasks>

<output_format>
<!-- TODO: Response must be Markdown with the following structure: -->
<!-- TODO: - `## Summary` containing 1-3 bullet takeaways. -->
<!-- TODO: - `## Findings` containing a table with columns `Severity | Category | Location | Issue | Recommendation`; include one row per finding and use `file:line` for the Location column. -->
<!-- TODO: - `## Overall Verdict` with a single-line decision such as `:white_check_mark: Approve` or `:x: Request changes`. -->
<!-- TODO: Wrap all code snippets in fenced blocks labelled with appropriate language hints (for example, \`\`\`python). -->
</output_format>
<!-- TEMPLATE END -->

/*******************************************************************************
 *  YOUR TEMPLATE ENDS HERE
 *  
 *  Next step: Test it!
 *  Go to: 3.2-code-review-automation.ipynb
 *  Run: test_activity_3_2(test_code="...", variables={...})
 ******************************************************************************/
````

---

### Step 4: Test Your Template

---

**🧪 Test in Notebook:**

Open `3.2-code-review-automation.ipynb` and run:

```python
# Test with the authentication code vulnerability
test_code = """
+ import hashlib
+ import time
+
+ SESSION_CACHE = {}
+
+ def authenticate_user(db, username, password):
+     username = username or ""
+     password = password or ""
+
+     query = f"SELECT id, password_hash, failed_attempts FROM users WHERE username = '{username}'"
+     rows = db.execute(query)
+     user = rows[0]
+
+     hashed = hashlib.md5(password.encode()).hexdigest()
+
+     if hashed != user["password_hash"]:
+         db.execute(f"UPDATE users SET failed_attempts = {user['failed_attempts'] + 1} WHERE id = {user['id']}")
+         return {"status": "error"}
+
+     if username not in SESSION_CACHE:
+         SESSION_CACHE[username] = f"{user['id']}-{int(time.time())}"
+
+     permissions = []
+     for role in db.fetch_roles():
+         if db.has_role(user["id"], role["id"]):
+             permissions.append(role["name"])
+
+     time.sleep(0.5)
+     db.write_audit_entry(user["id"], username)
+
+     return {"status": "ok", "session": SESSION_CACHE[username], "permissions": permissions}
"""
 
 test_activity_3_2(
     test_code=test_code,
     variables={
         'tech_stack': 'Python',
         'repo_name': 'user-auth-service',
         'service_name': 'Authentication API',
         'change_purpose': 'Add user login endpoint'
     }
 )
 ```
 
 **Your template's output:**
 <!-- TEST RESULT -->
 ```
 [Results will be automatically saved here when you test]
 ```
 <!-- TEST RESULT END -->
 
**Self-Check:**
- [ ] Did it identify security issues (SQL injection, weak hashing, predictable tokens)?
- [ ] Did it flag performance or scalability problems (blocking sleeps, N+1 queries, unnecessary work)?
- [ ] Did it call out maintainability concerns (global state, missing resource cleanup, lack of separation of concerns)?
- [ ] Did it note robustness or testing gaps (silent failures, missing validation, error handling)?
- [ ] Did it provide actionable fixes with severity levels and clear categories?
- [ ] Is the review output well-structured and easy for engineers to follow?

## ✅ Self-Assessment Checklist

Before considering this activity complete, verify:

- [ ] My template reviews multiple dimensions (security, performance, quality)
- [ ] My template identifies common issues in the test code
- [ ] Each finding includes severity rating and category
- [ ] Each finding suggests a concrete fix
- [ ] Output is well-structured and readable
- [ ] Template uses parameterization ({{variables}})
- [ ] I tested with the provided code sample
- [ ] I drew inspiration from AWS patterns without over-complicating

---

## 🚀 Next Steps

### Compare with Solution
Once you're satisfied with your template, compare it with the official solution:  
📖 [`solutions/activity-3.2-code-review-solution.md`](../solutions/activity-3.2-code-review-solution.md)

### Keep Iterating
- Save a copy of your finished template in your repo (for example, `prompts/code-review-template.xml`) so you can reuse and improve it.
- Drop it into your pull-request workflow or CI pipeline and tweak it as you gather feedback from teammates.
- Start a changelog for prompt revisions—treat it like any other piece of your development toolkit.

### Reflect
What did you learn?
```
1. 

2. 

3. 
```

### Continue Learning
Return to `3.3-test-generation-automation.ipynb` to continue with **Section 2: Test Generation**

---

## 💡 Need Help?

**Common Issues:**

| Problem | Solution |
|---------|----------|
| Template too generic | Add specific checks for each dimension (security, performance, quality) |
| Missing issues | Review AWS patterns - what dimensions do they cover? Be systematic. |
| Output not structured | Use explicit section markers in your `<output_format>` block |
| No severity levels | Define clear criteria: CRITICAL (security/data loss), MAJOR (bugs), MINOR (quality) |

**Still stuck?** Check the solution file for guidance, but try to solve it yourself first!

---

**📅 Completed on:** ___________  
**⏱️ Time taken:** ___________ minutes

---

## 🎓 Learning Notes

Use this space to capture key insights:

```
What worked well in my template:


What I would improve:


How I'll apply this to my projects:


```
