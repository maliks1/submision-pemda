# Submission PEMDA

Project ini adalah pipeline ETL sederhana berbasis Python untuk mengambil data produk dari situs fashion, membersihkan dan menormalkan datanya, lalu menyimpannya ke file CSV.

## Fitur

- Extract data produk dari `https://fashion-studio.dicoding.dev/`
- Transform data seperti validasi rating, normalisasi ukuran dan gender, konversi harga ke IDR, dan penghapusan data duplikat
- Load hasil akhir ke file CSV
- Tersedia test untuk proses extract, transform, dan load

## Struktur Project

- `main.py` - entry point untuk menjalankan pipeline ETL
- `utils/extract.py` - mengambil data dari website
- `utils/transform.py` - membersihkan dan mengolah data
- `utils/load.py` - menulis hasil ke file CSV
- `tests/` - kumpulan test

## Prasyarat

- Python 3
- Paket dependency dari `requirements.txt`

## Instalasi

Aktifkan virtual environment yang sudah tersedia:

```bash
c:\Users\submission-pemda\.venv\Scripts\Activate.ps1
```

Lalu install dependency:

```bash
pip install -r requirements.txt
```

## Cara Menjalankan

Jalankan pipeline utama:

```bash
python main.py
```

Hasilnya akan ditulis ke `products.csv` di root project.

## Cara Menjalankan Test

```bash
python -m pytest
```

## Output

File output default adalah `products.csv`. File ini berisi data produk yang sudah diproses dalam format CSV dengan kolom:

`id,Title,Price,Rating,Colors,Size,Gender`

## Catatan

- Project ini menggunakan scraping web, jadi hasil bisa berubah jika struktur website sumber berubah.
- Jika ingin menyimpan hasil ke file lain, sesuaikan parameter output pada fungsi load.