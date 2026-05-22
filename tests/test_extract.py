from utils import extract


def test_extract_returns_list():
    products = extract.extract_products()
    assert isinstance(products, list)
    assert len(products) >= 1
    assert 'id' in products[0]
    assert 'Title' in products[0]
    assert 'Price' in products[0]
    assert 'Colors' in products[0]
    assert 'Size' in products[0]
    assert 'Gender' in products[0]
