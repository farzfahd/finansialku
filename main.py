#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    FINANSIALKU: PENCATAT KEUANGAN HARIAN                  ║
║                                                                           ║
║  🎨 Dibuat dengan penuh dedikasi dan cinta untuk membantu mengelola       ║
║     keuangan pribadi dengan lebih baik dan terorganisir                   ║
║                                                                           ║
║  👨‍💻 PEMBUAT UTAMA                                                         ║
║     Nama     : M. Farzana Al Fahad                                        ║
║     Sekolah  : SMAN 2 Pare                                                ║
║     Email    : harfanasamsung@gmail.com                                   ║
║     GitHub   : farzfahd                                                   ║
║     LinkedIn : Muhammad Farzana Al Fahad                                  ║
║                                                                           ║
║  🤝 PEMBUAT PEMBANTU                                                      ║
║     Nama     : Irwansyah                                                  ║
║     Sekolah  : SMAN 2 Pare                                                ║
║                                                                           ║
║  📅 Timeline Project                                                      ║
║     Dimulai  : 26 Oktober 2025                                            ║
║     Selesai  : 2 November 2025                                            ║
║     Durasi   : 8 hari pengembangan intensif                               ║
║                                                                           ║
║  📝 Version: 2.0.0 (Beautiful CLI Edition)                                ║
║  📜 License: MIT License                                                  ║
║                                                                           ║
║  💡 Pesan Rahasia untuk yang membaca source code:                         ║
║     "Keuangan yang sehat dimulai dari pencatatan yang disiplin.           ║
║      Semoga aplikasi ini membantu Anda mencapai kebebasan finansial!"     ║
║                                                                           ║
║  🌟 Special Thanks:                                                       ║
║     - Python Community untuk tools yang luar biasa                        ║
║     - Colorama & Tabulate untuk membuat CLI lebih indah                   ║
║     - Pandas untuk data processing yang powerful                          ║
║     - Guru dan teman-teman SMAN 2 Pare yang mendukung project ini         ║
║     - Claude AI untuk membantu debugging dan optimasi kode                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

🔐 RAHASIA DEVELOPER:
Aplikasi ini adalah project kolaborasi dua siswa SMAN 2 Pare yang berawal 
dari tugas sekolah tentang manajemen keuangan. Apa yang dimulai sebagai 
project sederhana berkembang menjadi aplikasi yang komprehensif dengan fitur
yang jauh melebihi ekspektasi awal.

Dalam 8 hari pengembangan, kami mengalami banyak trial and error, mulai dari
belajar pandas dari nol, memahami datetime manipulation, hingga membuat UI
yang user-friendly dengan colorama. Setiap bug yang diperbaiki mengajarkan
kami sesuatu yang baru tentang programming.

Fun Facts dari perjalanan development:
- Versi 1.0 hanya 200 baris tanpa warna, sekarang 800+ baris dengan full colors
- Menghabiskan 3 hari hanya untuk memperbaiki sistem ID transaksi
- Bug terbesar: lupa strip() whitespace di ID, bikin transaksi hilang!
- Feature favorit: Laporan bulanan dengan breakdown per kategori
- Easter egg menu 99 ditambahkan di hari terakhir sebagai sentuhan personal

Jika Anda membaca ini dan tertarik belajar Python atau berkontribusi,
jangan ragu untuk menghubungi kami! Kami percaya knowledge sharing adalah
kunci pembelajaran yang efektif. Together we grow! 🚀

Pesan khusus untuk siswa/i SMAN 2 Pare yang membaca ini:
"Coding bukan tentang jadi sempurna, tapi tentang terus belajar dan improve.
Jangan takut mencoba project baru, setiap baris kode adalah pembelajaran!"
"""

import datetime
import os
import pandas as pd
import json
import glob
from colorama import Fore, Back, Style, init
from tabulate import tabulate

# Inisialisasi colorama untuk kompatibilitas Windows
# 💭 Rahasia: colorama ini lifesaver untuk Windows users!
# Tanpa ini, warna di Windows Command Prompt bakal berantakan
init(autoreset=True)

FILE_ANGGARAN = 'anggaran.json'
x = 0

# 🎭 EASTER EGG: Variabel rahasia untuk tracking
# Jika user memasukkan 'about' atau '99' di menu, akan muncul info pembuat
SECRET_MENU_TRIGGERED = False

# 🔮 Developer's Magic Numbers (hanya pembuat yang tahu artinya)
# 42 = Answer to everything (Douglas Adams reference - favorit Farzana!)
# 1337 = Leet speak untuk "elite" 
# 2610 = Tanggal mulai project (26 Oktober = 26/10)
# 0211 = Tanggal selesai project (02 November = 02/11)
MAGIC_NUMBER = 42
PROJECT_START = 2610  # 26 Oktober 2025 - Hari dimulainya petualangan coding
PROJECT_END = 211     # 2 November 2025 - Achievement unlocked! 🎉

# ==================== FUNGSI UTILITAS TAMPILAN ====================
# 🎨 Section ini berisi semua fungsi untuk membuat CLI lebih cantik
# Rahasia: Awalnya cuma print() biasa, sekarang full colored! 

def clear_screen():
    """
    Membersihkan layar terminal untuk tampilan yang lebih rapi
    
    💡 Developer Note: Fungsi sederhana tapi impact-nya besar untuk UX!
    Windows pakai 'cls', Unix/Linux/Mac pakai 'clear'
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    """Mencetak header dengan style yang menarik"""
    width = 70
    print("\n" + "=" * width)
    print(f"{Fore.CYAN}{Style.BRIGHT}{text.center(width)}{Style.RESET_ALL}")
    print("=" * width + "\n")

def print_success(text):
    """Mencetak pesan sukses dengan warna hijau"""
    print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ {text}{Style.RESET_ALL}\n")

def print_error(text):
    """Mencetak pesan error dengan warna merah"""
    print(f"\n{Fore.RED}{Style.BRIGHT}✗ {text}{Style.RESET_ALL}\n")

def print_info(text):
    """Mencetak informasi dengan warna biru"""
    print(f"{Fore.BLUE}ℹ {text}{Style.RESET_ALL}")

def print_warning(text):
    """Mencetak peringatan dengan warna kuning"""
    print(f"{Fore.YELLOW}⚠ {text}{Style.RESET_ALL}")

def print_money(label, amount, color=Fore.GREEN):
    """Mencetak informasi uang dengan format yang konsisten"""
    print(f"{label}: {color}{Style.BRIGHT}Rp {amount:,.0f}{Style.RESET_ALL}")

def print_divider():
    """Mencetak garis pemisah"""
    print(f"{Fore.CYAN}{'─' * 70}{Style.RESET_ALL}")

def show_menu():
    """
    Menampilkan menu utama dengan style yang menarik
    
    🎨 Design Philosophy: Menu adalah first impression user!
    Makanya dibuat se-menarik dan se-informatif mungkin
    """
    menu_items = [
        ["1", " 💰 Mengatur Anggaran", "Tetapkan batas pengeluaran harian & bulanan"],
        ["2", " 📈 Mencatat Pemasukan", "Catat pendapatan yang Anda terima"],
        ["3", " 📉 Mencatat Pengeluaran", "Catat pengeluaran dengan kategori"],
        ["4", " 📊 Laporan Rekap Keuangan", "Lihat laporan harian atau bulanan"],
        ["5", " ✏️ Edit Rekap Keuangan", " Ubah transaksi yang sudah tercatat"],
        ["6", " 🚪 Keluar", "Tutup aplikasi"],
        ["99", "ℹ️ Tentang Aplikasi", "Info pembuat & versi aplikasi"]  # 🔐 Secret menu!
    ]
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}{'MENU UTAMA':^70}{Style.RESET_ALL}")
    print_divider()
    
    for item in menu_items:
        print(f"{Fore.CYAN}{Style.BRIGHT}{item[0]}.{Style.RESET_ALL} {Fore.WHITE}{Style.BRIGHT}{item[1]:<30}{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}{item[2]}{Style.RESET_ALL}")
    
    print_divider()

# ==================== FUNGSI INTI APLIKASI ====================

def inputAngkaAman(prompt):
    """Memvalidasi input angka dari user dengan tampilan yang lebih baik"""
    while True:
        try: 
            nilaiInput = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}{prompt}")
            intInput = int(nilaiInput)

            if intInput < 0:
                print_error("Angka tidak boleh kurang dari 0 atau bilangan negatif.")
                continue
            return intInput
        except ValueError:
            print_error("Input tidak valid. Masukkan nilai angka saja.")

def jalurPenyimpanan(tanggal):
    """Menentukan jalur penyimpanan file CSV berdasarkan tanggal"""
    folder = tanggal.strftime("%Y")
    fileCSV = tanggal.strftime("%m_%Y.csv")
    jalurPenuh = os.path.join(folder, fileCSV)

    if not os.path.exists(folder):
        os.makedirs(folder)
        print_info(f"Folder {folder} telah dibuat!")

    return jalurPenuh

def catatTransaksi(ID, deskripsi, kategori, pengeluaran=0, pemasukan=0):
    """Mencatat transaksi ke dalam file CSV"""
    tanggalHariIni = datetime.date.today()
    jalurPencatatan = jalurPenyimpanan(tanggalHariIni)

    dataPencatatan = pd.DataFrame([{
        'ID': ID,
        'Tanggal': tanggalHariIni.strftime('%d-%m-%Y'),
        'Deskripsi': deskripsi,
        'Pemasukan': pemasukan,
        'Pengeluaran': pengeluaran,
        'Kategori': kategori
    }])

    if not os.path.exists(jalurPencatatan):
        dataPencatatan.to_csv(jalurPencatatan, mode='w', header=True, index=False)
        print_info(f"File transaksi baru telah dibuat: {jalurPencatatan}")
    else:
        dataPencatatan.to_csv(jalurPencatatan, mode='a', header=False, index=False)

def urutanID(tanggal):
    """Menentukan urutan ID transaksi pada tanggal tertentu"""
    tanggalStr = tanggal.strftime("%d-%m-%Y")
    jalurCSV = jalurPenyimpanan(tanggal)

    if os.path.exists(jalurCSV):
        df = pd.read_csv(jalurCSV, dtype={'ID': str})
        dfHariIni = df[df['Tanggal'] == tanggalStr]
        dfHariIni = dfHariIni[dfHariIni['ID'].astype(str).str.len() == 9]
        
        urutan = len(dfHariIni) + 1
        return urutan
    else:
        return 1

def generateID(tanggal):
    """Menghasilkan ID unik untuk setiap transaksi"""
    dayID = f"{tanggal.day:02d}"
    monthID = f"{tanggal.month:02d}"
    yearID = tanggal.strftime('%y')

    tanggalID = f"{dayID}{monthID}{yearID}"
    urutan = urutanID(tanggal)

    return f"{tanggalID}{urutan:03d}"

# ==================== FITUR RAHASIA: TENTANG PEMBUAT ====================
# 🎭 Easter egg yang hanya muncul jika user memasukkan '99' di menu
# atau mengetik 'about' di prompt

def show_about():
    """
    Menampilkan informasi tentang pembuat dan aplikasi
    
    🔐 Secret Feature: Ini adalah easter egg yang tersembunyi!
    User bisa akses dengan cara:
    1. Pilih menu 99 (yang muncul di daftar menu)
    2. Ketik 'about' di prompt manapun (upcoming feature)
    
    💭 Developer's Thought: Setiap aplikasi harus punya 'soul' dan cerita
    di baliknya. Ini adalah tempat dimana cerita kolaborasi kami diceritakan.
    
    🏫 Made with pride by SMAN 2 Pare students!
    """
    clear_screen()
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}")
    print("╔═══════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                           ║")
    print("║                  ℹ️  TENTANG FINANSIALKU - VERSI 2.0.0                    ║")
    print("║                                                                           ║")
    print("╚═══════════════════════════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}📱 Informasi Aplikasi{Style.RESET_ALL}")
    print_divider()
    print(f"{Fore.WHITE}Nama         : {Fore.CYAN}Finansialku - Pencatat Keuangan Harian{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Versi        : {Fore.CYAN}2.0.0 (Beautiful CLI Edition){Style.RESET_ALL}")
    print(f"{Fore.WHITE}Tanggal Mulai: {Fore.CYAN}26 Oktober 2025{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Tanggal Rilis: {Fore.CYAN}2 November 2025{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Durasi       : {Fore.CYAN}8 hari pengembangan intensif{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Lisensi      : {Fore.CYAN}MIT License - Free & Open Source{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Bahasa       : {Fore.CYAN}Python 3.6+{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}👨‍💻 Tim Pengembang{Style.RESET_ALL}")
    print_divider()
    
    # Pembuat Utama
    print(f"\n{Fore.GREEN}{Style.BRIGHT}PEMBUAT UTAMA:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Nama         : {Fore.GREEN}{Style.BRIGHT}M. Farzana Al Fahad{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Sekolah      : {Fore.GREEN}SMAN 2 Pare{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Email        : {Fore.GREEN}harfanasamsung@gmail.com{Style.RESET_ALL}")
    print(f"{Fore.WHITE}GitHub       : {Fore.GREEN}github.com/farzfahd{Style.RESET_ALL}")
    print(f"{Fore.WHITE}LinkedIn     : {Fore.GREEN}linkedin.com/in/Muhammad Farzana Al Fahad{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Role         : {Fore.GREEN}Lead Developer, System Architecture, Core Logic{Style.RESET_ALL}")
    
    # Pembuat Pembantu
    print(f"\n{Fore.CYAN}{Style.BRIGHT}PEMBUAT PEMBANTU:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Nama         : {Fore.CYAN}{Style.BRIGHT}Irwansyah{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Sekolah      : {Fore.CYAN}SMAN 2 Pare{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Role         : {Fore.CYAN}Testing, Debugging, Feature Ideas{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}💡 Filosofi Aplikasi{Style.RESET_ALL}")
    print_divider()
    print(f"{Fore.LIGHTBLACK_EX}\"Keuangan yang sehat dimulai dari pencatatan yang disiplin.{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX} Aplikasi ini dibuat untuk membantu siapa saja mencapai{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX} kebebasan finansial melalui manajemen keuangan yang lebih baik.\"{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🛠️ Technology Stack{Style.RESET_ALL}")
    print_divider()
    tech_stack = [
        ["Python 3.6+", "Core programming language"],
        ["Pandas", "Data processing & CSV handling"],
        ["Colorama", "Cross-platform colored terminal"],
        ["Tabulate", "Beautiful table formatting"],
        ["JSON", "Configuration & budget storage"],
        ["Datetime", "Transaction date management"],
        ["OS & Glob", "File system operations"]
    ]
    print(tabulate(tech_stack, headers=['Library', 'Fungsi'], tablefmt='grid'))
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🌟 Fitur Utama{Style.RESET_ALL}")
    print_divider()
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Manajemen anggaran harian & bulanan")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Pencatatan pemasukan & pengeluaran dengan 7 kategori")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Laporan keuangan dinamis (harian & bulanan)")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Edit transaksi dengan update otomatis")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} ID transaksi unik 9 digit untuk setiap pencatatan")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Penyimpanan lokal yang aman (CSV & JSON)")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Interface CLI yang indah dengan warna")
    print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Rincian pengeluaran per kategori dengan persentase")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}📊 Statistik Pengembangan{Style.RESET_ALL}")
    print_divider()
    print(f"  {Fore.CYAN}📝{Style.RESET_ALL} Total Lines of Code  : {Fore.WHITE}800+ baris{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}⏱️ {Style.RESET_ALL}Waktu Pengembangan   : {Fore.WHITE}8 hari (26 Okt - 2 Nov 2025){Style.RESET_ALL}")
    print(f"  {Fore.CYAN}☕{Style.RESET_ALL} Cangkir Kopi/Teh     : {Fore.WHITE}0{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}🐛{Style.RESET_ALL} Bug Fixed            : {Fore.WHITE}Banyak sekali, terutama masalah ID!{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}💪{Style.RESET_ALL} Motivasi             : {Fore.WHITE}100% Student Passion Project!{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}🏫{Style.RESET_ALL} Pride of             : {Fore.WHITE}SMAN 2 Pare 🎓{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🎯 Cerita di Balik Aplikasi{Style.RESET_ALL}")
    print_divider()
    print(f"{Fore.WHITE}Finansialku adalah hasil kolaborasi dua siswa SMAN 2 Pare yang berawal{Style.RESET_ALL}")
    print(f"{Fore.WHITE}dari keinginan sederhana untuk membuat aplikasi pencatat keuangan yang{Style.RESET_ALL}")
    print(f"{Fore.WHITE}mudah digunakan. Project ini mengajarkan kami banyak hal tentang Python,{Style.RESET_ALL}")
    print(f"{Fore.WHITE}manajemen data, dan pentingnya user experience dalam software development.{Style.RESET_ALL}")
    print(f"\n{Fore.WHITE}Dalam 8 hari pengembangan, kami belajar dari nol tentang pandas, datetime,{Style.RESET_ALL}")
    print(f"{Fore.WHITE}dan bagaimana membuat CLI yang tidak hanya fungsional tapi juga indah.{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Setiap bug adalah pelajaran, setiap fitur baru adalah achievement! 🚀{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🙏 Special Thanks To{Style.RESET_ALL}")
    print_divider()
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Python Community - untuk ekosistem yang luar biasa")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Stack Overflow - untuk jawaban semua pertanyaan coding")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} GitHub - untuk platform berbagi kode")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Claude AI - untuk membantu debugging dan optimasi")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Guru SMAN 2 Pare - untuk dukungan dan bimbingan")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Keluarga & Teman - untuk dukungan moral")
    print(f"  {Fore.MAGENTA}♥{Style.RESET_ALL} Anda - untuk menggunakan aplikasi ini! 🎉")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}📮 Ingin Berkontribusi atau Memberikan Feedback?{Style.RESET_ALL}")
    print_divider()
    print(f"{Fore.WHITE}Aplikasi ini open-source dan terbuka untuk kontribusi!{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Silakan fork repository, buat pull request, atau kirim feedback ke:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}📧 harfanasamsung@gmail.com{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🔗 github.com/farzfahd/finansialku{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🎓 Pesan untuk Pelajar SMAN 2 Pare{Style.RESET_ALL}")
    print_divider()
    print(f"{Fore.WHITE}Jika kalian membaca ini dan tertarik belajar coding, don't be afraid!{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Kami juga mulai dari nol. Yang penting adalah curiosity dan kemauan{Style.RESET_ALL}")
    print(f"{Fore.WHITE}untuk terus belajar. Setiap project, sekecil apapun, adalah langkah{Style.RESET_ALL}")
    print(f"{Fore.WHITE}menuju improvement. Keep coding, keep learning! 💻🚀{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'─' * 75}{Style.RESET_ALL}")
    print(f"\n{Fore.LIGHTBLACK_EX}    Dibuat dengan ❤️  dan ☕ oleh M. Farzana Al Fahad & Irwansyah{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}               Proudly from SMAN 2 Pare 🎓{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}              © 2025 - All Rights Reserved{Style.RESET_ALL}\n")
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali ke menu...{Style.RESET_ALL}")

def muatAnggaran():
    """Memuat data anggaran dari file JSON"""
    if os.path.exists(FILE_ANGGARAN):
        with open(FILE_ANGGARAN, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {'anggaran_harian': 0, 'anggaran_bulanan': 0, 'sisa_uang': 0, "tabungan": {"Sepatu": 100000}}
                unggahAnggaran(data)
                print_warning("File anggaran rusak/kosong. Menggunakan nilai default")
    else:
        data = {'anggaran_harian': 0, 'anggaran_bulanan': 0, 'sisa_uang': 0, "tabungan": {}}
    
    return data

def unggahAnggaran(dataAnggaran):
    """Menyimpan data anggaran ke file JSON"""
    with open(FILE_ANGGARAN, 'w') as f:
        json.dump(dataAnggaran, f, indent=4)

def mengaturAnggaran():
    """Fitur untuk mengatur anggaran harian dan bulanan"""
    clear_screen()
    print_header("💰 PENGATURAN ANGGARAN")

    anggaranLama = muatAnggaran()

    tabunganLama = anggaranLama.get('tabungan', {})

    print_info("Anggaran saat ini:")
    print_money("  • Harian ", anggaranLama['anggaran_harian'], Fore.CYAN)
    print_money("  • Bulanan", anggaranLama['anggaran_bulanan'], Fore.CYAN)
    print()

    promptAnggaranHarian = f"Masukkan batas anggaran harian: "
    harianBaru = inputAngkaAman(promptAnggaranHarian)

    promptAnggaranBulanan = f"Masukkan batas anggaran bulanan: "
    bulananBaru = inputAngkaAman(promptAnggaranBulanan)

    dataBaru = {
        'anggaran_harian': harianBaru, 
        'anggaran_bulanan': bulananBaru, 
        'sisa_uang': anggaranLama['sisa_uang'],
        'tabungan': tabunganLama
    }
    unggahAnggaran(dataBaru)

    print_success("Anggaran berhasil diperbarui!")
    print_money("💵 Anggaran Harian ", dataBaru['anggaran_harian'], Fore.GREEN)
    print_money("💵 Anggaran Bulanan", dataBaru['anggaran_bulanan'], Fore.GREEN)
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali ke menu...{Style.RESET_ALL}")

# ==================== FITUR KEDUA: PENCATATAN PEMASUKAN ====================

def mencatatPemasukan():
    """Fitur untuk mencatat pemasukan"""
    clear_screen()
    print_header("📈 MENCATAT PEMASUKAN")
    
    dataLama = muatAnggaran()
    tanggal = datetime.date.today()
    
    tabunganLama = dataLama.get('tabungan', {})

    jumlah = inputAngkaAman('Masukkan jumlah pemasukan (Rp): ')
    deskripsi = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan deskripsi: ")
    kategori = "Pemasukan"

    transaksiID = generateID(tanggal)
    jumlahPositif = abs(jumlah)
    catatTransaksi(transaksiID, deskripsi, pemasukan=jumlahPositif, kategori=kategori)

    dataPemasukan = {
        'anggaran_harian': dataLama['anggaran_harian'],
        'anggaran_bulanan': dataLama['anggaran_bulanan'],
        'sisa_uang': dataLama['sisa_uang'] + jumlahPositif,
        'tabungan': tabunganLama
    }

    unggahAnggaran(dataPemasukan)

    print_success(f"Pemasukan berhasil dicatat!")
    print(f"  {Fore.CYAN}ID Transaksi:{Style.RESET_ALL} {transaksiID}")
    print_money("  Jumlah      ", jumlahPositif, Fore.GREEN)
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali ke menu...{Style.RESET_ALL}")

# ==================== FITUR KETIGA: PENCATATAN PENGELUARAN ====================
def pengeluaranMenabung():
    angaran = muatAnggaran()

def mencatatPengeluaran():
    """Fitur untuk mencatat pengeluaran"""
    clear_screen()
    print_header("📉 MENCATAT PENGELUARAN")
    
    dataLama = muatAnggaran()
    tanggal = datetime.date.today()

    tabunganLama = dataLama.get('tabungan', {})

    jumlah = inputAngkaAman('Masukkan jumlah pengeluaran (Rp): ')
    print(f"\n{Fore.CYAN}Pilih Kategori Pengeluaran:{Style.RESET_ALL}")
    kategori_list = [
        ["1", "🍔 Makanan dan Minuman"],
        ["2", "🛍️ Belanja"],
        ["3", "🚗 Transportasi"],
        ["4", "🎭 Gaya Hidup"],
        ["5", "🏠 Belanja Pokok"],
        ["6", "❤️ Donasi"],
        ["7", "📦 Lainnya"]
    ]
    
    for kat in kategori_list:
        print(f"  {kat[0]}. {kat[1]}")
    
    kategori = inputAngkaAman("\nMasukkan kategori (1-7): ")

    deskripsi = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan deskripsi: ")
    
    dictKategori = {
        1: "Makanan dan Minuman", 
        2: "Belanja", 
        3: "Transportasi", 
        4: "Gaya Hidup", 
        5: "Belanja Pokok", 
        6: "Donasi", 
        7: "Lainnya"
    }
    
    transaksiID = generateID(tanggal)
    catatTransaksi(transaksiID, deskripsi, pengeluaran=jumlah, kategori=dictKategori[kategori])

    dataPengeluaran = {
        'anggaran_harian': dataLama['anggaran_harian'],
        'anggaran_bulanan': dataLama['anggaran_bulanan'],
        'sisa_uang': dataLama['sisa_uang'] - jumlah,
        'tabungan': tabunganLama
    }

    unggahAnggaran(dataPengeluaran)

    print_success(f"Pengeluaran berhasil dicatat!")
    print(f"  {Fore.CYAN}ID Transaksi:{Style.RESET_ALL} {transaksiID}")
    print(f"  {Fore.CYAN}Kategori    :{Style.RESET_ALL} {dictKategori[kategori]}")
    print_money("  Jumlah      ", jumlah, Fore.RED)
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali ke menu...{Style.RESET_ALL}")

# ==================== FITUR KEEMPAT: LAPORAN KEUANGAN ====================

def muatSemuaTransaksi():
    """Memuat semua transaksi dari semua file CSV"""
    semuaFile = glob.glob(os.path.join('**', '*.csv'), recursive=True)

    fileTransaksi = [f for f in semuaFile
                     if f.count('_') == 1 and f.endswith('.csv') and os.path.basename(f) != 'anggaran.json']
    
    if not fileTransaksi:
        return pd.DataFrame({
            'ID': [], 'Tanggal': [], 'Deskripsi': [], 
            'Pemasukan': [], 'Pengeluaran': [], 'Kategori': []
        })
    
    try:
        listDF = [pd.read_csv(f, dtype={'ID': str}) for f in fileTransaksi]
        semuaDF = pd.concat(listDF, ignore_index=True)

        semuaDF['Tanggal'] = pd.to_datetime(semuaDF['Tanggal'], format='%d-%m-%Y')
        semuaDF['ID'] = semuaDF['ID'].str.strip()

        return semuaDF

    except Exception as e:
        print_error(f"Error saat penggabungan file: {e}")
        return pd.DataFrame()

def muatTransaksiBulan(bulan, tahun):
    """Memuat transaksi dari bulan dan tahun tertentu"""
    namaFolder = str(tahun)
    namaFile = f"{bulan:02d}_{tahun}.csv"
    jalurFile = os.path.join(namaFolder, namaFile)

    if os.path.exists(jalurFile):
        try:
            df = pd.read_csv(jalurFile, dtype={'ID': str})
            df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d-%m-%Y')
            df['ID'] = df['ID'].str.strip()
            return df
        except pd.errors.EmptyDataError:
            print_error(f"File data {namaFile} kosong!")
            return pd.DataFrame()
        except Exception as e:
            print_error(f"Error saat membaca CSV: {e}")
            return pd.DataFrame()
    else:
        return pd.DataFrame()

def laporanHarian(dfSemua):
    """Menampilkan laporan transaksi harian"""
    today = datetime.date.today()
    anggaran = muatAnggaran()

    while True:
        try:
            tahun_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Tahun (YYYY, default {today.year}): ")
            tahun = int(tahun_str) if tahun_str else today.year
            if tahun < 0: raise ValueError("Tahun tidak boleh negatif.")
            
            bulan_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Bulan (MM, default {today.month:02d}): ")
            bulan = int(bulan_str) if bulan_str else today.month
            if bulan < 1 or bulan > 12: raise ValueError("Bulan tidak valid (1-12).")

            hari_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Tanggal (DD, default {today.day:02d}): ")
            hari = int(hari_str) if hari_str else today.day
            
            tanggalPilihan = datetime.date(tahun, bulan, hari).strftime('%d-%m-%Y')
            break 
        except ValueError as e:
            print_error(f"Input tidak valid: {e}. Masukkan angka yang benar.")
        except Exception:
            print_error("Tanggal tidak valid (misalnya, tanggal 30 di Februari). Coba lagi.")

    clear_screen()
    print_header(f"📅 LAPORAN HARIAN - {tanggalPilihan}")

    dfPilihan = dfSemua[dfSemua['Tanggal'].dt.strftime('%d-%m-%Y') == tanggalPilihan]

    if dfPilihan.empty:
        print_warning("Tidak ada transaksi pada hari tersebut")
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
        return

    pengeluaranPilihan = dfPilihan['Pengeluaran'].sum()
    sisaAnggaran = anggaran['anggaran_harian'] - pengeluaranPilihan

    # Ringkasan anggaran
    print(f"{Fore.CYAN}Ringkasan Anggaran:{Style.RESET_ALL}")
    print_money("  Batas Harian  ", anggaran['anggaran_harian'], Fore.CYAN)
    print_money("  Total Keluar  ", pengeluaranPilihan, Fore.RED)
    
    if sisaAnggaran >= 0:
        print_money("  Sisa Anggaran ", sisaAnggaran, Fore.GREEN)
    else:
        print_money("  Overbudget    ", abs(sisaAnggaran), Fore.RED)
    
    print_divider()

    # Tabel transaksi
    print(f"\n{Fore.CYAN}Daftar Transaksi:{Style.RESET_ALL}\n")
    
    # Format DataFrame untuk ditampilkan
    df_display = dfPilihan[['ID', 'Deskripsi', 'Pemasukan', 'Pengeluaran', 'Kategori']].copy()
    df_display['Pemasukan'] = df_display['Pemasukan'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    df_display['Pengeluaran'] = df_display['Pengeluaran'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    
    print(tabulate(df_display, headers='keys', tablefmt='grid', showindex=False))
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")

def laporanBulanan(dfSemua):
    """Menampilkan laporan transaksi bulanan"""
    today = datetime.date.today()
    anggaran = muatAnggaran()

    while True:
        try:
            tahun_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Tahun (YYYY, default {today.year}): ")
            tahun = int(tahun_str) if tahun_str else today.year
            if tahun < 0: raise ValueError("Tahun tidak boleh negatif.")

            bulan_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Bulan (MM, default {today.month:02d}): ")
            bulan = int(bulan_str) if bulan_str else today.month
            if bulan < 1 or bulan > 12: raise ValueError("Bulan tidak valid (1-12).")
            
            break
        except ValueError as e:
            print_error(f"Input tidak valid: {e}. Masukkan angka yang benar.")

    clear_screen()
    print_header(f"📊 LAPORAN BULANAN - {bulan:02d}/{tahun}")

    dfSemua['Bulan_Tahun'] = dfSemua['Tanggal'].dt.to_period('M')
    targetPeriod = pd.Period(f'{tahun}-{bulan:02d}', 'M')

    dfPilihan = dfSemua[dfSemua['Bulan_Tahun'] == targetPeriod].copy()

    if dfPilihan.empty:
        print_warning("Tidak ada transaksi pada bulan tersebut")
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
        return

    pemasukan = dfPilihan['Pemasukan'].sum()
    pengeluaran = dfPilihan['Pengeluaran'].sum()
    saldoBulan = pemasukan - pengeluaran
    
    # Ringkasan bulanan
    print(f"{Fore.CYAN}Ringkasan Bulanan:{Style.RESET_ALL}")
    print_money("  Total Masuk   ", pemasukan, Fore.GREEN)
    print_money("  Total Keluar  ", pengeluaran, Fore.RED)
    print_divider()
    
    if saldoBulan >= 0:
        print_money("  Saldo Bersih  ", saldoBulan, Fore.GREEN)
    else:
        print_money("  Defisit       ", abs(saldoBulan), Fore.RED)
    
    print_divider()

    # Rincian per kategori
    print(f"\n{Fore.CYAN}Rincian Pengeluaran per Kategori:{Style.RESET_ALL}\n")
    laporanKategori = dfPilihan.groupby('Kategori')['Pengeluaran'].sum().sort_values(ascending=False)
    
    kategori_data = []
    for kategori, jumlah in laporanKategori.items():
        if jumlah > 0:  # Hanya tampilkan kategori yang ada pengeluarannya
            persentase = (jumlah / pengeluaran * 100) if pengeluaran > 0 else 0
            kategori_data.append([kategori, f"Rp {jumlah:,.0f}", f"{persentase:.1f}%"])
    
    if kategori_data:
        print(tabulate(kategori_data, headers=['Kategori', 'Jumlah', 'Persentase'], tablefmt='grid'))
    
    print_divider()

    # Tabel semua transaksi
    print(f"\n{Fore.CYAN}Semua Transaksi Bulan {bulan:02d}/{tahun}:{Style.RESET_ALL}\n")
    
    df_display = dfPilihan[['ID', 'Tanggal', 'Deskripsi', 'Pemasukan', 'Pengeluaran', 'Kategori']].copy()
    df_display['Tanggal'] = df_display['Tanggal'].dt.strftime('%d-%m-%Y')
    df_display['Pemasukan'] = df_display['Pemasukan'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    df_display['Pengeluaran'] = df_display['Pengeluaran'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    
    print(tabulate(df_display, headers='keys', tablefmt='grid', showindex=False))
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")

def laporanKeuangan():
    """Menu utama untuk laporan keuangan"""
    clear_screen()
    print_header("📊 LAPORAN REKAP KEUANGAN")

    dfSemua = muatSemuaTransaksi()

    if dfSemua.empty:
        print_warning("Data transaksi masih kosong. Tidak ada laporan yang bisa ditampilkan.")
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
        return
    
    totalSaldo = dfSemua['Pemasukan'].sum() - dfSemua['Pengeluaran'].sum()
    print_money("💰 Total Saldo Anda", totalSaldo, Fore.GREEN if totalSaldo >= 0 else Fore.RED)
    print_divider()

    print(f"\n{Fore.CYAN}Pilih Jenis Laporan:{Style.RESET_ALL}")
    print("  1. 📅 Laporan Harian")
    print("  2. 📊 Laporan Bulanan")

    pilihanLaporan = inputAngkaAman("\nMasukkan pilihan (1 atau 2): ")

    if pilihanLaporan == 1:
        laporanHarian(dfSemua=dfSemua)
    elif pilihanLaporan == 2: 
        laporanBulanan(dfSemua)
    else:
        print_error('Masukkan pilihan yang valid!')
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")

# ==================== FITUR KELIMA: EDIT TRANSAKSI ====================

def cariTransaksi(IDTransaksi, bulan, tahun):
    """Mencari transaksi berdasarkan ID, bulan, dan tahun"""
    namaFolder = str(tahun)
    namaFile = f"{bulan:02d}_{tahun}.csv" 
    jalurFile = os.path.join(namaFolder, namaFile)

    if not os.path.exists(jalurFile):
        return pd.DataFrame(), None
    
    try: 
        df = pd.read_csv(jalurFile, dtype={'ID': str})
        df['ID'] = df['ID'].str.strip()
        dfTransaksi = df[df['ID'] == IDTransaksi].copy()

        if not dfTransaksi.empty:
            return dfTransaksi, jalurFile
    except Exception:
        pass

    return pd.DataFrame(), None

def updateSaldoGlobal(barisLama, pemasukanBaru, pengeluaranBaru, tipeLama):
    """Memperbarui saldo global setelah edit transaksi"""
    dataLama = muatAnggaran()
    sisaUangLama = dataLama['sisa_uang']
    
    # Kembalikan transaksi lama
    if tipeLama == 'Pemasukan':
        sisaUangLama -= int(barisLama['Pemasukan'])
    else:
        sisaUangLama += int(barisLama['Pengeluaran'])

    # Terapkan transaksi baru
    sisaUangBaru = sisaUangLama + pemasukanBaru - pengeluaranBaru
    dataLama['sisa_uang'] = int(sisaUangBaru) 

    dataLama['anggaran_harian'] = int(dataLama['anggaran_harian'])
    dataLama['anggaran_bulanan'] = int(dataLama['anggaran_bulanan'])
    
    unggahAnggaran(dataLama)
    print_money("💰 Saldo global diperbarui", int(sisaUangBaru), Fore.GREEN)

def editTransaksi(dfLama, jalurFile):
    """Mengedit transaksi yang sudah ada"""
    barisLama = dfLama.iloc[0].copy()
    IDTarget = barisLama['ID']

    clear_screen()
    print_header("✏️  EDIT TRANSAKSI")
    
    print(f"{Fore.CYAN}Data Transaksi Lama:{Style.RESET_ALL}\n")
    data_lama = [[
        barisLama['ID'],
        barisLama['Tanggal'],
        barisLama['Deskripsi'],
        f"Rp {barisLama['Pemasukan']:,.0f}" if barisLama['Pemasukan'] > 0 else "-",
        f"Rp {barisLama['Pengeluaran']:,.0f}" if barisLama['Pengeluaran'] > 0 else "-",
        barisLama['Kategori']
    ]]
    print(tabulate(data_lama, headers=['ID', 'Tanggal', 'Deskripsi', 'Pemasukan', 'Pengeluaran', 'Kategori'], tablefmt='grid'))
    print_divider()

    deskripsiBaru = input(f"\n{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Deskripsi baru (Enter = tetap): ")
    if not deskripsiBaru:
        deskripsiBaru = barisLama['Deskripsi']

    tipeLama = 'Pemasukan' if barisLama['Pemasukan'] > 0 else 'Pengeluaran'
    jumlahLama = barisLama['Pemasukan'] if barisLama['Pemasukan'] > 0 else barisLama['Pengeluaran']

    print(f"\n{Fore.CYAN}Transaksi Lama:{Style.RESET_ALL} {tipeLama} - Rp {jumlahLama:,.0f}")
    print("\n1. Tetap dengan tipe yang sama")
    print("2. Ubah tipe transaksi")
    pilihanTipe = inputAngkaAman("\nPilihan (1/2): ")
    
    promptJumlah = f"Masukkan Jumlah baru (Enter = Rp {jumlahLama:,.0f}): "
    jumlahInput = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}{promptJumlah}")
    jumlahBaru = int(jumlahInput) if jumlahInput else jumlahLama
    
    pemasukanBaru = 0
    pengeluaranBaru = 0
    kategoriBaru = barisLama['Kategori']

    if pilihanTipe == 2:
        tipeBaru = 'Pengeluaran' if tipeLama == 'Pemasukan' else 'Pemasukan'
        print_info(f"Tipe diubah menjadi: {tipeBaru}")
    else:
        tipeBaru = tipeLama

    if tipeBaru == 'Pemasukan':
        kategoriBaru = 'Pemasukan'
        pemasukanBaru = jumlahBaru
    else: 
        pengeluaranBaru = jumlahBaru
        
        print(f"\n{Fore.CYAN}Pilih Kategori Baru:{Style.RESET_ALL}")
        kategori_list = [
            ["1", "🍔 Makanan dan Minuman"],
            ["2", "🛍️ Belanja"],
            ["3", "🚗 Transportasi"],
            ["4", "🎭 Gaya Hidup"],
            ["5", "🏠 Belanja Pokok"],
            ["6", "❤️ Donasi"],
            ["7", "📦 Lainnya"]
        ]
        
        for kat in kategori_list:
            print(f"  {kat[0]}. {kat[1]}")
        
        kategoriIndex = inputAngkaAman(f"\nMasukkan kategori (1-7, default = {barisLama['Kategori']}): ")
        dictKategori = {
            1: "Makanan dan Minuman", 
            2: "Belanja", 
            3: "Transportasi", 
            4: "Gaya Hidup", 
            5: "Belanja Pokok", 
            6: "Donasi", 
            7: "Lainnya"
        }
        kategoriBaru = dictKategori.get(kategoriIndex, barisLama['Kategori'])

    # Update file CSV
    dfBulanPenuh = pd.read_csv(jalurFile, dtype={'ID': str})
    indexBaris = dfBulanPenuh[dfBulanPenuh['ID'] == IDTarget].index

    if not indexBaris.empty:
        dfBulanPenuh.loc[indexBaris, 'Deskripsi'] = deskripsiBaru
        dfBulanPenuh.loc[indexBaris, 'Pemasukan'] = pemasukanBaru
        dfBulanPenuh.loc[indexBaris, 'Pengeluaran'] = pengeluaranBaru
        dfBulanPenuh.loc[indexBaris, 'Kategori'] = kategoriBaru

        dfBulanPenuh.to_csv(jalurFile, mode="w", header=True, index=False)

        updateSaldoGlobal(barisLama, pemasukanBaru, pengeluaranBaru, tipeLama)
        
        print_success("Transaksi berhasil diperbarui!")
    else:
        print_error("Gagal menemukan ID dalam file. Tidak ada yang diubah.")
    
    input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")

def fiturEditKeuangan():
    """Menu utama untuk edit transaksi"""
    clear_screen()
    print_header("✏️  EDIT TRANSAKSI KEUANGAN")
    
    today = datetime.date.today()
    
    while True:
        try:
            tahun_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Tahun (YYYY, default {today.year}): ")
            tahun = int(tahun_str) if tahun_str else today.year
            if tahun < 0: raise ValueError("Tahun tidak boleh negatif.")
            
            bulan_str = input(f"{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan Bulan (MM, default {today.month:02d}): ")
            bulan = int(bulan_str) if bulan_str else today.month
            if bulan < 1 or bulan > 12: raise ValueError("Bulan tidak valid (1-12).")
            
            break
        except ValueError as e:
            print_error(f"Input tidak valid: {e}. Masukkan angka yang benar.")

    dfPilihan = muatTransaksiBulan(bulan, tahun) 
    
    if dfPilihan.empty:
        print_warning(f"Tidak ada transaksi pada bulan {bulan:02d}/{tahun}. Tidak ada yang bisa diedit.")
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
        return
    
    clear_screen()
    print_header(f"✏️  TRANSAKSI BULAN {bulan:02d}/{tahun}")
    
    df_display = dfPilihan[['ID', 'Tanggal', 'Deskripsi', 'Pemasukan', 'Pengeluaran', 'Kategori']].copy()
    df_display['Tanggal'] = pd.to_datetime(df_display['Tanggal']).dt.strftime('%d-%m-%Y')
    df_display['Pemasukan'] = df_display['Pemasukan'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    df_display['Pengeluaran'] = df_display['Pengeluaran'].apply(lambda x: f"Rp {x:,.0f}" if x > 0 else "-")
    
    print(tabulate(df_display, headers='keys', tablefmt='grid', showindex=False))
    print_divider()

    transaksiID = input(f"\n{Fore.YELLOW}➜ {Style.RESET_ALL}Masukkan ID Transaksi (9 digit): ")

    dfLama, jalurFile = cariTransaksi(transaksiID, bulan, tahun)

    if dfLama.empty:
        print_error(f"Transaksi dengan ID '{transaksiID}' tidak ditemukan di bulan {bulan:02d}/{tahun}.")
        input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
        return

    editTransaksi(dfLama, jalurFile)

# ==================== PROGRAM UTAMA ====================

def main():
    """
    Fungsi utama program - The heart of everything! ❤️
    
    🎯 Design Pattern: Main loop dengan error handling yang comprehensive
    
    💭 Developer's Journey:
    Versi 1.0: Simple while True dengan try-except basic
    Versi 2.0: Added graceful exit, KeyboardInterrupt handling, dan easter egg!
    
    🔐 Secret: Coba ketik angka ajaib untuk surprise! 😉
    
    🏫 Created by: Farzana & Irwansyah (SMAN 2 Pare)
    """
    global x
    
    while True:
        if x == 0:
            clear_screen()
            print(f"\n{Fore.CYAN}{Style.BRIGHT}")
            print("╔═══════════════════════════════════════════════════════════════════╗")
            print("║                                                                   ║")
            print("║          🪙  FINANSIALKU: PENCATAT KEUANGAN HARIAN  🪙            ║")
            print("║                                                                   ║")
            print("║              Kelola Keuangan Anda dengan Lebih Baik               ║")
            print("║                                                                   ║")
            print("╚═══════════════════════════════════════════════════════════════════╝")
            print(Style.RESET_ALL)
            
            # Informasi pembuat yang terlihat di welcome screen
            print(f"{Fore.LIGHTBLACK_EX}{'Dibuat oleh M. Farzana Al Fahad & Irwansyah | SMAN 2 Pare':^70}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}{'Version 2.0.0 | © 2025 | Ketik 99 untuk info lengkap':^70}{Style.RESET_ALL}\n")
            x = 1

        try:
            show_menu()
            fitur = inputAngkaAman("Silakan pilih fitur (1-6): ")

            if fitur == 1:
                mengaturAnggaran()
            elif fitur == 2:
                mencatatPemasukan()
            elif fitur == 3:
                mencatatPengeluaran()
            elif fitur == 4:
                laporanKeuangan()
            elif fitur == 5:
                fiturEditKeuangan()
            elif fitur == 6:
                clear_screen()
                print(f"\n{Fore.CYAN}{Style.BRIGHT}")
                print("╔═══════════════════════════════════════════════════════════════════╗")
                print("║                                                                   ║")
                print("║           Terima kasih telah menggunakan Finansialku! 🙏          ║")
                print("║                                                                   ║")
                print("║                Semoga keuangan Anda selalu sehat! 💰              ║")
                print("║                                                                   ║")
                print("╚═══════════════════════════════════════════════════════════════════╝")
                print(Style.RESET_ALL)
                print(f"\n{Fore.LIGHTBLACK_EX}       Dibuat dengan ❤️  oleh Farzana & Irwansyah (SMAN 2 Pare){Style.RESET_ALL}")
                print(f"{Fore.LIGHTBLACK_EX}               github.com/farzfahd | harfanasamsung@gmail.com{Style.RESET_ALL}\n")
                break
            elif fitur == 99:
                # 🎭 EASTER EGG! Menu rahasia tentang pembuat
                show_about()
            elif fitur == 42:
                # 🔮 SUPER SECRET! Developer's favorite number
                clear_screen()
                print(f"\n{Fore.MAGENTA}{Style.BRIGHT}")
                print("🎉 Selamat! Anda menemukan Easter Egg rahasia! 🎉")
                print(f"\n{Fore.YELLOW}Angka 42 adalah 'Answer to Life, Universe, and Everything'")
                print(f"berdasarkan novel 'The Hitchhiker's Guide to the Galaxy'")
                print(f"\n{Fore.CYAN}Fun fact: Developer aplikasi ini (Farzana) adalah fans berat sci-fi! 🚀")
                print(f"{Fore.CYAN}Favorite movies: Interstellar, The Martian, Inception{Style.RESET_ALL}\n")
                input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
            elif fitur == 2610:
                # 🎊 SECRET: Tanggal mulai project!
                clear_screen()
                print(f"\n{Fore.GREEN}{Style.BRIGHT}")
                print("🎊 Wow! Anda menemukan tanggal special: 26 Oktober 2025! 🎊")
                print(f"\n{Fore.CYAN}Ini adalah hari pertama kami memulai project Finansialku!")
                print(f"{Fore.CYAN}Hari dimana perjalanan coding 8 hari yang intens dimulai...")
                print(f"{Fore.CYAN}From zero to hero in 8 days! 💪{Style.RESET_ALL}\n")
                input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
            elif fitur == 211:
                # 🎉 SECRET: Tanggal selesai project!
                clear_screen()
                print(f"\n{Fore.GREEN}{Style.BRIGHT}")
                print("🎉 Achievement Unlocked! Tanggal 2 November 2025! 🎉")
                print(f"\n{Fore.CYAN}Ini adalah hari dimana Finansialku versi 2.0 selesai!")
                print(f"{Fore.CYAN}8 hari pengembangan, puluhan bug fixed, ratusan line of code...")
                print(f"{Fore.CYAN}Dan akhirnya, aplikasi ini siap membantu mengelola keuangan Anda! 🚀")
                print(f"\n{Fore.YELLOW}Total effort: Farzana (Lead Dev) + Irwansyah (Helper)")
                print(f"{Fore.YELLOW}Location: SMAN 2 Pare, Kediri, Indonesia 🇮🇩{Style.RESET_ALL}\n")
                input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk kembali...{Style.RESET_ALL}")
            else:
                print_error("Pilihan tidak valid! Masukkan angka 1-6 (atau 99 untuk info).")
                input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
                
        except ValueError:
            print_error("Input tidak valid! Masukkan angka 1-6.")
            input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")
        except KeyboardInterrupt:
            # Handle Ctrl+C dengan elegan
            clear_screen()
            print(f"\n\n{Fore.YELLOW}Program dihentikan oleh user. Sampai jumpa! 👋{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Terima kasih telah menggunakan Finansialku ❤️{Style.RESET_ALL}")
            print(f"{Fore.LIGHTBLACK_EX}Created by Farzana & Irwansyah - SMAN 2 Pare{Style.RESET_ALL}\n")
            break
        except Exception as e:
            print_error(f"Terjadi kesalahan: {e}")
            input(f"\n{Fore.LIGHTBLACK_EX}Tekan Enter untuk melanjutkan...{Style.RESET_ALL}")

if __name__ == "__main__":
    # 🚀 Program starts here!
    # Pesan rahasia: Jika Anda membaca ini, semoga harimu menyenangkan! 😊
    # 
    # Special dedication untuk siswa-siswi SMAN 2 Pare yang membaca source code ini:
    # "Coding is not about being perfect, it's about constant improvement.
    #  Setiap project adalah pembelajaran. Keep coding, keep growing! 💻🚀"
    # 
    # - Farzana & Irwansyah, November 2025
    main()