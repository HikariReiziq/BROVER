# 01 — PROFIL TIM ASPRAK & HARD CONSTRAINTS

> **Fungsi Dokumen:** Acuan tunggal identitas **Tim Asprak** (5/5 anggota lengkap termasuk Dosen Biologi/Dokter Hewan UNJ), peran Hipster–Hacker–Hustler, kapabilitas teknis & veteriner, checklist administratif, batasan ruang lingkup (*hard constraints*), dan preferensi interaksi AI Agent.

---

## 1. Identitas & Susunan Tim

- **Nama Tim:** **Asprak** *(nama resmi tim setelah bergabungnya anggota dosen perempuan pada slot ke-5)*.
- **Komposisi Saat Ini:** **5 orang dari kapasitas maksimal 5 orang (`5/5 slot TERPENUHI`)**.
- **Judul Final Proyek:** **`BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`**
  - Kepanjangan merek `BROVER` = *Broiler Inspection & Health Rover*, sengaja tidak dicantumkan di judul agar ringkas dan tidak bergantung pada keputusan bentuk platform.

| No | Nama Anggota | Peran dalam Tim | Latar Belakang & Keahlian Utama |
| :-: | :--- | :--- | :--- |
| 1 | **M. Hikari Reiziq Rakhmadinta** | **Ketua Tim**, **Hustler** *(Strategi, Bisnis, Mitra & Pitching)* | Mahasiswa Teknologi Informasi **ITS** — riset pengguna dan harga paket, kemitraan Dinas Pangan dan Pertanian Kota Cimahi dan peternak mitra, BMC, hilirisasi, & komunikasi produk. |
| 2 | **Ahmad Syauqi Reza** | **Hacker** *(Embedded/IoT, Edge, & Backend)* | Mahasiswa Teknologi Informasi **ITS** — pengembangan firmware *embedded/IoT*, *edge*, *backend*, & konektivitas perangkat. |
| 3 | **Arya Bisma Putra Refman** | **Hacker** *(Software, AI/ML, & Sistem)* | Mahasiswa Teknologi Informasi **ITS** — pelatihan dan kuantisasi detektor CV feses Apache-2.0, set uji lokal bersama dokter hewan, evaluasi akurasi per sumber foto, layanan inferensi BROVER Saku, & integrasi sistem. |
| 4 | **Aditya Reza Daffansyah** | **Hipster** *(UI/UX, Dashboard, & Visual Produk)* | Mahasiswa Teknologi Informasi **ITS** — desain antarmuka *dashboard* web/PWA, alur interaksi peternak/Dokter Hewan, & desain produk. |
| 5 | **Dr. drh. Atin Supiyani, M.Si.** | **Anggota Tim — Pakar Domain Veteriner** | **Dosen Aktif Biologi UNJ (Dokter Hewan)** — bidang **Fisiologi & Kesehatan Hewan**. Memenuhi syarat wajib legal-administratif `[Pedoman, Hal. 3]` sekaligus menjadi validator ilmiah gejala klinis penyakit unggas, *Disease Triage Dictionary*, & protokol kesehatan kandang. |

---

## 2. Profil Kapabilitas Multidisiplin Tim (`4 TI ITS + 1 Dokter Hewan UNJ`)

Kombinasi 4 mahasiswa Teknologi Informasi **ITS** dan 1 Doktor Dokter Hewan **UNJ** menjawab langsung **Rubrik #5 (*Kapasitas & Relevansi Tim* — bobot 10%: *hardware, software, domain expert, business*)**:
- **Software Engineering & Sistem Informasi:** Pengembangan aplikasi web/PWA (`Next.js`), *backend API* hemat sumber daya (`Golang`), integrasi protokol Wi-Fi lokal & MQTT/HTTPS.
- ***Computer Vision* Feses (satu-satunya AI):** Satu detektor berlisensi Apache-2.0 (`YOLOX`/`RT-DETR`) untuk feses abnormal, dikuantisasi `RKNN INT8` di `Orange Pi 3B` dan diekspor `ONNX` untuk server BROVER Saku; akurasi dilaporkan terpisah untuk foto rover dan foto HP. Audio AI tidak lagi masuk lingkup.
- **IoT & *Embedded Systems*:** Integrasi mikrokontroler `ESP32`, komputer *Edge* (`Raspberry Pi 4` PoC → `Orange Pi 3B` Final), servo kamera dua posisi, sensor mikroklimat (`SHT31`) dan indikator tren `NH₃` (`DFRobot SEN0567`) di tiang setinggi ayam, dok dengan mode stasiun, dan sistem keamanan *Dead-Man's Switch*.
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
- **Bukan Sensor Tembak Suhu Tubuh (*Thermogun/IR*):** Dikecualikan secara eksplisit oleh tim; pemantauan suhu berfokus pada suhu & kelembapan lingkungan (*bird-level* `SHT31`) berdasar standar umur `Cobb 500` & `Ross 308`.
- **Pengadaan Lokal:** Seluruh komponen dibeli dari e-commerce dan distributor lokal Indonesia.
- **Tidak Ada Sewa Antarfarm Jangka Pendek:** Langganan BROVER Kandang berlaku per kandang; unit hanya dipindah setelah kontrak selesai melalui protokol pemindahan unit.
- **Bukan Karya Konseptual Murni:** Luaran wajib berupa *working prototype* yang dapat dibangun dan diuji `[Pedoman, Hal. 4]`, `[Portal Web]`.

### B. Prinsip Kejujuran & Anti-*Overclaim*
- **Highlight Utama:** **Sistem Inspeksi dan Skrining Gejala Penyakit & Pemantauan Mikroklimat Menggunakan `Rover Inspeksi`** (bukan menonjolkan "mobil/robot kendali jarak jauh").
- **Mode Operasi Jujur:** Tahap saat ini disetir operator lewat dashboard web via **Wi-Fi lokal nirkabel (100% tanpa kabel)**; **CV navigasi dan penjadwalan otomatis** dicatat jelas sebagai ***Future Work***.
- **Standar Ilmiah:** Tidak menggunakan skor kesehatan 0–100 buatan sendiri; gunakan **Standar Umur `Cobb 500` & `Ross 308`** & jurnal *peer-reviewed* (**0 *preprint*** arXiv/bioRxiv/SSRN). Sensor `DFRobot SEN0567` dilaporkan jujur sebagai **indikator tren kualitatif NH₃**.
- **Pembedaan Veteriner (WOAH):** Fokus judul & produk adalah **Inspeksi & Skrining Gejala Penyakit** (menindaklanjuti masukan Medik Veteriner Ahli Muda Dinas Peternakan), bukan alat biosekuriti dan bukan alat diagnosis otomatis, serta tidak meresepkan antibiotik; SOP biosekuriti (`1 Unit = 1 Kandang`, sanitasi roda, dan protokol pemindahan unit) dijaga sebagai protokol operasional alat. Kata *dini* baru dipakai setelah selisih waktu skrining terukur saat pilot.

---

## 5. Preferensi Interaksi & Gaya Kerja AI Agent

- **To the Point & Bahasa Jelas:** Langsung ke inti persoalan tanpa basa-basi, hindari jargon membingungkan (jangan pakai `"wahana"`, `"UAV"`, `"LAN-First"`, `"derau lingkungan"`).
- **Berbasis Fakta & Sumber:** Setiap angka, aturan, dan klaim wajib merujuk sumber terverifikasi (`[Pedoman]`, `[Sosialisasi]`, `[Portal Web]`, `[PT ECG]`, `[PT Zara]`, WOAH, Cobb 500, atau jurnal *peer-reviewed*). Dilarang mengarang data.
- **Struktur Rapi:** Utamakan **tabel**, **bullet points**, dan **bold** untuk pemindaian cepat.
