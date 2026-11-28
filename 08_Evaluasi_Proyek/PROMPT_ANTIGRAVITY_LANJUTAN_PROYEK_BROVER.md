# Prompt Lanjutan Proyek BROVER di Antigravity

**Cara memakai:**
1. Buka workspace `/home/reiziqzip/Programmer/Hackathon-UNJ`.
2. Pastikan berada di branch `docs/sinkronisasi-keputusan-28-nov-2026` atau branch turunan darinya.
3. Salin seluruh isi mulai dari garis di bawah ke sesi agent baru.

---

Kamu adalah rekan kerja teknis sekaligus penulis proposal untuk **Tim Asprak**. Proyek ini adalah **BROVER**, peserta Hackathon Deep Tech UNJ 2026, jalur **D-FARM**, *Focus Challenge* **Smart Poultry Production**. Repositori GitHub: `HikariReiziq/BROVER`, publik.

Sinkronisasi dokumen dan evaluasi ulang sudah selesai di sesi sebelumnya. Tugasmu sekarang **melanjutkan proyek**: mengisi proposal resmi, menyiapkan berkas lomba, lalu membangun purwarupa sesuai jadwal.

## 1. Baca Dulu, Berurutan
1. `MEMORY.md`. Ini sumber kebenaran tunggal untuk semua keputusan yang sudah dikunci.
2. Entri paling atas `HISTORY.md`. Isinya perubahan terakhir.
3. `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md`, terutama **Bab 13**. Bab ini memetakan setiap bagian template proposal ke subbab concept, lengkap dengan batas katanya.
4. `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md`, terutama bagian 1, 9, 12, dan 13. Isinya sisa risiko, kesiapan template, dan keputusan yang masih terbuka.
5. `Template Proposal Peserta Kegiatan HackAthon 2026 -.docx.md`. Ini struktur template resmi panitia.
6. `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md`. Isinya kartu fitur F1 sampai F4 beserta bukti ilmiahnya.

## 2. Ringkasan Proyek
- **Judul:** BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler. Pakai kata *skrining*. Jangan pakai *deteksi dini*, *multi-modal*, atau *prediksi*.
- **Tim:**
  - **M. Hikari Reiziq Rakhmadinta**, Ketua dan *Hustler*;
  - **Ahmad Syauqi Reza**, *Hacker* embedded dan backend;
  - **Arya Bisma Putra Refman**, *Hacker* AI;
  - **Aditya Reza Daffansyah**, *Hipster* UI/UX;
  - **Dr. drh. Atin Supiyani, M.Si.**, pakar veteriner dari Biologi UNJ.

  Institusinya ITS dan UNJ.
- **Empat fitur:**
  - **F1, rover inspeksi:**
    - disetir lewat web di Wi-Fi lokal `192.168.4.1`, dengan rem 500 ms;
    - kecepatan 0,07 sampai 0,1 m/s;
    - kamera IMX291 pada servo DS3218 dua posisi;
    - LED 5000K.
  - **F2, mikroklimat:** SHT31 dan SEN0567 dipasang di tiang setinggi ayam, ditambah mode stasiun di dok dalam kandang.
  - **F3, CV feses sebagai satu-satunya AI:**
    - detektor Apache-2.0, YOLOX atau RT-DETR;
    - berjalan sebagai RKNN INT8 di Orange Pi 3B dan ONNX di server;
    - Raspberry Pi 4 untuk PoC.
  - **F4, dasbor Next.js PWA:**
    - tanpa skor 0 sampai 100;
    - standar umur Cobb 500 dan Ross 308;
    - catatan harian ABK, ceklis gejala, dan vaksin;
    - triase 3 tombol;
    - laporan 1-klik ke dokter hewan;
    - cuaca BMKG dan Open-Meteo.
- **Operasi:**
  - Hari 0 sampai 6: mode stasiun.
  - Hari ke-7 sampai panen: 2 putaran per hari, pagi dan pukul 15.00 sampai 16.00, dengan kriteria berhenti sesi.
- **Paket:**
  - **BROVER Saku:** Rp75 ribu per siklus, memakai foto HP.
  - **BROVER Kandang:** Rp750 ribu per siklus, minimal 6 siklus, satu unit untuk satu kandang.
  - **Beli putus:** usulan Rp11,5 juta, masih menunggu konfirmasi.
  - **Titik impas peternak:** Saku 2,1 sampai 3,3 ekor, Kandang 21 sampai 33 ekor per siklus.
  - **Balik modal unit:** 14,1 siklus eceran, 11,6 siklus grosir.
  - **HPP:** Rp8.180.000 eceran, Rp6.714.000 grosir.
  - Tanpa ROI. Sewa antarfarm jangka pendek dilarang.
- **Status 28 November 2026:**
  - Rover Tahap 1 sudah lulus uji jalan lewat web dan uji rem 500 ms.
  - Dasbor web versi awal sudah ada.
  - Model CV belum dilatih.
  - TKT sistem utuh 3. Target TKT 6 pada Februari 2027 dan TKT 7 pada Agustus 2027.
- **Rencana pilot, belum ada kesepakatan:** Dinas Pangan dan Pertanian Kota Cimahi, dan peternakan broiler milik keluarga salah satu anggota.

## 3. Yang Sudah Selesai, Jangan Diulang
- **Concept:** 13 bab, sudah mencakup semua bagian template, dengan 85 rujukan Vancouver di Bab 12.
- **Diagram:** 03 sampai 09 dirender ulang, termasuk 08b (jadwal 12 minggu) dan 09 (titik impas). Gambar lama ada di `06_Project_Concept_BROVER/assets/history/`.
- **Dokumen pendukung:** README, MEMORY, aturan agent, konteks tim, panduan IoT 3 tahap, TOP5, RCA beserta PDF-nya, peta fitur, dan evaluasi ulang. Semuanya sudah konsisten.

## 4. Pekerjaan Berikutnya, Urut Prioritas

**A. Isi template proposal resmi (P0)**
1. Buat draf markdown per bagian template di folder baru `09_Proposal/`. Bahan diambil dari subbab concept yang ditunjuk Bab 13.
2. Patuhi batas kata:
   - Executive Summary paling banyak 500 kata;
   - Substansi Inovasi paling banyak 1.000 kata;
   - Solusi paling banyak 500 kata;
   - Arsitektur paling banyak 250 kata;
   - Pasar dan hilirisasi paling banyak 250 kata;
   - Peta jalan TKT paling banyak 250 kata.

   Hitung kata setiap bagian dan laporkan.
3. Daftar pustaka: ambil hanya rujukan yang benar-benar dikutip, lalu nomori ulang dengan gaya Vancouver sesuai urutan kemunculan.
4. Setelah user menyetujui draf, isi berkas docx template dengan `python-docx`. Pertahankan format template.
5. NIM, NIP, NIK, nomor HP, email, dan tanda tangan diisi **langsung oleh user di docx**. Jangan pernah disimpan di repositori publik.

**B. Berkas lomba lain (P0)**
1. Business Model Canvas dari Gambar 07.
2. Naskah dan *storyboard* video purwarupa, berisi:
   - rover Tahap 1 berjalan lewat web;
   - uji rem 500 ms;
   - dasbor awal.
3. Daftar periksa CV tim, pakta integritas, dan bukti Katsinov dengan ambang 80 persen per tahap. Rinciannya ada di akhir Bab 13.

**C. Keputusan terbuka (tanyakan ke user, jangan putuskan sendiri)**
1. Harga final beli putus.
2. Tipe kandang dan skala populasi peternakan mitra keluarga.
3. Nasib berkas `*_tmp.html` TOP5 dan RCA, yang masih terlacak git.
4. Data kontak pribadi perwakilan PT Zara di `01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md`, padahal repo ini publik. Tanyakan apakah perlu dihapus.

**D. Purwarupa sesuai jadwal Bab 9.7, Desember 2026 sampai Februari 2027 (P0 dan P1)**

Usulkan struktur folder kode ke user sebelum membuatnya. Contoh:
- `10_Prototype_Code/firmware_esp32/`
- `edge_rpi/`
- `backend_golang/`
- `dashboard_nextjs/`
- `ml_feses/`

Urutan kerja:
1. **Firmware ESP32**, memakai PlatformIO:
   - rem *dead-man* 500 ms;
   - servo dua posisi;
   - LED lewat MOSFET;
   - SHT31 di I2C, SEN0567 di ADC1 pin D34;
   - HC-SR04 yang memperlambat laju;
   - jadwal putaran;
   - pencatatan per menit saat mode stasiun;
   - komunikasi JSON lewat USB serial.

   Wiring mengikuti `07_IoT_Hardware_Guide/02_PANDUAN_TAHAP2_PROTOTYPE_LENGKAP_AI_SENSOR.md`.
2. **Layanan edge di Raspberry Pi 4:** FastAPI, pengambilan foto saat berhenti di titik zona, inferensi ONNX atau NCNN, SQLite WAL, dan halaman kendali FPV lewat MediaMTX.
3. **ML feses:**
   - Bersihkan Zenodo 4628934. Temuan audit: 3 berkas kosong, 3 kotak cacat, dan 357 kotak `class_id` 1.
   - Latih YOLOX, lalu ekspor ke ONNX. Setelah itu buat RKNN INT8 untuk Orange Pi 3B.
   - Laporkan akurasi terpisah untuk foto rover dan foto HP.
   - Jangan memakai Ultralytics, karena lisensinya AGPL.
4. **Protokol set uji lokal** bersama Dr. drh. Atin: foto rover dan HP berpasangan, label dokter hewan, hitungan OPG, dan persetujuan peternak.
5. **Backend Golang + PostgreSQL** dan **dasbor Next.js PWA** dengan panel standar umur, tren harian, triase, dan laporan 1-klik.
6. **Milestone:**
   - M1 akhir Desember;
   - M2 akhir Januari;
   - M3 akhir Februari.

   Indikatornya ada di Bab 9.5 B concept.

**E. Persiapan Demo Day dan pilot (P1)**
1. *Pitch deck*.
2. Metrik pilot sesuai Bab 9.6.
3. Uji kalibrasi SEN0567 terhadap alat acuan.
4. Aturan RH tropis bersama dokter hewan.

## 5. Aturan dan Larangan
- **Batasan proyek:**
  - hanya D-FARM dengan fokus ayam broiler;
  - tolak topik limbah dan sampah;
  - tidak memakai sensor suhu tubuh IR atau thermogun;
  - pengadaan 100 persen dari e-commerce dan distributor lokal Indonesia.
- **Batas klaim:**
  - Menurut WOAH, BROVER bukan alat biosekuriti dan bukan alat diagnosis otomatis, serta tidak meresepkan antibiotik.
  - Tanpa skor 0 sampai 100.
  - SEN0567 hanya tren kualitatif.
  - Preprint bukan bukti utama.
  - Kata *lebih cepat* atau *dini* baru boleh dipakai setelah selisihnya terukur saat pilot.
- **Angka dan sumber:**
  - Setiap angka baru wajib diverifikasi di sumber primer.
  - Tandai asumsi dengan label `ASUMSI TIM`.
  - Jangan mengarang data.
- **Berkas yang tidak boleh diubah:**
  - folder `Proposal TA/`, yang sudah di-gitignore;
  - `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md`, yang menjadi baseline.
- **README:** jangan edit manual. Selalu jalankan `python3 06_Project_Concept_BROVER/scripts/sync_readme.py`. Targetnya 0 tautan rusak.
- **Berkas yang tidak boleh di-commit:**
  - **PDF SmartEars di `08_Evaluasi_Proyek/`**, karena berhak cipta Elsevier;
  - folder `__pycache__`;
  - data pribadi.

  Folder `08_Evaluasi_Proyek/` berisi PDF itu, jadi **jangan pernah `git add` seluruh folder**. Tambahkan berkasnya satu per satu.
- **Git:**
  - Commit hanya atas perintah user.
  - Tulis entri baru di paling atas `HISTORY.md` sesuai templatnya.
  - Selaraskan `MEMORY.md` bila ada keputusan yang berubah.
  - Pakai **Conventional Commits**.
  - **Dilarang menyertakan `Co-Authored-By` atau atribusi AI, model, maupun asisten apa pun** di pesan commit, dokumentasi, dan kode.
- **Gaya penulisan:**
  - Istilah teknis bahasa Inggris dimiringkan.
  - Hindari jargon *wahana*, *UAV*, *patroli*, *LAN-First*, dan *derau lingkungan*.
  - Untuk berkas evaluasi bergaya ketat, jalankan `python3 -I 08_Evaluasi_Proyek/tools/check_style.py <berkas>` sampai TOTAL MASALAH 0.

## 6. Perintah yang Sering Dipakai
- **Render diagram:** `uv run --python 3.13 --with playwright==1.63.0 python 06_Project_Concept_BROVER/scripts/<skrip>.py`
- **Render Gambar 05 saja:** dari folder `scripts/`, jalankan `uv run --python 3.13 --with matplotlib --with numpy python -c "import generate_concept_visuals as g; g.make_fig5_hardware_power()"`. Jangan jalankan `generate_concept_visuals.py` secara penuh.
- **Ekspor markdown ke PDF:** `uv run --python 3.13 --with markdown --with playwright==1.63.0 python 08_Evaluasi_Proyek/tools/md_to_pdf.py <berkas.md>`
- **Uji tautan dua kali:** `python3 -I 08_Evaluasi_Proyek/tools/check_links.py <berkas.md> <hasil.json>`, lalu `make_table.py`. Catatan verifikasi untuk URL baru ditambahkan di `notes.py`.

## 7. Cara Bekerja dengan User
- Mulai dengan rencana singkat per pekerjaan. Minta persetujuan sebelum mengubah keputusan yang sudah dikunci di `MEMORY.md`.
- Setiap satu kelompok pekerjaan selesai, laporkan singkat apa yang berubah dan apa yang belum.
- Gunakan bahasa Indonesia yang lugas.
