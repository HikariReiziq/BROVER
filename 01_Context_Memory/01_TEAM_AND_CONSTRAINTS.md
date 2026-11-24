# 01 — PROFIL TIM ASPRAK & HARD CONSTRAINTS

> **Fungsi Dokumen:** Acuan tunggal identitas **Tim Asprak** (5/5 anggota lengkap termasuk Dosen Biologi/Dokter Hewan UNJ), peran Hipster–Hacker–Hustler, kapabilitas teknis & veteriner, checklist administratif, batasan ruang lingkup (*hard constraints*), dan preferensi interaksi AI Agent.

---

## 1. Identitas & Susunan Tim

- **Nama Tim:** **Asprak** *(nama resmi tim setelah bergabungnya anggota dosen perempuan pada slot ke-5)*.
- **Komposisi Saat Ini:** **5 orang dari kapasitas maksimal 5 orang (`5/5 slot TERPENUHI`)**.
- **Judul Final Proyek:** **`BROVER (Broiler Inspection & Health Rover): Sistem Inspeksi Berbasis Multi-Modal AI dan Edge–Cloud untuk Deteksi Dini Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`**

| No | Nama Anggota | Peran dalam Tim | Latar Belakang & Keahlian Utama |
| :-: | :--- | :--- | :--- |
| 1 | **M. Hikari Reiziq Rakhmadinta** | **Hustler** *(Strategi, Bisnis, Mitra & Pitching)* | Mahasiswa Teknologi Informasi **ITS** — riset pengguna, validasi mitra/Dinas Peternakan, BMC, hilirisasi, & komunikasi produk. |
| 2 | **Ahmad Syauqi Reza** | **Hacker** *(Embedded/IoT, Edge, & Backend)* | Mahasiswa Teknologi Informasi **ITS** — pengembangan firmware *embedded/IoT*, *edge*, *backend*, & konektivitas perangkat. |
| 3 | **Arya Bisma Putra Refman** | **Hacker** *(Software, AI/ML, & Sistem)* | Mahasiswa Teknologi Informasi **ITS** — pengembangan perangkat lunak, pelatihan model *Multi-Modal AI*, & integrasi sistem. |
| 4 | **Aditya Reza Daffansyah** | **Hipster** *(UI/UX, Dashboard, & Visual Produk)* | Mahasiswa Teknologi Informasi **ITS** — desain antarmuka *dashboard* web/PWA, alur interaksi peternak/Dokter Hewan, & desain produk. |
| 5 | **Dr. drh. Atin Supiyani, M.Si.** | **Anggota Tim — Pakar Domain Veteriner** | **Dosen Aktif Biologi UNJ (Dokter Hewan)** — bidang **Fisiologi & Kesehatan Hewan**. Memenuhi syarat wajib legal-administratif `[Pedoman, Hal. 3]` sekaligus menjadi validator ilmiah gejala klinis penyakit unggas, *Disease Triage Dictionary*, & protokol kesehatan kandang. |

---

## 2. Profil Kapabilitas Multidisiplin Tim (`4 TI ITS + 1 Dokter Hewan UNJ`)

Kombinasi 4 mahasiswa Teknologi Informasi **ITS** dan 1 Doktor Dokter Hewan **UNJ** menjawab langsung **Rubrik #5 (*Kapasitas & Relevansi Tim* — bobot 10%: *hardware, software, domain expert, business*)**:
- **Software Engineering & Sistem Informasi:** Pengembangan aplikasi web/PWA (`Next.js`), *backend API* hemat sumber daya (`Golang`), integrasi protokol Wi-Fi lokal & MQTT/HTTPS.
- **Multi-Modal AI (*Computer Vision* & *Audio AI*):** Deteksi objek citra feses abnormal & fisik ayam (`YOLOv8n/11n` → `NCNN`/`RKNN`) serta klasifikasi audio pernapasan 5 detik (`Log-Mel Spectrogram` + `MobileNetV3-Small`/`2D CNN`).
- **IoT & *Embedded Systems*:** Integrasi mikrokontroler `ESP32`, komputer *Edge* (`Raspberry Pi 4` PoC → `Orange Pi 3B` Final), sensor mikroklimat (`SHT31`), indikator tren `NH₃` (`DFRobot SEN0567`), dan sistem keamanan *Dead-Man's Switch*.
- **Domain Kesehatan Hewan & Fisiologi Unggas (`Dr. drh. Atin Supiyani, M.Si.`):** Validasi klinis gejala penyakit broiler (CRD, Colibacillosis, Coccidiosis, ND, IB, AI), kesesuaian fisiologi mikroklimat per fase umur (`Cobb 500`), verifikasi Kamus Gejala Penyakit, serta pendampingan etika & uji lapangan kandang.

---

## 3. Catatan Administratif Kritis (Status Terkini)

| No | Syarat Kritis | Status | Ketentuan Resmi & Sumber |
| :-: | :--- | :---: | :--- |
| 1 | **Slot Ke-5 Dosen Aktif UNJ** | **TERPENUHI** | Terisi oleh **Dr. drh. Atin Supiyani, M.Si.** (Dosen Biologi UNJ), memenuhi syarat 3–5 orang (min. 1 dosen aktif UNJ) sekaligus 5 anggota tahap pelaksanaan/bootcamp `[Pedoman, Hal. 3]`, `[Portal Web FAQ #5]`. |
| 2 | **Akun Portal Hackathon untuk Semua Anggota** | *Wajib Cek* | Seluruh 5 anggota (Ketua + 3 mahasiswa + Dr. drh. Atin Supiyani, M.Si.) wajib memiliki akun aktif di `ditisip.unj.ac.id/subdirektorat-inovasi/hackathon` `[Portal Web]`. |
| 3 | **Batas Pengajuan Ketua Tim** | *Wajib Patuh* | Ketua tim berstatus anggota aktif institusi terkait dan maksimal mengajukan **1 judul pada 1 program Hackathon** `[Pedoman, Hal. 3]`. |
| 4 | **Komitmen Kehadiran Finalis** | *Wajib Patuh* | Jika lolos 10 finalis D-FARM, tim wajib mengikuti *Capacity Building*, *Bootcamp*, *Mentoring*, dan *Demo Day* dengan kehadiran **minimal 80%** `[Pedoman, Hal. 3 & 6]`. |

---

## 4. Hard Constraints & Ruang Lingkup Tim

### A. Batasan Mutlak (Dilarang / Dikecualikan)
- **Hanya Jalur Pangan (`D-FARM UNJ`):** Fokus 100% pada sub-program pangan & ketahanan pangan (khususnya peternakan ayam broiler, *open* & *closed house*). Abaikan sepenuhnya jalur kesehatan manusia (**D-MARC UNJ**) dan materi **PTML**.
- **Tolak Topik Pengolahan Limbah / Sampah:** Tim **TIDAK tertarik** dan mengecualikan:
  - Challenge ke-4 D-FARM: *Circular Food Production & Waste-to-Value* (kompos, biogas, maggot, pakan dari limbah).
  - Area *Food Waste Reduction Technology* apabila merujuk pada pengolahan limbah/sampah.
  - Topik edukasi iuran pengelolaan sampah di luar slide resmi PT ECG.
- **Bukan Sensor Tembak Suhu Tubuh (*Thermogun/IR*):** Dikecualikan secara eksplisit oleh tim; pemantauan suhu berfokus pada suhu & kelembapan lingkungan (*bird-level* `SHT31`) berdasar standar umur `Cobb 500`.
- **Bukan Karya Konseptual Murni:** Luaran wajib berupa *working prototype* yang dapat dibangun dan diuji `[Pedoman, Hal. 4]`, `[Portal Web]`.

### B. Prinsip Kejujuran & Anti-*Overclaim*
- **Highlight Utama:** **Sistem Inspeksi Deteksi Dini Gejala Penyakit & Pemantauan Mikroklimat Menggunakan `Rover Inspeksi`** (bukan menonjolkan "mobil/robot kendali jarak jauh").
- **Mode Operasi Jujur:** Tahap saat ini dikendalikan operator lewat dashboard web via **Wi-Fi lokal nirkabel (100% tanpa kabel)**; **otomatisasi jadwal & *setup* jalur** dicatat jelas sebagai ***Future Work***.
- **Standar Ilmiah:** Tidak menggunakan skor kesehatan 0–100 buatan sendiri; gunakan **Standar Umur `Cobb 500`** & jurnal *peer-reviewed* (**0 *preprint*** arXiv/bioRxiv/SSRN). Sensor `DFRobot SEN0567` dilaporkan jujur sebagai **indikator tren kualitatif NH₃**.
- **Pembedaan Veteriner (WOAH):** Fokus judul & produk adalah **Inspeksi & Deteksi Dini Gejala Penyakit** (menindaklanjuti masukan Medik Veteriner Ahli Muda Dinas Peternakan), bukan klaim alat biosekuriti; SOP biosekuriti (`1 Unit = 1 Kandang` & sanitasi roda) dijaga sebagai protokol operasional alat.

---

## 5. Preferensi Interaksi & Gaya Kerja AI Agent

- **To the Point & Bahasa Jelas:** Langsung ke inti persoalan tanpa basa-basi, hindari jargon membingungkan (jangan pakai `"wahana"`, `"UAV"`, `"LAN-First"`, `"derau lingkungan"`).
- **Berbasis Fakta & Sumber:** Setiap angka, aturan, dan klaim wajib merujuk sumber terverifikasi (`[Pedoman]`, `[Sosialisasi]`, `[Portal Web]`, `[PT ECG]`, `[PT Zara]`, WOAH, Cobb 500, atau jurnal *peer-reviewed*). Dilarang mengarang data.
- **Struktur Rapi:** Utamakan **tabel**, **bullet points**, dan **bold** untuk pemindaian cepat.
