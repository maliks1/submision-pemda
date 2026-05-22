from utils import transform


def test_transform_adds_price_with_tax():
    products = [{'id': '1', 'Title': 'A', 'Price': '$100', 'Colors': '2 Colors', 'Size': 'M', 'Gender': 'Men'}]
    out = transform.transform_products(products)
    assert out[0]['price_with_tax'] == 110.0
