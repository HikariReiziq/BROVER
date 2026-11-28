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

## [2026-11-29 00:03 WIB] — `docs(brover): sync documents with the 28 Nov 2026 locked decisions, cover the proposal template, re-render diagrams, and rebuild TOP5/RCA PDFs`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — sinkronisasi seluruh dokumen dengan keputusan final tim 28 November 2026 (4 fitur, CV feses satu-satunya AI, dua paket BROVER Saku dan BROVER Kandang, titik impas tanpa ROI) serta kelengkapan bab template proposal resmi.
- **Ringkasan Perubahan:**
  - **Concept (`PROJECT_CONCEPT_BROVER.md`):** ditulis ulang menjadi 13 bab. Tambahan: 3.3 Rumusan Masalah, 3.4 Calon Pengguna, 4.5 Komponen *Deeptech*, matriks paket, 8.3 diagram blok, 9.2 A–G (paket, titik impas, beli putus, protokol pemindahan unit), 9.5 status TKT dan milestone M0–M5, 9.6 pilot dan hilirisasi, 9.7 jadwal purwarupa 12 minggu, 9.8 target luaran, Bab 12 format Vancouver (85 entri), dan Bab 13 pemetaan ke template. Koreksi: rentang BOM, bab WOAH 6.5, tabel Ross 308, titik impas Saku 2,1–3,3 ekor.
  - **Peta fitur (`PETA_FITUR_DAN_BUKTI_BROVER.md`):** bagian yang terdampak keputusan baru diperbarui; urutan penulis Quarles dan Kling dikoreksi; tabel tautan 8.1 ditambah dan diuji dua kali.
  - **Diagram:** 03, 04a, 04b, 04c, 05, 06, 07, dan 08 dirender ulang; ditambah `08b_jadwal_purwarupa_3_bulan_brover` dan `09_titik_impas_paket_brover`. Gambar lama dan `09_proyeksi_keuntungan_5tahun_brover` diarsipkan di `06_Project_Concept_BROVER/assets/history/2026-11-28_sebelum_sinkronisasi/` beserta README.
  - **Memori & konteks:** `MEMORY.md`, `.agent/rules/hackathon-context.md`, dan `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` diselaraskan; `README.md` disinkronkan lewat `sync_readme.py`.
  - **Panduan IoT:** ketiga panduan dibersihkan dari mikrofon dan audio; ditambah servo dua posisi, tiang sensor, dok, dan mode stasiun; klaim FPS dan suhu baterai yang tidak terverifikasi diganti. Foto mikrofon diarsipkan di `07_IoT_Hardware_Guide/assets/history/`.
  - **TOP5 & RCA:** label ayam petelur pada kasus Hari Farm, catatan verifikasi Wilcox dan Anwar Sani, dan PDF dibuat ulang dengan skrip baru `08_Evaluasi_Proyek/tools/md_to_pdf.py`.
  - **Evaluasi & prompt lanjutan:** `EVALUASI_ULANG_BROVER.md` ditulis; prompt lanjutan proyek untuk sesi agent berikutnya ditambahkan; sebutan nama alat AI di dua prompt lama dinetralkan.
  - **Commit perdana folder:** `07_IoT_Hardware_Guide/` dan `08_Evaluasi_Proyek/` mulai dilacak git (tanpa PDF SmartEars dan `__pycache__`), bersama template proposal resmi panitia (`.docx` dan `.docx.md`).
- **File Terdampak:**
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`, `README.md`, `MEMORY.md`, `HISTORY.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_architecture_svg.py`, `generate_workflow_svgs.py`, `generate_business_timeline_svgs.py`, `generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_*`, `04a_*`, `04b_*`, `04c_*`, `05_*`, `06_*`, `07_*`, `08_*` (SVG/PNG)
  - `[NEW]` `06_Project_Concept_BROVER/assets/08b_jadwal_purwarupa_3_bulan_brover.svg/.png`, `09_titik_impas_paket_brover.svg/.png`
  - `[MOVE]` `06_Project_Concept_BROVER/assets/09_proyeksi_keuntungan_5tahun_brover.svg/.png` dan `04_alur_kerja_4lapis_biosekuriti.png` ke `assets/history/2026-11-28_sebelum_sinkronisasi/`
  - `[NEW]` `06_Project_Concept_BROVER/assets/history/2026-11-28_sebelum_sinkronisasi/` (salinan gambar lama + `README.md`)
  - `[MODIFY]` `.agent/rules/hackathon-context.md`, `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md`
  - `[MODIFY]` `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md`, `08_Evaluasi_Proyek/tools/notes.py`
  - `[NEW]` `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md`, `08_Evaluasi_Proyek/tools/md_to_pdf.py`, `08_Evaluasi_Proyek/PROMPT_LANJUTAN_SINKRONISASI_TAHAP6_SAMPAI_11.md`, `08_Evaluasi_Proyek/PROMPT_ANTIGRAVITY_LANJUTAN_PROYEK_BROVER.md`
  - `[NEW]` pertama kali dilacak: `07_IoT_Hardware_Guide/` (panduan, foto komponen, skrip), `08_Evaluasi_Proyek/` (evaluasi, peta fitur, prompt, `tools/`), `Template Proposal Peserta Kegiatan HackAthon 2026 -.docx` & `.docx.md`
  - `[MODIFY]` `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md` (+ `_tmp.html`, `.md.pdf`), `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md` (+ `_tmp.html`, `.md.pdf`)
  - `[MODIFY]` `07_IoT_Hardware_Guide/01_*.md`, `02_*.md`, `03_*.md`, `scripts/fetch_component_images.py`; `[MOVE]` 3 foto mikrofon ke `07_IoT_Hardware_Guide/assets/history/`
- **Alasan / Keputusan Penting:** dokumen lama masih memuat skema *Multi-Modal AI*, audio, sewa per siklus, beli sepaket Rp11,5 juta, dan ROI 498% yang sudah diganti keputusan tim 28 November 2026; concept juga harus menjadi sumber lengkap untuk mengisi template proposal, termasuk jadwal purwarupa maksimal 3 bulan.
- **Verifikasi:** setiap PNG yang dirender ulang dilihat langsung; grep teks SVG bebas istilah lama; palet grafik 08b dan 09 lolos validator buta warna; spesifikasi papan pada Gambar 05 dicek ke laman resmi; 72 rujukan gambar panduan IoT valid; PDF TOP5 memuat 37 objek gambar unik dan PDF RCA 5 gambar; `EVALUASI_ULANG_BROVER.md` lolos `check_style.py` dengan TOTAL MASALAH 0 dan 36 tautannya diuji dua kali; `sync_readme.py` melaporkan 0 tautan rusak; tidak ada commit.

---

## [2026-11-27 20:32 WIB] — `docs(hardware-guide): sync Stage 1 rover guide with actual team inventory and expand 7-phase physical assembly instructions`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penyelarasan penuh `01_PANDUAN_TAHAP1_ROVER_KONTROL_WEB.md` terhadap seluruh komponen aktual yang telah dimiliki, dipinjam dari lab, dan dibeli (`Wintonic INR 18650 2200mAh`, `BMS 2S 7,4V 8A`, `3× PCT-223`, `Kabel 22 AWG Merah`, `12× MLCC 100 nF 50V`, `Fuse 5A/2A + 3× Fuse Holder Putar 5×20 mm`), sekaligus memperluas panduan rakit fisik menjadi **Fase 0 s.d. Fase 7** super detail.
- **Ringkasan Perubahan:**
  - Memperbarui seluruh tabel inventaris Tahap 1 (`22` item aktual berstatus lengkap siap rakit; menghapus kebutuhan `XT30` karena tergantikan oleh `3× PCT-223`, holder 2-slot, dan saklar).
  - Menambahkan peta pemakaian eksak **`3× PCT-223`** (termasuk trik mengambil `GND` *breadboard* dari `Buck OUT-` agar 3 lubang `PCT-223 #2` pas tanpa kelebihan kabel), aturan penandaan *heat-shrink* hitam untuk potongan `GND` pada kabel `22 AWG` merah, catatan *wake-up* `BMS 2S 8A`, dan spesifikasi jujur baterai `Wintonic INR 18650` (`2,5 A` maks, *Flat Top*, non-protected).
  - Memperluas Bagian 6 menjadi panduan perakitan langkah demi langkah **Fase 0 (Cek Fisik Lab & Pemotongan Kabel)** → **Fase 1 (Sasis & Solder 4 Motor + MLCC)** → **Fase 2 (`TB6612FNG` & `2× Breadboard 830`)** → **Fase 3 (Rail 2 `BMS 2S 8A` + Saklar + `Fuse Holder Putar 5A` + `3× PCT-223`)** → **Fase 4 (*Physical Gate* Multimeter & Set `5,00V`)** → **Fase 5 (Kapasitor + 9 Jumper Sinyal)** → **Fase 6 (Tata Letak Sasis `25×15 cm` & Aturan Aman USB Upload)** → **Fase 7 (Kriteria Lulus)**.
- **File Terdampak:**
  - `[MODIFY]` `07_IoT_Hardware_Guide/01_PANDUAN_TAHAP1_ROVER_KONTROL_WEB.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memastikan panduan di meja kerja 100% cocok dengan fisik komponen aktual tim (nol kebingungan pin atau jumlah lubang konektor saat merakit pertama kali).
- **Verifikasi:** Audit otomatis memastikan `22/22` baris komponen & foto `.jpg` valid, `0` tabel pecah, `0` tautan lokal rusak, `0` harga rupiah, `0` blok kode program, dan `PROJECT_CONCEPT_BROVER.md` tetap utuh.

---

## [2026-11-25 15:20 WIB] — `refactor(hardware-guide): restructure IoT documentation into 3 progressive anti-overclaim guides (Web Rover -> Full Prototype with INMP441 on RPi 4B -> Final Field-Ready)`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penataan ulang panduan IoT dari 2 file menjadi **3 file bertahap** bebas harga dan tanpa blok kode program dulu, menyertakan stok eksisting **`INMP441`** & **`Raspberry Pi 4 Model B`**, serta hasil riset objektif anti-*overclaim* (`2× Breadboard 830`, `1× TB6612FNG` + 4 pagar aman, `Wago 221` jalur daya luar *breadboard*, dan `INMP441` langsung ke 40-pin I2S `RPi 4B`).
- **Ringkasan Perubahan:**
  - **File 1 (`07_IoT_Hardware_Guide/01_PANDUAN_TAHAP1_ROVER_KONTROL_WEB.md`):** Panduan khusus merakit mobil 4WD kontrol website HP (`http://192.168.4.1`, `DOIT ESP32 DEVKIT V1 30-Pin`, `2× Breadboard 830` dirapatkan, `1× TB6612FNG` + 4 aturan pengaman anti-*stall*, `Wago 221` pemisah jalur daya `18 AWG` di luar *breadboard*, 24 item berfoto `.jpg` lengkap dengan kolom `Fungsi Utama` & `Alasan Objektif`).
  - **File 2 (`07_IoT_Hardware_Guide/02_PANDUAN_TAHAP2_PROTOTYPE_LENGKAP_AI_SENSOR.md`):** Panduan lanjutan integrasi `Raspberry Pi 4 Model B`, Webcam USB, **`INMP441` (sudah dimiliki → langsung ke Header 40-Pin I2S `RPi 4B` + catatan jujur `ALSA softvol` Bookworm Kernel 6.6)**, `Servo Tilt`, `LED 5V` + MOSFET `3,3V`, `SHT31`, `SEN0567`, `HC-SR04` (divider `1 kΩ + 2 kΩ`), audit jujur bobot `≤800–1.000 g` + transisi *perfboard* sebelum demo (17 item tambahan berfoto `.jpg`).
  - **File 3 (`07_IoT_Hardware_Guide/03_PANDUAN_IOT_FINAL_FIELD_READY.md`):** Versi Final *Field-Ready* (`TKT 5–6+`) berpenomoran urut `03`, memperbarui status `INMP441` menjadi *Reuse dari Prototype*, menambahkan kolom `Alasan Objektif Dipilih`, dan menghilangkan blok kode agar konsisten tanpa codingan dulu (25 item utama berfoto `.jpg` + 10 item pasif/alat Lab UNJ).
  - **Aset & Pembersihan:** Menambahkan foto `assets/poc/39_wago_221_connector.jpg` (Wikimedia Commons, lolos inspeksi visual) & salinan `assets/poc/40_inmp441_i2s_mic.jpg`; menghapus 2 file draft lama (`01_PANDUAN_IOT_PROTOTYPE_POC.md` & `02_PANDUAN_IOT_FINAL_FIELD_READY.md`); menyinkronkan `MEMORY.md` & `HISTORY.md` (membiarkan `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` utuh).
- **File Terdampak:**
  - `[NEW]` `07_IoT_Hardware_Guide/01_PANDUAN_TAHAP1_ROVER_KONTROL_WEB.md`
  - `[NEW]` `07_IoT_Hardware_Guide/02_PANDUAN_TAHAP2_PROTOTYPE_LENGKAP_AI_SENSOR.md`
  - `[NEW]` `07_IoT_Hardware_Guide/03_PANDUAN_IOT_FINAL_FIELD_READY.md`
  - `[NEW]` `07_IoT_Hardware_Guide/assets/poc/39_wago_221_connector.jpg`
  - `[NEW]` `07_IoT_Hardware_Guide/assets/poc/40_inmp441_i2s_mic.jpg`
  - `[DELETE]` `07_IoT_Hardware_Guide/01_PANDUAN_IOT_PROTOTYPE_POC.md`
  - `[DELETE]` `07_IoT_Hardware_Guide/02_PANDUAN_IOT_FINAL_FIELD_READY.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memungkinkan tim menuntaskan kendali mobil via website HP di *breadboard* dulu sebelum mengintegrasikan multi-modal AI (`INMP441` + CV + sensor), sekaligus memastikan setiap pilihan hardware berdiri di atas alasan objektif tanpa *overclaim*.
- **Verifikasi:** Audit otomatis mengonfirmasi `76/76` baris komponen (`24` + `17` + `35`), `66/66` gambar `.jpg` valid, `0` tautan rusak, `0` tabel pecah, `0` blok kode program, `0` harga rupiah, `0` jargon terlarang, dan `PROJECT_CONCEPT_BROVER.md` tetap bersih.

---

## [2026-11-25 14:48 WIB] — `docs(hardware-guide): add dedicated to-the-point function column for every component in Prototype and Final IoT guides`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penyempurnaan keterbacaan daftar komponen pada kedua file panduan IoT (`07_IoT_Hardware_Guide/`) dengan menambahkan kolom khusus **`Fungsi Utama (*To The Point*)`** berbahasa orang awam untuk seluruh 38 item Prototype dan 25 item utama + 10 item pasif/alat Final.
- **Ringkasan Perubahan:**
  - Memisahkan penjelasan fungsi praktis (kolom 5: *"benda ini buat apa di BROVER?"*) dari spesifikasi teknis angka/nilai (kolom 6) pada seluruh 5 sub-tabel (`38/38` item) di `01_PANDUAN_IOT_PROTOTYPE_POC.md`.
  - Menambahkan kolom **`Fungsi Utama (*To The Point*)`** pada seluruh 4 sub-tabel utama (`25/25` item) serta mengubah daftar bullet **Kelompok E (10 item pasif PCB & alat Lab UNJ)** menjadi tabel terstruktur berkolom fungsi pada `02_PANDUAN_IOT_FINAL_FIELD_READY.md`.
- **File Terdampak:**
  - `[MODIFY]` `07_IoT_Hardware_Guide/01_PANDUAN_IOT_PROTOTYPE_POC.md`
  - `[MODIFY]` `07_IoT_Hardware_Guide/02_PANDUAN_IOT_FINAL_FIELD_READY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memastikan siapa pun anggota tim maupun pembaca awam langsung memahami kegunaan setiap komponen/alat dalam 3 detik sebelum mengecek spesifikasi teknis dan harga aktual di marketplace.
- **Verifikasi:** Audit struktur tabel mengonfirmasi seluruh `73` baris item (`38` PoC + `25` Final + `10` pasif/alat Final) memiliki kolom fungsi terisi penuh dengan jumlah kolom valid, `63/63` foto `.jpg` tetap valid, `0` harga rupiah, dan `0` perubahan pada `PROJECT_CONCEPT_BROVER.md`.

---

## [2026-11-25 14:35 WIB] — `feat(hardware-guide): add complete layperson IoT Prototype & Final guides with 63 verified JPG component photos and pin-to-pin wiring`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Pembuatan 2 buku panduan teknis IoT lapangan bebas harga (`07_IoT_Hardware_Guide/`) dengan rincian lengkap komponen pasif, alat kerja, software/library, panduan warna kabel pin-ke-pin untuk `DOIT ESP32 DEVKIT V1 (30-Pin)`, dan foto `.jpg` untuk setiap item.
- **Ringkasan Perubahan:**
  - **Panduan IoT Prototype PoC (`07_IoT_Hardware_Guide/01_PANDUAN_IOT_PROTOTYPE_POC.md`):** Menyusun panduan ramah pemula dengan strategi rakit 3 tahap berurutan (**Tahap 1A Mobil Jalan via Website `http://192.168.4.1` dari `ESP32` mandiri + *Dead-Man's Switch 500 ms*** → **Tahap 1B Sensor & Aktuator** → **Tahap 1C Integrasi `Raspberry Pi 4` + Kamera + Audio AI**), daftar lengkap **38 item** (termasuk komponen pasif: kabel silikon `18 AWG`, jumper DuPont, resistor `1 kΩ`/`2 kΩ`/`4,7 kΩ`/`220 Ω`/`10 kΩ`, kapasitor elektrolit `470–1000 µF` & keramik `100 nF`, *perfboard*, *pin header*, *terminal block*, `XT30`/`JST-XH`, sekring `5A`, saklar `10A`, *heat-shrink*, solder, timah `0,8 mm`, flux, multimeter, dll.) lengkap dengan **38 foto `.jpg` lokal**, software/library/plugin (`VS Code` + `PlatformIO`, `ESPAsyncWebServer`, `MediaMTX`, `MQTTX`), tabel warna kabel pin-ke-pin `DOIT ESP32 DEVKIT V1 (30-Pin)`, kode uji siap pakai Tahap 1A, troubleshooting, dan link referensi YouTube/GitHub/Hugging Face terverifikasi.
  - **Panduan IoT Final *Field-Ready* (`07_IoT_Hardware_Guide/02_PANDUAN_IOT_FINAL_FIELD_READY.md`):** Menyusun panduan upgrade siap kandang broiler (`Orange Pi 3B` + `eMMC 32GB` + Antena Wi-Fi `2,4 GHz`, *Custom Carrier PCB* `KiCad 8` + *Conformal Coating*, `4× JGB37-520`, `2× BTS7960 43A`, Ban RC `110–120 mm`, Box Panel `IP65` + 3D Print `PETG`, `IMX291`, `DS3218`, `INMP441`, `FS304-SHT31`, `SEN0567`, `A02YYUW`, `LiFePO₄ 4S 12,8V 6Ah` + Charger `14,6V`, `2× XL4015`, `INA219` + shunt `0,01 Ω`, `16 AWG`/`XT60`/`GX16`/`PG7`, *Kill Switch IP65*, & *Cleaning Dock*) lengkap dengan **25 foto `.jpg` lokal**, software (`KiCad 8`, `FreeCAD`, `rknn-toolkit2`, `Golang`), tabel warna kabel pin-ke-pin, SOP sanitasi 3 langkah, dan link referensi terverifikasi.
  - **Pengunduh & Normalisasi Foto Komponen (`07_IoT_Hardware_Guide/scripts/fetch_component_images.py`):** Membuat skrip pengunduh foto produk resmi (Adafruit, Pololu, DFRobot Wiki, Orange Pi Official, Wikimedia Commons) berformat `.jpg` seragam `480×360 px` di `assets/poc/` dan `assets/final/`.
  - **Kepatuhan Batasan:** `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` dibiarkan utuh sesuai arahan tim hingga panduan hardware tervalidasi; `MEMORY.md` dan `HISTORY.md` disinkronkan.
- **File Terdampak:**
  - `[NEW]` `07_IoT_Hardware_Guide/01_PANDUAN_IOT_PROTOTYPE_POC.md`
  - `[NEW]` `07_IoT_Hardware_Guide/02_PANDUAN_IOT_FINAL_FIELD_READY.md`
  - `[NEW]` `07_IoT_Hardware_Guide/scripts/fetch_component_images.py`
  - `[NEW]` `07_IoT_Hardware_Guide/assets/poc/*.jpg` (`38 files`)
  - `[NEW]` `07_IoT_Hardware_Guide/assets/final/*.jpg` (`25 files`)
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memudahkan tim mengecek harga komponen nyata secara manual tanpa kebingungan spesifikasi komponen kecil/pasif maupun arah kabel saat merakit Prototype bertahap dari mobil kontrol web menuju unit Final siap kandang.
- **Verifikasi:** Audit otomatis mengonfirmasi `63/63` gambar `.jpg` valid & terbuka, `0` tautan rusak, `0` nominal harga (`Rp`), `0` jargon terlarang/Alibaba, serta inspeksi visual 100% seluruh 63 gambar lewat *contact sheet* QA.

---

## [2026-11-24 19:28 WIB] — `refactor(visuals,docs): simplify 06-09 visuals for laypeople, redesign TKT roadmap with peer-reviewed basis, replace PoC rover photo, and sync README`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penyederhanaan bahasa dan tampilan seluruh visual kunci (`06`, `07`, `08`, `09`) agar bersih, bebas jargon teknis, dan ramah orang awam; penggantian foto kit rover PoC (`04d_ilustrasi_rover_4wd_poc.png`); penguatan landasan ilmiah TKT berbasis Permenristekdikti & jurnal *peer-reviewed*; serta sinkronisasi 100% `README.md` dan publikasi ke GitHub.
- **Ringkasan Perubahan:**
  - **Desain Ulang Peta Jalan TKT ke Vektor SVG (`06_roadmap_tkt_dan_evolusi_brover.svg/.png`):** Menggantikan grafik `matplotlib` lama dengan diagram tangga naik (*Ascending Staircase* `3200×1840 px`) berisi 4 jenjang (`TKT 3–4 Purwarupa Awal` → `TKT 5–6 Purwarupa Siap Kandang` → `TKT 7 Uji Kandang Mitra` → `TKT 8–9 Produk Siap Pasar`), bar progres skala `1–9`, tanpa label angka tahap, serta pita landasan ilmiah berbasis **Permenristekdikti RI No. 42 Tahun 2016**, **Mankins (2009, *Acta Astronautica* Q1)**, **Rowe *et al.* (2019, *Animals* Q1)**, dan **Olechowski *et al.* (2020, *Systems Engineering*)** (ditambahkan ke Bab 9.5 & Bab 12 Referensi `50–53`).
  - **Penyederhanaan *Project Timeline* (`08_project_timeline_brover.svg/.png`):** Menghapus *pill badge*, subjudul, rentang bulan/tahun pada judul (`Jadwal Pelaksanaan Proyek BROVER`), angka tahap pada header fase (`SELEKSI`, `BOOTCAMP & PROTOTYPING`, `DEMO DAY`, `MATCHING`, `PILOT TESTING & HILIRISASI`), subteks kecil di bawah kegiatan, jargon teknis (`>80%`, `Golang`, `IP54+`, `4 modul`, `3 Pilar`, `Katsinov`, `Koleksi Data`), ikon wajik *Milestone Kunci*, dan angka tahun pada legenda; menambahkan pita tipis `2026 | 2027` di atas nama bulan bersih (`Nov`–`Agu`) dan kolom minggu `1–4`.
  - **Penyederhanaan BMC (`07`) & Grafik Proyeksi 5 Tahun (`09`):** Menghapus *pill badge* dan subjudul panjang di `09` serta mengganti istilah/jargon teknis (`IP54+`, `PWA`, `FPV`, `Custom Carrier PCB`, `Edge INT8`, `Direct BOM`, `VPS Golang`, `LiFePO₄`, `in-kind`, `Unit Economics`, `TCO`, `Go-To-Market`) menjadi bahasa Indonesia bisnis yang jernih bagi orang awam dan investor.
  - **Penggantian Foto Kit Rover PoC (`04d_ilustrasi_rover_4wd_poc.png`):** Memotong bersih bingkai iklan marketplace dari `image.png`, menyimpan sebagai `04d_ilustrasi_rover_4wd_poc.png`, menghapus `07_kit_4wd_poc_eksisting.jpg` serta `image.png`, dan menampilkannya pada Bab 7 dengan label `[ILUSTRASI REFERENSI KONFIGURASI HARDWARE]`.
  - **Sinkronisasi Penuh & Kebersihan Git:** Menyinkronkan `README.md` 100% identik dengan `PROJECT_CONCEPT_BROVER.md` via `sync_readme.py`, mengecualikan PDF inspirasi eksternal `4 IT 1 ELEKTRO_NUSAQC_PROPOSAL.pdf` di `.gitignore`, dan memperbarui `MEMORY.md` serta `HISTORY.md`.
- **File Terdampak:**
  - `[NEW]` `06_Project_Concept_BROVER/assets/04d_ilustrasi_rover_4wd_poc.png`
  - `[NEW]` `06_Project_Concept_BROVER/assets/06_roadmap_tkt_dan_evolusi_brover.svg`
  - `[DELETE]` `06_Project_Concept_BROVER/assets/07_kit_4wd_poc_eksisting.jpg`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_business_timeline_svgs.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/06_roadmap_tkt_dan_evolusi_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/07_business_model_canvas_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/08_project_timeline_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/09_proyeksi_keuntungan_5tahun_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `README.md`
  - `[MODIFY]` `.gitignore`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memastikan seluruh visual proposal dan halaman utama GitHub langsung dipahami pembaca awam maupun dewan juri tanpa distraksi jargon teknis, serta setiap klaim kenaikan TKT ditopang langsung oleh regulasi resmi dan literatur *peer-reviewed*.
- **Verifikasi:** Validasi paritas 100% antara `PROJECT_CONCEPT_BROVER.md` dan `README.md` lulus; `0` *em-dash* & `0` Alibaba di seluruh markdown dan `8` SVG; `22/22` tautan lokal valid; Bab `1–12` & Referensi `1–53` berurutan; seluruh PNG (`04d`, `06`, `07`, `08`, `09`) lolos inspeksi visual langsung.

---

## [2026-11-24 19:04 WIB] — `feat(business,visuals): switch to 100% RI sourcing + All-In no-subscription pricing, redesign BMC & W1-W4 Timeline, and add 5-year investor ROI chart`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Finalisasi model bisnis murni sepaket tanpa langganan bulanan (Opsi 2), 100% rantai pasok e-commerce & distributor lokal Indonesia (menghapus Alibaba), desain ulang BMC & Project Timeline mingguan (`W1–W4`), serta penambahan grafik proyeksi keuntungan 5 tahun bagi investor/peternak.
- **Ringkasan Perubahan:**
  - **100% Pengadaan Indonesia & Skema Jual Murni All-In Sepaket (Opsi 2):** Menghapus seluruh rujukan Alibaba pada Bab 4.4, 8.2, 9.1, 9.2, 9.4, dan 10; menyusun perbandingan **HPP Eceran 1 Unit RI (`Rp8,23 juta`)** vs **HPP Grosir Distributor Lokal RI ≥20–50 Unit (`~Rp6,75 juta`, Direct BOM `Rp5,90 jt` + overhead `Rp850 rb`)**. Menetapkan harga jual **All-In Sepaket `Rp11,50 juta/unit`** (termasuk Website PWA, cadangan operasional server Cloud 3 tahun `Rp900 rb/unit` + *auto-prune* arsip >6 bulan, & *Cleaning Dock*; nol langganan bulanan) dengan untung kotor bersih **`Rp2,37 juta/unit` (`20,6%`, eceran)** hingga **`Rp3,85 juta/unit` (`33,5%`, grosir RI)**, serta pendapatan berulang alami dari **Paket Suku Cadang Aus & Kalibrasi Berkala (`~Rp1,5 juta` tiap 2–3 tahun)** dan **Skema Sewa `Rp550–650 ribu/siklus`** bagi peternak skala 3.000–5.000 ekor.
  - **Proyeksi Keuntungan 5 Tahun (30 Siklus) untuk Investor (`09_proyeksi_keuntungan_5tahun_brover.svg/.png`):** Membuat grafik perbandingan laba kumulatif 5 tahun **Dengan vs Tanpa `BROVER`** pada kandang menengah `15.000 ekor` (setara rata-rata 6 farm mitra PT Zara) berbasis `Pramuwidyatama et al. (2023)` dengan TCO `Rp13,00 juta` (beli All-In `Rp11,50 jt` + ganti sensor/baterai Tahun ke-3 `Rp1,50 jt`): selisih untung bersih 5 tahun **`+Rp25,85 juta` (`ROI 199%`, Konservatif 15%)**, **`+Rp64,70 juta` (`ROI 498%`, Moderat 30%, BEP Tahun ke-2)**, dan **`+Rp115,00 juta` (`ROI 885%`, Optimistis 50%)**, dilengkapi pembanding jujur skala `3.000 ekor` (`+Rp13,10 juta`, lebih cocok sewa/koperasi) dan alasan objektif memilih horizon 5 tahun (bukan 10 tahun).
  - **Desain Ulang BMC (`07`) & Project Timeline Mingguan `W1–W4` (`08`):** Memperbarui `07_business_model_canvas_brover.svg/.png` (judul bersih `Business Model Canvas`, 100% RI + All-In tanpa langganan bulanan, catatan kaki berbasis data BPS 2025, PT Zara/PT Edura, & wawancara praktisi Edufarmers × PecahTelur) dan `08_project_timeline_brover.svg/.png` (`1920×980` → `3840×1960 px` dengan **40 kolom minggu eksplisit `1 | 2 | 3 | 4` pada seluruh 10 bulan Nov 2026–Agu 2027**).
  - **Adopsi Antena Wi-Fi Eksternal 2,4 GHz (Bab 7.1, 8.1, & 8.2):** Menambahkan catatan rekayasa adopsi antena Wi-Fi eksternal vertikal (terinspirasi tata letak rover berkamera 4WD) pada `Orange Pi 3B` versi final untuk kestabilan jangkauan kandang panjang `60–120 m` sembari mempertegas pembedaan dari `ESP32-CAM`/`L298N` kit hobi.
  - **Sinkronisasi Penuh:** Menjalankan `sync_readme.py` untuk memperbarui `README.md` root GitHub serta menyelaraskan `MEMORY.md`.
- **File Terdampak:**
  - `[NEW]` `06_Project_Concept_BROVER/assets/09_proyeksi_keuntungan_5tahun_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_business_timeline_svgs.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/07_business_model_canvas_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/08_project_timeline_brover.svg` & `.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `README.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Menghilangkan hambatan adopsi peternak akibat tagihan bulanan (*subscription fatigue*) dan kompleksitas impor langsung tahap awal, memperjelas *unit economics* tim serta proyeksi laba 5 tahun bagi investor, dan menyajikan jadwal pelaksanaan mingguan (`W1–W4`) yang mudah dipahami.
- **Verifikasi:** Validasi XML & anti *double-escape* lulus pada seluruh `7` SVG; `0` *em-dash* & `0` rujukan Alibaba pada seluruh SVG, `PROJECT_CONCEPT_BROVER.md`, dan `README.md`; `22/22` tautan lokal valid di kedua markdown; Bab `1–12` & Referensi `1–49` berurutan; seluruh PNG (`07`, `08`, `09`) lolos inspeksi visual langsung tanpa tabrakan teks maupun garis.

---

## [2026-11-24 18:32 WIB] — `feat(docs,visuals): audit real e-commerce BOM/COGS, add SOTA/KPI/AI Governance/Conclusion, generate User Flow/BMC/Timeline SVGs, and sync root README.md`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Audit ulang harga BOM lintas e-commerce Indonesia & Alibaba, pengayaan proposal hasil benchmarking rubrik Hackathon UNJ 2026, pembuatan 3 diagram vektor baru (`04c`, `07`, `08`), dan pembuatan `README.md` root untuk GitHub.
- **Ringkasan Perubahan:**
  - **Audit Harga BOM Nyata (Bab 8.2 & Ringkasan Eksekutif):** Memverifikasi ulang 19 item komponen pada Tokopedia, Shopee, Lazada, Blibli (+ grosir Alibaba) serta menambahkan komponen wajib (`Charger LiFePO₄ 14,6V`, `Bracket Motor 37 mm`, `Cleaning Dock`) dan *overhead* perakitan/ongkir/garansi: **HPP Eceran 1 Unit RI `~Rp8,23 juta`** (Direct BOM `Rp5,46–9,65 jt` + overhead `Rp950 rb`) vs **HPP Produksi Batch ≥50 Unit Lokal+Alibaba *landed* `~Rp4,57 juta`** (Direct BOM `~Rp3,72 jt` + overhead `Rp850 rb`); menyelaraskan harga `DFRobot SEN0567` menjadi `Rp175–230 rb`.
  - **Strategi Harga Aman 2-Tahap, Simulasi ROI, Tata Kelola AI, & *Risk Register* (Bab 9):** Menetapkan harga aman anti-rugi (*Pilot* `Rp10,5–11,5 jt` → *Komersial Batch* `Rp7,9–8,9 jt/unit` / Sewa `Rp450–500 rb/siklus` / Cloud `Rp100–150 rb/bln`), simulasi sensitivitas ROI 3 skenario (*Konservatif/Moderat/Optimistis*) berbasis `Pramuwidyatama et al. (2023)`, matriks Tata Kelola AI/Privasi/Etika Veteriner (*explicit consent*, anti-*overtrust*/AMR, transparansi bukti, lisensi AI/BMKG, HKI/NDA UNJ), serta *Risk Register* 8 risiko (`R01–R08`).
  - **SOTA, *Research Gap*, KPI, & Kesimpulan (Bab 4.4 & Bab 10):** Menambahkan tabel perbandingan SOTA (`ChickenBoy`, `Octopus XO`, CCTV statis, `Henomaly`, `SmartEars` vs `BROVER`), tabel target KPI terukur (PoC vs Bootcamp), dan Bab 10 Kesimpulan (Bab 11 Dataset, Bab 12 Referensi 1–49).
  - **3 Visual Vektor Baru (SVG → PNG via Playwright):** Membuat `06_Project_Concept_BROVER/scripts/generate_business_timeline_svgs.py` menghasilkan `04c_user_flow_brover.svg/.png` (User Flow 3 jalur peran + `mermaid` User Flow ringkas di bawahnya), `07_business_model_canvas_brover.svg/.png` (BMC 9-blok Osterwalder ramah awam), dan `08_project_timeline_brover.svg/.png` (*Gantt Chart* 10 bulan Nov 2026–Agu 2027 sesuai `[Pedoman, Hal. 4]`).
  - **Sinkronisasi `README.md` Root GitHub:** Membuat `06_Project_Concept_BROVER/scripts/sync_readme.py` dan menghasilkan `README.md` di root repository dengan pemetaan otomatis seluruh tautan gambar dan file relatif; menyelaraskan `MEMORY.md`.
- **File Terdampak:**
  - `[NEW]` `06_Project_Concept_BROVER/scripts/generate_business_timeline_svgs.py`
  - `[NEW]` `06_Project_Concept_BROVER/scripts/sync_readme.py`
  - `[NEW]` `06_Project_Concept_BROVER/assets/04c_user_flow_brover.svg` & `.png`
  - `[NEW]` `06_Project_Concept_BROVER/assets/07_business_model_canvas_brover.svg` & `.png`
  - `[NEW]` `06_Project_Concept_BROVER/assets/08_project_timeline_brover.svg` & `.png`
  - `[NEW]` `README.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Mencegah kesalahan penetapan harga jual di bawah HPP eceran ritel Indonesia, memisahkan tegas *User Flow* bagi awam dari proses mesin, melengkapi aspek penentu rubrik juri UNJ (Kebaruan 30%, Kelayakan 20%, Bisnis 15%), serta membuat halaman utama GitHub langsung informatif lewat `README.md`.
- **Verifikasi:** Validasi XML & anti *double-escape* lulus pada `04c`, `07`, `08`; `0` *em-dash* di seluruh SVG, `PROJECT_CONCEPT_BROVER.md`, dan `README.md`; `21/21` tautan lokal valid di kedua markdown; Bab `1–12` & Referensi `1–49` berurutan; seluruh PNG lolos inspeksi visual langsung.

---

## [2026-11-24 16:53 WIB] — `feat(docs,visuals): add Ross 308 standards, Website-First strategy, split 04a/04b vector diagrams, and justify 15s audio + <=0.1 m/s`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penyempurnaan Bab 4.2, Bab 5, Bab 6, dan aset visual alur kerja `BROVER` sesuai rencana yang disetujui.
- **Ringkasan Perubahan:**
  - **Standar Umur `Ross 308` + Jurnal *Peer-Reviewed*:** Menambahkan tabel suhu, RH, dan target bobot resmi **`Ross 308`** (*Aviagen Ross Broiler Management Handbook* 2018 & *Ross 308 Performance Objectives* 2022) serta rujukan lingkungan tropis *peer-reviewed* (`Quintana-Ospina et al., Animals, 2023`) berdampingan dengan `Cobb 500` di Bab 4.2.
  - **Strategi *Website-First* + Mobile Native (*Future Work*):** Mempertegas di Bab 5 (*Tech Stack*) bahwa tahap awal fokus pada **Website (`Next.js` PWA) + halaman kendali FPV web lokal langsung dari `RPi 4` / `Orange Pi 3B` (`http://192.168.4.1`)** agar browser HP bebas blokir *Mixed Content* (`https://` → `ws://`) dan tetap jalan luring, sementara **Aplikasi Mobile Native (`Flutter`/`React Native`)** ditetapkan sebagai *Future Work* (TKT 8–9).
  - **Pemisahan Gambar 04 Menjadi 2 Diagram Vektor Mandiri (SVG → PNG):** Membuat `06_Project_Concept_BROVER/scripts/generate_workflow_svgs.py` menghasilkan:
    - `04a_pola_jalur_inspeksi_rover.svg` / `.png` (`2560×1680 px`): denah jalur huruf U yang *to the point* tanpa blok `"Batas Jujur"` maupun teks `"RUANG PUTAR & CLEANING DOCK (Zona Dalam — 1 Unit = 1 Kandang)"`.
    - `04b_alur_4tahap_inspeksi_brover.svg` / `.png` (`3200×1520 px`): alur 4-tahap horizontal berikon besar, panah tegas, 3 tombol aksi visual, dan SOP sanitasi roda 3 langkah.
  - **Justifikasi Ilmiah Bagian 6.2 (`≤0,1 m/s` & Audio `15 Detik` = `3×5 Detik` *Voting*):** Menambahkan sitasi *peer-reviewed* eksplisit untuk batas kecepatan **`≤0,1 m/s`** (`RobôFrango PMC11011048`, `AviSense PMC13696172`, `Parajuli et al. 2020 Trans. ASABE`, `Octopus XO`) serta meningkatkan durasi berhenti *Stop–Mute–Sample* dari `5 detik` tunggal menjadi **`15 detik` (`~1–2 detik` jeda hening + `3 segmen × 5 detik` *voting* model *SmartEars*, Qiao *et al.*, *Comp. Electron. Agric.*, 2026)** agar gejala intermiten tertangkap; menyelaraskan `03_arsitektur_sistem_brover.svg/.png`, `MEMORY.md`, dan memperbarui Daftar Pustaka (49 referensi terverifikasi, berurutan 1–49).
- **File Terdampak:**
  - `[NEW]` `06_Project_Concept_BROVER/scripts/generate_workflow_svgs.py`
  - `[NEW]` `06_Project_Concept_BROVER/assets/04a_pola_jalur_inspeksi_rover.svg`
  - `[NEW]` `06_Project_Concept_BROVER/assets/04a_pola_jalur_inspeksi_rover.png`
  - `[NEW]` `06_Project_Concept_BROVER/assets/04b_alur_4tahap_inspeksi_brover.svg`
  - `[NEW]` `06_Project_Concept_BROVER/assets/04b_alur_4tahap_inspeksi_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_architecture_svg.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.svg`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Memenuhi kebutuhan acuan ganda `Cobb 500` & `Ross 308`, memisahkan diagram jalur vs alur 4-tahap agar terbaca cepat oleh orang awam, memvalidasi keamanan arsitektur kontrol FPV berbasis website di HP, dan memastikan setiap angka teknis (`≤0,1 m/s` dan `15 detik = 3×5 detik`) berdiri di atas literatur *peer-reviewed* yang objektif.
- **Verifikasi:** Validasi XML & anti *double-escape* lulus pada `03`, `04a`, `04b`; `0` *em-dash* di seluruh SVG & `PROJECT_CONCEPT_BROVER.md`; `17/17` tautan lokal valid; Bab 11 berurutan `1..49`; seluruh PNG lolos inspeksi visual langsung.

---

## [2026-11-24 16:28 WIB] — `feat(docs,visuals): adopt hybrid BMKG + Open-Meteo weather API, clarify Cobb 500, and highlight web Rover control`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penyempurnaan arsitektur cuaca luar (Opsi 1: Hibrida `BMKG` + `Open-Meteo`), penambahan penjelasan ramah awam untuk `Cobb 500`, serta penegasan kendali `Rover` langsung lewat website.
- **Ringkasan Perubahan:**
  - **Cuaca Luar Hibrida `BMKG` + `Open-Meteo`:** Memperbarui Fitur 2, Bab 5 (*Tech Stack*), Panel 1, Mitigasi *Worst-Case* #1, `MEMORY.md`, dan Diagram Arsitektur 03 agar memisahkan tegas **pemetaan zona dalam kandang (100% sensor fisik `Rover`)** vs **prakiraan cuaca luar kandang** memakai `BMKG API Publik` (`adm4` desa/kelurahan, 0–72 jam) + `Open-Meteo API` (`ECMWF IFS` per 1 jam 1–7 hari sebagai *automatic fallback*), di-cache 3–6 jam di backend `Golang`; menambahkan referensi resmi BMKG (#44) sehingga Daftar Pustaka menjadi 46 referensi terverifikasi.
  - **Penjelasan Istilah `Cobb 500`:** Menambahkan keterangan lugas bahwa `Cobb 500` adalah bibit/*strain* ayam broiler komersial dominan di Indonesia (bersama `Ross 308`) dengan panduan suhu-RH resmi per umur pada Ringkasan Eksekutif, Fitur 2, `MEMORY.md`, dan Diagram Arsitektur 03.
  - **Penegasan Kendali `Rover` Lewat Website:** Memperjelas eksplisit bahwa `Rover Inspeksi` dikendalikan operator langsung lewat website (browser HP/laptop via Wi-Fi lokal nirkabel) di Zona 1, Zona 3 (Panel 3), Zona 4A Diagram Arsitektur 03 (`SVG` + `PNG` `3200×1840 px`), Ringkasan Eksekutif, Fitur 1, dan `MEMORY.md`.
- **File Terdampak:**
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_architecture_svg.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.svg`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** `Google Weather API` dibatasi *internal usage only* di Indonesia; kombinasi `BMKG` (stasiun/radar lokal RI level desa) + `Open-Meteo` (resolusi per jam 1–7 hari & *fallback* andal) memberikan akurasi, ketahanan, dan kredibilitas nasional paling objektif, sementara penjelasan `Cobb 500` dan kendali website menghilangkan ambiguitas bagi pembaca awam.
- **Verifikasi:** Validasi XML SVG lulus, render PNG `3200×1840 px` (`732,5 KB`), `0` *em-dash* di `PROJECT_CONCEPT_BROVER.md` & `.svg`, dan lolos inspeksi visual langsung (nol tumpang tindih/potongan).

---

## [2026-11-24 13:55 WIB] — `feat(visuals): redesign BROVER architecture diagram to layperson-friendly vector SVG`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Desain ulang diagram arsitektur `BROVER` agar mudah dipahami orang awam dalam 5–10 detik berdasarkan *C4 Model* (Simon Brown), *Paivio Dual Coding & Mayer Multimedia Learning*, serta *Elsevier/Nature Graphical Abstract Guidelines* (Opsi 1 Hibrida Cerdas + Opsi A 1 Diagram Terpadu).
- **Ringkasan Perubahan:**
  - Membuat generator vektor baru `06_Project_Concept_BROVER/scripts/generate_architecture_svg.py` dengan alur linier kiri ke kanan (`1. Rover di Kandang` → `2. Koneksi & Server` → `3. Dasbor Aplikasi` → `4. Tindakan Nyata: Peternak/ABK & Dokter Hewan/Dinas`), 12+ ikon vektor *flat-line* kustom (rover, kamera, mikrofon, sensor udara, chip AI, rem aman, Wi-Fi, cloud/cuaca, laptop+HP, peternak, stetoskop), serta *pill badge* ringkas *tech stack* (`RPi 4 / Orange Pi 3B`, `ESP32`, `SHT31 & SEN0567`, `Golang`, `PostgreSQL`, `Open-Meteo`, `Next.js PWA`, `Standar Cobb 500`).
  - Menyimpan sumber vektor yang dapat diedit di `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.svg` dan me-render PNG resolusi tinggi (`3200×1840 px`, 2× scale) melalui Playwright Chromium ke `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.png`.
  - Mendelegasikan pemanggilan Fig 3 pada `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py` ke `generate_architecture_svg.py` agar tidak tertimpa diagram Matplotlib lama.
  - Memperbarui *caption* Gambar 03 pada `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` agar lebih lugas bagi pembaca lintas bidang (`0` *em-dash*).
- **File Terdampak:**
  - `[NEW]` `06_Project_Concept_BROVER/scripts/generate_architecture_svg.py`
  - `[NEW]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.svg`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/03_arsitektur_sistem_brover.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Diagram blok teks lama (>160 kata jargon + kode seri BOM tanpa ikon) menyulitkan pembaca non-teknis; pemisahan alur awam + *pill badge* teknologi menjaga keterbacaan bagi peternak/dokter hewan sekaligus menampilkan *tech stack* secara ringkas bagi juri teknis.
- **Verifikasi:** Validasi XML SVG lolos, render PNG `3200×1840 px` (`723,9 KB`), `0` *em-dash*, dan lolos 2 tahap inspeksi visual langsung (nol tumpang tindih, nol teks terpotong).

---

## [2026-11-24 13:28 WIB] — `docs: refocus BROVER background on disease margin risk and sync references`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Penajaman *problem-solution fit* pada Bab 2 (Latar Belakang) `PROJECT_CONCEPT_BROVER.md` sesuai Opsi 1 yang disetujui.
- **Ringkasan Perubahan:**
  - Menghapus rincian persentase biaya pakan/DOC (`Junaidi et al., 2023`) serta penyebutan fase pakan di Bab 2 (Latar Belakang) agar tidak memicu salah paham ruang lingkup seolah-olah `BROVER` menyelesaikan masalah biaya pakan/DOC.
  - Mengganti langsung dengan angka primer Scopus Q1 margin kotor normal (`Rp5,28 juta/siklus` skala 3.000 ekor) vs kerugian wabah (`Rp22,89–57,35 juta`, `Pramuwidyatama et al., 2023`) serta fokus pada pemantauan penyakit dan suhu-RH per umur.
  - Menghapus entri yatim `Junaidi et al. (2023)` dari Bab 11 dan merapikan penomoran Daftar Pustaka (45 referensi terverifikasi).
- **File Terdampak:**
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Menjaga keselarasan ketat antara latar belakang masalah dan solusi inspeksi penyakit/mikroklimat `BROVER` serta sinkronisasi sitasi–daftar pustaka sesuai APA 7 / IEEE.

---

## [2026-11-24 13:18 WIB] — `fix(docs): swap technical role descriptions between Ahmad Syauqi Reza and Arya Bisma Putra Refman`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Koreksi penukaran rincian peran teknis kedua anggota `Hacker`.
- **Ringkasan Perubahan:**
  - Memperbarui peran **Ahmad Syauqi Reza (`Hacker`)** menjadi fokus *Embedded/IoT (`ESP32`), Custom Carrier PCB, Wi-Fi Lokal, Edge AI, & Backend Golang*.
  - Memperbarui peran **Arya Bisma Putra Refman (`Hacker`)** menjadi fokus *Software Engineering, pelatihan & kuantisasi Multi-Modal AI, & Integrasi Sistem*.
- **File Terdampak:**
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Menyelaraskan rincian tugas teknis pada seluruh dokumen agar sesuai pembagian peran aktual tim.

---

## [2026-11-24 12:01 WIB] — `docs: align academic writing style (EYD V, APA 7, IEEE), rewrite executive summary, and simplify vicious cycle diagram`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Audit dan penyempurnaan gaya penulisan ilmiah internasional/nasional pada 3 dokumen inti serta penyederhanaan visual *Vicious Cycle*.
- **Ringkasan Perubahan:**
  - **Standar Tanda Baca (EYD V, APA 7th, IEEE):** Menghilangkan seluruh penggunaan *em-dash* (`—`) non-standar dari total **659 kemunculan menjadi 0** di ketiga dokumen (`V3_TRANSPARAN.md`: 352→0; `ROOT_CAUSE...md`: 200→0; `PROJECT_CONCEPT_BROVER.md`: 107→0), digantikan titik dua (`:`), koma (`,`), titik (`.`), atau tanda kurung sesuai peran sintaktik; menyeragamkan tanda hubung `Edge-Cloud`.
  - **Penertiban Tanda Petik Ganda & Tanda Seru:** Menghapus seluruh *scare quotes* non-kutipan dan tanda seru di luar kutipan judul asli sumber (hanya mempertahankan tanda petik untuk kutipan verbatim resmi dari jurnal/BBPKH/DFRobot).
  - **Kalibrasi *Academic Hedging* (Anti-*Overclaim*):** Mengganti diksi hiperbolis/absolut (*katastrofik, mutlak, jebol, meruntuhkan benteng, kalah telak, nol risiko, 100% kualitatif*) dengan formulasi objektif dan terukur, membakukan ejaan KBBI EYD V (`respons`), serta mengganti panah simbolik di prosa menjadi konjungsi baku.
  - **Ringkasan Eksekutif Standar Harvard/MIT/Purdue OWL:** Menulis ulang Ringkasan Eksekutif di `PROJECT_CONCEPT_BROVER.md` agar mandiri (*standalone*), bebas angka teknis mikro komponen, dan berfokus pada Masalah, Solusi, Nilai Ekonomi, serta Kesiapan Bertahap.
  - **Penyederhanaan Grafik *Vicious Cycle* (Elsevier/Nature Graphical Abstract Guidelines):** Membuat skrip `03_Root_Cause_Analysis/scripts/generate_vicious_cycle.py` dan meregenerasi `03_vicious_cycle_mikroklimat_dan_penyakit.png` (300 DPI) menjadi ringkas (~80 kata inti, 2 poin pendek per tahap, font besar, bebas kepadatan teks, dan lolos inspeksi visual).
- **File Terdampak:**
  - `[MODIFY]` `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md`
  - `[MODIFY]` `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md`
  - `[NEW]` `03_Root_Cause_Analysis/scripts/generate_vicious_cycle.py`
  - `[MODIFY]` `03_Root_Cause_Analysis/assets/03_vicious_cycle_mikroklimat_dan_penyakit.png`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Menyelaraskan kualitas dokumen riset dan proposal dengan standar karya tulis ilmiah internasional (APA 7, IEEE, Elsevier/Nature) serta EYD V Kemendikbudristek, dan meningkatkan keterbacaan visual *Vicious Cycle*.
- **Verifikasi:** Audit otomatis memastikan `0` *em-dash*, `0` *scare quotes*, `0` tanda baca ganda, `0` tautan lokal rusak (`58/58` valid lintas 3 dokumen), dan grafik `03_vicious_cycle_mikroklimat_dan_penyakit.png` terverifikasi visual bebas tumpang tindih.

---

## [2026-11-24 11:07 WIB] — `fix(docs): correct student affiliation to Teknologi Informasi ITS`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Koreksi afiliasi universitas 4 anggota mahasiswa (kolaborasi lintas institusi ITS × UNJ).
- **Ringkasan Perubahan:**
  - Memperbaiki afiliasi **M. Hikari Reiziq Rakhmadinta, Ahmad Syauqi Reza, Arya Bisma Putra Refman, dan Aditya Reza Daffansyah** menjadi **Mahasiswa Teknologi Informasi ITS** (bukan UNJ), berkolaborasi dengan **Dr. drh. Atin Supiyani, M.Si.** (Dosen Aktif Biologi **UNJ**).
  - Memperbarui footer grafik `06_roadmap_tkt_dan_evolusi_brover.png` agar mencantumkan `4 TI ITS + DR. DRH. ATIN SUPIYANI, M.SI. UNJ`.
- **File Terdampak:**
  - `[MODIFY]` `.agent/rules/hackathon-context.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
  - `[MODIFY]` `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/scripts/generate_concept_visuals.py`
  - `[MODIFY]` `06_Project_Concept_BROVER/assets/06_roadmap_tkt_dan_evolusi_brover.png`
- **Alasan / Keputusan Penting:** Menjamin akurasi faktual identitas institusi seluruh anggota Tim Asprak sebelum pendaftaran & penyusunan proposal.
- **Verifikasi:** Audit grep memastikan `0` sisa `"Teknologi Informasi UNJ"` dan grafik `06` diregenerasi ulang bersih.

---

## [2026-11-24 11:04 WIB] — `chore: remove obsolete problem research V1/V2 drafts and update memory logs`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Pembersihan file & aset riset lama (V1 & V2) yang sudah tidak terpakai dan digantikan penuh oleh `V3_TRANSPARAN.md`.
- **Ringkasan Perubahan:**
  - Menghapus manual arsip usang V1 & V2 di folder `02_Problem_Research/` (`14 files` total: 2 markdown + 12 PNG aset lama).
  - Memperbarui catatan pada `MEMORY.md` dan header `TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md`.
- **File Terdampak:**
  - `[DELETE]` `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA.md`
  - `[DELETE]` `02_Problem_Research/terlaluOverClaim_TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V2.md`
  - `[DELETE]` `02_Problem_Research/assets_v2/` (5 gambar)
  - `[DELETE]` `02_Problem_Research/terlaluOverClaim_assets/` (7 gambar)
  - `[MODIFY]` `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
- **Alasan / Keputusan Penting:** Merampingkan repository agar hanya menyimpan dokumen riset aktif (`V3_TRANSPARAN.md`) yang terverifikasi.
- **Verifikasi:** Audit grep memastikan `0` tautan rusak di folder `01`, `03`, `04`, `05`, maupun `06_Project_Concept_BROVER/`.

---

## [2026-11-24 10:58 WIB] — `docs: clarify Dr. drh. Atin Supiyani, M.Si. role as team member`
- **Kontributor / Konteks:** Tim Asprak (`HikariReiziq`) — Koreksi status peran anggota ke-5 pada seluruh dokumen konteks dan konsep proyek.
- **Ringkasan Perubahan:**
  - Mengubah penyebutan peran **Dr. drh. Atin Supiyani, M.Si.** (Dosen Biologi UNJ — bidang Fisiologi & Kesehatan Hewan) dari sebelumnya *"Dosen Pembimbing"* menjadi **`Anggota Tim — Pakar Domain Veteriner`** di seluruh dokumen aktif.
- **File Terdampak:**
  - `[MODIFY]` `.agent/rules/hackathon-context.md`
  - `[MODIFY]` `MEMORY.md`
  - `[MODIFY]` `HISTORY.md`
  - `[MODIFY]` `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md`
  - `[MODIFY]` `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`
- **Alasan / Keputusan Penting:** Dr. drh. Atin Supiyani, M.Si. berstatus sebagai anggota aktif Tim Asprak (bukan dosen pembimbing terpisah).
- **Verifikasi:** Audit grep memastikan `0` sisa penyebutan *"Dosen Pembimbing"* pada seluruh dokumen aktif.

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
