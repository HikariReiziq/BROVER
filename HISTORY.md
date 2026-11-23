# HISTORY — Log Kronologis Perubahan Repository `BROVER`

> **ATURAN WAJIB KONTRIBUTOR & AI AGENT:**  
> Siapapun yang mengubah, menambah, atau menghapus file di repository ini **WAJIB** menambahkan entri baru di bagian paling atas daftar riwayat di bawah ini sebelum melakukan `git commit`.  
> - Gunakan standar **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).  
> - **Dilarang** mencantumkan atribusi AI/model/assistant (`Co-Authored-By` non-manusia) pada pesan commit maupun catatan riwayat.  
> - Apabila perubahan memengaruhi arsitektur, keputusan produk, atau struktur tim, perbarui juga [`MEMORY.md`](./MEMORY.md).

### Template Entri Baru (Salin ke Paling Atas Daftar Riwayat)
```markdown
## [YYYY-MM-DD HH:MM WIB] — <type(scope): ringkasan singkat>
- **Kontributor / Konteks:** <Nama anggota tim / sesi kerja>
- **Ringkasan Perubahan:**
  - ...
- **File Terdampak:**
  - `path/file`
- **Alasan / Keputusan Penting:** <mengapa perubahan dilakukan>
- **Verifikasi:** <hasil tes / audit / inspeksi>
```

---

## [2026-11-24 00:08 WIB] — `docs: finalize BROVER title, Team Asprak profile, Cobb 500 dashboard, and memory/history protocol`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Finalisasi konsep, perbaikan judul pasca-masukan Dinas Peternakan, dan penambahan dokumentasi memori lintas-sesi.
- **Ringkasan Perubahan:**
  - **Judul Final Terkunci (Opsi 1):** Mengubah judul proyek dari klaim biosekuriti & penyakit endemik menjadi **`BROVER (Broiler Inspection & Health Rover): Sistem Inspeksi Berbasis Multi-Modal AI dan Edge–Cloud untuk Deteksi Dini Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`**.
  - **Identitas Tim Lengkap (`5/5`):** Memperbarui nama tim menjadi **`Asprak`** dengan peran resmi **M. Hikari Reiziq Rakhmadinta (Hustler)**, **Ahmad Syauqi Reza (Hacker)**, **Arya Bisma Putra Refman (Hacker)**, **Aditya Reza Daffansyah (Hipster)**, dan anggota ke-5 **Dr. drh. Atin Supiyani, M.Si.** (Dosen Biologi UNJ — bidang Fisiologi & Kesehatan Hewan).
  - **Penajaman 5 Fitur Utama & Filosofi `Rover Inspeksi`:** Mengunci *highlight* utama pada Sistem Inspeksi Deteksi Dini Gejala Penyakit menggunakan `Rover Inspeksi` (filosofi *NASA Rover* untuk lingkungan berisiko biosekuriti; ISO 8373:2021 Pasal 4.16), pencatatan jujur kendali operator via **Wi-Fi lokal nirkabel (100% tanpa kabel)** + *Dead-Man's Switch* `500 ms` saat ini, dan **otomatisasi penuh terjadwal + *setup* jalur** pada ***Future Work***.
  - **Pembaruan Total Dashboard Website (Fitur 5):** Menghapus "Skor Kesehatan 0–100" yang rancu dan menggantinya dengan **4 Panel Indikator Objektif Berbasis Standar Umur Resmi `Cobb 500`** (Matriks Suhu–RH 2018/2021, fase pakan *Pre-Starter/Starter/Finisher*, target bobot `Cobb500` 2017/2020, 3 tombol aksi *Human-in-the-Loop* ala `aremyhens.fit`, catatan harian ABK untuk deplesi/bobot/FCR, dan Laporan 1-Klik ke Dokter Hewan).
  - **Penyederhanaan Bahasa & Tambahan Referensi:** Mengganti istilah kaku (`LAN-First` → Wi-Fi lokal nirkabel tanpa kabel; `Derau Lingkungan` → `Suara Bising Kandang`) serta melengkapi referensi terverifikasi menjadi **46 rujukan** (WOAH, Cobb 500, Ritz *et al.* 2004, Naseem & King 2018, ISO 8373:2021, Baltrušaitis *et al.* 2019, Shi *et al.* 2016, Edufarmers × PecahTelur — **0 *preprint***).
  - **Regenerasi Grafik Visual:** Memperbarui `generate_concept_visuals.py` dan meregenerasi 4 grafik 300 DPI (`03`, `04`, `05`, `06`) termasuk perbaikan jarak label `Zona B2` vs `Zona C1` pada grafik `04`.
  - **Penyeragaman Label Riset Aktif:** Memperbarui label nama tim menjadi `Tim Asprak` pada 4 dokumen riset aktif di folder `02`–`05` tanpa mengubah substansi maupun angka riset.
  - **Protokol Memori & Riwayat:** Menambahkan [`MEMORY.md`](./MEMORY.md) dan [`HISTORY.md`](./HISTORY.md) di root repository serta mengunci aturan wajib baca/tulis riwayat dan standar *Conventional Commits* pada [`.agent/rules/hackathon-context.md`](./.agent/rules/hackathon-context.md).
- **File Terdampak:**
  - `[NEW]` `MEMORY.md`
  - `[NEW]` `HISTORY.md`
  - `[MODIFY]` `.agent/rules/hackathon-context.md`
  - `[MODIFY]` `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md`
  - `[MODIFY]` `01_Context_Memory/02_HACKATHON_DFARM_RULES.md`
  - `[MODIFY]` `01_Context_Memory/03_MITRA_PT_ECG_EDURA.md`
  - `[MODIFY]` `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md`
  - `[MODIFY]` `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md`
  - `[MODIFY]` `04_OpenSource_Solution_Discovery/00_INDEX_RINGKASAN_OPENSOURCE.md`
  - `[MODIFY]` `05_Curated_Winners_And_Top_OpenSource/00_RINGKASAN_KURASI_DAN_ELIMINASI.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/04_alur_kerja_4lapis_biosekuriti.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/05_komparasi_komputasi_dan_baterai_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/06_roadmap_tkt_dan_evolusi_brover.png`
- **Alasan / Keputusan Penting:**
  - Masukan **Medik Veteriner Ahli Muda (Dinas Peternakan)** & **WOAH *Terrestrial Animal Health Code*** membedakan tegas antara *biosekuriti* (perisai pencegahan) vs *inspeksi/deteksi dini penyakit*.
  - Praktik peternakan broiler lapangan (*Edufarmers × PecahTelur* — kasus kematian 2.000/12.000 ekor akibat *Colibacillosis* & variasi suhu ideal DOC vs panen) membuktikan dashboard harus mengikuti standar umur resmi `Cobb 500`, bukan skor arbitrer 0–100.
  - Penambahan `MEMORY.md` & `HISTORY.md` memastikan kolaborasi lintas anggota tim dan lintas sesi AI agent selalu sinkron tanpa kehilangan konteks.
- **Verifikasi:**
  - Regenerasi 4 grafik 300 DPI berhasil (`exit 0`) dan lolos inspeksi visual (0 tumpang tindih, 0 teks terpotong).
  - Audit otomatis pada seluruh 10 file target lulus dengan `0` error (0 sisa nama tim lama, 0 jargon terlarang, 0 *preprint*, 16/16 tautan & gambar lokal valid).

---

## [2026-11-21 13:40 WIB] — `aeba4f7` — `Feat: Adding Project Concept` (Initial Commit)
- **Kontributor / Konteks:** `HikariReiziq` — Inisialisasi repository dan unggahan seluruh dokumen riset dasar hingga konsep awal `BROVER`.
- **Ringkasan Perubahan:**
  - Menambahkan dokumen resmi panitia & mitra (`00 Materi Sosialisasi/`, `01 Panduan Platform Hackathon UNJ.pdf`, `02 Buku Pedoman Hackathon 2026.pdf`).
  - Menambahkan basis konteks (`01_Context_Memory/`), riset masalah peternakan unggas Indonesia (`02_Problem_Research/` V1–V3), *Root Cause Analysis* (`03_Root_Cause_Analysis/`), katalog & kurasi solusi *open-source* (`04_OpenSource_Solution_Discovery/`, `05_Curated_Winners_And_Top_OpenSource/`), serta dokumen konsep awal `BROVER` (`06_Project_Concept_BROVER/`).
- **File Terdampak:** `97 files` (inisialisasi awal repository).
- **Alasan / Keputusan Penting:** Membangun fondasi riset berbasis bukti (*demand-driven innovation*) untuk Hackathon Deep Tech UNJ 2026 jalur `D-FARM UNJ`.
