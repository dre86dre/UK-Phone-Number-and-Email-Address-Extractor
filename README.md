# UK Phone Number and Email Address Extractor

UK Phone Number and Email Address Extractor is a simple Python utility that scans text in your clipboard for **UK mobile phone numbers** and **email addresses**. It extracts them, formats UK mobile numbers to include the `+44` country code, and replaces the clipboard content with just the extracted contacts.  

No more manual searching or copying—just select, copy, and run.  

---

## Features

- Extracts **UK mobile phone numbers** from clipboard text  
- Extracts **email addresses** from clipboard text  
- Formats UK mobile numbers with `+44` automatically  
- Replaces clipboard content with extracted results  
- Works with a single copy-paste operation: `Ctrl+A`, `Ctrl+C`, then run the program  

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/clipboard-contact-extractor.git
   cd clipboard-contact-extractor
Install dependencies (requires Python 3):

bash
Copy code
pip install -r requirements.txt
Dependencies:

pyperclip (for clipboard access)

re (Python built-in, for regex extraction)

Usage
Copy the text you want to scan to your clipboard (Ctrl+A → Ctrl+C).

Run the program:

bash
Copy code
python extract_contacts.py
Your clipboard will now contain only the extracted UK mobile numbers (formatted with +44) and email addresses. Paste it anywhere (Ctrl+V).

Example
Clipboard text before running:

graphql
Copy code
Hello, please contact me at 07123 456789 or john.doe@example.com. You can also reach my colleague on 07456 987654 or jane.smith@example.co.uk.
Clipboard content after running:

diff
Copy code
+447123456789
+447456987654
john.doe@example.com
jane.smith@example.co.uk
Script (extract_contacts.py)
python
Copy code
import re
import pyperclip

def extract_contacts(text):
    # Regex for UK mobile numbers (starting 07 with 10–11 digits)
    phone_pattern = re.compile(r'\b07\d{8,10}\b')
    # Regex for email addresses
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    phones = phone_pattern.findall(text)
    emails = email_pattern.findall(text)

    # Format UK mobile numbers with +44 (remove leading zero)
    formatted_phones = [re.sub(r'^0', '+44', num) for num in phones]

    return formatted_phones + emails

def main():
    text = pyperclip.paste()
    contacts = extract_contacts(text)
    result = '\n'.join(contacts)
    pyperclip.copy(result)
    print("Extracted contacts copied to clipboard:")
    print(result)

if __name__ == "__main__":
    main()
Contributing
Feel free to open issues or submit pull requests!

License
This project is licensed under the MIT License.
