# 00 — RINGKASAN KURASI KETAT, AUDIT ELIMINASI & TOP 15 WAJIB DICEK PERTAMA

> **Status Tahapan:** Audit Kuantitatif & Kurasi Ketat Referensi *Open-Source* Berkualitas Tinggi — Tim MBOYZ, Hackathon Deep Tech UNJ 2026 (`D-FARM UNJ`, Challenge #1: Ayam Pedaging/Broiler & Petelur/Layer).  
> **Disiplin Tahapan:** Dokumen ini **100% murni laporan audit metrik aktual dan kurasi referensi publik** untuk dicek secara manual. **Tidak ada usulan konsep produk, nama produk, atau arsitektur final Tim MBOYZ.**  
> **Proteksi Arsip:** Folder `00 Materi Sosialisasi/`, `01_Context_Memory/`, `02_Problem_Research/`, `03_Root_Cause_Analysis/`, serta arsip mentah `04_OpenSource_Solution_Discovery/` dipertahankan utuh tanpa modifikasi.

---

## 1. Statistik Sebelum (`04/`) vs Sesudah Kurasi Ketat (`05/`)

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]` *Seluruh angka dihitung secara terprogram melalui [audit_quality_and_links.py](./scripts/audit_quality_and_links.py) dan tercatat di [quality_audit_log.json](./scripts/quality_audit_log.json) (`94/94` tautan unik lolos `HTTP 200`, `0` gagal, `0` duplikasi URL lintas file).*

### A. Ringkasan Hasil Kurasi per File di `05_Curated_Winners_And_Top_OpenSource/`

| No | File Kurasi | Total Entri | Tier S (*Winners*) | Tier A (*High-Traction*) | Tier B (*Research/Lab/RI*) | Masalah #1 | Masalah #2 | `#1 & #2` | Dipertahankan dari `04/` | Temuan Baru Fase B |
| :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | [01_VERIFIED_HACKATHON_CONTEST_WINNERS.md](./01_VERIFIED_HACKATHON_CONTEST_WINNERS.md) | **10** | **10** | 0 | 0 | 4 | 0 | 6 | 4 | **+6** |
| 2 | [02_TOP_GITHUB_HIGH_TRACTION_DAN_RISET.md](./02_TOP_GITHUB_HIGH_TRACTION_DAN_RISET.md) | **29** | 0 | **21** | **8** | 22 | 1 | 6 | 14 | **+15** |
| 3 | [03_TOP_DATASETS_MODELS_SPACES_DAN_VIDEO.md](./03_TOP_DATASETS_MODELS_SPACES_DAN_VIDEO.md) | **26** | 0 | **18** | **8** | 15 | 2 | 9 | 20 | **+6** |
| — | **TOTAL TERKURASI KETAT (`05/`)** | **65** | **10** | **39** | **16** | **41** | **3** | **21** | **38** | **+27** |

### B. Laporan Transparan Audit Eliminasi terhadap 126 Entri Lama (`04_OpenSource_Solution_Discovery/`)

| File Sumber Lama (`04/`) | Entri Awal | Lolos ke `05/` | Dieliminasi | Alasan Utama Eliminasi |
| :--- | :-: | :-: | :-: | :--- |
| `01_HACKATHON_DAN_MAKER_PROJECTS.md` | 26 | 6 | **20** | 8 proyek Devpost & 1 DoraHacks terbukti **bukan juara** (`winner=False`); 11 proyek Hackster/Instructables/Hackaday tidak memiliki status juara maupun traksi Tier A (`≥5.000 views` atau `≥25 likes`). |
| `02_GITHUB_REPOS_PENYAKIT_DAN_BIOSEKURITI.md` | 33 | 7 | **26** | Repo tugas kuliah/prototipe awal dengan `<15 Stars` & `<5 Forks` tanpa afiliasi jurnal *peer-reviewed* atau lab universitas. |
| `03_GITHUB_REPOS_HEAT_STRESS_DAN_MIKROKLIMAT.md` | 27 | 3 | **24** | Repo IoT dasar/simulasi dengan `0–6 Stars` & `<5 Forks` tanpa bukti publikasi ilmiah atau traksi komunitas. |
| `04_DATASETS_MODELS_KAGGLE_HF_ROBOFLOW.md` | 31 | 17 | **14** | Dataset Kaggle `<10 Upvotes` & `<500 Downloads` (tanpa DOI), model/dataset HF `<100 Downloads` & `<5 Likes`, serta HF Spaces berstatus `SLEEPING`. |
| `05_YOUTUBE_DEMO_OPENSOURCE.md` | 9 | 5 | **4** | Video tutorial standalone `<5.000 Views` tanpa repositori Tier A. *(Catatan: 2 video Tier A — Krish Naik & esp32-coop — digabungkan langsung ke entri repositorinya di file `02`).* |
| **TOTAL AUDIT ARSIP LAMA (`04/`)** | **126** | **38 (`30,2%`)** | **88 (`69,8%`)** | **+27 entri baru berkualitas tinggi** ditemukan di Fase B → total final **`65` entri terkurasi (`94/94` URL `HTTP 200`)**. |

> **Catatan Pembersihan *False Positive* Fase B:** Selama pencarian agresif bintang tinggi di GitHub dan pemenang Devpost/Instructables, beberapa kandidat *false positive* berhasil dideteksi dari pemeriksaan README/HTML dan **dibuang mutlak**, antara lain: `0xriyadh/chicken-coop` (31⭐ — ternyata aplikasi cek ruang kelas universitas), `RuoyuChen10/Image_weighing` (37⭐ — khusus karkas itik *White Pekin Duck*, bukan ayam), `microsoft/poultry-cafos` (40⭐ — pemetaan satelit lokasi gudang, bukan on-farm #1/#2), `Pyteak` (tidak memiliki *badge Winner* resmi di Devpost & repo GitHub `404`), serta `Sift` (pelacak penarikan daging ritel FSIS, bukan manajemen kandang).

---

## 2. Top 15 Paling Wajib Dicek Pertama

`[SINTESIS ANALITIS AI AGENT — BERBASIS BUKTI TIER 1–3, PERLU VALIDASI PENELITI]` *Daftar prioritas pengecekan manual yang disusun berdasarkan status pemenang lomba terverifikasi (Tier S), traksi adopsi tertinggi (Tier A), atau kedalaman riset/konteks Indonesia (Tier B) terhadap 5 Akar Masalah RCA. Bukan rekomendasi konsep produk final Tim MBOYZ.*

| Peringkat | Nama Proyek / Repo / Dataset | Tier | Masalah | Bukti Kualitas / Traksi Aktual | Alasan Bernilai Tinggi untuk Dicek Manual | Lokasi & Tautan Langsung |
| :-: | :--- | :-: | :-: | :--- | :--- | :--- |
| **1** | **Henomaly** | **TIER S** | `#1 & #2` | 🏆 Winner QNX & Photon Track @ *AI Hackathon 2026 by LA Hacks* | Edge-AI Raspberry Pi + YOLO memantau perilaku *panting*/inaktivitas & feses terhadap *baseline* kandang + kode GitHub aktif. | File `01` — [Devpost](https://devpost.com/software/holy-crap) \| [GitHub](https://github.com/RishitRai/Henomaly) |
| **2** | **PoultryGuard AI (`SIRAGU`)** | **TIER S** | `#1 & #2` | 🏆 Winner Excellence in Innovation @ *AnimalHack 2026* | IoT ESP32 pemantau lingkungan + auto-deteksi *sensor fault/drift* + alert Telegram + live Netlify & GitHub. | File `01` — [Devpost](https://devpost.com/software/poultryguard-ai-node-health-hub-with-real-time-diagnostics) \| [GitHub](https://github.com/skarthik2745/SIRAGU-Poultry-Monitoring) |
| **3** | **Project FarmSpeak** | **TIER S** | `#1 & #2` | 🏆 Winner First Place @ *Africa Deep Tech Challenge 2025* | Arsitektur solar-IoT SHT31 + MQ-135 (NH₃/CO₂) untuk kontrol iklim otomatis & peringatan penyakit di iklim tropis/berkembang. | File `01` — [Devpost](https://devpost.com/software/project-farmspeak) \| [YouTube](https://www.youtube.com/watch?v=WQw-_dekpuA) |
| **4** | **Smart Coop 2.0** | **TIER S** | `#1 & #2` | 🏆 Contest Winner @ *Hackster Arduino UNO Q* \| 👁 8.185 Views | Edge AI ONNX (predator/telur) + audio distress + PCB kustom + kode & model ONNX lengkap di GitHub. | File `01` — [Arduino Hub](https://projecthub.arduino.cc/shebinjosejacob/smart-coop-20-787f34) \| [GitHub](https://github.com/CodersCafeTech/Smart-Coop-V2) |
| **5** | **SecuriVax** | **TIER S** | `#1` *(Cold Chain)* | 🏆 Best Overall Hack @ *HopHacks Fall 2026* \| ⭐ 3 | Referensi pemenang umum untuk pelacakan integritas *cold chain* vaksin 2–8°C beserta kode GitHub & demo video. | File `01` — [Devpost](https://devpost.com/software/xxxx-4bm0we) \| [GitHub](https://github.com/SoumilBhandari/SecuriVax) |
| **6** | **AWS IoT Vaccine Carrier Cold Box** | **TIER S** | `#1` *(Cold Chain)* | 🏆 Winners Gallery @ *Reinventing Healthy Spaces with AWS* | Implementasi *hardware* sensor Sub-1 GHz + AWS IoT untuk kotak pembawa vaksin lapangan (MIT License). | File `01` — [Hackster](https://www.hackster.io/mtrobregado/aws-iot-vaccine-carrier-cold-box-9c7fba) \| [GitHub](https://github.com/mtrobregado/Vaccine-Carrier-Cold-Box-Temperature-Monitoring) |
| **7** | **CoopCommand** | **TIER A** | `#1 & #2` | ⭐ 42 Stars \| 🍴 8 Forks \| GPL-3.0 \| 👁 2.900+ Views | *Open-hardware* paling matang (PCB, BOM, DHT22, DS18B20 air minum, relai kipas/pemanas, ESP32-CAM). | File `02` — [GitHub](https://github.com/hms-11/CoopCommand) \| [Hackaday](https://hackaday.io/project/179275-coopcommand) |
| **8** | **Multi-View Broiler Tracking (`decide-ugent`)** | **TIER B** | `#1` | 📄 *Comput. Electron. Agric.* Q1 (2025) — Ghent Univ. \| ⭐ 5 | Kode riset Q1 mutakhir untuk pelacakan individu broiler multi-kamera guna deteksi dini kelumpuhan/penyakit. | File `02` — [GitHub](https://github.com/decide-ugent/multi-view-broiler-tracking) |
| **9** | **ChickenBot Multimodal Pipeline (`417steven`)** | **TIER B** | `#1 & #2` | 📄 Multimodal RGB + Thermal + Env Time-Lag Pipeline | Contoh arsitektur paling lengkap yang mengorelasikan kamera RGB+Thermal (dispersi & suhu inti) dengan Suhu, RH, NH₃, CO₂ & log HVAC. | File `02` — [GitHub](https://github.com/417steven/chickenbot) |
| **10** | **Broiler Carcass Candidate Detection (`jeongrubin`)** | **TIER B** | `#1` | 📄 Paper Pipeline (YOLOv8s + U-Net + BiLSTM 120m) | Memecahkan masalah klasik CCTV kandang (membedakan ayam tidur vs bangkai mati menggunakan sekuens masker 120 menit). | File `02` — [GitHub](https://github.com/jeongrubin/broiler-carcass-candidate-detection) |
| **11** | **PCR-Annotated Poultry Disease Dataset (`Zenodo 5801834`)** | **TIER A** | `#1` | 📥 36.265 Downloads \| 👁 25.005 Views | Dataset *gold-standard* berlabel PCR (Coccidiosis, Salmonella, NCD, Healthy) lengkap anotasi YOLO & segmentasi. | File `03` — [Zenodo](https://zenodo.org/records/5801834) |
| **12** | **Chicken Health & Behavior Multimodal (`IceKhoffi`)** | **TIER A** | `#1 & #2` | 📥 723 Downloads \| ♥ 4 Likes \| **Bahasa ID & EN** | Dataset multimodal langka (visual *object detection* + audio vokalisasi) bertag Indonesia & Inggris untuk deteksi dini penyakit/perilaku. | File `03` — [Hugging Face](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) |
| **13** | **SmartEars Respiratory Audio (`Mendeley dy6gtvt4mk`)** | **TIER B** | `#1` | 📄 Mendeley DOI `10.17632/dy6gtvt4mk.2` \| 6.000 Segmen | Dataset audio kandang komersial nyata (termasuk kelas derau kipas ventilasi) untuk deteksi ngorok/penyakit pernapasan. | File `03` — [Mendeley Data](https://data.mendeley.com/datasets/dy6gtvt4mk/2) |
| **14** | **Evet-Africa Poultry Disease Ecosystem** | **TIER A** | `#1` | 📥 1.163 Downloads \| 🟢 **Live Gradio Space (`RUNNING`)** | Bisa langsung diuji coba secara *live* di browser bersama bobot YOLO11 dan dataset publiknya. | File `03` — [HF Space](https://huggingface.co/spaces/Evet-Africa/poultry-disease-detector) \| [Dataset](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) |
| **15** | **Environmental Monitoring Broiler (`Mendeley m9nsjhtsph`)** | **TIER B** | `#2` | 📄 Mendeley DOI `10.17632/m9nsjhtsph.1` \| 1.920 Observasi | Dataset telemetri multi-parameter (Suhu dalam/luar, RH, NH₃, CO₂, cahaya, umur) siap pakai untuk pemodelan mikroklimat. | File `03` — [Mendeley Data](https://data.mendeley.com/datasets/m9nsjhtsph/1) |

---

## 3. Reproduksibilitas Audit

Untuk memverifikasi ulang seluruh tautan (`HTTP 200`) serta metrik kualitas aktual (*Winner badge*, *Stars*, *Forks*, *Downloads*, *Votes*):

```bash
python3 05_Curated_Winners_And_Top_OpenSource/scripts/audit_quality_and_links.py
```

Bukti mentah hasil audit tersimpan di [scripts/quality_audit_log.json](./scripts/quality_audit_log.json).
