import re
import json

def parse_receipt(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    # --- Prices ---
    prices = re.findall(r'\d[\d ]*,\d{2}', text)
    prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

    # --- Product names ---
    product_pattern = re.compile(r'\d+\.\n(.+?)\n\d', re.DOTALL)
    products = [p.strip().replace("\n", " ") for p in product_pattern.findall(text)]

    # --- Total amount ---
    total_match = re.search(r'ИТОГО:\n([\d ]+,\d{2})', text)
    total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else None

    # --- Date and time ---
    datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', text)
    datetime = datetime_match.group(1) if datetime_match else None

    # --- Payment method ---
    payment_match = re.search(r'(Банковская карта|Наличные):', text)
    payment_method = payment_match.group(1) if payment_match else None

    return {
        "products": products,
        "prices": prices,
        "total": total,
        "datetime": datetime,
        "payment_method": payment_method
    }

if __name__ == "__main__":
    data = parse_receipt("raw.txt")
    print(json.dumps(data, ensure_ascii=False, indent=2))


import re

s = input()

pattern = r'^ab*$'

if re.match(pattern, s):
    print("Match")
else:
    print("No match")


import re

s = input()

pattern = r'^ab{2,3}$'

if re.match(pattern, s):
    print("Match")
else:
    print("No match")


import re

s = input()

# pattern: lowercase letters + underscore + lowercase letters (one or more times)
pattern = r'\b[a-z]+(?:_[a-z]+)+\b'

matches = re.findall(pattern, s)

for m in matches:
    print(m)


import re

s = input()

pattern = r'\b[A-Z][a-z]+\b'

matches = re.findall(pattern, s)

for m in matches:
    print(m)


import re

s = input()

pattern = r'^a.*b$'

if re.match(pattern, s):
    print("Match")
else:
    print("No match")


import re

s = input()

result = re.sub(r'[ ,.]', ':', s)

print(result)


s = input()

parts = s.split('_')

# First word stays lowercase, others capitalized
camel = parts[0] + ''.join(word.capitalize() for word in parts[1:])

print(camel)


import re

s = input()

# Split before each uppercase letter (but not at the start)
parts = re.split(r'(?=[A-Z])', s)

# Remove empty strings if any
parts = [p for p in parts if p]

print(parts)


import re

s = input()

# Insert a space before each uppercase letter (except the first one)
result = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

print(result)


import re

s = input()

# Insert underscore before uppercase letters (except at the start)
snake = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

print(snake)