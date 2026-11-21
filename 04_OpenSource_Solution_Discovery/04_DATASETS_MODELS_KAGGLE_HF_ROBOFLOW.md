# 04 — DATASET, PRETRAINED MODELS & AI SPACES (*OPEN-SOURCE*)

> **Cakupan Platform:** Kaggle (diverifikasi `HTTP 200` melalui *Official Public REST API* `/api/v1/datasets/view/...`), Hugging Face (Models, Datasets, & Gradio/Docker Spaces), Mendeley Data, dan Zenodo.  
> **Catatan Transparansi Roboflow Universe:** Terdapat pada Bagian E di bawah (jujur melaporkan status `HTTP 403` Cloudflare tanpa *bypass*).  
> `[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

---

## A. Kaggle Datasets (`kaggle.com/datasets`)

- [ ] **Chicken Disease Image Classification (`allandclive/chicken-disease-1`)** — `[Masalah #1]` `[Dataset CV Feses — 4 Kelas PCR, 266 MB]`
  - **Ringkasan:** Dataset citra feses ayam paling populer di Kaggle (85 *upvotes*, >9.200 unduhan) berisi 4 kelas diagnostik terverifikasi (Coccidiosis, Salmonella, Newcastle Disease, Healthy) untuk pelatihan CNN/Vision Transformer.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/allandclive/chicken-disease-1) *(HTTP 200 via Kaggle Public API)*

- [ ] **Poultry Diseases Detection (`kausthubkannan/poultry-diseases-detection`)** — `[Masalah #1]` `[Dataset CV Feses — 8,08 GB]`
  - **Ringkasan:** Koleksi berskala besar (45 *upvotes*, >4.400 unduhan, ~8 GB) berisi citra feses ayam resolusi tinggi untuk pelatihan deteksi Coccidiosis, Salmonella, dan Newcastle Disease.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/kausthubkannan/poultry-diseases-detection) *(HTTP 200 via Kaggle Public API)*

- [ ] **Poultry Pathology Visual Dataset (`chandrashekarnatesh/poultry-diseases`)** — `[Masalah #1]` `[Dataset CV Patologi & Penyakit Unggas — 12,88 GB]`
  - **Ringkasan:** Dataset visual patologi unggas berukuran ~12,9 GB (40 *upvotes*, >4.300 unduhan) yang digunakan luas untuk pelatihan *transfer learning* diagnostik penyakit ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/chandrashekarnatesh/poultry-diseases) *(HTTP 200 via Kaggle Public API)*

- [ ] **Poultry Disease Fecal Image Dataset (`abdulmuqsitalam/poultry-disease-fecal-image-dataset`)** — `[Masalah #1]` `[Dataset CV Feses Terkurasi 17K+ Citra — 7,95 GB]`
  - **Ringkasan:** Kumpulan lebih dari 17.000 citra feses unggas terkurasi (~7,95 GB) yang dirancang untuk klasifikasi penyakit saluran pencernaan ayam secara otomatis.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/abdulmuqsitalam/poultry-disease-fecal-image-dataset) *(HTTP 200 via Kaggle Public API)*

- [ ] **Chicken Health Images Dataset — RGB & Thermal (`ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal`)** — `[#1 & #2]` `[Dataset Multimodal RGB + Thermal / Kontributor Indonesia — 89 MB]`
  - **Ringkasan:** Dataset multimodal berlisensi CC0 karya kontributor Indonesia (Eko Supriyanto) berisi pasangan citra RGB dan termal inframerah ayam dengan kategori *Healthy*, *Sick*, dan *Dead* untuk deteksi penyakit maupun anomali suhu tubuh.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) *(HTTP 200 via Kaggle Public API)*

- [ ] **ChickenAct / ChickenVerse (`amirivojdan/chickenact`)** — `[#1 & #2]` `[Dataset CV Multi-Task Perilaku Ayam — 1,88 GB]`
  - **Ringkasan:** Dataset *open-source* multi-tugas berskala besar (1,88 GB) untuk deteksi, segmentasi, dan pengenalan aktivitas/perilaku ayam di kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/amirivojdan/chickenact) *(HTTP 200 via Kaggle Public API)*

- [ ] **Broiler Chicken Sick & Healthy 3-Classes (`aqiii2742/broiler-chiken-sick-and-healthy3-classes`)** — `[Masalah #1]` `[Dataset CV Ayam Broiler Sakit vs Sehat — 93 MB]`
  - **Ringkasan:** Dataset citra ayam broiler (3 kelas kondisi sehat dan sakit) untuk pelatihan model deteksi objek atau klasifikasi kondisi fisik ayam di lantai kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/aqiii2742/broiler-chiken-sick-and-healthy3-classes) *(HTTP 200 via Kaggle Public API)*

- [ ] **Environmental Effect on Egg Production (`faysal1998/environmental-effect-on-egg-production`)** — `[Masalah #2]` `[Dataset Tabular Mikroklimat & Produksi Telur]`
  - **Ringkasan:** Dataset tabular (10 *upvotes*, ~984 unduhan) yang memetakan pengaruh variabel lingkungan kandang terhadap kinerja produksi ayam petelur (*layer*).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/faysal1998/environmental-effect-on-egg-production) *(HTTP 200 via Kaggle Public API)*

- [ ] **Prediction of Egg Production Rate in Poultry (`deepikabidri/prediction-of-egg-production-rate-in-poultry`)** — `[Masalah #2]` `[Dataset Tabular Humidex, Kualitas Udara & Air]`
  - **Ringkasan:** Dataset pemodelan dampak *humidex* (indeks panas-kelembapan), kualitas udara, dan kualitas air terhadap laju produksi telur untuk analisis *heat stress* pada layer.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/deepikabidri/prediction-of-egg-production-rate-in-poultry) *(HTTP 200 via Kaggle Public API)*

- [ ] **PCMC Egg Production & Environment (`ashirwadkatkamwar/pcmc-egg-production-and-environment`)** — `[Masalah #2]` `[Dataset Tabular Amonia NH₃, Suhu & Produksi Telur]`
  - **Ringkasan:** Data pencatatan peternakan yang menghubungkan kadar amonia (`NH₃`) dan suhu kandang dengan capaian produksi telur harian.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Kaggle Dataset](https://www.kaggle.com/datasets/ashirwadkatkamwar/pcmc-egg-production-and-environment) *(HTTP 200 via Kaggle Public API)*

---

## B. Hugging Face — Pretrained Models, Datasets & Interactive Spaces (`huggingface.co`)

- [ ] **Evet-Africa Poultry Disease Ecosystem (`Evet-Africa/poultry-disease-detector`)** — `[Masalah #1]` `[YOLO11 Model + Live Gradio Space RUNNING + Dataset]`
  - **Ringkasan:** Paket *open-source* lengkap (AGPL-3.0) mencakup model deteksi objek YOLO11, dataset berlabel (>1.160 unduhan), dan demo interaktif Gradio Space yang berstatus aktif (`RUNNING`).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/Evet-Africa/poultry-disease-detector) *(HTTP 200)*
    - Demo Live: [Hugging Face Space (RUNNING)](https://huggingface.co/spaces/Evet-Africa/poultry-disease-detector) *(HTTP 200)*
    - Dataset/Model: [Hugging Face Dataset](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) *(HTTP 200)*

- [ ] **PoultryVision (`Williamsanderson/PoultryVision`)** — `[Masalah #1]` `[Pretrained Model / YOLOv11 Ultralytics Object Detection]`
  - **Ringkasan:** Model deteksi objek berbasis Ultralytics YOLOv11 (171 unduhan) yang dilatih khusus untuk kebutuhan *computer vision* pada lingkungan peternakan unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/Williamsanderson/PoultryVision) *(HTTP 200)*

- [ ] **Fine-Tuned ViT for Poultry Excreta (`dzinampini/finetuned-vit-for-poultry-excreta-classification`)** — `[Masalah #1]` `[Pretrained Model / Vision Transformer ViT-Base Apache-2.0]`
  - **Ringkasan:** Model *Vision Transformer* (`google/vit-base-patch16-224-in21k`) berlisensi permisif Apache-2.0 yang sudah di-*fine-tune* untuk klasifikasi citra feses unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/dzinampini/finetuned-vit-for-poultry-excreta-classification) *(HTTP 200)*

- [ ] **Broiler Feces Classifier (`arcsu1/Broiler-Feces-Classifier`)** — `[Masalah #1]` `[Pretrained Model / Klasifikasi Feses Broiler]`
  - **Ringkasan:** Model klasifikasi citra feses khusus ayam broiler untuk deteksi dini penyakit infeksius kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/arcsu1/Broiler-Feces-Classifier) *(HTTP 200)*

- [ ] **MedGemma Poultry VLM (`lourimi/medgemma-poultry`)** — `[Masalah #1]` `[Pretrained VLM / Fine-tuned google/medgemma-4b-it]`
  - **Ringkasan:** Eksperimen *Vision-Language Model* berbasis `google/medgemma-4b-it` yang di-*fine-tune* untuk domain diagnostik kesehatan unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Model](https://huggingface.co/lourimi/medgemma-poultry) *(HTTP 200)*

- [ ] **Poultry Disease Detection Audio Dataset (`Darayut/poultry-disease-detection-audio-dataset`)** — `[Masalah #1]` `[Dataset Audio Pernapasan & Suara Penyakit Ayam]`
  - **Ringkasan:** Dataset audio siap pakai dalam format Hugging Face (`audio` + `label`) untuk melatih model klasifikasi akustik deteksi dini penyakit ayam dari suara kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/Darayut/poultry-disease-detection-audio-dataset) *(HTTP 200)*

- [ ] **Chicken Feces Dataset — Baseline Clean (`iagovarela/poultry-disease-dataset`)** — `[Masalah #1]` `[Dataset CV Feses Terkurasi — 562 Unduhan]`
  - **Ringkasan:** Dataset citra feses ayam bersih dan terkurasi yang dirancang sebagai *baseline* pelatihan model klasifikasi penyakit unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/iagovarela/poultry-disease-dataset) *(HTTP 200)*

- [ ] **Poultry Fecal Federated Learning Dataset (`Dianyo/poultry-fecal-fl`)** — `[Masalah #1]` `[Dataset CV Feses untuk Federated Learning]`
  - **Ringkasan:** Dataset citra feses ayam berformat Parquet di Hugging Face (235 unduhan) yang disiapkan untuk skenario pelatihan terdistribusi (*Federated Learning*) lintas peternakan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/Dianyo/poultry-fecal-fl) *(HTTP 200)*

- [ ] **Real Poultry Videos (`34data/v14-real-poultry-videos`)** — `[#1 & #2]` `[Dataset Video Nyata Kandang Unggas]`
  - **Ringkasan:** Koleksi rekaman video asli lingkungan kandang ayam untuk pengembangan model pelacakan perilaku flok, deteksi anomali, maupun *heat stress*.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/34data/v14-real-poultry-videos) *(HTTP 200)*

- [ ] **Poultry Disease Dataset — Kontributor Indonesia (`abdkupang/poultry-disease-dataset`)** — `[Masalah #1]` `[Dataset CV Object Detection — Kontributor Kupang]`
  - **Ringkasan:** Dataset deteksi objek penyakit unggas di Hugging Face yang diunggah oleh kontributor asal Indonesia (Kupang) untuk pengembangan model CV lokal.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Dataset](https://huggingface.co/datasets/abdkupang/poultry-disease-dataset) *(HTTP 200)*

- [ ] **Chicken Disease Detector — Sound Space (`azouzmobileapp/chicken-disease-detector-sound`)** — `[Masalah #1]` `[Gradio Space / Deteksi Penyakit Berbasis Audio]`
  - **Ringkasan:** Aplikasi demo interaktif Gradio Space untuk mendeteksi penyakit ayam dari rekaman audio/suara kandang. *(Catatan: status Space `SLEEPING` — akan aktif otomatis saat dibuka/dibangunkan).*
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Space](https://huggingface.co/spaces/azouzmobileapp/chicken-disease-detector-sound) *(HTTP 200)*

- [ ] **Poultry Disease MobileNetV2 Demo (`Subarctic1153/poultry-disease-mobilenetv2-demo`)** — `[Masalah #1]` `[Gradio Space / MobileNetV2 Classifier]`
  - **Ringkasan:** Demo Gradio interaktif klasifikasi penyakit unggas berbasis arsitektur ringan MobileNetV2 *(status Space `SLEEPING` — on-demand wake)*.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Space](https://huggingface.co/spaces/Subarctic1153/poultry-disease-mobilenetv2-demo) *(HTTP 200)*

- [ ] **Broiler Dashboard Space (`PLum18/broiler-dashboard`)** — `[#1 & #2]` `[Docker/Streamlit Space / Dashboard Performa Broiler]`
  - **Ringkasan:** Template *dashboard* pemantauan operasional ayam broiler berbasis Docker/Streamlit yang di-host publik di Hugging Face Spaces *(status `SLEEPING` — on-demand wake)*.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Hugging Face Space](https://huggingface.co/spaces/PLum18/broiler-dashboard) *(HTTP 200)*

---

## C. Mendeley Data (`data.mendeley.com`)

- [ ] **SmartEars: Poultry Respiratory Monitoring Audio Dataset** — `[Masalah #1]` `[Dataset Audio Pernapasan Komersial — 6.000 Segmen]`
  - **Ringkasan:** Dataset akustik kandang komersial berisi 6.000 segmen audio bersih berdurasi 5 detik (dari 11.686 potongan awal) berlabel *Healthy*, *Sick*, dan *None* (derau kipas/ventilasi) untuk klasifikasi spektrogram penyakit pernapasan ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/dy6gtvt4mk/2) *(HTTP 200)*

- [ ] **Poultry Vocalization Signal Dataset for Early Disease Detection** — `[Masalah #1]` `[Dataset Audio .wav Penyakit Pernapasan — 65 Hari]`
  - **Ringkasan:** Koleksi 346 rekaman sinyal audio `.wav` (kategori *healthy*, *noise*, *unhealthy*) hasil pemantauan akustik kontinu selama 65 hari pada ayam yang mengalami infeksi saluran pernapasan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/zp4nf2dxbh/1) *(HTTP 200)*

- [ ] **Sick and Healthy: Thermal Images of Broiler Avian 48** — `[#1 & #2]` `[Dataset Citra Termal Inframerah — 600 Ekor Broiler]`
  - **Ringkasan:** Dataset citra kamera termal inframerah dari 600 ekor ayam broiler Cobb Avian 48 (sehat vs sakit, berbagai umur dan sudut pengambilan) untuk penelitian deteksi demam, penyakit, dan stres termal.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/vwbb4dc9b7/1) *(HTTP 200)*

- [ ] **Environmental Monitoring of Broiler Chickens During Summer and Winter** — `[Masalah #2]` `[Dataset Sensor Mikroklimat — 1.920 Observasi NH₃/CO₂/Suhu/RH]`
  - **Ringkasan:** Dataset telemetri 1.920 observasi lingkungan kandang broiler mencakup suhu dalam/luar, kelembapan relatif, amonia (`NH₃`), karbon dioksida (`CO₂`), intensitas cahaya, dan umur flok.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Mendeley Data](https://data.mendeley.com/datasets/m9nsjhtsph/1) *(HTTP 200)*

---

## D. Zenodo Open-Access Datasets (`zenodo.org`)

- [ ] **Machine Learning Dataset for Poultry Diseases Diagnostics — PCR Annotated** — `[Masalah #1]` `[Dataset CV Feses Terverifikasi PCR + Anotasi YOLO]`
  - **Ringkasan:** Dataset rujukan utama (DOI `10.5281/zenodo.5801834`) berisi ribuan citra feses ayam berlabel PCR (Coccidiosis, Salmonella, Newcastle Disease, Healthy) lengkap dengan bundel anotasi deteksi objek YOLO dan segmentasi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo Record 5801834](https://zenodo.org/records/5801834) *(HTTP 200)* | [Zenodo Record 4628934](https://zenodo.org/records/4628934) *(HTTP 200)*

- [ ] **ChickenSense Dataset** — `[#1 & #2]` `[Dataset Deep Learning Monitoring Unggas Berbiaya Rendah]`
  - **Ringkasan:** Dataset terbuka (DOI `10.5281/zenodo.8212853`) pendukung sistem *ChickenSense* untuk pemantauan kesehatan dan kondisi unggas *real-time* berbasis *deep learning* berbiaya rendah.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/8212853) *(HTTP 200)*

- [ ] **Chick Call Dataset** — `[#1 & #2]` `[Dataset Audio Panggilan/Vokalisasi Anak Ayam]`
  - **Ringkasan:** Kumpulan rekaman audio terbuka (DOI `10.5281/zenodo.6655837`) panggilan/vokalisasi anak ayam untuk pelatihan model klasifikasi bioakustik dan deteksi stres dini fase *brooding*.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/6655837) *(HTTP 200)*

- [ ] **ChickenVerse: Detection, Segmentation & Behavior Recognition (2026)** — `[#1 & #2]` `[Dataset CV Deteksi, Segmentasi & Perilaku Ayam]`
  - **Ringkasan:** Dataset riset terbuka terbaru (Juni 2026, DOI `10.5281/zenodo.20672799`) untuk deteksi objek, segmentasi instans, dan pengenalan perilaku ayam secara komprehensif.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [Zenodo](https://zenodo.org/records/20672799) *(HTTP 200)*

---

## E. Catatan Transparansi Verifikasi Roboflow Universe (`HTTP 403 Cloudflare`)

<!-- UNVERIFIED_REF_START -->
> **Status Jujur (Tidak Dimasukkan ke Statistik Terverifikasi):** Penelusuran indeks web menemukan kandidat dataset Roboflow Universe yang relevan (*Broiler Chicken Healthy and Sick*, *Poultry Mortality Detection — Suguna Foods*, *Chicken Disease Dataset Fecal*, *Chicken Broiler YOLO Thesis — Panting/Behavior*, dan workspace *TA Ayam Sakit*). Namun, seluruh halaman `universe.roboflow.com` mengembalikan **`HTTP 403`** akibat proteksi bot Cloudflare saat diakses oleh skrip otomatis, dan koneksi Chrome DevTools lokal (`DevToolsActivePort`) sedang tidak aktif untuk verifikasi browser otomatis. Sesuai aturan anti-bypass dan anti-halusinasi, **kandidat Roboflow Universe di bawah TIDAK dihitung dalam total entri terverifikasi**; silakan buka secara manual di browser Anda bila ingin meninjau:
> - `https://universe.roboflow.com/technicalresearch/broiler-chicken-healthy-and-sick` *(HTTP 403 Cloudflare — Cek Manual)*
> - `https://universe.roboflow.com/suguna-foods-private-limited-fjgdl/poultry-mortality-detection-zpykq` *(HTTP 403 Cloudflare — Cek Manual)*
> - `https://universe.roboflow.com/charan-7q0md/healthy-and-sick-chicken-detection-kavqw` *(HTTP 403 Cloudflare — Cek Manual)*
> - `https://universe.roboflow.com/h-mdtos/chicken-disease-dataset-fecal` *(HTTP 403 Cloudflare — Cek Manual)*
> - `https://universe.roboflow.com/yolov8-chicken-broiler-thesis-s2/chicken-broiler-yolo-thesis-march-ver1-2026` *(HTTP 403 Cloudflare — Cek Manual)*
> - `https://universe.roboflow.com/ta-ayam-sakit` *(HTTP 403 Cloudflare — Cek Manual)*
<!-- UNVERIFIED_REF_END -->
