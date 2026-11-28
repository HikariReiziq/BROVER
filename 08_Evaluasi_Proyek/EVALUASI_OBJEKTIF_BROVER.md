# Evaluasi Objektif Proyek BROVER

- **Peran penelaah:** penelaah independen dengan sudut pandang juri Hackathon Deep Tech, insinyur sistem *embedded* dan AI, serta penelaah domain peternakan unggas.
- **Tanggal pemeriksaan:** 28 November 2026.
- **Ruang lingkup:** seluruh berkas proyek BROVER di repositori ini, ditambah berkas `Proposal TA/` yang dibaca hanya untuk perbandingan silang. Tidak ada berkas lain yang diubah. Laporan ini adalah satu-satunya berkas baru.
- **Metode verifikasi:**
  1. Membaca langsung berkas lokal wajib sesuai Bagian 2 permintaan.
  2. Memeriksa klaim kunci ke sumber primer: API Zenodo, DataCite, Crossref, OpenAlex, Semantic Scholar, Europe PMC, Hugging Face, GitHub, metadata Croissant Kaggle, laman resmi pabrikan, dan teks penuh jurnal akses terbuka.
  3. Untuk klaim angka anotasi, isi arsip diunduh ke memori lalu dihitung ulang, bukan hanya dibaca dari deskripsi.
  4. Seluruh tautan di laporan diuji dua kali. Hasilnya ada di Bab 12.
- **Label status klaim:** **Terverifikasi**, **Keliru**, **Parsial**, dan **Tidak dapat diverifikasi**.
- **Pemisahan isi:** setiap bab memisahkan *fakta terverifikasi*, *keterbatasan nyata*, dan *usulan perbaikan*.
- **Batas laporan ini:**
  - Naskah berbayar yang tidak dapat dibaca utuh, yaitu artikel jurnal SmartEars, Cuan dan kawan-kawan 2022, serta Sun dan kawan-kawan 2023 dan 2024, hanya dinilai dari metadata resmi dan deskripsi dataset.
  - Angka biaya alternatif pada Bab 10 adalah estimasi teknik yang memakai harga komponen dari audit BOM BROVER sendiri. Angka tersebut bukan audit harga pasar baru.
  - Penulisan judul asli BROVER di laporan ini memakai koma sebagai pengganti tanda kurung karena aturan gaya laporan.
- **Catatan koreksi, 28 November 2026:** versi awal laporan ini memakai batas operasi lantai hari ke-5 sampai sekitar 23 sebagai kelemahan utama rover. Batas itu ternyata berasal dari [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/), robot penggaru sekam selebar 80 cm, tanpa alasan tertulis. Studi robot kecil menunjukkan operasi sampai menjelang panen layak: [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) hari 3 sampai 37, [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) hari 7 sampai 42 pada kepadatan hingga 32 kg per m2, [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) pada umur 2 sampai 8 minggu, dan [Balthazar dkk. 2024](https://doi.org/10.3390/ani14071014) yang mencatat benturan bila robot terlalu lambat. Baris yang terdampak sudah dikoreksi. Kelemahan rover lain tetap berlaku: cakupan pita jalur sempit, waktu operator, pengukuran hanya per sesi, serta risiko sekam basah dan fomit. Judul BROVER juga sudah diganti tim menjadi BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler.

---

## 1. Ringkasan Eksekutif Putusan Evaluasi dan Peta Prioritas Temuan

### 1.1 Putusan Singkat per Agenda

| No | Agenda | Putusan | Tingkat |
| :-: | :--- | :--- | :-: |
| 1 | Judul proyek | Frasa *Deteksi Dini* dan *Multi-Modal AI* adalah *overclaim*. Tidak ada modalitas BROVER yang diukur waktu kemunculan gejalanya, dan tidak ada fusi lintas modalitas yang tervalidasi. Frasa *Sistem Inspeksi* dan *Edge-Cloud* dapat dipertahankan. | Kritis |
| 2 | Latar belakang dan rumusan masalah | Masalah mikroklimat didukung bukti kuat dan langsung dapat diintervensi. Masalah penyakit didukung bukti, tetapi angka kerugian yang dipakai adalah simulasi HPAI H5N1 yang tidak dapat dideteksi BROVER, dan indikator dini terkuat menurut RCA tim sendiri belum disentuh. | Tinggi |
| 3 | Analisis dataset TA | Sebagian besar angka kunci TA terkonfirmasi, termasuk audit anotasi YOLO yang tereplikasi persis sampai nama berkas. Ditemukan 11 kekeliruan atau ketidaktepatan. Bab 11A BROVER memuat kekeliruan yang lebih berat daripada berkas TA. | Tinggi |
| 4 | Fitur deteksi penyakit feses dan fisik | Model #1 feses layak sebagai skrining anomali visual bila ditambah data broiler lokal. Model #2 fisik tidak memiliki dasar data penyakit yang sah dan harus diganti fungsinya atau dihapus dari klaim penyakit. | Kritis |
| 5 | Audio respirasi | Data terbuka hanya dua sumber independen. Bukti deteksi lebih awal hanya berasal dari eksperimen inokulasi dengan rekaman kontinu. Protokol 15 detik dari platform bergerak belum memiliki pembanding ilmiah dan tidak dapat mematikan blower kandang. | Tinggi |
| 6 | Model AI dan sinergi TA | Pilihan model wajar. Hasil TA relevan langsung untuk Model #1 dan Orange Pi 3B, tetapi kemungkinan besar tersedia setelah Demo Day. Beban 2 anggota Hacker saat ini melebihi kapasitas. | Tinggi |
| 7 | Matriks fitur | Dari 10 fitur, empat fitur inti layak, tiga fitur pendukung, dan tiga fitur berisiko. Satu fitur inti justru belum ada, yaitu pencatatan tren air minum dan deplesi harian. | Sedang |
| 8 | Solusi, panduan IoT, dan bisnis | Aritmetika BOM konsisten. Proyeksi ROI 498 persen tidak dapat dipertahankan di depan juri. Skema sewa antarfarm bertentangan dengan SOP 1 unit untuk 1 kandang. | Tinggi |
| 9 | Keberadaan rover beroda | Rover bukan komponen yang tidak tergantikan. Rover adalah titik lemah terbesar karena cakupan pita sempit, waktu operator, pengukuran hanya per sesi, dan risiko fomit di sekam. Alasan jendela hari ke-5 sampai 23 sudah dikoreksi, lihat catatan koreksi. | Tinggi |

### 1.2 Peta Prioritas 12 Temuan Teratas

| No | Temuan | Bukti Utama | Rubrik Terdampak | Prioritas |
| :-: | :--- | :--- | :--- | :-: |
| 1 | Bab 11A BROVER menyebut Zenodo 5801834 memiliki anotasi YOLO dan menjadi dataset utama Model #1. Faktanya, rekaman itu hanya berisi 4 arsip klasifikasi PCR, dan seluruh fesesnya dari ayam petelur, persilangan, dan lokal. | [Zenodo 5801834](https://zenodo.org/records/5801834), [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | Kelayakan Teknis 20% | P0 |
| 2 | Judul memakai *Deteksi Dini*, padahal TA pengguna sendiri mengganti istilah itu dengan skrining karena waktu kemunculan gejala tidak diukur. | `Proposal TA/docs/06_BLUEPRINT_TOPIK_TA_FESES_AYAM.md` | Kebaruan 30%, Relevansi 25% | P0 |
| 3 | Model #2 fisik bersandar pada ChickenVerse yang ternyata hanya berisi 15 perilaku normal tanpa kelas sakit, berlisensi non-komersial, dan berstatus *preprint*. | [ChickenVerse GitHub](https://github.com/amirivojdan/ChickenVerse), [Zenodo 20672799](https://zenodo.org/records/20672799) | Kelayakan Teknis 20% | P0 |
| 4 | Dokumen BROVER semula membatasi rover pada hari ke-5 sampai sekitar 23 dengan meniru robot penggaru sekam Octopus XO, sehingga fase *finisher* yang paling rawan cekaman panas sore tidak terlayani. Studi robot kecil menunjukkan batas ini bisa diganti menjadi hari ke-7 sampai panen dengan uji bertahap. | [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/), [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785), [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710), [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111) | Relevansi 25% | P0, sudah dikerjakan di concept |
| 5 | Dasar ROI 498 persen adalah skenario jual dini wabah HPAI hasil simulasi bio-ekonomi, ditambah asumsi efektivitas 30 persen tanpa data. | [Pramuwidyatama dkk. 2023](https://doi.org/10.1016/j.prevetmed.2022.105833) | Pasar dan Bisnis 15% | P0 |
| 6 | Protokol *Stop-Mute-Sample* hanya mematikan motor dan kipas rover. Blower kandang tetap berjalan, dan review terbaru menyebut suara mesin kandang tumpang tindih spektrum dengan suara ayam hingga di atas 18 kHz. | [Sharifuzzaman dkk. 2026](https://doi.org/10.3390/ai7020058) | Kelayakan Teknis 20% | P0 |
| 7 | BROVER menulis AviSense beroperasi hingga sekitar 0,09 m/s. Teks penuh menyebut sekitar 0,05 m/s. Parajuli 2020 hanya menguji 0,2 sampai 0,6 m/s, jadi klaim aman di bawah ambang stres adalah ekstrapolasi. | [AviSense PMC13696172](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/), [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | Kelayakan Teknis 20% | P1 |
| 8 | Dataset audio IceKhoffi adalah salinan dataset vokalisasi Bowen University, sehingga Bab 11A menghitung satu sumber audio dua kali. | [IceKhoffi README](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal), [Mendeley zp4nf2dxbh](https://data.mendeley.com/datasets/zp4nf2dxbh/1) | Kelayakan Teknis 20% | P1 |
| 9 | Sensor `SEN0567` resmi bersifat kualitatif, tetapi Panel 1 dibandingkan dengan ambang Cobb di bawah 10 ppm dan bahaya di atas 20 ppm yang bersifat kuantitatif. | [Wiki DFRobot SEN0567](https://wiki.dfrobot.com/sen0567/), [Cobb Broiler Guide 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) | Kelayakan Teknis 20% | P1 |
| 10 | Keselarasan mitra lemah: slide PT Zara mengarah ke AI plus IoT untuk FCR melalui estimasi bobot per ekor dan pemantauan tempat pakan, sedangkan masalah tertulis PT Edura sama sekali bukan unggas. | `00 Materi Sosialisasi/PT Zara Properti Farm.pdf` halaman 11, `01_Context_Memory/03_MITRA_PT_ECG_EDURA.md` | Relevansi 25% | P1 |
| 11 | Indikator dini terkuat menurut RCA tim sendiri adalah konsumsi air dan pakan serta tren mortalitas harian. BROVER hanya menyediakan isian manual opsional. | `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md`, [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511) | Relevansi 25% | P1 |
| 12 | Beban kerja 2 Hacker mencakup firmware, PCB, edge Python lalu Golang dan C++, backend, tiga model AI, dan integrasi cuaca ganda dalam jadwal seleksi hingga Demo Day. | `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` Bab 5 dan 9.5 | Kapasitas Tim 10%, Kelayakan 20% | P1 |

### 1.3 Hal yang Sudah Kuat dan Layak Dipertahankan

- **Dasbor berbasis standar umur.** Tabel suhu terhadap kelembapan pada Bab 4.2 BROVER cocok persis dengan tabel resmi [Cobb Broiler Guide 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf), mulai hari 0 sampai kepadatan 28 kg per m2.
- **Penolakan skor kesehatan 0 sampai 100 dan alur 3 tombol verifikasi manusia.** Keduanya sejalan dengan posisi alat skrining. Model rujukan [mosiAfrica](https://huggingface.co/mosiAfrica/poultry-disease-mobilenetv2) juga menyebut dirinya *screening aid*, bukan diagnosis.
- **Kejujuran sensor amonia di teks utama.** Wiki resmi DFRobot memang menulis *Qualitative only*.
- **Arsitektur luring.** Endpoint [BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) dan Open-Meteo yang dirujuk berfungsi saat diuji.
- **Panduan IoT Tahap 1.** Urutan rakit, sekring, BMS, gerbang uji multimeter, dan pemisahan jalur daya sudah disiplin dan realistis.

---

## 2. Evaluasi Judul Proyek BROVER dan Alternatif Usulan Judul Bebas Overclaim

**Judul saat ini, ditulis tanpa tanda kurung:** BROVER, Broiler Inspection & Health Rover: Sistem Inspeksi Berbasis Multi-Modal AI dan Edge-Cloud untuk Deteksi Dini Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler.

### 2.1 Bedah Frasa demi Frasa

| Frasa | Klaim yang Tersirat bagi Juri | Bukti yang Tersedia | Putusan |
| :--- | :--- | :--- | :-: |
| BROVER, *Broiler Inspection & Health Rover* | Rover adalah inti solusi dan mampu menilai kesehatan ayam. | Bab 10 laporan ini menunjukkan rover adalah komponen yang paling mudah digantikan. Kata *Health* menyiratkan penilaian status kesehatan, padahal keluaran sistem adalah skrining tanda yang tampak. | **Parsial** |
| Sistem Inspeksi | Sistem membantu kegiatan inspeksi oleh manusia. | Alur 3 tombol dan laporan dokter hewan memang memosisikan sistem sebagai pendukung inspeksi. Rujukan [Henomaly](https://github.com/RishitRai/Henomaly) memakai posisi yang sama: menandai untuk ditinjau, bukan mendiagnosis. | **Tepat** |
| Berbasis *Multi-Modal AI* | Ada model yang menggabungkan citra, suara, dan sensor untuk keputusan bersama yang lebih akurat daripada satu modalitas. | Bab 5 BROVER menulis tiga model dilatih dan dijalankan sekuensial, lalu hasilnya ditampilkan berdampingan. Aturan audio memicu kamera hanya kaskade. Taksonomi [Baltrušaitis dkk. 2019](https://doi.org/10.1109/TPAMI.2018.2798607) menempatkan fusi, keselarasan, dan representasi bersama sebagai inti pembelajaran multimodal. Tidak ada eksperimen fusi pada KPI. Blueprint TA bahkan menolak istilah ini untuk dirinya sendiri. | **Overclaim** |
| *Edge-Cloud* | Inferensi lokal di perangkat dan sinkronisasi ke server. | Desain memang menjalankan inferensi di perangkat dan memakai server untuk sinkronisasi, arsip, laporan, dan cuaca. Bukti pendukung inferensi lokal: pada [Susanto dkk. 2026](https://doi.org/10.62411/jcta.17963), latensi jaringan menyita 97,4 persen total latensi *edge-cloud*, menurut ekstraksi SLR TA. | **Dapat dipertahankan** |
| Deteksi Dini | Sistem menemukan penyakit sebelum peternak biasanya menyadari, dengan selang waktu yang terukur. | Lihat 2.2. Tidak ada modalitas yang divalidasi selang waktunya, dan tidak ada KPI waktu tunggu deteksi. | **Overclaim** |
| Gejala Penyakit | Sistem mengenali gejala penyakit tertentu. | Anomali feses dan suara abnormal adalah tanda klinis, tetapi tidak spesifik satu penyakit. Studi kasus [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) membutuhkan HI, ELISA, PCR, dan flotasi feses untuk memilah koinfeksi. | **Parsial** |
| Pemantauan Mikroklimat | Pemantauan berkelanjutan sepanjang siklus. | Rover hanya mengambil sampel titik per zona selama sesi. Walau rover dapat beroperasi sampai menjelang panen, itu tetap pemantauan berkala, bukan pemantauan berkelanjutan. | **Parsial** |
| Kandang Ayam Broiler | Teruji untuk broiler. | Sasaran benar, tetapi data feses utama tidak berisi broiler: [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) menulis citra diambil dari ayam petelur, persilangan, dan lokal, lalu membandingkannya dengan broiler yang hanya hidup sekitar 5 minggu. | **Parsial** |

### 2.2 Uji Ketat Frasa Deteksi Dini terhadap Setiap Modalitas

1. **Citra feses.**
   - Fakta: kelas `salmo` pada [Zenodo 4628934](https://zenodo.org/records/4628934) diambil satu minggu setelah inokulasi, dan kelas `ncd` dalam tiga hari setelah inokulasi. Kelas `healthy` dan `cocci` berlabel pengamatan di peternakan.
   - Fakta: dataset tidak mencatat hari kemunculan gejala dan tidak memiliki seri waktu per ayam.
   - Kesimpulan: data hanya mendukung pengenalan feses yang sudah tampak abnormal. Itu skrining, bukan deteksi dini.
2. **Audio pernapasan.**
   - Fakta: bukti terkuat datang dari [Mahdavian dkk. 2021](https://doi.org/10.1016/j.apacoust.2020.107756). Broiler yang ditantang IB terdeteksi pada hari ke-3 pascainokulasi dengan akurasi 83 persen, dan ND pada hari ke-4 dengan akurasi 80 persen.
   - Keterbatasan: kondisi itu adalah eksperimen inokulasi dengan kelompok kontrol dan rekaman berulang. BROVER mengambil sampel 15 detik per zona dari platform bergerak dan tidak merancang uji waktu tunggu.
   - Kesimpulan: audio adalah satu-satunya modalitas dengan dasar ilmiah untuk kata dini, tetapi desain BROVER saat ini tidak mereproduksi kondisi bukti tersebut.
3. **Mikroklimat dan amonia.**
   - Fakta: ambang suhu pukul 16.00 di atas 32,8 derajat Celsius dan THI di atas 79 memprediksi mortalitas pada kandang tanpa pendingin di Jawa Tengah, menurut Tabel 6 [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111).
   - Keterbatasan: nilai AUC hanya 0,694 dan 0,709 dengan spesifisitas sekitar 65 persen, jadi ambang ini prediktor sedang yang akan menghasilkan banyak peringatan palsu.
   - Kesimpulan: modalitas ini sah disebut peringatan dini kondisi berisiko, bukan deteksi dini gejala penyakit.

**Putusan judul:** judul lama mengandung *overclaim* pada dua frasa inti, yaitu *Multi-Modal AI* dan *Deteksi Dini*. Kata dini baru layak dipakai bila tim menjalankan validasi longitudinal di kandang mitra. Contoh KPI yang sah: median selisih hari antara peringatan pertama sistem dan diagnosis yang dikonfirmasi dokter hewan atau lonjakan deplesi, diukur pada beberapa siklus.

### 2.3 Tiga Alternatif Judul yang Jujur

| Opsi | Usulan Judul | Kapan Dipakai | Alasan Kekuatan di Depan Juri |
| :-: | :--- | :--- | :--- |
| A | **BROVER: Sistem Inspeksi Bergerak Berbasis Edge AI untuk Skrining Tanda Klinis yang Tampak dan Pemantauan Berkala Mikroklimat Setinggi Ayam pada Kandang Broiler** | Bila tim tetap menjadikan rover sebagai platform utama. | Mempertahankan merek dan rover, menyebut cakupan apa adanya, dan masih memuat dua masalah utama. |
| B | **BROVER: Sistem Pendukung Inspeksi Harian Kandang Broiler Berbasis Edge AI untuk Skrining Anomali Feses dan Evaluasi Mikroklimat terhadap Standar Umur dengan Verifikasi Dokter Hewan** | Rekomendasi utama, bila platform diubah menjadi hibrida sesuai Bab 10. | Menonjolkan nilai yang sudah terbukti kuat: standar umur Cobb dan Ross, verifikasi manusia, dan peran Dr. drh. Atin Supiyani, M.Si. |
| C | **Skrining Anomali Feses dan Pemantauan Mikroklimat Kandang Ayam Broiler Berbasis Computer Vision dan Sensor pada Perangkat Edge** | Bila tim ingin keselarasan istilah maksimal dengan judul TA. | Memakai istilah skrining dan perangkat *edge* yang sama dengan TA, sehingga hasil TA dapat dikutip langsung sebagai fondasi Model #1. |

- **Catatan merek:** bila rover tidak lagi menjadi inti, nama BROVER dapat dipertahankan sebagai merek produk, tetapi kepanjangan *Health Rover* sebaiknya tidak dipakai.
- **Catatan istilah multimodal:** istilah multisensor atau multisumber lebih tepat. Istilah *Multi-Modal AI* baru layak bila tim melatih dan menguji aturan fusi, lalu menunjukkan fusi lebih baik daripada modalitas tunggal pada data uji yang sama.

---

## 3. Evaluasi Latar Belakang, Rumusan Masalah, dan Keselarasan dengan Mitra

### 3.1 Rantai Bukti dari Data Makro ke Intervensi BROVER

| Klaim di Bab 2 dan 3 BROVER | Sumber | Status | Relevansi terhadap yang Benar-benar Diintervensi BROVER |
| :--- | :--- | :-: | :--- |
| Populasi broiler nasional 3,32 miliar ekor, struktur 60 persen industri dan 40 persen peternak kecil-menengah | Slide PT Zara halaman 9 dan [Sumiati dkk. 2025](https://doi.org/10.5713/ab.24.0678) | **Terverifikasi** | Konteks pasar, bukan bukti masalah teknis. |
| Margin kotor normal Rp5,28 juta per siklus dan kerugian Rp22,89 sampai Rp57,35 juta | Tabel 4 [Pramuwidyatama dkk. 2023](https://doi.org/10.1016/j.prevetmed.2022.105833), dicek dari gambar lampiran lokal `02_Problem_Research/assets_v3/lampiran_jurnal_asli/L03_M1_pramuwidyatama2023_tabel4_hpai_ekonomi.png` | **Terverifikasi angka, Parsial pemakaian** | Angka benar, tetapi berlaku khusus HPAI H5N1 dalam simulasi bio-ekonomi. Nilai negatif itu adalah margin kotor, bukan kerugian langsung. Introduksi HPAI hari ke-22 masih menghasilkan margin positif 4,07 juta. BROVER tidak memiliki model yang mendeteksi HPAI. |
| Penyakit bakteri pernapasan dominan dengan predisposisi ventilasi buruk, kepadatan, dan amonia | [Laman Medion 2026](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/) | **Terverifikasi** | Relevan kuat untuk modul mikroklimat. Untuk model feses, hanya koksidiosis yang beririsan langsung dengan kelas dataset. |
| Kasus Hari Farm: AI dikira snot, kematian naik sampai 80 ekor per hari | [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/) | **Terverifikasi, Parsial pemakaian** | Kasus itu terjadi pada peternakan ayam petelur sekitar 10 ribu ekor, bukan broiler. BROVER tidak menandai fakta ini. |
| Skor biosekuriti eksternal 0,28 pada 19 farm | [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010) | **Terverifikasi sebagian** | Judul dan abstrak cocok: 19 farm broiler Jawa Barat dengan tingkat biosekuriti sebagai variabel. Gambar lampiran lokal `L04` hanya memuat definisi variabel, sehingga angka 0,28 dan klaim 4 farm tutup tidak dicek ulang. Angka ini mendukung masalah, tetapi BROVER secara tegas bukan alat biosekuriti, jadi tidak dapat dipakai untuk mengukur manfaat BROVER. |
| 62 persen titik ukur pada zona THI berat, RH rerata 81,9 persen, FPD 40 persen | [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052), Tabel 2 dan 3 pada lampiran lokal `L07a` dan `L07b` | **Terverifikasi sebagian** | RH rerata 81,9 persen dengan rentang 66 sampai 96 persen, amonia rerata 7,28 ppm, dan sekitar 40 persen ayam dengan skor FPD 1 ke atas dicek dari tabel. Angka 62 persen THI berat tidak dicek ulang. Relevan kuat untuk sensor setinggi ayam dan dasbor umur. |
| Kadar air *litter* 46,42 persen di dataran rendah | [Hasibuan dkk. 2021](https://doi.org/10.31186/jspi.id.16.2.171-179), Tabel 3 teks penuh | **Terverifikasi** | Angka berlaku untuk kandang tertutup dataran rendah pada umur 28 hari, sedangkan kadar normal menurut makalah 20 sampai 25 persen. Relevan untuk mikroklimat, sekaligus menjadi bukti hambatan fisik bagi rover. |
| Koinfeksi AI H5, H9, IB, *M. gallisepticum*, dan koksidiosis pada 11.000 broiler | [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) | **Terverifikasi** | Menguatkan perlunya verifikasi dokter hewan. Kasus ini didiagnosis dengan uji laboratorium, bukan citra. |
| Wawancara Edufarmers x PecahTelur | [YouTube FKCNKnTRif0](https://www.youtube.com/watch?v=FKCNKnTRif0) | **Tidak dapat diverifikasi isi** | Tautan aktif, tetapi isi video tidak ditranskrip dalam evaluasi ini. Status non-*peer-reviewed* sudah dicantumkan benar oleh BROVER. |

### 3.2 Lompatan Logika yang Perlu Ditutup

1. **Dari kerugian HPAI ke manfaat BROVER.**
   - Fakta: angka Rp22,89 juta adalah skenario jual dini pada hari ke-8. Skenario jual dini justru adalah praktik *panic selling* yang menyebarkan virus, menurut RCA tim sendiri.
   - Fakta: HPAI adalah penyakit yang penanganannya melibatkan otoritas veteriner. Kode kesehatan hewan [WOAH](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/terrestrial-code-online-access/) mengatur surveilans dan pelaporannya.
   - Masalah: model BROVER mengenali feses abnormal dan suara abnormal secara umum. Belum ada jalur sebab akibat yang terukur dari peringatan BROVER ke penurunan kerugian HPAI sebesar 30 persen.
2. **Dari penyakit dominan ke kelas model.**
   - Fakta: penyakit klinis broiler teratas menurut Medion adalah CRD, kompleks CRD, dan colibacillosis.
   - Fakta: kelas dataset feses publik adalah *Healthy*, *Coccidiosis*, *Salmonella*, dan *Newcastle Disease*.
   - Masalah: hanya koksidiosis yang beririsan kuat. CRD dan colibacillosis tidak terwakili sebagai kelas visual feses.
3. **Dari akar masalah RCA ke fitur.**
   - Fakta: RCA tim, bagian 2.2 butir c dan 4B butir 2, menyebut indikator dini yang hilang adalah penurunan konsumsi pakan dan air, perubahan perilaku, dan tren mortalitas harian.
   - Fakta: [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511) menulis penurunan mendadak konsumsi air dapat menandakan masalah pada flok. [Manning, Chadd, dan Baines 2007](https://doi.org/10.1017/s0043933907001274) mengusulkan konsumsi air sebagai indikator kesejahteraan broiler. Templat catatan harian [Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) memuat kolom mortalitas, konsumsi air, dan konsumsi pakan.
   - Masalah: BROVER hanya menyediakan isian manual opsional pada Panel 4.
4. **Dari klaim jangkauan ke kenyataan cakupan.**
   - Klaim: 1 unit menjangkau hampir seluruh populasi.
   - Fakta: belum ada perhitungan cakupan. Bab 10 menunjukkan kamera hanya merekam pita sekitar 8 sampai 17 persen luas lantai kandang 120 m per sesi.

### 3.3 Keselarasan dengan Mitra

| Mitra | Masalah atau Arah yang Tertulis di Materi Resmi | Kaitan dengan BROVER | Putusan |
| :--- | :--- | :--- | :-: |
| PT Zara Propertifarm, KANOPIS | Halaman 11 slide: *AI + IoT for Smarter Feed Conversion Ratio*, yaitu AI pengendali ADG lewat estimasi bobot per ekor dan IoT pemantau tempat pakan, dengan manfaat data bobot dan kesehatan *real-time*. Lapisan teks slide juga menyebut dua masalah tambahan, yaitu biaya listrik PLN dan gas LPG. Halaman 8 memvalidasi 6 farm dengan total 85.000 ekor. | BROVER menyentuh sisi pemantauan kesehatan dan kondisi lingkungan yang memengaruhi FCR. Estimasi bobot, pemantauan tempat pakan, listrik, dan LPG tidak disentuh. | **Parsial** |
| PT Edura Cipta Gemilang | Masalah tertulis meliputi QC katering, pajak, pemesanan via WhatsApp, kontrak *franchise*, dan PIC MICE. Peran di hackathon adalah dukungan *in-kind* perangkat keras dan juri. | Tidak ada masalah unggas. Kaitan sah hanya sebagai mitra perakitan, pengadaan, dan komersialisasi PTNBH. | **Tidak terkait masalah, terkait peran** |

**Usulan pembingkaian ulang:** tulis bahwa BROVER mendukung visi pemantauan kesehatan dan lingkungan pada peta jalan AI plus IoT PT Zara untuk pelanggan KANOPIS. Jangan menulis bahwa BROVER menjawab *problem statement* utama PT Zara. Untuk Edura, tulis peran sebagai mitra perakitan dan *in-kind*, bukan pemilik masalah.

### 3.4 Usulan Rumusan Masalah yang Lebih Jujur

1. Bagaimana membantu ABK broiler di kandang terbuka dan tertutup menemukan anomali feses dan kondisi mikroklimat di luar standar umur lebih cepat daripada observasi harian manual?
2. Seberapa akurat skrining anomali feses pada data broiler lokal Indonesia yang diberi label oleh dokter hewan dan, bila memungkinkan, dikonfirmasi uji OPG koksidiosis?
3. Apakah evaluasi mikroklimat setinggi ayam terhadap standar umur Cobb 500 dan Ross 308 dapat beroperasi luring dengan biaya yang terjangkau peternak kecil-menengah?

---

## 4. Pemeriksaan Ulang Dataset Feses RGB terhadap Fisik dan Perilaku Ayam RGB

Bab ini memeriksa ulang klaim di empat berkas `Proposal TA/Dataset/01` sampai `04` serta Bab 11A `PROJECT_CONCEPT_BROVER.md`. Setiap baris diuji ke sumber asli, bukan ke ringkasan AI Agent sebelumnya.

### 4.1 Jalur Feses RGB

| Sumber | Klaim di Berkas TA | Hasil Pemeriksaan Langsung | Status |
| :--- | :--- | :--- | :-: |
| [Zenodo 4628934](https://zenodo.org/records/4628934) | 6.812 citra, `cocci` 2.103, `healthy` 2.057, `salmo` 2.276, `ncd` 376, label YOLO dan masker, CC BY 4.0 | Cocok dengan API Zenodo. Deskripsi resmi menambahkan bahwa kelas `salmo` dan `ncd` berasal dari ayam yang diinokulasi. | **Terverifikasi** |
| Arsip `imgObjDet_Yolo.zip` di Zenodo 4628934 | 6.812 berkas label, 9.090 kotak, 357 kotak `class_id` 1, 3 berkas kosong, 3 kotak lebar nol atau negatif, 38,2 persen kotak di bawah 5 persen luas | Arsip diunduh ke memori dan dihitung ulang. Hasilnya persis: 357 kotak terdiri atas 356 di `cocci` dan 1 di `salmo`; berkas kosong `cocci.1272.txt`, `salmo.1539.txt`, `salmo.1596.txt`; kotak rusak di `cocci.523.txt`, `cocci.990.txt`, `cocci.1138.txt`; median luas 8,55 persen dan rerata 15,61 persen. | **Terverifikasi** |
| [Zenodo 5801834](https://zenodo.org/records/5801834) | 1.255 citra PCR: 373, 347, 349, 186; tanpa kotak; ayam petelur, persilangan, dan lokal | Cocok. Isi rekaman hanya `pcrsalmo.zip`, `pcrhealthy.zip`, `pcrcocci.zip`, dan `pcrncd.zip`. | **Terverifikasi** |
| [Zenodo 23374400](https://zenodo.org/records/23374400) | Paket audit Pratama, Noersasongko, Alzami, 14 Oktober 2026, sisa 6.494 citra farm dan 1.201 citra PCR | README di dalam arsip menyatakan *1,201 / 6,494 kept*. README juga menyatakan artikelnya baru dikirim ke *Tropical Animal Health and Production*, jadi belum melalui telaah sejawat. | **Terverifikasi**, dengan catatan status naskah |
| [Mendeley 8pnbzpt2k9.1](https://data.mendeley.com/datasets/8pnbzpt2k9/1) dan [Dianyo/poultry-health](https://huggingface.co/datasets/Dianyo/poultry-health) | 14.618 citra 100 x 100, broiler dan layer, CC BY 4.0, split 11.694 dan 2.924 | Jumlah, lisensi, dan split cocok dengan API Mendeley dan *datasets-server* Hugging Face. | **Terverifikasi** |
| Artikel [Data in Brief 109517](https://doi.org/10.1016/j.dib.2023.109517) | Ditulis Adebayo dkk. 2023 | Crossref mencatat penulis pertama Halleluyah O. Aworinde. Nama Adebayo adalah penulis pertama rekaman datasetnya, bukan artikelnya. | **Keliru** |
| [HF iagovarela](https://huggingface.co/datasets/iagovarela/poultry-disease-dataset) | 9.611 citra, `salmonella` 3.009, `healthy` 2.985, `coccidiosis` 2.958, `newcastle` 659, tanpa lisensi | Berkas `labels.csv` dihitung ulang dan cocok persis. Tag lisensi memang kosong. | **Terverifikasi** |
| [HF Dianyo/poultry-fecal-fl](https://huggingface.co/datasets/Dianyo/poultry-fecal-fl) | Tolok ukur bebas kebocoran terkait makalah lokakarya | Tag repositori menunjuk ke arXiv dan tanpa lisensi. Sesuai aturan proyek, sumber ini hanya pembanding, bukan bukti primer. | **Terverifikasi**, status *preprint* |
| [Kaggle allandclive](https://www.kaggle.com/datasets/allandclive/chicken-disease-1) | 8.067 citra gabungan F1 dan F2, lisensi mengikuti CC BY 4.0 | Metadata Croissant Kaggle menyatakan lisensi *Unknown* dan citra diubah ke 224 piksel. Jumlah 8.067 tidak dapat dihitung tanpa akun. | **Parsial** |
| [Kaggle chandrashekarnatesh](https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases) | Ditaruh di jalur fisik dengan risiko foto nekropsi | Metadata Croissant menyatakan isinya citra feses dari ODK, yaitu turunan dataset Tanzania, diaugmentasi hingga 100.000 citra per kelas, 12,58 GB, lisensi MIT. | **Keliru klasifikasi** |
| [mosiAfrica MobileNetV2](https://huggingface.co/mosiAfrica/poultry-disease-mobilenetv2) | Akurasi 97,9 persen, Macro F1 0,972 pada 57 citra uji | Metrik cocok. Set uji berjumlah 1.022 citra. Angka 57 hanya jumlah citra Newcastle di set uji. | **Keliru sebagian** |
| [Henomaly](https://github.com/RishitRai/Henomaly) | 98,5 sampai 99,6 persen di farm, turun ke 74,6 sampai 78,2 persen di PCR; 49 duplikat; 19 pasang PCR berlabel ganda; recall 0,29 ke 0,80 | Semua angka cocok dengan README. Lisensi AGPL-3.0. Proyek hackathon ini bukan publikasi *peer-reviewed*. | **Terverifikasi** |
| [krishnaik06](https://github.com/krishnaik06/Chicken-Disease-Classification-Projects) | 90 bintang, 110 fork, VGG16, MIT | Cocok. Tambahan: `params.yaml` memakai 2 kelas dan 1 *epoch*, jadi repositori ini tutorial pipeline, bukan acuan model. | **Terverifikasi** |
| Notebook Kaggle ajheshbasnet | Tautan contoh notebook | Tautan mengembalikan kode 404 saat diuji. | **Keliru, tautan mati** |

### 4.2 Jurnal Jalur Feses 2022 sampai 2026

| Jurnal | Klaim di `Dataset/03` | Hasil Pemeriksaan | Status |
| :--- | :--- | :--- | :-: |
| [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | Akurasi tertinggi MobileNetV2 98,02 persen | Abstrak menyebut Xception 98,24 persen sebagai tertinggi dan MobileNetV2 98,02 persen. MobileNetV2 direkomendasikan karena lebih ringan, bukan karena paling akurat. Teks penuh juga menyatakan data berasal dari ayam petelur, persilangan, dan lokal. | **Keliru** |
| [Degu dan Simegn 2023](https://doi.org/10.1016/j.atech.2023.100221) | YOLOv3 plus ResNet50 dua tahap | Abstrak: 10.500 citra Zenodo, mAP ROI 87,48 persen, akurasi ResNet50 98,7 persen. Namun SLR TA sendiri menggugurkan studi ini pada QA dengan skor 45,8 persen, dan `Dataset/03` tidak mencatatnya. | **Terverifikasi angka, Parsial konteks** |
| [Chidziwisano dkk. 2025](https://doi.org/10.1016/j.compag.2024.109765) | Penurunan berat lintas negara | Teks penuh: MobileNet multikelas 0,91 di Tanzania turun ke 0,69 di Malawi, DenseNet 0,95 ke 0,63, ResNet 0,72 ke 0,42. Ras lokal *Mikolongwe* disebut sebagai salah satu penyebab. | **Terverifikasi** |
| [Taşdelen dan Arslan 2025](https://doi.org/10.1016/j.jestch.2025.102002) | MobileNetV2 97,1 persen | Abstrak cocok. SLR TA menemukan augmentasi dilakukan sebelum validasi silang sehingga terjadi kebocoran, lalu menggugurkan studi ini. `Dataset/03` tidak mencatatnya. | **Terverifikasi angka, Parsial konteks** |
| [Islam dkk. 2025](https://doi.org/10.1016/j.atech.2025.101557) | Klasifikasi feses ringan dengan fusi ruang warna RGB, HSV, CIELAB | Abstrak: fitur *handcrafted* multi-ruang warna dengan pengklasifikasi ANN, akurasi 97,04 persen. Ini bukan *deep learning*. SLR TA juga menggugurkannya karena kebocoran data. | **Parsial** |
| [Aworinde dkk. 2023](https://doi.org/10.1016/j.dib.2023.109517) | Data in Brief, deskripsi dataset Nigeria | Isi cocok, atribusi penulis pertama keliru seperti di 4.1. | **Parsial** |

### 4.3 Jalur Fisik dan Perilaku RGB

| Sumber | Klaim di Berkas TA | Hasil Pemeriksaan Langsung | Status |
| :--- | :--- | :--- | :-: |
| [PIO Zenodo 16686320](https://zenodo.org/records/16686320) dan [makalah Scientific Data](https://doi.org/10.1038/s41597-026-07114-5) | 1.435 citra, 327.289 anotasi, 1 kelas, CC BY 4.0 | Zenodo menyebut 1.435 citra, sedangkan abstrak makalah menyebut 1.487 citra. Instans, kelas, dan lisensi cocok. | **Terverifikasi**, ada selisih angka antarsumber |
| [ChickenVerse Zenodo 20672799](https://zenodo.org/records/20672799) | 6.539 citra, 153.764 objek, 15.250 klip, 15 perilaku, CC BY-NC-SA 4.0, *preprint* SSRN | Cocok. Daftar 15 kelas: *resting, feeding, preening, walking, drinking, stretching, standing, litter pecking, running, litter scratching, dust bathing, head scratching, body shaking, wing flapping, defecation*. Tidak ada kelas sakit atau postur abnormal. | **Terverifikasi** |
| [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset) | 102 video, 898.607 frame, 3.560 lintasan, umur 10 sampai 40 hari, AGPL-3.0, lokakarya CV4Animals | Cocok. TA tidak menyebut bahwa labelnya memuat *Inactive*, *Sleeping*, *Panting*, *Sneezing*, dan *Fluffy_Feathers*. Label tetap perilaku, bukan diagnosis. | **Terverifikasi**, kurang lengkap |
| [NESTLER Zenodo 20924893](https://zenodo.org/records/20924893) | 4 perilaku plus 4 titik kunci, CC BY 4.0, direkam di Sliven, Bulgaria | Deskripsi resmi menyebut tiga video dari Bulgaria dan tiga video dari Rwanda. | **Parsial** |
| [MVBroTrack](https://github.com/decide-ugent/multi-view-broiler-tracking) dan [Cardoen dkk. 2025](https://doi.org/10.1016/j.compag.2025.110435) | 4 kamera atas, AGPL-3.0 | Lisensi dan judul makalah cocok. | **Terverifikasi** |
| [Evet-Africa](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) | Sekitar 406 citra, 26 kelas dengan 18 organ dalam, train sama dengan val, AGPL-3.0 | API menunjukkan 407 citra dan 407 label. `dataset.yaml` memang menulis `train: images` dan `val: images`. Kelas dan lisensi cocok. | **Terverifikasi** |
| [IceKhoffi dataset](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) | Cabang visi hanya 24 citra satu kelas | Repositori dataset kini berisi 603 citra dan 603 label satu kelas. Angka 24 berasal dari README [model IceKhoffi](https://huggingface.co/IceKhoffi/chicken-object-detection-yolov11s) yang memang dilatih 21 plus 3 citra. Sumber visualnya kanal YouTube Kipster Farm, yaitu peternakan ayam petelur. Cabang audionya salinan dataset vokalisasi Bowen University. | **Keliru sebagian** |
| [Kaggle ekosupriyanto](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) | Sehat terhadap tidak sehat, lisensi perlu verifikasi | Croissant menyatakan lisensi CC0, tiga kelas *healthy*, *sick*, *dead*, gambar dari *controlled poultry farm environments* dengan kamera dua spektrum, arsip 89,18 MB. Jumlah per kelas, spesies, negara, dan metode diagnosis tidak dicantumkan. | **Parsial** |
| [jeongrubin](https://github.com/jeongrubin/broiler-carcass-candidate-detection) | Membuktikan secara empiris frame RGB tunggal tidak memadai | README adalah ringkasan portofolio tesis: 1 farm, 1 CCTV, 10 hari, 112 bangkai dan 112 hidup, sekuens 120 menit, F1 0,7961. Ambiguitas satu frame dinyatakan sebagai premis, bukan diuji dengan pembanding satu frame. Kode, bobot, dan data tidak dirilis. | **Keliru**, dilebih-lebihkan |
| [Elmessery dkk. 2023](https://doi.org/10.3390/agriculture13081527) | Hasil terbaik bergantung termal dan data privat | Abstrak: 10.000 citra visual dan termal, 50.000 anotasi, kelas *lethargic chickens, slipped tendons, diseased eyes, stressed beaks open, pendulous crop, healthy*. Model termal YOLOv8 terbaik dengan mAP50 0,988. | **Terverifikasi** |
| [Tong dkk. 2024](https://doi.org/10.1016/j.compag.2024.109432) | mAP 95,1 persen, F1 94,2 persen, INT8 di atas 20 FPS, data tertutup | Abstrak cocok. TA tidak menyebut bahwa subjeknya ayam petelur dalam kandang baterai berumur 20 sampai 60 minggu di Tianjin, dan kelas sakit mencakup *frailty*, *fearfulness*, dan jengger kecil, menurut versi naskah penulis. Relevansi untuk broiler di lantai sekam rendah. | **Terverifikasi**, kurang lengkap |
| [Nasiri dkk. 2024](https://doi.org/10.1016/j.compag.2024.108930) | Deteksi dan penghitungan perilaku broiler | Judul cocok. Klaim beban GPU server tidak dapat dicek dari abstrak terbuka. | **Parsial** |
| [Mendeley txjj8mwtz6](https://data.mendeley.com/datasets/txjj8mwtz6/1) | Data fitur postur tabular Zhang 2017, CC BY NC 3.0 | Cocok. Isinya lima berkas xlsx untuk algoritma peringatan dini broiler sakit berbasis postur. | **Terverifikasi** |
| [PoultryVision model](https://huggingface.co/Williamsanderson/PoultryVision) | AGPL-3.0, dataset terkunci | Model AGPL-3.0. Dataset pendampingnya mengembalikan kode 401. | **Terverifikasi** |
| Syafaah dkk. 2024 dan unggahan Roboflow 31 serta 430 citra | Data privat kecil | Laman repositori UMM menolak akses otomatis. Unggahan Roboflow tidak diperiksa. | **Tidak dapat diverifikasi** |

### 4.4 Daftar 11 Kekeliruan atau Ketidaktepatan di Berkas Dataset TA

1. Machuve dkk. 2022: model tertinggi adalah Xception 98,24 persen, bukan MobileNetV2.
2. mosiAfrica: set uji 1.022 citra, bukan 57 citra.
3. IceKhoffi: dataset kini berisi 603 citra. Angka 24 hanya berlaku untuk model.
4. Data in Brief 109517: penulis pertama Aworinde, bukan Adebayo.
5. chandrashekarnatesh: dataset feses, bukan dataset fisik.
6. NESTLER: video juga berasal dari Rwanda, bukan hanya Bulgaria.
7. jeongrubin: tidak membuktikan secara empiris keterbatasan satu frame, dan tidak merilis kode.
8. `Dataset/03` mencantumkan Degu dan Simegn, Taşdelen dan Arslan, serta Islam dkk. sebagai rujukan tanpa catatan bahwa ketiganya gugur pada QA di SLR TA sendiri.
9. Islam dkk. 2025 adalah metode fitur *handcrafted*, bukan *deep learning*.
10. Lisensi Kaggle allandclive di laman resmi adalah *Unknown*, bukan CC BY 4.0, walaupun data asalnya CC BY 4.0.
11. Tautan notebook Kaggle ajheshbasnet sudah mati dengan kode 404.

**Catatan kelengkapan, bukan kekeliruan:** TA belum mencatat konteks ayam petelur dalam kandang baterai pada Tong dkk. 2024, label perilaku terkait kesehatan pada Big Broiler, dan lisensi CC0 serta tiga kelas pada Kaggle ekosupriyanto.

**Kesimpulan audit TA:** inti analisis TA benar. Jalur feses memang jauh lebih layak daripada jalur fisik, karena jalur fisik publik tidak memiliki label penyakit ayam hidup yang sah dan berskala besar. Kekeliruan yang ditemukan tidak membalik kesimpulan TA, tetapi perlu diperbaiki sebelum dikutip di naskah.

### 4.5 Dataset Publik yang Terlewat

| Dataset | Fakta Terverifikasi | Relevansi |
| :--- | :--- | :--- |
| Poultry Mortality Detection V11 milik Suguna Foods, salinan arsip di [Zenodo 24599397](https://zenodo.org/records/24599397), sumber asli di [Roboflow Universe](https://universe.roboflow.com/suguna-foods-private-limited-fjgdl/poultry-mortality-detection-zpykq/dataset/11) | CC BY 4.0, 3.544 citra YOLOv8, satu kelas *Dead-Bird-Annotations*. Isi arsip dihitung ulang: hanya 1.363 citra sumber unik karena Roboflow membuat 3 versi augmentasi per citra latih. Makalah pendampingnya belum terbit. | Satu-satunya dataset publik berlisensi komersial yang ditemukan untuk deteksi bangkai unggas. Cocok untuk merevisi Model #2 menjadi deteksi kandidat bangkai. Spesies dan jenis kandang perlu dicek visual sebelum dipakai. |
| [HF Darayut audio](https://huggingface.co/datasets/Darayut/poultry-disease-detection-audio-dataset) | 6.346 klip, tanpa lisensi, tanpa README asal-usul. | Jumlahnya sama dengan 6.000 klip SmartEars ditambah 346 klip Bowen. Kemungkinan besar unggahan ulang, bukan data baru. Ini inferensi dari jumlah, belum diperiksa per berkas. |

Pencarian API Zenodo dan Hugging Face untuk kata kunci feses ayam, kotoran broiler, broiler sakit, dan suara pernapasan ayam pada November 2026 tidak menemukan dataset RGB feses broiler atau dataset penyakit fisik broiler hidup yang baru dan berlisensi jelas.

### 4.6 Audit Ketidaksinkronan Bab 11A BROVER terhadap Temuan TA

| Baris Bab 11A | Klaim BROVER | Fakta | Status | Perbaikan |
| :-: | :--- | :--- | :-: | :--- |
| 1 | Zenodo 5801834 adalah dataset utama Model #1 dengan anotasi deteksi objek YOLO | Tidak ada label YOLO. Data dari ayam petelur, persilangan, dan lokal. Kotak YOLO hanya ada di Zenodo 4628934. | **Keliru** | Pakai 4628934 yang sudah dibersihkan untuk latih, 5801834 hanya untuk uji eksternal tingkat citra. |
| 1 | 36.265 unduhan, DOI Machuve dkk. 2022 | API Zenodo kini menunjukkan statistik 36.615 yang identik pada kedua rekaman, jadi angka unduhan tidak spesifik untuk satu rekaman. DOI dataset terbit 2021, makalahnya 2022. | **Parsial** | Hapus angka unduhan dari argumen kualitas. |
| 2 | Kaggle allandclive sebagai pengayaan latih dan validasi | Salinan gabungan F1 dan F2, sehingga memakai keduanya bersama Zenodo membawa duplikat dan kebocoran. Lisensi laman *Unknown*. | **Parsial** | Jangan dipakai bersama Zenodo. |
| 3 | iagovarela sebagai *baseline* bersih | Tanpa lisensi dan merupakan gabungan beberapa sumber yang memuat Machuve. | **Parsial** | Hanya untuk audit asal-usul. |
| 4 | Kaggle ekosupriyanto sebagai dataset utama Model #2, lisensi CC0, kontributor Indonesia | Lisensi CC0 dan kelas *healthy*, *sick*, *dead* benar. Asal Indonesia tidak tercantum di metadata. Jumlah citra dan metode diagnosis tidak diketahui. | **Parsial** | Turunkan menjadi data eksplorasi, bukan dataset utama. |
| 5 | ChickenVerse untuk postur abnormal dan perilaku | Tidak ada kelas postur abnormal. Lisensi melarang penggunaan komersial. Status *preprint*. | **Keliru** | Hapus dari rencana komersial. |
| 6 | PIO untuk deteksi dan distribusi broiler | Benar, satu kelas tanpa label kesehatan. | **Terverifikasi** | Tetap sebagai latar sekam. |
| 7 | Evet-Africa cadangan khusus 8 kelas eksternal | Fakta benar, tetapi rata-rata hanya sekitar 15 citra per kelas dan train sama dengan val. | **Parsial** | Jangan dipakai untuk klaim akurasi. |
| 8 | SmartEars 6.000 segmen 5 detik 44,1 kHz, kelas None berarti bising kandang | 6.000 klip dan 3 kelas benar. Kelas None menurut DataCite berarti tidak ada suara ayam, bukan khusus bising kipas. Laju sampel 44,1 kHz tidak tercantum di sumber terbuka yang dapat diakses. | **Parsial** | Tulis definisi kelas sesuai sumber. |
| 9 | Poultry Vocalization 346 berkas, rekaman longitudinal 65 hari | Benar. Namun direkam pada 96 kHz di kandang eksperimen dengan label sakit berdasarkan suara, tanpa konfirmasi laboratorium. | **Parsial** | Cantumkan batas label. |
| 10 | IceKhoffi untuk pengayaan Model #2 dan #3 | Audio adalah salinan baris 9. Visi adalah satu kelas ayam umum dari peternakan petelur. | **Keliru** | Hapus untuk menghindari hitung ganda. |
| 11 | Data mikroklimat Mendeley m9nsjhtsph untuk kalibrasi | 1.920 observasi benar, tetapi deskripsi resmi menyebut tidak ada tanggal, lokasi sensor, maupun luaran biologis. | **Parsial** | Hanya untuk uji perangkat lunak. |
| 13 | jeongrubin sebagai acuan algoritma mati dan tidur | Tidak ada kode. Butuh CCTV diam 120 menit. | **Parsial** | Sebut sebagai bukti batas metode, bukan acuan implementasi. |
| 15 | zebular13 untuk segmentasi rekaman dan bising latar | Deskripsi repositori: data vokalisasi untuk penerjemahan bahasa ayam ke manusia. | **Keliru peran** | Hapus atau ganti dengan studi penyaringan suara broiler. |
| 21 | SIRAGU dan Smart Coop 2.0 sebagai rujukan | Repositori tanpa lisensi, 0 dan 2 bintang. | **Parsial** | Rujuk sebagai inspirasi, jangan salin kode. |
| 22 | YOLOv8n NCNN sekitar 2,3 FPS di Raspberry Pi 4 dari dokumentasi Ultralytics | Laman yang dirujuk kini hanya memuat tolok ukur Raspberry Pi 5, misalnya YOLO26n NCNN 67,03 ms per citra. Angka Raspberry Pi 4 tidak ditemukan. | **Tidak dapat diverifikasi** | Ukur sendiri di perangkat tim. |
| 23 | PoultryVision untuk *transfer learning* Model #2 | Model mendeteksi ayam dan telur, bukan status sakit. Dataset terkunci. | **Parsial** | Hanya untuk deteksi ayam umum. |

---

## 5. Evaluasi Fitur Deteksi Penyakit Feses dan Fisik Ayam serta Fungsi Asli Dataset Fisik Publik

### 5.1 Jawaban Lugas atas Pertanyaan Inti

**Apakah fitur deteksi penyakit dari citra feses dan fisik ayam mungkin diwujudkan tim dengan dataset publik yang ada sekarang?**

| Fitur | Jawaban | Syarat Agar Jujur |
| :--- | :--- | :--- |
| Model #1 CV feses | **Mungkin, sebagai skrining anomali visual feses.** Tidak mungkin sebagai diagnosis koksidiosis, salmonelosis, atau ND. | Latih dari Zenodo 4628934 yang dibersihkan, uji eksternal di Zenodo 5801834 pada tingkat citra, tambah data feses broiler lokal di atas sekam dengan label dokter hewan, dan laporkan penurunan kinerja lintas domain secara terbuka. |
| Model #2 CV fisik ayam untuk penyakit | **Tidak mungkin secara sah dengan data publik saat ini.** | Ganti fungsinya menjadi deteksi kandidat bangkai atau ayam tidak bergerak untuk diperiksa manusia, atau hapus klaim penyakit dari Model #2. |

### 5.2 Bukti untuk Model #1 Feses

- **Kinerja di dalam domain sudah jenuh, kinerja di luar domain turun tajam.**
  - Henomaly: 98,5 sampai 99,6 persen di uji farm, turun ke 74,6 sampai 78,2 persen di set PCR, menurut [README Henomaly](https://github.com/RishitRai/Henomaly).
  - Chidziwisano dkk. 2025: MobileNet multikelas turun dari 0,91 ke 0,69 saat diuji di Malawi, menurut [teks makalah](https://doi.org/10.1016/j.compag.2024.109765).
  - Uji skala kandang Henomaly: recall detektor feses hanya 0,29 sebelum *fine-tune* dengan latar kandang dari video PIO dan NESTLER, lalu naik ke 0,80.
- **Pintasan latar belakang nyata.** Kelas `salmo` dan `ncd` diambil dari ayam yang diinokulasi, menurut deskripsi [Zenodo 4628934](https://zenodo.org/records/4628934). Henomaly menulis bahwa latar inokulasi dapat mewakili kelas.
- **Tidak ada broiler di data latih.** [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) menyatakan citra diambil dari ayam petelur, persilangan, dan lokal.
- **Domain kamera berbeda.** Data publik feses diambil manusia dengan ponsel dari jarak dekat, menurut Machuve dkk. 2022 yang memakai aplikasi ODK di ponsel dan [Aworinde dkk. 2023](https://doi.org/10.1016/j.dib.2023.109517) yang memakai kamera ponsel. Kamera rover berada rendah dan miring sekitar 45 derajat ke depan, sehingga sudut pandang dan skala objek berbeda.

**Usulan konkret untuk Model #1:**
1. Tampilkan tiga kategori visual kepada peternak: feses berdarah atau indikasi koksidiosis, feses encer atau diare, dan feses tampak normal. Empat kelas penelitian TA tetap dipakai di eksperimen, tetapi tidak ditampilkan sebagai nama penyakit.
2. Kumpulkan data lokal bersama Dr. drh. Atin Supiyani, M.Si. Untuk koksidiosis, label terbaik adalah hitungan OPG dari flotasi feses, seperti yang dipakai pada studi kasus [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) dengan 4.400 OPG.
3. Ukur dan laporkan kinerja pada tiga lapis: data Tanzania bersih, set PCR, dan data broiler lokal. Angka tunggal 98 persen dari literatur tidak boleh dipakai sebagai target produk.

### 5.3 Apa yang Sebenarnya Dideteksi Dataset dan Model Fisik Publik

| Kategori Tugas | Dataset atau Model | Label Sebenarnya | Lisensi | Dapat Dipakai untuk Klaim Penyakit? |
| :--- | :--- | :--- | :--- | :-: |
| Keberadaan dan hitung ayam | [PIO](https://zenodo.org/records/16686320), ChickenDet di [ChickenVerse](https://github.com/amirivojdan/ChickenVerse), [IceKhoffi visi](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal), [PoultryVision](https://huggingface.co/Williamsanderson/PoultryVision) | Satu kelas ayam, atau ayam dan telur | CC BY 4.0, CC BY-NC-SA 4.0, tanpa lisensi, AGPL-3.0 | Tidak |
| Perilaku dan postur | ChickenAct di ChickenVerse, [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset), [NESTLER](https://zenodo.org/records/20924893) | Makan, minum, istirahat, berjalan, tidur, tidak aktif, terengah, bersin, dan perilaku normal lain | CC BY-NC-SA 4.0, AGPL-3.0, CC BY 4.0 | Tidak secara langsung. Perilaku seperti terengah dan tidak aktif dapat menjadi indikator kesejahteraan dan cekaman panas bila diamati lama dari kamera tetap. |
| Pelacakan individu | [MVBroTrack](https://github.com/decide-ugent/multi-view-broiler-tracking) | Identitas dan lintasan | AGPL-3.0 | Tidak |
| Bangkai | [Suguna Poultry Mortality V11](https://zenodo.org/records/24599397), [jeongrubin](https://github.com/jeongrubin/broiler-carcass-candidate-detection) | Bangkai satu kelas, atau bangkai terhadap hidup dari sekuens 120 menit | CC BY 4.0, data tesis tidak dirilis | Tidak untuk penyakit. Ya untuk kandidat mortalitas. |
| Sehat, sakit, mati pada ayam hidup | [Kaggle ekosupriyanto](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) | *Healthy*, *sick*, *dead* dari lingkungan terkontrol, tanpa protokol diagnosis | CC0 | Lemah, karena asal-usul dan dasar label tidak jelas. |
| Patologi fisik dengan data privat | [Elmessery dkk. 2023](https://doi.org/10.3390/agriculture13081527), [Tong dkk. 2024](https://doi.org/10.1016/j.compag.2024.109432) | Lesu, tendon tergelincir, mata sakit, paruh terbuka, tembolok menggantung; atau sehat dan sakit pada layer kandang baterai | Data tidak publik | Bukti bahwa masalah dapat diteliti, bukan sumber data untuk tim. |
| Organ nekropsi | [Evet-Africa](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) | 18 dari 26 kelas adalah lesi organ dalam | AGPL-3.0 | Tidak untuk ayam hidup di lantai kandang. |

### 5.4 Kendala Satu Frame RGB dan Platform yang Bergerak

1. **Ayam tidur, lesu, dan mati tampak serupa pada satu frame.** Studi paling dekat, [jeongrubin](https://github.com/jeongrubin/broiler-carcass-candidate-detection), memilih sekuens masker selama 120 menit dari CCTV yang diam justru karena ayam hidup yang beristirahat dapat tidak bergerak lama. Big Broiler juga memisahkan label *Sleeping*, *Inactive*, dan *Lying* sebagai perilaku normal.
2. **Ayam menjauh dari robot.** Pada [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644), jarak menghindar broiler terhadap robot 83 sampai 110 cm bila robot hanya muncul pada hari uji, dan turun ke 30 sampai 63 cm bila robot hadir setiap hari. Artinya, kamera rover yang setinggi ayam lebih sering merekam ayam yang sedang menyingkir daripada ayam dalam posisi alaminya.
3. **Ayam yang terbiasa justru mendekat.** Pada [AviSense](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/), anak ayam yang sering terpapar robot lebih cepat mendekati robot. Ini menambah risiko oklusi kamera dan risiko ayam terlindas.
4. **Pengamatan perilaku butuh garis dasar yang lama.** Henomaly membandingkan setiap kandang terhadap garis dasarnya sendiri memakai kamera kandang tetap, menurut [laman Devpost Henomaly](https://devpost.com/software/holy-crap). Rover yang melintas beberapa menit per hari tidak dapat membangun garis dasar perilaku yang setara.

### 5.5 Putusan untuk Model #2

**Putusan: ganti fungsi, jangan pertahankan sebagai deteksi penyakit fisik.**

| Opsi | Isi | Data | Beban Kerja | Rekomendasi |
| :-: | :--- | :--- | :--- | :-: |
| A | Ganti menjadi deteksi kandidat bangkai atau ayam tidak bergerak. Saat kandidat terdeteksi, rover berhenti dan mengamati 30 sampai 60 detik, atau operator memastikan lewat video. | Suguna CC BY 4.0 ditambah foto lokal | Sedang | **Utama** |
| B | Hapus Model #2 dari lingkup lomba, lalu pindahkan ke pekerjaan lanjutan. | Tidak perlu | Rendah | Cadangan bila waktu sempit |
| C | Pertahankan sebagai deteksi ayam lesu dan gejala fisik. | Tidak ada data sah | Tinggi | **Ditolak** |

- Nilai opsi A tetap terbatas. ABK sudah mengambil bangkai setiap hari, jadi manfaatnya adalah pencatatan otomatis jumlah dan lokasi bangkai untuk tren deplesi, bukan deteksi dini penyakit.
- Jika opsi A dipilih, dasbor harus menyebutnya kandidat bangkai untuk diverifikasi, bukan ayam sakit.

---

## 6. Audit Independen Dataset, Model, dan Kelayakan Fitur Audio Respirasi Ayam

### 6.1 Inventaris Sumber Audio yang Diperiksa

| Sumber | Fakta Terverifikasi | Keterbatasan Nyata | Status Keterbukaan |
| :--- | :--- | :--- | :--- |
| SmartEars: [dataset DOI 10.17632/dy6gtvt4mk.2](https://doi.org/10.17632/dy6gtvt4mk.2), [deskripsi DataCite](https://api.datacite.org/dois/10.17632/dy6gtvt4mk.2), dan [artikel Qiao dkk. 2026](https://doi.org/10.1016/j.compag.2025.111241) | Dari 11.686 potongan, 6.000 klip 5 detik dirilis dengan 2.000 klip per kelas *Healthy*, *Sick*, dan *None*. Kelas *None* berarti tidak ada suara ayam. Label berasal dari beberapa putaran anotasi dokter hewan. Model terbaik RegNet dengan fitur Logfbank, akurasi 96,03 persen pada uji independen. Sistem dipasang di 3 peternakan besar di Hebei, Tiongkok, dan menemukan kejadian penyakit terkonfirmasi sekitar 19 Maret 2024. Lisensi CC BY 4.0. | Teks penuh berbayar dan tidak dapat dibaca. Spesies, sistem kandang, dan laju sampel tidak tercantum di deskripsi terbuka. Deskripsi hanya menyebut bising dari *cages*, perilaku ayam, aktivitas manusia, dan ventilasi mekanis sebagai sumber bising. API publik Mendeley mengembalikan *not found* walaupun DOI aktif. Tidak ditemukan tautan kode atau bobot model. | Data terbuka sebagian. Model tidak terbuka. |
| Bowen University: [Mendeley zp4nf2dxbh](https://data.mendeley.com/datasets/zp4nf2dxbh/1) dan [Data in Brief 109528](https://doi.org/10.1016/j.dib.2023.109528), teks di [PMC10477058](https://pmc.ncbi.nlm.nih.gov/articles/PMC10477058/) | 346 berkas: *healthy* 139, *noise* 86, *unhealthy* 121. Seratus DOC dibagi dua kelompok, satu diobati untuk penyakit pernapasan dan satu tidak. Ayam dikandangkan di lingkungan terpantau. Rekaman 24-bit 96 kHz tiga kali sehari selama 65 hari. Kelompok tanpa pengobatan mulai terdengar sakit setelah 30 hari. | Label sakit berdasarkan suara, tanpa konfirmasi laboratorium. Mikrofon sengaja dijauhkan untuk mengurangi bising. Skala kecil dan kondisi eksperimen. | Terbuka, CC BY 4.0 |
| [IceKhoffi audio](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) | README menyatakan sumber audio adalah dataset Bowen di atas. | Bukan data baru. | Tanpa lisensi |
| [HF Darayut](https://huggingface.co/datasets/Darayut/poultry-disease-detection-audio-dataset) | 6.346 klip tanpa README asal-usul. | Kemungkinan unggahan ulang gabungan SmartEars dan Bowen. | Tanpa lisensi |
| [Mahdavian dkk. 2021](https://doi.org/10.1016/j.apacoust.2020.107756) | Broiler kontrol, ditantang IB, dan ditantang ND. Wavelet entropy mendeteksi IB pada hari ke-3 pascainokulasi dengan akurasi 83 persen, ND pada hari ke-4 dengan akurasi 80 persen. | Eksperimen inokulasi, bukan kandang komersial. | Data tidak terbuka |
| [Carpentier dkk. 2019](https://doi.org/10.1016/j.compag.2019.05.013) | Deteksi bersin otomatis pada kelompok 51 ayam pedaging dengan banyak sumber bising. Ada 763 bersin teranotasi dari 480 menit rekaman, dan bersin hanya 0,24 persen dari potongan kandidat. Sensitivitas 66,7 persen, presisi 88,4 persen. | Satu dari tiga bersin terlewat walau rekaman kontinu. | Data tidak terbuka |
| [Cuan dkk. 2022](https://doi.org/10.1016/j.compag.2022.106740) | Jaringan DPVN untuk mendeteksi ND dari vokalisasi yang diekstrak dari bising kompleks. | Teks penuh berbayar. Metrik tidak diperiksa dalam evaluasi ini. | Data tidak terbuka |
| [Soster dkk. 2025](https://doi.org/10.1016/j.psj.2025.104962) | Sepuluh ayam jantan Ross 308 umur 1 sampai 36 hari, empat jenis vokalisasi, akurasi seimbang 91,1 persen. | Tugasnya vokalisasi kesejahteraan, bukan penyakit. | Tidak diperiksa |
| Review [Sharifuzzaman dkk. 2026](https://doi.org/10.3390/ai7020058), [PDF penerbit](https://mdpi-res.com/d_attachment/ai/ai-07-00058/article_deploy/ai-07-00058.pdf) | Hambatan utama adalah bising latar, ketimpangan data, validasi multi-farm terbatas, dan penerapan. Suara kipas, *feeder*, dan pemanas tumpang tindih spektrum hingga di atas 18 kHz. Tabel pengaturan perekaman di review didominasi mikrofon tetap di tripod, plafon, *feeder*, atau tengah kandang, dan banyak di antaranya merekam kontinu. | Klaim kelayakan pada fasilitas skala komersial dengan presisi dan recall di atas 90 persen merujuk ke studi batuk babi, yaitu [Wang dkk. 2024](https://doi.org/10.1016/j.biosystemseng.2024.01.002), bukan ayam. | Akses terbuka |

### 6.2 Jawaban atas Pertanyaan Agenda 5

1. **Apakah dataset dan model audio respirasi ayam lengkap dan terbuka?**
   - Tidak lengkap. Hanya dua sumber data terbuka yang independen, yaitu SmartEars dan Bowen. Sumber lain adalah salinan.
   - Tidak ditemukan dataset suara broiler Indonesia.
   - Tidak ditemukan bobot model SmartEars yang dapat dipakai ulang. Klaim BROVER tentang adaptasi model SmartEars berarti melatih ulang dari nol dengan data SmartEars.
2. **Apakah sudah pernah diimplementasikan nyata di kandang komersial atau perangkat edge?**
   - Ya untuk sistem mikrofon tetap: SmartEars dipasang di 3 peternakan besar dan menemukan kejadian penyakit terkonfirmasi.
   - Tidak ditemukan bukti publik tentang skrining suara pernapasan unggas dari platform bergerak yang berhenti sebentar per zona.
3. **Seberapa realistis protokol 15 detik dengan INMP441?**

| Aspek | Fakta | Penilaian |
| :--- | :--- | :--- |
| Kemampuan mikrofon | [Datasheet INMP441](https://microcontroller-course.web.cern.ch/Project_Material/resources/INMP441.pdf): SNR 61 dBA, sensitivitas -26 dBFS, respons datar 60 Hz sampai 15 kHz, batas tekanan akustik 120 dB SPL. Vokalisasi umum ayam berada di sekitar 1 sampai 4 kHz menurut review AI 2026. | Mikrofon bukan hambatan utama. Hambatannya adalah adegan akustik kandang. |
| Blower kandang | Protokol hanya menghentikan motor dan kipas rover. Blower atau kipas terowongan kandang tertutup tetap berjalan, dan suara mesin tumpang tindih spektrum dengan suara ayam. | **Tidak realistis** sebagai penyaring bising. Kelas Suara Bising Kandang hanya menandai klip gagal, tidak memulihkan sinyal napas. |
| Hujan di atap seng | Tidak ditemukan studi *peer-reviewed* yang mengukur pengaruh hujan atap seng pada klasifikasi suara unggas. | Risiko yang belum terukur. Wajib diuji di kandang terbuka mitra. |
| Ribuan broiler | Kelas *None* SmartEars berarti tidak ada suara ayam. Di kandang 15.000 ekor hampir tidak pernah ada momen tanpa suara ayam. | Pemetaan kelas BROVER ke kelas SmartEars tidak setara. |
| Durasi 15 detik | Bukti deteksi lebih awal berasal dari rekaman berulang atau kontinu. Carpentier dkk. 2019 mencatat 763 bersin dalam 480 menit, yaitu sekitar 1,6 bersin per menit untuk 51 ekor, dan tetap melewatkan sekitar sepertiga bersin. | Ilustrasi kasar dengan asumsi laju setara eksperimen itu: satu klip 15 detik rata-rata hanya memuat sekitar 0,4 bersin, sehingga sebagian besar klip tidak memuat bersin sama sekali, sebelum dikurangi sensitivitas detektor. Belum ada desain uji waktu tunggu. |
| Klaim radius 3 sampai 5 meter | Tidak ditemukan sumber untuk angka ini di dokumen BROVER maupun literatur yang diperiksa. | **Tidak dapat diverifikasi.** Hapus atau ukur sendiri. |
| Laju sampel 44,1 kHz | Bowen direkam 96 kHz. Laju SmartEars tidak tercantum di sumber terbuka. | Bukan masalah besar karena dapat diubah, tetapi jangan ditulis sebagai fakta SmartEars. |

### 6.3 Putusan Audio

- **Untuk lomba:** turunkan fitur menjadi rekam, simpan, dan putar ulang klip suara untuk dokter hewan. Klasifikasi tiga kelas disajikan sebagai eksperimen dengan label hasil uji, bukan fitur deteksi.
- **Untuk riset lanjutan:** bila audio ingin menjadi fitur inti, pindahkan ke 1 sampai 2 mikrofon tetap per kandang yang merekam kontinu, lalu hitung tren laju kejadian mirip bersin dan batuk per hari. Uji apakah jam malam dengan aktivitas dan bising lebih rendah memberi sinyal lebih bersih. Desain kontinu ini sesuai dengan cara bukti ilmiah yang ada dikumpulkan.
- **Label wajib:** kumpulkan klip lokal dengan label dokter hewan dan, bila ada kasus, konfirmasi laboratorium pada flok yang sama.

---

## 7. Evaluasi Model AI ke Depan dan Peta Sinergi Proposal TA ke Proyek Lomba BROVER

### 7.1 Penilaian Model yang Direncanakan BROVER

| Komponen | Rencana BROVER | Fakta Terverifikasi | Penilaian | Usulan |
| :--- | :--- | :--- | :--- | :--- |
| Detektor CV | `YOLOv8n` atau `YOLO11n`, NCNN di Raspberry Pi 4, RKNN INT8 di Orange Pi 3B | Repositori [Ultralytics](https://github.com/ultralytics/ultralytics) berlisensi AGPL-3.0. [Dokumentasi Raspberry Pi Ultralytics](https://docs.ultralytics.com/guides/raspberry-pi/) kini memuat keluarga YOLO26 dan tolok ukur Raspberry Pi 5, misalnya YOLO11n ONNX 147,20 ms per citra dan YOLO26n NCNN 67,03 ms per citra pada 640 piksel. Angka Raspberry Pi 4 tidak tersedia lagi. | Layak untuk PoC. Belum layak untuk produk tertutup tanpa lisensi komersial. | Pakai `YOLO11n` untuk PoC, lalu ukur sendiri FPS di Raspberry Pi 4 milik tim. |
| Jalur lisensi komersial | Migrasi ke `YOLOX-Nano`, `RT-DETR`, atau `MobileNetV3` berlisensi Apache-2.0 | [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX), [MMDetection](https://github.com/open-mmlab/mmdetection) untuk RTMDet, dan [RT-DETR](https://github.com/lyuwenyu/RT-DETR) berlisensi Apache-2.0. [rknn_model_zoo](https://github.com/airockchip/rknn_model_zoo) berlisensi Apache-2.0, sedangkan [rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2) tidak memakai lisensi standar di GitHub. | Arah benar. | Samakan dengan pilihan TA, yaitu `RTMDet-Tiny` atau `YOLOX-Tiny`. Baca syarat lisensi `rknn-toolkit2` sebelum komersialisasi. |
| Klasifikasi audio | `Log-Mel Spectrogram` dengan `MobileNetV3-Small` atau `2D CNN`, segmen 5 detik, *voting* 3 x 5 detik | SmartEars memakai fitur Logfbank dan RegNet dengan akurasi 96,03 persen, menurut deskripsi DataCite. Bobot model tidak ditemukan. | Pilihan arsitektur bukan hambatan utama. Hambatannya data dan adegan akustik, lihat Bab 6. | Tunda pelatihan klasifikasi untuk lomba. |
| Perangkat *edge* final | Orange Pi 3B, RK3566, NPU 0,8 TOPS, RAM 4 atau 8 GB | [Laman resmi Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) mencantumkan RK3566, NPU 0,8 TOPS, RAM 2, 4, atau 8 GB, Wi-Fi 5, dan modul eMMC. Estimasi 15 sampai 20 FPS di berkas TA adalah perkiraan, belum pengukuran. | Pilihan wajar untuk beban sekuensial. | Jadikan pengukuran RM3 TA sebagai bukti FPS, bukan perkiraan. |
| Model #2 fisik | YOLO dengan data Kaggle, ChickenVerse, dan PIO | Lihat Bab 5. | Tidak sah untuk penyakit. | Ganti fungsi atau hapus. |

### 7.2 Peta Sinergi Hasil TA ke Model #1 BROVER

| Keluaran TA | Isi Menurut Blueprint TA | Manfaat Sah bagi BROVER | Batas yang Wajib Dijaga |
| :--- | :--- | :--- | :--- |
| RM1 | Perbandingan deteksi objek multikelas terhadap *pipeline* lokalisasi-klasifikasi dengan uji McNemar dan *bootstrap* CI | Menentukan apakah Model #1 cukup satu detektor atau perlu detektor ditambah pengklasifikasi potongan, berdasar bukti statistik. | Data TA tidak berisi broiler, menurut batasan butir 3 blueprint TA. |
| RM2 | Penurunan kinerja di set PCR dan komposit latar sekam PIO serta NESTLER, plus efek augmentasi latar | Memberi target kinerja realistis bagi Model #1 di lantai sekam, bukan angka 98 persen dari literatur. | Komposit adalah simulasi, bukan uji kandang Indonesia, menurut batasan butir 6 blueprint TA. |
| RM3 | *Trade-off* kinerja, ukuran berkas, dan latensi FP32 terhadap INT8 di ONNX Runtime CPU dan RKNN NPU | Memberi angka latensi nyata di papan yang sama dengan BROVER final. Ini menggantikan estimasi FPS yang kini belum terverifikasi. | Satu jenis papan, menurut batasan butir 9 blueprint TA. |
| Artefak minggu 1 sampai 4 | Pembersihan anotasi D1, deduplikasi MD5 dan pHash, pembagian berstrata, uji *toolchain* ekspor | Dapat dipakai lebih awal untuk Model #1 tanpa menunggu hasil akhir TA. | Hanya bila jadwal TA sudah berjalan. |
| Kriteria lisensi | Detektor Apache-2.0 sebagai kriteria pemilihan | Menyelesaikan risiko AGPL-3.0 pada produk tertutup. | Tetap uji kinerja, bukan sekadar lisensi. |

**Kecocokan jadwal, dengan asumsi yang dinyatakan:**
- Blueprint TA menyatakan durasi pelaksanaan 16 minggu dan proposal sedang disusun pada mata kuliah dengan pengumpulan final di minggu 16. Tanggal mulai eksekusi tidak tercantum.
- Konteks lomba menempatkan *bootcamp* pada Desember 2026 sampai Februari 2027 dan Demo Day pada Maret 2027, menurut `01_Context_Memory/02_HACKATHON_DFARM_RULES.md`.
- Bila eksekusi TA dimulai semester berikutnya, hasil lengkap RM1 sampai RM3 kemungkinan baru tersedia setelah Demo Day. Hasil TA paling tepat dipakai untuk tahap *pilot testing* dan hilirisasi pada Mei sampai Agustus 2027.

**Batas integritas akademik:** TA dikerjakan oleh M. Hikari Reiziq Rakhmadinta yang di tim lomba berperan sebagai Hustler. BROVER boleh memakai keluaran TA dengan atribusi. Sebaliknya, kontribusi anggota tim lomba tidak boleh masuk ke TA tanpa persetujuan dosen pembimbing. Pisahkan repositori kode dan catat asal setiap artefak.

### 7.3 Batas Beban Kerja 2 Anggota Hacker

Prinsip yang diusulkan: setiap Hacker memegang paling banyak dua jalur besar pada saat yang sama.

| Komponen | Pemilik Saat Ini | Seleksi November 2026 | Bootcamp Desember 2026 sampai Februari 2027 | Setelah Demo Day |
| :--- | :--- | :--- | :--- | :--- |
| Firmware ESP32: gerak, rem darurat 500 ms, sensor I2C dan ADC | Ahmad Syauqi Reza | Wajib | Wajib | Pertahankan |
| Halaman kendali Wi-Fi lokal dan *streaming* video | Ahmad Syauqi Reza | Wajib bila rover tetap | Sederhanakan bila platform hibrida | Sesuai keputusan Bab 10 |
| Inferensi Model #1 di Raspberry Pi 4 dengan Python | Arya Bisma Putra Refman | Demo *baseline* publik | Wajib, ditambah data lokal | Pindah ke Orange Pi 3B |
| Daemon Golang dan C++ RKNN di perangkat | Ahmad dan Arya | Tunda | Tunda, pakai Python `rknn-toolkit-lite2` | Optimasi setelah pilot |
| Backend Golang, PostgreSQL, Mosquitto, MinIO | Ahmad Syauqi Reza | Tunda | Sederhanakan menjadi satu layanan sinkron HTTP dan satu basis data | Tambah broker bila skala menuntut |
| Dasbor Next.js 4 panel | Aditya Reza Daffansyah | Panel 1 dan Panel 2 | Lengkap | Pertahankan |
| Model #2 | Arya Bisma Putra Refman | Hapus dari demo | Opsi A kandidat bangkai bila ada waktu | Sesuai data lokal |
| Klasifikasi audio | Arya Bisma Putra Refman | Rekam dan putar ulang saja | Eksperimen terpisah | Mikrofon tetap |
| Cuaca BMKG dan Open-Meteo | Ahmad Syauqi Reza | Satu sumber | Satu sumber dengan *cache* | Hibrida bila terbukti perlu |
| *Custom carrier PCB* dan *conformal coating* | Ahmad Syauqi Reza | Tunda | Tunda, pakai *perfboard* | Setelah validasi lapangan |
| Mekanik Tahap 3: JGB37-520, BTS7960, LiFePO4, IP65 | Ahmad dan Lab UNJ | Tunda | Hanya bila rover tetap menjadi platform | Sesuai keputusan Bab 10 |
| Laporan 1-klik WhatsApp atau PDF | Aditya dan Arya | Opsional | Wajib | Pertahankan |

---

## 8. Evaluasi Project Concept dan Matriks Keterlacakan Masalah terhadap Fitur

**Akar masalah yang dipakai sebagai acuan,** sesuai RCA tim di `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md` bagian 4B:
- **AM1:** titik buta mikroklimat multi-parameter dan gradien spasial kandang.
- **AM2:** keterlambatan deteksi gangguan kesehatan flok karena mengandalkan observasi visual sesaat, tanpa pelacakan konsumsi pakan dan air, perilaku, dan tren mortalitas harian.
- **AM3:** kebocoran biosekuriti eksternal.
- **AM4:** kerentanan proteksi vaksin dan imunosupresi.
- **AM5:** kesenjangan kapasitas dan disiplin SDM atau ABK.

### 8.1 Matriks Keterlacakan

| No | Fitur | Akar Masalah | Bukti Pendukung | Celah atau Risiko | Kelompok | Keputusan |
| :-: | :--- | :-: | :--- | :--- | :--- | :--- |
| 1 | Rover Inspeksi kendali website Wi-Fi lokal | AM1 dan AM2, sebagian | [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) membuktikan robot darat broiler dapat mencatat suhu, kelembapan, dan amonia. Respons ayam terhadap robot terdokumentasi pada [RobôFrango](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/), AviSense, dan Parajuli. Operasi sampai menjelang panen didukung [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) dan [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710). | Cakupan pita sempit, operator 40 sampai 80 menit per putaran di kandang 120 m, fomit, dan traksi di sekam basah. | **Berisiko atau kurang terkait** | Bukan syarat utama. Ubah bentuk platform, lihat Bab 10. |
| 2 | Sensor `SHT31` atau `FS304-SHT31` dan `SEN0567` setinggi ayam | AM1 | [Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) meminta sensor suhu dipasang setinggi ayam dan amonia di bawah 10 ppm. [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052) mencatat RH rerata 81,9 persen dengan rentang 66 sampai 96 persen pada 14 flok di Jawa Barat. | `SEN0567` kualitatif, sehingga tidak dapat menguji ambang 10 dan 20 ppm. Bila dipasang di rover, data hanya titik sesaat. | **Inti** | Pertahankan sebagai node tetap atau alat genggam. Tampilkan tren relatif terhadap garis dasar kandang. Untuk varian pro, gunakan sensor elektrokimia terkalibrasi seperti [DFRobot SEN0469](https://www.dfrobot.com/product-2513.html). |
| 3 | Prakiraan cuaca hibrida BMKG dan Open-Meteo | AM1 | Ambang sore pukul 16.00 pada [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111). [Data BMKG](https://data.bmkg.go.id/) dan [Open-Meteo](https://open-meteo.com/) aktif. | Dua integrasi untuk satu fungsi pendukung. | **Pendukung** | Pilih satu sumber utama untuk lomba. |
| 4 | CV feses | AM2 | Data publik tersedia dan relevan untuk koksidiosis. | Tidak ada broiler, domain kamera berbeda, label lemah. | **Inti bersyarat** | Skrining tiga kategori visual dengan data lokal berlabel dokter hewan. |
| 5 | CV fisik ayam | AM2 | Tidak ada dataset penyakit ayam hidup yang sah. | Klaim palsu bila dipertahankan. | **Berisiko** | Ganti menjadi kandidat bangkai atau hapus. |
| 6 | Audio pernapasan 15 detik | AM2 | Bukti terkuat dari mikrofon tetap dan eksperimen inokulasi. | Blower kandang, sampel pendek, data tipis. | **Berisiko** | Rekam dan putar ulang. Mikrofon tetap untuk riset. |
| 7 | Dasbor 4 panel standar umur Cobb 500 dan Ross 308 | AM1 dan AM5 | Tabel suhu terhadap RH di Bab 4.2 BROVER cocok persis dengan Cobb 2021. Templat catatan harian Cobb memuat mortalitas, air, pakan, suhu, RH, CO2, dan amonia. | Tabel Cobb hanya sampai RH 70 persen, sedangkan rerata RH kandang Jawa Barat 81,9 persen. Tabel Ross belum diaudit dalam laporan ini. | **Inti** | Pertahankan. Tambah aturan tertulis untuk RH di atas 70 persen bersama THI. Minta Dr. drh. Atin Supiyani, M.Si. memvalidasi tabel Ross terhadap dokumen resmi Aviagen. |
| 8 | Tiga tombol triase manusia | AM2 dan AM5 | Pola yang sama dipakai [aremyhens.fit](https://aremyhens.fit/). | Butuh disiplin isian ABK. | **Inti** | Pertahankan, sekaligus jadikan sumber label untuk pelatihan ulang. |
| 9 | Laporan 1-klik dokter hewan | AM2 | RCA tim mencatat jeda ke laboratorium dan data yang terputus antara peternak, *poultry shop*, dan Dinas. | Perlu persetujuan eksplisit peternak, sudah dirancang. | **Pendukung** | Pertahankan karena murah dan bernilai. |
| 10 | SOP sanitasi roda 1 unit untuk 1 kandang | AM3, khusus risiko yang dibawa rover sendiri | [PMC12414267](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/) menekankan pembersihan mekanis sebelum disinfeksi. [PMC11416347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/) menulis disinfektan berdaya rendah hampir tidak efektif terhadap koksidia. | Hanya menurunkan risiko yang ditambahkan rover. Bertentangan dengan skema sewa yang memindahkan unit antarfarm. | **Pendukung, wajib bila rover tetap** | Wajib bila rover dipakai. Larang perpindahan antarfarm tanpa protokol dekontaminasi. |
| 11 | Belum ada: tren konsumsi air, pakan, dan deplesi harian | AM2 | [Edge dkk. 2025](https://doi.org/10.1016/j.japr.2024.100511), [Manning, Chadd, dan Baines 2007](https://doi.org/10.1017/s0043933907001274), dan templat catatan Cobb. | Saat ini hanya isian manual opsional. | **Inti yang belum ada** | Jadikan panel utama dengan grafik tren dan peringatan penurunan mendadak. Meter air otomatis sebagai pengembangan. |

### 8.2 Ringkasan Klasifikasi

- **Fitur inti wajib:** sensor setinggi ayam, CV feses sebagai skrining, dasbor 4 panel standar umur, dan tiga tombol triase. Satu fitur inti yang harus ditambahkan: tren air, pakan, dan deplesi harian.
- **Fitur pendukung bernilai tambah:** cuaca luar satu sumber, laporan 1-klik dokter hewan, dan SOP sanitasi bila rover tetap dipakai.
- **Fitur berisiko berlebihan atau kurang terkait:** rover sebagai syarat utama, CV fisik untuk penyakit, dan klasifikasi audio 15 detik.

---

## 9. Evaluasi Solusi Menyeluruh, Panduan IoT 3 Tahap, Bisnis, dan Kesiapan Rubrik Juri

### 9.1 Arsitektur Website-First Luring di 192.168.4.1

**Fakta yang kuat:**
- Halaman kendali yang disajikan langsung dari perangkat di jaringan Wi-Fi lokal menghindari ketergantungan internet. Uji endpoint menunjukkan sumber cuaca yang dirujuk aktif, tetapi sistem inti memang tidak memerlukannya.
- Rem darurat 500 ms di ESP32 adalah pengaman yang tepat untuk kendali jarak jauh di dekat hewan.

**Keterbatasan nyata:**
- Rem darurat berbasis sinyal detak membuat operator harus terus terhubung dan terus menekan kontrol selama rover bergerak. Di kandang 120 m dengan kecepatan 0,1 m/s, satu putaran membutuhkan sekitar 40 menit kendali kontinu, lihat Bab 10.
- Antena eksternal baru ada di versi final. Pada PoC, jangkauan Wi-Fi bawaan sepanjang kandang 60 sampai 120 m dengan rangka besi belum diuji.

**Usulan:**
- Ukur RSSI dan latensi video pada jarak 30, 60, 90, dan 120 m di kandang mitra sebelum mengklaim jangkauan.
- Pasang kata sandi WPA2 pada jaringan lokal dan catat prosedur bila HP ABK otomatis berpindah ke data seluler.

### 9.2 Panduan IoT 3 Tahap

| Tahap | Kekuatan | Celah | Perbaikan |
| :-: | :--- | :--- | :--- |
| 1, mobil kontrol web | Inventaris aktual lengkap, sekring dan BMS, jalur daya di luar *breadboard*, gerbang uji multimeter, kriteria lulus terukur termasuk 1 m dalam 10 detik dan rem 0,5 detik. | Tidak ada celah besar untuk uji lantai datar. | Rekam video uji kriteria lulus sebagai bukti purwarupa untuk berkas seleksi. |
| 2, prototipe AI dan sensor | Audit bobot 800 sampai 1.000 g, pemisahan jalur daya, catatan jujur penguatan perangkat lunak INMP441, pembagi tegangan HC-SR04. | Kriteria lulus masih mewajibkan inferensi CV fisik dan klasifikasi audio tiga kelas, padahal Bab 5 dan 6 menunjukkan keduanya belum sah. Bagian tautan masih merujuk Zenodo 5801834 sebagai data latih feses. | Ubah kriteria menjadi inferensi CV feses dan rekam audio yang dapat diputar ulang. Perbaiki rujukan dataset. |
| 3, versi final kandang | Pilihan LiFePO4, BTS7960, ban 110 sampai 120 mm, IP65, PETG, dan PCB berlapis sudah beralasan. | Seluruh tahap mengasumsikan rover tetap menjadi platform. Beban mekanik dan elektronik berat untuk 2 Hacker. Kolong 5 sampai 6 cm lebih rendah daripada tebal sekam maksimum 10 cm dan hanya sedikit di atas rerata 5,1 cm yang tercatat pada Tabel 3 [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052). Laman TDK untuk status siklus hidup INMP441 tidak dapat dibaca otomatis. | Tunda sampai keputusan platform di Bab 10. Cek status produksi INMP441 di distributor sebelum produksi massal. |

### 9.3 Struktur Biaya, Harga, dan Proyeksi

| Butir | Klaim BROVER | Pemeriksaan | Status |
| :--- | :--- | :--- | :-: |
| Subtotal BOM 19 item | Rp7.275.000 eceran, Rp5.900.000 grosir | Dijumlahkan ulang dari Bab 8.2, hasilnya persis sama. Harga per item tidak diaudit ulang ke marketplace dalam evaluasi ini. | **Terverifikasi aritmetika** |
| HPP per unit | Rp8.225.000 dan Rp6.750.000 | Konsisten dengan *overhead* Rp950.000 dan Rp850.000. | **Terverifikasi aritmetika** |
| Untung kotor | Rp2,37 juta atau 20,6 persen, dan Rp3,85 juta atau 33,5 persen | Konsisten dengan harga Rp11,50 juta dan cadangan *cloud* Rp900.000. | **Terverifikasi aritmetika** |
| Biaya yang belum dihitung | Tidak disebut | PPN, margin kanal penjualan bersama KANOPIS atau TSO, layanan lapangan di luar cadangan garansi 10 persen, amortisasi riset, dan sertifikasi. Materi PT Edura sendiri mencatat pajak dapat melampaui margin pada bisnis bermargin tipis, menurut `01_Context_Memory/03_MITRA_PT_ECG_EDURA.md`. | **Celah** |
| Pembanding impor | ChickenBoy di atas Rp100 juta, Octopus XO impor Eropa | Harga Octopus XO 20 ribu sampai 34 ribu euro tercantum di [FAQ resmi](https://www.octopusbiosafety.com/en/faq/xo-en/). [Brosur ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf) tidak mencantumkan harga. | **Parsial** |
| Sewa per siklus | Rp550 ribu sampai Rp650 ribu untuk peternak 3.000 sampai 5.000 ekor | Setara 10,4 sampai 12,3 persen margin kotor normal Rp5,28 juta per siklus untuk 3.000 ekor menurut Pramuwidyatama dkk. 2023. Unit sewaan yang berpindah antarfarm bertentangan dengan SOP 1 unit untuk 1 kandang. | **Berisiko** |

**Asumsi proyeksi 5 tahun dan status buktinya:**

| Asumsi di Bab 9.2 BROVER | Status Bukti |
| :--- | :--- |
| Margin normal Rp26,4 juta per siklus untuk 15.000 ekor | Hasil perkalian linear dari model 3.000 ekor. Skala ekonomi tidak dimodelkan. |
| Kerugian Rp114,45 juta per kejadian | Lima kali skenario jual dini HPAI hari ke-8. Penyakit dan skenarionya tidak sesuai dengan fitur BROVER. |
| Dua kejadian wabah dalam 5 tahun | Tanpa sumber. |
| BROVER mencegah 30 persen kerugian wabah dan 20 persen kerugian mikroklimat rutin | Tanpa data uji. |
| Kerugian mikroklimat rutin Rp1,5 juta per siklus | Tanpa sumber di dokumen BROVER. |
| TCO Rp13 juta | Konsisten dengan harga dan biaya ganti sensor. |

**Putusan:** ROI 498 persen dan titik impas tahun ke-2 tidak dapat dipertahankan di depan juri karena tiga asumsi utamanya tanpa data.

**Usulan pengganti: analisis titik impas yang dapat diuji di pilot.**
- Rumus: TCO Rp13 juta dibagi 30 siklus sama dengan Rp433.333 per siklus.
- Nilai satu ekor ayam panen: bobot 2,0 sampai 2,1 kg menurut [laman Medion](https://www.medion.co.id/info-medion/closed-house-solusi-peningkatan-performa-ayam/), dikali harga ayam hidup Rp16.000 sampai Rp17.500 per kg menurut catatan riset tim di `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md`, menghasilkan Rp32.000 sampai Rp36.750 per ekor. Harga ini wajib diperbarui dengan harga pasar saat pitching.
- Hasil: alat impas bila mencegah kematian atau kerugian setara 12 sampai 14 ekor per siklus pada kandang 15.000 ekor, yaitu sekitar 0,08 sampai 0,09 persen populasi.
- Untuk sewa Rp550 ribu sampai Rp650 ribu, peternak 3.000 ekor impas pada 15 sampai 20 ekor per siklus, yaitu sekitar 0,5 sampai 0,7 persen populasi.
- Angka ini adalah hipotesis pilot. Ukur dengan membandingkan deplesi dan FCR antarflok atau antarkandang selama beberapa siklus, dengan bantuan Dr. drh. Atin Supiyani, M.Si.

### 9.4 Kesiapan terhadap Lima Kriteria Rubrik

Penilaian memakai skala kualitatif Kuat, Cukup, dan Lemah, sesuai sikap proyek yang menolak skor angka arbitrer.

| Kriteria dan Bobot | Kesiapan Saat Ini | Alasan | Perbaikan Paling Berdampak |
| :--- | :-: | :--- | :--- |
| Kebaruan dan Inovasi DeepTech, 30% | **Cukup** | Klaim satu-satunya sistem inspeksi bergerak multimodal terjangkau pada Bab 4.4 BROVER adalah *overclaim*. Robot darat broiler dengan sensor suhu, kelembapan, dan amonia sudah ada pada Octopus XO. Sistem rel dengan kamera, NH3, CO2, deteksi bangkai, dan penilaian ekskreta sudah ada pada ChickenBoy. Triase feses dengan tiga tombol sudah dipakai Henomaly. | Tonjolkan kebaruan yang nyata: biaya rendah, operasi luring, evaluasi standar umur Cobb dan Ross untuk peternak Indonesia, alur dokter hewan, dan data feses broiler lokal berlabel uji OPG bila berhasil dikumpulkan. |
| Relevansi Solusi, 25% | **Cukup** | Kuat untuk cekaman panas dan mikroklimat. Sebagian untuk penyakit. Keselarasan mitra sebagian. | Tambah tren air, pakan, dan deplesi. Bingkai ulang kaitan dengan peta jalan AI plus IoT PT Zara. |
| Kelayakan Teknis dan Purwarupa, 20% | **Cukup untuk PoC, Lemah untuk klaim AI dan lapangan** | Tahap 1 dan 2 realistis. Model #2, audio, dan cakupan rover belum sah. | Sempitkan lingkup demo dan ukur KPI sendiri. |
| Potensi Pasar dan Model Bisnis, 15% | **Cukup** | Harga dan HPP konsisten. ROI berlebihan. Sewa antarfarm berisiko biosekuriti. | Ganti dengan titik impas. Batasi sewa pada satu farm per unit. |
| Kapasitas dan Relevansi Tim, 10% | **Kuat** | Kombinasi TI dan dokter hewan relevan. | Pangkas lingkup agar beban 2 Hacker masuk akal, lihat Bab 7.3. |

### 9.5 Titik Paling Rawan Diserang Juri dan Jawaban Jujur yang Disiapkan

| No | Pertanyaan Juri yang Paling Mungkin | Jawaban Jujur yang Disarankan |
| :-: | :--- | :--- |
| 1 | Data feses Anda bukan dari broiler dan tidak berlatar sekam. Bagaimana Anda tahu model bekerja di kandang? | Akui batasnya, tunjukkan penurunan lintas domain dari Henomaly dan Chidziwisano, lalu tunjukkan rencana data lokal berlabel dokter hewan dan uji OPG. |
| 2 | Apa bukti bahwa sistem ini mendeteksi dini? | Ganti istilah menjadi skrining, lalu tunjukkan rencana uji waktu tunggu di pilot. |
| 3 | Mengapa tidak memakai beberapa sensor statis dan kamera tetap yang lebih murah dan bekerja 24 jam? | Jawab dengan perbandingan Bab 10 dan keputusan platform hibrida. |
| 4 | Apakah rover masih bisa masuk kandang di fase akhir saat ayam besar dan padat? | Tunjukkan bukti Dennis dkk. 2020 dan Marin dkk. 2024, rencana uji bertahap hari ke-7 sampai panen, kriteria berhenti, dan node sensor tetap untuk puncak panas sore. |
| 5 | Bagaimana audio bekerja saat blower menyala? | Akui bahwa fitur ini masih rekam dan putar ulang, dengan rencana mikrofon tetap. |
| 6 | Dari mana ROI 498 persen? | Ganti dengan titik impas 12 sampai 14 ekor per siklus sebagai hipotesis pilot. |
| 7 | Sensor amonia Anda kualitatif. Bagaimana membandingkan dengan batas Cobb 10 ppm? | Tampilkan tren relatif dan sebut opsi sensor elektrokimia terkalibrasi untuk varian pro. |
| 8 | Bukankah rover justru membawa kotoran antarkandang? | Tunjukkan SOP 1 unit 1 kandang dan larangan sewa antarfarm tanpa dekontaminasi. |
| 9 | Model YOLO berlisensi AGPL. Bagaimana menjualnya tertutup? | Tunjukkan jalur detektor Apache-2.0 yang sama dengan TA. |
| 10 | Apa hubungannya dengan masalah PT Zara? | Posisikan sebagai pendukung pemantauan kesehatan dan lingkungan pada peta jalan AI plus IoT untuk FCR, bukan pengganti estimasi bobot. |

---

## 10. Evaluasi Fundamental: Perbandingan Objektif Rover Beroda terhadap Alternatif Non-Rover

### 10.1 Asumsi dan Perhitungan Dasar

| Parameter | Nilai | Sumber atau Status |
| :--- | :--- | :--- |
| Kandang A, tertutup | 120 m x 12 m, 1.440 m2, sekitar 20.000 ekor per lantai | Spesifikasi kandang impor di slide PT Zara, menurut `01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md` |
| Kandang B, terbuka | 60 m x 8 m, 480 m2 | Asumsi penelaah |
| Kecepatan rover | 0,1 m/s, atau 0,05 m/s seperti AviSense | Dokumen BROVER dan [AviSense](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/) |
| Jalur inspeksi | Pola U, panjang sekitar 2 kali panjang kandang per putaran | Gambar 04a BROVER |
| Lebar jejak kamera feses | 0,5 m | Asumsi penelaah untuk kamera miring 45 derajat dengan jarak pandang 30 sampai 50 cm |
| Waktu satu putaran kandang A | 240 m dibagi 0,1 m/s sama dengan 40 menit, atau 80 menit pada 0,05 m/s, belum termasuk berhenti di zona | Perhitungan |
| Waktu satu putaran kandang B | 20 menit pada 0,1 m/s, atau 40 menit pada 0,05 m/s | Perhitungan |
| Luas lantai yang terekam kamera feses per putaran | Kandang A: 240 m x 0,5 m sama dengan 120 m2, atau sekitar 8 persen lantai. Dua putaran empat lajur sekitar 17 persen. Kandang B: sekitar 12,5 persen | Perhitungan dengan asumsi di atas |
| Jendela operasi rover | Target hari ke-7 sampai panen, umumnya hari 27 sampai 35, setelah koreksi | [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785), [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710), dan [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) untuk batas lama |
| Kepadatan akhir siklus | 25 sampai 30 kg per m2 pada kandang tertutup, 13 sampai 15 kg per m2 pada kandang terbuka | [Laman Medion](https://www.medion.co.id/info-medion/closed-house-solusi-peningkatan-performa-ayam/) |

**Implikasi langsung:** klaim 1 unit menjangkau hampir seluruh populasi tidak sesuai perhitungan. Rover mengambil sampel pita sempit, hanya pada dua pertiga awal siklus, dan menuntut operator mengendalikan secara terus-menerus selama puluhan menit.

### 10.2 Perbandingan Head-to-Head

Estimasi biaya memakai harga eceran dari audit BOM BROVER sendiri: ESP32 Rp65.000, probe `FS304-SHT31` Rp325.000, `SEN0567` Rp230.000, kamera `IMX291` Rp550.000, Orange Pi 3B dengan eMMC Rp1.950.000, dan `INMP441` Rp45.000. Kotak, catu daya, dan kabel pendek per node diasumsikan Rp200.000 sampai Rp300.000. Kabel jalur dan pemasangan per kandang diasumsikan Rp300.000 sampai Rp1.000.000. Semua asumsi ini belum diaudit ke pasar.

| Parameter | Rover Darat Beroda | Kamera dan Sensor Statis | Rel atau Kabel Gantung | Aplikasi Ponsel ABK |
| :--- | :--- | :--- | :--- | :--- |
| Biaya perangkat per kandang | Harga jual Rp11,50 juta, HPP Rp6,75 juta sampai Rp8,23 juta | Kandang A: 6 node udara sekitar Rp4,9 juta sampai Rp5,5 juta, ditambah 1 Orange Pi 3B, 2 sampai 4 kamera, 2 mikrofon, dan kabel, total sekitar Rp8,6 juta sampai Rp10,8 juta. Kandang B: sekitar Rp5,9 juta sampai Rp6,5 juta | Kepala sensor sekitar Rp3,9 juta dari komponen yang sama, ditambah rel atau kabel, katrol, dan penggerak 60 sampai 120 m yang harganya belum diaudit | Ponsel milik ABK bila sudah ada, ditambah alat sensor genggam sekitar Rp0,8 juta sampai Rp0,9 juta |
| Waktu operasi dalam siklus | Hari ke-7 sampai panen, per sesi, belum teruji di kandang tropis | Hari 0 sampai panen, 24 jam | Hari 0 sampai panen. ChickenBoy beroperasi dari hari pertama sampai terakhir | Hari 0 sampai panen, mengikuti rutinitas ABK |
| Melihat feses jarak dekat | Ya, tetapi hanya pita di jalur | Hanya titik tetap. Dasbor [aremyhens.fit](https://aremyhens.fit/) milik Henomaly menulis kamera pandangan kandang penuh tidak dapat membaca kotoran karena objeknya terlalu kecil | Dari sekitar 0,5 m di atas ayam. ChickenBoy menyatakan mampu menilai ekskreta, tetapi lantai makin tertutup ayam di akhir siklus | Ya, dan paling sesuai domain dataset karena data publik diambil manusia dengan ponsel dari jarak dekat |
| Membaca udara setinggi ayam | Ya, titik sesaat per zona | Ya, kontinu, sesuai anjuran [Cobb 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) memasang sensor setinggi ayam | Perlu lengan turun. ChickenBoy memakai lengan teleskopik | Ya, titik sesaat bila memakai alat sensor genggam |
| Sekam lembap hingga 46 persen | Risiko traksi dan kandas, tercatat sebagai risiko R02 di BROVER | Tidak terpengaruh | Tidak terpengaruh | Tidak terpengaruh |
| Kepadatan 25 sampai 30 kg per m2 di minggu 4 dan 5 | Bisa dilalui robot kecil hingga 32 kg per m2 menurut Marin dkk. 2024, tetapi kontak dengan ayam meningkat dan laju melambat | Tidak terhalang, hanya oklusi pandangan | Tidak terhalang, oklusi lantai | Manusia tetap berjalan seperti biasa |
| Risiko stres atau panik | Jarak menghindar robot 83 sampai 110 cm melebihi jarak terhadap manusia 48 sampai 82 cm bila robot jarang hadir, menurut [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644). Pemakaian harian menurunkannya | Hampir tidak ada | Rendah. ChickenBoy memakai penunjuk laser untuk membuat ayam bergerak | Sama dengan rutinitas ABK |
| Kontaminasi silang | Roda menjadi fomit. SOP 1 unit 1 kandang mengurangi risiko antarkandang, tetapi sewa antarfarm menambah risiko | Rendah | Rendah, tanpa kontak sekam | Tidak menambah jalur baru karena ABK sudah masuk setiap hari |
| Waktu operator | 40 sampai 80 menit kendali kontinu per putaran di kandang A | Tidak ada | Tidak ada setelah terpasang | Beberapa menit tambahan pada rutinitas berkeliling |
| Kesiapan teknis tim | Tahap 1 dan 2 realistis, versi lapangan berat | Tinggi, IoT standar | Sedang, perlu pekerjaan mekanik rel | Tinggi, memakai PWA dan model yang sama |
| Daya tarik demo juri | Tinggi | Sedang | Sedang sampai tinggi | Sedang |

**Preseden platform non-rover yang bergerak:**
- ChickenBoy berjalan di rel sekitar 0,5 m di atas ayam selama 24 jam dari hari pertama sampai terakhir siklus, menurut brosurnya.
- Tong dkk. 2024 memasang kamera cerdas pada kereta pakan otomatis yang bergerak di kandang baterai ayam petelur, menurut versi naskah penulis dari [artikel tersebut](https://doi.org/10.1016/j.compag.2024.109432). Ini contoh menumpang pada peralatan bergerak yang sudah ada.

### 10.3 Kelebihan Rover yang Tetap Diakui

1. Geometri kamera dan pencahayaan LED yang seragam untuk citra feses, tanpa memasang infrastruktur tetap.
2. Pengukuran udara setinggi ayam di banyak titik dengan satu set sensor.
3. Mengurangi frekuensi orang masuk kandang bila kelak menjadi otonom.
4. Nilai demonstrasi yang tinggi di depan juri dan investor.

### 10.4 Putusan Platform

**Putusan:** rover beroda **bukan** komponen yang tidak tergantikan. Pada desain saat ini, rover adalah **titik lemah terbesar** proyek karena:
- hanya mengukur per sesi, sehingga puncak panas sore di fase akhir tetap butuh node sensor tetap, walau rover dapat beroperasi sampai menjelang panen;
- hanya merekam sekitar 8 sampai 17 persen lantai kandang 120 m per sesi;
- menuntut operator mengendalikan secara kontinu selama puluhan menit;
- menambah risiko mekanis di sekam basah dan risiko fomit;
- menuntut beban mekanik dan elektronik terbesar bagi 2 Hacker.

**Rekomendasi bentuk platform:**

| Prioritas | Bentuk | Isi | Alasan |
| :-: | :--- | :--- | :--- |
| 1, direkomendasikan untuk lomba | Hibrida | Node sensor tetap setinggi ayam 2 sampai 6 unit per kandang untuk suhu, RH, tren amonia, dan opsional mikrofon. Aplikasi PWA luring di ponsel ABK untuk memotret feses saat berkeliling, menjalankan Model #1, dan mengisi tren air, pakan, dan deplesi. | Bekerja sepanjang siklus, sesuai domain data feses, waktu operator kecil, biaya setara atau lebih rendah, dan beban teknis paling masuk akal. |
| 2, bila tim mempertahankan rover | Rover sebagai modul pengambil sampel | Batasi klaim pada hari ke-7 sampai panen dengan uji bertahap dan pada pita jalur. Jangan menjual sewa antarfarm. Ukur cakupan, waktu operator, dan respons ayam di pilot. | Menjaga merek dan aset demo tanpa klaim palsu. |
| 3, pengembangan lanjutan | Troli di kabel atau rel gantung | Kepala sensor yang sama berjalan di atas ayam sepanjang siklus. | Menghapus masalah sekam, fomit, dan jendela operasi. Preseden komersial sudah ada. |

---

## 11. Daftar Tindak Lanjut Prioritas dan Rekomendasi Revisi Konkret

**Keterangan prioritas:** P0 sebelum berkas seleksi dikirim, P1 selama *bootcamp*, P2 setelah Demo Day.

| No | Tindakan | Berkas atau Area | Prioritas | Peran Penanggung Jawab | Dasar | Kriteria Selesai |
| :-: | :--- | :--- | :-: | :--- | :--- | :--- |
| 1 | Ganti judul dengan salah satu opsi di Bab 2.3, lalu hapus frasa *Deteksi Dini* dan *Multi-Modal AI* dari judul, ringkasan eksekutif, BMC, dan visual. | `PROJECT_CONCEPT_BROVER.md`, `README.md`, `MEMORY.md`, `.agent/rules/hackathon-context.md`, `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` | P0 | Hustler, divalidasi Dr. drh. Atin Supiyani, M.Si. | Bab 2 | Tidak ada lagi klaim deteksi dini tanpa rencana uji waktu tunggu. |
| 2 | Koreksi seluruh baris Bab 11A yang berstatus Keliru, Parsial, atau Tidak dapat diverifikasi di Bab 4.6, yaitu baris 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 15, 21, 22, dan 23, termasuk rujukan dataset di panduan IoT Tahap 2 dan 3. | Bab 11A BROVER, bagian tautan panduan `07_IoT_Hardware_Guide/02` dan `03` | P0 | Hacker AI | Bab 4.6 | Setiap dataset tercatat dengan lisensi, spesies, label, dan peran yang benar. |
| 3 | Ganti fungsi Model #2 menjadi kandidat bangkai untuk verifikasi manusia, atau hapus dari lingkup lomba. | Fitur 3, Bab 6.2, KPI Bab 4.4 | P0 | Hacker AI dan Dr. drh. Atin Supiyani, M.Si. | Bab 5.5 | Tidak ada klaim ayam lesu atau gejala fisik tanpa data sah. |
| 4 | Turunkan fitur audio menjadi rekam, simpan, dan putar ulang. Hapus klaim radius 3 sampai 5 m. Tulis definisi kelas *None* sesuai SmartEars. | Fitur 4, Bab 6.2, risiko R04 | P0 | Hacker AI | Bab 6 | Klaim audio tidak melebihi bukti. |
| 5 | Ganti proyeksi ROI 498 persen dengan analisis titik impas dan hipotesis pilot. | Bab 9.2 BROVER, grafik 09, BMC | P0 | Hustler | Bab 9.3 | Setiap asumsi tertulis dengan sumber atau label asumsi. |
| 6 | Perbaiki angka yang tidak cocok sumber: AviSense 0,05 m/s, cakupan uji Parajuli 0,2 sampai 0,6 m/s, angka Raspberry Pi 4 Ultralytics, harga dan sensor suara ChickenBoy, bobot Octopus XO, nomor klausul ISO 8373, label layer pada kasus Hari Farm, dan konteks HPAI pada angka Pramuwidyatama. | Bab 2, 3, 4.3, 4.4, 6.2, 7.1, dan 8.1 BROVER | P0 | Hustler | Bab 3.1, 4.6, 12.2 | Setiap angka memiliki tautan dengan isi yang cocok. |
| 7 | Rumuskan ulang keselarasan mitra: pendukung pemantauan kesehatan dan lingkungan pada peta jalan AI plus IoT PT Zara, dan Edura sebagai mitra perakitan. | Bab 2 dan BMC | P0 | Hustler | Bab 3.3 | Tidak ada klaim menjawab *problem statement* utama PT Zara. |
| 8 | Ganti tautan akar API BMKG dengan laman data resmi atau endpoint adm4. | Referensi 47 BROVER | P0 | Hustler | Bab 12.2 | Tautan berstatus 200 dan isinya sesuai. |
| 9 | Putuskan bentuk platform: hibrida atau rover. Ukur cakupan lantai, waktu operator, dan respons ayam di kandang mitra. | Seluruh konsep dan panduan IoT | P1 | Seluruh tim | Bab 10 | Keputusan tertulis dengan data uji. |
| 10 | Kumpulkan data feses broiler lokal di atas sekam dengan label dokter hewan dan hitungan OPG untuk koksidiosis, lengkap dengan persetujuan peternak. | Model #1 | P1 | Dr. drh. Atin Supiyani, M.Si. dan Hacker AI | Bab 5.2 | Ada set uji lokal yang terpisah dari data latih. |
| 11 | Tambah panel tren konsumsi air, pakan, dan deplesi harian dengan peringatan penurunan mendadak. | Fitur 5, Panel 4 | P1 | Hipster dan Hacker Embedded | Bab 3.2 dan 8.1 | Grafik tren tampil dan peringatan teruji. |
| 12 | Tulis aturan evaluasi untuk RH di atas 70 persen bersama THI, dan ubah tampilan amonia menjadi tren relatif terhadap garis dasar kandang. | Panel 1 | P1 | Hacker Embedded dan Dr. drh. Atin Supiyani, M.Si. | Bab 8.1 | Aturan tertulis dan diuji pada data kandang. |
| 13 | Validasi tabel Ross 308 di Bab 4.2 terhadap dokumen resmi Aviagen. | Bab 4.2 bagian B BROVER | P1 | Dr. drh. Atin Supiyani, M.Si. | Bab 8.1 | Setiap angka bertanda halaman sumber. |
| 14 | Tetapkan detektor Apache-2.0 yang sama dengan TA dan baca syarat lisensi `rknn-toolkit2`. | Bab 9.3 BROVER | P1 | Hacker AI | Bab 7.1 | Model kandidat Apache-2.0 sudah diuji di perangkat. |
| 15 | Sederhanakan arsitektur perangkat lunak sesuai daftar tunda di Bab 7.3. | Bab 5 BROVER | P1 | Hacker Embedded dan Hacker AI | Bab 7.3 | Daftar fitur tunda disetujui tim. |
| 16 | Riset mikrofon tetap per kandang untuk tren laju bersin dan batuk. | Riset lanjutan | P2 | Hacker AI | Bab 6.3 | Rekaman kontinu beberapa siklus berlabel dokter hewan. |
| 17 | Kaji troli kabel atau rel gantung untuk sepanjang siklus. | Riset lanjutan | P2 | Hacker Embedded | Bab 10.4 | Purwarupa mekanik dan uji di kandang. |
| 18 | Uji waktu tunggu deteksi di pilot sebelum memakai kata dini lagi. | Pilot Mei sampai Agustus 2027 | P2 | Seluruh tim | Bab 2.2 | Median selisih hari terukur pada beberapa siklus. |

**Catatan perbaikan untuk berkas TA, dikerjakan nanti di ruang kerja TA dan tidak diubah oleh laporan ini:**
1. `Dataset/03`: Xception adalah model tertinggi di Machuve dkk. 2022.
2. `Dataset/03`: tandai Degu dan Simegn, Taşdelen dan Arslan, serta Islam dkk. sebagai studi yang gugur QA, dan sebut Islam dkk. sebagai metode *handcrafted*.
3. `Dataset/03`: set uji mosiAfrica 1.022 citra.
4. `Dataset/03`: hapus tautan notebook Kaggle ajheshbasnet.
5. `Dataset/01`: IceKhoffi kini 603 citra, sumber visual peternakan ayam petelur, audio salinan Bowen.
6. `Dataset/01`: pindahkan chandrashekarnatesh ke jalur feses.
7. `Dataset/01`: NESTLER direkam di Bulgaria dan Rwanda.
8. `Dataset/01` dan `04`: ubah klaim jeongrubin dari pembuktian empiris menjadi premis studi.
9. `Dataset/02`: penulis pertama Data in Brief 109517 adalah Aworinde.
10. `Dataset/02`: lisensi laman Kaggle allandclive tercatat *Unknown*.
11. Tambahkan dataset Suguna Poultry Mortality V11 sebagai catatan jalur fisik.

---

## 12. Daftar Tautan Sumber Terverifikasi beserta Hasil Pengecekan Ulang Akses dan Isi

### 12.1 Metode Pengecekan

- Setiap URL di laporan ini diuji dua kali dengan permintaan HTTP nyata, mengikuti pengalihan, memakai identitas peramban umum.
- Untuk tautan DOI, keberadaan dan judul juga dicek ke API Crossref karena banyak penerbit menolak akses otomatis dengan kode 403.
- Kolom verifikasi isi menjelaskan cara isi dicocokkan dengan klaim di laporan, misalnya lewat API resmi, teks penuh, atau arsip yang dihitung ulang.
- Kode 202 dari IEEE dan kode 403 dari penerbit adalah penolakan atau penundaan akses bot, bukan tautan mati, selama metadata Crossref cocok.

### 12.2 Seluruh Tautan di Laporan Ini

| No | Tautan | Uji Pertama | Uji Ulang Kedua | Verifikasi Isi |
| :-: | :--- | :-: | :-: | :--- |
| 1 | [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) | 200 | 200 | Teks FAQ: 0,12 m/s, turun ke 0,04 m/s, hari 5 sampai sekitar 23, harga 20 sampai 34 ribu euro. |
| 2 | [Dennis dkk. 2020](https://doi.org/10.1080/00071668.2020.1759785) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak Europe PMC: 1.597 Ross 308, robot dikemudikan manual 3 kali sehari, layak dioperasikan hari 3 sampai 37 dengan gangguan terbatas. |
| 3 | [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) | 200 | 200 | Crossref judul cocok. Teks PMC11017054: robot 6,2 kg, hari 7 sampai 42, kepadatan maksimum 32 kg per m2, Cobb 500, Argentina. |
| 4 | [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | 200 | 200 | Abstrak: kecepatan uji 0,2, 0,4, 0,6 m/s; jarak menghindar 83 sampai 110 cm. |
| 5 | [Balthazar dkk. 2024](https://doi.org/10.3390/ani14071014) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok. Abstrak Europe PMC: 6 minggu, kecepatan 12 rpm memicu benturan, 26 rpm tanpa benturan. |
| 6 | [Zenodo 5801834](https://zenodo.org/records/5801834) | 200 | 200 | API Zenodo: 4 arsip klasifikasi PCR, 1.255 citra, CC BY 4.0, ayam petelur, persilangan, dan lokal. |
| 7 | [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | 200 | 200 | Teks penuh: data dari ayam petelur, persilangan, dan lokal; Xception 98,24 persen tertinggi. |
| 8 | [ChickenVerse GitHub](https://github.com/amirivojdan/ChickenVerse) | 200 | 200 | README dan farm_class_counts.csv: 15 kelas perilaku normal, CC BY-NC-SA 4.0, preprint SSRN. |
| 9 | [Zenodo 20672799](https://zenodo.org/records/20672799) | 200 | 200 | API Zenodo: lisensi CC BY-NC-SA 4.0, ChickenDet dan ChickenAct. |
| 10 | [Mohammadi dkk. 2026](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok; Tabel 6 dari lampiran lokal: 32,8 dan 79, AUC 0,694 dan 0,709. |
| 11 | [Pramuwidyatama dkk. 2023](https://doi.org/10.1016/j.prevetmed.2022.105833) | 200 | 200 | Crossref judul khusus HPAI; Tabel 4 dibaca dari lampiran lokal. |
| 12 | [Sharifuzzaman dkk. 2026](https://doi.org/10.3390/ai7020058) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref judul cocok; teks PDF penerbit dibaca untuk klaim bising dan validasi. |
| 13 | [AviSense PMC13696172](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/) | 200 | 200 | Teks penuh Europe PMC: robot bergerak sekitar 0,05 m/s. |
| 14 | [IceKhoffi README](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) | 200 | 200 | API dan README: 603 citra, 603 label, satu kelas; audio dari dataset Bowen. |
| 15 | [Mendeley zp4nf2dxbh](https://data.mendeley.com/datasets/zp4nf2dxbh/1) | 200 | 200 | API Mendeley: 346 berkas, 139, 86, 121, CC BY 4.0. |
| 16 | [Wiki DFRobot SEN0567](https://wiki.dfrobot.com/sen0567/) | 200 | 200 | Teks wiki: Qualitative only, 1 sampai 300 ppm. |
| 17 | [Cobb Broiler Guide 2021](https://www.cobbgenetics.com/assets/Cobb-Files/Broiler-Guide_English-2021-min.pdf) | 200 | 200 | Teks PDF: tabel suhu terhadap RH, sensor setinggi ayam, amonia di bawah 10 ppm. |
| 18 | [Edge dkk. 2024](https://doi.org/10.1016/j.japr.2024.100511) | 200 | 200 | Abstrak OpenAlex: penurunan mendadak konsumsi air dapat menandakan masalah. |
| 19 | [mosiAfrica](https://huggingface.co/mosiAfrica/poultry-disease-mobilenetv2) | 200 | 200 | Model card: uji 1.022 citra, Newcastle 57 citra, MIT, screening aid. |
| 20 | [BMKG adm4](https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=31.71.03.1001) | 200 | 200 | Respons JSON prakiraan cuaca tingkat desa. |
| 21 | [Henomaly](https://github.com/RishitRai/Henomaly) | 200 | 200 | README: angka uji farm dan PCR, AGPL-3.0, kamera kandang tetap. |
| 22 | [Baltrušaitis dkk. 2019](https://doi.org/10.1109/TPAMI.2018.2798607) | 202, registri DOI cocok | 202, registri DOI cocok | Crossref: judul survei dan taksonomi pembelajaran multimodal cocok. |
| 23 | [Susanto dkk. 2026](https://doi.org/10.62411/jcta.17963) | 200 | 200 | Crossref judul cocok; angka latensi dari ekstraksi SLR TA. |
| 24 | [Hartady dkk. 2026](https://doi.org/10.3390/vetsci13040364) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref dan abstrak: 11.000 broiler, koinfeksi AI H5 dan H9. |
| 25 | [Zenodo 4628934](https://zenodo.org/records/4628934) | 200 | 200 | API Zenodo dan isi imgObjDet_Yolo.zip dihitung ulang di memori. |
| 26 | [Mahdavian dkk. 2021](https://doi.org/10.1016/j.apacoust.2020.107756) | 200 | 200 | Abstrak: IB hari ke-3 83 persen, ND hari ke-4 80 persen. |
| 27 | [Sumiati dkk. 2025](https://doi.org/10.5713/ab.24.0678) | 200 | 200 | Crossref dan abstrak OpenAlex: porsi 60 dan 40 persen. |
| 28 | [Laman Medion 2026](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/) | 200 | 200 | Teks laman: penyakit bakteri pernapasan dominan dengan predisposisi ventilasi dan amonia. |
| 29 | [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/) | 200 | 200 | Teks laman: peternakan layer sekitar 10 ribu ekor, Desember 2022. |
| 30 | [Anwar Sani dkk. 2025](https://doi.org/10.1016/j.psj.2025.106010) | 200 | 200 | Crossref dan abstrak cocok; angka skor 0,28 tidak dicek ulang. |
| 31 | [Wilcox dkk. 2025](https://doi.org/10.1017/awf.2025.10052) | 200 | 200 | Abstrak OpenAlex dan Tabel 2 serta 3 dari lampiran lokal. |
| 32 | [Hasibuan dkk. 2021](https://doi.org/10.31186/jspi.id.16.2.171-179) | 200 | 200 | Teks penuh PDF penerbit: Tabel 3 kadar air 46,42 persen. |
| 33 | [YouTube FKCNKnTRif0](https://www.youtube.com/watch?v=FKCNKnTRif0) | 200 | 200 | Video aktif; isi tidak ditranskrip. |
| 34 | [WOAH](https://www.woah.org/en/what-we-do/standards/codes-and-manuals/terrestrial-code-online-access/) | 200 | 200 | Laman aktif berjudul Codes and Manuals WOAH. |
| 35 | [Manning, Chadd, dan Baines 2007](https://doi.org/10.1017/s0043933907001274) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul konsumsi air sebagai indikator kesejahteraan broiler. |
| 36 | [Zenodo 23374400](https://zenodo.org/records/23374400) | 200 | 200 | API Zenodo dan README arsip: 1.201 dan 6.494 citra, naskah masih submitted. |
| 37 | [Mendeley 8pnbzpt2k9.1](https://data.mendeley.com/datasets/8pnbzpt2k9/1) | 200 | 200 | API Mendeley: 14.618 citra 100 x 100, broiler dan layer, CC BY 4.0. |
| 38 | [Dianyo/poultry-health](https://huggingface.co/datasets/Dianyo/poultry-health) | 200 | 200 | datasets-server: split 11.694 dan 2.924, CC BY 4.0. |
| 39 | [Data in Brief 109517](https://doi.org/10.1016/j.dib.2023.109517) | 200 | 200 | Crossref: penulis pertama Aworinde. |
| 40 | [HF iagovarela](https://huggingface.co/datasets/iagovarela/poultry-disease-dataset) | 200 | 200 | labels.csv dihitung ulang: 9.611 baris, tanpa lisensi. |
| 41 | [HF Dianyo/poultry-fecal-fl](https://huggingface.co/datasets/Dianyo/poultry-fecal-fl) | 200 | 200 | API: tanpa lisensi, tag arXiv. |
| 42 | [Kaggle allandclive](https://www.kaggle.com/datasets/allandclive/chicken-disease-1) | 200 | 200 | Metadata Croissant: lisensi Unknown, 224 piksel. |
| 43 | [Kaggle chandrashekarnatesh](https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases) | 200 | 200 | Metadata Croissant: citra feses ODK teraugmentasi, MIT, 12,58 GB. |
| 44 | [krishnaik06](https://github.com/krishnaik06/Chicken-Disease-Classification-Projects) | 200 | 200 | API GitHub dan params.yaml: MIT, VGG16, 2 kelas, 1 epoch. |
| 45 | [Degu dan Simegn 2023](https://doi.org/10.1016/j.atech.2023.100221) | 200 | 200 | Abstrak OpenAlex: 10.500 citra, mAP 87,48 persen, akurasi 98,7 persen. |
| 46 | [Chidziwisano dkk. 2025](https://doi.org/10.1016/j.compag.2024.109765) | 200 | 200 | Teks penuh lokal SLR TA: tabel akurasi Tanzania dan Malawi. |
| 47 | [Taşdelen dan Arslan 2025](https://doi.org/10.1016/j.jestch.2025.102002) | 200 | 200 | Abstrak OpenAlex: MobileNetV2 97,1 persen. |
| 48 | [Islam dkk. 2025](https://doi.org/10.1016/j.atech.2025.101557) | 200 | 200 | Abstrak OpenAlex: fitur handcrafted dan ANN 97,04 persen. |
| 49 | [PIO Zenodo 16686320](https://zenodo.org/records/16686320) | 200 | 200 | API Zenodo: 1.435 citra, 327.289 instans, CC BY 4.0. |
| 50 | [makalah Scientific Data](https://doi.org/10.1038/s41597-026-07114-5) | 200 | 200 | Abstrak OpenAlex: 1.487 citra, 327.289 instans. |
| 51 | [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset) | 200 | 200 | README: 102 video, 28 label perilaku dan postur, AGPL-3.0. |
| 52 | [NESTLER Zenodo 20924893](https://zenodo.org/records/20924893) | 200 | 200 | API Zenodo: CC BY 4.0, video Bulgaria dan Rwanda. |
| 53 | [MVBroTrack](https://github.com/decide-ugent/multi-view-broiler-tracking) | 200 | 200 | API GitHub: AGPL-3.0. |
| 54 | [Cardoen dkk. 2025](https://doi.org/10.1016/j.compag.2025.110435) | 200 | 200 | Crossref: judul deteksi dan pelacakan multi-kamera cocok. |
| 55 | [Evet-Africa](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) | 200 | 200 | API dan dataset.yaml: 407 citra, train sama dengan val, AGPL-3.0. |
| 56 | [model IceKhoffi](https://huggingface.co/IceKhoffi/chicken-object-detection-yolov11s) | 200 | 200 | README model: 24 citra, 21 latih dan 3 validasi. |
| 57 | [Kaggle ekosupriyanto](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) | 200 | 200 | Metadata Croissant: CC0, healthy, sick, dead, 89,18 MB. |
| 58 | [jeongrubin](https://github.com/jeongrubin/broiler-carcass-candidate-detection) | 200 | 200 | README: ringkasan tesis, F1 0,7961, kode dan data tidak dirilis. |
| 59 | [Elmessery dkk. 2023](https://doi.org/10.3390/agriculture13081527) | 403, registri DOI cocok | 403, registri DOI cocok | Abstrak OpenAlex: 10.000 citra visual dan termal, mAP50 0,988 termal. |
| 60 | [Tong dkk. 2024](https://doi.org/10.1016/j.compag.2024.109432) | 200 | 200 | Abstrak Semantic Scholar: mAP 95,1 persen, F1 94,2 persen; konteks subjek dari naskah penulis. |
| 61 | [Nasiri dkk. 2024](https://doi.org/10.1016/j.compag.2024.108930) | 200 | 200 | Crossref: judul deteksi dan penghitungan perilaku broiler cocok. |
| 62 | [Mendeley txjj8mwtz6](https://data.mendeley.com/datasets/txjj8mwtz6/1) | 200 | 200 | API Mendeley: lima berkas xlsx, CC BY NC 3.0. |
| 63 | [PoultryVision model](https://huggingface.co/Williamsanderson/PoultryVision) | 200 | 200 | API HF: AGPL-3.0; dataset pendamping kode 401. |
| 64 | [Zenodo 24599397](https://zenodo.org/records/24599397) | 200 | 200 | API Zenodo dan isi arsip dibaca via range: 1 kelas, 1.363 citra sumber unik. |
| 65 | [Roboflow Universe](https://universe.roboflow.com/suguna-foods-private-limited-fjgdl/poultry-mortality-detection-zpykq/dataset/11) | 403, penolakan bot | 200 | Pengambilan manual pertama berstatus 200 dengan judul Poultry Mortality Detection v11; uji otomatis berstatus 403 karena pembatasan bot. Isi dataset diverifikasi lewat salinan Zenodo. |
| 66 | [HF Darayut audio](https://huggingface.co/datasets/Darayut/poultry-disease-detection-audio-dataset) | 200 | 200 | README: 6.346 contoh audio, tanpa lisensi. |
| 67 | [laman Devpost Henomaly](https://devpost.com/software/holy-crap) | 200 | 200 | Teks laman: Winner QNX dan Photon iMessage Track. |
| 68 | [dataset DOI 10.17632/dy6gtvt4mk.2](https://doi.org/10.17632/dy6gtvt4mk.2) | 200 | 200 | DataCite: deskripsi, lisensi CC BY 4.0, 6.000 klip. |
| 69 | [deskripsi DataCite](https://api.datacite.org/dois/10.17632/dy6gtvt4mk.2) | 200 | 200 | JSON DataCite: deskripsi lengkap SmartEars. |
| 70 | [artikel Qiao dkk. 2026](https://doi.org/10.1016/j.compag.2025.111241) | 200 | 200 | Crossref: penulis Qiao dkk., volume 241. |
| 71 | [Data in Brief 109528](https://doi.org/10.1016/j.dib.2023.109528) | 200 | 200 | Crossref dan teks Europe PMC: 100 DOC, 96 kHz, 65 hari. |
| 72 | [PMC10477058](https://pmc.ncbi.nlm.nih.gov/articles/PMC10477058/) | 200 | 200 | Laman aktif berjudul artikel dataset vokalisasi. |
| 73 | [Carpentier dkk. 2019](https://doi.org/10.1016/j.compag.2019.05.013) | 200 | 200 | Crossref dan abstrak: 763 bersin, sensitivitas 66,7 persen. |
| 74 | [Cuan dkk. 2022](https://doi.org/10.1016/j.compag.2022.106740) | 200 | 200 | Crossref: judul deteksi ND berbasis suara cocok. |
| 75 | [Soster dkk. 2025](https://doi.org/10.1016/j.psj.2025.104962) | 200 | 200 | Abstrak Semantic Scholar: 10 ayam Ross 308, 91,1 persen. |
| 76 | [PDF penerbit](https://mdpi-res.com/d_attachment/ai/ai-07-00058/article_deploy/ai-07-00058.pdf) | 200 | 200 | Teks PDF dibaca, termasuk daftar rujukan. |
| 77 | [Wang dkk. 2024](https://doi.org/10.1016/j.biosystemseng.2024.01.002) | 200 | 200 | Crossref: judul batuk babi cocok. |
| 78 | [Datasheet INMP441](https://microcontroller-course.web.cern.ch/Project_Material/resources/INMP441.pdf) | 200 | 200 | Teks datasheet cermin: SNR 61 dBA, 60 Hz sampai 15 kHz. |
| 79 | [Ultralytics](https://github.com/ultralytics/ultralytics) | 200 | 200 | API GitHub: AGPL-3.0. |
| 80 | [Dokumentasi Raspberry Pi Ultralytics](https://docs.ultralytics.com/guides/raspberry-pi/) | 200 | 200 | Teks laman: tolok ukur Raspberry Pi 5 dan YOLO26. |
| 81 | [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) | 200 | 200 | API GitHub: Apache-2.0. |
| 82 | [MMDetection](https://github.com/open-mmlab/mmdetection) | 200 | 200 | API GitHub: Apache-2.0. |
| 83 | [RT-DETR](https://github.com/lyuwenyu/RT-DETR) | 200 | 200 | API GitHub: Apache-2.0. |
| 84 | [rknn_model_zoo](https://github.com/airockchip/rknn_model_zoo) | 200 | 200 | API GitHub: Apache-2.0. |
| 85 | [rknn-toolkit2](https://github.com/airockchip/rknn-toolkit2) | 200 | 200 | API GitHub: NOASSERTION. |
| 86 | [Laman resmi Orange Pi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) | 200 | 200 | Teks laman: RK3566, NPU 0,8 TOPS, RAM 2, 4, 8 GB. |
| 87 | [RobôFrango](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/) | 200 | 200 | Teks penuh: 0,04 dan 0,07 m/s. |
| 88 | [DFRobot SEN0469](https://www.dfrobot.com/product-2513.html) | 200 | 200 | Teks laman: NH3 Sensor Calibrated, prinsip elektrokimia. |
| 89 | [Data BMKG](https://data.bmkg.go.id/) | 200 | 200 | Laman aktif. |
| 90 | [Open-Meteo](https://open-meteo.com/) | 200 | 200 | Laman aktif; API ECMWF diuji berfungsi. |
| 91 | [aremyhens.fit](https://aremyhens.fit/) | 200 | 200 | Teks dasbor: Barn health 0/100 dan tiga tombol tindakan. |
| 92 | [PMC12414267](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/) | 200 | 200 | Abstrak Europe PMC: pembersihan dan disinfeksi kandang. |
| 93 | [PMC11416347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/) | 200 | 200 | Teks penuh: disinfektan berdaya rendah hampir tidak efektif. |
| 94 | [Brosur ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf) | 200 | 200 | Teks brosur: rel 0,5 m, 24/7, tanpa harga. |
| 95 | [laman Medion](https://www.medion.co.id/info-medion/closed-house-solusi-peningkatan-performa-ayam/) | 200 | 200 | Teks laman: 13 sampai 15 dan 25 sampai 30 kg per m2. |
| 96 | [Akar API BMKG](https://api.bmkg.go.id/) | 404, mati | 404, mati | Akar API tanpa laman; dicatat sebagai temuan. |
| 97 | [Notebook Kaggle ajheshbasnet](https://www.kaggle.com/code/ajheshbasnet/chiken-disease-detection) | 404, mati | 404, mati | Tautan lama TA, mati; dicatat sebagai temuan. |
| 98 | [ISO 8373:2021](https://www.iso.org/standard/75539.html) | 403, penolakan bot | 403, penolakan bot | Penolakan bot; isi tidak dapat dicek otomatis. |
| 99 | [Repositori UMM 85141](https://eprints.umm.ac.id/id/eprint/85141) | 403, penolakan bot | 403, penolakan bot | Penolakan bot; isi tidak dapat dicek otomatis. |
| 100 | [Raspberry Pi Software](https://www.raspberrypi.com/software/) | 403, penolakan bot | 200 | Penolakan bot pada laman perangkat lunak resmi. |
| 101 | [Raspberry Pi Configuration](https://www.raspberrypi.com/documentation/computers/configuration.html) | 200 | 200 | Penolakan bot pada laman dokumentasi resmi. |
| 102 | [Driver Silabs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) | 403, penolakan bot | 403, penolakan bot | Penolakan bot pada laman driver resmi. |
| 103 | [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) | 403, penolakan bot | 403, penolakan bot | Penolakan bot pada laman perangkat lunak resmi. |
| 104 | [Olechowski dkk. 2020](https://doi.org/10.1002/sys.21533) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul TRL cocok. |
| 105 | [Rowe dkk. 2019](https://doi.org/10.3390/ani9090614) | 403, registri DOI cocok | 403, registri DOI cocok | Crossref: judul tinjauan PLF unggas cocok. |
| 106 | [Shi dkk. 2016](https://doi.org/10.1109/JIOT.2016.2579198) | 202, registri DOI cocok | 202, registri DOI cocok | Crossref: judul Edge Computing cocok. |
| 107 | [zebular13](https://github.com/zebular13/ChickenLanguageDataset) | 200 | 200 | API GitHub: deskripsi penerjemahan bahasa ayam. |

### 12.3 Audit Tautan Lama di Dokumen BROVER dan TA

Pemindaian otomatis menemukan 167 URL unik pada `PROJECT_CONCEPT_BROVER.md`, tiga panduan IoT, `Proposal TA/Dataset/01` sampai `04`, dan blueprint TA. Hasil uji akses: 151 URL berkode 200, 2 URL berkode 202 dari IEEE, 12 URL berkode 403 karena penolakan bot, dan 2 URL berkode 404.

**A. Tautan mati atau tidak dapat diakses otomatis**

| Lokasi | Tautan Lama | Status | Temuan | Tindakan |
| :--- | :--- | :-: | :--- | :--- |
| Referensi 47 BROVER | [Akar API BMKG](https://api.bmkg.go.id/) | 404 | Akar API tidak memiliki laman. Endpoint resmi adm4 dan [laman data BMKG](https://data.bmkg.go.id/) berfungsi. | Ganti tautan. |
| `Proposal TA/Dataset/03` | [Notebook Kaggle ajheshbasnet](https://www.kaggle.com/code/ajheshbasnet/chiken-disease-detection) | 404 | Tautan mati. | Hapus. |
| Referensi 21 BROVER | [ISO 8373:2021](https://www.iso.org/standard/75539.html) | 403 | Laman menolak akses otomatis. Nomor klausul 4.16 untuk *mobile platform* tidak dapat diverifikasi dari sumber terbuka. | Hapus nomor klausul atau cek dari dokumen standar resmi. |
| `Proposal TA/Dataset/03` | [Repositori UMM 85141](https://eprints.umm.ac.id/id/eprint/85141) | 403 | Klaim Syafaah dkk. 2024 tidak dapat dicek. | Cek manual lewat peramban. |
| Panduan IoT Tahap 1 sampai 3 | [Raspberry Pi Software](https://www.raspberrypi.com/software/), [Raspberry Pi Configuration](https://www.raspberrypi.com/documentation/computers/configuration.html), [Driver Silabs](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers), [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/) | 403 atau 200 | Laman perangkat lunak resmi menolak bot secara tidak konsisten antarpengujian. Bukan tautan mati. | Tidak perlu diubah. |
| Referensi BROVER, enam DOI penerbit Wiley, MDPI, PeerJ, dan Researchers Links | Misalnya [Olechowski dkk. 2020](https://doi.org/10.1002/sys.21533) dan [Rowe dkk. 2019](https://doi.org/10.3390/ani9090614) | 403 | Semua DOI ada di Crossref dengan judul yang cocok. | Tidak perlu diubah. |
| Referensi 19 dan 20 BROVER | [Baltrušaitis dkk. 2019](https://doi.org/10.1109/TPAMI.2018.2798607) dan [Shi dkk. 2016](https://doi.org/10.1109/JIOT.2016.2579198) | 202 | IEEE menunda respons bot. DOI dan judul cocok di Crossref. | Tidak perlu diubah. |

**B. Tautan aktif tetapi isi tidak cocok dengan kutipan**

| Lokasi | Sumber | Kutipan di Dokumen | Isi Sebenarnya | Status |
| :--- | :--- | :--- | :--- | :-: |
| Bab 11A baris 1 dan panduan IoT | [Zenodo 5801834](https://zenodo.org/records/5801834) | Berisi anotasi YOLO dan menjadi data utama Model #1 | Hanya arsip klasifikasi PCR, ayam petelur, persilangan, dan lokal | **Keliru** |
| Bab 4.1 Fitur 3 dan Bab 11A baris 5 | [ChickenVerse](https://github.com/amirivojdan/ChickenVerse) | Melatih postur abnormal | 15 perilaku normal, tanpa kelas sakit | **Keliru** |
| Bab 7.1 dan 11C | [Ultralytics Raspberry Pi](https://docs.ultralytics.com/guides/raspberry-pi/) | YOLOv8n NCNN sekitar 2,3 FPS di Raspberry Pi 4 | Kini hanya tolok ukur Raspberry Pi 5 dan YOLO26 | **Tidak dapat diverifikasi** |
| Bab 6.2 | [AviSense PMC13696172](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/) | Beroperasi hingga sekitar 0,09 m/s | Sekitar 0,05 m/s | **Keliru** |
| Bab 6.2 | [Parajuli dkk. 2020](https://doi.org/10.13031/trans.13644) | Kecepatan 0,1 m/s aman di bawah ambang stres | Hanya menguji 0,2, 0,4, dan 0,6 m/s | **Parsial, ekstrapolasi** |
| Bab 2 dan 4.4 | [FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) | Bobot sekitar 80 kg | Bobot tidak tercantum. Hari ke-5 sampai sekitar 23 dan kecepatan 0,04 sampai 0,12 m/s cocok | **Parsial** |
| Bab 4.4 | [Brosur ChickenBoy](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf) | Harga di atas Rp100 juta dan memantau suara | Harga tidak tercantum. Yang ada sensor tingkat kebisingan | **Parsial** |
| Bab 4.1 Panel 2 | [aremyhens.fit](https://aremyhens.fit/) | Rujukan UX triase tanpa skor 0 sampai 100 | Dasbornya sendiri menampilkan Barn health 0/100. Tiga tombol memang ada | **Parsial** |
| Bab 11A baris 10 | [IceKhoffi](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) | Pengayaan Model #2 dan #3 | Audio salinan Bowen, visi satu kelas ayam petelur | **Keliru** |
| Bab 11B baris 15 | [zebular13](https://github.com/zebular13/ChickenLanguageDataset) | Prapemrosesan suara bising dan vokalisasi untuk penyakit | Data untuk penerjemahan bahasa ayam ke manusia | **Keliru peran** |
| Bab 11A baris 8 | [SmartEars DOI](https://doi.org/10.17632/dy6gtvt4mk.2) | Kelas None adalah bising kipas, hujan, dan aktivitas | Kelas None berarti tidak ada suara ayam | **Parsial** |
| Bab 3.1 butir 4 | [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/) | Kasus lapangan untuk masalah broiler | Peternakan ayam petelur | **Parsial** |
| `Proposal TA/Dataset/03` | [Machuve dkk. 2022](https://doi.org/10.3389/frai.2022.733345) | MobileNetV2 akurasi tertinggi | Xception tertinggi | **Keliru** |
| `Proposal TA/Dataset/02` | [Data in Brief 109517](https://doi.org/10.1016/j.dib.2023.109517) | Adebayo dkk. 2023 | Aworinde dkk. 2023 | **Keliru** |

### 12.4 Ringkasan Hasil Dua Kali Pengecekan

- **Jumlah tautan unik di laporan:** 107.
- **Uji pertama:** kode 200 sebanyak 88, kode 202 sebanyak 2, kode 403 sebanyak 15, kode 404 sebanyak 2.
- **Uji ulang kedua:** kode 200 sebanyak 90, kode 202 sebanyak 2, kode 403 sebanyak 13, kode 404 sebanyak 2.
- **Tautan yang kodenya berubah antarpengujian, merujuk nomor di tabel 12.2:** nomor 65 dari kode 403 ke 200; nomor 100 dari kode 403 ke 200. Perubahan ini berasal dari pembatasan bot yang tidak konsisten, bukan perubahan isi.
- **Tautan mati yang sengaja dicantumkan sebagai temuan:** akar API BMKG dan notebook Kaggle ajheshbasnet.
- **Penolakan bot:** semua tautan DOI berkode 403 atau 202 sudah dicocokkan judulnya di registri Crossref. Laman non-DOI berkode 403 dicatat apa adanya dan tidak dipakai sebagai satu-satunya bukti klaim.
