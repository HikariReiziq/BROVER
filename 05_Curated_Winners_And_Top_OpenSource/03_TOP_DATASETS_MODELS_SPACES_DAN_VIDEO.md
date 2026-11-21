# 03 — TOP DATASETS, PRETRAINED MODELS, AI SPACES & YOUTUBE OPEN-SOURCE (*TIER A & B*)

> **Ambang Kelulusan Ketat:**
> - **Kaggle (Tier A):** `≥ 10 Upvotes` ATAU `≥ 500 Downloads` *(plus Tier B dataset multimodal Indonesia)*.
> - **Hugging Face (Tier A):** `≥ 100 Downloads` ATAU `≥ 5 Likes` ATAU Space aktif **`RUNNING`**.
> - **Zenodo & Mendeley Data (Tier A/B):** Dataset riset terbuka dengan DOI permanen, traksi unduhan tinggi, atau terhubung langsung ke publikasi ilmiah *peer-reviewed* / konsorsium riset.
> - **YouTube Standalone (Tier A):** `≥ 5.000 Views` + tautan kode/skematik aktif *(video yang sudah dipasangkan dengan proyek di file `01` atau `02` tidak diulang di sini)*.  
> `[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

---

## A. Top Kaggle Datasets (`kaggle.com/datasets`, Urut Unduhan & *Upvotes* Tertinggi)

- [ ] **Chicken Disease Image Classification (`allandclive/chicken-disease-1`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses — 4 Kelas PCR, 266 MB]`
  - **Bukti Kualitas / Traksi:** `📥 9.211 Downloads | 👍 85 Upvotes | 👁 42.313 Views` *(Kaggle Public API)*
  - **Ringkasan:** Dataset citra feses ayam paling banyak digunakan di Kaggle untuk klasifikasi 4 kelas (Coccidiosis, Salmonella, Newcastle Disease, Healthy) sebagai *benchmark* standar pelatihan CNN/ViT.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/allandclive/chicken-disease-1) *(HTTP 200 via Kaggle Public API)*

- [ ] **Poultry Diseases Detection (`kausthubkannan/poultry-diseases-detection`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses Skala Besar — 8,08 GB]`
  - **Bukti Kualitas / Traksi:** `📥 4.476 Downloads | 👍 45 Upvotes | 👁 16.727 Views` *(Kaggle Public API)*
  - **Ringkasan:** Koleksi citra feses ayam beresolusi tinggi berukuran ~8 GB yang luas dipakai untuk pelatihan model *transfer learning* deteksi 3 penyakit pencernaan utama unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/kausthubkannan/poultry-diseases-detection) *(HTTP 200 via Kaggle Public API)*

- [ ] **Poultry Pathology Visual Dataset (`chandrashekarnatesh/poultry-diseases`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Patologi Unggas — 12,88 GB]`
  - **Bukti Kualitas / Traksi:** `📥 4.330 Downloads | 👍 40 Upvotes | 👁 16.247 Views` *(Kaggle Public API)*
  - **Ringkasan:** Dataset visual patologi penyakit unggas terbesar di Kaggle (~12,9 GB) untuk membangun klasifier diagnosis visual penyakit ayam berakurasi tinggi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases) *(HTTP 200 via Kaggle Public API)*

- [ ] **Environmental Effect on Egg Production (`faysal1998/environmental-effect-on-egg-production`)** — `[TIER A]` `[Masalah #2]` `[Dataset Tabular Mikroklimat & Produksi Telur]`
  - **Bukti Kualitas / Traksi:** `📥 984 Downloads | 👍 10 Upvotes | 👁 5.132 Views` *(Kaggle Public API)*
  - **Ringkasan:** Dataset tabular terbuka yang menghubungkan variabel kondisi lingkungan kandang dengan capaian produksi telur ayam petelur (*layer*).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/faysal1998/environmental-effect-on-egg-production) *(HTTP 200 via Kaggle Public API)*

- [ ] **Chicken Disease Dataset Split (`efoeetienneblavo/chicken-disease-dataset`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses Siap Latih — Train/Val/Test]`
  - **Bukti Kualitas / Traksi:** `📥 679 Downloads | 👍 6 Upvotes | 👁 4.188 Views` *(Kaggle Public API)*
  - **Ringkasan:** Versi terstruktur (*train/val/test split*) dari dataset citra feses penyakit ayam berukuran 266 MB yang siap langsung digunakan dalam pipeline PyTorch/TensorFlow.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/efoeetienneblavo/chicken-disease-dataset) *(HTTP 200 via Kaggle Public API)*

- [ ] **E. coli Data in Poultry & Dairy (`alamshihab075/e-coli-data-poultry-and-dairy-in-bangladesh`)** — `[TIER A]` `[Masalah #1]` `[Dataset Isolat E. coli & Profil Resistensi Unggas]`
  - **Bukti Kualitas / Traksi:** `👍 23 Upvotes | 📥 60 Downloads | 👁 520 Views` *(Kaggle Public API)*
  - **Ringkasan:** Dataset observasi isolat bakteri *Escherichia coli* (penyebab *Colibacillosis* sekunder pada ayam) beserta variabel sumber isolat dan profil kerentanan/resistensi antibiotik.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/alamshihab075/e-coli-data-poultry-and-dairy-in-bangladesh) *(HTTP 200 via Kaggle Public API)*

- [ ] **Chicken Health Images Dataset — RGB & Thermal (`ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal`)** — `[TIER B]` `[#1 & #2]` `[Dataset Multimodal RGB + Thermal IR — Kontributor Indonesia]`
  - **Bukti Kualitas / Traksi:** `📄 Curated Indonesian Multimodal Dataset (CC0 Public Domain)` | `📥 265 Downloads | 👍 2 Upvotes` *(Kaggle Public API)*
  - **Ringkasan:** Dataset dual-spektrum (RGB + kamera termal inframerah) karya kontributor Indonesia (Eko Supriyanto) berlabel *Healthy*, *Sick*, dan *Dead* untuk riset deteksi demam, *heat stress*, dan mortalitas unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) *(HTTP 200 via Kaggle Public API)*

---

## B. Top Hugging Face Models, Datasets & Live Space (`huggingface.co`, Urut Unduhan Tertinggi)

- [ ] **DETR ResNet-50 Chicken Object Detector (`joe611/chickens`)** — `[TIER A]` `[#1 & #2]` `[Pretrained Model / facebook/detr-resnet-50 Apache-2.0]`
  - **Bukti Kualitas / Traksi:** `📥 2.247 Downloads | Apache-2.0 License` *(Hugging Face Hub API)*
  - **Ringkasan:** Model deteksi objek ayam berbasis Transformer (`facebook/detr-resnet-50`) dengan jumlah unduhan tertinggi di Hugging Face yang dapat langsung digunakan atau di-*fine-tune* untuk deteksi & pelacakan populasi flok.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/joe611/chickens) *(HTTP 200)*

- [ ] **Evet-Africa Poultry Disease Ecosystem (`Evet-Africa/poultry-disease-detector`)** — `[TIER A]` `[Masalah #1]` `[YOLO11 Model + Dataset + Live RUNNING Gradio Space]`
  - **Bukti Kualitas / Traksi:** `📥 1.163 Downloads (Dataset) | 🟢 Live Gradio Space (RUNNING) | AGPL-3.0 License` *(Hugging Face Hub API)*
  - **Ringkasan:** Ekosistem terbuka lengkap mencakup dataset penyakit ayam, bobot model deteksi objek YOLO11, dan aplikasi web interaktif Gradio Space yang berstatus aktif (`RUNNING`) untuk uji inferensi langsung.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) *(HTTP 200)*
    - Dataset / Model: [Hugging Face Model](https://huggingface.co/Evet-Africa/poultry-disease-detector) *(HTTP 200)*
    - Demo Live: [Hugging Face Space (RUNNING)](https://huggingface.co/spaces/Evet-Africa/poultry-disease-detector) *(HTTP 200)*

- [ ] **Chicken Health & Behavior Multimodal Dataset (`IceKhoffi/chicken-health-behavior-multimodal`)** — `[TIER A]` `[#1 & #2]` `[Dataset Multimodal Vision + Audio — Bahasa Indonesia & Inggris]`
  - **Bukti Kualitas / Traksi:** `📥 723 Downloads | ♥ 4 Likes | Languages: ID & EN` *(Hugging Face Hub API)*
  - **Ringkasan:** Dataset multimodal langka bertag bahasa Indonesia & Inggris yang menggabungkan data visual (*object-detection*) dan audio (*vocalization-analysis*) untuk deteksi dini penyakit serta analisis perilaku ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) *(HTTP 200)*

- [ ] **Chicken Feces Baseline Clean (`iagovarela/poultry-disease-dataset`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses Terkurasi]`
  - **Bukti Kualitas / Traksi:** `📥 562 Downloads` *(Hugging Face Hub API)*
  - **Ringkasan:** Dataset citra feses ayam bersih dalam format Hugging Face untuk melatih model *baseline* klasifikasi penyakit pencernaan unggas tanpa perlu pembersihan manual berat.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/iagovarela/poultry-disease-dataset) *(HTTP 200)*

- [ ] **Chicken Counting Density Map (`ioaihsc/Task2_Chicken_Counting_Train2`)** — `[TIER A]` `[#1 & #2]` `[Dataset CV Density-Map Penghitungan & Kerumunan Ayam]`
  - **Bukti Kualitas / Traksi:** `📥 338 Downloads` *(Hugging Face Hub API)*
  - **Ringkasan:** Dataset *computer vision* berisi pasangan citra kandang dan *density map* 2D untuk melatih model estimasi kepadatan dan pola berkerumun/menyebar (*huddling/crowding*) ayam pada flok padat.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/ioaihsc/Task2_Chicken_Counting_Train2) *(HTTP 200)*

- [ ] **Poultry Fecal Federated Learning (`Dianyo/poultry-fecal-fl`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses Format Parquet / Federated Learning]`
  - **Bukti Kualitas / Traksi:** `📥 235 Downloads` *(Hugging Face Hub API)*
  - **Ringkasan:** Dataset citra feses ayam terpartisi berformat Parquet yang disiapkan untuk skenario pelatihan model kolaboratif lintas peternakan (*Federated Learning*) tanpa membagikan data mentah kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/Dianyo/poultry-fecal-fl) *(HTTP 200)*

- [ ] **PoultryVision (`Williamsanderson/PoultryVision`)** — `[TIER A]` `[Masalah #1]` `[Pretrained Model / YOLOv11 Ultralytics]`
  - **Bukti Kualitas / Traksi:** `📥 171 Downloads | ♥ 1 Like | AGPL-3.0 License` *(Hugging Face Hub API)*
  - **Ringkasan:** Bobot model *pretrained* Ultralytics YOLOv11 khusus deteksi objek unggas yang siap digunakan sebagai titik awal *fine-tuning* sistem kamera kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/Williamsanderson/PoultryVision) *(HTTP 200)*

---

## C. Top Scientific & Peer-Reviewed Open Datasets (`zenodo.org` & `data.mendeley.com`)

- [ ] **PCR-Annotated Poultry Disease Diagnostics Dataset (`Zenodo 5801834`)** — `[TIER A]` `[Masalah #1]` `[Dataset CV Feses Terverifikasi PCR + Anotasi YOLO]`
  - **Bukti Kualitas / Traksi:** `📥 36.265 Downloads | 👁 25.005 Views | DOI: 10.5281/zenodo.5801834` *(Zenodo API)*
  - **Ringkasan:** Dataset rujukan ilmiah terpopuler berisi ribuan citra feses ayam terverifikasi uji PCR (*Coccidiosis, Salmonella, Newcastle Disease, Healthy*) lengkap dengan anotasi deteksi objek YOLO dan segmentasi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo Record 5801834](https://zenodo.org/records/5801834) *(HTTP 200)*

- [ ] **ChickenVerse: Detection, Segmentation & Behavior Recognition (2026)** — `[TIER A]` `[#1 & #2]` `[Dataset CV Multi-Task Deteksi, Segmentasi & Perilaku]`
  - **Bukti Kualitas / Traksi:** `📥 3.228 Downloads | 👁 725 Views | DOI: 10.5281/zenodo.20672799` *(Zenodo API)*
  - **Ringkasan:** Dataset riset terbuka mutakhir (2026) untuk pelatihan deteksi objek, segmentasi instans, dan pengenalan perilaku ayam secara komprehensif pada kondisi kandang nyata.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/20672799) *(HTTP 200)*

- [ ] **NESTLER — Poultry Behaviour Analytics Detection Dataset** — `[TIER B]` `[#1 & #2]` `[Dataset Video Perilaku Unggas — EU Horizon Grant 101060762]`
  - **Bukti Kualitas / Traksi:** `📄 Official EU Horizon One Health Research Dataset (Grant No. 101060762)` | `📥 1.136 Downloads | 👁 962 Views | DOI: 10.5281/zenodo.20924893`
  - **Ringkasan:** Dataset video perilaku unggas dari konsorsium riset EU-Africa *One Health* (NESTLER) untuk pengembangan algoritma analitik perilaku dan pemantauan kesejahteraan/kesehatan ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/20924893) *(HTTP 200)*

- [ ] **ChickenSense Sound Feed-Intake Monitoring Dataset** — `[TIER B]` `[Masalah #1]` `[Dataset Audio AI Pemantauan Konsumsi Pakan Real-Time]`
  - **Bukti Kualitas / Traksi:** `📄 Official Research Dataset (ChickenSense)` | `📥 374 Downloads | 👁 690 Views | DOI: 10.5281/zenodo.8212853`
  - **Ringkasan:** Dataset akustik terbuka untuk mendeteksi dan mengukur aktivitas makan (*feed intake*) unggas secara *real-time* menggunakan mikrofon berbiaya rendah (indikator dini penurunan nafsu makan akibat penyakit atau *heat stress*).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/8212853) *(HTTP 200)*

- [ ] **Chick Call Dataset (`EUSIPCO 2022`)** — `[TIER B]` `[#1 & #2]` `[Dataset Audio Vokalisasi Anak Ayam Fase Brooding]`
  - **Bukti Kualitas / Traksi:** `📄 Official Paper Dataset: EUSIPCO 2022` | `📥 207 Downloads | 👁 529 Views | DOI: 10.5281/zenodo.6655837`
  - **Ringkasan:** Dataset panggilan vokal anak ayam (*chick calls*) berlabel untuk pengembangan model *signal processing* / *deep learning* pendeteksi stres termal atau ketidaknyamanan pada fase awal pemeliharaan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/6655837) *(HTTP 200)*

- [ ] **SmartEars: Poultry Respiratory Monitoring Audio Dataset** — `[TIER B]` `[Masalah #1]` `[Dataset Audio Pernapasan Komersial — 6.000 Segmen 5 Detik]`
  - **Bukti Kualitas / Traksi:** `📄 Official Mendeley Research Dataset | DOI: 10.17632/dy6gtvt4mk.2`
  - **Ringkasan:** Kumpulan 6.000 segmen audio kandang komersial berdurasi 5 detik yang telah dibersihkan dan dilabeli (*Healthy, Sick, None/derau kipas*) khusus untuk klasifikasi spektrogram penyakit pernapasan ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/dy6gtvt4mk/2) *(HTTP 200)*

- [ ] **Poultry Vocalization Signal Dataset for Early Disease Detection** — `[TIER B]` `[Masalah #1]` `[Dataset Audio .wav Penyakit Pernapasan — 65 Hari]`
  - **Bukti Kualitas / Traksi:** `📄 Official Mendeley Research Dataset | DOI: 10.17632/zp4nf2dxbh.1`
  - **Ringkasan:** Rekaman 346 file sinyal audio `.wav` (*healthy, noise, unhealthy*) hasil pemantauan akustik longitudinal selama 65 hari pada flok ayam yang terserang penyakit pernapasan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/zp4nf2dxbh/1) *(HTTP 200)*

- [ ] **Sick and Healthy: Thermal Images of Broiler Avian 48** — `[TIER B]` `[#1 & #2]` `[Dataset Citra Termal Inframerah — 600 Ekor Broiler]`
  - **Bukti Kualitas / Traksi:** `📄 Official Mendeley Research Dataset | DOI: 10.17632/vwbb4dc9b7.1`
  - **Ringkasan:** Koleksi citra termal inframerah dari 600 ekor ayam broiler Cobb Avian 48 (kondisi sehat vs sakit lintas umur dan sudut pengambilan) untuk mendeteksi demam, infeksi, maupun cekaman panas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/vwbb4dc9b7/1) *(HTTP 200)*

- [ ] **Environmental Monitoring of Broiler Chickens During Summer and Winter** — `[TIER B]` `[Masalah #2]` `[Dataset Sensor Mikroklimat — 1.920 Observasi NH₃/CO₂/Suhu/RH]`
  - **Bukti Kualitas / Traksi:** `📄 Official Mendeley Research Dataset | DOI: 10.17632/m9nsjhtsph.1`
  - **Ringkasan:** Dataset sensor lingkungan kandang broiler berisi 1.920 observasi lengkap meliputi suhu dalam/luar, kelembapan relatif, amonia (`NH₃`), `CO₂`, pencahayaan, dan umur ayam untuk pelatihan model prediktif mikroklimat.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/m9nsjhtsph/1) *(HTTP 200)*

---

## D. Top Standalone YouTube & Maker Open-Source (`≥ 5.000 Views` + Kode Aktif)

> **Catatan Anti-Duplikasi:** Video tutorial populer **Krish Naik** (`276.228 views` → `krishnaik06/Chicken-Disease-Classification-Projects`, ⭐90) dan **esp32-coop** (`1.238 views` → `ESP32-COOP-DOC`, ⭐168) sudah tertaut langsung pada entri repositorinya di `02_TOP_GITHUB_HIGH_TRACTION_DAN_RISET.md`.

- [ ] **Smart Phone Operated Automatic Chicken Coop Door — CodeMakesItGo** — `[TIER A]` `[Masalah #1]` `[Biosekuriti Akses / Skematik Relai 12V & 5V + Firmware]`
  - **Bukti Kualitas / Traksi:** `👁 18.258 Views (YouTube)` | `⭐ 2 Stars` + Skematik lengkap di GitHub & Instructables
  - **Ringkasan:** Video demonstrasi dan panduan skematik rangkaian elektronik pengendali pintu kandang ayam otomatis yang dapat dipantau dari ponsel untuk pengamanan akses kandang harian.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://youtu.be/RmLc_RDQBD4) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/CodeMakesItGo/ChickenCoopDoor) *(HTTP 200)*
    - Dataset / Model: [Instructables Schematic](https://www.instructables.com/Smart-Phone-Operated-Chicken-Coop-Door-/) *(HTTP 200)*

- [ ] **Computerized Poultry Management System (C# & SQL Server) — Iszzytech** — `[TIER A]` `[Masalah #1]` `[Desktop Recording Flok & Mortalitas + Source Code]`
  - **Bukti Kualitas / Traksi:** `👁 13.493 Views (YouTube)` | `⭐ 2 Stars` + *Source code* lengkap di GitHub
  - **Ringkasan:** Demonstrasi perangkat lunak pencatatan peternakan ayam berbasis C# dan SQL Server untuk pengelolaan populasi, mortalitas, dan laporan operasional harian kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=Fnlyil9ettM) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/Iszzytech/computerized-poultry) *(HTTP 200)*

- [ ] **$50 DIY AI Smart Coop — Coders Cafe** — `[TIER A]` `[#1 & #2]` `[Edge AI Predator/Biosekuriti + Otomasi Kandang]`
  - **Bukti Kualitas / Traksi:** `👁 8.233 Views (YouTube)` + Dokumentasi lengkap Hackster.io + Kode & Sirkuit GitHub
  - **Ringkasan:** Panduan *maker* berbiaya rendah untuk membangun kandang pintar dengan deteksi ancaman predator berbasis *computer vision*, pintu otomatis motor *stepper*, dan notifikasi ke aplikasi mobile.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=dbEeGJjQNNE) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/CodersCafeTech/AI-Smart-Coop) *(HTTP 200)*
    - Dataset / Model: [Hackster.io Guide](https://www.hackster.io/coderscafe/50-diy-ai-smart-coop-4ae70e) *(HTTP 200)*
