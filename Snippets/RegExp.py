# Regular Expressions Practice
import re
import string

def main():
    sample_string = "This is a sample string"
    sample_ip = "10.16.1.101"
    sample_alpha_numerical = "This is a sample 123 and abc"

    # Groups to have the outcome in brackets
    # Group to have the outcome without brackets
    test_string = re.search(r'([a-zA-Z\s].+)', sample_string).group(0)
    test_ip = re.search(r'([\d\.]+)', sample_ip).group(0)
    test_alpha = re.search(r'(...$)',sample_alpha_numerical).group(0)    
    test_numerical = re.search(r'(\d\d\d)',sample_alpha_numerical).group(0)
    
    print(test_string)
    print(test_ip)
    print(test_alpha)
    print(test_numerical)

main()