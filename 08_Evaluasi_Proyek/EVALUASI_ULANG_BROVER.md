# Evaluasi Ulang Proyek BROVER Setelah Sinkronisasi 28 November 2026

**Lingkup:** seluruh berkas aktif proyek BROVER milik Tim Asprak untuk Hackathon Deep Tech UNJ 2026 jalur D-FARM, setelah sinkronisasi terhadap keputusan final tim per 28 November 2026.

**Acuan pembanding:** `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md` sebagai baseline. Berkas baseline tidak diubah.

**Metode:**
- Setiap angka baru dicek ke sumber primer.
- Setiap gambar yang dirender ulang dilihat langsung.
- Teks SVG di-grep untuk pola lama.
- Rujukan gambar markdown diuji keberadaannya.
- Jumlah gambar di PDF dihitung dengan `pdfimages`.
- Semua tautan di laporan ini diuji dua kali.

**Gaya laporan:** tanpa tanda pisah, tanda petik, apostrof, simbol pasal, dan tanda kurung di luar sintaks tautan. Path berkas ditulis dalam format kode.

---

## 1. Ringkasan Putusan dan Peta Prioritas

**Putusan singkat:** dokumen inti BROVER sekarang konsisten satu sama lain. Berkas yang diperiksa: concept, README, MEMORY, aturan agent, konteks tim, peta fitur, panduan IoT, TOP5, RCA, dan seluruh diagram.

Isinya sama untuk judul, empat fitur, satu model CV feses, dua paket langganan, angka BOM dan HPP, titik impas, jadwal rover, dan status TKT. Skema lama tidak lagi muncul sebagai klaim BROVER, yaitu:
- *Multi-Modal AI*;
- audio;
- Model fisik ayam;
- sewa per siklus;
- beli sepaket tanpa langganan;
- ROI 498 persen.

Kelemahan terbesar yang tersisa bukan lagi soal dokumen, tetapi soal bukti lapangan:
- model CV feses belum dilatih;
- set uji lokal feses broiler di atas sekam belum ada;
- pilot belum disepakati tertulis;
- harga beli putus masih usulan.

| No | Sisa Masalah | Rubrik Terdampak | Prioritas | Tindakan |
| :-: | :--- | :--- | :-: | :--- |
| 1 | Model CV feses belum dilatih dan set uji lokal belum ada, sehingga akurasi belum bisa diklaim | Kelayakan Teknis 20 persen | P0 | Latih detektor Apache-2.0 *baseline* sebelum M1 dan kumpulkan foto rover dan HP berpasangan sebelum M2 |
| 2 | Kesepakatan uji lapangan dengan Dinas Pangan dan Pertanian Kota Cimahi dan peternakan keluarga anggota belum tertulis | Relevansi 25 persen, Bisnis 15 persen | P0 | Surat persetujuan atau LoI paling lambat Business Matching April 2027 |
| 3 | Pengaruh BROVER terhadap kematian dan FCR belum diukur, sehingga titik impas masih hipotesis | Bisnis 15 persen | P1 | Jalankan metrik pilot Bab 9.6 concept |
| 4 | Harga beli putus Rp11,5 juta belum dikonfirmasi tim | Bisnis 15 persen | P1 | Keputusan tim sebelum *pitch deck* |
| 5 | `SEN0567` belum dikalibrasi dan aturan RH di atas 70 persen belum tertulis | Kelayakan Teknis 20 persen | P1 | Kalibrasi terhadap alat acuan dan aturan tertulis bersama Dr. drh. Atin Supiyani, M.Si. |
| 6 | Respons ayam terhadap rover pada akhir siklus belum diuji di kandang tropis | Kelayakan Teknis 20 persen | P1 | Sesi pendek dengan kriteria berhenti dan pencatatan sentuhan |
| 7 | Jalur BROVER Saku bergantung pada akurasi foto HP | Kelayakan Teknis 20 persen, Bisnis 15 persen | P1 | Gerbang peluncuran Saku berbasis akurasi per sumber foto |
| 8 | Beban kerja dua anggota *Hacker* tetap tinggi walau lingkup dipangkas | Tim 10 persen | P1 | Jadwal 12 minggu Bab 9.7 dipantau mingguan |

---

## 2. Status Setiap Temuan dan Rekomendasi Evaluasi Objektif

**Keterangan status:**
- **Selesai:** sudah diperbaiki di berkas.
- **Sebagian:** sebagian sudah dikerjakan.
- **Belum:** belum dikerjakan.
- **Digantikan:** temuan tidak relevan lagi karena keputusan tim menghapus fitur terkait.

### 2.1 Dua Belas Temuan Teratas

| No | Temuan Baseline | Status | Bukti Lokasi |
| :-: | :--- | :-: | :--- |
| 1 | Zenodo 5801834 ditulis berlabel YOLO | Selesai | Concept Bab 11 tabel A baris 2 menulis label PCR tanpa label YOLO. Tautan dataset di panduan IoT 02 dan 03 disamakan dengan Bab 11. |
| 2 | Judul memakai frasa deteksi dini | Selesai | Judul di concept Bab 1, `README.md`, `MEMORY.md`, `.agent/rules/hackathon-context.md`, dan `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` memakai kata skrining |
| 3 | Model fisik bersandar pada ChickenVerse | Digantikan | Model fisik dihapus. Lihat tabel fitur dihapus di concept Bab 4 dan butir 3 Bab 1 peta fitur. |
| 4 | Batas hari ke-5 sampai 23 meniru Octopus XO | Selesai | Concept Bab 6 butir 3 memakai hari ke-7 sampai panen. Batas hari ke-5 sampai 23 hanya disebut sebagai milik Octopus XO. |
| 5 | ROI 498 persen tanpa data efektivitas | Selesai | Concept Bab 9.2 D memakai titik impas. Gambar 09 baru menggantikan grafik lama yang diarsipkan. |
| 6 | Protokol rekam suara tidak meredam blower kandang | Digantikan | Audio dihapus dari lingkup. Riset mikrofon tetap menjadi pengembangan lanjutan di Bab 9.5 D. |
| 7 | Kecepatan AviSense dan cakupan uji Parajuli salah kutip | Selesai | Concept Bab 6 butir 5 menulis AviSense sekitar 0,05 m/s dan Parajuli hanya menguji 0,2, 0,4, dan 0,6 m/s |
| 8 | Dataset audio IceKhoffi terhitung dua kali | Digantikan | Audio dihapus. Dataset tersebut tidak lagi ada di Bab 11. |
| 9 | `SEN0567` kualitatif dibandingkan dengan ambang ppm | Selesai | Concept Bab 4 dan risiko R04 menampilkan tren per zona pada jam yang sama. Kalibrasi terhadap alat acuan dilakukan saat pilot. |
| 10 | Keselarasan mitra lemah | Selesai | Concept Bab 2 dan BMC Bab 9.1 menempatkan PT Zara sebagai calon mitra *bundling* dan pendukung pemantauan kesehatan dan lingkungan. PT Edura menjadi dukungan *in-kind* perakitan. |
| 11 | Indikator air, pakan, dan mortalitas harian hanya opsional | Selesai | Fitur F4 memuat tren harian deplesi, pakan, dan air dari catatan ABK. Lihat concept Bab 4 dan Gambar 04c. |
| 12 | Beban kerja dua anggota *Hacker* terlalu besar | Sebagian | Lingkup dipangkas menjadi satu model, audio dihapus, dan jalur Saku dibangun setelah inferensi rover berjalan. Penanggung jawab per minggu ada di Bab 9.7. Risiko tetap ada. |

### 2.2 Delapan Belas Rekomendasi

| No | Rekomendasi Baseline | Status | Bukti Lokasi |
| :-: | :--- | :-: | :--- |
| 1 | Ganti judul dan hapus frasa lama | Selesai | Grep Tahap 9: frasa lama hanya muncul sebagai catatan larangan atau penghapusan |
| 2 | Koreksi Bab 11A dan tautan dataset panduan IoT | Selesai | Concept Bab 11 dengan catatan audit per baris; panduan IoT 02 dan 03 bagian tautan |
| 3 | Ubah atau hapus Model fisik | Digantikan | Dihapus dari lingkup |
| 4 | Turunkan klaim audio | Digantikan | Dihapus dari lingkup |
| 5 | Ganti ROI dengan titik impas | Selesai | Concept Bab 9.2 D dan Gambar 09 |
| 6 | Koreksi angka yang tidak cocok sumber | Selesai | Koreksi AviSense, Parajuli, FPS Ultralytics, ChickenBoy, Octopus XO, nomor pasal ISO 8373, Hari Farm, dan konteks HPAI pada Pramuwidyatama. Hari Farm kini berlabel petelur di TOP5 dan RCA. |
| 7 | Rumuskan ulang keselarasan mitra | Selesai | Concept Bab 2 dan Bab 9.1 |
| 8 | Ganti tautan akar API BMKG | Selesai | Concept Bab 12 entri 73 memakai endpoint adm4 |
| 9 | Putuskan bentuk platform dengan data uji | Sebagian | Keputusan sudah ditulis: rover dengan dok dan mode stasiun. Data uji lapangan menunggu pilot. |
| 10 | Kumpulkan set uji lokal berlabel dokter hewan | Belum | Direncanakan di Bab 9.7 baris 7 dan milestone M2 |
| 11 | Panel tren air, pakan, dan deplesi | Sebagian | Sudah masuk rancangan F4; implementasi menunggu dasbor Tahap 2 |
| 12 | Aturan RH di atas 70 persen dan tren amonia | Sebagian | Tren amonia per zona sudah dirancang; aturan RH tropis belum tertulis |
| 13 | Validasi tabel Ross 308 | Selesai | Tabel Bab 4.2 dikoreksi terhadap dokumen Aviagen. Hari 3 menjadi 102 g, batas bawah tanpa dasar dihapus, dan nilai 1.675 g yang ternyata milik Cobb dipindahkan. |
| 14 | Detektor Apache-2.0 dan syarat `rknn-toolkit2` | Selesai | Concept Bab 5 dan Bab 11 tabel C; syarat lisensi `rknn-toolkit2` dicatat untuk dibaca sebelum komersialisasi |
| 15 | Sederhanakan arsitektur | Sebagian | Satu model dan pustaka audio dihapus; jalur Saku ditunda sampai inferensi rover berjalan |
| 16 | Riset mikrofon tetap | Tetap P2 | Pengembangan lanjutan Bab 9.5 D |
| 17 | Kaji rel gantung | Tetap P2 | Pengembangan lanjutan Bab 9.5 D |
| 18 | Ukur waktu tunggu skrining sebelum memakai kata dini | Tetap P2 | Metrik pilot Bab 9.6 |

---

## 3. Audit Konsistensi Antarberkas

| Aspek | Nilai Acuan di Concept | Berkas yang Dicocokkan | Hasil |
| :--- | :--- | :--- | :--- |
| Judul | Sistem Inspeksi Multisensor Berbasis AI dan *Edge-Cloud* untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler | `README.md`, `MEMORY.md`, aturan agent, `01_TEAM_AND_CONSTRAINTS.md` | Sama |
| Fitur | F1 rover, F2 mikroklimat dengan mode stasiun, F3 CV feses, F4 dasbor | Diagram 03, 04a, 04b, 04c, panduan IoT 01 sampai 03, peta fitur | Sama |
| BOM dan HPP | 18 item, HPP Rp8.180.000 eceran dan Rp6.714.000 grosir | Concept Bab 8.2, 9.1, 9.2 C, `MEMORY.md`, Gambar 07 | Sama |
| Harga paket | Saku Rp75.000, Kandang Rp750.000 per siklus, usulan beli putus Rp11,5 juta | Concept Bab 9.1 dan 9.2, `MEMORY.md`, aturan agent, Gambar 07 dan 09 | Sama |
| Titik impas | Kandang 21 sampai 33 ekor, Saku 2,1 sampai 3,3 ekor | Concept Bab 9.2 D dan Bab 10, `MEMORY.md`, Gambar 07 dan 09 | Sama setelah koreksi Saku |
| Jadwal rover | Hari ke-7 sampai panen, 2 putaran per hari, 0,07 sampai 0,1 m/s | Concept Bab 6, panduan IoT 01 sampai 03, Gambar 04a dan 04b | Sama |
| Dataset | Zenodo 4628934 berlabel YOLO, Zenodo 5801834 berlabel PCR, Mendeley 8pnbzpt2k9, set uji lokal | Concept Bab 11, panduan IoT 02 dan 03 | Sama |
| Model | Satu detektor Apache-2.0, RKNN INT8 di *edge*, ONNX di server | Concept Bab 5, `MEMORY.md`, panduan IoT 02 dan 03, Gambar 03 dan 05 | Sama |
| TKT | Sistem utuh TKT 3, target 6 akhir *bootcamp* dan 7 akhir program | Concept Bab 9.5 A, `MEMORY.md`, Gambar 06 | Sama |
| Jadwal 3 bulan | 14 baris kegiatan, M1 sampai M3 | Concept Bab 9.7, Gambar 08b, tugas Desember sampai Februari di Gambar 08 | Sama |
| Rujukan | 85 entri Vancouver di Bab 12, sitasi teks nama dan tahun | Concept Bab 12 | Lengkap |

**Kekeliruan yang ditemukan dan diperbaiki selama audit ini:**
1. **Titik impas BROVER Saku tertulis 2 sampai 3 ekor.** Hitungannya Rp75.000 dibagi Rp36.200 sampai Rp22.700, yaitu 2,1 sampai 3,3 ekor. Pada nilai ayam terendah, tiga ekor belum menutup biaya paket. Angka dikoreksi di concept, `MEMORY.md`, dan Gambar 07 serta 09.
2. **Gambar 06 lama membagi kelompok TKT secara keliru**, yaitu riset dasar TKT 1 sampai 4. Materi resmi pengukuran TKT dari [LPPM Undip](https://lppm.undip.ac.id/wp-content/uploads/Materi-Sosialisasi-TRL1.pdf) membagi Riset Dasar TKT 1 sampai 3, Riset Terapan 4 sampai 6, dan Riset Pengembangan 7 sampai 9. Pita skala sekarang memakai jenis lingkungan uji, dan pembagian resmi ditulis di kaki gambar.
3. **Spanduk Gambar 06 lama menulis bahwa Rowe dkk. 2019 membuktikan sebagian besar alat berhenti di TKT 3 sampai 4.** Klaim itu tidak ada di sumber. Kalimat diganti sesuai abstrak [Rowe dkk. 2019](https://doi.org/10.3390/ani9090614).
4. **Gambar 05 lama memuat angka FPS YOLOv8n dan suhu *thermal runaway* yang tidak terverifikasi.** Gambar diganti tabel spesifikasi resmi dari:
   - [Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html): NPU 0,8 TOPS;
   - [Orange Pi 5](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html): NPU 6 TOPS;
   - [Luckfox Pico Ultra](https://www.luckfox.com/EN-Luckfox-Pico-Ultra?ci=502): NPU 1 TOPS INT8 dan RAM 256 MB;
   - [Raspberry Pi 4](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-product-brief.pdf): tanpa NPU.
5. **Gambar 04b lama mengaitkan kebijakan satu unit untuk satu kandang langsung ke WOAH.** Sekarang kebijakan itu ditulis sebagai SOP tim dengan protokol pemindahan unit.
6. **Panduan IoT 03 masih menautkan tutorial YOLOv8 dan repo Custom-YoloV8-NPU.** Keduanya diganti [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX). Panduan 03 juga masih memuat angka FPS dan suhu baterai yang tidak terverifikasi; keduanya sekarang mengikuti *datasheet* sel yang dibeli.

---

## 4. Kecocokan Judul dengan Isi, Frasa demi Frasa

| Frasa Judul | Isi Concept yang Mendukung | Status |
| :--- | :--- | :--- |
| BROVER | Nama merek. Kepanjangannya hanya ditulis di bagian filosofi. | Cocok |
| Sistem Inspeksi | Rover berhenti di titik zona tetap dua kali sehari; BROVER Saku memakai foto HP | Cocok |
| Multisensor | Kamera, `SHT31`, `SEN0567`, sensor jarak, dan `INA219` pada satu platform. Istilah ini dipilih sesuai taksonomi [Baltrušaitis dkk. 2019](https://doi.org/10.1109/TPAMI.2018.2798607), karena AI hanya memakai satu modalitas, yaitu citra. | Cocok |
| Berbasis AI | Satu detektor CV feses berlisensi Apache-2.0 | Cocok, dengan klaim akurasi menunggu set uji lokal |
| *Edge-Cloud* | Inferensi BROVER Kandang di `Orange Pi 3B`; BROVER Saku dan sinkronisasi data di server pusat | Cocok |
| Skrining Gejala Penyakit | CV feses dan ceklis gejala pernapasan ABK, diakhiri triase tiga tombol oleh manusia | Cocok; tidak ada klaim diagnosis |
| Pemantauan Mikroklimat | Suhu, RH, dan tren amonia setinggi ayam terhadap standar umur Cobb dan Ross, ditambah mode stasiun di dok | Cocok |
| Kandang Ayam Broiler | Standar Cobb 500 dan Ross 308; data publik feses bukan broiler, sehingga set uji lokal wajib | Cocok, dengan catatan data |

**Catatan jujur:** kata multisensor dan *edge* berlaku penuh untuk BROVER Kandang. BROVER Saku adalah varian paket tanpa sensor rover, dan inferensinya berjalan di server. Judul menggambarkan sistem utuh. Batasan Saku dijelaskan di matriks paket concept Bab 4.

---

## 5. Kartu Fitur: Apakah Setiap Klaim Punya Bukti

| Fitur | Klaim Utama | Bukti yang Dipakai | Penilaian |
| :--- | :--- | :--- | :--- |
| F1 Rover | Kecepatan 0,07 sampai 0,1 m/s dan operasi hari ke-7 sampai panen | Robot RobôFrango di [da Rocha Balthazar dkk. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/), AviSense di [Caliva dkk. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/), dan cakupan uji [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | Cukup sebagai dasar desain awal. Batas akhir siklus tetap harus diuji di kandang mitra. |
| F1 Kamera | Satu kamera pada servo dua posisi cukup karena foto diambil saat berhenti | Keputusan rekayasa dengan alasan tertulis di concept Bab 8.1 | Masuk akal. Ketahanan servo di kandang belum diuji. |
| F2 Udara | `SEN0567` adalah indikator tren kualitatif | [Wiki DFRobot SEN0567](https://wiki.dfrobot.com/sen0567/) menulis *qualitative only* | Klaim sesuai sumber |
| F2 Standar umur | Suhu dan RH dibandingkan dengan tabel umur | [Panduan Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf); tabel Ross dikoreksi terhadap dokumen Aviagen | Cukup. Aturan RH tropis di atas 70 persen masih harus disusun. |
| F3 CV feses | Skrining feses abnormal dari foto rover dan HP | Data latih [Zenodo 4628934](https://zenodo.org/records/4628934) dan uji [Zenodo 5801834](https://zenodo.org/records/5801834). Sumber datanya ayam petelur, persilangan, dan lokal di Tanzania menurut [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345). Penurunan akurasi lintas domain terlihat di [Henomaly](https://github.com/RishitRai/Henomaly). | Belum ada bukti akurasi untuk broiler di atas sekam. Klaim dibatasi pada skrining sampai set uji lokal tersedia. |
| F4 Dasbor | Tren air, pakan, dan deplesi sebagai tanda masalah | Penurunan mendadak konsumsi air dapat menandakan masalah menurut [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511); pola tiga tombol dari [aremyhens.fit](https://aremyhens.fit/) tanpa meniru skor 0 sampai 100 | Cukup sebagai dasar desain |
| F4 Cuaca | Cuaca luar dari BMKG tingkat desa dengan cadangan Open-Meteo | [Endpoint BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) mengembalikan JSON prakiraan | Klaim sesuai sumber |

---

## 6. Bisnis

1. **Riset harga paket:** harga berbasis biaya tim dan titik impas peternak, karena pembanding tidak menayangkan harga publik. Contohnya BroilerX, yang laman harganya tidak memuat angka saat diakses 28 November 2026.

   Sumber harga ayam hidup:
   - batas bawah Rp19.500 per kg mulai 15 Juli 2026 menurut [detikFinance 7 Juli 2026](https://finance.detik.com/berita-ekonomi-bisnis/d-8562724/alasan-harga-ayam-di-peternak-dipatok-paling-murah-rp-19-500-kg);
   - harga acuan Rp25.000 per kg menurut [Perbadan 6 Tahun 2024](https://peraturan.go.id/files/peraturan-bapanas-no-6-tahun-2024.pdf);
   - kondisi harga di bawah HPP peternak menurut [detikFinance 4 Oktober 2026](https://finance.detik.com/berita-ekonomi-bisnis/d-8691259/harga-ayam-di-kandang-anjlok-lagi).

   Biaya server mengacu pada [Biznet Gio NEO Lite](https://www.biznetgio.com/product/neo-lite).
2. **Titik impas per paket:** nilai satu ekor terselamatkan Rp22.700 sampai Rp36.200, yaitu pendapatan panen dikurangi sisa pakan. FCR fase *grower* sampai *finisher* 1,61 dan deplesi normal mengacu pada [Zulfan dkk. 2025](https://doi.org/10.4025/actascianimsci.v48i1.74435).

   Hasilnya:
   - BROVER Kandang: 21 sampai 33 ekor per siklus, atau 4,2 sampai 13,4 persen dari kematian normal kandang tertutup 10.000 sampai 20.000 ekor;
   - BROVER Saku: 2,1 sampai 3,3 ekor per siklus.

   Sensitivitas terhadap harga ayam hidup dan bobot panen ada di concept Bab 9.2 D.
3. **Lama balik modal unit rover:**
   - 14,1 siklus untuk unit eceran dan 11,6 siklus untuk unit grosir;
   - kontribusi sekitar Rp578.900 per siklus;
   - asumsi dukungan teknis, umur alat, dan pembagi server diberi label `ASUMSI TIM`;
   - pajak dan margin kanal belum dihitung dan sudah dicatat jujur di concept.
4. **Konsistensi kedua paket:** nama, isi, harga, dan cara tagih sama di beberapa tempat:
   - concept Bab 9.1 BMC, 9.2 A, dan Bab 10;
   - `MEMORY.md` dan aturan agent;
   - Gambar 07 dan 09.

   Penagihan per siklus beralasan karena RHPP kemitraan terbit 3 sampai 7 hari setelah panen menurut [Amam dan Harsita 2024](https://ejournal.uin-suska.ac.id/index.php/peternakan/article/view/21188).
5. **Protokol pemindahan unit:** delapan langkah di concept Bab 9.2 G berdasar sumber berikut:
   - [WOAH Terrestrial Code](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/terrestrial-code-online-access/) Bab 6.5: peralatan dibersihkan, didisinfeksi, dan dicatat;
   - [Hansson dkk. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/): pembersihan bahan organik sebelum disinfeksi;
   - [Zhao dkk. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/): disinfektan berdaya rendah hampir tidak efektif terhadap ookista koksidia.

   Sewa antarfarm jangka pendek tetap dilarang.
6. **Catatan risiko bisnis:** modal armada langganan Rp6,7 sampai 8,2 juta per unit di muka adalah risiko terbesar tim. Opsi beli putus untuk mitra B2B mengurangi risiko ini, tetapi harganya masih menunggu konfirmasi.

---

## 7. Kesiapan per Rubrik Juri dan Titik Serangan

| Kriteria | Bobot | Kekuatan | Kelemahan | Kesiapan |
| :--- | :-: | :--- | :--- | :-: |
| Kebaruan | 30 persen | Kombinasi rover kecil, mode stasiun di dok, CV feses berstandar, dan standar umur dengan pembanding SOTA yang jujur, yaitu [AvianAlert](https://github.com/farhan-439/avian_alert), [Talingan](https://github.com/FadhlanHawali/Talingan-Android), dan [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) | Tiap komponen sudah ada di tempat lain; kebaruannya ada di integrasi untuk kandang Indonesia | Sedang |
| Relevansi | 25 persen | Data masalah Indonesia terverifikasi, misalnya [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052) dan [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010) | Mitra uji belum menandatangani kesepakatan | Sedang |
| Kelayakan Teknis | 20 persen | Rover Tahap 1 lulus uji jalan dan rem 500 ms; jadwal 12 minggu rinci | Model dan data lokal belum ada | Sedang |
| Bisnis | 15 persen | Dua paket, titik impas, dan balik modal dengan asumsi berlabel | Harga belum diuji ke peternak; efek belum terukur | Sedang |
| Tim | 10 persen | Empat TI ITS dan satu dokter hewan UNJ dengan peran jelas | Beban kerja dua anggota *Hacker* | Baik |

| Serangan Juri | Jawaban Jujur yang Disiapkan |
| :--- | :--- |
| Dataset feses publik bukan broiler | Benar. Karena itu set uji lokal foto rover dan HP berpasangan berlabel dokter hewan menjadi syarat klaim akurasi, dan akurasi dilaporkan per sumber foto. |
| Mengapa rover, bukan CCTV | Foto feses perlu jarak dekat dan cahaya seragam di lantai, dan sensor perlu setinggi ayam di banyak zona. Di luar putaran, rover tetap mengukur udara dari dok. |
| Ayam terganggu oleh rover | Operasi mulai hari ke-7, kecepatan 0,07 sampai 0,1 m/s, dan ada kriteria berhenti sesi. Robot serupa sudah diuji sepanjang siklus oleh [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) dan [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710). |
| Sensor amonia murah tidak akurat | Ditampilkan sebagai tren kualitatif dan dikalibrasi terhadap alat acuan saat pilot |
| Apa bukti BROVER menurunkan kematian | Belum ada. Titik impas adalah hipotesis pilot, dan pilot membandingkan deplesi dan FCR antarflok bersama dokter hewan. |
| Apa beda dengan Octopus XO | Octopus XO adalah robot penggaru sekam selebar 80 cm dengan harga 20 sampai 34 ribu euro. BROVER berfokus pada skrining feses dan udara dengan paket per siklus yang dibayar setelah panen. |
| Rover menjadi pembawa patogen | SOP satu unit untuk satu kandang, sanitasi roda setiap putaran, dan protokol pemindahan unit delapan langkah |
| Kandang tanpa internet | BROVER Kandang berjalan penuh di Wi-Fi lokal. BROVER Saku mengantre foto sampai ada sinyal. |

---

## 8. Audit Gambar dan Diagram

| Gambar | Status | Catatan Teks dan Isi |
| :--- | :--- | :--- |
| 01 dan 02 Medion | Tidak diubah | Gambar asli sumber. Keterangan di concept menyebut grafik PCR mencampur broiler dan petelur. |
| 03 Arsitektur | Dirender ulang | Dua jalur Kandang di *edge* dan Saku di server, satu detektor Apache-2.0, tanpa audio |
| 04a Pola jalur | Dirender ulang | Titik zona tetap, dok di area *brooding*, 2 putaran per hari, mode stasiun |
| 04b Alur 4 tahap | Dirender ulang | CV feses, status udara terhadap umur, ceklis ABK, triase tiga tombol, laporan dokter hewan |
| 04c Alur pengguna | Dirender ulang | Alur dua paket dan catatan harian ABK |
| 04d Ilustrasi kit 4WD | Tetap dipakai | Foto referensi bentuk kit dari marketplace, bukan foto rover tim; keterangannya sudah menyebut ilustrasi |
| 05 Komputasi dan daya | Dibuat ulang | Tabel spesifikasi resmi papan komputasi dan daya PoC terhadap final; tanpa angka FPS |
| 06 Peta jalan TKT | Dirender ulang | Kelompok TKT diperbaiki; tanpa skema sewa |
| 07 BMC | Dirender ulang | Dua paket dan beli putus, calon mitra ditulis sebagai rencana |
| 08 Jadwal 10 bulan | Dirender ulang | 13 tugas selaras Bab 9.7, pilot mulai hari ke-7 |
| 08b Jadwal 3 bulan | Baru | Gantt 12 minggu, 14 baris, milestone M1 sampai M3; palet tiga warna lolos validator buta warna |
| 09 Titik impas | Baru | Mengganti proyeksi ROI 5 tahun; palet dua warna lolos validator buta warna |

- **Arsip gambar lama:**
  - Gambar 03 sampai 09 versi lama dan grafik 04 lama yang tidak dirujuk disimpan di `06_Project_Concept_BROVER/assets/history/2026-11-28_sebelum_sinkronisasi/` dengan README.
  - Tiga foto mikrofon disimpan di `07_IoT_Hardware_Guide/assets/history/`.
- **Grep teks SVG:** pola lama kosong. Dua kecocokan yang tersisa sah, yaitu tulisan tanpa skor 0 sampai 100 dan riset mikrofon tetap sebagai pengembangan lanjutan.
- **Rujukan gambar markdown:** semuanya valid.
  - concept: 13
  - README: 13
  - TOP5: 37
  - RCA: 5
  - panduan IoT: 72
- **Jumlah gambar di PDF, dihitung dengan `pdfimages`:**
  - PDF TOP5: 37 objek gambar unik dalam 44 halaman. Gambar tabel yang tinggi terpotong ke beberapa halaman, sehingga objek yang sama muncul lebih dari sekali.
  - PDF RCA: 5 gambar dalam 22 halaman.
  - Kedua PDF dibuat dengan skrip baru `08_Evaluasi_Proyek/tools/md_to_pdf.py`, yang menunggu semua gambar termuat. PDF lama hanya memuat 6 gambar untuk TOP5 dan 3 gambar untuk RCA.

---

## 9. Sisa Risiko dan Perbaikan Berprioritas

| No | Perbaikan | Prioritas | Penanggung Jawab | Kriteria Selesai |
| :-: | :--- | :-: | :--- | :--- |
| 1 | Latih detektor Apache-2.0 *baseline* dan jalankan di `Raspberry Pi 4` | P0 | Arya | M1 akhir Desember 2026 |
| 2 | Kumpulkan set uji lokal foto rover dan HP berpasangan dengan label dokter hewan dan OPG | P0 | Dr. drh. Atin Supiyani, M.Si., dan Arya | Jumlah sampel dan sebaran kelas dilaporkan |
| 3 | Dapatkan persetujuan tertulis dua calon mitra uji | P0 | Hikari | Dokumen bertanda tangan |
| 4 | Konfirmasi harga beli putus | P1 | Seluruh tim | Harga final tertulis di concept dan BMC |
| 5 | Tulis aturan RH tropis dan ambang tren amonia | P1 | Ahmad dan Dr. drh. Atin Supiyani, M.Si. | Aturan tertulis dan diuji pada data kandang |
| 6 | Uji bak sekam, baterai, dan mode stasiun | P1 | Ahmad | M2 dan M3 tercapai |
| 7 | Ukur akurasi foto HP sebelum membuka BROVER Saku | P1 | Arya dan Aditya | Akurasi per sumber foto dilaporkan |
| 8 | Ukur selisih waktu peringatan sistem terhadap konfirmasi dokter hewan | P2 | Seluruh tim | Data pilot sebelum memakai kata dini |
| 9 | Isi template proposal dari concept sesuai Bab 13 | P0 | Hikari dan Aditya | Semua bagian template terisi dalam batas kata |

---

## 10. Tautan yang Diuji Dua Kali

Setiap tautan diuji dua kali dengan `08_Evaluasi_Proyek/tools/check_links.py` pada 29 November 2026. Tautan DOI yang berkode 403 atau 202 dicocokkan judulnya ke registri Crossref. Kolom verifikasi isi mencatat bagian sumber yang benar-benar dibaca.

### 10.1 Seluruh Tautan di Laporan Ini

| No | Tautan | Uji Pertama | Uji Ulang Kedua | Verifikasi Isi |
| :-: | :--- | :-: | :-: | :--- |
| 1 | [LPPM Undip](https://lppm.undip.ac.id/wp-content/uploads/Materi-Sosialisasi-TRL1.pdf) | 200 | 200 | PDF hal. 16: Riset Dasar TKT 1 sampai 3, Riset Terapan 4 sampai 6, Riset Pengembangan 7 sampai 9; definisi TKT 3 sampai 7. |
| 2 | [Rowe dkk. 2019](https://doi.org/10.3390/ani9090614) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul tinjauan PLF unggas cocok. |
| 3 | [Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) | 200 | 200 | Teks laman: RK3566, NPU 0,8 TOPS, RAM 2, 4, 8 GB. |
| 4 | [Orange Pi 5](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html) | 200 | 200 | Laman resmi: RK3588S, NPU hingga 6 TOPS INT4, INT8, INT16, RAM 4, 8, 16 GB LPDDR4/4X, daya 5V 4A. |
| 5 | [Luckfox Pico Ultra](https://www.luckfox.com/EN-Luckfox-Pico-Ultra?ci=502) | 200 | 200 | Laman resmi: RV1106G3, NPU 1 TOPS INT8, RAM 256 MB DDR3L, eMMC 8 GB. |
| 6 | [Raspberry Pi 4](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-product-brief.pdf) | 200 | 200 | Product brief: BCM2711 4x Cortex-A72 1,8 GHz, RAM 1 sampai 8 GB LPDDR4, tanpa NPU, daya 5V 3A USB-C. |
| 7 | [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) | 200 | 200 | API GitHub: Apache-2.0. |
| 8 | [Baltrušaitis dkk. 2019](https://doi.org/10.1109/TPAMI.2018.2798607) | 202, registri DOI cocok | 202, registri DOI cocok | Crossref: judul survei dan taksonomi pembelajaran multimodal cocok. |
| 9 | [da Rocha Balthazar dkk. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/) | 200 | 200 | Teks penuh: 0,04 dan 0,07 m/s. |
| 10 | [Caliva dkk. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/) | 200 | 200 | Teks penuh Europe PMC: robot bergerak sekitar 0,05 m/s. |
| 11 | [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | 200 | 200 | Abstrak: kecepatan uji 0,2, 0,4, 0,6 m/s; jarak menghindar 83 sampai 110 cm. |
| 12 | [Wiki DFRobot SEN0567](https://wiki.dfrobot.com/sen0567/) | 200 | 200 | Teks wiki: Qualitative only, 1 sampai 300 ppm. |
| 13 | [Panduan Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) | 200 | 200 | Teks PDF: tabel suhu terhadap RH, sensor setinggi ayam, amonia di bawah 10 ppm. |
| 14 | [Zenodo 4628934](https://zenodo.org/records/4628934) | 200 | 200 | API Zenodo dan isi imgObjDet_Yolo.zip dihitung ulang di memori. |
| 15 | [Zenodo 5801834](https://zenodo.org/records/5801834) | 200 | 200 | API Zenodo: 4 arsip klasifikasi PCR, 1.255 citra, CC BY 4.0, ayam petelur, persilangan, dan lokal. |
| 16 | [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | 200 | 200 | Teks penuh: data dari ayam petelur, persilangan, dan lokal; Xception 98,24 persen tertinggi. |
| 17 | [Henomaly](https://github.com/RishitRai/Henomaly) | 200 | 200 | README: angka uji farm dan PCR, AGPL-3.0, kamera kandang tetap. |
| 18 | [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511) | 200 | 200 | Abstrak OpenAlex: penurunan mendadak konsumsi air dapat menandakan masalah. |
| 19 | [aremyhens.fit](https://aremyhens.fit/) | 200 | 200 | Teks dasbor: Barn health 0/100 dan tiga tombol tindakan. |
| 20 | [Endpoint BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) | 200 | 200 | Respons JSON prakiraan cuaca tingkat desa. |
| 21 | [detikFinance 7 Juli 2026](https://finance.detik.com/berita-ekonomi-bisnis/d-8562724/alasan-harga-ayam-di-peternak-dipatok-paling-murah-rp-19-500-kg) | 200 | 200 | Teks berita: harga ayam hidup di peternak paling murah Rp19.500 per kg, berlaku mulai 15 Juli. |
| 22 | [Perbadan 6 Tahun 2024](https://peraturan.go.id/files/peraturan-bapanas-no-6-tahun-2024.pdf) | 200 | 200 | Teks PDF: harga acuan daging ayam ras atau ayam hidup di produsen Rp25.000 per kg. |
| 23 | [detikFinance 4 Oktober 2026](https://finance.detik.com/berita-ekonomi-bisnis/d-8691259/harga-ayam-di-kandang-anjlok-lagi) | 200 | 200 | Teks berita: harga di kandang Rp21.000 sampai 22.000 per kg, HPP peternak Rp23.000 sampai 23.500 per kg. |
| 24 | [Biznet Gio NEO Lite](https://www.biznetgio.com/product/neo-lite) | 200 | 200 | Laman harga resmi: VPS 2 vCPU 4 GB Rp139.000 per bulan. |
| 25 | [Zulfan dkk. 2025](https://doi.org/10.4025/actascianimsci.v48i1.74435) | 200 | 200 | Crossref judul cocok, terbit daring 3 Nov 2025, vol 48; Tabel 1: deplesi 2,47 dan 4,54 persen, FCR grower-finisher 1,61. |
| 26 | [Amam dan Harsita 2024](https://ejournal.uin-suska.ac.id/index.php/peternakan/article/view/21188) | 200 | 200 | Teks artikel: dokumen RHPP umumnya dikeluarkan 3 sampai 7 hari setelah panen terakhir. |
| 27 | [WOAH Terrestrial Code](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/terrestrial-code-online-access/) | 200 | 200 | Laman aktif berjudul Codes and Manuals WOAH. |
| 28 | [Hansson dkk. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/) | 200 | 200 | Abstrak Europe PMC: pembersihan dan disinfeksi kandang. |
| 29 | [Zhao dkk. 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/) | 200 | 200 | Teks penuh: disinfektan berdaya rendah hampir tidak efektif. |
| 30 | [AvianAlert](https://github.com/farhan-439/avian_alert) | 200 | 200 | README: juara 1 Data Science Cornell Digital Agriculture Hackathon 2025, suara dan feses. |
| 31 | [Talingan](https://github.com/FadhlanHawali/Talingan-Android) | 200 | 200 | API GitHub dan README: produk IoT dan AI suara untuk penyakit pernapasan ayam, tanpa lisensi. |
| 32 | [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) | 200 | 200 | Teks FAQ: 0,12 m/s, turun ke 0,04 m/s, hari 5 sampai sekitar 23, harga 20 sampai 34 ribu euro. |
| 33 | [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052) | 200 | 200 | Abstrak OpenAlex dan Tabel 2 serta 3 dari lampiran lokal. |
| 34 | [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010) | 200 | 200 | Crossref dan abstrak cocok; angka skor 0,28 tidak dicek ulang. |
| 35 | [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak Europe PMC: 1.597 Ross 308, robot dikemudikan manual 3 kali sehari, layak dioperasikan hari 3 sampai 37 dengan gangguan terbatas. |
| 36 | [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) | 200 | 200 | Crossref judul cocok. Teks PMC11017054: robot 6,2 kg, hari 7 sampai 42, kepadatan maksimum 32 kg per m2, Cobb 500, Argentina. |

### 10.2 Ringkasan Hasil Dua Kali Pengecekan

- **Jumlah tautan unik di laporan:** 36.
- **Uji pertama:** kode 200 sebanyak 33, kode 202 sebanyak 1, kode 403 sebanyak 2.
- **Uji ulang kedua:** kode 200 sebanyak 33, kode 202 sebanyak 1, kode 403 sebanyak 2.
- **Tautan yang kodenya berubah antarpengujian:** tidak ada.
- **Penolakan bot:** semua tautan DOI berkode 403 atau 202 sudah dicocokkan judulnya di registri Crossref. Laman non-DOI berkode 403 dicatat apa adanya dan tidak dipakai sebagai satu-satunya bukti klaim.

---

## 11. Catatan Perubahan Peta Fitur dan Bukti

Berkas `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md` hanya diubah pada bagian yang terdampak keputusan baru dan pada kekeliruan faktual:
1. **Bab 1:** butir 7 tentang servo dan dua peran foto HP; butir 11 diganti; butir 12 sampai 15 ditambah, berisi paket dan harga, jalur inferensi, satu model, dan otomatisasi sebagai pengembangan lanjutan.
2. **Bab 2:** baris F1 dan alur butir 3.
3. **Kartu F1:**
   - cara kerja butir 2 dan 5;
   - servo `DS3218` seharga Rp215.000 masuk daftar alat;
   - batas jujur BROVER Saku;
   - pekerjaan tim untuk servo.
4. **Kartu F3:** cara kerja butir 1 dan 2, serta pekerjaan tim untuk foto berpasangan.
5. **Bab 7:** butir 2, 6, dan 15 diperbarui dengan tautan PIO, YOLOv5-CBAM, dan PoultryBot; butir 16 baru.
6. **Tabel 8.1:** baris 79 sampai 81 ditambah, masing-masing berkode 200 pada dua uji.
7. **Bagian 8.2:** sekarang 81 tautan.
   - Uji pertama: 67 berkode 200 dan 14 berkode 403.
   - Uji kedua: 66 berkode 200 dan 15 berkode 403.
8. **Koreksi faktual:** urutan penulis studi vaksinasi IB ditulis Quarles dan Kling, sesuai metadata Crossref.
9. **Pemeriksaan gaya:** `check_style.py` pada peta fitur menghasilkan TOTAL MASALAH 0.

---

## 12. Kesiapan Bagian Template Proposal

| Bagian Template | Batas | Sumber di Concept | Kesiapan |
| :--- | :--- | :--- | :--- |
| Sampul dan lembar pengesahan | Tidak ada | Bab 1 dan Bab 13 | Siap. Data pribadi diisi langsung di docx. |
| Executive Summary | 500 kata | Ringkasan Eksekutif, sekitar 449 kata | Siap |
| Deskripsi permasalahan dan target pengguna | Bagian dari 1.000 kata | Bab 2, 3.1 sampai 3.4 | Siap, perlu diringkas |
| Solusi dan teknologi | 500 kata | Bab 4.1, matriks paket, 4.5, Bab 5 | Siap, perlu diringkas |
| Arsitektur dan cara kerja | 250 kata | Gambar 03, Bab 6, diagram blok 8.3, Bab 9.5 A | Siap |
| Pasar, model bisnis, dan hilirisasi | 250 kata | Bab 9.2 A sampai F dan 9.6 | Siap; harga beli putus menunggu konfirmasi |
| Business Model Canvas | Tidak ada | Bab 9.1 dan Gambar 07 | Siap |
| Jadwal pengembangan purwarupa | Maksimal 3 bulan | Bab 9.7 dan Gambar 08b | Siap |
| Peta jalan dan target TKT | 250 kata | Bab 9.5 A dan B, Gambar 06 | Siap |
| Target luaran dan indikator | Tidak ada | Bab 9.8 | Siap |
| Profil tim | Tabel | Bab 1 dan Bab 9.5 D | Siap |
| Lampiran portofolio | Tidak ada | Daftar periksa di Bab 13 | Disiapkan terpisah, tidak disimpan di repositori publik |
| Daftar pustaka | Gaya Vancouver | Bab 12, 85 entri | Siap; nomori ulang sesuai urutan kutipan di proposal |

**Berkas wajib di luar isi proposal:**
- formulir pendaftaran;
- CV tim;
- pakta integritas;
- tautan foto atau video purwarupa;
- bukti Katsinov.

Semuanya tercatat di akhir Bab 13. Usulan video purwarupa: rover Tahap 1 berjalan lewat web, uji rem 500 ms, dan dasbor awal.

---

## 13. Keputusan yang Masih Terbuka untuk User

1. **Harga final beli putus BROVER Kandang:** usulan saat ini Rp11,5 juta per unit.
2. **Data peternakan mitra keluarga:** tipe kandang dan skala populasinya.
3. **Berkas `*_tmp.html` TOP5 dan RCA:** dibuat ulang dengan path relatif dan tetap terlacak git. Perlu diputuskan apakah tetap disimpan atau dikeluarkan dari repositori.
4. **PDF SmartEars di `08_Evaluasi_Proyek/`:** tidak disentuh, tidak dipindah, dan `.gitignore` tidak diubah. Berkas ini berhak cipta Elsevier dan tidak boleh di-commit.
5. **Status git:** belum ada commit. Bila diminta commit, gunakan Conventional Commits tanpa atribusi AI.
