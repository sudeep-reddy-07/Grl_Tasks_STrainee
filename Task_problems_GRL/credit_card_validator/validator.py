import re

def validate_credit_card(card_number):
    """
    Validates whether a credit card number is valid based on the following rules:
    - Starts with 4, 5, or 6
    - Contains exactly 16 digits or digits grouped in 4 separated by hyphens
    - No other separators are allowed
    - Must not have 4 or more consecutive repeated digits
    
    Parameters:
    card_number (str): The credit card number to be validated
    
    Returns:
    str: 'Valid' if the card is valid, otherwise 'Invalid'
    """
    # Regex to match valid card formats: 
    pattern = r"^[456]\d{3}(-?\d{4}){3}$"
    # Check if card matches the pattern
    if re.match(pattern, card_number):
        # Remove hyphens to check for consecutive digits
        card_number = card_number.replace("-", "")
        # Check for 4 or more consecutive repeated digits
        if re.search(r"(\d)\1{3}", card_number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    # Read the number of credit card numbers
    n = int(input("Enter the number of credit card numbers: ").strip())
    # Process each card number and validate
    for _ in range(n):
        card_number = input().strip()
        print(validate_credit_card(card_number))
