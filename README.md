# Physics Laboratory III - Experiments

Bu klasör Marmara Üniversitesi Fizik Bölümü Fizik Laboratuvarı III dersine ait deneyleri içermektedir.

## Deney Listesi

1. **Deney 1**: Metallerin Özgül Isısının Tayini
2. **Deney 2**: Gliserinin Viskozite Katsayısı
3. **Deney 3**: İnce Kenarlı Mercek
4. **Deney 4**: Işığın Kırılması
5. **Deney 5**: Paralel Yüzlü Bloktan Işık Geçişi
6. **Deney 6**: Polarizasyon
7. **Deney 7**: Kırınım (Genel)
8. **Deney 8**: Tek Yarık Kırınımı

## Klasör Yapısı

Her deney klasörü şu dosyaları içermektedir:

```
X/
├── README.md          # Deney açıklaması
├── data.py           # Veri analizi ve grafik üretimi
├── measurements.csv  # Ham ölçüm verileri
├── report.tex        # LaTeX raporu
└── graphs/           # Üretilen grafikler
```

## Kullanım

1. **Veri Girişi**: `measurements.csv` dosyasına deneysel verilerinizi girin
2. **Analiz**: `python data.py` komutu ile veri analizini çalıştırın
3. **Grafik Üretimi**: Grafikler otomatik olarak `graphs/` klasörüne kaydedilir
4. **Rapor**: LaTeX dosyasını derleyerek raporu oluşturun

## LaTeX Raporu Derleme

```bash
cd X/  # Deney klasörüne git
pdflatex report.tex
```

## Gereksinimler

- Python 3.x
- numpy
- matplotlib
- pandas
- LaTeX dağıtımı (TeX Live, MiKTeX vb.)

## Not

Her hafta yapılan deneyin verilerini ilgili klasöre ekleyip, Python scriptini çalıştırarak grafikler oluşturun. Sonrasında LaTeX raporu derleyerek hocaya teslim edin.
