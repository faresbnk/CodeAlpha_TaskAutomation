"""
CodeAlpha Python Internship -> Task03: Task Automation with Python Scripts
Automation idea: extract all email addresses from a .txt file and save them
to another file.

Concepts used: re, file handling, functions, error handling.

Usage:
    python extract_emails.py                      # uses sample_input.txt -> emails.txt
    python extract_emails.py my_file.txt out.txt  # custom input and output files
"""

import re
import sys

# A practical regular expression for matching email addresses
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in the text."""
    found = re.findall(EMAIL_PATTERN, text)
    # Emails are case-insensitive, so lowercase before removing duplicates
    unique = sorted(set(email.lower() for email in found))
    return unique


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "sample_input.txt"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "emails.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: could not find '{input_file}'.")
        return

    emails = extract_emails(text)

    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Found {len(emails)} unique email address(es) in '{input_file}'.")
    print(f"Saved to '{output_file}'.")


if __name__ == "__main__":
    main()
