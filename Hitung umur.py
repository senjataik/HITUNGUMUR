from datetime import datetime

def hitung_umur(tanggal_lahir):
    # Konversi string tanggal lahir ke format datetime
    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
    # Tanggal hari ini
    hari_ini = datetime.now()
    # Hitung umur
    umur_tahun = hari_ini.year - tanggal_lahir.year
    # Periksa apakah ulang tahun sudah lewat tahun ini
    if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
        umur_tahun -= 1
    return umur_tahun

# Input tanggal lahir dari pengguna
tanggal_lahir_input = input("Masukkan tanggal lahir Anda (format: YYYY-MM-DD): ")
try:
    umur = hitung_umur(tanggal_lahir_input)
    print(f"Umur Anda adalah {umur} tahun.")
except ValueError:
    print("Format tanggal yang dimasukkan tidak valid. Harap gunakan format YYYY-MM-DD.")
