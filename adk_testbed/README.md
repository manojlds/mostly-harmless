# ADK testbed (local-only)

This folder is a self-contained ADK testbed for experimenting with agent
behavior and evaluation locally. It uses a simple agent with one tool call and
a `.test.json` evaluation file that mirrors the ADK evaluation format.

## Setup

```bash
cd adk_testbed
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Configure credentials

This testbed targets the `opencode/zen-glm-4.7-free` model in `agent.py`. The
agent expects an OpenCode-compatible API key in `OPENCODE_ZEN_API_KEY`, and
the OpenAI-compatible base URL set to the OpenCode endpoint.

If you keep secrets in a file, create a `.env` in this directory and load it
before running ADK commands.

```bash
export OPENCODE_ZEN_API_KEY="your-key"
export OPENAI_API_KEY="$OPENCODE_ZEN_API_KEY"
export OPENAI_BASE_URL="https://opencode.ai/zen/v1"
# Some OpenAI-compatible clients use OPENAI_API_BASE instead.
export OPENAI_API_BASE="https://opencode.ai/zen/v1"
```

## Run the agent (CLI)

```bash
cd adk_testbed
uv run adk run .
```

## Run the evaluation (pytest)

```bash
cd adk_testbed
uv run pytest tests/test_eval.py
```

## Evaluate configuration

The evaluation fixtures live in `evals/`:

- `evals/simple_time.test.json`: single-session test case

The test runner uses `AgentEvaluator.evaluate()` from ADK to execute the evals.
With no `test_config.json`, ADK uses its default criteria, which include tool
trajectory matching and response match scoring.

## Creating new eval files

To add a new test, copy `evals/simple_time.test.json` and update the values:

1. Set `eval_set_id` and `eval_id` to new identifiers.
2. Update `user_content` to the prompt you want to test.
3. Update `intermediate_data.tool_uses` to the tool calls you expect the agent
   to make.
4. Update `final_response` to the expected answer (used by response matching
   criteria).

You can also use the ADK Web UI to capture a session and save it as an eval
case, then export the JSON into the `evals/` folder.

## Project layout

```
adk_testbed/
  agent.py
  evals/
    simple_time.test.json
  tests/
    test_eval.py
  requirements.txt
```
