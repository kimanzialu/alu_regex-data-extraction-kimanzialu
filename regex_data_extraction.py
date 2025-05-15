"""
This script implements regex patterns to extract various data types from text.
"""

import re

# Email addresses regex
# Matches formats like user@example.com, firstname.lastname@company.co.uk
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# URLs regex
# Matches formats like https://www.example.com, https://subdomain.example.org/page
url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'

# Phone numbers regex
# Matches formats like (123) 456-7890, 123-456-7890, 123.456.7890
phone_pattern = r'(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]?\d{4}'

# Credit card numbers regex
# Matches formats like 1234 5678 9012 3456, 1234-5678-9012-3456
credit_card_pattern = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}'

# Time regex
# Matches formats like 14:30 (24-hour), 2:30 PM (12-hour)
time_pattern = r'(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s*(?:AM|PM|am|pm)|(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9]))'

def extract_data(text):
    """
    Extract different types of data from the input text.
    """
    results = {
        'emails': re.findall(email_pattern, text),
        'urls': re.findall(url_pattern, text),
        'phone_numbers': re.findall(phone_pattern, text),
        'credit_cards': re.findall(credit_card_pattern, text),
        'times': re.findall(time_pattern, text)
    }
    return results

def print_results(results):
    """
    Print the extraction results in a readable format.
    """
    print("\n===== Data Extraction Results =====")
    for data_type, items in results.items():
        print(f"\n{data_type.upper()}:")
        if items:
            for item in items:
                print(f"  - {item}")
        else:
            print("  No items found")

def main():
    """
    Main function to test the regex patterns with sample text.
    """
    # Sample text containing various data types to extract
    sample_text = """
    Contact us at user@example.com or firstname.lastname@company.co.uk
    Visit our website at https://www.example.com or https://subdomain.example.org/page
    Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
    Payment accepted with credit card: 1234 5678 9012 3456 or 1234-5678-9012-3456
    Office hours: 14:30 to 17:00 or from 9:30 AM to 5:30 PM
    """
    
    # Extract data from sample text
    results = extract_data(sample_text)
    
    # Display the results
    print_results(results)
    
    # Test with user input
    print("\n===== Test with your own text =====")
    print("Enter some text to extract data from (press Ctrl+D or Ctrl+Z to finish):")
    
    user_input = ""
    try:
        while True:
            line = input()
            user_input += line + "\n"
    except EOFError:
        pass
    
    if user_input.strip():
        user_results = extract_data(user_input)
        print_results(user_results)

if __name__ == "__main__":
    main()
