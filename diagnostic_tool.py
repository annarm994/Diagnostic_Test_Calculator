def calculate_probabilities(prevalence, sensitivity, specificity):
    # Calculate P(Test+|Disease-)
    p_test_pos_given_disease_neg = 1 - specificity
    
    # Calculate P(Test+)
    p_test_pos = (sensitivity * prevalence) + (p_test_pos_given_disease_neg * (1 - prevalence))
    
    # Calculate P(Disease|Test+)
    p_disease_given_test_pos = (sensitivity * prevalence) / p_test_pos
    
    # Calculate P(Test-|Disease+)
    p_test_neg_given_disease_pos = 1 - sensitivity
    
    # Calculate P(Test-)
    p_test_neg = (p_test_neg_given_disease_pos * prevalence) + (specificity * (1 - prevalence))
    
    # Calculate P(Disease|Test-)
    p_disease_given_test_neg = (p_test_neg_given_disease_pos * prevalence) / p_test_neg
    
    return p_disease_given_test_pos, p_disease_given_test_neg

def main():
    print("Welcome to the Diagnostic Tool!")
    
    # Input fields
    prevalence = float(input("Enter the prevalence of the disease (as a decimal, e.g., 0.01 for 1%): "))
    sensitivity = float(input("Enter the sensitivity of the test (as a decimal, e.g., 0.99 for 99%): "))
    specificity = float(input("Enter the specificity of the test (as a decimal, e.g., 0.99 for 99%): "))
    
    # Calculate probabilities
    p_disease_given_test_pos, p_disease_given_test_neg = calculate_probabilities(prevalence, sensitivity, specificity)
    
    # Display results
    print(f"Probability of having the disease if tested positive: {p_disease_given_test_pos:.4f}")
    print(f"Probability of having the disease if tested negative: {p_disease_given_test_neg:.4f}")

if __name__ == "__main__":
    main()
