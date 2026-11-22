
import os
import time

from groq import Groq

from .cost_calculator import create_provider_result


def call_groq(prompt: str):

    model = os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-20b"
    )

    input_price = float(
        os.getenv("GROQ_INPUT_PRICE", "0.075")
    )

    output_price = float(
        os.getenv("GROQ_OUTPUT_PRICE", "0.30")
    )

    billing_mode = os.getenv(
        "GROQ_BILLING_MODE",
        "paid"
    )

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key or api_key == "your_groq_api_key":
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add your Groq API key to the .env file."
        )

    client = Groq(api_key=api_key)

    start_time = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end_time = time.perf_counter()

    usage = response.usage

    if usage is None:
        raise RuntimeError(
            "Groq did not return token usage metadata."
        )

    input_tokens = usage.prompt_tokens or 0
    output_tokens = usage.completion_tokens or 0

    result = create_provider_result(
        provider="Groq",
        model=model,
        response=response.choices[0].message.content or "",
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_seconds=end_time - start_time,
        input_price=input_price,
        output_price=output_price,
        billing_mode=billing_mode
    )

    return result
