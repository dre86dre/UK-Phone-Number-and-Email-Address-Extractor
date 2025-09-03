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
<br>
## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/dre86dre/UK-Phone-Number-and-Email-Address-Extractor.git

2. Install dependencies (requires Python 3):
   ```bash
   pip install -r requirements.txt

Dependencies:
- `pyperclip` (for clipboard access)
- `re` (Python built-in, for regex extraction)


## Usage

1. Copy the text you want to scan to your clipboard (Ctrl+A → Ctrl+C).

2. Run the program:
   ```bash
   python ukPhoneNumberAndEmailAddressExtractor.py


3. Your clipboard will now contain only the extracted UK mobile numbers (formatted with `+44`) and email addresses. Paste it anywhere (`Ctrl+V`).


## Example

Clipboard text before running:
   ```graphql
   Hello, please contact me at 07123 456789 or john.doe@example.com. You can also reach my colleague on 07456 987654 or jane.smith@example.co.uk.
   ```

Clipboard content after running:
   ```diff
   +447123456789
   +447456987654
   john.doe@example.com
   jane.smith@example.co.uk
   
