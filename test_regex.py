"""
Tests the extraction of different data types from text using regex patterns.
"""

import regex_data_extraction as rex

def test_email_extraction():
    """Test extraction of email addresses."""
    test_text = "Contact us at user@example.com or firstname.lastname@company.co.uk"
    results = rex.extract_data(test_text)
    
    print("Testing email extraction:")
    expected = ["user@example.com", "firstname.lastname@company.co.uk"]
    found = results["emails"]
    
    print(f"Expected: {expected}")
    print(f"Found: {found}")
    print(f"Test {'PASSED' if set(expected) == set(found) else 'FAILED'}")
    print()

def test_url_extraction():
    """Test extraction of URLs."""
    test_text = "Visit www.example.com or subdomain.example.org/page"
    results = rex.extract_data(test_text)
    
    print("Testing URL extraction:")
    expected = ["https://www.example.com", "https://subdomain.example.org/page"]
    found = results["urls"]
    
    print(f"Expected: {expected}")
    print(f"Found: {found}")
    print(f"Test {'PASSED' if set(expected) == set(found) else 'FAILED'}")
    print()

def test_phone_extraction():
    """Test extraction of phone numbers."""
    test_text = "Call (123) 456-7890 or 123-456-7890 or 123.456.7890"
    results = rex.extract_data(test_text)
    
    print("Testing phone number extraction:")
    expected = ["(123) 456-7890", "123-456-7890", "123.456.7890"]
    found = results["phone_numbers"]
    
    print(f"Expected: {expected}")
    print(f"Found: {found}")
    print(f"Test {'PASSED' if set(expected) == set(found) else 'FAILED'}")
    print()

def test_credit_card_extraction():
    """Test extraction of credit card numbers."""
    test_text = "Payment with 1234 5678 9012 3456 or 1234-5678-9012-3456"
    results = rex.extract_data(test_text)
    
    print("Testing credit card extraction:")
    expected = ["1234 5678 9012 3456", "1234-5678-9012-3456"]
    found = results["credit_cards"]
    
    print(f"Expected: {expected}")
    print(f"Found: {found}")
    print(f"Test {'PASSED' if set(expected) == set(found) else 'FAILED'}")
    print()

def test_time_extraction():
    """Test extraction of time formats."""
    test_text = "Hours: 14:30 to 17:00 or from 9:30 AM to 5:30 PM"
    results = rex.extract_data(test_text)
    
    print("Testing time format extraction:")
    expected = ["14:30", "17:00", "9:30 AM", "5:30 PM"]
    found = results["times"]
    
    print(f"Expected: {expected}")
    print(f"Found: {found}")
    print(f"Test {'PASSED' if set(expected) == set(found) else 'FAILED'}")
    print()

def run_all_tests():
    """Run all test cases."""
    print("===== Running Tests =====\n")
    test_email_extraction()
    test_url_extraction()
    test_phone_extraction()
    test_credit_card_extraction()
    test_time_extraction()
    print("===== Tests Complete =====")

if __name__ == "__main__":
    run_all_tests()
