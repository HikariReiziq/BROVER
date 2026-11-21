# 02 — REPOSITORI GITHUB OPEN-SOURCE: MASALAH #1 (PENYAKIT ENDEMIK, BIOSEKURITI & COLD CHAIN VAKSIN)

> **Cakupan:** Repositori GitHub non-kosong (*verified code/files*) khusus **Masalah #1** — meliputi Computer Vision feses ayam, CV deteksi ayam sakit/mati/perilaku, Audio/Vokalisasi ayam, Biosekuriti & SPK/Vaksinasi, serta *Cold Chain* Vaksin (2–8°C).  
> **Anti-Duplikasi:** Repositori yang sudah tercakup di `01_HACKATHON_DAN_MAKER_PROJECTS.md` atau `05_YOUTUBE_DEMO_OPENSOURCE.md` **tidak diulang** di sini, serta salinan tutorial kloning identik telah disaring agar beragam secara arsitektur dan *tech stack*.  
> `[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

---

## A. Computer Vision — Klasifikasi Feses Ayam (Coccidiosis, Salmonella, Newcastle Disease)

- [ ] **Chicken AI (`oualidrouabah/poultry-disease-detection-app`)** — `[Masalah #1]` `[CV Feses / Flutter + TFLite Mobile Offline]`
  - **Ringkasan:** Aplikasi mobile lintas-platform berbasis Flutter (Dart) dan TensorFlow Lite (DenseNet) untuk mendeteksi penyakit ayam (Coccidiosis, Salmonella, NCD) secara *offline* langsung dari foto feses di kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/oualidrouabah/poultry-disease-detection-app) *(HTTP 200)*

- [ ] **Poultry Disease Detection Android (`jothammicheni/Poultry-Disease-Detection-App`)** — `[Masalah #1]` `[CV Feses / Android Java + Rekomendasi Penanganan]`
  - **Ringkasan:** Aplikasi Android natif (Java) yang mendeteksi Newcastle Disease, Salmonella, dan Coccidiosis dari citra feses ayam sekaligus menampilkan panduan langkah penanganan awal bagi peternak.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/jothammicheni/Poultry-Disease-Detection-App) *(HTTP 200)*

- [ ] **Diagnostics Poultry Disease Identifier (`Saeed-dev2/poultry_Form_Disease_Deep-Learning-Machine-Learning-Computer-vision`)** — `[Masalah #1]` `[CV Feses / TensorFlow + Streamlit Web App]`
  - **Ringkasan:** Pipeline *deep learning* TensorFlow/Keras dan antarmuka web interaktif Streamlit lengkap dengan dokumentasi arsitektur untuk klasifikasi citra feses ayam (Coccidiosis, Salmonella, NCD, Healthy).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Saeed-dev2/poultry_Form_Disease_Deep-Learning-Machine-Learning-Computer-vision) *(HTTP 200)*

- [ ] **Automated Poultry Disease Detection & QA Assistant (`SumitChougale09/Automated-Poultry-disease-detection`)** — `[Masalah #1]` `[CV Feses + Hybrid RAG QA Assistant]`
  - **Ringkasan:** Sistem hibrida yang menggabungkan model *deep learning* klasifikasi penyakit unggas berbasis citra dengan asisten tanya-jawab *Retrieval-Augmented Generation* (RAG) untuk panduan klinis di lapangan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/SumitChougale09/Automated-Poultry-disease-detection) *(HTTP 200)*

- [ ] **Explainable AI Chicken Disease Classification (`Hamza-khan-11/chicken-disease-classification-using-deeplearning`)** — `[Masalah #1]` `[CV Feses / VGG16 + Explainable AI]`
  - **Ringkasan:** Implementasi *transfer learning* VGG16 untuk klasifikasi feses ayam (Healthy, Coccidiosis, Salmonella, NCD) dilengkapi notebook *Explainable AI* guna memvisualisasikan area visual feses yang memicu diagnosis model.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Hamza-khan-11/chicken-disease-classification-using-deeplearning) *(HTTP 200)*

- [ ] **ChickenHealth AI (`bagaskara112/chicken-disease-classifier`)** — `[Masalah #1]` `[CV Feses / TensorFlow CNN Web App — Indonesia]`
  - **Ringkasan:** Proyek pengembang Indonesia berupa sistem web Python/TensorFlow untuk klasifikasi penyakit ayam dari citra feses lengkap dengan konfigurasi *deployment* (`app.py`, `Procfile`).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/bagaskara112/chicken-disease-classifier) *(HTTP 200)*

- [ ] **Chicken Disease MLOps End-to-End (`AdMub/Chicken-Disease-Classification-End-to-End-Project`)** — `[Masalah #1]` `[CV Feses / MLOps DVC + Docker + CI/CD]`
  - **Ringkasan:** Pipeline MLOps terstruktur menggunakan DVC (*Data Version Control*), Docker, dan GitHub Actions CI/CD untuk melatih dan mendeploy model CNN deteksi parasit Coccidiosis dari citra feses ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/AdMub/Chicken-Disease-Classification-End-to-End-Project) *(HTTP 200)*

- [ ] **ChickenCare-AI (`Calvin-Rondozai/Chicken-feces-disease-classifier`)** — `[Masalah #1]` `[CV Feses / Web Classifier]`
  - **Ringkasan:** Aplikasi web klasifikasi kesehatan unggas berbasis analisis citra feses untuk skrining dini penyakit pencernaan ayam secara cepat oleh peternak.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Calvin-Rondozai/Chicken-feces-disease-classifier) *(HTTP 200)*

- [ ] **MobileNetV2 Poultry Disease Classifier (`prabhavathi11-code/Transfer-Learning-Based-Classification-of-Poultry-Diseases-for-Enhanced-Health-Management`)** — `[Masalah #1]` `[CV Feses / MobileNetV2 Ringan]`
  - **Ringkasan:** Klasifikasi penyakit ayam berbasis *transfer learning* arsitektur ringan MobileNetV2 yang dirancang agar mudah diimplementasikan pada antarmuka web sederhana atau perangkat *edge* terbatas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/prabhavathi11-code/Transfer-Learning-Based-Classification-of-Poultry-Diseases-for-Enhanced-Health-Management) *(HTTP 200)*

---

## B. Computer Vision — Deteksi Ayam Sakit, Mati (*Mortality*), Postur & Anomali Perilaku Flok

- [ ] **Broiler Carcass Candidate Detection (`jeongrubin/broiler-carcass-candidate-detection`)** — `[Masalah #1]` `[CV CCTV Mortalitas / YOLOv8s + U-Net + Mask Sequence]`
  - **Ringkasan:** Pipeline deteksi kandidat bangkai ayam mati (*mortality*) langsung dari rekaman CCTV kandang broiler menggunakan kombinasi YOLOv8s, segmentasi U-Net, dan analisis sekuens masker untuk mendeteksi ayam tidak bergerak.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/jeongrubin/broiler-carcass-candidate-detection) *(HTTP 200)*

- [ ] **Big Broiler Dataset & Tracking (`decide-ugent/big-broiler-dataset`)** — `[Masalah #1]` `[CV Multi-Object Tracking & Perilaku Broiler — Ghent Univ.]`
  - **Ringkasan:** Kode dan kerangka kerja *open-source* dari Ghent University untuk *multi-object tracking* dan pengenalan perilaku halus (*fine-grained behaviour*) ayam broiler pada video skala besar guna deteksi dini anomali kesehatan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/decide-ugent/big-broiler-dataset) *(HTTP 200)*

- [ ] **Multi-View Broiler Tracking (`decide-ugent/multi-view-broiler-tracking`)** — `[Masalah #1]` `[CV Multi-Kamera Tracking Flok Broiler]`
  - **Ringkasan:** Pipeline *computer vision* multi-sudut pandang kamera untuk deteksi dan pelacakan lintasan individu broiler secara kontinu demi memantau tingkat aktivitas dan kelumpuhan/lesu di kandang komersial.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/decide-ugent/multi-view-broiler-tracking) *(HTTP 200)*

- [ ] **Flock Guard (`bharath-inukurthi/hen-disease-detection-model`)** — `[Masalah #1]` `[CV Deteksi Ayam Sakit / YOLOv8 Real-Time]`
  - **Ringkasan:** Model pemantauan kesehatan unggas berbasis YOLOv8 untuk mendeteksi indikasi ayam sakit secara *real-time* dari tangkapan kamera kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/bharath-inukurthi/hen-disease-detection-model) *(HTTP 200)*

- [ ] **Roost Poultry Farm Management (`Khizar7786/Roost-poultry-farm-management`)** — `[Masalah #1]` `[CV YOLO + ByteTrack Counting & Health Monitoring]`
  - **Ringkasan:** Platform pemantauan kandang ayam berbasis AI yang menggabungkan deteksi YOLO dan pelacakan ByteTrack untuk penghitungan populasi anak ayam serta pengawasan status kesehatan flok.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Khizar7786/Roost-poultry-farm-management) *(HTTP 200)*

- [ ] **Poultry Watch (`AqibMehmoodMalik/Poultry-Watch---Early-Disease-Detection-for-Broiler-Chickens`)** — `[Masalah #1]` `[CV Deteksi Dini Penyakit Ayam Broiler]`
  - **Ringkasan:** Sistem deteksi dini penyakit ayam broiler berbasis *computer vision* yang memproses citra kandang untuk mengidentifikasi tanda-tanda klinis awal ayam sakit.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/AqibMehmoodMalik/Poultry-Watch---Early-Disease-Detection-for-Broiler-Chickens) *(HTTP 200)*

- [ ] **Real-Time Poultry Disease CNN/YOLO (`digvijay990/Poultry_Farm-Disease-detection-Using-CNN`)** — `[Masalah #1]` `[CV Real-Time Object Detection best.pt + Web App]`
  - **Ringkasan:** Aplikasi Python (`app.py`) dengan bobot model terlatih (`best.pt`) untuk deteksi dini penyakit unggas secara *real-time* dari aliran gambar/video kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/digvijay990/Poultry_Farm-Disease-detection-Using-CNN) *(HTTP 200)*

- [ ] **ClumsyChickens (`AlexHsuYu/ClumsyChickens`)** — `[Masalah #1]` `[CV Instance Segmentation Mask R-CNN Broiler]`
  - **Ringkasan:** Implementasi beberapa *backbone* Mask R-CNN untuk segmentasi dan deteksi individu ayam broiler di lantai kandang komersial guna mendukung analitik postur dan kepadatan flok.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/AlexHsuYu/ClumsyChickens) *(HTTP 200)*

- [ ] **Broiler Feed Pecking Analysis System — BFPAS (`UchiteL0515/Broiler-Feed-Pecking-Analysis-System---BFPAS`)** — `[Masalah #1]` `[Anomali Perilaku Makan / Early Warning Kesehatan]`
  - **Ringkasan:** Purwarupa aplikasi Flutter/ML untuk mendeteksi anomali kesehatan dini pada ayam broiler melalui analisis penurunan atau perubahan pola perilaku mematuk pakan (*feed pecking*).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/UchiteL0515/Broiler-Feed-Pecking-Analysis-System---BFPAS) *(HTTP 200)*

- [ ] **Broiler Platform Weighing Anomaly Analysis (`yuka-m-sora/broiler-monitoring-analysis`)** — `[Masalah #1]` `[Early Warning Anomali Bobot & Pertumbuhan Flok]`
  - **Ringkasan:** Aplikasi analisis Python/Streamlit untuk memproses data penimbangan otomatis broiler dan mendeteksi penyimpangan kurva pertumbuhan sebagai indikator dini gangguan kesehatan flok.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/yuka-m-sora/broiler-monitoring-analysis) *(HTTP 200)*

---

## C. Audio / Acoustic AI — Vokalisasi & Deteksi Stres/Pernapasan Ayam

- [ ] **ChickenLanguageDataset (`zebular13/ChickenLanguageDataset`)** — `[#1 & #2]` `[Audio AI / Dataset & Skrip Vokalisasi Ayam]`
  - **Ringkasan:** Repositori *open-source* populer (47 bintang) berisi kumpulan rekaman audio vokalisasi ayam berlabel (segmen panjang, vokalisasi tunggal, dan derau latar) untuk melatih model *machine learning* klasifikasi suara/distress ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/zebular13/ChickenLanguageDataset) *(HTTP 200)*

- [ ] **CVC-Fusion (`CoderYLH/CVC-Fusion`)** — `[#1 & #2]` `[Audio AI / 1D MobileNetV2 Multi-Domain Feature Fusion]`
  - **Ringkasan:** Model ringan *Chicken Vocalization Classification-Fusion* berbasis *encoder* 1D MobileNetV2 dengan fusi fitur multi-domain akustik untuk mengenali pola vokalisasi ayam di bawah tekanan *heat stress* maupun kondisi abnormal.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/CoderYLH/CVC-Fusion) *(HTTP 200)*

---

## D. Biosekuriti Kandang, Manajemen Vaksinasi & Sistem Pendukung Keputusan (SPK)

- [ ] **BioGuard Farm Hub (`atchayas-ai/bioguard-farm-hub`)** — `[Masalah #1]` `[Biosekuriti / Visitor Log & Protokol Kandang]`
  - **Ringkasan:** Portal web TypeScript manajemen biosekuriti peternakan ayam (dan ternak intensif) yang mencakup daftar periksa protokol biosekuriti, pencatatan tamu/pengunjung (*visitor management*), kesehatan hewan, dan pelaporan insiden.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/atchayas-ai/bioguard-farm-hub) *(HTTP 200)*
    - Demo Live: [Vercel](https://bioguard-farm-hub.vercel.app) *(HTTP 200)*

- [ ] **AgroArmor (`pravallika7610/AgroArmor`)** — `[Masalah #1]` `[Biosekuriti & Edukasi Penyakit Unggas]`
  - **Ringkasan:** Platform web manajemen biosekuriti dan kewaspadaan penyakit khusus peternakan ayam dengan dukungan multi-bahasa, pelacakan kepatuhan SOP kandang, dan basis data MongoDB.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/pravallika7610/AgroArmor) *(HTTP 200)*
    - Demo Live: [Render](https://agroarmourlsm-frontend.onrender.com/) *(HTTP 200)*

- [ ] **Smart Poultry Platform (`SiddharthHiraou/smart-poultry-platform`)** — `[#1 & #2]` `[YOLOv8 Disease Detection + IoT MQTT Climate Control]`
  - **Ringkasan:** Platform TypeScript terintegrasi yang memadukan deteksi penyakit ayam berbasis YOLOv8, pemantauan & kontrol iklim kandang via MQTT, serta manajemen alur kerja operasional harian pekerja kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/SiddharthHiraou/smart-poultry-platform) *(HTTP 200)*

- [ ] **Poultry Guard AI Web Application (`Apurva35973/Polutry-Guard-AI-Web-Application`)** — `[#1 & #2]` `[Biosekuriti + Monitoring Mortalitas & Lingkungan]`
  - **Ringkasan:** Aplikasi web biosekuriti dan pemantauan peternakan ayam yang melacak suhu, kelembapan, mortalitas harian, serta konsumsi pakan untuk peringatan anomali dini.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Apurva35973/Polutry-Guard-AI-Web-Application) *(HTTP 200)*

- [ ] **TelelBirds (`kngeno/telelbirds`)** — `[Masalah #1]` `[Manajemen Flok & Pengingat Jadwal Vaksinasi — Django]`
  - **Ringkasan:** Sistem manajemen peternakan ayam *open-source* berbasis Python/Django yang mencakup pelacakan *batch* ayam, pencatatan kesehatan, dan sistem pengingat jadwal imunisasi/vaksinasi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/kngeno/telelbirds) *(HTTP 200)*

- [ ] **ChiRex (`januriawan/chirex`)** — `[Masalah #1]` `[SPK Diagnosa Penyakit Ayam Certainty Factor — Indonesia]`
  - **Ringkasan:** Aplikasi web *open-source* Indonesia (96 bintang) berupa sistem pakar diagnosa awal penyakit ayam berbasis metode *Certainty Factor* untuk membantu pekerja kandang membedakan gejala klinis penyakit unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/januriawan/chirex) *(HTTP 200)*

- [ ] **KawanKandang (`gntrr/kawan-kandang-app`)** — `[Masalah #1]` `[SPK Deteksi Dini Penyakit Ayam Broiler — Indonesia]`
  - **Ringkasan:** Aplikasi web Laravel (Indonesia) berupa Sistem Pendukung Keputusan untuk skrining dini gejala penyakit pada ayam broiler guna membantu peternak merespons sebelum kematian melonjak.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/gntrr/kawan-kandang-app) *(HTTP 200)*

---

## E. Pemantauan *Cold Chain* Vaksin (Rentang 2–8°C)

- [ ] **Smart IoT Cold Chain Monitoring (`subbuu-aadhii/Cold-Chain-Monitoring`)** — `[Masalah #1]` `[IoT Cold Chain 2–8°C / ESP32 + PCB + GPS/GSM]`
  - **Ringkasan:** Sistem pemantauan rantai dingin vaksin berbasis ESP32 dilengkapi skematik PCB, file CAD, kontrol suhu otomatis, dan pelacakan GPS/GSM untuk menjaga suhu vaksin tetap stabil saat distribusi/penyimpanan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/subbuu-aadhii/Cold-Chain-Monitoring) *(HTTP 200)*

- [ ] **VacciTrack (`netai2909/VacciTrack`)** — `[Masalah #1]` `[IoT Cold Chain 2–8°C / Arduino + Live Dashboard]`
  - **Ringkasan:** Pemantau suhu rantai dingin vaksin berbiaya rendah berbasis sensor Arduino yang terhubung ke *dashboard* web *real-time* untuk mendeteksi ekskursi suhu penyimpanan di area pedesaan/minim infrastruktur.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/netai2909/VacciTrack) *(HTTP 200)*
    - Demo Live: [Vercel](https://vacci-track-lake.vercel.app) *(HTTP 200)*

- [ ] **Portable Peltier Vaccine Carrier (`harrisroby/peltier-vaccine-carrier`)** — `[Masalah #1]` `[Hardware Cold Chain Aktif 2–8°C / Arduino + Peltier]`
  - **Ringkasan:** Purwarupa kotak pembawa vaksin portabel berbasis Arduino dan modul pendingin Peltier dengan kontrol ON/OFF aktif untuk menjaga stabilitas suhu 2–8°C saat membawa vaksin ke kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/harrisroby/peltier-vaccine-carrier) *(HTTP 200)*

- [ ] **Pharma ColdChain IIoT Pipeline (`chahinezachiou76/Pharma-ColdChain-IIoT`)** — `[Masalah #1]` `[IIoT Cold Chain / MQTT Mosquitto + OPC UA + Terraform]`
  - **Ringkasan:** Arsitektur *data pipeline* IIoT *end-to-end* untuk pemantauan suhu rantai dingin vaksin secara *real-time* menggunakan protokol MQTT (Mosquitto), OPC UA, dan otomasi *cloud* Terraform.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/chahinezachiou76/Pharma-ColdChain-IIoT) *(HTTP 200)*

- [ ] **Vaccine Temperature Monitoring IoT (`MananDesai28/Vaccine-Temperature-Monitoring-System-using-IoT`)** — `[Masalah #1]` `[IoT Cold Chain / ESP32 Real-Time Alert]`
  - **Ringkasan:** Purwarupa pemantau suhu dan kelembapan penyimpanan vaksin berbasis ESP32 dengan peringatan dini saat suhu melewati ambang aman 2–8°C.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/MananDesai28/Vaccine-Temperature-Monitoring-System-using-IoT) *(HTTP 200)*
