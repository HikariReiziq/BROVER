# MEMORY: Single Source of Truth Proyek `BROVER` (Tim `Asprak`)

> **WAJIB DIBACA PERTAMA KALI** oleh setiap anggota tim maupun AI agent pada sesi baru sebelum membaca file lain atau melakukan perubahan di repository ini.  
> **ATURAN WAJIB:** Setiap perubahan pada repository **WAJIB** dicatat di [`HISTORY.md`](./HISTORY.md), dan apabila ada keputusan teknis/produk/tim yang berubah, **WAJIB** diperbarui juga pada file `MEMORY.md` ini.  
> **Pembaruan terakhir:** 28 November 2026, sinkronisasi keputusan final tim. Rincian perubahan dan sisa risiko ada di [`EVALUASI_ULANG_BROVER.md`](./08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md).

---

## 1. Identitas Proyek & Tim Terkunci

- **Kompetisi:** Hackathon Deep Tech UNJ 2026, Jalur Pangan **`D-FARM UNJ`**, *Focus Challenge* **Smart Poultry Production** (Pedoman hal. 2; portal menulis *Smart Egg Production*).
- **Judul Final Proyek:**
  > **`BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler`**
  > Kepanjangan merek `BROVER` = *Broiler Inspection & Health Rover*, hanya ditulis di bagian filosofi. Kata kunci produk adalah **skrining**; kata *deteksi dini*, *multi-modal*, dan *prediksi* tidak dipakai.
- **Nama Tim:** **Asprak** (`5/5` anggota: 4 mahasiswa Teknologi Informasi **ITS** + 1 dosen aktif Biologi **UNJ**; syarat minimal 1 dosen aktif UNJ **TERPENUHI**). Institusi di sampul proposal: **ITS dan UNJ**.
  1. **M. Hikari Reiziq Rakhmadinta**, **Ketua Tim**, *Hustler* (TI ITS): strategi produk, riset harga paket, kemitraan Dinas dan peternak mitra, BMC, *pitching*.
  2. **Ahmad Syauqi Reza**, *Hacker* (TI ITS): firmware `ESP32`, sensor di tiang dan dok, *carrier PCB*, Wi-Fi lokal, *backend* `Golang`.
  3. **Arya Bisma Putra Refman**, *Hacker* (TI ITS): pelatihan dan kuantisasi detektor feses Apache-2.0, set uji lokal, evaluasi akurasi per sumber foto, layanan inferensi BROVER Saku.
  4. **Aditya Reza Daffansyah**, *Hipster* (TI ITS): UI/UX dasbor `Next.js` PWA, halaman kendali rover, alur unggah foto HP, desain casing.
  5. **Dr. drh. Atin Supiyani, M.Si.**, Pakar Domain Veteriner (Dosen Biologi UNJ, Fisiologi & Kesehatan Hewan): label set uji lokal dan hitungan OPG, kamus gejala, aturan RH tropis dan ambang amonia, etika uji lapangan.
- **Data pribadi** (NIM/NIP/NIK, nomor HP, email, isi portofolio) **tidak disimpan di repositori**; diisi langsung di berkas docx proposal.
- **Filosofi Produk (`BROVER` = *Broiler* + *Rover*):** terinspirasi *NASA Planetary Rover*, kendaraan beroda pembawa instrumen yang masuk ke lingkungan kotor agar manusia tidak terlalu sering masuk. Sebutan utama: **`Rover Inspeksi`**.

---

## 2. Keputusan Teknis & Produk yang Sudah Dikunci (28 November 2026)

### A. Empat Fitur
1. **F1 `Rover Inspeksi`:** disetir lewat web di Wi-Fi lokal (`192.168.4.1`), rem *Dead-Man's Switch* `500 ms` di `ESP32`, kecepatan `0,07–0,1 m/s`, sensor jarak memperlambat laju, bumper lunak. Kamera `IMX291` pada servo `DS3218` dua posisi: depan `~0–15°` (FPV, kelak CV navigasi) dan bawah `~45°` (foto feses saat berhenti di titik zona) dengan LED `5000K CRI >90`. Foto HP menjadi cadangan BROVER Kandang dan sumber utama BROVER Saku.
2. **F2 Mikroklimat:** `SHT31` + `DFRobot SEN0567` di tiang setinggi ayam; status Normal/Waspada/Bahaya terhadap tabel umur `Cobb 500`/`Ross 308` dan THI. Saat tidak berkeliling, rover parkir di dok dalam kandang dan mencatat udara per menit (**mode stasiun**). `SEN0567` dilaporkan sebagai indikator tren kualitatif dan dikalibrasi terhadap alat acuan saat pilot.
3. **F3 CV Feses (satu-satunya AI):** satu detektor berlisensi **Apache-2.0** (`YOLOX`/`RT-DETR`), satu pipeline, dilatih dari data publik + foto rover. Diekspor ke **RKNN INT8** (`Orange Pi 3B`) dan **ONNX FP32** (server, ONNX Runtime CPU untuk BROVER Saku). PoC di `Raspberry Pi 4` (NCNN/ONNX). Set uji lokal memuat foto rover dan HP berpasangan; akurasi dilaporkan terpisah per sumber foto; BROVER Saku punya gerbang peluncuran. Inferensi langsung di HP adalah *future work*.
4. **F4 Dasbor `Next.js` PWA (tanpa skor 0–100):** standar umur, tren harian deplesi/pakan/air dari catatan ABK, ceklis gejala pernapasan dan catatan vaksin, triase 3 tombol (`Akan Saya Cek` / `Terlihat Normal` / `Laporkan ke Dokter Hewan`), laporan 1-klik WA/PDF, cuaca BMKG `adm4` dengan cadangan Open-Meteo.
- **Dihapus dari lingkup:** audio dan mikrofon (`INMP441`), Model #2 fisik ayam, deteksi bangkai, *node* sensor tetap, dan CO₂.
- **Operasi:** hari 0–6 mode stasiun; hari ke-7 sampai panen **2 putaran per hari** (pagi dan pukul 15.00–16.00); sesi dihentikan bila ayam tidak menyingkir, ada ayam terdorong jatuh atau terluka, atau suhu melewati ambang cekaman panas.
- ***Future work*:** CV navigasi, penjadwalan otomatis, inferensi di HP, modul CO₂, kamera termal, riset mikrofon tetap, aplikasi mobile native, modul rel gantung.

### B. Arsitektur & Biaya
- ***Edge-cloud*, luring dulu:** BROVER Kandang berjalan di Wi-Fi lokal + `SQLite WAL` tanpa internet. BROVER Saku mengantre foto di PWA saat tidak ada sinyal, lalu diproses di server pusat (`Golang` + `PostgreSQL` + ONNX Runtime; VPS kelas 2 vCPU / 4 GB sekitar Rp139 ribu/bulan dibagi banyak peternak). Jalur server Saku dibangun setelah inferensi rover berjalan.
- **Perangkat final:** `Orange Pi 3B` (RK3566, NPU 0,8 TOPS, RAM 4 GB, eMMC), `ESP32`, *custom carrier PCB* + *conformal coating*, `LiFePO₄` 4S 12,8 V 6 Ah + charger 14,6 V di dok, `4× JGB37-520`, `2× BTS7960`, `A02YYUW`, `FS304-SHT31`, `SEN0567`, `IMX291` + `DS3218`.
- **BOM 18 item (tanpa `INMP441`):** subtotal Rp5.395.000–9.620.000; titik eceran **Rp7.230.000**, grosir **Rp5.864.000**. **HPP unit:** eceran **Rp8.180.000**, grosir **Rp6.714.000**. Pengadaan 100% e-commerce dan distributor lokal Indonesia.

### C. Paket & Bisnis (Titik Impas, Tanpa ROI)
- **BROVER Saku:** Rp75.000/siklus; foto HP, tanpa perangkat, tanpa kontrak minimum. Titik impas peternak setara **2,1–3,3 ekor** ayam terselamatkan per siklus.
- **BROVER Kandang (langganan):** Rp750.000/siklus per kandang; kontrak minimal 6 siklus; perawatan oleh tim. Titik impas **21–33 ekor** per siklus. Balik modal unit bagi tim **14,1 siklus** (eceran) atau **11,6 siklus** (grosir).
- **Beli putus BROVER Kandang:** usulan **Rp11,5 juta/unit**, termasuk *cloud* 6 siklus pertama lalu iuran opsional Rp75.000/siklus. **Harga final masih menunggu konfirmasi tim.**
- Semua paket ditagih per siklus setelah panen (RHPP terbit 3–7 hari setelah panen). Nilai 1 ekor terselamatkan Rp22.700–36.200. Titik impas adalah **hipotesis pilot**, bukan klaim manfaat. Proyeksi ROI 5 tahun lama sudah dihapus.
- **Langganan berlaku per kandang.** Unit hanya dipindah setelah kontrak selesai, mengikuti protokol pemindahan unit (Bab 9.2 G concept, berbasis WOAH Bab 6.5). **Sewa antarfarm jangka pendek dilarang.**

### D. Status & Rencana
- **Status 28 November 2026:** rover Tahap 1 sudah dirakit dan lulus uji jalan lewat web serta rem 500 ms; dasbor web versi awal berjalan; model CV belum dilatih. **TKT sistem utuh 3**; gerak dan kendali web TKT 4; dasbor TKT 4. Target **TKT 6** akhir *bootcamp* (Feb 2027) dan **TKT 7** akhir program (Agu 2027).
- **Milestone:** M0 Nov 2026; M1 akhir Desember; M2 akhir Januari; M3 akhir Februari 2027; M4 Demo Day Maret 2027; M5 pilot Mei–Agustus 2027. Jadwal 12 minggu ada di Bab 9.7 concept dan Gambar 08b.
- **Rencana uji lapangan (belum kesepakatan tertulis):** Dinas Pangan dan Pertanian Kota Cimahi; peternakan broiler milik keluarga salah satu anggota tim (hubungan keluarga diungkap terbuka; tipe kandang dan skala menunggu konfirmasi). LoI ditargetkan April 2027.

---

## 3. *Hard Constraints* & Aturan Anti-*Overclaim* (WAJIB DIPATUHI)

1. **Hanya Jalur `D-FARM UNJ` (ayam broiler, *open* & *closed house*):** tolak topik pengolahan limbah/sampah (*waste-to-value*, kompos, biogas, maggot), abaikan `D-MARC`/PTML, dan **jangan** gunakan sensor tembak suhu tubuh (*thermogun/IR*).
2. **Pembedaan Veteriner (WOAH & masukan Medik Veteriner Dinas Peternakan):** `BROVER` adalah **alat inspeksi dan skrining gejala penyakit**, bukan alat biosekuriti dan bukan alat diagnosis otomatis; tidak pernah menampilkan resep atau dosis antibiotik.
3. **Anti-*Overclaim* Teknis & Ilmiah:**
   - *Preprint* (`arXiv`, `bioRxiv`, `medRxiv`, `SSRN`) tidak boleh menjadi bukti utama; gunakan jurnal *peer-reviewed* dan panduan resmi (`Cobb 500`, `Ross 308`, Kementan RI, WOAH).
   - Tidak ada skor kesehatan 0–100.
   - `DFRobot SEN0567` dilaporkan sebagai **indikator tren kualitatif NH₃**, bukan ppm sertifikasi lab.
   - Kata *lebih cepat* atau *dini* baru dipakai setelah selisih waktu antara peringatan sistem dan konfirmasi dokter hewan terukur saat pilot.
   - Operasi lantai mulai **hari ke-7 sampai panen**, kecepatan awal `0,07–0,1 m/s`, dengan kriteria berhenti sesi.
4. **Pengadaan 100% dari e-commerce dan distributor lokal Indonesia.**
5. **Bahasa Bersih:** hindari kata `"wahana"`, `"UAV"`, `"patroli"`, `"LAN-First"`, `"derau lingkungan"`, serta nama tim lama pada dokumen aktif.
6. **Aturan Git & Riwayat (MUTLAK):**
   - **WAJIB mencatat setiap perubahan repository di [`HISTORY.md`](./HISTORY.md)** (dan memperbarui `MEMORY.md` jika konteks/keputusan berubah).
   - **WAJIB menggunakan standar *Conventional Commits*** (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, dll.).
   - **DILARANG keras menyertakan trailer `Co-Authored-By` atau atribusi kontribusi AI/model/assistant mana pun** di dalam pesan commit, dokumentasi, maupun kode.

---

## 4. Peta Struktur Folder Repository

| Folder / File | Status | Isi & Fungsi |
| :--- | :---: | :--- |
| [`README.md`](./README.md) | **Aktif (GitHub Root)** | Salinan sinkron dari `PROJECT_CONCEPT_BROVER.md` dengan tautan relatif siap tampil di GitHub. **Jangan diedit manual**; jalankan `06_Project_Concept_BROVER/scripts/sync_readme.py`. |
| [`MEMORY.md`](./MEMORY.md) | **Aktif (Utama)** | Ringkasan konteks & keputusan terkunci (baca pertama kali). |
| [`HISTORY.md`](./HISTORY.md) | **Aktif (Wajib Log)** | Log kronologis seluruh perubahan repository. |
| [`.agent/rules/hackathon-context.md`](./.agent/rules/hackathon-context.md) | **Aktif (Rule)** | Aturan permanen AI agent untuk workspace ini. |
| [`00 Materi Sosialisasi/`](./00%20Materi%20Sosialisasi/) & PDF Pedoman di akar | **Arsip Resmi (Jangan Ubah)** | Dokumen asli panitia & mitra (PT ECG, PT Zara, Pedoman 2026). |
| `Template Proposal Peserta Kegiatan HackAthon 2026 -.docx` & `.docx.md` | **Arsip Resmi** | Template proposal panitia; versi markdown dipakai untuk membaca struktur. Pemetaan isinya ada di Bab 13 concept. |
| [`01_Context_Memory/`](./01_Context_Memory/) | **Aktif** | Profil Tim `Asprak`, aturan D-FARM & rubrik juri, profil PT Edura & PT Zara. |
| [`02_Problem_Research/`](./02_Problem_Research/) | **Referensi Riset** | Riset Top 5 masalah unggas Indonesia (`V3_TRANSPARAN.md` + `assets_v3/` + PDF). |
| [`03_Root_Cause_Analysis/`](./03_Root_Cause_Analysis/) | **Referensi Riset** | Bedah Ishikawa 6 dimensi, *5 Whys*, & *Vicious Cycle* penyakit + mikroklimat (+ PDF). |
| [`04_OpenSource_Solution_Discovery/`](./04_OpenSource_Solution_Discovery/) | **Referensi Riset** | Katalog terverifikasi proyek, GitHub, dataset, & model *open-source*. |
| [`05_Curated_Winners_And_Top_OpenSource/`](./05_Curated_Winners_And_Top_OpenSource/) | **Referensi Riset** | Audit kuantitatif & kurasi pemenang hackathon, repo, dan dataset terbaik. |
| [`06_Project_Concept_BROVER/`](./06_Project_Concept_BROVER/) | **Aktif (Utama)** | Concept lengkap **13 Bab** (`PROJECT_CONCEPT_BROVER.md`, termasuk Bab 13 pemetaan ke template proposal), gambar (`assets/`), skrip generator (`scripts/`), dan arsip gambar lama (`assets/history/`). |
| [`07_IoT_Hardware_Guide/`](./07_IoT_Hardware_Guide/) | **Aktif (Panduan 3 Tahap)** | Panduan Tahap 1 mobil kontrol web `192.168.4.1`, Tahap 2 purwarupa `Raspberry Pi 4` + servo kamera + tiang sensor + dok, dan Tahap 3 final `Orange Pi 3B` + `LiFePO₄` + *carrier PCB*. Foto komponen yang tidak dipakai lagi diarsipkan di `assets/history/`. |
| [`08_Evaluasi_Proyek/`](./08_Evaluasi_Proyek/) | **Aktif (Evaluasi)** | `EVALUASI_OBJEKTIF_BROVER.md` (baseline, jangan diubah), `PETA_FITUR_DAN_BUKTI_BROVER.md` (kartu fitur & bukti), `EVALUASI_ULANG_BROVER.md` (evaluasi setelah sinkronisasi 28 Nov 2026), prompt sesi agent (`PROMPT_*.md`), dan `tools/` (cek tautan, cek gaya, ekspor PDF). **PDF SmartEars di folder ini berhak cipta Elsevier dan tidak boleh di-commit**, jadi jangan `git add` seluruh folder. |

---

## 5. Status Progres & Langkah Berikutnya

- **Sudah Selesai:** riset masalah V3, RCA, kurasi *open-source*, judul final, tim 5/5, concept **13 Bab** yang sudah mencakup semua bagian template proposal (rumusan masalah, calon pengguna, komponen *deeptech*, status TKT, jadwal purwarupa 3 bulan, rencana pilot & hilirisasi, target luaran, 85 rujukan Vancouver), 13 gambar aktif termasuk `08b` jadwal 3 bulan dan `09` titik impas, panduan IoT 3 tahap, peta fitur & bukti, serta evaluasi ulang.
- **Tahap Berikutnya:**
  1. **Isi template proposal resmi dari concept**, mengikuti tabel pemetaan di **Bab 13** (batas kata per bagian, berkas wajib di luar proposal).
  2. Konfirmasi harga final beli putus dan detail peternakan mitra pilot.
  3. Kerjakan jadwal 12 minggu Bab 9.7: Rover Tahap 2, detektor Apache-2.0, set uji lokal berpasangan, dan dasbor.
  4. Untuk sesi agent berikutnya, pakai prompt [`PROMPT_ANTIGRAVITY_LANJUTAN_PROYEK_BROVER.md`](./08_Evaluasi_Proyek/PROMPT_ANTIGRAVITY_LANJUTAN_PROYEK_BROVER.md) di branch `docs/sinkronisasi-keputusan-28-nov-2026`.
