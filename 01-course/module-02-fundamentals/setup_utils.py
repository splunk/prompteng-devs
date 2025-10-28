"""
Module 2: Shared setup utilities
--------------------------------
Provides a single place to configure AI providers and helper functions that
each notebook can import. Mirrors the Module 3 helper style while keeping the
surface area focused on the tactics taught in this module.
"""

from __future__ import annotations

import base64
import os
from pathlib import Path
from typing import Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

import anthropic
import openai

try:
    import requests
except ImportError:  # pragma: no cover - requests is part of requirements but guard just in case
    requests = None  # type: ignore


# ============================================
# 🎯 PROVIDER CONFIGURATION
# ============================================

AVAILABLE_PROVIDERS: Tuple[str, ...] = ("openai", "claude", "circuit")

# Default provider can be overridden via environment variable
PROVIDER: str = os.getenv("MODULE2_PROVIDER", "claude").lower()

# Default models per provider (customisable via environment variables)
OPENAI_DEFAULT_MODEL: str = os.getenv("MODULE2_OPENAI_MODEL", "gpt-5")
CLAUDE_DEFAULT_MODEL: str = os.getenv("MODULE2_CLAUDE_MODEL", "claude-sonnet-4")
CIRCUIT_DEFAULT_MODEL: str = os.getenv("MODULE2_CIRCUIT_MODEL", "gpt-4o")

# GitHub Copilot proxy defaults (Option A)
_OPENAI_BASE_URL = os.getenv("MODULE2_OPENAI_BASE_URL", "http://localhost:7711/v1")
_CLAUDE_BASE_URL = os.getenv("MODULE2_CLAUDE_BASE_URL", "http://localhost:7711")
_PROXY_API_KEY = os.getenv("MODULE2_PROXY_API_KEY", "dummy-key")

openai_client: openai.OpenAI = openai.OpenAI(
    base_url=_OPENAI_BASE_URL,
    api_key=_PROXY_API_KEY,
)

claude_client: anthropic.Anthropic = anthropic.Anthropic(
    base_url=_CLAUDE_BASE_URL,
    api_key=_PROXY_API_KEY,
)

circuit_client: Optional["openai.AzureOpenAI"] = None
circuit_app_key: Optional[str] = None


# ============================================
# 🔧 OPTIONAL CONFIG HELPERS
# ============================================

def configure_openai_from_env(api_key_env: str = "OPENAI_API_KEY") -> openai.OpenAI:
    """
    Configure the OpenAI client directly using an API key from the environment.

    1. Add your key to `.env` (or export it in your shell)
    2. Run `configure_openai_from_env()` in a notebook cell
    3. Optionally call `set_provider("openai")` if you want to switch providers
    """
    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError as exc:  # pragma: no cover - dotenv is in requirements but guard just in case
        raise RuntimeError("python-dotenv is required for configure_openai_from_env") from exc

    load_dotenv()
    api_key = os.getenv(api_key_env)
    if not api_key:
        raise RuntimeError(
            f"Environment variable '{api_key_env}' not set. "
            "Add it to your .env file or export it in your shell."
        )

    global openai_client
    openai_client = openai.OpenAI(api_key=api_key)
    return openai_client


def configure_circuit_from_env() -> "openai.AzureOpenAI":
    """
    Configure CircuIT (Azure OpenAI) access using the environment variables:

    - CISCO_CLIENT_ID
    - CISCO_CLIENT_SECRET
    - CISCO_OPENAI_APP_KEY

    These values can be generated from https://ai-chat.cisco.com/bridgeit-platform/api/home
    """
    if requests is None:
        raise RuntimeError("The 'requests' package is required to configure CircuIT access")

    try:
        from dotenv import load_dotenv  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("python-dotenv is required for configure_circuit_from_env") from exc

    from openai import AzureOpenAI

    load_dotenv()

    client_id = os.getenv("CISCO_CLIENT_ID")
    client_secret = os.getenv("CISCO_CLIENT_SECRET")
    app_key = os.getenv("CISCO_OPENAI_APP_KEY")

    if not client_id or not client_secret or not app_key:
        raise RuntimeError(
            "CISCO_CLIENT_ID, CISCO_CLIENT_SECRET, and CISCO_OPENAI_APP_KEY "
            "must be set in your environment to use CircuIT."
        )

    url = "https://id.cisco.com/oauth2/default/v1/token"
    payload = "grant_type=client_credentials"
    creds = f"{client_id}:{client_secret}".encode("utf-8")
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {base64.b64encode(creds).decode('utf-8')}",
    }

    token_response = requests.post(url, headers=headers, data=payload, timeout=30)
    token_response.raise_for_status()
    token_data = token_response.json()

    client = AzureOpenAI(
        azure_endpoint="https://chat-ai.cisco.com",
        api_key=token_data.get("access_token"),
        api_version="2024-12-01-preview",
    )

    global circuit_client, circuit_app_key
    circuit_client = client
    circuit_app_key = app_key
    return client


# ============================================
# 🤖 COMPLETION HELPERS
# ============================================

def _extract_text_from_blocks(blocks: Iterable) -> str:
    """Extract text content from response blocks returned by Anthropic."""
    parts: List[str] = []
    for block in blocks:
        text_val = getattr(block, "text", None)
        if isinstance(text_val, str):
            parts.append(text_val)
        elif isinstance(block, Mapping):
            text = block.get("text")
            if isinstance(text, str):
                parts.append(text)
    return "\n".join(parts)


def _ensure_messages(messages: Sequence[MutableMapping[str, object]]) -> List[MutableMapping[str, object]]:
    if not isinstance(messages, Sequence):
        raise TypeError("messages must be a sequence of {'role': ..., 'content': ...} dictionaries")
    normalized: List[MutableMapping[str, object]] = []
    for message in messages:
        if not isinstance(message, MutableMapping):
            raise TypeError("Each message must be a dict-like object")
        if "role" not in message or "content" not in message:
            raise ValueError("Each message must contain 'role' and 'content' keys")
        normalized.append(message)  # shallow copy is fine
    return normalized


def get_provider() -> str:
    """Return the currently configured provider."""
    return PROVIDER


def set_provider(provider_name: str) -> str:
    """Set the active provider for requests."""
    provider_normalized = provider_name.lower()
    if provider_normalized not in AVAILABLE_PROVIDERS:
        raise ValueError(f"Unknown provider '{provider_name}'. Choose from {AVAILABLE_PROVIDERS}.")
    global PROVIDER
    PROVIDER = provider_normalized
    return PROVIDER


def get_default_model(provider: Optional[str] = None) -> str:
    """Get the default model for the given provider (or the active provider)."""
    provider = (provider or PROVIDER).lower()
    if provider == "claude":
        return CLAUDE_DEFAULT_MODEL
    if provider == "circuit":
        return CIRCUIT_DEFAULT_MODEL
    return OPENAI_DEFAULT_MODEL


def get_openai_completion(
    messages: Sequence[MutableMapping[str, object]],
    model: Optional[str] = None,
    temperature: float = 0.0,
) -> str:
    """Get a chat completion from OpenAI (GitHub Copilot proxy or direct)."""
    if openai_client is None:
        raise RuntimeError("OpenAI client is not configured. Run configure_openai_from_env() first.")

    cleaned_messages = _ensure_messages(messages)
    response = openai_client.chat.completions.create(
        model=model or get_default_model("openai"),
        messages=cleaned_messages,
        temperature=temperature,
    )
    return response.choices[0].message.content or ""


def get_claude_completion(
    messages: Sequence[MutableMapping[str, object]],
    model: Optional[str] = None,
    temperature: float = 0.0,
) -> str:
    """Get a chat completion from Claude (via GitHub Copilot proxy)."""
    if claude_client is None:
        raise RuntimeError("Claude client is not configured.")

    cleaned_messages = _ensure_messages(messages)
    response = claude_client.messages.create(
        model=model or get_default_model("claude"),
        max_tokens=8192,
        messages=cleaned_messages,
        temperature=temperature,
    )
    return _extract_text_from_blocks(getattr(response, "content", []))


def get_circuit_completion(
    messages: Sequence[MutableMapping[str, object]],
    model: Optional[str] = None,
    temperature: float = 0.0,
) -> str:
    """Get a chat completion from CircuIT (Azure OpenAI)."""
    if circuit_client is None or circuit_app_key is None:
        raise RuntimeError(
            "CircuIT client not configured. Call configure_circuit_from_env() and set_provider('circuit')."
        )

    cleaned_messages = _ensure_messages(messages)
    response = circuit_client.chat.completions.create(
        model=model or get_default_model("circuit"),
        messages=cleaned_messages,
        temperature=temperature,
        user=f'{{"appkey": "{circuit_app_key}"}}',
    )
    return response.choices[0].message.content or ""


def get_chat_completion(
    messages: Sequence[MutableMapping[str, object]],
    model: Optional[str] = None,
    temperature: float = 0.0,
) -> str:
    """Route to the correct provider-specific completion helper."""
    provider = PROVIDER.lower()
    if provider == "claude":
        return get_claude_completion(messages, model, temperature)
    if provider == "circuit":
        return get_circuit_completion(messages, model, temperature)
    return get_openai_completion(messages, model, temperature)


# ============================================
# 🧪 CONNECTION TEST
# ============================================

def test_connection(
    expected_phrase: str = "Module 2 setup verified! Ready to learn core techniques.",
    temperature: float = 0.0,
) -> Tuple[bool, str]:
    """
    Run a simple round-trip request to confirm connectivity.

    Returns:
        tuple (success: bool, response: str)
    """
    messages = [
        {
            "role": "system",
            "content": "You are a prompt engineering instructor.",
        },
        {
            "role": "user",
            "content": f"Respond with exactly: '{expected_phrase}'",
        },
    ]

    response = get_chat_completion(messages, temperature=temperature)
    normalized = response.lower() if response else ""
    success = expected_phrase.lower() in normalized

    print("🧪 Connection Test")
    print(f"🤖 Provider: {PROVIDER.upper()} (model: {get_default_model()})")
    print(f"📝 Response: {response}")
    if success:
        print("✅ Connection looks good!")
    else:
        print("⚠️ Unexpected response. Double-check your provider configuration.")

    return success, response


# ============================================
# 🔖 MISC HELPERS
# ============================================

def read_markdown(path: str | Path) -> str:
    """Convenience helper: read a markdown file as text."""
    file_path = Path(path)
    return file_path.read_text()


def save_markdown(path: str | Path, content: str) -> None:
    """Save text to a markdown file."""
    file_path = Path(path)
    file_path.write_text(content)


# ============================================
# 📊 PROMPT EVALUATION (Traditional Metrics + LLM-as-Judge)
# ============================================

def _calculate_traditional_metrics(
    messages: Sequence[MutableMapping[str, object]],
    expected_tactics: Sequence[str],
) -> Mapping[str, object]:
    """
    Calculate objective, quantitative metrics for prompt evaluation.

    Returns:
        Dictionary with metric scores and evidence
    """
    prompt_text = str(messages)
    metrics = {}

    # 1. Structure Detection
    has_system_message = any(msg.get("role") == "system" for msg in messages)
    metrics["has_system_message"] = has_system_message

    # 2. XML Tag Detection (for structured inputs)
    xml_tags = []
    common_tags = ["code", "requirements", "context", "example", "document", "thinking", "output",
                   "test_file", "source_code", "analysis", "quotes", "evaluation"]
    for tag in common_tags:
        if f"<{tag}>" in prompt_text.lower():
            xml_tags.append(tag)
    metrics["xml_tags_found"] = xml_tags
    metrics["uses_xml_structure"] = len(xml_tags) > 0

    # 3. Few-Shot Pattern Detection
    assistant_messages = [msg for msg in messages if msg.get("role") == "assistant"]
    metrics["example_count"] = len(assistant_messages)
    metrics["uses_few_shot"] = len(assistant_messages) >= 2

    # 4. Chain-of-Thought Keywords
    cot_keywords = ["step-by-step", "think through", "reasoning", "analyze", "before", "first", "then"]
    cot_found = [kw for kw in cot_keywords if kw in prompt_text.lower()]
    metrics["cot_keywords_found"] = cot_found
    metrics["uses_cot"] = len(cot_found) > 0

    # 5. Role Prompting Detection
    role_indicators = ["you are a", "you are an", "act as", "role:", "persona:"]
    role_found = [ind for ind in role_indicators if ind in prompt_text.lower()]
    metrics["role_indicators"] = role_found
    metrics["uses_role_prompting"] = len(role_found) > 0

    # 6. Tree of Thoughts Detection (multiple approaches/alternatives)
    tot_keywords = ["approach a", "approach b", "approach c", "alternative", "option 1", "option 2", "multiple approaches", "different solutions"]
    tot_tags = ["<approach_a>", "<approach_b>", "<approach_c>", "<option_1>", "<option_2>", "<alternative_"]
    tot_found = [kw for kw in tot_keywords if kw in prompt_text.lower()]
    tot_tags_found = [tag for tag in tot_tags if tag in prompt_text.lower()]
    metrics["tot_keywords_found"] = tot_found + tot_tags_found
    metrics["uses_tree_of_thoughts"] = len(tot_found) >= 2 or len(tot_tags_found) >= 2  # At least 2 approaches

    # 7. LLM-as-Judge Detection (evaluation rubrics, scoring, weighted criteria)
    judge_keywords = ["rubric", "evaluate", "score", "rate", "criteria", "weighted", "judge", "assessment", "compare", "0-10", "1-10"]
    judge_found = [kw for kw in judge_keywords if kw in prompt_text.lower()]
    has_percentages = "%" in prompt_text  # Weighted criteria like "40%", "30%"
    metrics["judge_keywords_found"] = judge_found
    metrics["uses_llm_as_judge"] = len(judge_found) >= 3 or (len(judge_found) >= 2 and has_percentages)

    # 8. Document Structure Detection (for citations)
    has_doc_structure = "<documents>" in prompt_text.lower() or "<document>" in prompt_text.lower()
    has_source_tags = "<source>" in prompt_text.lower()
    metrics["uses_document_structure"] = has_doc_structure and has_source_tags

    # 9. Prompt Length Analysis
    total_chars = len(prompt_text)
    metrics["total_characters"] = total_chars
    metrics["complexity"] = "high" if total_chars > 1000 else "medium" if total_chars > 300 else "low"

    return metrics


def evaluate_prompt(
    messages: Sequence[MutableMapping[str, object]],
    activity_name: str,
    expected_tactics: Sequence[str],
) -> str:
    """
    Evaluate a student's prompt using Traditional Metrics + LLM-as-Judge.

    This function provides comprehensive automated feedback by combining:
    1. Traditional eval metrics (objective, fast, deterministic)
    2. LLM-as-Judge (subjective, nuanced, educational)

    Args:
        messages: The student's prompt (list of message dictionaries)
        activity_name: Name of the activity (e.g., "Activity 2.1")
        expected_tactics: List of tactics that should be present
                         (e.g., ["Role Prompting", "Structured Inputs"])

    Returns:
        String containing the full evaluation with metrics, feedback, and skill recommendations

    Example:
        >>> messages = [
        ...     {"role": "system", "content": "You are a QA engineer..."},
        ...     {"role": "user", "content": "<test_file>...</test_file>"}
        ... ]
        >>> evaluate_prompt(
        ...     messages=messages,
        ...     activity_name="Activity 2.1",
        ...     expected_tactics=["Role Prompting", "Structured Inputs"]
        ... )
    """

    # STEP 1: Calculate Traditional Metrics (Fast & Objective)
    metrics = _calculate_traditional_metrics(messages, expected_tactics)

    # Convert messages to string for LLM analysis
    prompt_text = str(messages)

    # STEP 2: Format Traditional Metrics for Display
    xml_tags = metrics.get('xml_tags_found', [])
    cot_keywords = metrics.get('cot_keywords_found', [])
    role_indicators = metrics.get('role_indicators', [])
    complexity = str(metrics.get('complexity', 'unknown'))

    tot_keywords = metrics.get('tot_keywords_found', [])
    judge_keywords = metrics.get('judge_keywords_found', [])

    metrics_summary = f"""
📏 TRADITIONAL EVAL METRICS (Objective Analysis)
{'=' * 70}

**Structure Analysis:**
- Has system message: {'✅ Yes' if metrics.get('has_system_message') else '❌ No'}
- XML tags detected: {', '.join(xml_tags) if xml_tags else 'None'}
- Uses structured inputs: {'✅ Yes' if metrics.get('uses_xml_structure') else '❌ No'}

**Tactic Detection:**
- Few-shot examples: {metrics.get('example_count', 0)} examples {'✅' if metrics.get('uses_few_shot') else '❌'}
- Chain-of-thought keywords: {', '.join(cot_keywords) if cot_keywords else 'None'} {'✅' if metrics.get('uses_cot') else '❌'}
- Role indicators: {', '.join(role_indicators) if role_indicators else 'None'} {'✅' if metrics.get('uses_role_prompting') else '❌'}
- Tree of Thoughts indicators: {', '.join(tot_keywords) if tot_keywords else 'None'} {'✅' if metrics.get('uses_tree_of_thoughts') else '❌'}
- LLM-as-Judge indicators: {', '.join(judge_keywords) if judge_keywords else 'None'} {'✅' if metrics.get('uses_llm_as_judge') else '❌'}
- Document structure: {'✅ Yes' if metrics.get('uses_document_structure') else '❌ No'}

**Complexity:**
- Total characters: {metrics.get('total_characters', 0)}
- Complexity level: {complexity.upper()}

{'=' * 70}
"""

    # Build tactic descriptions dynamically based on expected_tactics
    tactic_descriptions = {
        "Role Prompting": "Check for specific, relevant persona with clear expertise domain",
        "Structured Inputs": "Check for meaningful organization and clear section boundaries",
        "Few-Shot Examples": "Check for high-quality examples that teach the desired pattern",
        "Chain-of-Thought": "Check for systematic reasoning instructions",
        "Reference Citations": "Check for proper document structure and quote extraction",
        "Prompt Chaining": "Check for multi-step workflow with clear dependencies",
        "LLM-as-Judge": "Check for clear evaluation rubrics and weighted criteria",
        "Tree of Thoughts": "Check for exploring multiple solution approaches/alternatives in parallel"
    }

    # Only include expected tactics in the evaluation criteria
    criteria_list = []
    for i, tactic in enumerate(expected_tactics, 1):
        if tactic in tactic_descriptions:
            criteria_list.append(f"{i}. **{tactic}**: {tactic_descriptions[tactic]}")

    criteria_text = "\n".join(criteria_list)

    # STEP 3: LLM-as-Judge Evaluation (Subjective & Nuanced)
    evaluation_prompt = f"""You are an expert prompt engineering instructor evaluating a student's work.

<traditional_metrics>
{metrics_summary}
</traditional_metrics>

<student_prompt>
{prompt_text}
</student_prompt>

<expected_tactics>
{', '.join(expected_tactics)}
</expected_tactics>

<evaluation_criteria>
The traditional metrics above show WHAT patterns exist. Your job as LLM-as-Judge is to evaluate HOW WELL they're implemented.

Analyze whether the student successfully applied ONLY THE EXPECTED TACTICS listed above:

{criteria_text}

IMPORTANT: Only evaluate the tactics listed above. Do not evaluate other tactics that are not in the expected list.

Use the traditional metrics as a starting point, but evaluate the QUALITY and EFFECTIVENESS of implementation.
</evaluation_criteria>

For each expected tactic (and ONLY the expected tactics), provide:
- ✅ if well-implemented (8-10/10 quality) with specific evidence
- ⚠️ if partially implemented (5-7/10 quality) with constructive suggestions
- ❌ if missing or poorly done (0-4/10 quality) with clear explanation

Format your response as:

<evaluation>
**Tactic 1 Name**: ✅/⚠️/❌ (Quality Score: X/10)
Evidence: [Quote specific parts showing implementation]
Quality Assessment: [Why this score? What's good/bad?]
Improvement Suggestions: [Specific actionable advice if not perfect]

**Tactic 2 Name**: ✅/⚠️/❌ (Quality Score: X/10)
Evidence: [Quote specific parts]
Quality Assessment: [Analysis]
Improvement Suggestions: [Advice]
</evaluation>

<skills_demonstrated>
List the specific skills (from Module 2 Skills Checklist) they can check off.

Activity skill mappings:
- Activity 2.1 (Role Prompting + Structured Inputs): Skills #1-4
- Activity 2.2 (Few-Shot + Chain-of-Thought): Skills #5-8
- Activity 2.3 (Reference Citations + Prompt Chaining): Skills #9-12
- Activity 2.4 (Tree of Thoughts + LLM-as-Judge): Skills #13-16

Based on the activity name and tactics evaluated, list appropriate skill numbers.
Format: "- Skill #X: [Description that includes the tactic name]"
Only list skills where the tactic received ✅ (8-10/10) or strong ⚠️ (7/10).

IMPORTANT: For Activity 2.4, use skills #13-16 and mention BOTH Tree of Thoughts AND LLM-as-Judge in the descriptions.
</skills_demonstrated>

<combined_score>
Calculate an overall score (0-100) considering both:
- Traditional metrics (40% weight): Presence of correct patterns
- Quality assessment (60% weight): Effectiveness of implementation
Show your calculation.
</combined_score>

<overall_feedback>
2-3 sentences of encouraging, actionable feedback on their prompt quality.
Highlight the strongest aspect and the most important area for improvement.
</overall_feedback>
"""

    # Get LLM-as-Judge evaluation
    evaluation_messages: List[MutableMapping[str, object]] = [{"role": "user", "content": evaluation_prompt}]
    llm_judgment = get_chat_completion(evaluation_messages)

    # STEP 4: Print Combined Results
    print("=" * 70)
    print(f"📊 COMPREHENSIVE EVALUATION: {activity_name}")
    print("=" * 70)
    print(metrics_summary)
    print("\n👨‍⚖️ LLM-AS-JUDGE EVALUATION (Qualitative Analysis)")
    print("=" * 70)
    print(llm_judgment)
    print("\n" + "=" * 70)
    print("💡 Next Steps:")
    print("  1. Review traditional metrics (objective indicators)")
    print("  2. Read LLM judge feedback (quality assessment)")
    print("  3. Check off demonstrated skills in Skills Checklist")
    print("  4. Focus on the top improvement suggestion")
    print("  5. Revise and re-evaluate to see score improvement")
    print("=" * 70)

    return f"{metrics_summary}\n\n{llm_judgment}"


# ============================================
# 📦 MODULE REGISTRATION
# ============================================

__all__ = [
    "AVAILABLE_PROVIDERS",
    "CLAUDE_DEFAULT_MODEL",
    "CIRCUIT_DEFAULT_MODEL",
    "OPENAI_DEFAULT_MODEL",
    "configure_circuit_from_env",
    "configure_openai_from_env",
    "evaluate_prompt",
    "get_chat_completion",
    "get_claude_completion",
    "get_circuit_completion",
    "get_default_model",
    "get_openai_completion",
    "get_provider",
    "read_markdown",
    "save_markdown",
    "set_provider",
    "test_connection",
]

# Allow notebooks to check that setup has been imported
import sys

sys.modules["__module2_setup__"] = sys.modules[__name__]

print("✅ Module 2 setup utilities loaded successfully!")
print(f"🤖 Provider: {get_provider().upper()}")
print(f"📝 Default model: {get_default_model()}")
