import re


def _parse_rating(value):
    text = str(value or '').strip()
    match = re.search(r'(\d+(?:\.\d+)?)', text)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def _parse_colors(value):
    text = str(value or '').strip()
    match = re.search(r'(\d+)', text)
    if not match:
        return 0
    return int(match.group(1))


def _clean_prefixed_text(value, prefix):
    text = str(value or '').strip()
    if text.lower().startswith(prefix.lower()):
        return text.split(':', 1)[1].strip()
    return text


def transform_products(products):
    transformed = []
    seen_rows = set()
    for p in products:
        item = dict(p)

        rating = _parse_rating(item.get('Rating'))
        if rating is None:
            continue
        item['Rating'] = rating

        item['Colors'] = _parse_colors(item.get('Colors'))
        item['Size'] = _clean_prefixed_text(item.get('Size'), 'Size:')
        item['Gender'] = _clean_prefixed_text(item.get('Gender'), 'Gender:')

        price_raw = (item.get('Price') or '').strip()
        normalized_price = price_raw.replace('$', '').replace(',', '')
        price = normalized_price or 0
        try:
            price = float(price)
        except (TypeError, ValueError):
            price = 0.0
        # Konversi USD ke IDR (1 USD = 16000 IDR)
        price_idr = round(price * 16000, 2)
        item['Price'] = f" {price_idr:.2f}"

        row_key = tuple(sorted(item.items()))
        if row_key in seen_rows:
            continue
        seen_rows.add(row_key)

        transformed.append(item)
    return transformed
