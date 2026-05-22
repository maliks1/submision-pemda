from utils import load


def test_load_writes_file(tmp_path):
    products = [{'id': '1', 'Title': 'A', 'Price': '$100', 'Colors': '2 Colors', 'Size': 'M', 'Gender': 'Men'}]
    out = tmp_path / 'out.csv'
    path = load.load_to_file(products, str(out))
    assert out.exists()
    content = out.read_text(encoding='utf-8')
    assert 'id,Title,Price,Colors,Size,Gender' in content
    assert 'A' in content
