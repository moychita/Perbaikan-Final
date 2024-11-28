def hitung_tabungan_awal(saldo, bunga, tahun):
    riwayat_saldo = [] 
    for i in range(1, tahun + 1):
        saldo += saldo * (bunga / 100)
        riwayat_saldo.append(saldo)  
        print(f"Tahun {i}: Saldo Anda adalah Rp {saldo:,.2f}") 
    return saldo, riwayat_saldo

def format_riwayat(riwayat):
    return "\n".join([f"Tahun {i + 1}: Rp {saldo:,.2f}" for i, saldo in enumerate(riwayat)])

def main():
    print("=== Kalkulator Pertumbuhan Tabungan ===")
    try:
        saldo_awal = float(input("Masukkan jumlah tabungan awal (Rp): "))
        bunga_tahunan = float(input("Masukkan suku bunga tahunan (%): "))
        jumlah_tahun = int(input("Masukkan jumlah tahun: "))

        if saldo_awal <= 0 or bunga_tahunan <= 0 or jumlah_tahun <= 0:
            print("Semua input harus bernilai positif.")
        else:
            saldo_akhir, riwayat_saldo = hitung_tabungan_awal(saldo_awal, bunga_tahunan, jumlah_tahun)
            print("\n=== Riwayat Tabungan Anda ===")
            print(format_riwayat(riwayat_saldo)) 
            print(f"\nTotal tabungan Anda setelah {jumlah_tahun} tahun adalah Rp {saldo_akhir:,.2f}")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")

if __name__ == "__main__":
    main()