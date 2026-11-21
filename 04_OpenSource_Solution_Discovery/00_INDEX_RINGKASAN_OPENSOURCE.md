# 00 — INDEX & RINGKASAN EKSPLORASI SOLUSI OPEN-SOURCE (MASALAH #1 & #2 PETERNAKAN AYAM)

> **Status Tahapan:** Eksplorasi & Verifikasi Referensi Solusi *Open-Source* Publik — Tim MBOYZ, Hackathon Deep Tech UNJ 2026 (`D-FARM UNJ`, Challenge #1: Ayam Pedaging/Broiler & Petelur/Layer).  
> **Disiplin Tahapan:** Dokumen ini **100% murni katalog terverifikasi referensi *open-source* yang sudah ada di publik** agar dapat dicek secara manual oleh tim. **Tidak ada usulan konsep produk final, nama produk, maupun penguncian arsitektur Tim MBOYZ di sini.** Seluruh topik pengolahan limbah/sampah (*manure*, kompos, biogas, maggot) dan non-unggas telah dibuang mutlak.  
> **Proteksi Arsip:** Folder `00 Materi Sosialisasi/`, `01_Context_Memory/`, `02_Problem_Research/`, dan `03_Root_Cause_Analysis/` dipertahankan utuh tanpa perubahan.

---

## 1. Ringkasan Statistik per File & Sebaran Masalah (#1 vs #2)

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]` *Dihitung langsung dari seluruh entri terverifikasi pada file `01–05` dengan audit tautan otomatis `scripts/verify_links.py` (0 duplikasi lintas file).*

| No | File Katalog | Jumlah Entri Unik | Masalah #1 (Penyakit & Biosekuriti) | Masalah #2 (*Heat Stress* & Mikroklimat) | Gabungan `#1 & #2` | Tautan Unik Lolos Audit |
| :-: | :--- | :-: | :-: | :-: | :-: | :-: |
| 1 | [01_HACKATHON_DAN_MAKER_PROJECTS.md](./01_HACKATHON_DAN_MAKER_PROJECTS.md) | **26** | 10 | 8 | 8 | **61** |
| 2 | [02_GITHUB_REPOS_PENYAKIT_DAN_BIOSEKURITI.md](./02_GITHUB_REPOS_PENYAKIT_DAN_BIOSEKURITI.md) | **33** | 29 | 0 | 4 | **36** |
| 3 | [03_GITHUB_REPOS_HEAT_STRESS_DAN_MIKROKLIMAT.md](./03_GITHUB_REPOS_HEAT_STRESS_DAN_MIKROKLIMAT.md) | **27** | 0 | 25 | 2 | **27** |
| 4 | [04_DATASETS_MODELS_KAGGLE_HF_ROBOFLOW.md](./04_DATASETS_MODELS_KAGGLE_HF_ROBOFLOW.md) | **31** | 19 | 4 | 8 | **34** |
| 5 | [05_YOUTUBE_DEMO_OPENSOURCE.md](./05_YOUTUBE_DEMO_OPENSOURCE.md) | **9** | 8 | 1 | 0 | **21** |
| — | **TOTAL TERVERIFIKASI (DEDUPLIKASI PENUH)** | **126** | **66** | **38** | **22** | **179 / 179 (`100%`)** |

---

## 2. Sebaran Tautan Terverifikasi Lintas Platform

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]` *Mencakup seluruh tautan utama dan sub-tautan (kode, demo live, dataset/model, pitch deck, dan video demo) yang tercatat pada `scripts/verification_log.json`.*

| Kelompok Platform | Platform / Domain | Jumlah Tautan Unik | Metode Verifikasi |
| :--- | :--- | :-: | :--- |
| **Repositori Kode** | `github.com` (non-kosong, diverifikasi isi root) | **84** | `HTTP 200` + GitHub Contents API |
| **Video Demo & Tutorial** | `youtube.com` / `youtu.be` (`13` gabung di file `01` + `9` standalone di file `05`) | **22** | `HTTP 200` (YouTube Official oEmbed API) |
| **Dataset, Model & AI Space** | `huggingface.co` (Models, Datasets, Gradio/Docker Spaces) | **15** | `HTTP 200` + HF Hub API |
| **Dataset & Kompetisi** | `kaggle.com/datasets` | **10** | `HTTP 200` (Kaggle Official Public API) |
| **Dataset Ilmiah Terbuka** | `zenodo.org` (`5`) & `data.mendeley.com` (`4`) | **9** | `HTTP 200` |
| **Hackathon Showcase** | `devpost.com` (`11`) & `dorahacks.io` (`1`) | **12** | `HTTP 200` |
| **Hardware & Maker Hub** | `hackster.io` (`9`), `instructables.com` (`5`), `hackaday.io` (`2`), `projecthub.arduino.cc` (`1`) | **17** | `HTTP 200` |
| **Live Demo & Simulasi** | `vercel.app` (`5`), `netlify.app` (`1`), `onrender.com` (`1`), `wokwi.com` (`1`) | **8** | `HTTP 200` (bebas soft-404) |
| **Pitch Deck / Dokumen** | `canva.com` (`1`), `drive.google.com` (`1`) | **2** | `HTTP 200` |
| **Catatan Verifikasi** | Total agregat = `179` tautan unik (`0` duplikat antar-file `01–05`) | **179** | Log lengkap di [verification_log.json](./scripts/verification_log.json) |

---

## 3. Pemetaan Singkat terhadap 5 Akar Masalah Operasional RCA (`03_Root_Cause_Analysis/`)

`[SINTESIS ANALITIS AI AGENT — BERBASIS BUKTI TIER 1–3, PERLU VALIDASI PENELITI]` *Pemetaan cakupan referensi open-source terhadap 5 titik akar masalah operasional hasil Deep RCA (hanya sebagai peta navigasi pengecekan manual, bukan rekomendasi desain).*

| No | Akar Masalah Operasional RCA | Rujukan File Utama yang Relevan untuk Dicek Manual |
| :-: | :--- | :--- |
| **1** | **Titik Buta Mikroklimat Multi-Parameter (Suhu–RH–*Wind Chill*–NH₃) & Gradien Spasial** | File `03` (Bagian B–D: Fuzzy Mamdani NH₃, ML prediksi *exhaust fan*, optimasi energi kipas, Heat Index, ESP32-S3 NH₃+PM2.5), File `01` (*PoultryGuard AI*, *Project FarmSpeak*, *CoopCommand*), File `04` (Mendeley `m9nsjhtsph` 1.920 observasi NH₃/CO₂/Suhu/RH; Kaggle *humidex* & NH₃). |
| **2** | **Keterlambatan Deteksi Dini Gangguan Kesehatan Flok** | File `02` (Bagian A–C: CV feses mobile/web/XAI, CV CCTV mortalitas YOLOv8+U-Net, tracking multi-kamera Ghent Univ., audio vokalisasi `CVC-Fusion` & `ChickenLanguageDataset`, anomali *feed pecking*), File `03` (Bagian A: multimodal RGB+Thermal `chickenbot`, YOLO perilaku *closed house* RI), File `04` (Mendeley *SmartEars* 6.000 audio, Zenodo PCR feses & *ChickenVerse* 2026, Kaggle RGB+Thermal RI, HF YOLO11 *RUNNING* Space). |
| **3** | **Kebocoran Biosekuriti Eksternal & Jalur Transmisi Mekanis (`0,28/1,0`)** | File `01` (*FarmSeva*, *Fluviator* drone burung liar, *Smart Coop 2.0*, *$50 DIY AI Smart Coop*, *FlockWatch*), File `02` (Bagian D: *BioGuard Farm Hub* log pengunjung, *AgroArmor*), File `05` (otomasi pintu/akses kandang ESP32). |
| **4** | **Kerentanan Proteksi Vaksin & *Cold Chain* (2–8°C)** | File `01` (*VAXGUARD*, *Cold Chain Auditor* ESP32+DS18B20+MicroSD), File `02` (Bagian E: *Cold-Chain-Monitoring* PCB/GPS, *VacciTrack* live Vercel, *Peltier Vaccine Carrier* 2–8°C, *Pharma-ColdChain-IIoT*, *TelelBirds* pengingat vaksinasi). |
| **5** | **Kesenjangan Kapasitas, Pencatatan & Disiplin Operasional ABK** | File `01` (*Poultry-Hub*, *Poultry Pulse*), File `02` (Bagian D: *ChiRex*, *KawanKandang*, *Smart Poultry Platform* alur kerja kandang, *Hybrid RAG QA Assistant*), File `05` (tutorial *end-to-end* Indonesia & sistem manajemen flok). |

---

## 4. Catatan Transparansi Platform Minim / Terbatas

- **`taikai.network` (`0` proyek) & `lablab.ai` (`0` proyek):** Tidak ditemukan proyek *open-source* peternakan ayam/unggas yang relevan.
- **`hackathon.com` (`0` proyek individual):** Hanya ditemukan halaman pengumuman acara (*Wazihub IoT Hackathon* trek *Poultry*), tanpa repositori artefak proyek individual.
- **`universe.roboflow.com` (`HTTP 403` Cloudflare):** Seluruh 6 kandidat URL Roboflow Universe yang ditemukan di indeks web mengembalikan `HTTP 403` proteksi bot Cloudflare saat diakses skrip, sedangkan koneksi Chrome DevTools lokal (`DevToolsActivePort`) sedang tidak aktif sehingga belum dapat diverifikasi via browser. Oleh karena itu, kandidat Roboflow Universe **tidak dihitung dalam 126 entri terverifikasi** dan dicatat terpisah pada Bagian E [04_DATASETS_MODELS_KAGGLE_HF_ROBOFLOW.md](./04_DATASETS_MODELS_KAGGLE_HF_ROBOFLOW.md) untuk pengecekan manual di browser Anda.
- **Pembersihan Link Mati:** Repositori GitHub yang terbukti `404` atau kosong (tanpa kode/file selain `README.md`/`LICENSE`) telah dibuang dari daftar final.

---

## 5. Cara Menjalankan Ulang Audit Tautan

```bash
python3 04_OpenSource_Solution_Discovery/scripts/verify_links.py
```

Hasil audit mentah (URL, kode status HTTP, URL akhir, metode verifikasi, dan *timestamp* UTC) tersimpan di [scripts/verification_log.json](./scripts/verification_log.json).
