import math
import unittest

from ai_cost_tracker.cost_calculator import calculate_cost


class CalculateCostTests(unittest.TestCase):
    def test_cost_uses_separate_input_and_output_prices(self) -> None:
        self.assertAlmostEqual(
            calculate_cost(2_000, 500, 0.10, 0.40),
            0.0004,
        )

    def test_zero_tokens_cost_nothing(self) -> None:
        self.assertEqual(calculate_cost(0, 0, 0.10, 0.40), 0)

    def test_negative_values_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_cost(1, 0, -0.10, 0.40)

    def test_non_finite_prices_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_cost(1, 0, math.inf, 0.40)


if __name__ == "__main__":
    unittest.main()
