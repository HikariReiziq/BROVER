---
trigger: always_on
---

# HACKATHON DEEP TECH UNJ 2026 — MASTER CONTEXT (TIM ASPRAK)

## 1. Identitas & Fokus Aktif
- **Tim:** **Asprak** — **5/5 anggota lengkap** (kolaborasi 4 mahasiswa Teknologi Informasi **ITS** + 1 Dosen Aktif **UNJ**):
  1. **M. Hikari Reiziq Rakhmadinta** — **Ketua Tim**, **Hustler** *(Mahasiswa Teknologi Informasi ITS)*
  2. **Ahmad Syauqi Reza** — **Hacker** *(Mahasiswa Teknologi Informasi ITS)*
  3. **Arya Bisma Putra Refman** — **Hacker** *(Mahasiswa Teknologi Informasi ITS)*
  4. **Aditya Reza Daffansyah** — **Hipster** *(Mahasiswa Teknologi Informasi ITS)*
  5. **Dr. drh. Atin Supiyani, M.Si.** — **Anggota Tim — Pakar Domain Veteriner** *(Dosen Biologi UNJ — bidang Fisiologi & Kesehatan Hewan)*
- **Status Slot Ke-5 (TERPENUHI):** Syarat legal-administratif **minimal 1 dosen aktif UNJ** (`[Pedoman, Hal. 3]`) sekaligus kapasitas **5 anggota** pada tahap pelaksanaan/bootcamp telah terpenuhi. Pastikan seluruh 5 anggota memiliki akun aktif di portal resmi hackathon.
- **Fokus Lomba:** **Hackathon Deep Tech UNJ 2026 — Jalur Pangan (`D-FARM UNJ`)**, *Focus Challenge* **Smart Poultry Production** (Pedoman hal. 2; portal menulis *Smart Egg Production*).
- **Judul Final Proyek Terkunci:** **`BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`** *(kepanjangan merek `BROVER` = Broiler Inspection & Health Rover, sengaja tidak dicantumkan di judul; filosofi `BROVER` = Broiler + Rover terinspirasi NASA Rover; sebutan utama `Rover Inspeksi`; fokus skrining gejala penyakit & mikroklimat, bukan klaim alat biosekuriti; kata deteksi dini, multi-modal, dan prediksi tidak dipakai).*
- **Empat Fitur Terkunci (28 Nov 2026):** F1 `Rover Inspeksi` dengan kamera `IMX291` pada servo dua posisi; F2 `SHT31` + `SEN0567` di tiang setinggi ayam plus mode stasiun di dok; F3 CV feses sebagai **satu-satunya AI** (detektor Apache-2.0, RKNN INT8 di `Orange Pi 3B`, ONNX di server untuk BROVER Saku); F4 dasbor PWA tanpa skor 0–100. Audio, Model #2 fisik ayam, deteksi bangkai, *node* tetap, dan CO₂ sudah dihapus dari lingkup.
- **Dua Paket:** **BROVER Saku** Rp75 ribu/siklus (foto HP) dan **BROVER Kandang** Rp750 ribu/siklus per kandang (minimal 6 siklus), plus usulan beli putus Rp11,5 juta/unit yang masih menunggu konfirmasi. Bisnis disajikan sebagai titik impas, bukan ROI.
- **Prinsip Lomba:** *Demand-Driven Innovation* berbasis *problem statement* nyata mitra menuju *working prototype* & hilirisasi (bukan lomba esai / *policy brief*).

## 2. Hard Constraints (WAJIB DIPATUHI DI SETIAP CHAT)
1. **Hanya Jalur Pangan (`D-FARM UNJ`):** Abaikan sepenuhnya jalur kesehatan/alkes/farmasi (**D-MARC UNJ**) dan dokumen **PTML**.
2. **Tolak Topik Limbah/Sampah:** Tim **TIDAK tertarik** pada topik pengolahan limbah/sampah (*Circular Production / Waste-to-Value*, kompos, biogas, maggot, pakan dari limbah, *Food Waste Reduction* berbasis pengolahan limbah, maupun edukasi iuran sampah). Jangan pernah mengusulkan ide di ranah ini.
3. **Anti-*Overclaim* & Transparansi Operasional:**
   - Sorotan utama proyek adalah **Sistem Inspeksi dan Skrining Gejala Penyakit & Pemantauan Mikroklimat Menggunakan `Rover Inspeksi`** (bukan menonjolkan "mobil/robot remote control").
   - Jujur bahwa tahap saat ini disetir operator lewat **Wi-Fi lokal nirkabel (100% tanpa kabel)**, sedangkan **CV navigasi dan penjadwalan otomatis** adalah ***Future Work***.
   - Menurut WOAH, `BROVER` **bukan alat biosekuriti dan bukan alat diagnosis otomatis**, serta tidak meresepkan antibiotik. Kata *lebih cepat* atau *dini* baru dipakai setelah selisih waktu terukur saat pilot.
   - Pengadaan komponen **100% dari e-commerce dan distributor lokal Indonesia**.
   - Langganan BROVER Kandang berlaku **per kandang** dengan protokol pemindahan unit; **sewa antarfarm jangka pendek dilarang**.
   - Gunakan **Standar Umur Resmi (`Cobb 500` & `Ross 308`)** & jurnal *peer-reviewed* (bukan skor kesehatan 0–100 arbitrer; bukan *preprint* arXiv/bioRxiv/SSRN); sensor `DFRobot SEN0567` dilaporkan sebagai **indikator tren kualitatif NH₃**; tidak menggunakan sensor tembak suhu tubuh inframerah (*thermogun/IR*).
4. **Anti-Halusinasi & Berbasis Fakta:** Jangan mengarang angka, kutipan, syarat, atau klaim teknis. Rujuk selalu fakta terverifikasi beserta sumbernya; bedakan tegas antara data slide resmi dan data transkrip/portal.
5. **Realistis untuk Tim Multidisiplin (4 TI ITS + 1 Dokter Hewan UNJ):** Diskusi teknis harus selaras dengan kapabilitas inti tim (*software engineering*, AI/ML *Computer Vision* untuk CV feses, data/analytics, IoT/embedded) serta validasi klinis **Dr. drh. Atin Supiyani, M.Si.**
6. **Gaya Komunikasi:** Bahasa Indonesia profesional, lugas, bebas jargon membingungkan (hindari `"wahana"`, `"UAV"`, `"patroli"`, `"LAN-First"`, `"derau lingkungan"`), terstruktur (tabel/bullet/bold), tanpa basa-basi.
7. **Protokol Wajib `MEMORY.md`, `HISTORY.md`, & Standar Git:**
   - Pada awal setiap sesi baru, **WAJIB membaca `MEMORY.md` dan `HISTORY.md`** di root repository agar langsung sinkron dengan keputusan & perubahan terkini.
   - **WAJIB mencatat setiap perubahan repository di `HISTORY.md`** (mengikuti template entri paling atas) sebelum commit, serta memperbarui `MEMORY.md` apabila terdapat perubahan keputusan teknis, arsitektur, atau status tim.
   - **Standar Commit Git:** Selalu gunakan ***Conventional Commits*** (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`) dan **DILARANG keras menyertakan trailer `Co-Authored-By` atau atribusi kontribusi AI/model/assistant mana pun** di pesan commit maupun file repository.

## 3. Aturan Routing Memori (WAJIB BACA SESUAI TOPIK)
Jangan membaca ulang file PDF mentah di workspace (termasuk `00 Materi Sosialisasi/*.pdf` atau `02 Buku Pedoman Hackathon 2026.pdf`) kecuali diminta eksplisit oleh user atau untuk verifikasi visual khusus. Gunakan basis memori terverifikasi di root & folder `01_Context_Memory/`:

| Topik Diskusi / Kebutuhan Konteks | File Wajib Dibaca |
| :--- | :--- |
| **Ringkasan Master & Kronologi Perubahan Repository (WAJIB BACA PERTAMA & WAJIB UPDATE)** | `MEMORY.md` & `HISTORY.md` |
| Profil tim `Asprak` (5/5 anggota + peran Hipster/Hacker/Hustler + Dr. drh. Atin Supiyani, M.Si.), kapabilitas, *hard constraints* | `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` |
| Aturan lomba, rekonsiliasi 3 sumber (Portal/Pedoman/Sosialisasi), ruang lingkup D-FARM, timeline, berkas, Katsinov/TKT, **rubrik penilaian juri**, HKI/NDA, fasilitas UNJ | `01_Context_Memory/02_HACKATHON_DFARM_RULES.md` |
| Mitra **PT Edura Cipta Gemilang (Edura)** — profil Badan Usaha Milik UNJ (PTNBH), peran mitra & juri, struktur/IT internal, 6 unit bisnis, model bisnis 6 langkah, daftar masalah (Slide vs Transkrip) | `01_Context_Memory/03_MITRA_PT_ECG_EDURA.md` |
| Mitra **PT Zara Propertifarm Indonesia (KANOPIS)** — masalah *closed house* impor, validasi JAPFA & 6 farm Bogor, data BPS 2025, roadmap TKT 9 (AI+IoT FCR, listrik, LPG), 6 *lessons learned*, anti *fake innovation* | `01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md` |
| Konsep final proyek **`BROVER`** (13 Bab): 4 fitur, dua paket & titik impas, BOM PoC & Final, TKT & milestone, jadwal purwarupa 3 bulan, rencana pilot, referensi Vancouver | `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` |
| Mengisi **template proposal resmi** (batas kata, sumber per bagian, berkas wajib) | Bab 13 concept & `Template Proposal Peserta Kegiatan HackAthon 2026 -.docx.md` |
| Kartu fitur F1–F4, bukti ilmiah per fitur, & tautan teruji | `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md` |
| Evaluasi proyek: baseline (jangan diubah) & evaluasi ulang setelah sinkronisasi 28 Nov 2026 | `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md` & `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md` |
| Panduan perakitan IoT 3 tahap | `07_IoT_Hardware_Guide/` |
