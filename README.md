# AI Two Provider Cost Tracker

A Python application that sends the same prompt to **Google Gemini** and **Groq**, then compares their responses, token usage, estimated API costs, and response times.

The project was created as part of the Agentic AI course assignment.

## Features

- Calls Google Gemini and Groq using their APIs
- Sends the same user prompt to both providers
- Displays each provider's generated response
- Tracks input and output tokens
- Calculates estimated API cost using separate input and output prices
- Measures API response time
- Handles provider API errors independently
- Saves provider results to `results.json`
- Keeps API keys in environment variables

## Technologies

- Python
- [uv](https://docs.astral.sh/uv/)
- Google GenAI SDK
- Groq SDK
- python-dotenv
- JSON

## Project Structure

```text
ai-cost-tracker/
├── tracker.py
├── main.py
├── results.json
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── ai_cost_tracker/
│       ├── __init__.py
│       ├── main.py
│       ├── gemini_provider.py
│       ├── groq_provider.py
│       └── cost_calculator.py
└── tests/
    └── test_main.py
```

## Requirements

- Python 3.14 or a compatible version supported by the project
- uv
- Gemini API key
- Groq API key

## Installation

Clone the repository:

```bash
git clone https://github.com/sbrjprogrammer/a1-cost-tracker.git
cd a1-cost-tracker
```

Install the project dependencies:

```bash
uv sync
```

## Environment Setup

Create a `.env` file in the project root by copying `.env.example`.

```bash
cp .env.example .env
```

Open `.env` and add your own API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key

GEMINI_MODEL=gemini-3.5-flash-lite
GROQ_MODEL=openai/gpt-oss-20b

GEMINI_INPUT_PRICE=0.30
GEMINI_OUTPUT_PRICE=2.50

GROQ_INPUT_PRICE=0.075
GROQ_OUTPUT_PRICE=0.30

GEMINI_BILLING_MODE=free
GROQ_BILLING_MODE=paid
```

**Security:** Never commit or upload your `.env` file. The file is excluded through `.gitignore`. Use `.env.example` to document the required environment variables without exposing API keys.

## Run the Application

Run the tracker from the project root:

```bash
uv run tracker.py
```

Enter a prompt when requested. The application sends it to both providers and displays their responses, token usage, estimated costs, and response times.

After the API calls, the results are saved automatically to:

```text
results.json
```

## Cost Calculation

The tracker calculates costs using the following formulas:

```text
Input Cost = Input Tokens × Input Price per Million / 1,000,000

Output Cost = Output Tokens × Output Price per Million / 1,000,000

Total Cost = Input Cost + Output Cost
```

The displayed cost is an estimate based on the configured price per million tokens. For free-tier API usage, it represents the equivalent cost at the configured published rates, not necessarily an amount charged to the account.

## Sample Output

Example comparison from a successful run:

```text
FINAL COMPARISON
---------------------------------------------------------------------------
Provider          Input     Output    Time (s)    Cost (USD)
---------------------------------------------------------------------------
Google Gemini     4         510       3.31        $0.00127620
Groq              74        898       1.55        $0.00027495
---------------------------------------------------------------------------
```

Token counts, response times, and costs vary depending on the prompt and API response. The complete provider results are saved in `results.json`.

## Tests

Run the unit tests:

```bash
uv run python -m unittest discover -s tests -v
```

The tests cover cost calculation, zero-token costs, negative values, and invalid price values.

## What I Learned

I learned how to integrate two LLM providers into one Python application and compare their token usage and estimated costs. I also practiced using environment variables to protect API keys, measuring API response time, handling API errors, and saving structured results in JSON.

## Author

Shahzaib Siraj

GitHub: [sbrjprogrammer](https://github.com/sbrjprogrammer)
