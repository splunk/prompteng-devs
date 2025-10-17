"""
Module 3: Shared Setup Utilities
This file contains all setup code to avoid repetition across notebooks.
Run setup once, then import these functions in any notebook.
"""

import openai
import anthropic
import os
import re
from pathlib import Path

# ============================================
# 🎯 CONFIGURATION
# ============================================
# Set your preference: "openai", "claude", or "circuit"
PROVIDER = "claude"

# Available models by provider
OPENAI_DEFAULT_MODEL = "gpt-5"  # Works with OpenAI API, GitHub Copilot
CIRCUIT_DEFAULT_MODEL = "gpt-4o"
CLAUDE_DEFAULT_MODEL = "claude-sonnet-4"

# ============================================
# 🤖 AI CLIENT INITIALIZATION
# ============================================

# OPTION A: GitHub Copilot Proxy (Default - Recommended for Course)
# Use local proxy that routes through GitHub Copilot
# Supports both OpenAI and Claude models via single proxy
openai_client = openai.OpenAI(
    base_url="http://localhost:7711/v1",
    api_key="dummy-key"
)

claude_client = anthropic.Anthropic(
    api_key="dummy-key",
    base_url="http://localhost:7711"
)

# Placeholder for CircuIT client (will be set if Option C is uncommented)
circuit_client = None
circuit_app_key = None

# OPTION B: Direct OpenAI API
# IMPORTANT: Comment out Option A (lines 27-38) before using this option
# Setup: Add your API key to .env file, then uncomment and run
# from dotenv import load_dotenv
# 
# load_dotenv()
# 
# openai_client = openai.OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")  # Set this in your .env file
# )
# 


# OPTION C: CircuIT APIs (Azure OpenAI)
# IMPORTANT: Comment out Option A (lines 27-38) before using this option
# Supported models: gpt-4, gpt-4o (not gpt-5)
# Setup: Configure environment variables in .env file:
#   - CISCO_CLIENT_ID
#   - CISCO_CLIENT_SECRET  
#   - CISCO_OPENAI_APP_KEY
# Get values from: https://ai-chat.cisco.com/bridgeit-platform/api/home
# Then uncomment and run (also change PROVIDER to "circuit" at the top):
# import traceback
# import requests
# import base64
# from dotenv import load_dotenv
# from openai import AzureOpenAI
# 
# # Load environment variables
# load_dotenv()
# 
# # OpenAI version to use
# openai.api_type = "azure"
# openai.api_version = "2024-12-01-preview"
# 
# # Get API_KEY wrapped in token - using environment variables
# client_id = os.getenv("CISCO_CLIENT_ID")
# client_secret = os.getenv("CISCO_CLIENT_SECRET")
# 
# url = "https://id.cisco.com/oauth2/default/v1/token"
# 
# payload = "grant_type=client_credentials"
# value = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")
# headers = {
#     "Accept": "*/*",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Authorization": f"Basic {value}",
# }
# 
# token_response = requests.request("POST", url, headers=headers, data=payload)
# print(token_response.text)
# token_data = token_response.json()
# 
# circuit_client = AzureOpenAI(
#     azure_endpoint="https://chat-ai.cisco.com",
#     api_key=token_data.get("access_token"),
#     api_version="2024-12-01-preview",
# )
# 
# circuit_app_key = os.getenv("CISCO_OPENAI_APP_KEY")
# 
# print("✅ CircuIT API configured successfully!")


# ============================================
# 🔧 HELPER FUNCTIONS
# ============================================

def _extract_text_from_blocks(blocks):
    """Extract text content from response blocks returned by the API."""
    parts = []
    for block in blocks:
        text_val = getattr(block, "text", None)
        if isinstance(text_val, str):
            parts.append(text_val)
        elif isinstance(block, dict):
            t = block.get("text")
            if isinstance(t, str):
                parts.append(t)
    return "\n".join(parts)


def get_openai_completion(messages, model=None, temperature=0.0):
    """Get completion from OpenAI models via GitHub Copilot."""
    if model is None:
        model = OPENAI_DEFAULT_MODEL
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}\n💡 Make sure GitHub Copilot proxy is running on port 7711"


def get_claude_completion(messages, model=None, temperature=0.0):
    """Get completion from Claude models via GitHub Copilot."""
    if model is None:
        model = CLAUDE_DEFAULT_MODEL
    try:
        response = claude_client.messages.create(
            model=model,
            max_tokens=8192,
            messages=messages,
            temperature=temperature
        )
        return _extract_text_from_blocks(getattr(response, "content", []))
    except Exception as e:
        return f"❌ Error: {e}\n💡 Make sure GitHub Copilot proxy is running on port 7711"


def get_circuit_completion(messages, model=None, temperature=0.0):
    """Get completion from CircuIT APIs (Azure OpenAI via Cisco)."""
    if circuit_client is None or circuit_app_key is None:
        return "❌ Error: CircuIT not configured\n💡 Uncomment Option C in setup_utils.py and set your CircuIT credentials"
    
    if model is None:
        model = CIRCUIT_DEFAULT_MODEL
    try:
        response = circuit_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            user=f'{{"appkey": "{circuit_app_key}"}}'  # CircuIT requires app_key in user field
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}\n💡 Check your CircuIT credentials and connection"


def get_chat_completion(messages, model=None, temperature=0.0):
    """
    Generic function to get chat completion from any provider.
    Routes to the appropriate provider-specific function based on PROVIDER setting.
    """
    if PROVIDER.lower() == "claude":
        return get_claude_completion(messages, model, temperature)
    elif PROVIDER.lower() == "circuit":
        return get_circuit_completion(messages, model, temperature)
    else:  # Default to OpenAI
        return get_openai_completion(messages, model, temperature)


def get_default_model():
    """Get the default model for the current provider."""
    if PROVIDER.lower() == "claude":
        return CLAUDE_DEFAULT_MODEL
    elif PROVIDER.lower() == "circuit":
        return CIRCUIT_DEFAULT_MODEL
    else:  # Default to OpenAI
        return OPENAI_DEFAULT_MODEL


# ============================================
# 🧪 ACTIVITY and SOLUTION TESTING FUNCTIONS
# ============================================

def extract_template_from_activity(activity_file):
    """
    Extract the prompt template from an activity markdown file.
    Looks for content between: <!-- TEMPLATE START --> and <!-- TEMPLATE END -->
    
    Args:
        activity_file: Path to the activity .md file
        
    Returns:
        tuple: (template_text, error_message)
    """
    try:
        file_path = Path(activity_file)
        if not file_path.exists():
            return None, f"❌ File not found: {activity_file}"
        
        content = file_path.read_text()
        
        # Extract template between markers
        match = re.search(
            r'<!-- TEMPLATE START -->(.*?)<!-- TEMPLATE END -->',
            content,
            re.DOTALL
        )
        
        if match:
            template = match.group(1).strip()
            # Remove markdown code block markers if present
            # template = re.sub(r'^```\w*\n', '', template)
            # template = re.sub(r'\n```$', '', template)
            return template, None
        else:
            return None, "⚠️ Template markers not found. Make sure your template is between:\n   <!-- TEMPLATE START -->\n   <!-- TEMPLATE END -->"
            
    except Exception as e:
        return None, f"❌ Error reading file: {e}"


def test_activity(activity_file, test_code=None, variables=None, auto_save=True):
    """
    Test your activity template directly from the .md file.
    
    IMPORTANT: Complete your activity template BEFORE running this function!
    - Open the activity file (e.g., 'activities/activity-3.2-code-review.md')
    - Replace all <!-- TODO: ... --> comments with your actual content
    - Fill in role, guidelines, tasks, and output format sections
    - Save the file, then run this test function
    
    Args:
        activity_file: Path to your activity file (e.g., 'activities/activity-3.2-code-review.md')
        test_code: Optional code sample to review (uses example from file if not provided)
        variables: Optional dict of template variables (e.g., {'tech_stack': 'Python', 'repo_name': 'my-app'})
        auto_save: If True, prompts to save result back to activity file
    
    Returns:
        The AI's response
    """
    print("="*70)
    print("🧪 TESTING YOUR ACTIVITY TEMPLATE")
    print("="*70)
    print("\n⚠️  REMINDER: Make sure you've completed your template first!")
    print("   (Replace all <!-- TODO: ... --> comments with actual content)")
    
    # Extract template
    print(f"\n📖 Reading template from: {activity_file}")
    template, error = extract_template_from_activity(activity_file)
    
    if error or template is None:
        print(error if error else "❌ Error: Template extraction failed")
        return None
    
    print("✅ Template loaded successfully!")
    print(f"📏 Template length: {len(template)} characters\n")
    
    # Substitute variables if provided
    if variables:
        print("🔄 Substituting template variables...")
        for key, value in variables.items():
            placeholder = "{{" + key + "}}"
            template = template.replace(placeholder, str(value))
            print(f"   • {placeholder} → {value}")
        print()
    
    # Add test code if provided
    if test_code:
        print("📝 Using provided test code\n")
        # Replace common placeholders
        template = template.replace("{{code_diff}}", test_code)
        template = template.replace("{{code}}", test_code)
        template = template.replace("{{code_sample}}", test_code)
    
    # Execute prompt
    print("🤖 Sending to AI model...")
    print("-"*70)
    
    try:
        messages = [{"role": "user", "content": template}]
        response = get_chat_completion(messages)
        
        # Check if response contains error message
        if response and ("❌ Error" in response or "Error:" in response):
            print("\n" + response)
            print("-"*70)
            print("\n⚠️ AI request failed. Please check:")
            print("   • GitHub Copilot proxy is running (for Option A)")
            print("   • API keys are configured correctly (for Options B/C)")
            print("   • PROVIDER setting matches your active option")
            print("   • Template contains valid content")
            return None
        
        print(response)
        print("-"*70)
        
        # Save result back to activity file
        if auto_save and response:
            print("\n" + "="*70)
            print("📝 SAVE RESULT")
            print("="*70)
            print("⬆️  LOOK AT THE TOP OF YOUR IDE FOR THE INPUT BOX! ⬆️")
            print("    Type 'y' or 'n' in the input field at the top of the screen")
            print("="*70)
            try:
                save_result = input("💾 Save this result to your activity file? (y/n): ")
                if save_result.lower() == 'y':
                    save_test_result(activity_file, test_code, response)
                    print("✅ Result saved to activity file!")
                else:
                    print("⏭️  Result not saved. You can run this test again anytime.")
            except Exception as save_error:
                print(f"⚠️ Could not save result: {save_error}")
        
        return response
        
    except Exception as e:
        print(f"\n❌ Unexpected error during AI request: {e}")
        print("-"*70)
        print("\n💡 Troubleshooting:")
        print("   • Verify your API configuration is correct")
        print("   • Check that template placeholders are properly filled")
        print("   • Ensure your selected provider is available")
        return None


def save_test_result(activity_file, test_code, response):
    """Save test results back to the activity file."""
    file_path = Path(activity_file)
    content = file_path.read_text()
    original_content = content

    # Find the test results section and update it
    timestamp = __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cleaned_response = response.strip()
    result_block = (
        f"<!-- TEST RESULT - Last Updated: {timestamp} -->\n"
        f"{cleaned_response}\n"
        f"<!-- TEST RESULT END -->"
    )
    updated = False

    # Replace existing result or insert after "Your template's output:"
    if '<!-- TEST RESULT' in content:
        content = re.sub(
            r'<!-- TEST RESULT.*?TEST RESULT END -->',
            result_block,
            content,
            flags=re.DOTALL
        )
        updated = True
    else:
        # Find where to insert (after various possible markers)
        patterns = [
            r"(\*\*Your template's output:\*\*\s*```[^\n]*\n)",
            r"(\*\*Output:\*\*\s*```[^\n]*\n)",
            r"(### Test Results\s*\n)"
        ]
        for pattern in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, r'\1' + result_block + '\n', content)
                updated = True
                break

    if not updated:
        # Append a new Test Results section at the end if no markers were found
        append_block = "\n\n### Test Results\n" + result_block + "\n"
        content = content.rstrip() + append_block
        updated = True

    if content == original_content:
        raise RuntimeError("No changes were applied while attempting to save the test result.")

    file_path.write_text(content)


def list_activities():
    """Show available activities to test."""
    activities_dir = Path('activities')
    
    if not activities_dir.exists():
        print("❌ Activities directory not found")
        print("💡 Make sure you're running from the module-03-applications directory")
        return
    
    print("="*70)
    print("📚 AVAILABLE ACTIVITIES")
    print("="*70)
    
    activity_files = sorted(activities_dir.glob('activity-*.md'))
    
    if not activity_files:
        print("⚠️ No activity files found")
        return
    
    for i, file in enumerate(activity_files, 1):
        # Extract title from file
        try:
            content = file.read_text()
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file.name
            
            print(f"{i}. {file.name}")
            print(f"   {title}")
            print()
        except:
            print(f"{i}. {file.name}")
            print()
    
    print("="*70)
    print("💡 Usage: test_activity('activities/activity-3.2-code-review.md')")


# Quick access functions for each activity
def test_activity_3_2(test_code=None, variables=None):
    """
    Quick helper for Activity 3.2: Comprehensive Code Review
    
    IMPORTANT: Complete your template in the activity file BEFORE running this!
    """
    return test_activity('activities/activity-3.2-code-review.md', test_code=test_code, variables=variables)


def test_activity_3_2_solution(test_code=None, variables=None):
    """
    Test the provided solution for Activity 3.2: Comprehensive Code Review
    
    Use this to see how the solution template works before building your own.
    Note: auto_save is disabled for solution files to keep them as clean references.
    """
    return test_activity('solutions/activity-3.2-code-review-solution.md', test_code=test_code, variables=variables, auto_save=False)


def test_activity_3_3(test_code=None, variables=None):
    """
    Quick helper for Activity 3.3: Test Generation
    
    IMPORTANT: Complete your template in the activity file BEFORE running this!
    """
    return test_activity('activities/activity-3.3-test-generation.md', test_code=test_code, variables=variables)


def test_activity_3_3_solution(test_code=None, variables=None):
    """
    Test the provided solution for Activity 3.3: Test Generation
    
    Use this to see how the solution template works before building your own.
    Note: auto_save is disabled for solution files to keep them as clean references.
    """
    return test_activity('solutions/activity-3.3-test-generation-solution.md', test_code=test_code, variables=variables, auto_save=False)


def test_activity_3_1(test_code=None, variables=None):
    """
    Backwards-compatible helper for the former Activity 3.1 (now Activity 3.2).
    """
    print("⚠️ Activity 3.1 has been renumbered to Activity 3.2. Routing to test_activity_3_2().")
    return test_activity_3_2(test_code=test_code, variables=variables)


def test_activity_3_1_solution(test_code=None, variables=None):
    """
    Backwards-compatible helper for the former Activity 3.1 solution (now Activity 3.2).
    """
    print("⚠️ Activity 3.1 solution has been renumbered to Activity 3.2. Routing to test_activity_3_2_solution().")
    return test_activity_3_2_solution(test_code=test_code, variables=variables)


# ============================================
# 🧪 CONNECTION TEST
# ============================================

def test_connection():
    """Test connection to AI services."""
    print("🔄 Testing connection to GitHub Copilot proxy...")
    test_result = get_chat_completion([
        {"role": "user", "content": "Say 'Connection successful!' if you can read this."}
    ])
    
    if test_result and ("successful" in test_result.lower() or "success" in test_result.lower()):
        print(f"✅ Connection successful! Using {PROVIDER.upper()} provider with model: {get_default_model()}")
        print(f"📝 Response: {test_result}")
        return True
    else:
        print("⚠️ Connection test completed but response unexpected:")
        print(f"📝 Response: {test_result}")
        return False


# ============================================
# 📊 MODULE INITIALIZATION
# ============================================

# Mark module as loaded for checking in notebooks
import sys
sys.modules['__module3_setup__'] = sys.modules[__name__]

print("✅ Module 3 setup utilities loaded successfully!")
print(f"🤖 Provider: {PROVIDER.upper()}")
print(f"📝 Default model: {get_default_model()}")
