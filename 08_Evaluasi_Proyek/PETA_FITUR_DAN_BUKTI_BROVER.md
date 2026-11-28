# Peta Fitur dan Bukti BROVER

- **Untuk:** Tim Asprak, sebagai pegangan menyusun ulang `PROJECT_CONCEPT_BROVER.md` dan membangun prototipe.
- **Tanggal:** 28 November 2026.
- **Judul proyek, tidak berubah:** BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler.
- **Isi dokumen:**
  1. keputusan tim;
  2. gambaran sistem dalam satu halaman;
  3. empat kartu fitur final, masing-masing berisi masalah yang dijawab, fungsi, cara kerja, alat, data, model, jurnal, contoh, batas, dan pekerjaan tim;
  4. fitur yang dihapus beserta alasannya;
  5. perbedaan skrining dan diagnosis;
  6. lampiran ringkas;
  7. daftar perbaikan berprioritas;
  8. tabel tautan.
- **Label status:**
  - **Terverifikasi:** isi sumber dibaca dan cocok dengan klaim.
  - **Parsial:** sebagian cocok, atau hanya judul dan abstrak yang terbaca.
  - **Tidak dapat diverifikasi:** sumber tertutup atau tidak bisa diakses.
- **Batas dokumen:**
  - Harga diambil dari BOM concept Bab 8.2, kecuali yang disebut lain.
  - Situs jurnal studi kasus broiler Cianjur tidak bisa diakses, jadi studi itu tidak dipakai.
  - Beberapa makalah lama hanya terbaca judul dan abstraknya, dan ditandai demikian.

---

## 1. Keputusan Tim per 28 November 2026

1. **Judul tetap.** Frasa *Skrining Gejala Penyakit* dipertahankan, karena BROVER bukan alat diagnosis.
2. **AI hanya satu:** CV feses, yaitu Model #1.
3. **Dihapus:** AI audio, CV fisik dan perilaku ayam, deteksi bangkai, serta sensor CO2 pada MVP.
4. **SHT31 dan SEN0567 tetap di rover**, dipasang di tiang setinggi ayam. Node sensor tetap tidak dipakai.
5. **Mode stasiun:** saat tidak berkeliling, termasuk malam hari dan hari ke-0 sampai 6, rover parkir di dok di dalam kandang dan terus mencatat suhu, kelembapan, dan amonia setiap menit.
6. **Amonia disajikan sebagai tren** terhadap garis dasar per zona dan per jam yang sama. SEN0567 dikalibrasi terhadap alat acuan saat pilot.
7. **Foto feses diambil oleh rover** dengan sudut dan lampu seragam.
   - **Kamera:** kamera USB IMX291 dipasang pada servo tahan air DS3218 dengan dua posisi:
     - posisi depan sekitar 0 sampai 15 derajat untuk tampilan FPV saat operator menyetir, dan kelak untuk CV navigasi;
     - posisi bawah sekitar 45 derajat untuk foto feses.
   - **Dua peran foto HP:** cadangan saat rover tidak bisa masuk pada paket BROVER Kandang, dan jalur utama pada paket BROVER Saku.
8. **Rover beroperasi setiap hari dari hari ke-7 sampai panen**, dinaikkan bertahap dengan kriteria berhenti. Jadwalnya 2 putaran di MVP, yaitu pagi dan sore pukul 15.00 sampai 16.00, lalu 3 putaran setelah otomatisasi. Rover tidak berkeliling terus-menerus.
9. **Kamera termal** hanya untuk riset lanjutan.
10. **Kasus Hari Farm**, yang merupakan peternakan ayam petelur, diganti dengan sumber broiler.
11. **Sinkronisasi dokumen dikerjakan pada 28 November 2026.**
    - Concept, README, dan MEMORY repo mengikuti dokumen ini.
    - Status setiap butir Bab 7 dicatat di `EVALUASI_ULANG_BROVER.md`.
12. **Dua paket langganan:**
    - **BROVER Saku** untuk peternak kecil, Rp75.000 per siklus. Isinya CV feses lewat foto HP dan semua fitur dasbor kecuali data sensor.
    - **BROVER Kandang** untuk peternak menengah dan besar, Rp750.000 per siklus dengan kontrak minimal 6 siklus. Isinya rover lengkap per kandang, dan tersedia juga opsi beli putus.
    - Tagihan per siklus dipilih karena RHPP kemitraan terbit 3 sampai 7 hari setelah panen.
    - Rincian dan titik impasnya ada di concept Bab 9.2.
13. **Jalur inferensi:**
    - BROVER Kandang memproses foto di Orange Pi.
    - BROVER Saku memproses foto HP di server pusat. Foto diantre saat luring.
    - Jalur Saku dibangun setelah inferensi rover berjalan.
    - Inferensi langsung di HP menjadi riset lanjutan.
14. **Satu model, rover dulu:**
    - Satu detektor Apache-2.0 diekspor ke RKNN INT8 dan ONNX FP32.
    - Set uji lokal memuat foto rover dan foto HP berpasangan.
    - BROVER Saku baru dijual setelah akurasi pada foto HP diukur dan model disesuaikan.
15. **Otomatisasi rover tetap riset lanjutan P2.** Prototipe dikendalikan manual.

---

## 2. Gambaran Sistem dalam Satu Halaman

| Fitur | Masalah yang Dijawab | Alat Utama | Jenis |
| :--- | :--- | :--- | :--- |
| F1 Rover Inspeksi dan Foto HP | Foto feses yang seragam di titik zona yang sama setiap hari | Rover dengan kamera IMX291 pada servo DS3218 dua posisi, lampu LED, dan dok di dalam kandang. Aplikasi web untuk unggah foto HP, yang menjadi jalur utama paket BROVER Saku. | Platform |
| F2 Sensor Mikroklimat di Rover | Cekaman panas dan faktor pemicu penyakit pernapasan, yaitu amonia dan kelembapan | SHT31 dan SEN0567 di tiang rover, aktif saat putaran dan saat parkir di dok | Aturan standar umur Cobb dan Ross |
| F3 CV Feses | Skrining tanda penyakit pencernaan pada feses | Orange Pi 3B dengan detektor INT8 | **AI** |
| F4 Dasbor | Menyatukan semua data menjadi daftar tindakan dan laporan ke dokter hewan | Aplikasi web dan server cloud | Aturan dan tampilan |

**Alur kerja harian:**
1. **Di luar jam putaran,** rover parkir di dok di dalam kandang dan mencatat suhu, kelembapan, dan tren amonia setiap menit. Pada hari ke-0 sampai 6, rover hanya berada di dok.
2. **Pagi dan sore pukul 15.00 sampai 16.00,** operator menjalankan rover ke titik zona tetap. Di setiap titik, rover berhenti, mencatat mikroklimat zona, menyalakan lampu, lalu memotret feses. Saat rover tidak bisa masuk, ABK memotret dengan HP.
3. **Orange Pi** menjalankan CV feses. Pada paket BROVER Saku, foto HP diproses di server pusat dengan model yang sama. Feses yang tampak abnormal masuk daftar triase.
4. **ABK mengisi catatan harian:** ayam mati dan afkir, pakan terpakai, angka meteran air, dan ceklis gejala pernapasan seperti ngorok atau bersin.
5. **Dasbor** menampilkan status per parameter, tren harian, dan daftar triase dengan 3 tombol: *Akan Saya Cek*, *Terlihat Normal*, dan *Laporkan ke Dokter Hewan*.
6. **Laporan 1-klik** mengirim bukti foto, grafik lingkungan, dan catatan harian ke dokter hewan. Diagnosis tetap dilakukan dokter hewan.

---

## 3. Kartu Fitur

### F1. Rover Inspeksi Pembawa Kamera Feses, dengan Unggah Foto HP

- **Masalah yang dijawab:** model CV butuh foto feses yang seragam. Foto acak dari HP berbeda sudut, jarak, dan cahaya. Rover memberi titik zona, sudut, dan lampu yang sama setiap hari.
- **Fungsi:** membawa kamera menyusuri lorong kandang untuk memotret feses di titik zona tetap.
- **Cara kerja:**
  1. Setiap hari ada 2 putaran di MVP, yaitu pagi dan sore pukul 15.00 sampai 16.00. Operator menyetir rover lewat halaman web di HP. *Dead-man switch* 500 ms menghentikan motor bila sinyal putus.
  2. Di setiap titik zona, rover berhenti, mencatat mikroklimat zona untuk F2, dan menyalakan LED 5000K. Lalu servo memiringkan kamera ke posisi bawah sekitar 45 derajat untuk memotret sekam. Selama berjalan, kamera berada di posisi depan sekitar 0 sampai 15 derajat untuk tampilan FPV operator.
  3. Foto langsung diproses F3 di Orange Pi.
  4. Selesai putaran, rover kembali ke dok di dalam kandang untuk diisi daya sambil tetap mencatat mikroklimat. Ini mode stasiun.
  5. Bila rover tidak bisa masuk, ABK mengunggah foto HP lewat aplikasi web yang sama. Foto itu dikirim lewat Wi-Fi lokal ke Orange Pi. Pada paket BROVER Saku, foto HP adalah jalur utama dan diproses di server pusat.
- **Alat dan harga eceran dari BOM concept:**
  - Orange Pi 3B, Rp1.950.000;
  - kamera IMX291, Rp550.000;
  - servo tahan air DS3218, Rp215.000;
  - LED 5000K, Rp50.000;
  - sensor jarak A02YYUW, Rp410.000;
  - dok pengisian di dalam kandang, yang sudah ada di BOM sebagai *Cleaning Dock* Rp200.000, ditambah stopkontak di dalam kandang;
  - motor, roda, sasis, baterai LiFePO4 yang tahan 3 sampai 4 jam, dan kelistrikan.
- **Data dan model:** tidak ada model. Rover adalah platform.
- **Batas operasi:** setiap hari dari hari ke-7 sampai panen, dinaikkan bertahap. Alasannya ada di Lampiran 6.1.
- **Kenapa rover tidak berkeliling terus-menerus:**
  1. Setiap kali lewat, robot membuat ayam di zona itu menyingkir. Robot [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) hanya bergerak 2 jam per hari, dan penulisnya menyebut belum ada data untuk paparan yang lebih lama. Robot [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) berjalan 3 kali sehari.
  2. Robot yang memantau 24 jam, yaitu [ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf), berjalan di rel di atas ayam, bukan di lantai.
  3. Panduan Cobb 2021 menyebut periode gelap penting bagi kekebalan dan konversi pakan, sehingga rover tidak berkeliling pada malam hari.
  4. Penulis SmartEars memilih alat yang diam karena lebih sedikit menimbulkan stres dibanding robot yang berkeliling.
  5. Baterai rover hanya tahan 3 sampai 4 jam.
  6. Data terus-menerus sudah didapat dari mode stasiun, dan cakupan zona dari putaran.

  Setelah otomatisasi, putaran bisa naik menjadi 3 per hari, ditambah putaran khusus bila THI atau amonia di dok melewati ambang.

| Jurnal Rujukan | Isi | Status |
| :--- | :--- | :-: |
| [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) | Robot dikemudikan manual untuk mengukur iklim setinggi ayam, hari 3 sampai 37, pada 1.597 Ross 308. Gangguan perilaku terbatas, kematian dan produksi tetap wajar. | Terverifikasi dari abstrak |
| [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) | Robot 6,2 kg dengan *ground clearance* 4 sampai 8 cm, hari 7 sampai 42, kandang komersial Cobb 500 sampai 32 kg per m2. Gangguan terbesar terjadi pada minggu pertama. | Terverifikasi |
| [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | Ayam umur 2 sampai 8 minggu. Robot tidak menimbulkan stres lebih besar daripada manusia. | Terverifikasi dari abstrak |
| [Balthazar dkk. 2024](https://doi.org/10.3390/ani14071014) | Robot terlalu lambat, yaitu 0,04 m/s menurut [teks penuhnya](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/), membuat ayam tidak menyingkir sehingga terjadi benturan | Terverifikasi |

- **Contoh yang sudah ada:**
  - [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/): robot penggaru sekam yang juga mencatat suhu, kelembapan, dan amonia.
  - [ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf): robot rel gantung yang memantau sepanjang siklus.
- **Batas jujur:**
  - Kamera hanya merekam pita lantai di sepanjang jalur rover.
  - Operator harus menyetir selama sesi.
  - Belum ada uji robot di closed house tropis Indonesia.
  - Juri bisa bertanya kenapa tidak cukup memakai HP. Jawabannya: sudut, lampu, dan titik zona yang seragam membuat masukan model konsisten. Untuk peternak kecil yang tidak membutuhkan rover, tersedia paket BROVER Saku berbasis foto HP.
- **Pekerjaan tim:**
  - pasang bumper depan lunak;
  - ubah aturan sensor jarak dari berhenti total menjadi memperlambat laju;
  - kecepatan awal 0,07 sampai 0,1 m/s;
  - tambahkan fitur unggah foto HP;
  - tempatkan dok di dalam kandang, di area *brooding* atau tengah kandang, lengkap dengan stopkontak;
  - buat jadwal putaran dan mode stasiun di firmware dan dasbor;
  - pasang kamera IMX291 pada servo DS3218 dengan dua posisi, yaitu depan untuk FPV dan bawah untuk feses. Dua kamera USB tetap, satu menghadap depan dan satu menghadap bawah, hanya cadangan bila servo bermasalah saat uji lapangan.

### F2. Sensor Mikroklimat di Rover: Suhu, Kelembapan, dan Tren Amonia

- **Masalah yang dijawab:**
  - **Cekaman panas.** Suhu di atas 32,8 derajat dan THI di atas 79 pada pukul 16.00 memprediksi kematian broiler, menurut [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111).
  - **Pemicu penyakit pernapasan.** Menurut [Medion 2026](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/), penyakit pernapasan bakterial dipicu ventilasi buruk, kepadatan, amonia tinggi, dan fluktuasi cuaca. Penyakit yang disebut adalah CRD, CRD kompleks, colibacillosis, coryza, dan fowl cholera. Amonia tinggi juga disebut memicu ILT.
- **Fungsi:** mengukur kondisi udara setinggi ayam di setiap zona saat putaran, dan terus-menerus di satu titik saat rover parkir di dok, lalu memberi status dan rekomendasi tindakan.
- **Cara kerja:**
  1. SHT31 dan SEN0567 dipasang di tiang rover setinggi ayam, jauh dari panas Orange Pi dan motor supaya bacaan suhu tidak bias.
  2. **Saat putaran,** rover berhenti di titik zona tetap, misalnya dekat inlet, tengah, dan dekat kipas, sampai bacaan stabil. Lama berhenti ditentukan saat pilot.
  3. **Saat parkir di dok,** rover mencatat setiap menit. Ini mode stasiun. Pada hari ke-0 sampai 6, rover hanya berada di dok.
  4. Suhu dan kelembapan dibandingkan dengan tabel standar umur Cobb atau Ross, lalu THI dihitung.
  5. Amonia ditampilkan sebagai tren. Data per zona dibandingkan dengan data jam yang sama di hari-hari sebelumnya, dan data dok dibandingkan dengan garis dasarnya. Saat pilot, SEN0567 dikalibrasi terhadap alat acuan pinjaman, supaya ambang 10 dan 25 ppm bisa dipakai.
  6. Dasbor menampilkan status per parameter, yaitu Normal, Waspada, atau Bahaya, beserta tindakan yang disarankan. Tidak ada skor 0 sampai 100.
- **Alat dan biaya:** tidak ada tambahan biaya. Probe SHT31 Rp325.000 dan SEN0567 Rp230.000 sudah ada di BOM concept, begitu pula dok sebagai *Cleaning Dock*. Yang perlu disiapkan hanya stopkontak di dalam kandang.
- **Kenapa tidak memakai node sensor tetap:**
  - [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) menulis bahwa kandang broiler besar hanya punya sedikit sensor tetap, letaknya sering jauh di atas zona ayam, dan memasang jaringan sensor tetap yang rapat tidak hemat biaya. Robot yang berkeliling bisa mengukur iklim setinggi ayam di banyak lokasi.
  - [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) juga mencatat suhu, kelembapan, dan amonia sambil bekerja.
  - Celah waktu di antara putaran ditutup oleh mode stasiun. Alarm kipas mati atau listrik padam tetap menjadi tugas kontroler closed house, yang di Indonesia sudah memakai kontrol lingkungan otomatis menurut [Rosyida dkk. 2026](https://doi.org/10.48084/etasr.17149).
- **Data dan model:** tidak memakai AI. Fitur ini memakai aturan dari panduan resmi dan jurnal.

| Parameter | Target atau Ambang | Sumber |
| :--- | :--- | :--- |
| Suhu dan RH per umur | Tabel standar umur | [Panduan Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf), tabel Ross di concept Bab 4.2 |
| THI sore | Waspada bila suhu di atas 32,8 derajat atau THI di atas 79 | Mohammadi dkk. 2026 |
| RH | Di bawah 65 persen. Tabel RH Cobb berhenti di 70 persen, sehingga aturan untuk RH tropis yang lebih tinggi perlu dibuat bersama dokter hewan. | Panduan Cobb 2021 |
| NH3 | Target di bawah 10 ppm. Waspada sekitar 10 sampai 15 ppm. Bahaya sekitar 25 ppm atau lebih. | Cobb 2021, Barbosa 2024, Zhou 2020, Quarles dan Kling 1974, Bist 2022 |

**Dasar ilmiah hubungan amonia dengan penyakit pernapasan:**

| Sumber | Temuan | Status |
| :--- | :--- | :-: |
| [Quarles dan Kling 1974](https://doi.org/10.3382/ps.0531592) | Broiler terpapar amonia 25 dan 50 ppm pada umur 4 sampai 8 minggu, lalu divaksin IB. Hasilnya **airsacculitis berat** pada minggu 6 dan 8, bakteri di udara naik, dan karkas yang ditolak bertambah. | Terverifikasi dari abstrak |
| [Anderson dkk. 1964](https://doi.org/10.2307/1587967) | Judulnya: amonia menurunkan ketahanan terhadap virus ND. Pendahuluannya mencatat amonia 50 sampai 100 ppm di kandang tertutup. | Parsial, hasil lengkap tidak terbaca |
| [Liu dkk. 2020](https://doi.org/10.1016/j.psj.2020.03.019) | Amonia selama 7 hari menaikkan bakteri *Escherichia/Shigella* di paru dan memicu radang paru. Ini berkaitan dengan colibacillosis. | Terverifikasi dari abstrak |
| [Zhou dkk. 2020](https://doi.org/10.1016/j.psj.2019.12.063) dan [Zhou dkk. 2021](https://doi.org/10.1016/j.psj.2020.11.026) | 15 ppm selama 3 hari memicu radang trakea dan mengubah bakteri di trakea. 25 sampai 35 ppm menurunkan pertumbuhan. | Terverifikasi dari abstrak |
| [Miles dkk. 2004](https://doi.org/10.1093/ps/83.10.1650) | 50 dan 75 ppm menurunkan bobot 6 dan 9 persen. 75 ppm menaikkan kematian menjadi 13,9 persen, dibanding 5,8 persen. | Terverifikasi dari abstrak |
| [Miles dkk. 2006](https://doi.org/10.1637/7386-052405r.1) | 25 sampai 75 ppm merusak mata. Jaringan saluran napas tidak terpengaruh pada level yang diuji. | Terverifikasi dari abstrak |
| [Beker dkk. 2004](https://doi.org/10.1093/japr/13.1.5) dan [Al-Mashhadani dan Beck 1985](https://doi.org/10.3382/ps.0642056) | Lesi trakea dan paru akibat amonia saja tidak konsisten pada kadar sedang | Terverifikasi dari abstrak |
| [Vučemilo dkk. 2008](https://doi.org/10.17221/329-cjas) | Di kandang 22.000 Ross 308, amonia naik dari 5 ppm di awal menjadi 25 ppm di akhir pemeliharaan. Endotoksin udara mencapai 99,4 EU per m3. | Terverifikasi dari abstrak |
| [Barbosa dkk. 2024](https://doi.org/10.3390/ani14040615) | *Machine learning* memprediksi risiko paparan amonia dan mengaitkannya dengan lesi trakea, bronkus, paru, mata, dan telapak kaki. Risiko sedang didefinisikan 10 sampai 14 ppm. Penelitian memakai sensor elektrokimia Dräger pada 1.250 ekor di Spanyol. | Terverifikasi |
| [Saputra dkk. 2020](https://jurnal.uns.ac.id/Sains-Peternakan/article/download/31636/26596) | Memakai istilah *mikroklimatik amonia*. Di closed house 60 m dan 120 m, amonia berkorelasi positif kuat dengan kelembapan dan kecepatan angin. | Terverifikasi |
| [Fajaryani dkk. 2024](https://journals.unpad.ac.id/jptt/article/download/48211/23878) | CO2 dan amonia yang terlalu tinggi mengganggu pernapasan, menurunkan daya tahan, dan menaikkan deplesi | Terverifikasi |

**Cara membaca bukti:** amonia **tidak bisa menunjuk nama penyakit**. Amonia adalah faktor pemicu yang memperberat penyakit pernapasan. Bukti terkuatnya ada pada airsacculitis dan colibacillosis bila amonia disertai pemicu lain, kerusakan mata, serta penurunan performa pada kadar tinggi. Karena itu, di proposal tulis *amonia meningkatkan risiko penyakit pernapasan*, bukan *amonia menyebabkan CRD*.

**Rekomendasi tindakan untuk peternak:**

| Kondisi | Tindakan |
| :--- | :--- |
| Amonia naik dari garis dasar, atau sekitar 10 sampai 15 ppm setelah kalibrasi | Cek kelembapan sekam dengan uji kepal dari panduan Cobb, cek tetesan nipple, tambah siklus ventilasi minimum. Ganti sekam yang basah dan tambahkan kapur bila perlu, sesuai saran Medion. |
| Sekitar 25 ppm atau lebih | Ventilasi segera. Konsultasikan dengan dokter hewan sebelum vaksinasi pernapasan. Saran ini kesimpulan dari studi Quarles dan Kling. |
| 50 ppm atau lebih | Darurat. Bobot turun, dan pada 75 ppm kematian naik. |
| RH di atas 65 persen | Atasi sumber air dan kelembapan, karena menurut Cobb amonia tinggi biasanya terkait kelembapan tinggi dan sekam basah |
| Waktu rawan | Pantau lebih ketat saat ventilasi minimum masa *brooding*, saat tirai ditutup karena malam atau hujan, dan di akhir siklus |
| Amonia tinggi dan ABK mencatat ngorok atau bersin | Laporkan ke dokter hewan. Nama penyakit hanya bisa dipastikan dengan uji laboratorium. |

- **Contoh yang sudah ada:**
  - Robot [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) dan [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/): mengukur iklim kandang sambil berkeliling.
  - [Lashari dkk. 2023](https://doi.org/10.7717/peerj-cs.1623): pembanding berupa node tetap nirkabel di farm broiler yang mengukur suhu, RH, O2, CO2, CO, dan NH3, dengan sensor NH3 elektrokimia yang dikalibrasi berkala.
  - [Studi sensor IoT 2025](https://doi.org/10.1016/j.atech.2025.101197): sensor amonia murah MQ-137 dikalibrasi terhadap alat industri, R 0,82.
- **Batas jujur:**
  - Data per zona hanya ada pada jam putaran. Data terus-menerus hanya ada di satu titik, yaitu lokasi dok.
  - Keliling terjadwal otomatis masih pengembangan lanjutan. Di MVP, putaran disetir operator.
  - Menurut [wiki resmi](https://wiki.dfrobot.com/sen0567/), SEN0567 hanya kualitatif dan bekerja pada RH 15 sampai 90 persen tanpa embun. Padahal RH kandang Jawa Barat rata-rata 81,9 persen dan bisa sampai 96 persen, menurut [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052).
  - Kepekaan SEN0567 terhadap gas lain tidak dicantumkan.
  - CO2 tidak diukur pada MVP. Alasannya ada di Bab 4.3.
- **Pekerjaan tim:**
  - pasang tiang sensor setinggi ayam, jauh dari sumber panas rover;
  - tempatkan dok di dalam kandang dengan stopkontak, di area *brooding* atau tengah kandang;
  - lapisi papan sirkuit agar tahan disinfektan, belajar dari pengalaman SmartEars;
  - tentukan lama berhenti per zona dan kalibrasi SEN0567 saat pilot;
  - buat logika tren amonia per zona dan per jam;
  - tetapkan ambang dan aturan RH bersama Dr. drh. Atin Supiyani, M.Si.

### F3. CV Feses, Model #1, Satu-satunya AI

- **Masalah yang dijawab:** menurut panduan Cobb 2021, *perubahan mendadak tampilan feses* adalah salah satu tanda penyakit yang harus dikenali pekerja kandang. Grafik klinis broiler Medion yang dikutip concept menempatkan koksidiosis di peringkat tiga.
- **Fungsi:** menandai feses yang tampak abnormal sebagai kandidat untuk dicek. Keluarannya berbunyi *pola feses mirip koksidiosis, perlu konfirmasi dokter hewan*, bukan *ayam terkena koksidiosis*.
- **Cara kerja:**
  1. Pada paket BROVER Kandang, foto rover dan foto HP cadangan masuk ke Orange Pi lewat Wi-Fi lokal. Pada paket BROVER Saku, foto HP diantre di aplikasi saat luring, lalu diproses di server pusat dengan ONNX Runtime CPU.
  2. Detektor menandai area feses beserta kelas dan tingkat keyakinannya. Satu model dilatih untuk foto rover terlebih dahulu, lalu diekspor ke RKNN INT8 untuk Orange Pi dan ONNX FP32 untuk server.
  3. Temuan masuk daftar triase F4.
  4. ABK memilih satu dari tiga tombol. Pilihan *Terlihat Normal* menjadi data latih perbaikan.

| Dataset | Isi | Jenis Ayam dan Kondisi | Lisensi | Peran |
| :--- | :--- | :--- | :--- | :--- |
| [Zenodo 4628934](https://zenodo.org/records/4628934) | 6.812 citra dengan label YOLO dan segmentasi. Audit TA menemukan berkas kosong dan kotak cacat. | Petelur, persilangan, dan ayam lokal di Tanzania | CC BY 4.0 | Data latih utama setelah label dibersihkan |
| [Zenodo 5801834](https://zenodo.org/records/5801834) | 1.255 citra berlabel PCR, untuk klasifikasi saja, tanpa label YOLO | Sama dengan di atas | CC BY 4.0 | Uji klasifikasi berlabel laboratorium |
| [Mendeley 8pnbzpt2k9](https://data.mendeley.com/datasets/8pnbzpt2k9/1) | 14.618 citra 100 x 100 piksel, sehat atau tidak sehat | **Broiler dan petelur**, Nigeria | CC BY 4.0 | Tambahan data sehat dan tidak sehat |
| Set uji lokal BROVER | Foto feses broiler di atas sekam, berlabel dokter hewan dan hitungan OPG untuk koksidiosis | Broiler Indonesia | Milik tim | **Wajib** untuk klaim akurasi. Cukup set uji kecil, bukan dataset penuh. |

| Model | Tugas | Lisensi | Catatan |
| :--- | :--- | :--- | :--- |
| [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) atau [RT-DETR](https://github.com/lyuwenyu/RT-DETR) | Deteksi area feses abnormal | Apache-2.0 | Disarankan, karena produk bisa dijual tanpa wajib membuka kode, dan sejalan dengan TA |
| [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) | Sama | AGPL-3.0 | Paling mudah dipakai, tetapi lisensinya mewajibkan kode dibuka bila dipakai dalam layanan |
| [rknn_model_zoo](https://github.com/airockchip/rknn_model_zoo) | Konversi INT8 untuk NPU 0,8 TOPS di [Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) | Apache-2.0 | Lisensi [rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2) tidak jelas, jadi baca dulu syaratnya |

| Jurnal Rujukan | Isi | Status |
| :--- | :--- | :-: |
| [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | Klasifikasi 4 kelas: koksidiosis, ND, salmonelosis, dan sehat. Xception 98,24 persen. Feses salmonela dan sehat mudah tertukar karena sama-sama putih. | Terverifikasi |
| [Wang dkk. 2019](https://doi.org/10.1155/2019/3823515) | Feses broiler Ross umur 25 sampai 35 hari, di kandang bertingkat dengan sabuk kotoran. Kelas abnormal berdasarkan bentuk, warna, dan kadar air. | Terverifikasi dari abstrak |
| [Aworinde dkk. 2023](https://doi.org/10.1016/j.dib.2023.109517) | Deskripsi dataset Nigeria berisi broiler dan petelur | Terverifikasi |

- **Contoh yang sudah ada:**
  - [Henomaly](https://github.com/RishitRai/Henomaly) dengan dasbor [aremyhens.fit](https://aremyhens.fit/): pemenang hackathon dengan kamera kandang tetap. Akurasinya hampir sempurna di data asal, lalu turun ke 74,6 sampai 78,2 persen saat diuji pada data berlabel PCR.
  - [mosiAfrica](https://huggingface.co/mosiAfrica/poultry-disease-mobilenetv2): model ponsel yang disebut sebagai alat bantu skrining.
  - [AvianAlert](https://github.com/farhan-439/avian_alert): juara 1 Cornell Digital Agriculture Hackathon 2025, memakai suara dan foto feses.
- **Batas jujur:**
  - Data publik bukan broiler di atas sekam.
  - Akurasi turun di peternakan baru.
  - Feses tidak menunjukkan penyakit pernapasan.
  - Koinfeksi hanya bisa dipilah lewat laboratorium.
- **Pekerjaan tim:**
  - kumpulkan set uji lokal bersama Dr. drh. Atin;
  - kumpulkan foto rover dan foto HP berpasangan dari titik feses yang sama, lalu bandingkan akurasinya. BROVER Saku baru dijual setelah akurasi foto HP diukur dan model disesuaikan;
  - pilih detektor Apache-2.0;
  - pakai ulang audit dataset dan pipeline dari TA di `Proposal TA/`.

### F4. Dasbor: Standar Umur, Tren Harian, Triase, dan Laporan Dokter Hewan

- **Masalah yang dijawab:**
  - Data kandang tercecer, sehingga keputusan pengobatan diambil tanpa dokter hewan.
  - Di 19 peternakan broiler mandiri di Bogor, keputusan memberi antibiotik datang dari PPL 47,4 persen, *technical service* 36,8 persen, dan pemilik 15,8 persen. Hanya satu orang yang dokter hewan, menurut [Sunandar dkk. 2024](https://journal.ipb.ac.id/index.php/actavetindones/article/download/42701/27932).
- **Fungsi:** menyatukan data F2, F3, dan catatan harian ABK menjadi status, tren, daftar tindakan, dan laporan ke dokter hewan.
- **Cara kerja:**
  1. **Panel standar umur:** suhu, RH, dan THI dibandingkan dengan tabel Cobb atau Ross sesuai umur ayam. Tren amonia ditampilkan berdampingan. Peringatan cuaca luar dari [API BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) dengan cadangan [Open-Meteo](https://open-meteo.com/).
  2. **Panel tren harian:** deplesi, pakan, dan air, beserta peringatan bila angkanya berubah tajam dibanding hari-hari sebelumnya.
  3. **Daftar triase:** temuan CV feses dan ceklis gejala pernapasan ABK, masing-masing dengan 3 tombol keputusan.
  4. **Catatan vaksinasi:** reaksi vaksin pernapasan bisa memicu gejala sementara, jadi tanggal vaksin menjadi konteks.
  5. **Laporan 1-klik** ke dokter hewan.
- **Apa itu deplesi:**
  - Deplesi adalah persentase kematian selama periode pemeliharaan, menurut [Candra dkk. 2025](https://jurnal.polinela.ac.id/index.php/peterpan/article/download/4496/2539/18005). Lembar catatan harian Cobb mencatat ayam mati dan ayam afkir setiap hari.
  - Contoh: dari 10.000 DOC, sampai hari ke-20 ada 300 ekor mati atau diafkir. Berarti deplesinya 3 persen.
- **Kenapa pakan dan air:**
  - Ini **bukan pengamatan perilaku**, melainkan angka yang dicatat ABK: jumlah ayam mati yang dipungut, karung pakan terpakai, dan angka meteran air.
  - Panduan Cobb 2021 meminta konsumsi air per kandang dicatat setiap 24 jam. Perubahan besar harus diselidiki, karena bisa menandakan gangguan kesehatan, kebocoran, atau masalah pakan.
  - [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511) dan [Manning dkk. 2007](https://doi.org/10.1017/s0043933907001274) juga memakai konsumsi air sebagai penanda kesehatan dan kesejahteraan.

| Tanda Penyakit Menurut Panduan Cobb 2021 | Cara BROVER |
| :--- | :--- |
| Perubahan pola konsumsi air dan pakan | Panel tren dari catatan ABK |
| Perubahan mendadak tampilan feses dan kondisi sekam | **F3 CV feses** |
| Kematian berlebih | Panel tren deplesi |
| Aktivitas atau perilaku ayam yang tidak biasa | Tidak dicakup, karena CV fisik dihapus. Diganti ceklis ABK. |

- **Data dan model:** tidak ada AI. Fitur ini memakai tabel Cobb dan Ross, ambang di kartu F2, dan aturan perubahan tajam yang ditetapkan bersama dokter hewan.
- **Contoh yang sudah ada:** [aremyhens.fit](https://aremyhens.fit/) memakai tiga tombol tindakan, tetapi dasbornya menampilkan skor 0 sampai 100. Skor seperti itu tidak dipakai BROVER.
- **Batas jujur:**
  - Panel tren bergantung pada disiplin ABK mengisi catatan.
  - Tidak semua kandang punya meteran air.
- **Pekerjaan tim:**
  - buat panel tren dan peringatannya;
  - tambahkan ceklis gejala pernapasan dan catatan vaksinasi;
  - validasi tabel Ross 308 di concept Bab 4.2 terhadap dokumen resmi Aviagen.

---

## 4. Fitur yang Dihapus dan Alasan Objektifnya

| Kriteria | AI Audio | CV Fisik dan Perilaku Ayam | Deteksi Bangkai | Sensor CO2 |
| :--- | :--- | :--- | :--- | :--- |
| Data terbuka berlabel kesehatan | Hanya 2: SmartEars di kandang baterai, Bowen 346 berkas | Big Broiler berlabel perilaku, bukan diagnosis | Ada, tetapi di luar fokus masalah | Tidak relevan |
| Cocok dengan broiler di lantai sekam | Tidak ada data seperti itu | Studi paruh terbuka dilakukan di kandang baterai | Paper utamanya dari kandang bertingkat | Tidak relevan |
| Beban kerja 2 Hacker | Berat, karena label harus dari dokter hewan | Berat, butuh detektor, pelacak, dan aturan perilaku | Sedang | Ringan |
| Nilai untuk masalah BROVER | Penyakit pernapasan, tetapi tidak spesifik | Tidak spesifik penyakit. Cekaman panas sudah terukur dari THI. | Bukan urgensi tim | Dampak langsung CO2 pada kadar kandang yang wajar lemah |
| Kebaruan | Rendah, karena sudah ada Talingan dan AvianAlert | Sedang | Rendah | Rendah |

### 4.1 Ringkasan Riset AI Audio, Disimpan untuk Riset Lanjutan

- **Cara kerja [SmartEars](https://doi.org/10.1016/j.compag.2025.111241), dibaca dari teks penuh:**
  - Mikrofon tetap dipasang di langit-langit lorong, 7 alat per ruang 110 x 16 m, total 97 alat di 13 ruang.
  - Kandangnya kandang baterai bertingkat, lebih dari 30.000 ekor per ruang.
  - Perangkatnya Raspberry Pi 4 dengan mikrofon USB, sekitar 73 dolar per alat. Sampling 22,05 kHz, dan setiap 30 detik diambil 5 detik suara.
  - MobileNetV3 mencapai 95,82 persen dengan waktu 497 ms per klip.
  - Tanpa penyesuaian, akurasi di peternakan lain turun ke 80,99 persen. Setelah disesuaikan, naik ke 99,76 persen.
  - Ketiga dokter hewan sepakat pada label yang sama hanya 28,79 persen.
  - [Dataset publiknya](https://doi.org/10.17632/dy6gtvt4mk.2) berisi 6.000 klip berlisensi CC BY 4.0.
- **Dataset lain:**
  - [Bowen University](https://data.mendeley.com/datasets/zp4nf2dxbh/1): 346 berkas, label sakit tanpa konfirmasi laboratorium.
  - [Zenodo 10433023](https://zenodo.org/records/10433023): ternyata suara stres ayam petelur, bukan data kesehatan broiler.
- **Studi Indonesia:** [Rosyida dkk. 2026](https://doi.org/10.48084/etasr.17149) dari UGM merekam Cobb 500 umur 17 sampai 30 hari dari Yogyakarta dan Blitar. Setiap ayam direkam di kandang isolasi, dan F1-nya 98,29 persen. Datanya bisa diminta ke penulis, jadi ini **peluang kolaborasi**.
- **Cara menangani suara banyak ayam:**
  - Hitung laju bersin pada kelompok 51 ekor, menurut [Carpentier dkk. 2019](https://doi.org/10.1016/j.compag.2019.05.013), dengan sensitivitas 66,7 persen.
  - Klasifikasi batuk dan ngorok pada 20.000 broiler lantai, menurut [Liu dkk. 2020](https://doi.org/10.1155/2020/2985478), dengan akurasi 93,8 persen.
  - Indeks seluruh kandang dengan satu mikrofon untuk sekitar 25 ribu ekor, menurut [Herborn dkk. 2020](https://doi.org/10.1098/rsif.2020.0086). Indeks ini memprediksi bobot dan kematian.
- **Contoh yang sudah ada:**
  - [Talingan](https://github.com/FadhlanHawali/Talingan-Android), dari Indonesia tahun 2020;
  - [AvianAlert](https://github.com/farhan-439/avian_alert);
  - [DKHowell](https://github.com/DKHowell/chicken-vocalizations).

### 4.2 Ringkasan Riset CV Fisik Ayam, Disimpan untuk Riset Lanjutan

- **Dataset paling cocok:** [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset), 102 video broiler lantai umur 10 sampai 40 hari, dengan 23 perilaku dan 4 postur. Lisensinya AGPL-3.0 dan ukurannya sekitar 32,5 GB.
- **Jurnal:**
  - [Okinda dkk. 2019](https://doi.org/10.1016/j.biosystemseng.2019.09.015): ND terdeteksi paling awal hari ke-4 dari postur dan gerak, pada ayam yang sengaja diinfeksi.
  - [Zhuang dkk. 2018](https://doi.org/10.1016/j.compag.2017.11.032): algoritma peringatan dini broiler sakit dari postur.
  - [Massari dkk. 2022](https://doi.org/10.3390/ani12070846): indeks kerumunan untuk cekaman panas.
  - [Ma dkk. 2025](https://doi.org/10.3390/ani15182732) dan [Kong dkk. 2026](https://doi.org/10.3390/ani16152408): deteksi paruh terbuka di kandang baterai.
  - [Elmessery dkk. 2023](https://doi.org/10.3390/agriculture13081527): citra termal terbaik, data tidak publik.
  - [Fodor dkk. 2023](https://doi.org/10.1016/j.psj.2023.102787): pose untuk pincang.

### 4.3 Alasan CO2 Tidak Masuk MVP

- [Reece dan Lott 1980](https://doi.org/10.3382/ps.0592400): CO2 3.000 dan 6.000 ppm selama *brooding* tidak menurunkan bobot. Baru 12.000 ppm yang menurunkannya sekitar 60 g.
- [McGovern dkk. 2001](https://library.csbe-scgab.ca/docs/journal/43/c9843.pdf): CO2 600 sampai 6.000 ppm tidak memengaruhi bobot akhir, kematian, maupun skor ascites. Saat ventilasi ditahan rendah pada ayam tua, yang naik justru amonia, debu, dan kelembapan. Kondisi ini sudah tertangkap F2.
- CO2 hanya punya nilai unik saat *brooding* dengan pemanas gas, ketika sekam masih segar dan amonia rendah. Cobb meminta CO2 di bawah 3.000 ppm dan CO di bawah 10 ppm.
- Sensor [SCD41](https://wiki.dfrobot.com/SKU_SEN0536_Gravity_SCD41_Infrared_CO2_Sensor) bagus, mengukur 400 sampai 5.000 ppm. Harga satu listing lokal sekitar Rp957 ribu, yang belum dicek ulang. SCD41 juga tidak mengukur CO.
- Jadi CO2 dijadikan modul opsional P2 untuk kandang berpemanas gas.

### 4.4 Usulan Kalimat Keterbatasan untuk Proposal

> Deteksi suara pernapasan dan perilaku ayam ditunda sebagai riset lanjutan, karena data terbuka untuk broiler di lantai sekam belum tersedia dan studi SmartEars menunjukkan model suara perlu disesuaikan ulang di setiap kandang. Pada tahap ini BROVER menangani penyakit pernapasan lewat pemantauan faktor pemicunya, yaitu amonia, kelembapan, dan suhu, ditambah ceklis gejala oleh ABK dan laporan ke dokter hewan.

---

## 5. Skrining, Bukan Diagnosis, dan Cakupan Penyakit

| | Diagnosis Penyakit | Skrining Gejala Penyakit |
| :--- | :--- | :--- |
| Pertanyaan | Ayam ini sakit **apa**? | Ada **tanda tidak normal** yang perlu dicek? |
| Dasar | Pemeriksaan dokter hewan dan uji laboratorium | Foto feses, tren angka harian, dan kondisi udara |
| Pelaku | Dokter hewan | Sistem dan ABK, lalu diteruskan ke dokter hewan |

**Empat alasan BROVER tidak mengklaim deteksi penyakit:**
1. Model hanya melihat tampilan feses. Satu tampilan bisa berasal dari sebab berbeda.
2. Koinfeksi umum di Indonesia. Kasus [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) pada 11.000 broiler di Majalengka butuh uji laboratorium untuk memilah koinfeksinya.
3. Akurasi turun di peternakan baru, seperti terlihat pada Henomaly.
4. Aturan proyek dan WOAH menyatakan BROVER bukan alat diagnosis otomatis.

| Kelompok Penyakit | Cara BROVER Menanganinya | Jenis |
| :--- | :--- | :--- |
| Koksidiosis | CV feses: feses berdarah atau cokelat gelap | AI |
| ND | CV feses untuk sebagian tanda, yaitu feses hijau. Dilengkapi ceklis ABK, catatan vaksin, dan dokter hewan. | AI dan manusia |
| Salmonelosis | CV feses: feses putih. Mudah tertukar dengan feses sehat. | AI |
| CRD, CRD kompleks, colibacillosis, coryza | Pencegahan lewat amonia, kelembapan, dan suhu dari F2, ditambah ceklis ABK dan dokter hewan | Aturan dan manusia |
| IB dan flu burung | Ceklis ABK, tren deplesi dan air, lalu dokter hewan. Flu burung wajib dilaporkan. | Aturan dan manusia |
| Cekaman panas | THI dan standar umur dari F2 | Aturan |

**Usulan kalimat pembuka Ringkasan di concept:**

> BROVER memantau amonia, kelembapan, dan suhu setinggi ayam sebagai faktor pemicu penyakit pernapasan, menskrining tanda penyakit pencernaan pada feses dengan computer vision, dan meneruskan bukti ke dokter hewan, tanpa mengklaim diagnosis.

---

## 6. Lampiran Ringkas

### 6.1 Batas Operasi Rover Hari ke-7 sampai Panen

- **Batas lama** hari ke-5 sampai 23 berasal dari [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/), robot penggaru sekam selebar 80 cm, tanpa alasan tertulis.
- **Studi robot kecil:** Dennis 2020 hari 3 sampai 37, Marin 2024 hari 7 sampai 42. Gangguan terbesar ada pada minggu pertama, sehingga awal yang dipilih adalah hari ke-7.
- **Umur panen closed house Indonesia:**
  - 27,06 dan 31,03 hari menurut [Candra dkk. 2025](https://jurnal.polinela.ac.id/index.php/peterpan/article/download/4496/2539/18005);
  - 34 hari menurut [Junita dkk. 2025](https://journals.unpad.ac.id/jptt/article/download/54863/25957);
  - 35 hari menurut [Wijayanto dkk. 2022](https://doi.org/10.22219/aras.v3i1.26592).
- **Kriteria berhenti sesi:** ayam tidak menyingkir, ada ayam terdorong jatuh atau terluka, atau suhu kandang melewati ambang cekaman panas.

### 6.2 Latar Belakang: Broiler, Bukan Petelur

- **Hampir semua sumber masalah di concept berasal dari broiler:**
  - [Pramuwidyatama dkk. 2023](https://doi.org/10.1016/j.prevetmed.2022.105833), khusus wabah HPAI;
  - Hartady dkk. 2026;
  - [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010);
  - Wilcox dkk. 2025;
  - Mohammadi dkk. 2026;
  - [Hasibuan dkk. 2021](https://doi.org/10.31186/jspi.id.16.2.171-179);
  - [Quintana-Ospina dkk. 2023](https://doi.org/10.3390/ani13213312).
- **Pengecualian:** grafik PCR Medion mencampur broiler dan petelur, dan kasus Hari Farm di [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/) terjadi di peternakan petelur.
- **Usulan pengganti Hari Farm di concept Bab 3.1 butir 4:**
  - **Kasus Hartady dkk. 2026:** koinfeksi pada 11.000 broiler di Majalengka yang hanya bisa dipilah lewat uji laboratorium.
  - **Studi Sunandar dkk. 2024:** keputusan antibiotik di 19 peternakan broiler mandiri Bogor hampir semuanya diambil bukan oleh dokter hewan.

### 6.3 Feses Broiler dan Petelur

- **Yang sama:** tanda penyakit pada feses, karena patogen dan spesiesnya sama.
- **Yang berbeda:** alas, umur, pakan, dan cara foto. Broiler di Indonesia berada di atas sekam, dengan kadar air sekam sampai 46,42 persen menurut Hasibuan 2021. Data Machuve berasal dari ayam yang hidup sampai 18 bulan. Wang 2019 memakai kandang bertingkat.
- **Belum ada** studi yang membandingkan tampilan visual feses keduanya secara langsung. Karena itu set uji lokal broiler di atas sekam wajib dibuat.

---

## 7. Daftar Perbaikan Berprioritas

**Keterangan:** P0 sebelum berkas seleksi, P1 selama *bootcamp*, P2 setelah Demo Day.

| No | Tindakan | Berkas atau Area | Prioritas | Kriteria Selesai |
| :-: | :--- | :--- | :-: | :--- |
| 1 | Hapus Model #2 CV fisik termasuk kata *carcass*, hapus Fitur 4 audio, dan ubah kategori Panel 2 menjadi CV feses dan ceklis ABK | Concept Bab 4, 5, dan 6 | P0 | Tidak ada lagi klaim AI audio, CV fisik, atau bangkai |
| 2 | Pertahankan SHT31 dan SEN0567 di rover pada tiang setinggi ayam. Tambahkan mode stasiun, dok di dalam kandang, dan jadwal 2 putaran per hari. Hapus mikrofon dari BOM. Servo DS3218 tetap dipakai untuk dua posisi kamera. | Concept Bab 4.1, 6, 7, dan 8.2 | P0 | Fitur 1, Fitur 2, dan BOM sesuai desain baru |
| 3 | Ganti kasus Hari Farm dengan Hartady 2026 dan Sunandar 2024 | Concept Bab 3.1 | P0 | Semua kasus latar belakang berasal dari broiler |
| 4 | Tulis kalimat pembuka Ringkasan dari Bab 5 dokumen ini | Concept Ringkasan dan Bab 4 | P0 | Hubungan dengan penyakit pernapasan terlihat sejak kalimat pertama |
| 5 | Koreksi tabel dataset: Zenodo 5801834 tanpa label YOLO, serta hapus dataset audio, fisik, dan bangkai | Concept Bab 11A, panduan IoT Tahap 2 dan 3 | P0 | Setiap dataset sesuai fitur yang tersisa |
| 6 | Tambah unggah foto HP ke Fitur 1 dan tech stack, sebagai cadangan paket BROVER Kandang dan jalur utama paket BROVER Saku | Concept Bab 4.1 dan 5 | P0 | Kedua peran foto HP dan jalur server Saku tertulis |
| 7 | Pasang tiang sensor, uji lama berhenti per zona, dan kalibrasi SEN0567 saat pilot | Prototipe | P1 | Ambang 10 dan 25 ppm bisa dipakai |
| 8 | Kumpulkan set uji lokal feses broiler di atas sekam | Model #1 | P1 | Ada set uji berlabel dokter hewan dan OPG |
| 9 | Panel tren deplesi, pakan, dan air, ceklis gejala pernapasan, dan catatan vaksin | Dasbor | P1 | Peringatan teruji |
| 10 | Bumper lunak, aturan sensor jarak, dan uji rover bertahap mulai hari ke-7 | Rover | P1 | Data sentuhan dan waktu putaran tercatat |
| 11 | Validasi tabel Ross 308 terhadap dokumen resmi Aviagen | Concept Bab 4.2 | P1 | Setiap angka bertanda halaman sumber |
| 12 | Modul CO2 untuk kandang berpemanas gas | Riset lanjutan | P2 | Uji pada masa *brooding* |
| 13 | Riset mikrofon tetap, termasuk kolaborasi data dengan penulis UGM | Riset lanjutan | P2 | Rekaman berlabel dokter hewan |
| 14 | Riset kamera termal untuk peta panas permukaan kelompok ayam | Riset lanjutan | P2 | Uji kamera termal murah di kandang |
| 15 | Otomatisasi rover. Pertama, CV navigasi untuk berhenti, melambat, dan berbelok dengan data deteksi ayam seperti [PIO](https://zenodo.org/records/16686320), [YOLOv5-CBAM broiler di atas sekam](https://doi.org/10.1016/j.aiia.2023.08.002), dan Big Broiler. Kedua, penjadwalan otomatis berupa putaran ketiga dan putaran khusus saat THI atau amonia di dok melewati ambang. Rujukan: [PoultryBot 2018](https://doi.org/10.1016/j.biosystemseng.2018.07.015), Marin 2024, dan Octopus XO. | Rover | P2 | Uji navigasi otomatis dan respons ayam |
| 16 | Ganti skema All-In dan proyeksi ROI dengan paket BROVER Saku dan BROVER Kandang, titik impas per paket, lama balik modal rover, dan protokol pemindahan unit | Concept Bab 9, BMC, diagram 07 dan 09 | P0 | Harga, titik impas, dan protokol tertulis dengan sumber atau label asumsi |

---

## 8. Daftar Tautan dan Hasil Pengecekan

Setiap tautan diuji dua kali dengan permintaan HTTP nyata. Untuk DOI, judul juga dicocokkan ke registri Crossref, karena banyak penerbit menolak akses otomatis dengan kode 403. Kode 202 dan 403 pada DOI adalah penolakan bot, bukan tautan mati, selama judul di registri cocok.

### 8.1 Seluruh Tautan di Dokumen Ini

| No | Tautan | Uji Pertama | Uji Ulang Kedua | Verifikasi Isi |
| :-: | :--- | :-: | :-: | :--- |
| 1 | [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) | 200 | 200 | Crossref judul cocok. Teks PMC11017054: robot 6,2 kg, hari 7 sampai 42, kepadatan maksimum 32 kg per m2, Cobb 500, Argentina. |
| 2 | [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak Europe PMC: 1.597 Ross 308, robot dikemudikan manual 3 kali sehari, layak dioperasikan hari 3 sampai 37 dengan gangguan terbatas. |
| 3 | [ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf) | 200 | 200 | Teks brosur: rel 0,5 m, 24/7, tanpa harga. |
| 4 | [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | 200 | 200 | Abstrak: kecepatan uji 0,2, 0,4, 0,6 m/s; jarak menghindar 83 sampai 110 cm. |
| 5 | [Balthazar dkk. 2024](https://doi.org/10.3390/ani14071014) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak Europe PMC: 6 minggu, kecepatan 12 rpm memicu benturan, 26 rpm tanpa benturan. |
| 6 | [teks penuhnya](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/) | 200 | 200 | Teks penuh: 0,04 dan 0,07 m/s. |
| 7 | [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) | 200 | 200 | Teks FAQ: 0,12 m/s, turun ke 0,04 m/s, hari 5 sampai sekitar 23, harga 20 sampai 34 ribu euro. |
| 8 | [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok; Tabel 6 dari lampiran lokal: 32,8 dan 79, AUC 0,694 dan 0,709. |
| 9 | [Medion 2026](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/) | 200 | 200 | Teks laman: penyakit bakteri pernapasan dominan dengan predisposisi ventilasi dan amonia. |
| 10 | [Rosyida dkk. 2026](https://doi.org/10.48084/etasr.17149) | 200 | 200 | Teks PDF ETASR: 1.140 segmen Cobb 500 umur 17 sampai 30 hari, Yogyakarta dan Blitar, data atas permintaan. |
| 11 | [Panduan Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) | 200 | 200 | Teks PDF: tabel suhu terhadap RH, sensor setinggi ayam, amonia di bawah 10 ppm. |
| 12 | [Quarles dan Kling 1974](https://doi.org/10.3382/ps.0531592) | 200 | 200 | Abstrak OpenAlex: broiler 25 dan 50 ppm umur 4 sampai 8 minggu plus vaksin IB, airsacculitis berat, karkas ditolak naik. |
| 13 | [Anderson dkk. 1964](https://doi.org/10.2307/1587967) | 200 | 200 | Crossref judul cocok. Pendahuluan OpenAlex: amonia 50 sampai 100 ppm di kandang tertutup. Hasil lengkap tidak terbaca. |
| 14 | [Liu dkk. 2020](https://doi.org/10.1016/j.psj.2020.03.019) | 200 | 200 | Abstrak Europe PMC: amonia 7 hari menaikkan Escherichia/Shigella di paru dan radang paru. |
| 15 | [Zhou dkk. 2020](https://doi.org/10.1016/j.psj.2019.12.063) | 200 | 200 | Abstrak Semantic Scholar: 15 ppm 3 hari menaikkan IL-6 trakea, 25 dan 35 ppm menurunkan pertumbuhan. |
| 16 | [Zhou dkk. 2021](https://doi.org/10.1016/j.psj.2020.11.026) | 200 | 200 | Abstrak Europe PMC: 15 ppm sudah mengubah mikrobiota trakea broiler Arbor Acres. |
| 17 | [Miles dkk. 2004](https://doi.org/10.1093/ps/83.10.1650) | 200 | 200 | Abstrak Semantic Scholar: bobot turun 6 dan 9 persen, kematian 13,9 persen pada 75 ppm. |
| 18 | [Miles dkk. 2006](https://doi.org/10.1637/7386-052405r.1) | 200 | 200 | Abstrak OpenAlex: 25 sampai 75 ppm merusak mata, jaringan napas tidak terpengaruh. |
| 19 | [Beker dkk. 2004](https://doi.org/10.1093/japr/13.1.5) | 200 | 200 | Abstrak Semantic Scholar: lesi trakea dan paru tidak dipengaruhi pada 30 dan 60 ppm. |
| 20 | [Al-Mashhadani dan Beck 1985](https://doi.org/10.3382/ps.0642056) | 200 | 200 | Abstrak Semantic Scholar: kehilangan silia tidak konsisten, dinding atrium paru menebal pada 75 dan 100 ppm. |
| 21 | [Vučemilo dkk. 2008](https://doi.org/10.17221/329-cjas) | 200 | 200 | Abstrak Semantic Scholar: 22.000 Ross 308, amonia 5,17 sampai 25,49 ppm, endotoksin sampai 99,40 EU per m3. |
| 22 | [Barbosa dkk. 2024](https://doi.org/10.3390/ani14040615) | 403, registri DOI cocok | 403, registri DOI cocok | Teks penuh Europe PMC: 1.250 ekor, sensor Dräger DOL 53, MLP di atas 98 persen, data dimuat di artikel. |
| 23 | [Saputra dkk. 2020](https://jurnal.uns.ac.id/Sains-Peternakan/article/download/31636/26596) | 200 | 200 | Teks PDF: Saputra dkk. 2020, mikroklimatik amonia, korelasi positif kuat dengan RH dan kecepatan angin. |
| 24 | [Fajaryani dkk. 2024](https://journals.unpad.ac.id/jptt/article/download/48211/23878) | 200 | 200 | Teks PDF: Fajaryani dkk. 2024, CO2 dan amonia tinggi mengganggu pernapasan dan menaikkan deplesi. |
| 25 | [Lashari dkk. 2023](https://doi.org/10.7717/peerj-cs.1623) | 200 | 403, registri DOI cocok | Teks penuh Europe PMC: node T, RH, O2, CO2 MQ-135, CO ZE07, NH3 ME3 elektrokimia. |
| 26 | [Studi sensor IoT 2025](https://doi.org/10.1016/j.atech.2025.101197) | 200 | 200 | Abstrak OpenAlex: MQ-137 R 0,82, BME280 R 0,95 terhadap instrumen acuan. |
| 27 | [wiki resmi](https://wiki.dfrobot.com/sen0567/) | 200 | 200 | Teks wiki: Qualitative only, 1 sampai 300 ppm. |
| 28 | [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052) | 200 | 200 | Abstrak OpenAlex dan Tabel 2 serta 3 dari lampiran lokal. |
| 29 | [Zenodo 4628934](https://zenodo.org/records/4628934) | 200 | 200 | API Zenodo dan isi imgObjDet_Yolo.zip dihitung ulang di memori. |
| 30 | [Zenodo 5801834](https://zenodo.org/records/5801834) | 200 | 200 | API Zenodo: 4 arsip klasifikasi PCR, 1.255 citra, CC BY 4.0, ayam petelur, persilangan, dan lokal. |
| 31 | [Mendeley 8pnbzpt2k9](https://data.mendeley.com/datasets/8pnbzpt2k9/1) | 200 | 200 | API Mendeley: 14.618 citra 100 x 100, broiler dan layer, CC BY 4.0. |
| 32 | [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) | 200 | 200 | API GitHub: Apache-2.0. |
| 33 | [RT-DETR](https://github.com/lyuwenyu/RT-DETR) | 200 | 200 | API GitHub: Apache-2.0. |
| 34 | [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) | 200 | 200 | API GitHub: AGPL-3.0. |
| 35 | [rknn_model_zoo](https://github.com/airockchip/rknn_model_zoo) | 200 | 200 | API GitHub: Apache-2.0. |
| 36 | [Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) | 200 | 200 | Teks laman: RK3566, NPU 0,8 TOPS, RAM 2, 4, 8 GB. |
| 37 | [rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2) | 200 | 200 | API GitHub: NOASSERTION. |
| 38 | [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | 200 | 200 | Teks penuh: data dari ayam petelur, persilangan, dan lokal; Xception 98,24 persen tertinggi. |
| 39 | [Wang dkk. 2019](https://doi.org/10.1155/2019/3823515) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok, CC BY 4.0. Abstrak OpenAlex: Ross umur 25 sampai 35 hari, kandang bertingkat dengan sabuk kotoran. |
| 40 | [Aworinde dkk. 2023](https://doi.org/10.1016/j.dib.2023.109517) | 200 | 200 | Crossref: penulis pertama Aworinde. |
| 41 | [Henomaly](https://github.com/RishitRai/Henomaly) | 200 | 200 | README: angka uji farm dan PCR, AGPL-3.0, kamera kandang tetap. |
| 42 | [aremyhens.fit](https://aremyhens.fit/) | 200 | 200 | Teks dasbor: Barn health 0/100 dan tiga tombol tindakan. |
| 43 | [mosiAfrica](https://huggingface.co/mosiAfrica/poultry-disease-mobilenetv2) | 200 | 200 | Model card: uji 1.022 citra, Newcastle 57 citra, MIT, screening aid. |
| 44 | [AvianAlert](https://github.com/farhan-439/avian_alert) | 200 | 200 | README: juara 1 Data Science Cornell Digital Agriculture Hackathon 2025, suara dan feses. |
| 45 | [Sunandar dkk. 2024](https://journal.ipb.ac.id/index.php/actavetindones/article/download/42701/27932) | 200 | 200 | Teks PDF: Sunandar dkk. 2024, 19 farm Bogor, PPL 47,4, TS 36,8, pemilik 15,8 persen, 1 dokter hewan. |
| 46 | [API BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) | 200 | 200 | Respons JSON prakiraan cuaca tingkat desa. |
| 47 | [Open-Meteo](https://open-meteo.com/) | 200 | 200 | Laman aktif; API ECMWF diuji berfungsi. |
| 48 | [Candra dkk. 2025](https://jurnal.polinela.ac.id/index.php/peterpan/article/download/4496/2539/18005) | 200 | 200 | Teks PDF Tabel 4: umur panen 27,06 dan 31,03 hari. |
| 49 | [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511) | 200 | 200 | Abstrak OpenAlex: penurunan mendadak konsumsi air dapat menandakan masalah. |
| 50 | [Manning dkk. 2007](https://doi.org/10.1017/s0043933907001274) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul konsumsi air sebagai indikator kesejahteraan broiler. |
| 51 | [SmartEars](https://doi.org/10.1016/j.compag.2025.111241) | 200 | 200 | Crossref: penulis Qiao dkk., volume 241. |
| 52 | [Dataset publiknya](https://doi.org/10.17632/dy6gtvt4mk.2) | 200 | 200 | DataCite: deskripsi, lisensi CC BY 4.0, 6.000 klip. |
| 53 | [Bowen University](https://data.mendeley.com/datasets/zp4nf2dxbh/1) | 200 | 200 | API Mendeley: 346 berkas, 139, 86, 121, CC BY 4.0. |
| 54 | [Zenodo 10433023](https://zenodo.org/records/10433023) | 200 | 200 | API Zenodo: suara stres ayam petelur, CC BY 4.0, sekitar 2,5 GB. |
| 55 | [Carpentier dkk. 2019](https://doi.org/10.1016/j.compag.2019.05.013) | 200 | 200 | Crossref dan abstrak: 763 bersin, sensitivitas 66,7 persen. |
| 56 | [Liu dkk. 2020](https://doi.org/10.1155/2020/2985478) | 403, registri DOI cocok | 403, registri DOI cocok | Abstrak OpenAlex: 20.000 broiler lantai, rekaman 24 jam seminggu, akurasi 93,8 persen. |
| 57 | [Herborn dkk. 2020](https://doi.org/10.1098/rsif.2020.0086) | 403, registri DOI cocok | 403, registri DOI cocok | Abstrak dan teks Europe PMC: 12 flok komersial, satu mikrofon, korelasi minus 0,88, data di figshare. |
| 58 | [Talingan](https://github.com/FadhlanHawali/Talingan-Android) | 200 | 200 | API GitHub dan README: produk IoT dan AI suara untuk penyakit pernapasan ayam, tanpa lisensi. |
| 59 | [DKHowell](https://github.com/DKHowell/chicken-vocalizations) | 200 | 200 | README: klasifikasi vokalisasi kandang industri dan prediksi kematian. |
| 60 | [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset) | 200 | 200 | README: 102 video, 28 label perilaku dan postur, AGPL-3.0. |
| 61 | [Okinda dkk. 2019](https://doi.org/10.1016/j.biosystemseng.2019.09.015) | 200 | 200 | Crossref judul cocok. Ringkasan OSTI: ND paling awal terdeteksi hari ke-4. |
| 62 | [Zhuang dkk. 2018](https://doi.org/10.1016/j.compag.2017.11.032) | 200 | 200 | Crossref: judul algoritma peringatan dini broiler sakit cocok. |
| 63 | [Massari dkk. 2022](https://doi.org/10.3390/ani12070846) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak: indeks kerumunan membedakan nyaman dan cekaman panas. |
| 64 | [Ma dkk. 2025](https://doi.org/10.3390/ani15182732) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul deteksi napas mulut terbuka broiler kandang baterai cocok. |
| 65 | [Kong dkk. 2026](https://doi.org/10.3390/ani16152408) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul paruh terbuka lewat inspeksi bergerak cocok. |
| 66 | [Elmessery dkk. 2023](https://doi.org/10.3390/agriculture13081527) | 403, registri DOI cocok | 403, registri DOI cocok | Abstrak OpenAlex: 10.000 citra visual dan termal, mAP50 0,988 termal. |
| 67 | [Fodor dkk. 2023](https://doi.org/10.1016/j.psj.2023.102787) | 200 | 200 | Crossref: judul estimasi pose dan pincang broiler cocok. |
| 68 | [Reece dan Lott 1980](https://doi.org/10.3382/ps.0592400) | 200 | 200 | Abstrak OpenAlex: 3.000 dan 6.000 ppm tanpa efek bobot, 12.000 ppm turun sekitar 60 g. |
| 69 | [McGovern dkk. 2001](https://library.csbe-scgab.ca/docs/journal/43/c9843.pdf) | 200 | 200 | Teks PDF: McGovern dkk. 2001, CO2 600 sampai 6.000 ppm tanpa efek bobot, kematian, dan ascites. |
| 70 | [SCD41](https://wiki.dfrobot.com/SKU_SEN0536_Gravity_SCD41_Infrared_CO2_Sensor) | 200 | 200 | Teks wiki: NDIR fotoakustik, 400 sampai 5.000 ppm, akurasi 40 ppm plus 5 persen. |
| 71 | [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref dan abstrak: 11.000 broiler, koinfeksi AI H5 dan H9. |
| 72 | [Junita dkk. 2025](https://journals.unpad.ac.id/jptt/article/download/54863/25957) | 200 | 200 | Teks PDF: pengamatan umur 23 sampai panen 34 hari. DOI tercetak di PDF tidak terdaftar. |
| 73 | [Wijayanto dkk. 2022](https://doi.org/10.22219/aras.v3i1.26592) | 200 | 200 | Teks PDF: ayam dipelihara umur 1 hingga 35 hari. |
| 74 | [Pramuwidyatama dkk. 2023](https://doi.org/10.1016/j.prevetmed.2022.105833) | 200 | 200 | Crossref judul khusus HPAI; Tabel 4 dibaca dari lampiran lokal. |
| 75 | [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010) | 200 | 200 | Crossref dan abstrak cocok; angka skor 0,28 tidak dicek ulang. |
| 76 | [Hasibuan dkk. 2021](https://doi.org/10.31186/jspi.id.16.2.171-179) | 200 | 200 | Teks penuh PDF penerbit: Tabel 3 kadar air 46,42 persen. |
| 77 | [Quintana-Ospina dkk. 2023](https://doi.org/10.3390/ani13213312) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul faktor lingkungan dan performa broiler tropis cocok. |
| 78 | [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/) | 200 | 200 | Teks laman: peternakan layer sekitar 10 ribu ekor, Desember 2022. |
| 79 | [PIO](https://zenodo.org/records/16686320) | 200 | 200 | API Zenodo: 1.435 citra, 327.289 instans, CC BY 4.0. Dipakai untuk riset navigasi, bukan penyakit. |
| 80 | [YOLOv5-CBAM broiler di atas sekam](https://doi.org/10.1016/j.aiia.2023.08.002) | 200 | 200 | Crossref judul cocok: deteksi broiler di lantai sekam dengan YOLOv5-CBAM, Guo dkk. 2023, CC BY-NC-ND 4.0. |
| 81 | [PoultryBot 2018](https://doi.org/10.1016/j.biosystemseng.2018.07.015) | 200 | 200 | Crossref judul cocok: evaluasi PoultryBot, platform robot mobil otonom untuk kandang unggas, Vroegindeweij dkk. 2018. |

### 8.2 Ringkasan Hasil Dua Kali Pengecekan

- **Jumlah tautan unik di dokumen:** 81.
- **Uji pertama:** kode 200 sebanyak 67, kode 403 sebanyak 14.
- **Uji ulang kedua:** kode 200 sebanyak 66, kode 403 sebanyak 15.
- **Tautan nomor 79 sampai 81** ditambahkan pada 28 November 2026 malam, mengikuti keputusan otomatisasi rover. Ketiganya diuji dua kali dan sama-sama berkode 200.
- **Tautan yang kodenya berubah antarpengujian, merujuk nomor di tabel 8.1:** nomor 25 dari kode 200 ke 403. Perubahan ini berasal dari pembatasan bot yang tidak konsisten, bukan perubahan isi.
- **Penolakan bot:** semua tautan DOI berkode 403 atau 202 sudah dicocokkan judulnya di registri Crossref. Laman non-DOI berkode 403 dicatat apa adanya dan tidak dipakai sebagai satu-satunya bukti klaim.
