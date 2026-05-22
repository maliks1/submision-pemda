def transform_products(products):
    transformed = []
    for p in products:
        item = dict(p)
        price_raw = (item.get('Price') or '').strip()
        normalized_price = price_raw.replace('$', '').replace(',', '')
        price = normalized_price or 0
        try:
            price = float(price)
        except (TypeError, ValueError):
            price = 0.0
        item['price_with_tax'] = round(price * 1.1, 2)
        transformed.append(item)
    return transformed
