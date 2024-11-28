# KALKULATOR PRTUMBUHAN TABUNGAN
Program ini merupakan kalkulator yang digunakan untuk menghitung pertumbuhan tabungan berdasarkan saldo awal, suku bunga tahunan, dan jangka waktu tertentu. Program ini menghitung saldo tabungan setiap tahun dan menampilkan riwayat saldo serta saldo akhir setelah jangka waktu yang ditentukan.

# Fitur

	•	Menghitung pertumbuhan tabungan berdasarkan suku bunga tahunan.
	•	Menampilkan saldo tabungan per tahun.
	•	Menyimpan dan menampilkan riwayat saldo setiap tahun dalam format yang rapi.
	•	Menampilkan total saldo akhir setelah periode tertentu.

# Cara Penggunaan

	1.	Jalankan program melalui editor python.
	2.	Program akan meminta Anda untuk memasukkan beberapa input:
	•	Jumlah tabungan awal (dalam Rupiah).
	•	Suku bunga tahunan (dalam persen).
	•	Jumlah tahun (periode waktu untuk perhitungan).
	3.	Program akan menghitung dan menampilkan saldo per tahun beserta total saldo setelah jumlah tahun yang ditentukan.
	4.	Riwayat saldo tabungan akan ditampilkan dengan format yang rapi.

# Penjelasan Program

1. Fungsi hitung_tabungan_awal(saldo, bunga, tahun)

Fungsi ini digunakan untuk menghitung saldo setiap tahun berdasarkan saldo awal, suku bunga tahunan, dan jangka waktu (dalam tahun). Setiap tahun, bunga ditambahkan ke saldo, dan saldo tersebut disimpan dalam list riwayat_saldo untuk ditampilkan nanti.

2. Fungsi format_riwayat(riwayat)

Fungsi ini digunakan untuk memformat list riwayat_saldo menjadi string yang rapi dengan mencantumkan tahun dan saldo yang sesuai.

3. Fungsi main()

Fungsi utama yang mengatur alur program, meminta input dari pengguna, dan menampilkan hasil perhitungan serta riwayat saldo tabungan.