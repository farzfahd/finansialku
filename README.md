# 🪙 Finansialku: Pencatat Keuangan Harian

`Finansialku` adalah aplikasi *Command-Line Interface* (CLI) berbasis Python yang dirancang untuk membantu Anda mengelola keuangan pribadi dengan mudah. Aplikasi ini memungkinkan Anda melacak pemasukan dan pengeluaran, mengatur anggaran, serta menghasilkan laporan keuangan yang komprehensif. Semua data tersimpan secara lokal di komputer Anda dalam format CSV dan JSON.

**Dikembangkan dengan ❤️ oleh siswa SMAN 2 Pare, Kediri, Jawa Timur**

-----

## Daftar Isi

  * [Tentang Pembuat](#tentang-pembuat)
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
  * [Easter Eggs](#easter-eggs)
  * [Troubleshooting](#troubleshooting)
  * [Kontribusi](#kontribusi)
  * [Lisensi](#lisensi)

-----

## Tentang Pembuat

### 👨‍💻 Tim Pengembang

**Pembuat Utama - Lead Developer**
  * **Nama**: M. Farzana Al Fahad
  * **Sekolah**: SMAN 2 Pare, Kediri, Jawa Timur
  * **Email**: harfanasamsung@gmail.com
  * **GitHub**: [github.com/farzfahd](https://github.com/farzfahd)
  * **LinkedIn**: [Muhammad Farzana Al Fahad](https://linkedin.com/in/Muhammad-Farzana-Al-Fahad)
  * **Role**: System Architecture, Core Logic Development, UI/UX Design

**Pembuat Pembantu - Assistant Developer**
  * **Nama**: Irwansyah
  * **Sekolah**: SMAN 2 Pare, Kediri, Jawa Timur
  * **Role**: Testing, Debugging, Feature Ideas & Feedback

### 📅 Timeline Pengembangan

  * **Tanggal Mulai**: 26 Oktober 2025
  * **Tanggal Selesai**: 2 November 2025
  * **Durasi**: 8 hari pengembangan intensif
  * **Total Lines of Code**: 800+ baris
  * **Versi Saat Ini**: 2.0.0 (Beautiful CLI Edition)

### 🎯 Motivasi Project

  * Membuat tool manajemen keuangan yang **sederhana** namun **powerful**
  * **Gratis** dan dapat bekerja **offline** tanpa koneksi internet
  * Solusi yang **accessible** untuk pelajar dan masyarakat umum
  * Membantu membentuk **disiplin finansial** melalui pencatatan rutin

-----

## Fitur Utama

  * **Manajemen Anggaran** — Tetapkan batas anggaran harian dan bulanan sebagai kontrol keuangan
  * **Pencatatan Transaksi** — Catat setiap pemasukan dan pengeluaran dengan mudah dan cepat
  * **Kategorisasi Lengkap** — 7 kategori pengeluaran: Makanan & Minuman, Belanja, Transportasi, Gaya Hidup, Belanja Pokok, Donasi, Lainnya
  * **Laporan Dinamis** — Hasilkan laporan harian atau bulanan sesuai kebutuhan
  * **Analisis Sederhana** — Lihat total saldo, rincian per kategori, dan perbandingan dengan anggaran
  * **Edit Transaksi** — Perbaiki kesalahan pencatatan dengan fitur edit yang fleksibel
  * **ID Transaksi Unik** — Setiap transaksi memiliki ID 9 digit untuk kemudahan penelusuran
  * **Penyimpanan Lokal** — Data aman tersimpan di komputer dalam format CSV dan JSON
  * **CLI yang Indah** — Interface berwarna yang nyaman di mata dengan tabel rapi

-----

## Instalasi

### Prasyarat

  * **Python 3.6+** — Bahasa pemrograman yang menjadi fondasi aplikasi
  * **PIP** — Manajer paket Python (biasanya sudah terinstal bersama Python)

**Library yang Dibutuhkan:**
  * **pandas** — Pengolahan data dan CSV handling (perlu diinstal)
  * **colorama** — Pewarnaan terminal cross-platform (perlu diinstal)
  * **tabulate** — Formatting tabel yang rapi (perlu diinstal)
  * **datetime, os, json, glob** — Built-in libraries (sudah ada di Python)

### Windows

1.  **Unduh Script**
    * Simpan `finansialku.py` di folder yang mudah diakses
    * Contoh: `C:\Users\NamaAnda\Documents\Finansialku`

2.  **Buka Command Prompt**
    * Tekan `Windows + R`, ketik `cmd`, tekan `Enter`
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
    pip install pandas colorama tabulate
    ```

### macOS & Linux

1.  **Unduh Script**
    * Simpan `finansialku.py` di folder yang mudah diakses
    * Contoh: `~/Documents/Finansialku`

2.  **Buka Terminal**
    * **macOS**: `Cmd + Space`, ketik "Terminal"
    * **Linux**: `Ctrl + Alt + T`

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
    pip3 install pandas colorama tabulate
    ```

-----

## Cara Penggunaan

### Menjalankan Aplikasi

**Pastikan virtual environment aktif** (terlihat `(venv)` di awal prompt)

```bash
# Windows
python finansialku.py

# macOS & Linux
python3 finansialku.py
```

**Tampilan Awal:**
```
╔═══════════════════════════════════════════════════════════════════╗
║          🪙  FINANSIALKU: PENCATAT KEUANGAN HARIAN  🪙          ║
╚═══════════════════════════════════════════════════════════════════╝

                            MENU UTAMA
──────────────────────────────────────────────────────────────────────
1. 💰 Mengatur Anggaran              Tetapkan batas pengeluaran...
2. 📈 Mencatat Pemasukan             Catat pendapatan yang Anda...
3. 📉 Mencatat Pengeluaran           Catat pengeluaran dengan...
4. 📊 Laporan Rekap Keuangan         Lihat laporan harian/bulanan
5. ✏️  Edit Rekap Keuangan           Ubah transaksi yang tercatat
6. 🚪 Keluar                         Tutup aplikasi
99. ℹ️  Tentang Aplikasi             Info pembuat & versi
```

### 1. Mengatur Anggaran

**Fungsi:** Menetapkan batas pengeluaran harian dan bulanan

**Langkah:**
  * Pilih opsi **1** dari menu utama
  * Masukkan **anggaran harian** (misal: `50000`)
  * Masukkan **anggaran bulanan** (misal: `1500000`)
  * Sistem menampilkan nilai lama sebagai referensi

**Hasil:**
  * File `anggaran.json` dibuat/diperbarui
  * Anggaran digunakan sebagai pembanding di laporan

**Contoh:**
```
Masukkan batas anggaran harian: 50000
Masukkan batas anggaran bulanan: 1500000

✅ Anggaran berhasil diperbarui
💵 Anggaran Harian: Rp.50,000
💵 Anggaran Bulanan: Rp.1,500,000
```

### 2. Mencatat Pemasukan

**Fungsi:** Mendokumentasikan setiap sumber pendapatan

**Langkah:**
  * Pilih opsi **2** dari menu utama
  * Masukkan **jumlah pemasukan** (misal: `5000000`)
  * Masukkan **deskripsi** (misal: `Gaji bulan November`)
  * Sistem otomatis membuat ID transaksi unik

**Hasil:**
  * Transaksi tercatat dalam file CSV bulan berjalan
  * Saldo global bertambah sesuai jumlah pemasukan
  * ID transaksi format `DDMMYYNNN` dibuat otomatis

**Format ID:** `011125001` = Transaksi pertama tanggal 1 November 2025

### 3. Mencatat Pengeluaran

**Fungsi:** Mencatat pengeluaran dengan kategorisasi detail

**Langkah:**
  * Pilih opsi **3** dari menu utama
  * Masukkan **jumlah pengeluaran** (misal: `25000`)
  * Masukkan **deskripsi** (misal: `Makan siang di kantin`)
  * Pilih **kategori** dari 7 pilihan:
    1. 🍔 Makanan dan Minuman
    2. 🛍️ Belanja
    3. 🚗 Transportasi
    4. 🎭 Gaya Hidup
    5. 🏠 Belanja Pokok
    6. ❤️ Donasi
    7. 📦 Lainnya

**Hasil:**
  * Transaksi tercatat dengan kategori yang dipilih
  * Saldo global berkurang sesuai jumlah pengeluaran
  * Data siap untuk analisis laporan bulanan

### 4. Laporan Rekap Keuangan

**Fungsi:** Menghasilkan laporan keuangan berdasarkan periode

**Langkah:**
  * Pilih opsi **4** dari menu utama
  * Lihat **total saldo** Anda saat ini
  * Pilih jenis laporan:

#### Laporan Harian (Pilihan 1)

**Input:**
  * Masukkan tahun (Enter = tahun ini)
  * Masukkan bulan (Enter = bulan ini)
  * Masukkan tanggal (Enter = hari ini)

**Output:**
  * Total pengeluaran hari tersebut
  * Perbandingan dengan anggaran harian
  * Status: Sisa anggaran atau Overbudget
  * Tabel lengkap semua transaksi hari itu

#### Laporan Bulanan (Pilihan 2)

**Input:**
  * Masukkan tahun (Enter = tahun ini)
  * Masukkan bulan (Enter = bulan ini)

**Output:**
  * Total pemasukan bulan tersebut
  * Total pengeluaran bulan tersebut
  * Saldo bersih (pemasukan - pengeluaran)
  * Rincian pengeluaran per kategori dengan persentase
  * Tabel lengkap semua transaksi bulan tersebut

**Contoh Output Bulanan:**
```
Total Pemasukan: Rp. 5,000,000
Total Pengeluaran: Rp. 1,250,000
**Saldo Bersih: Rp. 3,750,000**

Rincian per Kategori:
Makanan & Minuman    Rp. 650,000    52%
Transportasi         Rp. 300,000    24%
Belanja              Rp. 200,000    16%
```

### 5. Edit Rekap Keuangan

**Fungsi:** Memperbaiki atau mengubah transaksi yang sudah tercatat

**Langkah:**
  * Pilih opsi **5** dari menu utama
  * Masukkan **tahun** transaksi
  * Masukkan **bulan** transaksi
  * Sistem menampilkan semua transaksi di bulan tersebut
  * Masukkan **ID transaksi** (9 digit) yang ingin diubah

**Yang Dapat Diubah:**
  * **Deskripsi** — Ketik baru atau Enter untuk tetap
  * **Tipe Transaksi** — Ubah Pemasukan ↔ Pengeluaran
  * **Jumlah** — Masukkan nilai baru
  * **Kategori** — Pilih kategori baru (untuk pengeluaran)

**Hasil:**
  * File CSV diperbarui dengan data baru
  * Saldo global disesuaikan otomatis
  * Perubahan tersimpan permanen

### 6. Keluar

**Fungsi:** Menutup aplikasi dengan aman

**Langkah:**
  * Pilih opsi **6** dari menu utama
  * Aplikasi menampilkan pesan terima kasih
  * Semua data sudah otomatis tersimpan

-----

## Struktur File

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

**Penjelasan:**
  * `anggaran.json` — Menyimpan anggaran harian, bulanan, dan total saldo
  * `YYYY/` — Folder untuk setiap tahun (dibuat otomatis saat ada transaksi)
  * `MM_YYYY.csv` — File transaksi per bulan
  * **Kolom CSV**: ID, Tanggal, Deskripsi, Pemasukan, Pengeluaran, Kategori

**Format ID Transaksi:** `DDMMYYNNN`
  * `DD` = Tanggal (01-31)
  * `MM` = Bulan (01-12)
  * `YY` = Tahun (2 digit terakhir)
  * `NNN` = Nomor urut transaksi hari itu (001-999)
  * Contoh: `011125001` = Transaksi pertama tanggal 1 November 2025

-----

## Tips Penggunaan

  * **Catat Segera** — Masukkan transaksi langsung setelah terjadi agar tidak lupa
  * **Deskripsi Spesifik** — Gunakan deskripsi yang jelas (misal: "Makan siang di Kantin Bu Ani" bukan hanya "makan")
  * **Konsisten Kategori** — Pilih kategori yang sama untuk jenis pengeluaran sejenis
  * **Review Rutin** — Periksa laporan bulanan setiap awal bulan untuk evaluasi
  * **Sesuaikan Anggaran** — Update anggaran berdasarkan pola pengeluaran Anda setelah beberapa bulan
  * **Backup Berkala** — Salin folder data ke cloud storage atau eksternal drive
  * **Virtual Environment** — Selalu gunakan venv untuk menghindari konflik library
  * **Cek Saldo** — Gunakan laporan keuangan untuk memantau saldo secara berkala
  * **Eksplorasi Menu** — Jangan takut mencoba fitur-fitur yang ada

-----

## Easter Eggs

Aplikasi ini memiliki beberapa **fitur rahasia** yang bisa Anda temukan! 🎉

### 🎭 Menu Rahasia

**Menu 99 - Tentang Aplikasi**
  * **Cara Akses**: Ketik `99` di menu utama
  * **Isi**: Informasi lengkap tentang pembuat, timeline development, technology stack, statistik project, dan cerita di balik pembuatan aplikasi
  * **Bonus**: Lihat dedikasi khusus untuk siswa SMAN 2 Pare!

### 🔮 Angka-Angka Ajaib

Coba ketik angka-angka berikut di menu utama dan lihat apa yang terjadi:

**Angka 42**
  * **Hint**: "The Answer to Life, Universe, and Everything"
  * **Referensi**: Novel sci-fi klasik "The Hitchhiker's Guide to the Galaxy"
  * **Fakta**: Developer aplikasi ini adalah fans berat sci-fi! 🚀

**Angka 2610**
  * **Hint**: Tanggal spesial di bulan Oktober
  * **Clue**: Ini adalah hari dimulainya sesuatu yang special...
  * **Terkait**: Project Finansialku

**Angka 211**
  * **Hint**: Tanggal di bulan November
  * **Clue**: Achievement unlocked! 🎉
  * **Terkait**: Penyelesaian project

### 🔍 Pesan Tersembunyi

**Di Source Code:**
  * Buka file `finansialku.py` dengan text editor
  * Lihat bagian header (paling atas) untuk ASCII art box yang indah
  * Scroll ke bagian paling bawah sebelum `if __name__ == "__main__"`
  * Temukan komentar-komentar rahasia dengan emoji di berbagai fungsi
  * Cari "Developer's Journey" untuk melihat evolusi aplikasi

**Di Terminal:**
  * Tekan `Ctrl+C` saat aplikasi berjalan untuk melihat goodbye message khusus
  * Perhatikan footer di exit screen untuk kontak developer

### 💡 Hints Tambahan

  * Ada **magic numbers** tersembunyi di source code yang merepresentasikan tanggal-tanggal penting
  * Komentar-komentar dalam code penuh dengan emoji dan pesan personal dari developer
  * Setiap fitur punya "Developer Note" yang menjelaskan proses berpikir di balik implementasi
  * Ada fun facts tentang berapa banyak bug yang diperbaiki selama development!

**Challenge:** Bisakah Anda menemukan semua easter egg yang tersembunyi? 🕵️

-----

## Troubleshooting

### ❌ Error: `ModuleNotFoundError: No module named 'pandas'`

**Penyebab:** Library yang diperlukan belum terinstal

**Solusi:**
  * Aktifkan virtual environment terlebih dahulu
  * Windows: `pip install pandas colorama tabulate`
  * macOS/Linux: `pip3 install pandas colorama tabulate`
  * Alternatif: `python -m pip install pandas colorama tabulate`

### ❌ Error: `PermissionError` saat menyimpan file

**Penyebab:** Aplikasi tidak memiliki izin menulis di folder

**Solusi:**
  * **Windows**: Jalankan Command Prompt sebagai Administrator
  * **macOS/Linux**: Periksa permission dengan `ls -la`, ubah dengan `chmod 755`
  * **Semua OS**: Pindahkan aplikasi ke folder dengan akses penuh (misal: Documents)

### ❌ File `anggaran.json` rusak atau kosong

**Penyebab:** File JSON corrupt atau format tidak valid

**Solusi:**
  * Hapus file `anggaran.json`
  * Jalankan aplikasi, file baru dibuat otomatis dengan nilai default 0
  * Atur ulang anggaran melalui menu 1

### ❌ Data transaksi tidak muncul di laporan

**Penyebab:** File CSV mungkin rusak atau format tidak sesuai

**Solusi:**
  * Buka file CSV dengan text editor
  * Periksa format tanggal harus: `DD-MM-YYYY`
  * Pastikan tidak ada baris kosong di tengah data
  * Cek kolom header lengkap: ID, Tanggal, Deskripsi, Pemasukan, Pengeluaran, Kategori

### ❌ Virtual environment tidak bisa diaktifkan di Windows

**Penyebab:** Execution policy Windows membatasi script

**Solusi:**
  * Buka PowerShell sebagai Administrator
  * Jalankan: `Set-ExecutionPolicy RemoteSigned`
  * Ketik `Y` untuk konfirmasi
  * Coba aktifkan venv lagi

### ❌ Warna tidak muncul di terminal

**Penyebab:** Terminal tidak mendukung ANSI colors atau colorama belum terinstal

**Solusi:**
  * Pastikan colorama sudah terinstal: `pip list | grep colorama`
  * Windows: Gunakan Windows Terminal (lebih baik dari cmd biasa)
  * Coba terminal alternatif: ConEmu, Cmder, atau Git Bash

### ❌ Error saat mengedit transaksi

**Penyebab:** ID transaksi tidak ditemukan atau format salah

**Solusi:**
  * Pastikan ID 9 digit diketik dengan benar (tanpa spasi)
  * Cek kembali daftar transaksi yang ditampilkan
  * Pastikan bulan dan tahun sesuai dengan transaksi yang dicari
  * ID bersifat case-sensitive dan harus exact match

-----

## Kontribusi

Aplikasi ini **open-source** dan terbuka untuk kontribusi! 🤝

### 🌟 Cara Berkontribusi

**Fork & Pull Request:**
  * Fork repository ini
  * Buat branch untuk fitur baru: `git checkout -b fitur-baru`
  * Commit perubahan: `git commit -m "Menambahkan fitur X"`
  * Push ke branch: `git push origin fitur-baru`
  * Buat Pull Request dengan deskripsi lengkap

**Laporkan Bug:**
  * Gunakan GitHub Issues untuk melaporkan bug
  * Sertakan langkah-langkah untuk reproduce bug
  * Lampirkan screenshot jika memungkinkan

**Usulkan Fitur:**
  * Buat issue dengan label "enhancement"
  * Jelaskan fitur yang diinginkan dan use case-nya
  * Diskusikan dengan maintainer sebelum mulai coding

### 💡 Ide Pengembangan Masa Depan

  * 📊 Visualisasi grafik tren pengeluaran dengan matplotlib
  * 📄 Export laporan ke PDF atau Excel
  * ⏰ Reminder otomatis untuk pencatatan harian
  * 🔔 Notifikasi saat mendekati batas anggaran
  * 📈 Prediksi pengeluaran berdasarkan pola historis
  * 💱 Dukungan multi-mata uang
  * 🔐 Enkripsi data untuk keamanan ekstra
  * 📱 Versi GUI dengan Tkinter atau PyQt
  * ☁️ Sinkronisasi cloud opsional
  * 🎨 Tema warna yang bisa dikustomisasi

### 📮 Kontak Developer

**M. Farzana Al Fahad** (Lead Developer)
  * 📧 Email: harfanasamsung@gmail.com
  * 🔗 GitHub: [github.com/farzfahd](https://github.com/farzfahd)
  * 💼 LinkedIn: Muhammad Farzana Al Fahad

Jangan ragu untuk menghubungi jika Anda punya pertanyaan, saran, atau ingin berkolaborasi!

-----

## Lisensi

Aplikasi ini dikembangkan untuk keperluan personal dan edukasi. Anda bebas menggunakan, memodifikasi, dan mendistribusikan sesuai kebutuhan.

**MIT License** © 2025 M. Farzana Al Fahad & Irwansyah

-----

## Penutup

**Selamat mengelola keuangan Anda dengan lebih baik! 💰**

Aplikasi Finansialku dibuat dengan harapan dapat membantu siapa saja yang ingin memulai perjalanan menuju kebebasan finansial melalui pencatatan dan manajemen keuangan yang disiplin.

### 🎓 Pesan untuk Pelajar

Khusus untuk siswa-siswi SMAN 2 Pare dan pelajar di mana pun Anda berada:

  * **Jangan takut untuk mencoba** — Coding bukan tentang jadi sempurna dari awal
  * **Belajar dari error** — Setiap bug adalah pembelajaran berharga
  * **Start small, dream big** — Project ini dimulai dari ide sederhana
  * **Kolaborasi itu penting** — Dua kepala lebih baik dari satu
  * **Keep learning** — Technology terus berkembang, kita harus terus belajar

### 🙏 Special Thanks

  * **Python Community** — Untuk ekosistem yang luar biasa
  * **Stack Overflow** — Untuk jawaban semua pertanyaan coding
  * **Guru SMAN 2 Pare** — Untuk dukungan dan bimbingan
  * **Claude AI** — Untuk membantu optimasi kode dan dokumentasi
  * **Gemini AI** — Untuk membantu debugging dan memberikan ide-ide fitur
  * **Keluarga & Teman** — Untuk dukungan moral
  * **Anda** — Untuk menggunakan dan mendukung aplikasi ini! 🎉

---

**Dibuat dengan ❤️ dan ☕ oleh Farzana & Irwansyah**

**Proudly from SMAN 2 Pare, Kediri, Jawa Timur 🎓**
