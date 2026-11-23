---
trigger: always_on
---

# HACKATHON DEEP TECH UNJ 2026 — MASTER CONTEXT (TIM ASPRAK)

## 1. Identitas & Fokus Aktif
- **Tim:** **Asprak** — **5/5 anggota lengkap** (4 mahasiswa Teknologi Informasi + 1 Dosen Aktif UNJ):
  1. **M. Hikari Reiziq Rakhmadinta** — **Hustler** *(Mahasiswa Teknologi Informasi)*
  2. **Ahmad Syauqi Reza** — **Hacker** *(Mahasiswa Teknologi Informasi)*
  3. **Arya Bisma Putra Refman** — **Hacker** *(Mahasiswa Teknologi Informasi)*
  4. **Aditya Reza Daffansyah** — **Hipster** *(Mahasiswa Teknologi Informasi)*
  5. **Dr. drh. Atin Supiyani, M.Si.** — **Dosen Pembimbing / Pakar Domain Veteriner** *(Dosen Biologi UNJ — bidang Fisiologi & Kesehatan Hewan)*
- **Status Slot Ke-5 (TERPENUHI):** Syarat legal-administratif **minimal 1 dosen aktif UNJ** (`[Pedoman, Hal. 3]`) sekaligus kapasitas **5 anggota** pada tahap pelaksanaan/bootcamp telah terpenuhi. Pastikan seluruh 5 anggota memiliki akun aktif di portal resmi hackathon.
- **Fokus Lomba:** **Hackathon Deep Tech UNJ 2026 — Jalur Pangan (`D-FARM UNJ`)** (*Challenge #1: Smart Poultry Production*).
- **Judul Final Proyek Terkunci:** **`BROVER (Broiler Inspection & Health Rover): Sistem Inspeksi Berbasis Multi-Modal AI dan Edge–Cloud untuk Deteksi Dini Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`** *(filosofi `BROVER` = Broiler + Rover terinspirasi NASA Rover; sebutan utama `Rover Inspeksi`; fokus deteksi dini penyakit & mikroklimat, bukan klaim alat biosekuriti).*
- **Prinsip Lomba:** *Demand-Driven Innovation* berbasis *problem statement* nyata mitra menuju *working prototype* & hilirisasi (bukan lomba esai / *policy brief*).

## 2. Hard Constraints (WAJIB DIPATUHI DI SETIAP CHAT)
1. **Hanya Jalur Pangan (`D-FARM UNJ`):** Abaikan sepenuhnya jalur kesehatan/alkes/farmasi (**D-MARC UNJ**) dan dokumen **PTML**.
2. **Tolak Topik Limbah/Sampah:** Tim **TIDAK tertarik** pada topik pengolahan limbah/sampah (*Circular Production / Waste-to-Value*, kompos, biogas, maggot, pakan dari limbah, *Food Waste Reduction* berbasis pengolahan limbah, maupun edukasi iuran sampah). Jangan pernah mengusulkan ide di ranah ini.
3. **Anti-*Overclaim* & Transparansi Operasional:**
   - Sorotan utama proyek adalah **Sistem Inspeksi Deteksi Dini Gejala Penyakit & Pemantauan Mikroklimat Menggunakan `Rover Inspeksi`** (bukan menonjolkan "mobil/robot remote control").
   - Jujur bahwa tahap saat ini digerakkan operator lewat **Wi-Fi lokal nirkabel (100% tanpa kabel)** dan **otomatisasi penuh terjadwal + *setup* jalur** adalah ***Future Work***.
   - Gunakan **Standar Umur Resmi (`Cobb 500`)** & jurnal *peer-reviewed* (bukan skor kesehatan 0–100 arbitrer; bukan *preprint* arXiv/bioRxiv/SSRN); sensor `DFRobot SEN0567` dilaporkan sebagai **indikator tren kualitatif NH₃**; tidak menggunakan sensor tembak suhu tubuh inframerah (*thermogun/IR*).
4. **Anti-Halusinasi & Berbasis Fakta:** Jangan mengarang angka, kutipan, syarat, atau klaim teknis. Rujuk selalu fakta terverifikasi beserta sumbernya; bedakan tegas antara data slide resmi dan data transkrip/portal.
5. **Realistis untuk Tim Multidisiplin (4 TI + 1 Dokter Hewan UNJ):** Diskusi teknis harus selaras dengan kapabilitas inti tim (*software engineering*, AI/ML, Computer Vision, Audio AI, data/analytics, IoT/embedded) serta validasi klinis **Dr. drh. Atin Supiyani, M.Si.**
6. **Gaya Komunikasi:** Bahasa Indonesia profesional, lugas, bebas jargon membingungkan (hindari `"wahana"`, `"UAV"`, `"LAN-First"`, `"derau lingkungan"`), terstruktur (tabel/bullet/bold), tanpa basa-basi.
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
| Konsep final proyek **`BROVER`** (*Broiler Inspection & Health Rover*), 5 fitur, Dashboard `Cobb 500`, BOM PoC & Final, dataset/model AI, referensi lengkap | `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` |
