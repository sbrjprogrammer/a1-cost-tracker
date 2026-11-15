# # prices per 1M tokens, example values only
# prices = {"input": 0.10, "output": 0.40}

# def cost(tokens, price_per_million):
#     return tokens * price_per_million / 1_000_000

# total = cost(2000, prices["input"]) + cost(500, prices["output"])
# print(f"Cost per call: ${total:.6f}")

# Output= Cost per call: $0.000400

# prices per 1M tokens, example values only
prices = {
    "input": 0.10,
    "output": 0.40
}

def cost(tokens, price_per_million):
    return tokens * price_per_million / 1_000_000


total = cost(2000, prices["input"]) + cost(500, prices["output"])

print(f"Cost per call: ${total:.6f}")