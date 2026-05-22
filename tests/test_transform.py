from utils import transform


def test_transform_adds_price_with_tax():
    products = [{'id': '1', 'Title': 'A', 'Price': '$0.01', 'Rating': '4.8 / 5', 'Colors': '2 Colors', 'Size': 'Size: M', 'Gender': 'Gender: Men'}]
    out = transform.transform_products(products)
    assert out[0]['price_with_tax'] == 176.0


def test_transform_normalizes_target_columns():
    products = [{'id': '1', 'Title': 'A', 'Price': '$100', 'Rating': '4.8 / 5', 'Colors': '3 Colors', 'Size': 'Size: L', 'Gender': 'Gender: Women'}]
    out = transform.transform_products(products)

    assert out[0]['Rating'] == 4.8
    assert out[0]['Colors'] == 3
    assert out[0]['Size'] == 'L'
    assert out[0]['Gender'] == 'Women'


def test_transform_skips_invalid_rating():
    products = [{'id': '1', 'Title': 'A', 'Price': '$100', 'Rating': 'Invalid Rating', 'Colors': '3 Colors', 'Size': 'Size: L', 'Gender': 'Gender: Women'}]
    out = transform.transform_products(products)

    assert out == []
