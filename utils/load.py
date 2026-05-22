from pathlib import Path

def load_to_file(products, out_path=None):
    path = Path(out_path) if out_path else Path(__file__).resolve().parents[1] / 'products.csv'
    with path.open('w', encoding='utf-8') as f:
        f.write('id,Title,Price,Colors,Size,Gender\n')
        for p in products:
            f.write(
                f"{p.get('id','')},{p.get('Title','')},{p.get('Price','')},{p.get('Colors','')},{p.get('Size','')},{p.get('Gender','')}\n"
            )
    return str(path)
