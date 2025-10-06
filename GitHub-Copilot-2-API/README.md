# GitHub Copilot API Wrapper

Python implementation of a GitHub Copilot API wrapper that provides OpenAI-compatible endpoints. This service acts as an API proxy that can accept requests in multiple formats (OpenAI, Anthropic Claude, Google Gemini) and convert them to work with GitHub Copilot's API.


## Quick Start

### Prerequisites

- Python 3.10 or higher
- GitHub account with Copilot access [How to apply](./Apply_Github_Copilot.en.md)
- Internet connection for authentication, requires normal access to:
   - **Individual**: Default, uses `api.individual.githubcopilot.com`
   - **Business**: Uses `api.business.githubcopilot.com`
   - **Enterprise**: Uses `api.enterprise.githubcopilot.com`

### Installation

We recommend using [uv](https://docs.astral.sh/uv/) for package management:

#### Install uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Alternative: Install using pip
pip install uv
```

#### Download and install dependencies

```bash
# Clone the repository
git clone git@github.com:snehangshu-splunk/copilot-api.git
cd copilot2api

# Install dependencies
uv sync

# Install development dependencies (for testing)
uv sync --dev
```

### Authentication

Before starting the server, you need to authenticate with GitHub:

```bash
# Authenticate with GitHub (personal account)
uv run copilot2api auth

# For business account
uv run copilot2api auth --business

# For enterprise account
uv run copilot2api auth --enterprise

# Force re-authentication
uv run copilot2api auth --force
```

When authenticating for the first time, you will see the following information:
```
Press Ctrl+C to stop the server
Starting Copilot API server...
Starting GitHub device authorization flow...

Please enter the code '14B4-5D82' at:
https://github.com/login/device

Waiting for authorization...
```
You need to copy `https://github.com/login/device` to your browser, then log in to your GitHub account through the browser. This GitHub account should have GitHub Copilot functionality. After authentication is complete, copy '14B4-5D82' in the browser prompt box. This string of numbers is system-generated and may be different each time.

> **Don't copy the code here.** If you copy this, it will only cause your authorization to fail.

After successful device authorization:
- macOS or Linux:
  - In the `$HOME/.config/copilot2api/` directory, you will see the github-token file.
- Windows system:
  - You will find the github-token file in the `C:\Users\<username>\AppData\Roaming\copilot2api\` directory.


This is the key used to log in to GitHub Copilot. The key is `ghu_******`


### Start the Server

```bash
# Start API server (default port 7711)
uv run copilot2api start

# Start with debug mode (shows JSON request/response data)
uv run copilot2api start --debug

# Start on custom port
uv run copilot2api start --port 8080

# Start with verbose logging
uv run copilot2api start --verbose

# Start the service on all ports, default is 127.0.0.1
uv run copilot2api start --host 0.0.0.0
```
After full startup, you will see:

```
Starting Copilot API server...
Authenticated as: <CEC_ID>_cisco
Name: [Your Name at Github]
Fetched VSCode version: 1.102.2
Fetched Copilot Chat version: 0.30.0
 Copilot token obtained successfully!
Auto-detecting account type...
Copilot token auto-refresh scheduled in 1440 seconds
Copilot plan: business
Access type SKU: copilot_for_business_seat_multi_quota
 Account type detected: business
Switching from individual to business
 Copilot API initialized successfully!
⏳ Starting Fetching models from Copilot API...
API URL: https://api.business.githubcopilot.com/models
Account Type: business
✓ Fetching models from Copilot API completed successfully (1.14s)
 Found 29 available models
 Server initialized successfully!

📋 Available Models & Mappings

╭─────────────────────── OPENAI ────────────────────────╮
│                   OPENAI Models                       │
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┓    │
│ ┃ Model Name             ┃    Status    ┃ Vision ┃    │
│ ┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━┩    │
│ │ gpt-3.5-turbo          │ ✅ Available │ ❌ No  │    │
│ │ gpt-3.5-turbo-0613     │ ✅ Available │ ❌ No  │    │
│ │ gpt-4                  │ ✅ Available │ 👁️ Yes │    │
│ │ gpt-4-0125-preview     │ ✅ Available │ ❌ No  │    │
│ │ gpt-4-0613             │ ✅ Available │ ❌ No  │    │
│ │ gpt-4-o-preview        │ ✅ Available │ ❌ No  │    │
│ │ gpt-4.1                │ ✅ Available │ ❌ No  │    │
│ │ gpt-4.1-2025-04-14     │ ✅ Available │ ❌ No  │    │
│ │ gpt-4o                 │ ✅ Available │ 👁️ Yes │    │
│ │ gpt-4o-2024-05-13      │ ✅ Available │ ❌ No  │    │
│ │ gpt-4o-2024-08-06      │ ✅ Available │ ❌ No  │    │
│ │ gpt-4o-2024-11-20      │ ✅ Available │ ❌ No  │    │
│ │ gpt-4o-mini            │ ✅ Available │ ❌ No  │    │
│ │ gpt-4o-mini-2024-07-18 │ ✅ Available │ ❌ No  │    │
│ │ o3-mini                │ ✅ Available │ ❌ No  │    │
│ │ o3-mini-2025-01-31     │ ✅ Available │ ❌ No  │    │
│ │ o4-mini                │ ✅ Available │ 👁️ Yes │    │
│ │ o4-mini-2025-04-16     │ ✅ Available │ ❌ No  │    │
│ └────────────────────────┴──────────────┴────────┘    │
╰───────────────────────────────────────────────────────╯
╭────────────────────── ANTHROPIC ──────────────────────╮
│                   ANTHROPIC Models                    │
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┓ │
│ ┃ Model Name                ┃    Status    ┃ Vision ┃ │
│ ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━┩ │
│ │ claude-3.5-sonnet         │ ✅ Available │ 👁️ Yes │ │
│ │ claude-3.7-sonnet         │ ✅ Available │ 👁️ Yes │ │
│ │ claude-3.7-sonnet-thought │ ✅ Available │ 👁️ Yes │ │
│ │ claude-sonnet-4           │ ✅ Available │ 👁️ Yes │ │
│ └───────────────────────────┴──────────────┴────────┘ │
╰───────────────────────────────────────────────────────╯
╭─────────────────────── GOOGLE ────────────────────────╮
│                  GOOGLE Models                        │
│ ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━┓      │
│ ┃ Model Name           ┃    Status    ┃ Vision ┃      │
│ ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━┩      │
│ │ gemini-2.0-flash-001 │ ✅ Available │ 👁️ Yes │      │
│ │ gemini-2.5-pro       │ ✅ Available │ 👁️ Yes │      │
│ └──────────────────────┴──────────────┴────────┘      │
╰───────────────────────────────────────────────────────╯

🔄 Model Aliases & Transformations
          OpenAI Model Mappings
┏━━━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━━━┓
┃ Requested Model ┃  →  ┃ Actual Model  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━━━━━━━━┩
│ gpt-3.5         │  →  │ gpt-3.5-turbo │
│ gpt-4           │  →  │ gpt-4o        │
└─────────────────┴─────┴───────────────┘

               Anthropic Model Mappings
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Requested Model          ┃  →  ┃ Actual Model      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ claude                   │  →  │ claude-3.5-sonnet │
│ claude-4                 │  →  │ claude-sonnet-4   │
│ claude-sonnet            │  →  │ claude-3.5-sonnet │
│ claude-sonnet-4-20250514 │  →  │ claude-sonnet-4   │
└──────────────────────────┴─────┴───────────────────┘

             Google Model Mappings
┏━━━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Requested Model ┃  →  ┃ Actual Model         ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ gemini          │  →  │ gemini-2.0-flash-001 │
│ gemini-flash    │  →  │ gemini-2.0-flash-001 │
│ gemini-pro      │  →  │ gemini-2.5-pro       │
└─────────────────┴─────┴──────────────────────┘
```


## 📚 Usage Examples

### OpenAI Format

```python
import openai

# Configure client to use your local server
client = openai.OpenAI(
    api_key="dummy-key",
    base_url="http://localhost:7711/v1"
)

# Chat completion
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)

# Streaming response
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Text embeddings
embeddings = client.embeddings.create(
    model="text-embedding-ada-002",
    input="Hello world"
)

print(embeddings.data[0].embedding)
```

### Anthropic Claude Format

```python
import anthropic

# Configure client to use your local server
client = anthropic.Anthropic(
    api_key="dummy-key",
    base_url="http://localhost:7711"
)

# Create message
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)

# Streaming response
stream = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Tell me a joke"}],
    stream=True
)

for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text, end="")
```

### Google Gemini Format

```python
import google.generativeai as genai

# Configure to use local server
genai.configure(
    api_key="dummy-key",
    transport="rest",
    client_options={"api_endpoint": "http://localhost:7711"}
)

# Generate content
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Write a haiku about programming")

print(response.text)

# Chat conversation
chat = model.start_chat()
response = chat.send_message("Hello!")
print(response.text)
```

### cURL Examples

```bash
# OpenAI format
curl -X POST http://localhost:7711/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy-key" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'

# Anthropic format
curl -X POST http://localhost:7711/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: dummy-key" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "Hello!"}]
  }'

# Embeddings
curl -X POST http://localhost:7711/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer dummy-key" \
  -d '{
    "model": "text-embedding-ada-002",
    "input": "Hello world"
  }'
```
## Other Test Examples

The project includes comprehensive testing for all supported API formats:

```bash
# Run individual SDK tests
python test/test_openai_sdk.py
python test/test_claude_sdk.py
python test/test_gemini_sdk.py

# Test model functionality
python test/test_model_functionality.py

# Test embeddings
python test/test_embeddings_openai_sdk.py
```

## 🛠 API Endpoints

| Endpoint | Method | Description | Format |
|----------|--------|-------------|--------|
| `/` | GET | Server status | - |
| `/user` | GET | Authenticated user info | - |
| `/usage` | GET | Copilot usage info | - |
| `/v1/models` | GET | Available models | OpenAI |
| `/v1/chat/completions` | POST | Chat completions | OpenAI |
| `/v1/messages` | POST | Messages | Anthropic |
| `/v1/embeddings` | POST | Text embeddings | OpenAI |

## ⚙ Configuration

### Command Line Options

#### Authentication (`copilot2api auth`)

```bash
--verbose, -v    Enable verbose logging
--force, -f      Force re-authentication
--business       Use business GitHub account
--enterprise     Use enterprise GitHub account
```

#### Server (`copilot2api start`)

```bash
--port, -p           Port to run server on (default: 7711)
--verbose, -v        Enable verbose logging
--debug, -d          Enable debug mode with JSON logging
--debug-log PATH     Save debug logs to file
--individual         Force individual account type
--business           Force business account type
--enterprise         Force enterprise account type
--manual             Enable manual request approval
--rate-limit, -r N   Rate limit between requests (seconds)
--wait, -w           Wait instead of error when rate limited
--github-token, -g   Provide GitHub token directly
```

### Environment Variables

```bash
DEBUG=true                    # Enable debug mode
DEBUG_LOG_PATH=/path/to/log   # Debug log file path
GH_TOKEN=your_token           # Direct GitHub token (bypasses auth flow)
GITHUB_TOKEN=your_token       # Alternative GitHub token variable
```

## ✨ Features

- **Multi-provider Support**: Compatible with OpenAI, Anthropic/Claude, Google/Gemini

---

⭐ **If you find this repository useful, please give it a star!**