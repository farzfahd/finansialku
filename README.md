# 🪙 Finansialku: Pencatat Keuangan Harian

`Finansialku` adalah aplikasi *Command-Line Interface* (CLI) berbasis Python yang dirancang untuk membantu Anda mengelola keuangan pribadi dengan mudah. Aplikasi ini memungkinkan Anda melacak pemasukan dan pengeluaran, mengatur anggaran, serta menghasilkan laporan keuangan yang komprehensif. Semua data tersimpan secara lokal di komputer Anda dalam format CSV dan JSON.

-----

## Daftar Isi

  * [Fitur Utama](#fitur-utama)
  * [Instalasi](#instalasi)
      * [Prasyarat](#prasyarat)
      * [Windows](#windows)
      * [macOS & Linux](#macos--linux)
  * [Cara Penggunaan](#cara-penggunaan)
      * [Menjalankan Aplikasi](#menjalankan-aplikasi)
      * [1. Mengatur Anggaran](#1-mengatur-anggaran)
      * [2. Mencatat Pemasukan](#2-mencatat-pemasukan)
      * [3. Mencatat Pengeluaran](#3-mencatat-pengeluaran)
      * [4. Laporan Rekap Keuangan](#4-laporan-rekap-keuangan)
      * [5. Edit Rekap Keuangan](#5-edit-rekap-keuangan)
      * [6. Keluar](#6-keluar)
  * [Struktur File](#struktur-file)
  * [Tips Penggunaan](#tips-penggunaan)
  * [Troubleshooting](#troubleshooting)

-----

## Fitur Utama

  * **Manajemen Anggaran** — Tetapkan batas anggaran harian dan bulanan sebagai acuan pengeluaran Anda.
  * **Pencatatan Transaksi** — Catat setiap pemasukan dan pengeluaran dengan mudah dan cepat.
  * **Kategorisasi Lengkap** — Kelompokkan pengeluaran ke dalam 7 kategori: Makanan & Minuman, Belanja, Transportasi, Gaya Hidup, Belanja Pokok, Donasi, dan Lainnya.
  * **Laporan Dinamis** — Hasilkan laporan keuangan harian atau bulanan sesuai kebutuhan.
  * **Analisis Sederhana** — Lihat total saldo, rincian pengeluaran per kategori, dan perbandingan dengan anggaran.
  * **Edit Transaksi** — Perbaiki kesalahan pencatatan dengan fitur edit yang fleksibel.
  * **ID Transaksi Unik** — Setiap transaksi memiliki ID 9 digit untuk kemudahan penelusuran.
  * **Penyimpanan Lokal** — Data aman tersimpan di komputer Anda dalam format CSV dan JSON.

-----

## Instalasi

### Prasyarat

Pastikan sistem Anda memenuhi persyaratan berikut:

  * **Python 3.6+** — Bahasa pemrograman yang menjadi fondasi aplikasi.
  * **PIP** — Manajer paket Python (biasanya sudah terinstal bersama Python).

**Library yang Dibutuhkan**:
  * **pandas** — Library untuk pengolahan dan analisis data dalam format tabel (perlu diinstal manual)
  * **datetime** — Library untuk mengelola tanggal dan waktu transaksi (sudah built-in dalam Python)
  * **os** — Library untuk operasi file dan folder (sudah built-in dalam Python)
  * **json** — Library untuk menyimpan data anggaran (sudah built-in dalam Python)
  * **glob** — Library untuk mencari file dengan pola tertentu (sudah built-in dalam Python)

### Windows

1.  **Unduh Script**
    * Simpan kode aplikasi dalam file bernama `finansialku.py`
    * Letakkan di folder yang mudah diakses (misal: `Documents` atau `Desktop`)

2.  **Buka Command Prompt**
    * Tekan tombol `Windows + R`
    * Ketik `cmd` lalu tekan `Enter`
    * Atau cari "Command Prompt" di menu Start

3.  **Navigasi ke Folder Aplikasi**
    ```cmd
    cd C:\Users\NamaAnda\Documents\Finansialku
    ```

4.  **Buat Virtual Environment** (Sangat direkomendasikan)
    ```cmd
    python -m venv venv
    ```

5.  **Aktifkan Virtual Environment**
    ```cmd
    venv\Scripts\activate
    ```
    * Anda akan melihat `(venv)` di awal prompt

6.  **Install Dependensi**
    ```cmd
    pip install pandas
    ```
    * Tunggu hingga proses instalasi selesai

### macOS & Linux

1.  **Unduh Script**
    * Simpan kode aplikasi dalam file bernama `finansialku.py`
    * Letakkan di folder yang mudah diakses (misal: `~/Documents/Finansialku`)

2.  **Buka Terminal**
    * **macOS**: Tekan `Cmd + Space`, ketik "Terminal"
    * **Linux**: Tekan `Ctrl + Alt + T`

3.  **Navigasi ke Folder Aplikasi**
    ```bash
    cd ~/Documents/Finansialku
    ```

4.  **Buat Virtual Environment** (Sangat direkomendasikan)
    ```bash
    python3 -m venv venv
    ```

5.  **Aktifkan Virtual Environment**
    ```bash
    source venv/bin/activate
    ```
    * Anda akan melihat `(venv)` di awal prompt

6.  **Install Dependensi**
    ```bash
    pip3 install pandas
    ```
    * Tunggu hingga proses instalasi selesai

-----

## Cara Penggunaan

### Menjalankan Aplikasi

Pastikan virtual environment aktif (terlihat `(venv)` di awal prompt), lalu jalankan:

```bash
# Windows
python finansialku.py

# macOS & Linux
python3 finansialku.py
```

Anda akan melihat menu utama:

```
---👋 Selamat Datang di Aplikasi Pencatat Anggaran Harian 🪙---

Pilih Fitur yang Ingin Anda Gunakan
1. Mengatur Anggaran
2. Mencatat Pemasukan
3. Mencatat Pengeluaran
4. Laporan Rekap Keuangan
5. Edit Rekap Keuangan
6. Keluar
Silahkan pilih fitur (1-6):
```

### 1. Mengatur Anggaran

**Fungsi**: Menetapkan batas pengeluaran harian dan bulanan sebagai kontrol keuangan.

**Langkah-langkah**:
  * Pilih opsi **1** dari menu utama
  * Masukkan **anggaran harian** (misal: `50000` untuk Rp 50.000)
  * Masukkan **anggaran bulanan** (misal: `1500000` untuk Rp 1.500.000)
  * Sistem akan menampilkan nilai anggaran lama sebagai referensi
  * Tekan `Enter` untuk konfirmasi

**Hasil**: File `anggaran.json` akan dibuat/diperbarui dengan pengaturan baru Anda.

**Contoh**:
```
Masukkan batas anggaran harian (Batas harian saat ini: Rp.0): 50000
Masukkan batas anggaran bulanan (Batas bulanan saat ini: Rp.0): 1500000

✅ Anggaran berhasil diperbarui
💵 Anggaran Harian: Rp.50,000
💵 Anggaran Bulanan: Rp.1,500,000
```

### 2. Mencatat Pemasukan

**Fungsi**: Mendokumentasikan setiap sumber pendapatan yang Anda terima.

**Langkah-langkah**:
  * Pilih opsi **2** dari menu utama
  * Masukkan **jumlah pemasukan** (misal: `5000000`)
  * Masukkan **deskripsi** (misal: `Gaji bulan November`)
  * Sistem otomatis membuat ID transaksi unik

**Hasil**: 
  * Transaksi tercatat dalam file CSV bulan berjalan
  * Saldo global bertambah sesuai jumlah pemasukan
  * ID transaksi dibuat otomatis (format: `DDMMYYNNN`)

**Contoh**:
```
Masukkan jumlah pemasukan (Rp): 5000000
Masukkan Deskripsi: Gaji bulan November

✅ Pemasukan Rp.5,000,000 berhasil dicatat.
```

### 3. Mencatat Pengeluaran

**Fungsi**: Mencatat setiap pengeluaran dengan kategorisasi yang detail.

**Langkah-langkah**:
  * Pilih opsi **3** dari menu utama
  * Masukkan **jumlah pengeluaran** (misal: `25000`)
  * Masukkan **deskripsi** (misal: `Makan siang di kantin`)
  * Pilih **kategori** dari 7 pilihan:
    1. Makanan dan Minuman
    2. Belanja
    3. Transportasi
    4. Gaya Hidup
    5. Belanja Pokok
    6. Donasi
    7. Lainnya

**Hasil**:
  * Transaksi tercatat dalam file CSV bulan berjalan
  * Saldo global berkurang sesuai jumlah pengeluaran
  * Kategori tersimpan untuk analisis laporan

**Contoh**:
```
Masukkan jumlah pengeluaran (Rp): 25000
Masukkan deskripsi: Makan siang di kantin
Pilih Kategori Pengeluaran
1. Makanan dan Minuman
[...]
Masukkan kategori (1-7): 1

✅ Pengeluaran Rp.25,000 berhasil dicatat.
```

### 4. Laporan Rekap Keuangan

**Fungsi**: Menghasilkan laporan keuangan berdasarkan periode yang dipilih.

**Langkah-langkah**:
  * Pilih opsi **4** dari menu utama
  * Lihat **total saldo** Anda saat ini
  * Pilih jenis laporan:

#### **Laporan Harian** (Pilihan 1)
  * Masukkan **tahun** (tekan `Enter` untuk tahun ini)
  * Masukkan **bulan** (tekan `Enter` untuk bulan ini)
  * Masukkan **tanggal** (tekan `Enter` untuk hari ini)

**Menampilkan**:
  * Total pengeluaran pada hari tersebut
  * Perbandingan dengan anggaran harian
  * Daftar lengkap semua transaksi

#### **Laporan Bulanan** (Pilihan 2)
  * Masukkan **tahun** (tekan `Enter` untuk tahun ini)
  * Masukkan **bulan** (tekan `Enter` untuk bulan ini)

**Menampilkan**:
  * Total pemasukan bulan tersebut
  * Total pengeluaran bulan tersebut
  * Saldo bersih (pemasukan - pengeluaran)
  * Rincian pengeluaran per kategori (diurutkan dari terbesar)
  * Daftar lengkap semua transaksi

**Contoh Output Laporan Bulanan**:
```
---Laporan Bulan 11/2025---
Total Pemasukan: Rp. 5,000,000
Total Pengeluaran: Rp. 1,250,000
**Saldo Bersih Bulan 11: Rp. 3,750,000**

--- Rincian Pengeluaran per Kategori ---
Makanan dan Minuman    Rp. 650,000
Transportasi           Rp. 300,000
Belanja                Rp. 200,000
Gaya Hidup             Rp. 100,000
```

### 5. Edit Rekap Keuangan

**Fungsi**: Memperbaiki atau mengubah transaksi yang sudah tercatat.

**Langkah-langkah**:
  * Pilih opsi **5** dari menu utama
  * Masukkan **tahun** transaksi yang ingin diedit
  * Masukkan **bulan** transaksi yang ingin diedit
  * Sistem menampilkan **semua transaksi** di bulan tersebut
  * Masukkan **ID transaksi** (9 digit) yang ingin diubah
  * Sistem menampilkan **data lama** sebagai referensi

**Yang Dapat Diubah**:
  * **Deskripsi** — Ketik deskripsi baru atau tekan `Enter` untuk tetap
  * **Tipe Transaksi** — Ubah dari Pemasukan ke Pengeluaran atau sebaliknya
  * **Jumlah** — Masukkan nilai baru
  * **Kategori** — Pilih kategori baru (untuk pengeluaran)

**Hasil**:
  * File CSV diperbarui dengan data baru
  * Saldo global disesuaikan otomatis
  * Perubahan tersimpan permanen

**Contoh**:
```
--- Data Transaksi Lama ---
ID: 011125001
Deskripsi: Makan siang
Pemasukan: 0
Pengeluaran: 25000

Masukkan Deskripsi baru (Lama: Makan siang): Makan siang di kantin
Masukkan Jumlah baru (Lama: Rp.25,000): 30000

✅ Transaksi berhasil diperbarui!
💰 Saldo global diperbarui: Rp. 4,970,000
```

### 6. Keluar

**Fungsi**: Menutup aplikasi dengan aman.

**Langkah-langkah**:
  * Pilih opsi **6** dari menu utama
  * Aplikasi akan tertutup
  * Semua data sudah otomatis tersimpan

-----

## Struktur File

Aplikasi ini membuat dan mengelola file secara otomatis dengan struktur sebagai berikut:

```
/Finansialku-Project
    ├── finansialku.py         ← Script utama aplikasi
    ├── anggaran.json          ← Data anggaran & total saldo
    ├── venv/                  ← Virtual environment (opsional)
    │
    ├── 2025/                  ← Folder tahun (dibuat otomatis)
    │   ├── 10_2025.csv        ← Transaksi Oktober 2025
    │   ├── 11_2025.csv        ← Transaksi November 2025
    │   └── 12_2025.csv        ← Transaksi Desember 2025
    │
    └── 2026/                  ← Folder tahun berikutnya
        ├── 01_2026.csv        ← Transaksi Januari 2026
        └── 02_2026.csv        ← Transaksi Februari 2026
```

**Penjelasan**:
  * `anggaran.json` — Menyimpan anggaran harian, bulanan, dan total saldo
  * `YYYY/` — Folder untuk setiap tahun (dibuat otomatis saat ada transaksi)
  * `MM_YYYY.csv` — File transaksi per bulan dengan kolom: ID, Tanggal, Deskripsi, Pemasukan, Pengeluaran, Kategori

**Format ID Transaksi**: `DDMMYYNNN`
  * `DD` = Tanggal (2 digit)
  * `MM` = Bulan (2 digit)
  * `YY` = Tahun (2 digit terakhir)
  * `NNN` = Nomor urut transaksi hari itu (3 digit)
  * Contoh: `011125001` = Transaksi pertama tanggal 1 November 2025

-----

## Tips Penggunaan

  * **Catat Segera** — Masukkan transaksi sesegera mungkin agar tidak ada yang terlewat
  * **Deskripsi Jelas** — Gunakan deskripsi yang spesifik untuk memudahkan penelusuran
  * **Konsisten Kategori** — Pilih kategori secara konsisten untuk analisis yang akurat
  * **Review Rutin** — Periksa laporan bulanan setiap awal bulan untuk evaluasi
  * **Sesuaikan Anggaran** — Update anggaran berdasarkan pola pengeluaran Anda
  * **Backup Berkala** — Salin folder data ke cloud storage atau eksternal drive
  * **Virtual Environment** — Selalu gunakan venv untuk menghindari konflik library
  * **Cek Saldo** — Gunakan laporan keuangan untuk memantau saldo secara berkala

-----

## Troubleshooting

### ❌ Error: `ModuleNotFoundError: No module named 'pandas'`
**Penyebab**: Library pandas belum terinstal

**Solusi**:
  * Aktifkan virtual environment terlebih dahulu
  * Jalankan: `pip install pandas` (Windows) atau `pip3 install pandas` (macOS/Linux)
  * Jika masih error, coba: `python -m pip install pandas`

### ❌ Error: `PermissionError` saat menyimpan file
**Penyebab**: Aplikasi tidak memiliki izin menulis di folder tersebut

**Solusi**:
  * **Windows**: Jalankan Command Prompt sebagai Administrator
  * **macOS/Linux**: Periksa permission dengan `ls -la`, ubah jika perlu dengan `chmod 755 finansialku.py`
  * Pindahkan aplikasi ke folder yang memiliki akses penuh (misal: Documents)

### ❌ File `anggaran.json` rusak atau kosong
**Penyebab**: File JSON corrupt atau format tidak valid

**Solusi**:
  * Hapus file `anggaran.json`
  * Jalankan aplikasi, file baru akan dibuat otomatis dengan nilai default 0
  * Atur ulang anggaran melalui menu pertama

### ❌ Data transaksi tidak muncul di laporan
**Penyebab**: File CSV mungkin rusak atau format tanggal tidak sesuai

**Solusi**:
  * Buka file CSV dengan text editor (Notepad, VSCode)
  * Periksa format tanggal harus: `DD-MM-YYYY`
  * Pastikan tidak ada baris kosong di tengah data
  * Cek kolom header: ID, Tanggal, Deskripsi, Pemasukan, Pengeluaran, Kategori

### ❌ Virtual environment tidak bisa diaktifkan di Windows
**Penyebab**: Execution policy Windows membatasi menjalankan script

**Solusi**:
  * Buka PowerShell sebagai Administrator
  * Jalankan: `Set-ExecutionPolicy RemoteSigned`
  * Ketik `Y` untuk konfirmasi
  * Coba aktifkan venv lagi

### ❌ Error saat mengedit transaksi
**Penyebab**: ID transaksi tidak ditemukan atau salah format

**Solusi**:
  * Pastikan ID 9 digit diketik dengan benar
  * Cek kembali daftar transaksi yang ditampilkan
  * ID harus persis sama, tanpa spasi di awal atau akhir
  * Pastikan bulan dan tahun sesuai dengan transaksi yang dicari

-----

## Kontribusi & Pengembangan

Aplikasi ini bersifat open-source dan terbuka untuk pengembangan lebih lanjut. Beberapa ide fitur masa depan:

  * 📊 Visualisasi grafik tren pengeluaran
  * 📄 Export laporan ke PDF atau Excel
  * ⏰ Reminder otomatis untuk pencatatan
  * 🔔 Notifikasi saat mendekati batas anggaran
  * 📈 Prediksi pengeluaran berdasarkan pola historis
  * 💱 Dukungan multi-mata uang
  * 🔐 Enkripsi data untuk keamanan ekstra

-----

## Lisensi

Aplikasi ini dikembangkan untuk keperluan personal dan edukasi. Anda bebas menggunakan, memodifikasi, dan mendistribusikan sesuai kebutuhan.

-----

**Selamat mengelola keuangan Anda dengan lebih baik! 💰**

Jika menemukan bug atau memiliki saran, jangan ragu untuk memberikan feedback. Semoga Finansialku membantu Anda mencapai tujuan keuangan pribadi! 🎯
