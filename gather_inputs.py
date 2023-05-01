def get_input(prompt):
    return input(prompt)

def main():
    print("Hello and thank you for choosing me as your lawyer. I'm here to help you with your legal needs.")
    
    full_name = get_input("1. Please enter your full name: ")
    date_of_birth = get_input("2. Please enter your date of birth (YYYY-MM-DD): ")
    current_address = get_input("3. Please enter your current address: ")
    
    print("\nTypes of legal papers:")
    print("a. Contract")
    print("b. Will")
    print("c. Power of Attorney")
    print("d. Other")
    legal_paper_type = get_input("4. Please select the type of legal papers you require: ")
    
    situation_description = get_input("5. Please provide a brief description of the situation or transaction for which you require the legal papers: ")
    
    other_parties = get_input("6. Please enter the names and contact information of any other parties involved, if applicable (separate with commas): ")
    
    specific_provisions = get_input("7. Please list any specific provisions or clauses you would like to include in the legal papers: ")
    
    deadline = get_input("8. Please provide any deadlines or time-sensitive matters related to the legal papers: ")
    
    print("\nThank you for providing the necessary information. I will now proceed to create the required legal papers based on your inputs.")
    
if __name__ == "__main__":
    main()
