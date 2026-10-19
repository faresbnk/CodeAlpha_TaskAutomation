# CodeAlpha_TaskAutomation

Task 3 of the CodeAlpha Python Programming Internship.

**Automation chosen:** extract all email addresses from a `.txt` file and save them to another file.

## Features
- Finds emails using a regular expression
- Removes duplicates (case-insensitive) and sorts the results
- Handles a missing input file gracefully

## How to run
```bash
# Uses sample_input.txt and writes emails.txt
python extract_emails.py

# Or choose your own files
python extract_emails.py my_notes.txt my_emails.txt
```

## Concepts used
`re` (regular expressions), file handling, functions, `sys.argv`
