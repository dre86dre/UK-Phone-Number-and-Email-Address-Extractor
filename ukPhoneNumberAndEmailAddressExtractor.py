# Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# Create phone regex.

phoneRegex = re.compile(r'''(
    (\+44\s?7\d{3}                          # +44 followed by '7' and 3 more digits
    |\(?07\d{3}\)?)                         # or 07xxx with optional brackets
    (\s|-)?                                 # optional separator (space or dash)
    (\d{3})                                 # next 3 digits
    (\s|-)?                                 # optional separator
    (\d{3,4})                               # last 3 or 4 digits
    )''', re.VERBOSE)

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                       # username
    @                                       # @ symbol
    [a-zA-Z0-9.-]+                          # domain name
    (\.[a-zA-Z]{2,4})                       # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    prefix = groups[1]
    mid = groups[3]
    last = groups[5]

    # Normalize to +44 format
    if prefix.startswith('07'):
        normalized = '+44 ' + prefix[1:] + mid + last       # Replace leading 0 with +44 + space
    else:
        normalized = '+44 ' + prefix.lstrip('+44').replace(' ', '').replace('-', '') + mid + last       # Already starts with +44, just clean it

    normalized = '+44 ' + re.sub(r'\D', '', normalized[4:])     # Remove any stray spaces/dashes after +44 

    matches.append(normalized)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.

if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No mobile phone numbers or email addresses found.')