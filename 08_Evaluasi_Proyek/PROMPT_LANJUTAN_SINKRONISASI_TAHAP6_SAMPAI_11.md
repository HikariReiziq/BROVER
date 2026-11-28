# Prompt Lanjutan: Sinkronisasi BROVER Tahap 6 sampai 11

Salin seluruh isi di bawah garis ini ke sesi agent baru.

---

Kamu melanjutkan pekerjaan sinkronisasi dan evaluasi ulang proyek **BROVER** milik Tim **Asprak** (Hackathon Deep Tech UNJ 2026, jalur D-FARM, *Focus Challenge* Smart Poultry Production). Workspace: `/home/reiziqzip/Programmer/Hackathon-UNJ`. Sesi sebelumnya sudah menyelesaikan Tahap 1 sampai 5 dan sebagian Tahap 6 dari rencana yang **sudah disetujui user**. Lanjutkan dari titik berhenti. Jangan mengulang pekerjaan yang sudah selesai.

## 1. Baca Dulu, Berurutan
1. `MEMORY.md` di akar. Sudah diperbarui 28 Nov 2026 dan memuat semua keputusan terkunci.
2. `08_Evaluasi_Proyek/PROMPT_SESI_BARU_SINKRONISASI_DAN_EVALUASI_ULANG.md`. Ini spesifikasi lengkap tugas, gaya bahasa, dan larangan. Bagian 13 berisi pola grep konsistensi. Bagian evaluasi berisi 10 bagian wajib `EVALUASI_ULANG_BROVER.md`.
3. `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`. Sudah ditulis ulang menjadi 13 bab dan menjadi **sumber kebenaran** isi.
4. `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md`, berisi kartu fitur F1 sampai F4.
5. `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md`. Ini baseline dan **tidak boleh diubah**.

## 2. Tujuan Akhir
1. Semua berkas dalam lingkup konsisten dengan keputusan final tim per 28 Nov 2026.
2. Concept mencakup semua bagian template proposal. Bagian ini sudah selesai.
3. Diagram dirender ulang. Bagian ini sudah selesai.
4. PDF TOP5 dan RCA dibuat ulang lengkap dengan gambarnya.
5. Berkas baru `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md` ditulis.
6. Tidak ada commit.

## 3. Keputusan Terkunci
- **Judul:** "BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler". Pakai kata *skrining*. Jangan pakai *deteksi dini*, *multi-modal*, atau *prediksi*.
- **Empat fitur:**
  - **F1:** rover disetir lewat web di `192.168.4.1`, dengan rem 500 ms. Kecepatan 0,07 sampai 0,1 m/s. Kamera IMX291 dipasang pada servo DS3218 dua posisi: depan sekitar 0 sampai 15° untuk FPV, bawah sekitar 45° untuk feses, dengan LED 5000K. Sensor jarak memperlambat laju.
  - **F2:** SHT31 dan SEN0567 dipasang di tiang setinggi ayam. Ada mode stasiun di dok dalam kandang, dengan pencatatan per menit. SEN0567 hanya tren kualitatif.
  - **F3:** CV feses adalah **satu-satunya AI**. Detektor Apache-2.0 (YOLOX atau RT-DETR), RKNN INT8 di Orange Pi 3B, ONNX di server untuk Saku, PoC di Raspberry Pi 4 dengan NCNN atau ONNX.
  - **F4:** dasbor PWA tanpa skor 0 sampai 100, dengan catatan harian ABK, ceklis gejala dan vaksin, triase 3 tombol, laporan 1-klik ke dokter hewan, serta cuaca dari BMKG dan Open-Meteo.
- **Dihapus:** audio, mikrofon INMP441, Model #2 fisik ayam, deteksi bangkai, *node* tetap, CO2.
- **Operasi:**
  - Hari 0 sampai 6: mode stasiun.
  - Hari ke-7 sampai panen: 2 putaran per hari, pagi dan pukul 15.00 sampai 16.00.
- **Paket:**
  - **BROVER Saku:** Rp75 ribu per siklus.
  - **BROVER Kandang:** Rp750 ribu per siklus, minimal 6 siklus.
  - **Beli putus:** usulan Rp11,5 juta. Harga final menunggu konfirmasi.
  - **Titik impas:** Saku **2,1 sampai 3,3 ekor**, Kandang **21 sampai 33 ekor**.
  - **Balik modal unit:** 14,1 siklus untuk eceran, 11,6 siklus untuk grosir.
  - Tanpa ROI.
  - Langganan per kandang, dengan protokol pemindahan unit. Sewa antarfarm jangka pendek dilarang.
- **BOM 18 item:** HPP Rp8.180.000 untuk eceran dan Rp6.714.000 untuk grosir.
- **TKT sekarang:**
  - Sistem utuh: 3.
  - Gerak, kendali web, dan dasbor: 4.
  - Target: 6 pada Februari 2027 dan 7 pada Agustus 2027.
- **Ketua Tim:** M. Hikari Reiziq Rakhmadinta.
- **Rencana pilot:** Dinas Pangan dan Pertanian Kota Cimahi dan peternakan keluarga salah satu anggota. Keduanya belum ada kesepakatan.

## 4. Sudah Selesai, Jangan Diulang
- **Tahap 1:** riset harga dan verifikasi.
- **Tahap 2:** concept ditulis ulang menjadi 13 bab.
  - Bab 12 berisi 85 entri Vancouver. Entri 69 Raspberry Pi baru ditambahkan.
  - Bab 13 memetakan concept ke template.
  - PETA_FITUR sudah diperbarui.
- **Tahap 3:** diagram 03, 04a, 04b, 04c, 05, 06, 07, 08, **08b (baru)**, dan **09_titik_impas (baru)** dirender dan dicek visual.
  - Gambar lama diarsipkan di `06_Project_Concept_BROVER/assets/history/2026-11-28_sebelum_sinkronisasi/` beserta README-nya.
  - Grep SVG bersih.
- **Tahap 4:** `sync_readme.py` sudah dijalankan. Tinggal 1 tautan putus, yaitu `EVALUASI_ULANG_BROVER.md`, karena berkasnya belum ada.
- **Tahap 5:** `MEMORY.md`, `.agent/rules/hackathon-context.md`, dan `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` sudah diperbarui. Berkas 02 sampai 04 sudah dicek dan bersih.
- **Tahap 6 SELESAI:**
  - Panduan 01, 02, dan 03 sudah diperbarui.
  - Ketiga foto mikrofon sudah dipindah ke `07_IoT_Hardware_Guide/assets/history/`, lengkap dengan README.
  - Entri foto mikrofon dihapus dari `07_IoT_Hardware_Guide/scripts/fetch_component_images.py`.
  - 72 rujukan gambar di panduan sudah dicek dan valid.
  - Panduan 03 juga dikoreksi: angka FPS, suhu *thermal runaway*, dan umur siklus baterai yang tidak terverifikasi diganti menjadi "mengikuti datasheet sel"; *Cleaning Dock* diganti menjadi dok dengan mode stasiun.
- **Tahap 7 SELESAI:**
  - **Label petelur untuk kasus Hari Farm:** ditambahkan di TOP5 butir Wabah dan di RCA Why 1 serta Why 3.
  - **Kasus HPAI di RCA:** angka −Rp57,35 juta kini disebut simulasi margin kotor HPAI pada broiler (Pramuwidyatama 2023).
  - **Catatan verifikasi:** Wilcox 62% dan Anwar Sani 0,28 diberi keterangan "diverifikasi ke teks penuh".
  - **Kata "gulung tikar":** diganti menjadi "berhenti beternak atau berganti manajemen".
  - **Skrip baru `08_Evaluasi_Proyek/tools/md_to_pdf.py`:** memakai Python-Markdown, path relatif, dan Playwright A4. Skrip ini menulis ulang `*_tmp.html` dan `*.md.pdf` TOP5 serta RCA.
  - **Hasil verifikasi PDF:**
    - TOP5: 44 halaman, 37 objek gambar unik. Objek yang sama bisa muncul di beberapa halaman karena gambar tinggi terpotong.
    - RCA: 22 halaman, 5 gambar.
    - Semua gambar termuat.
- **Tahap 8 SELESAI:** entri HISTORY baru sudah ada paling atas, bertanggal 2026-11-29 00:03 WIB. Setelah evaluasi ulang selesai, tambahkan baris `[NEW] 08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md` ke entri itu.
- **Tahap 9 SELESAI:**
  - **Grep pola bagian 13:** semua kecocokan berada di konteks yang sah. Untuk grep di zsh, pakai `bash -c` dengan array; variabel zsh tidak dipecah per kata.
  - **Panduan 03:** tautan tutorial YOLOv8 dan repo Custom-YoloV8-NPU diganti tautan YOLOX.
  - **Rujukan gambar:** concept 13, README 13, TOP5 37, RCA 5. Semuanya valid.
  - **Angka lama:** tidak ada yang tersisa. Kecocokan "Rp550" hanya harga komponen BOM.
- **Tahap 10 SELESAI:**
  - **`EVALUASI_ULANG_BROVER.md` sudah ditulis:** 13 bagian, mencakup 10 bagian wajib, catatan perubahan PETA_FITUR, kesiapan template, dan keputusan terbuka.
  - **Gaya:** `check_style.py` menghasilkan TOTAL MASALAH 0.
  - **Tautan:** 36 tautan diuji dua kali dengan hasil identik, yaitu 33 berkode 200, 2 berkode 403, dan 1 berkode 202. Ketiga DOI yang bukan 200 cocok judulnya di registri Crossref.
  - **`notes.py`:** ditambah 10 catatan sehingga kini memuat 166 entri.
  - **README:** `sync_readme.py` dijalankan ulang dan melaporkan **0 tautan rusak**.
  - **HISTORY:** entri teratas sudah dilengkapi.
- **Tahap 11 SELESAI pada sesi sebelumnya**, berupa laporan akhir di chat. Sisa pekerjaan hanya keputusan user yang tercatat di bagian 13 evaluasi ulang. Belum ada commit.

## 5. Sisa Pekerjaan
**Tahap 6. Panduan 02, belum disentuh:**
- Judul diganti menjadi "Prototype Lengkap CV Feses, Sensor di Tiang, & Integrasi Website".
- Hapus bagian 2A INMP441, item 8 dan 9 (INMP441 dan mikrofon USB), baris Driver I2S, wiring 5A, uji 5, dan kriteria lulus Cek Napas.
- Nomori ulang item. Rujukan perfboard berubah menjadi item #13 sampai #15.
- Mermaid: hapus MIC.
- Ganti bagian 2A dengan servo dua posisi, tiang sensor, dan mode stasiun. Dok fisik baru dibuat di Tahap 3.
- HC-SR04 **memperlambat** laju, tidak menghentikan.
- Edge AI:
  - Ganti Ultralytics/YOLOv8n/2,3 FPS dengan detektor Apache-2.0 + ONNX/NCNN/ONNX Runtime.
  - Tautannya YOLOX `https://github.com/Megvii-BaseDetection/YOLOX` dan RT-DETR `https://github.com/lyuwenyu/RT-DETR`.
  - Tulis "kecepatan diukur sendiri".
- ESP32-C3 disebut **pembanding uji meja**, bukan *node*.
- Ganti "demo seleksi Nov 2026" dengan target **M1 akhir Desember 2026**.
- Ganti "peringatan dini" dengan "peringatan".
- Tautan dataset disamakan dengan Bab 11 concept:
  - Zenodo 4628934 berlabel YOLO.
  - Zenodo 5801834 hanya PCR, tanpa label YOLO.
  - Mendeley 8pnbzpt2k9.
  - Hapus SmartEars, multimodal, dan Kaggle RGB fisik.

**Tahap 6. Panduan 03:**
- Hapus item 15 INMP441 dan baris wiring-nya.
- Satu model RKNN.
- Baterai cukup untuk 2 putaran ditambah mode stasiun.
- Dok untuk pengisian daya dan sanitasi.
- Tautan dataset disamakan dengan Bab 11.

**Tahap 6. Foto mikrofon:**
- Pindahkan foto berikut ke `07_IoT_Hardware_Guide/assets/history/`. Folder 07 belum terlacak git, jadi cukup pakai `mv` biasa.
  - `07_IoT_Hardware_Guide/assets/poc/40_inmp441_i2s_mic.jpg`
  - `assets/poc/10_usb_microphone.jpg`
  - `assets/final/15_inmp441_i2s_mic.jpg`
- Pastikan tidak ada rujukan yang tersisa ke foto-foto itu.

**Tahap 7. TOP5 dan RCA:**
- Tambahkan label **petelur** untuk kasus Hari Farm: TOP5 baris sekitar 94, RCA baris sekitar 75 dan 77.
- Tambahkan catatan verifikasi:
  - Wilcox terverifikasi.
  - Anwar Sani 0,28 terverifikasi.
  - Ganti kata "gulung tikar" dengan "berhenti beternak atau berganti manajemen".
- Buat `08_Evaluasi_Proyek/tools/md_to_pdf.py`:
  - Python-Markdown dengan ekstensi tables.
  - Path relatif.
  - Playwright `page.pdf` ukuran A4 dengan `print_background`.
  - Tunggu semua gambar termuat.
- Tulis ulang `*_tmp.html` dan `*.md.pdf` dengan nama yang sama.
- Verifikasi dengan `pdfimages -list`, hanya hitung tipe `image` tanpa `smask`. Hasilnya harus **37** untuk TOP5 dan **5** untuk RCA.

**Tahap 8. HISTORY.md:**
- Tambah satu entri paling atas sesuai template yang ada.
- Tanpa atribusi AI.

**Tahap 9. Konsistensi:**
- Jalankan grep pola sesuai bagian 13 prompt lama.
- Cek semua rujukan gambar.
- Cocokkan angka BOM, HPP, harga, titik impas, jadwal, dan TKT antarberkas.

**Tahap 10. Tulis `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md`:**
- Isinya 10 bagian wajib dari prompt lama, ditambah catatan perubahan PETA_FITUR dan kesiapan setiap bagian template.
- Gaya ketat: tanpa em-dash, tanda kutip, apostrof, tanda kurung di luar sintaks tautan, simbol pasal, dan kata klise.
- Jalankan `tools/check_style.py` sampai TOTAL 0.
- Jalankan `tools/check_links.py` dua kali, lalu `tools/make_table.py`. Tambahkan catatan URL baru di `tools/notes.py`.
- Setelah berkas jadi, **jalankan ulang** `python3 06_Project_Concept_BROVER/scripts/sync_readme.py`. Targetnya 0 tautan putus.

**Tahap 11. Laporan akhir ke user, berisi:**
- perubahan per berkas;
- ringkasan evaluasi;
- keputusan yang masih terbuka, yaitu harga beli putus, detail kandang pilot, perlakuan `*_tmp.html`, dan PDF SmartEars yang tidak disentuh.

## 6. Temuan Sesi Lalu yang Wajib Masuk Evaluasi
- Rentang BOM lama tidak konsisten secara aritmetika. Sudah dihitung ulang.
- Bab WOAH tertulis 6.4, seharusnya 6.5.
- Tabel Ross 308 salah:
  - H3 tertulis 100, seharusnya 102.
  - Batas bawah 195 dan 485 tidak berdasar.
  - Nilai H28 1.675 g milik Cobb.
  - Aturan "4×" tidak ditemukan.
- Data Candra 2025 tidak konsisten dan tidak dipakai. Angka 3.000 ekor dari Pramuwidyatama tidak terverifikasi dan sudah diberi label.
- BroilerX tidak memiliki harga publik.
- "Kling dan Quarles" diperbaiki menjadi "Quarles dan Kling" di PETA_FITUR.
- Titik impas Saku tertulis 2 sampai 3 ekor, padahal hitungannya 2,1 sampai 3,3 ekor. Pada nilai ayam terendah, 3 ekor belum menutup biaya. Sudah dikoreksi di concept dan MEMORY.
- Diagram 06 lama membagi kelompok TKT secara salah. Yang benar menurut materi LPPM Undip Permenristekdikti 42/2016: Riset Dasar 1 sampai 3, Terapan 4 sampai 6, Pengembangan 7 sampai 9.
- Banner diagram 06 lama salah mengutip Rowe 2019.
- Gambar 05 lama memuat angka FPS YOLOv8n dan suhu *thermal runaway* yang tidak terverifikasi. Sekarang diganti tabel spesifikasi resmi:
  - Orange Pi 3B: NPU 0,8 TOPS.
  - Orange Pi 5: NPU 6 TOPS.
  - Luckfox RV1106G3: NPU 1 TOPS INT8, RAM 256 MB.
  - Raspberry Pi 4: tanpa NPU, CPU 1,8 GHz.
- Diagram 04b lama menulis kebijakan "1 Unit = 1 Kandang" berasal dari WOAH. Sekarang ditulis sebagai SOP tim.
- AviSense: kecepatan sekitar 0,05 m/s, bukan 0,09. Parajuli hanya menguji 0,2 sampai 0,6 m/s. Nomor pasal ISO 8373 dihapus. Zenodo 5801834 tidak memiliki label YOLO.
- Perubahan PETA_FITUR yang wajib dicatat:
  - Bab 1 butir 7, 11, dan 12 sampai 15.
  - Bab 2 baris F1 dan alur butir 3.
  - Kartu F1: servo DS3218 Rp215.000, batas Saku.
  - Kartu F3: satu model dan foto berpasangan.
  - Bab 7 butir 2, 6, 15, dan butir 16 yang baru.
  - Tabel 8.1 ditambah baris 79 sampai 81.
  - Bagian 8.2: 81 tautan. Uji 1 menghasilkan 200×67 dan 403×14. Uji 2 menghasilkan 200×66 dan 403×15.

## 7. Larangan
- Jangan ubah `Proposal TA/` maupun `EVALUASI_OBJEKTIF_BROVER.md`.
- Jangan edit README secara manual. Pakai `sync_readme.py`.
- Jangan jalankan `generate_concept_visuals.py` secara penuh.
- Jangan sentuh `.gitignore`. Isinya sudah berubah sebelum sesi dan bukan urusan kita.
- PDF SmartEars berhak cipta Elsevier: jangan di-commit, jangan dipindah.
- **Jangan commit atau push** tanpa perintah eksplisit user. Bila diminta commit, pakai Conventional Commits, isi HISTORY, dan selaraskan MEMORY. **Dilarang menambahkan Co-Authored-By atau atribusi AI.**
- Jangan menghapus berkas terlacak git tanpa izin user. Jangan menimpa berkas tanpa melihat isinya dulu.
- Data pribadi (NIM, NIP, NIK, HP, email) tidak boleh masuk ke berkas publik.
- Preprint tidak boleh menjadi bukti utama.

## 8. Perintah Render
Bila perlu render ulang, jalankan dari akar repo:
- Diagram SVG: `uv run --python 3.13 --with playwright==1.63.0 python 06_Project_Concept_BROVER/scripts/<skrip>.py`. Skripnya `generate_architecture_svg.py`, `generate_workflow_svgs.py`, dan `generate_business_timeline_svgs.py`.
- Gambar 05 saja: masuk ke `scripts/`, lalu jalankan `uv run --python 3.13 --with matplotlib --with numpy python -c "import generate_concept_visuals as g; g.make_fig5_hardware_power()"`.
- Setiap PNG hasil render wajib dilihat langsung.

Setelah setiap kelompok berkas selesai, laporkan singkat ke user apa saja yang berubah.
