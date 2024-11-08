import unittest
from math_quiz import generate_random_integer, get_random_operation, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operation(self):
        # Define valid operators
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = get_random_operation()
            # Check if the returned operator is in from valid set
            self.assertIn(operator, valid_operators, "The operator is not one of the expected operators.")


    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (7, 0, '+', '7 + 0', 7),
                (7, 0, '*', '7 * 0', 0),
                (5, 5, '-', '5 - 5', 0),
                (1, 1, '+', '1 + 1', 2),
    ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Call function_C and get the result
                problem, answer = perform_operation(num1, num2, operator)
                # Assert that the problem and answer match the expected values
                self.assertEqual(problem, expected_problem, f"Failed on {num1} {operator} {num2}")
                self.assertEqual(answer, expected_answer, f"Failed on {num1} {operator} {num2}")
if __name__ == "__main__":
    unittest.main()