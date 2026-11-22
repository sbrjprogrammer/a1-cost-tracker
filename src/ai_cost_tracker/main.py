
import json
from pathlib import Path

from dotenv import load_dotenv

from .gemini_provider import call_gemini
from .groq_provider import call_groq
from .cost_calculator import ProviderResult


load_dotenv()


def print_result(result: ProviderResult):
    print("\n" + "=" * 60)
    print(f"PROVIDER: {result.provider}")
    print(f"MODEL: {result.model}")
    print("=" * 60)

    print("\nAI RESPONSE:")
    print(result.response)

    print("\nUSAGE DETAILS:")
    print(f"Input tokens:  {result.input_tokens}")
    print(f"Output tokens: {result.output_tokens}")
    print(f"Total tokens:  {result.input_tokens + result.output_tokens}")

    input_cost = result.input_tokens * result.input_price / 1_000_000
    output_cost = result.output_tokens * result.output_price / 1_000_000

    print("\nCOST DETAILS:")
    print(f"Input cost: ${input_cost:.8f}")
    print(f"Output cost: ${output_cost:.8f}")
    print(f"Estimated cost: ${result.estimated_cost:.8f}")

    if result.billing_mode.lower() == "free":
        print("Billing status: FREE TIER")
        print("Note: Cost shown is the equivalent at published paid rates.")
    else:
        print("Billing status: PAID RATE ESTIMATE")

    print(f"Response time: {result.latency_seconds:.2f} seconds")
    print("=" * 60)


def save_results(results: list[ProviderResult]):
    output = []

    for result in results:
        provider_name = (
            "gemini" if result.provider == "Google Gemini" else "groq"
        )

        output.append({
            "provider": provider_name,
            "model": result.model,
            "reply": result.response,
            "input_tokens": result.input_tokens,
            "output_tokens": result.output_tokens,
            "input_price_per_m": result.input_price,
            "output_price_per_m": result.output_price,
            "cost_usd": result.estimated_cost
        })

    output_path = Path("results.json")
    output_path.write_text(
        json.dumps(output, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"\nResults saved successfully to: {output_path.resolve()}")


def main():
    print("\nAI TWO PROVIDER COST TRACKER")
    print("=" * 60)

    prompt = input("\nEnter your prompt: ").strip()

    if not prompt:
        print("Error: Prompt cannot be empty.")
        return

    providers = [
        ("Google Gemini", call_gemini),
        ("Groq", call_groq)
    ]

    results = []

    for provider_name, provider_function in providers:
        print(f"\nCalling {provider_name}...")

        try:
            result = provider_function(prompt)
            results.append(result)
            print_result(result)

        except Exception as error:
            print(f"\n{provider_name} API failed:")
            print(error)

    if results:
        print("\nFINAL COMPARISON")
        print("-" * 75)
        print(
            f"{'Provider':<18}"
            f"{'Input':<10}"
            f"{'Output':<10}"
            f"{'Time (s)':<12}"
            f"{'Cost (USD)':<15}"
        )
        print("-" * 75)

        for result in results:
            print(
                f"{result.provider:<18}"
                f"{result.input_tokens:<10}"
                f"{result.output_tokens:<10}"
                f"{result.latency_seconds:<12.2f}"
                f"${result.estimated_cost:<14.8f}"
            )

        print("-" * 75)
        save_results(results)

    else:
        print("\nBoth API calls failed. No results were saved.")

    print("\nCost tracking completed!")


if __name__ == "__main__":
    main()
