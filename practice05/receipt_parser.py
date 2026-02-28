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
