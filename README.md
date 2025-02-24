# **SiBetta - Sistem Identifikasi Ikan Cupang Berbasis AI**

SiBetta adalah aplikasi web berbasis kecerdasan buatan (AI) yang dirancang untuk mengidentifikasi jenis ikan cupang dari gambar yang diunggah oleh pengguna. Aplikasi ini ditujukan bagi pecinta ikan cupang, penjual, dan pembeli yang ingin mengetahui jenis ikan dengan cepat dan akurat.

## **📌 Fitur Utama**
- **Identifikasi Otomatis**: Unggah gambar ikan cupang dan dapatkan hasil klasifikasinya.
- **Akurasi Tinggi**: Model AI dilatih menggunakan dataset ikan cupang yang bervariasi.
- **Antarmuka Mudah Digunakan**: Desain UI yang sederhana dan ramah pengguna.
- **Pembaruan Berkala**: Model akan diperbarui secara berkala untuk meningkatkan akurasi.

---

## **📂 Struktur Proyek**
```
SiBetta/
├── .devcontainer/               # Konfigurasi untuk environment pengembangan
├── dataset/                     # Dataset gambar ikan cupang
├── models/                      # Model hasil pelatihan
├── static/                      # File statis untuk UI
├── templates/                   # Template HTML untuk tampilan web
├── app.py                       # Skrip utama aplikasi web
├── train_model.ipynb            # Notebook pelatihan model
├── requirements.txt             # Daftar dependensi Python
├── README.md                    # Dokumentasi proyek
└── LICENSE                      # Lisensi proyek
```

---

## **⚙️ Instalasi**
Pastikan Anda telah menginstal Python 3.x dan `pip`. Ikuti langkah-langkah berikut untuk menjalankan SiBetta secara lokal:

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/GilangArdhi/SiBetta.git
   cd SiBetta
   ```

2. **Buat dan aktifkan virtual environment** (opsional tetapi disarankan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk pengguna Unix/macOS
   # atau
   venv\Scripts\activate.bat  # Untuk pengguna Windows
   ```

3. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   ```bash
   python app.py
   ```
   Aplikasi akan berjalan di `http://localhost:5000/`.

---

## **🚀 Cara Menggunakan**
1. Buka aplikasi di browser Anda.
2. Unggah gambar ikan cupang yang ingin diidentifikasi.
3. Dapatkan hasil identifikasi beserta informasi jenis ikan.

---

## **🛠️ Pelatihan Model**
Jika Anda ingin melatih ulang model dengan dataset baru:

1. Letakkan dataset gambar di folder `dataset/`.
2. Jalankan notebook pelatihan:
   ```bash
   jupyter notebook train_model.ipynb
   ```
3. Simpan model hasil pelatihan ke dalam folder `models/`.

---

## **🤝 Kontribusi**
Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. **Fork repositori ini**.
2. **Buat branch fitur baru**:
   ```bash
   git checkout -b fitur-baru
   ```
3. **Commit perubahan Anda**:
   ```bash
   git commit -m 'Menambahkan fitur baru'
   ```
4. **Push ke branch**:
   ```bash
   git push origin fitur-baru
   ```
5. **Buat Pull Request**.

---

## **📜 Lisensi**
Proyek ini dilisensikan di bawah lisensi MIT. Silakan lihat file [LICENSE](https://github.com/GilangArdhi/SiBetta/blob/main/LICENSE) untuk informasi lebih lanjut.

---

Untuk informasi lebih lanjut, kunjungi [repositori SiBetta](https://github.com/GilangArdhi/SiBetta).

