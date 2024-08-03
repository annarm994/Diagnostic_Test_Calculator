# Diagnostic Tool

This tool calculates the probability of having a disease based on test results using Bayes' Theorem.

## How to Run

1. Ensure you have Python installed.
2. Clone this repository.
3. Run `python diagnostic_tool.py` and follow the prompts.

## Test Cases

Test cases can be run using the provided script in the repository to verify accuracy.

<!-- 

def test_calculate_probabilities():
    # Normal cases
    assert calculate_probabilities(0.01, 0.99, 0.99) == (0.5, 0.0001)
    assert calculate_probabilities(0.05, 0.95, 0.90) == (0.3239, 0.0053)
    assert calculate_probabilities(0.1, 0.90, 0.85) == (0.3913, 0.0158)
    
    # Edge cases
    assert calculate_probabilities(0.0, 0.99, 0.99) == (0.0, 0.0)
    assert calculate_probabilities(1.0, 0.99, 0.99) == (1.0, 1.0)
    assert calculate_probabilities(0.5, 1.0, 1.0) == (1.0, 0.0)

test_calculate_probabilities() 

-->
