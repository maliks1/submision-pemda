from utils import extract, transform, load


def main():
    products = extract.extract_products()
    products_t = transform.transform_products(products)
    out = load.load_to_file(products_t)
    print('Wrote', out)


if __name__ == '__main__':
    main()
