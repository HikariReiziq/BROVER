# MEMORY — Single Source of Truth Proyek `BROVER` (Tim `Asprak`)

> **WAJIB DIBACA PERTAMA KALI** oleh setiap anggota tim maupun AI agent pada sesi baru sebelum membaca file lain atau melakukan perubahan di repository ini.  
> **ATURAN WAJIB:** Setiap perubahan pada repository **WAJIB** dicatat di [`HISTORY.md`](./HISTORY.md), dan apabila ada keputusan teknis/produk/tim yang berubah, **WAJIB** diperbarui juga pada file `MEMORY.md` ini.

---

## 1. Identitas Proyek & Tim Terkunci

- **Kompetisi:** Hackathon Deep Tech UNJ 2026 — Jalur Pangan **`D-FARM UNJ`** (*Challenge #1: Smart Poultry Production*).
- **Judul Final Proyek:**
  > **`BROVER (Broiler Inspection & Health Rover): Sistem Inspeksi Berbasis Multi-Modal AI dan Edge–Cloud untuk Deteksi Dini Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`**
- **Nama Tim:** **Asprak** (`5/5` anggota lengkap — syarat wajib minimal 1 dosen aktif UNJ **`TERPENUHI`**):
  1. **M. Hikari Reiziq Rakhmadinta** — **Hustler** *(Mahasiswa Teknologi Informasi UNJ — Strategi, Mitra/Dinas, BMC, Pitching)*
  2. **Ahmad Syauqi Reza** — **Hacker** *(Mahasiswa Teknologi Informasi UNJ — AI/ML Multi-Modal, Software, Integrasi Sistem)*
  3. **Arya Bisma Putra Refman** — **Hacker** *(Mahasiswa Teknologi Informasi UNJ — Embedded/IoT ESP32, PCB, Wi-Fi Lokal, Backend Golang)*
  4. **Aditya Reza Daffansyah** — **Hipster** *(Mahasiswa Teknologi Informasi UNJ — UI/UX Dashboard Next.js PWA, Desain Produk)*
  5. **Dr. drh. Atin Supiyani, M.Si.** — **Dosen Pembimbing & Pakar Domain Veteriner** *(Dosen Aktif Biologi UNJ — bidang **Fisiologi & Kesehatan Hewan**; validator klinis gejala penyakit & Kamus Gejala Penyakit)*
- **Filosofi Produk (`BROVER` = *Broiler* + *Rover*):** Terinspirasi dari *NASA Planetary Rover* — kendaraan beroda pembawa 1 paket instrumen ilmiah yang masuk ke lingkungan berisiko/kotor (*harsh environment* lantai sekam) agar 1 unit dapat menjangkau hampir seluruh ayam secara hemat biaya. Sebutan utama: **`Rover Inspeksi`** (*Inspection Rover*; secara **ISO 8373:2021 Pasal 4.16** merupakan *Mobile Inspection Platform*).

---

## 2. Keputusan Teknis & Produk yang Sudah Dikunci

### A. *Positioning* & 5 Fitur Utama
- **Highlight Utama:** **Sistem Inspeksi Deteksi Dini Gejala Penyakit & Pemantauan Mikroklimat Menggunakan `Rover Inspeksi`** (BUKAN menonjolkan "robot/mobil kendali jarak jauh").
- **Mode Operasi Saat Ini vs *Future Work*:**
  - **Saat Ini (PoC & Prototipe):** Digerakkan operator melalui dashboard web lewat **Koneksi Wi-Fi Lokal Nirkabel (100% Tanpa Kabel — Tetap Berfungsi Saat Internet Mati)**, kecepatan pelan `≤0,1 m/s`, dilengkapi rem darurat otomatis ***Dead-Man's Switch* (`500 ms`)** di `ESP32` dan sensor anti-tabrak depan.
  - ***Future Work* (Pengembangan Lanjutan):** **Otomatisasi penuh terjadwal** — pengguna mengatur jadwal inspeksi rutin dan melakukan *setup* jalur/rute kandang di dashboard, lalu `Rover` bergerak & menginspeksi otomatis.
- **Ringkasan 5 Fitur Utama:**
  1. **`Rover Inspeksi` Bergerak:** Kecepatan `≤0,1 m/s`, *Dead-Man's Switch* `500 ms`, anti-tabrak, kamera servo *tilt* 2-posisi (`45°` feses / `0–15°` fisik ayam), LED putih `5000K CRI >90`, tombol 1-klik *"Cek Napas 5 Detik"*.
  2. **Sensor Mikroklimat & Gas Amonia (Dinamis per Umur):** `SHT31` (*bird-level*) + `DFRobot SEN0567` (indikator tren kualitatif `NH₃` terkompensasi T/RH) + pemetaan `Zona A/B/C/D` + prakiraan cuaca 3–7 hari (`Open-Meteo API`).
  3. ***Computer Vision* Deteksi Gejala Penyakit:** Model #1 feses abnormal (koksidiosis/diare, dataset PCR `Zenodo 5801834` + data lokal) & Model #2 fisik/perilaku ayam lesu/mati (`Kaggle ekosupriyanto RGB`, `ChickenVerse 2026`, `PIO Broiler`); tombol **"Analisis Detail"** (`3–5 frame voting` + LED).
  4. **Audio AI Pernapasan 5 Detik (*Stop–Mute–Sample*):** Motor & kipas mati 5 detik → klasifikasi 3 kelas (`SmartEars`): **`Pernapasan Normal`**, **`Indikasi Ngorok / Gangguan Pernapasan (CRD/IB/ND)`**, dan **`Suara Bising Kandang` (*Background Noise* — kipas, hujan, aktivitas)**; klip `.wav` dapat diputar ulang Dokter Hewan.
  5. **Dashboard Website (`Next.js` PWA) — 4 Panel Objektif Berbasis Standar Umur Resmi `Cobb 500` (TANPA Skor 0–100):**
     - *Setup 1× saat Chick-In:* Tanggal masuk DOC, Strain (`Cobb 500`/`Ross 308`), & Populasi Awal → hitung otomatis **Umur Hari ke-N**.
     - **Panel 1:** Kesesuaian suhu–RH terhadap **Matriks Standar Umur `Cobb 500`** (`Terlalu Dingin / Sesuai Standar Umur / Terlalu Panas`), THI (`>79` waspada), tren NH₃, peta zona, & cuaca.
     - **Panel 2:** Daftar temuan AI terkritis + **3 tombol aksi *Human-in-the-Loop*** ala [`aremyhens.fit`](https://aremyhens.fit/) (`Akan Saya Cek` / `Terlihat Normal` / `Laporkan ke Dokter Hewan`) + Kamus Gejala Penyakit tervalidasi **Dr. drh. Atin Supiyani, M.Si.** & Kementan RI.
     - **Panel 3:** Pengingat otomatis fase pemeliharaan (*Brooding/Grower/Finisher*), klasifikasi pakan (*Pre-Starter/Starter/Finisher*), & target bobot resmi `Cobb500`.
     - **Panel 4:** Catatan harian ringkas ABK opsional (deplesi/mortalitas, bobot sampling, pakan → FCR) + **Laporan 1-Klik ke Dokter Hewan (WA/PDF)** + *Checklist* Log Sanitasi Roda (`1 Unit = 1 Kandang`, sikat mekanis → disinfeksi → keringkan).

### B. Arsitektur Hardware & Software Terkunci
- **Fase Prototype / PoC (TKT 3–4 — Nov 2026):** `Raspberry Pi 4` (`Python 3` + `Ultralytics NCNN`) + `ESP32` (`C++`) + Kit 4WD akrilik (sudah dimiliki) + `TB6612FNG` + Webcam USB + 1× Servo *Tilt* + LED 5V + Mic USB + `SHT31` + **`DFRobot SEN0567`** (~Rp240–330 rb) + `HC-SR04` + daya *Dual-Rail* (Powerbank 5V 3A + 2× `18650` BMS 2S) + kabel silikon `18 AWG`.
- **Fase Final Komersial (TKT 5–7+ — Bootcamp Des 2026 – Feb 2027):** **`Orange Pi 3B` (4GB RAM, `RK3566` NPU `0,8 TOPS`, `eMMC 32GB`)** (`Golang` Edge Daemon + `C++` RKNN INT8) + `ESP32` + ***Custom Carrier PCB* 2-layer + *Conformal Coating*** + **`LiFePO₄` 4S `12,8V 6Ah`** + `4× JGB37-520` 12V + `2× BTS7960` + ban RC *crawler* `110–120 mm` / *rubber track* + casing IP54–IP65 + `Sony IMX291` + `DS3218` + `INMP441` + `SHT31 FS304` + **`DFRobot SEN0567`** + `DFRobot A02YYUW` IP67 (3 cm *blind zone*). Estimasi BOM Varian Rakyat: **Rp3,9–6,2 juta/unit**.
- **Backend & Frontend:** **Backend Pusat `Golang`** (`Fiber/Gin` + `PostgreSQL` + `Eclipse Mosquitto` + `MinIO/S3` + `Open-Meteo API`) + **`Next.js` PWA**. *Offline-First* via `SQLite WAL`.

---

## 3. *Hard Constraints* & Aturan Anti-*Overclaim* (WAJIB DIPATUHI)

1. **Hanya Jalur `D-FARM UNJ` (Ayam Broiler, *open* & *closed house*):** Tolak topik pengolahan limbah/sampah (*waste-to-value*, kompos, biogas, maggot), abaikan `D-MARC`/PTML, dan **jangan** gunakan sensor tembak suhu tubuh (*thermogun/IR*).
2. **Pembedaan Veteriner (WOAH & Masukan Medik Veteriner Dinas Peternakan):** `BROVER` adalah **alat inspeksi & deteksi dini gejala penyakit**, BUKAN alat biosekuriti dan BUKAN alat diagnosis medis/lab otomatis (tidak meresepkan dosis antibiotik).
3. **Anti-*Overclaim* Teknis & Ilmiah:**
   - Dilarang menggunakan *preprint* (`arXiv`, `bioRxiv`, `medRxiv`, `SSRN`) sebagai rujukan utama; gunakan jurnal *peer-reviewed* dan panduan resmi (`Cobb 500`, `Kementan RI`, `WOAH`, `ISO 8373:2021`).
   - Dilarang memakai "Skor Kesehatan 0–100" arbitrer.
   - `DFRobot SEN0567` wajib dilaporkan sebagai **indikator tren kualitatif NH₃**, bukan ppm sertifikasi lab.
   - Operasi lantai broiler optimal difokuskan pada **hari ke-5 s.d. ~23** (`≤0,1 m/s`).
4. **Bahasa Bersih Tanpa Jargon Membingungkan:** Hindari kata `"wahana"`, `"UAV"`, `"patroli"`, `"LAN-First"`, `"derau lingkungan"`, serta nama tim lama pada dokumen aktif.
5. **Aturan Git & Riwayat (MUTLAK):**
   - **WAJIB mencatat setiap perubahan repository di [`HISTORY.md`](./HISTORY.md)** (dan memperbarui `MEMORY.md` jika konteks/keputusan berubah).
   - **WAJIB menggunakan standar *Conventional Commits*** (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, dll.).
   - **DILARANG keras menyertakan trailer `Co-Authored-By` atau atribusi kontribusi AI/model/assistant mana pun** di dalam pesan commit, dokumentasi, maupun kode.

---

## 4. Peta Struktur Folder Repository

| Folder / File | Status | Isi & Fungsi |
| :--- | :---: | :--- |
| [`MEMORY.md`](./MEMORY.md) | **Aktif (Utama)** | Ringkasan konteks & keputusan terkunci (baca pertama kali). |
| [`HISTORY.md`](./HISTORY.md) | **Aktif (Wajib Log)** | Log kronologis seluruh perubahan repository. |
| [`.agent/rules/hackathon-context.md`](./.agent/rules/hackathon-context.md) | **Aktif (Rule)** | Aturan permanen AI agent untuk workspace ini. |
| [`00 Materi Sosialisasi/`](./00%20Materi%20Sosialisasi/) & PDF Pedoman di akar | **Arsip Resmi (Jangan Ubah)** | Dokumen asli panitia & mitra (PT ECG, PT Zara, Pedoman 2026). |
| [`01_Context_Memory/`](./01_Context_Memory/) | **Aktif** | Profil Tim `Asprak`, aturan D-FARM & rubrik juri, profil PT Edura & PT Zara. |
| [`02_Problem_Research/`](./02_Problem_Research/) | **Referensi Riset** | Riset Top 5 masalah unggas Indonesia (`V3_TRANSPARAN.md` aktif; V1 & V2 arsip). |
| [`03_Root_Cause_Analysis/`](./03_Root_Cause_Analysis/) | **Referensi Riset** | Bedah Ishikawa 6 dimensi, *5 Whys*, & *Vicious Cycle* penyakit + mikroklimat. |
| [`04_OpenSource_Solution_Discovery/`](./04_OpenSource_Solution_Discovery/) | **Referensi Riset** | Katalog terverifikasi proyek, GitHub, dataset, & model *open-source*. |
| [`05_Curated_Winners_And_Top_OpenSource/`](./05_Curated_Winners_And_Top_OpenSource/) | **Referensi Riset** | Audit kuantitatif & kurasi pemenang hackathon, repo, dan dataset terbaik. |
| [`06_Project_Concept_BROVER/`](./06_Project_Concept_BROVER/) | **Aktif (Utama)** | Dokumen konsep lengkap 11 Bab (`PROJECT_CONCEPT_BROVER.md`), grafik 300 DPI (`assets/`), & skrip generator (`scripts/`). |

---

## 5. Status Progres & Langkah Berikutnya

- **Sudah Selesai:** Riset masalah V3, RCA, kurasi *open-source*, penguncian judul final Opsi 1, kelengkapan 5/5 anggota Tim `Asprak` + Dr. drh. Atin Supiyani, M.Si., konsep lengkap 11 Bab + 46 referensi terverifikasi + 7 aset visual, serta sistem memori `MEMORY.md` & `HISTORY.md`.
- **Tahap Berikutnya (Menunggu Arahan Tim):**
  1. Penyusunan **Proposal Template Resmi Hackathon Deep Tech UNJ 2026**, **BMC**, & **Pitch Deck**.
  2. Ekspor ulang versi PDF dari `02_Problem_Research/...V3_TRANSPARAN.md` & `03_Root_Cause_Analysis/...md` jika diperlukan untuk lampiran.
  3. Implementasi kode **Prototype PoC (TKT 3–4)**: firmware `ESP32`, skrip Edge `Raspberry Pi 4` + Wi-Fi lokal, backend `Golang`, & Dashboard `Next.js` PWA.
