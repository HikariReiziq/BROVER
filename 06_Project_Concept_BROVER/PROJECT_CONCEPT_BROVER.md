# BROVER (*Broiler Biosecurity & Health Rover*) : Sistem Inspeksi Berkala Berbasis *Hybrid Edge–Cloud* dan *Multi-Modal AI* untuk Deteksi Dini Gejala Penyakit Endemik, Triase Biosekuriti, dan Pemantauan Mikroklimat Kandang Ayam Broiler

---

## 1. Judul, Identitas Tim, & Standar Transparansi Dokumen

- **Judul Final Proyek:**  
  **`BROVER (Broiler Biosecurity & Health Rover) : Sistem Inspeksi Berkala Berbasis Hybrid Edge–Cloud dan Multi-Modal AI untuk Deteksi Dini Gejala Penyakit Endemik, Triase Biosekuriti, dan Pemantauan Mikroklimat Kandang Ayam Broiler`**
- **Program & Jalur Kompetisi:** Hackathon Deep Tech UNJ 2026 — Jalur Pangan **`D-FARM UNJ`** (*Challenge #1: Smart Poultry Production*)
- **Tim Pengusul:** **Tim MBOYZ** (Teknologi Informasi — Universitas Negeri Jakarta)
  1. **M. Hikari Reiziq Rakhmadinta** *(Mahasiswa Teknologi Informasi)*
  2. **Arya Bisma Putra Refman** *(Mahasiswa Teknologi Informasi)*
  3. **Ahmad Syauqi Reza** *(Mahasiswa Teknologi Informasi)*
  4. **Aditya Reza Daffansyah** *(Mahasiswa Teknologi Informasi)*
  5. **Slot Ke-5 *(Wajib Dilengkapi Sebelum Pendaftaran Nov 2026)*:** **Minimal 1 Dosen Aktif UNJ** sesuai syarat legal-administratif Buku Pedoman Hackathon Deep Tech UNJ 2026 (`[Pedoman, Hal. 3]`).
- **Ruang Lingkup Mutlak (*Hard Constraints*):**
  - Fokus 100% pada **peternakan ayam pedaging (*broiler*)** — kompatibel untuk kandang ***open house*** maupun ***closed house*** di Indonesia.
  - **Tidak** mencakup jalur kesehatan manusia (`D-MARC`), **tidak** mencakup topik pengolahan limbah/sampah (*waste-to-value*, kompos, biogas, maggot), dan **tidak** menggunakan sensor tembak suhu tubuh inframerah (*thermogun/IR*).
- **Standar Transparansi (*Provenance Tags*):** Seluruh tabel, grafik, dan analisis dalam dokumen ini mematuhi 4 label transparansi:
  - **`[ASLI DARI SUMBER PRIMER]`** — Grafik/data diambil utuh tanpa modifikasi dari sumber resmi.
  - **`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`** — 100% angka berasal dari BPS, Kementan RI, PT Medion, *datasheet* resmi, atau jurnal *peer-reviewed* terverifikasi.
  - **`[SUARA LAPANGAN DARING — NON-PEER-REVIEWED]`** — Kesaksian praktisi/peternak Indonesia dari wawancara berita/YouTube untuk triangulasi realitas lapangan.
  - **`[SINTESIS REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT]`** — Rancangan arsitektur, alur kerja, *power budget*, BMC, dan roadmap TKT yang disusun untuk validasi dan eksekusi tim.

> **Ringkasan Eksekutif:** `BROVER` adalah sistem inspeksi berkala berbasis *rover* darat berkecepatan rendah (`≤0,1 m/s`) dengan arsitektur ***Hybrid Edge–Cloud (Offline-First)*** untuk peternakan ayam broiler di Indonesia. Sistem ini menyasar **Masalah #1 (Wabah Penyakit Endemik & Lemahnya Biosekuriti)** sebagai fokus utama melalui **3 model AI ringan sekuensial** (Visi Komputer feses abnormal, Visi Komputer gejala fisik/ayam lesu & mati, serta ***Zone-Scheduled Acoustic AI*** 5 detik untuk deteksi dini suara ngorok CRD/IB/ND) dan menyasar **Masalah #2 (Cekaman Panas/*Heat Stress* & Mikroklimat Tropis)** secara pasif melalui sensor `SHT31` (indeks THI), indikator tren gas amonia `DFRobot SEN0567`, serta integrasi prakiraan cuaca `Open-Meteo`. Seluruh keputusan didesain ***Human-in-the-Loop*** (didukung *Disease Triage Dictionary* berbasis Manual Penyakit Unggas Kementan RI) dan bebas *overclaim*—termasuk strategi 2 fase jujur dari **Prototipe PoC (`Raspberry Pi 4` + `ESP32` + Kit 4WD, TKT 3–4)** menuju **Rencana Final Komersial (`Orange Pi 3B` NPU 0,8 TOPS + `ESP32` + *Custom Carrier PCB* + `LiFePO₄` + penggerak medan sekam, TKT 6–9)**.

---

## 2. Latar Belakang

Sektor perunggasan merupakan tulang punggung utama pemenuhan protein hewani terjangkau di Indonesia. Berdasarkan data resmi **Badan Pusat Statistik (BPS) 2025** dan telaah ilmiah nasional (Sumiati *et al.*, *Animal Bioscience* Q1, 2025), populasi **ayam ras pedaging (*broiler*)** nasional menembus **3,32 miliar ekor/tahun** (`3.323.003.798` ekor) dengan produksi daging mencapai **4,06–4,28 juta ton/tahun** — jauh melampaui subsektor unggas lainnya (sebagai pembanding, populasi ayam ras petelur tercatat 426,12 juta ekor dengan produksi 6,31 juta ton telur).

Namun, struktur produksi broiler di Indonesia masih terbelah tajam secara teknologi: sekitar **60% pasokan** berasal dari peternakan industrial skala besar (*closed house*), sedangkan **~40% sisanya** ditopang oleh **lebih dari 1 juta peternak kecil–menengah** yang mayoritas masih mengoperasikan kandang terbuka (*open house*) dengan pengawasan manual (Sumiati *et al.*, 2025). Di sisi lain, inovasi kandang *closed house* bahan lokal untuk peternak rakyat juga mulai berkembang—seperti **KANOPIS** milik mitra industri Hackathon Deep Tech UNJ 2026, **PT Zara Propertifarm Indonesia**, yang telah tervalidasi pada 6 farm di Bogor (`85.000 ekor`) dan pengakuan kapasitas awal JAPFA (`300.000 ekor`)—namun manajemen pemantauan kesehatan harian di dalam kandang masih menjadi tantangan operasional kritis menuju TKT 9 ([04_MITRA_PT_ZARA_PROPERTIFARM.md](../01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md)).

Di tengah margin usaha peternak broiler mandiri yang sangat tipis—dengan **biaya pakan (62,27%–67,67%) dan DOC (26,10%–30,47%) menyerap 92,74%–93,77% total biaya produksi** (Junaidi *et al.*, *JWPR*, 2023)—keterlambatan deteksi wabah penyakit selama 24–72 jam saja dapat langsung menghapus keuntungan beberapa siklus sekaligus. Sementara itu, solusi robotika komersial luar negeri (seperti *ChickenBoy* Big Dutchman berbasis rel plafon atau *Octopus XO* Prancis berbobot ~80 kg) memiliki harga dan kompleksitas yang tidak terjangkau bagi peternak rakyat Indonesia. Diperlukan pendekatan rekayasa ***Demand-Driven DeepTech*** yang jujur, tahan terhadap keterbatasan sinyal internet dan listrik pedesaan, hemat biaya produksi, serta selaras dengan kapabilitas rekayasa perangkat lunak, AI, dan IoT Tim MBOYZ.

---

## 3. Masalah

Berdasarkan hasil riset sistematis dan triangulasi 35 artikel jurnal *peer-reviewed* Indonesia (2021–2026) dengan 20 sumber lapangan daring ([TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md](../02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md)) serta bedah *Root Cause Analysis* ([ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md](../03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md)), **`BROVER` memfokuskan solusi pada 2 masalah teknis-operasional paling stabil dan destruktif di Indonesia**:

### 3.1. Masalah Utama (#1) — Wabah Penyakit Endemik & Lemahnya Biosekuriti Kandang Rakyat

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

1. **Dampak Ekonomi Katastrofik per Wabah:** Pada pemodelan bio-ekonomi farm broiler Sektor 3 di Jawa Bagian Barat (skala 3.000 ekor, margin kotor normal hanya **Rp5,28 juta/siklus**), **1 kali wabah HPAI H5N1** membalik keuntungan menjadi kerugian rata-rata hingga **−Rp53,89 juta** (*tanpa tindakan*) hingga **−Rp57,35 juta** (*stamping out* tanpa kompensasi), mendorong peternak melakukan *panic selling* ayam sakit (**−Rp22,89 juta**) yang memperluas endemisitas regional (Pramuwidyatama *et al.*, *Prev. Vet. Med.* Q1, 2023).
2. **Dominasi Penyakit Pernapasan & Pencernaan di Broiler Indonesia:** Berdasarkan surveilans laboratorium nasional **PT Medion TEC (Januari 2026)**, penyakit positif PCR nasional dipimpin oleh ***Infectious Bronchitis* (IB ~17,7%)**, ***Avian Paramyxovirus* (AP ~14,8%)**, ***Newcastle Disease* (ND ~14,1%)**, **IBD/Gumboro (~10,6%)**, dan **AI H5N1 (~9,9%)**. Secara spesifik pada insiden klinis **ayam broiler (2023–Nov 2025)**, 3 penyakit teratas adalah **CRD / ngorok (>31%)**, **Colibacillosis (~17%)**, dan **Coccidiosis (~12%)**.

![Grafik Asli Surveilans Positif PCR Nasional 2025 — PT Medion TEC](./assets/01_medion_pcr_nasional_2025_asli.png)
*`[ASLI DARI SUMBER PRIMER]` Grafik 4 — Rangking Penyakit Pedaging & Petelur Positif PCR Nasional Jan–Nov 2025, disalin utuh dari [PT Medion TEC (Januari 2026)](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/).*

![Grafik Asli Ranking Penyakit Klinis Ayam Broiler 2023–Nov 2025 — PT Medion TEC](./assets/02_medion_broiler_klinis_2025_asli.png)
*`[ASLI DARI SUMBER PRIMER]` Grafik 1 — Rangking Penyakit Ayam Pedaging (Broiler) 2023–Nov 2025, disalin utuh dari [PT Medion TEC (Januari 2026)](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/), mengonfirmasi dominasi CRD (>31%), Colibacillosis (~17%), dan Coccidiosis (~12%).*

3. **Kepatuhan Biosekuriti & Literasi Pekerja Sangat Lemah:** Studi longitudinal 19 farm broiler (153 siklus) di Jawa Barat mengungkap skor **biosekuriti eksternal rata-rata hanya `0,28/1,0`**, pergerakan/pembelian **`0,48/1,0`**, dan **pekerja & peralatan `0,50/1,0`**; seluruh **4 farm dengan skor biosekuriti terendah akhirnya gulung tikar** (Anwar Sani *et al.*, *Poultry Science* Q1, 2025). Sementara itu, survei 200 pekerja kandang unggas Indonesia menunjukkan **`58%` pekerja** berada pada tingkat pengetahuan *Avian Influenza* kategori *Low–Moderate* (`33% Low`, `25% Moderate`) (Rehman *et al.*, *PeerJ* Q1, 2023).
4. **Koinfeksi & Deteksi Terlambat di Lapangan:** Penyakit di kandang Indonesia kerap muncul sebagai koinfeksi multifaktorial—seperti temuan studi kasus 11.000 broiler di Majalengka yang mengalami **koinfeksi simultan AI H5 + AI H9 + IB (CV antibodi 256%) + *M. gallisepticum* (31,25%) + koksidiosis (4.400 OPG)** di bawah tekanan amonia **20 ppm** (Hartady *et al.*, *Vet. Sci.* Q1, 2026). Akibat pengamatan visual kasatmata yang terlambat dan kemiripan gejala luar, peternak sering salah duga (misal kasus *Hari Farm*: wabah AI awalnya disangka snot hingga kematian melonjak 4→80 ekor/hari; `[SUARA LAPANGAN DARING]` TROBOS Livestock, 2024) dan mengandalkan antibiotik profilaktik/flushing sembarangan (`75,0%` *flushing*, hanya `8,3%` terapi terarah; Efendi *et al.*, *Vet. World* Q1, 2022).

### 3.2. Masalah Pasif (#2) — Cekaman Panas (*Heat Stress*) & Instabilitas Mikroklimat Tropis

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

1. **Tekanan Iklim Tropis Sepanjang Tahun:** Nilai rata-rata bulanan *Heat Stress Index* (HSI) Indonesia tahun 2023 melampaui ambang nyaman (`<150–160`) **di seluruh 12 bulan**, mencapai **155,5–165,4 (puncak 187,8)** di Indonesia Barat dan **150,0–166,4 (puncak 195,0)** di Indonesia Timur dengan suhu puncak `36°C` (Sumiati *et al.*, 2025).
2. **Bahkan Kandang *Closed House* Mengalami Gradien Mikroklimat Parah:** Pada 14 farm *closed/semi-closed house* di Jawa Barat (`2.104 ekor`, `84 titik ukur`), **`0,0%`** titik ukur berada di zona nyaman termal (`THI <72`), sementara **`62,0%` berada di zona *Severe Discomfort*** dan **`8,3%` *Life-Threatening* (`THI >85`)**, dengan kelembapan rerata **`81,9%` (`66%–96%`)**, `NH₃` `7,3 ± 6,4 ppm`, serta lesi *Foot-Pad Dermatitis* (FPD) mencapai **`40%`** akibat *wet litter* (Wilcox *et al.*, *Animal Welfare* Q1, 2025).
3. **Korelasi Langsung ke Mortalitas & FCR:** Di Jawa Tengah, analisis ROC membuktikan **suhu sore pukul 16:00 `>32,8°C`** (`AUC 0,694`, `p = 0,026`) dan **THI pukul 16:00 `>79`** (`AUC 0,709`, `p = 0,016`) signifikan memprediksi kematian broiler, sementara kadar air *litter* di dataran rendah mencapai **`46,42%`** dengan `NH₃` `13,11–14,94 ppm` (Mohammadi *et al.*, *AAVS*, 2026; Hasibuan *et al.*, *JSPI*, 2021). Kondisi mikroklimat ekstrem ini secara langsung **merusak silia trakea dan memicu lingkaran setan (*vicious cycle*) koinfeksi Masalah #1**.

---

## 4. Solusi (`BROVER`)

**`BROVER` (*Broiler Biosecurity & Health Rover*)** menghadirkan sistem inspeksi kandang berkala berbasis **kendaraan darat berkecepatan rendah (`≤0,1 m/s`)** dengan arsitektur ***Hybrid Edge–Cloud (Offline-First)*** untuk membantu peternak ayam broiler (*open* maupun *closed house*) mendeteksi tanda awal wabah penyakit dan ketimpangan mikroklimat per zona kandang sebelum meluas.

![Arsitektur Sistem BROVER — Hybrid Edge-Cloud & Offline-First](./assets/03_arsitektur_sistem_brover.png)
*`[SINTESIS REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT]` Diagram blok arsitektur Hybrid Edge–Cloud BROVER: pemisahan Real-Time MCU (`ESP32`) + Edge AI SBC (`RPi 4` PoC / `Orange Pi 3B` Final) + Backend `Golang` efisien + Aplikasi `Next.js` PWA.*

### 4.1. Empat Pilar Fungsional Utama `BROVER`

1. **Inspeksi Visual 2-Fungsi dengan 1 Kamera + 1 Servo *Tilt* (Computer Vision):**
   - **Posisi Bawah (`~45°`) saat bergerak pelan (`≤0,1 m/s`):** Memindai permukaan sekam jarak `30–50 cm` di depan roda untuk mendeteksi kandidat **feses abnormal** (indikasi berdarah/koksidiosis, diare putih-kapur, diare kehijauan) dengan verifikasi 2-tahap (*soft pause* + LED putih 5000K CRI >90 + *majority voting* 3–5 frame).
   - **Posisi Mendatar (`~0–15°`) saat *soft pause*:** Servo mengangkat kamera untuk memindai **gejala fisik eksternal, ayam lesu/menyendiri, dan kandidat ayam mati (*carcass*)** di kiri–kanan celah baris.
2. ***Zone-Scheduled Acoustic AI* (Deteksi Dini Pernapasan CRD/IB/ND):**
   - Berdasarkan data patologi unggas (`[Mekanisme Biologis Umum]`), suara pernapasan abnormal (*ngorok/rales*, bersin, batuk) muncul **lebih awal** dibanding gejala fisik berat di kamera, serta dapat ditangkap dari radius **3–5 meter menembus kerumunan ayam** dengan konsumsi daya sensor **15–50× lebih rendah** dibanding CV.
   - Setiap menempuh jarak tetap (`5–10 meter` / per zona), `BROVER` melakukan ***stop–mute–sample* 5 detik** (motor & kipas SBC mati total) untuk merekam & mengklasifikasi klip audio 5 detik (*Healthy / Indikasi Respirasi / Derau Kipas*). Jika audio mendeteksi ngorok, sistem otomatis memicu pemindaian CV intensif di zona tersebut.
3. **Pemantauan Mikroklimat Pasif & Integrasi Prakiraan Cuaca Preventif:**
   - Secara pasif selama inspeksi berlangsung, `BROVER` merekam **Suhu & Kelembapan Relatif (`SHT31`)** pada ketinggian aktual ayam (*bird-level*) untuk menghitung **THI** per zona, disertai pemantauan **indikator tren lonjakan gas Amonia (`DFRobot SEN0567`)** dengan kompensasi suhu/RH.
   - Backend secara berkala menarik prakiraan cuaca per-jam 3–7 hari ke depan dari **[Open-Meteo API](https://open-meteo.com/)** (dengan *cache* lokal 3–7 hari di rover) untuk menghasilkan **rekomendasi preventif** bagi peternak (mis. persiapan ventilasi/tirai/elektrolit sebelum puncak panas pukul 11.00–16.00).
4. **Protokol Biosekuriti 1-Kandang & *Human-in-the-Loop Disease Triage Dictionary*:**
   - Menerapkan kebijakan **1 Unit = 1 Kandang (*Dedicated Single-House Unit*)**, alur gerak tanpa melindas feses klinis segar, SOP sanitasi roda berbasis sains veteriner (sikat mekanis sebelum disinfeksi), **log kepatuhan biosekuriti digital**, serta ***Disease Triage Dictionary*** berbasis **[Manual Penyakit Unggas Ditjen PKH Kementan RI](https://wiki.isikhnas.com/images/d/dd/Manual_Penyakit_Unggas.pdf)** dan **[PT Medion TEC](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/)** dilengkapi **tombol ekspor 1-klik paket bukti (foto + klip audio 5 detik + grafik THI/NH₃) ke WhatsApp TSO/Dokter Hewan**.

### 4.2. Pagar Kejujuran & Batasan Operasional (Prinsip *Anti-Fake Innovation*)

`[SINTESIS REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT]`

Menjawab langsung peringatan **Anti-*Fake Innovation*** dari Mitra PT Zara Propertifarm Indonesia ([04_MITRA_PT_ZARA_PROPERTIFARM.md](../01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md#L108-L113)), `BROVER` menetapkan 5 batasan jujur berikut sejak awal:

| Aspek | Batasan Jujur yang Diterapkan `BROVER` | Bukti Ilmiah / Teknis Pendukung |
| :--- | :--- | :--- |
| **Fase Umur Operasi Lantai** | Inspeksi lantai terjadwal difokuskan pada **hari ke-5 s.d. ~23** (kecepatan `≤0,1 m/s`, bukan 24 jam nonstop). | Robot broiler komersial *Octopus XO* menetapkan operasi **hari ke-5–23** pada kecepatan `0,04–0,12 m/s` ([FAQ Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/)); mulai minggu ke-4–5 kepadatan broiler mencapai `13–30 kg/m²` ([PT Medion](https://www.medion.co.id/info-medion/closed-house-solusi-peningkatan-performa-ayam/)) dan ayam makin lamban bergeser ([PMC11011048](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/)). |
| **Klaim Biosekuriti Roda** | **Tidak mengklaim** *"melindas feses tampak sehat = roda steril"*. Biosekuriti ditegakkan lewat **1 unit/kandang** + **sikat mekanis & disinfeksi terjadwal**. | Fenomena ***subclinical/asymptomatic fecal shedding*** membuat feses tampak normal tetap bisa membawa *Salmonella*, NDV, atau *Eimeria* ([PMC13433518](https://pmc.ncbi.nlm.nih.gov/articles/PMC13433518/); [PLOS ONE, 2022](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0264028)); ookista *Eimeria* kebal disinfektan umum ([PMC11416347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/)). |
| **Klaim Diagnosis AI** | Output aplikasi adalah **Skrining/Triase Dini (*Human-in-the-Loop*)**, **bukan** diagnosis medis otomatis dan **tidak** meresepkan dosis antibiotik. | Kemiripan gejala koinfeksi lintas penyakit (mis. kasus Hari Farm AI dikira snot, [TROBOS 2024](https://troboslivestock.com/virus-ai-terus-mengintai/)) serta efek *domain shift* lintas kandang ([Henomaly](https://github.com/RishitRai/Henomaly): akurasi turun 99%→75–78%). |
| **Pengukuran Gas `NH₃`** | Sensor **`DFRobot SEN0567`** (~Rp240–330 rb) dilaporkan jujur sebagai **indikator tren kualitatif lonjakan `NH₃`** (dengan kompensasi Suhu/RH), bukan angka `ppm` absolut sertifikasi lab. | [Wiki Resmi DFRobot `SEN0567`](https://wiki.dfrobot.com/sen0567/) menyatakan eksplisit: *"Qualitative only—for quantitative, buy the Factory-calibrated Gas Sensor."* |
| **Status Kit 4WD Akrilik** | Kit 4WD akrilik + roda 65 mm (*ground clearance* 1,3–1,5 cm) hanya digunakan sebagai ***indoor PoC testbed* (TKT 3–4)**, **bukan** unit uji sekam basah lapangan. | Sekam broiler tebal `5–10 cm` (kadar air hingga `46,42%`, Hasibuan *et al.*, 2021) mensyaratkan upgrade motor *metal-gear* + roda *off-road*/*track* (*ground clearance* ≥5–6 cm) pada fase Bootcamp (TKT 5–6). |

---

## 5. Tech Stack

Pemilihan tumpukan teknologi `BROVER` menyeimbangkan **kecepatan pengembangan 4 mahasiswa TI**, **hemat daya di atas baterai rover**, dan **efisiensi biaya operasional server komersial**:

`[SINTESIS ARSITEKTUR SOFTWARE TIM MBOYZ — DISUSUN OLEH AI AGENT]`

| Lapisan Sistem | Teknologi Terpilih | Peran Spesifik & Justifikasi Teknis |
| :--- | :--- | :--- |
| **1. Firmware MCU (*Real-Time*)** | **`C++`** (`PlatformIO` / Arduino Framework pada **`ESP32`**) | Mengendalikan PWM/PID motor pelan (`≤0,1 m/s`), *hardware watchdog* (cutoff otomatis bila SBC *hang* >1 dtk), *stall protection* (*encoder* + arus), servo *tilt*, LED 5000K, serta pembacaan `SHT31` (I2C), `SEN0567` (ADC + kompensasi T/RH), `A02YYUW`/`HC-SR04`, dan `INA219`. Berkomunikasi via **UART Serial** ke SBC. |
| **2. Edge AI & Orchestrator (Di Atas Rover)** | • **Fase PoC (`RPi 4`):** **`Python 3`**, `OpenCV`, `NumPy/SciPy`, **`Ultralytics NCNN`**, `SQLite (WAL Mode)`, `Paho-MQTT`<br>• **Fase Final (`Orange Pi 3B`):** **`Golang` (*Edge Daemon/Orchestrator*)** + **`C++` (`rknn-toolkit-lite2` / RKNN C-API)** + `SQLite (WAL Mode)` | Pada fase PoC, Python mempercepat integrasi; pada fase Final, memindahkan manajemen UART/SQLite/MQTT/sync ke **`Golang`** dan inferensi NPU ke **`C++` RKNN** meminimalkan beban CPU/RAM sehingga menghemat baterai `LiFePO₄`. Mode `SQLite WAL` menjamin operasi **100% *Offline-First*** (>30 hari *ring-buffer* di eMMC). |
| **3. Training & Konversi Model AI** | **`PyTorch`**, **`Ultralytics`**, **`torchaudio` / `librosa`**, `ONNX`, `rknn-toolkit2` *(dijalankan di PC/Laptop ber-GPU lokal Tim MBOYZ)* | Pelatihan *offline* 3 model AI sekuensial: (1) CV Feses (`YOLOv8n/11n`), (2) CV Ayam Lesu/Mati & Gejala Fisik (`YOLOv8n/11n`), (3) Audio Respirasi 5 detik (`Log-Mel Spectrogram` + `MobileNetV3-Small` / `2D CNN`), lalu dikuantisasi **INT8** ke format **NCNN** (PoC) atau **RKNN** (Final). |
| **4. Backend Server Pusat & Broker** | **`Golang`** (`Fiber` / `Gin` / `Chi`), **`PostgreSQL`** (`pgx`), **`Eclipse Mosquitto`** (MQTT Broker), **`MinIO / S3`**, **`Open-Meteo API`**, Bot WhatsApp/Telegram | Karena 100% inferensi AI berlangsung di *Edge*, backend pusat tidak membutuhkan library ML Python. **`Golang`** (*compiled binary*, RAM *idle* hanya `~15–30 MB`, *goroutine* konkuren ringan) mampu melayani telemetri MQTT, penyimpanan foto/audio, *polling* cuaca `Open-Meteo`, dan notifikasi alert dari puluhan–ratusan kandang hanya pada **1 VPS hemat biaya** (sangat menguatkan struktur biaya BMC). |
| **5. Frontend Aplikasi Peternak** | **`Next.js` (React + Tailwind CSS)** berformat **PWA (*Progressive Web App*)** | **1 basis kode** langsung berfungsi mulus di **HP Android peternak** (ringan di jaringan 3G/4G pedesaan, dapat di-install ke *home screen*, mendukung *push notification*) sekaligus di **browser desktop** pemilik farm & dewan juri. Menyediakan peta zona kandang, galeri foto + pemutar audio 5 detik + tombol validasi *"Benar/Bukan"*, grafik THI & tren NH₃ + prakiraan cuaca, *Disease Triage Dictionary*, log biosekuriti, dan ekspor 1-klik ke WA TSO/Dokter Hewan. |

---

## 6. Cara Kerja

### 6.1. Pola Navigasi di Kandang Broiler & Alur 4-Lapis Biosekuriti

![Pola Navigasi Huruf U & Alur Kerja 4-Lapis Biosekuriti BROVER](./assets/04_alur_kerja_4lapis_biosekuriti.png)
*`[SINTESIS REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT]` (A) Pola navigasi huruf U/zig-zag menyusuri celah antar-baris pan feeder & nipple drinker dengan putar balik di ujung kandang 3–4 m; (B) Alur kerja 4-lapis biosekuriti & triase multi-modal.*

```mermaid
flowchart TD
    A["Mulai Sesi Inspeksi Terjadwal dari Cleaning Dock (<=0,1 m/s)"] --> B["Susuri Celah Antar-Baris Pan Feeder & Nipple (Pola Huruf U)<br/>CV Feses Aktif Ringan (3-5 FPS) | Audio MATI"]
    B --> C{"Pemicu Berhenti?"}
    C -- "Tiap 5-10 m (Zone-Scheduled)" --> D["SOFT PAUSE 5 Detik (Motor & Kipas SBC MATI)<br/>1. Rekam & Klasifikasi Audio Respirasi 5 dtk<br/>2. Baca SHT31 (Suhu/RH/THI) & SEN0567 (Tren NH3)"]
    C -- "Kandidat Feses 30-50 cm" --> E["SOFT PAUSE 3-5 Detik + Nyalakan LED 5000K CRI >90<br/>Ambil 3-5 Frame Voting CV Feses + Cek Audio 5 dtk"]
    D --> F{"Audio Terdeteksi<br/>Ngorok / Bersin?"}
    F -- "Normal" --> G["Servo Angkat Kamera (1x Jepret Postur Ayam)<br/>Lanjut Inspeksi"]
    F -- "Positif Ngorok" --> H["Servo Scan CV Gejala Fisik/Ayam Lesu Intensif<br/>Naikkan Skor Risiko Zona"]
    E --> I["Multi-Modal Zone Risk Fusion Engine (0-100)"]
    H --> I
    G --> B
    I -- "HIJAU (0-39)" --> B
    I -- "KUNING (40-69)<br/>Conf. 60-79% Tunggal" --> J["Simpan Foto + Koordinat Zona (Passive Log)<br/>Hindari Bercak & Lanjut Inspeksi"]
    I -- "MERAH (70-100)<br/>Conf. >=80% / Berdarah / Klaster / Ngorok" --> K["JANGAN Melindas Bercak -> Mundur Aman 20-30 cm<br/>Kirim Push Alert + Foto + Audio + Peta Zona ke PWA"]
    K --> L["Human-in-the-Loop: Peternak Cek Radius 2-3 m +<br/>Disease Triage Dictionary (Kementan/Medion) -> Ekspor WA TSO/Vet"]
    L --> M["Kembali ke Cleaning Dock -> SOP 3-Langkah Sanitasi Roda<br/>(Sikat Mekanis -> Disinfeksi -> Keringkan) + Centang Log Digital"]
```

### 6.2. Urutan Detail Eksekusi per Sesi Inspeksi

1. **Inisiasi & Gerak Pelan Berbasis Habituasi (`≤0,1 m/s`):** Berdasarkan studi *peer-reviewed* broiler terhadap robot darat (*AviSense*, [PMC13696172](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/); *RobôFrango*, [PMC11011048](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/)), paparan rutin robot berkecepatan rendah sejak awal siklus (hari ke-5) memicu pembiasaan (*habituation*) dan tidak mengubah perilaku alami ayam. Mengikuti tata letak standar [Cobb](https://www.cobbgenetics.com/assets/Cobb-Files/2024-Nipple-Drinker-Poster.pdf) dan [Aviagen Ross](https://aviagen.com/assets/Tech_Center/Ross_Broiler/Aviagen-ROSS-Broiler-PocketGuide-EN.pdf) (jarak antar-baris alat ±1,2–3,0 m; ruang ujung kandang 3–4 m), rover melaju lurus di celah antar-baris *pan feeder* dan *nipple drinker* lalu memutar di ujung kandang (tidak memotong menyamping di bawah pipa rendah).
2. ***Zone-Scheduled Audio* Memicu CV Intensif:** Saat berjalan, mikrofon dimatikan agar bebas bising roda. Setiap `5–10 meter` (berbasis *Hall Encoder* / odometri), motor dan kipas SBC berhenti total selama **5 detik** untuk merekam audio 5 detik (sesuai struktur segmen [SmartEars](https://data.mendeley.com/datasets/dy6gtvt4mk/2)) + membaca `SHT31` & `SEN0567`. Jika audio mendeteksi indikasi ngorok/bersin, servo langsung mengangkat kamera untuk pemindaian gejala fisik/ayam lesu lebih intensif di zona tersebut.
3. **Verifikasi 2-Tahap CV Feses & *Multi-Modal Risk Fusion*:** Jika kamera depan (miring 45°) menangkap kandidat feses abnormal pada jarak `30–50 cm`, rover melakukan *soft pause* 3–5 detik, menyalakan LED putih 5000K CRI >90 untuk menghilangkan bias cahaya redup kandang, lalu menjalankan *majority voting* 3–5 frame yang digabung dengan audio & mikroklimat menjadi **3 Level Risiko**:
   - **Hijau (`0–39`):** Normal → masuk log rutin → lanjut inspeksi.
   - **Kuning (`40–69`, *conf.* 60–79% tunggal):** Simpan foto bukti & koordinat zona sebagai ***Passive Log*** (peternak dapat memberi label *"Benar/Bukan"* untuk *active learning*) → hindari bercak & lanjut tanpa mengganggu peternak dengan *false alarm*.
   - **Merah (`70–100`, *conf.* ≥80% / feses berdarah / klaster ≥3 titik / +audio ngorok):** Rover **berhenti sebelum melindas bercak**, mundur aman `20–30 cm`, mencari jalur pulang/alternatif, dan mengirim **Push Alert + Foto + Klip Audio + Peta Zona (`Jalur X, ±Y meter`)** ke PWA peternak.
4. **Tindak Lanjut *Human-in-the-Loop* & SOP Sanitasi Roda Veteriner:** Peternak langsung menuju radius `2–3 meter` titik alert, memeriksa ayam lesu/menyendiri berpanduan *Disease Triage Dictionary* ([Manual Penyakit Unggas Kementan RI](https://wiki.isikhnas.com/images/d/dd/Manual_Penyakit_Unggas.pdf)), memisahkan ayam ke petak isolasi, dan menekan tombol ekspor 1-klik ke WhatsApp TSO/Dokter Hewan. Saat rover kembali ke *Cleaning Dock* di zona dalam kandang, aplikasi mengingatkan SOP 3-langkah berbasis bukti [PMC11416347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/) & [PMC12414267](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/) (karena ookista *Eimeria* kebal disinfektan biasa): **(1) sikat fisik/mekanis sekam dari alur ban → (2) semprot disinfektan spektrum luas → (3) keringkan penuh**, lalu centang log kepatuhan digital.

### 6.3. Mitigasi 7 Skenario *Worst-Case* Lapangan

`[SINTESIS REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT]`

| No | Skenario *Worst-Case* | Mekanisme Mitigasi pada `BROVER` |
| :-: | :--- | :--- |
| **1** | **Internet / Wi-Fi Kandang Mati Berhari-hari** | 100% *Offline-First*: 3 model AI jalan lokal, *ring-buffer* `SQLite WAL` di eMMC 32GB (>30 hari, otomatis jaga log Merah), *cache* cuaca 3–7 hari, serta **LED Merah + Buzzer fisik** di bodi & *dock*. |
| **2** | **Listrik PLN Padam (*Blackout* 5 Jam – 3 Hari)** | Saat *dock* kehilangan tegangan PLN, rover masuk ***Emergency Low-Power Mode*** (motor mati agar baterai `LiFePO₄` bertahan >12–24 jam, sensor Suhu/RH/NH₃ + alarm darurat tetap siaga memantau lonjakan panas). |
| **3** | **Roda Macet (*Stall*) di Sekam atau Baterai Habis di Tengah Flok** | Auto *Return-to-Dock* pada `25%` baterai (`INA219`); *stall detection* (*encoder* diam >2 dtk saat PWM aktif → mundur 15 cm & belok; gagal 3× → *cutoff* motor + kirim koordinat + *beep* pencari). |
| **4** | ***Domain Shift* & *False Positive* di Kandang Baru** | Pencahayaan standar LED 5000K CRI >90 + *fine-tuning* 300–500 foto sekam/feses lokal Indonesia saat Bootcamp + tombol konfirmasi *"Benar/Bukan"* di PWA (*active learning*). |
| **5** | **SBC *Crash* / RAM Penuh / *Overheat* di Suhu 35°C** | 3 model INT8 (<50 MB total) sangat lega di RAM 4GB; **`ESP32` *Hardware Watchdog*** memutus motor jika *heartbeat* SBC hilang >1 dtk & memicu *reboot*; beban `RK3566` rendah (`3,5–4,5 W`) dengan *heatsink*. |
| **6** | **MicroSD Korup Akibat Getaran / Mati Mendadak** | Versi Final memakai **eMMC bawaan `Orange Pi 3B`** (tahan getaran & siklus tulis tinggi) + transaksi `SQLite WAL`. |
| **7** | **Korosi Amonia (`NH₃`), Kelembapan 96%, & Debu Bulu** | Casing tertutup IP54–IP65 + ***Custom Carrier PCB* berlapis *Conformal Coating*** + probe `SHT31 FS304` berfilter + *splash-shield* busa di lubang mikrofon. |

---

## 7. Prototype (Fase PoC Awal — TKT 3–4, Seleksi Nov 2026)

Sesuai ketentuan fleksibilitas pendaftaran Buku Pedoman Hackathon Deep Tech UNJ 2026 (`TKT 3–4` diperbolehkan pada tahap seleksi proposal Nov 2026; [02_HACKATHON_DFARM_RULES.md](../01_Context_Memory/02_HACKATHON_DFARM_RULES.md#L95-L98)), fase **Prototype (PoC)** memaksimalkan **perangkat keras yang sudah dimiliki Tim MBOYZ** untuk membuktikan *end-to-end software*, inferensi 3 model AI, fusi risiko, dan integrasi PWA di permukaan uji simulasi (*indoor testbed*).

![Kit Smart Chassis 4WD Eksisting Tim MBOYZ untuk Fase PoC TKT 3–4](./assets/07_kit_4wd_poc_eksisting.jpg)
*`[DOKUMENTASI HARDWARE TIM MBOYZ]` Kit Smart Chassis 4WD akrilik (4× motor TT 1:48 + roda 65 mm) yang telah dimiliki tim sebagai platform PoC testbed awal (TKT 3–4) di lantai uji simulasi.*

### 7.1. Daftar Komponen Lengkap Versi Prototype Awal (PoC — TKT 3–4)

`[DATA DATASHEET & INVENTARIS TIM — DISUSUN OLEH AI AGENT]`

| Subsistem | Komponen Terpilih | Status Stok Tim | Spesifikasi Kunci & Alasan Teknis |
| :--- | :--- | :---: | :--- |
| **Edge AI SBC** | **`Raspberry Pi 4`** + *Heatsink* + MicroSD 32GB A2 | **Sudah Dimiliki** | Menjalankan `YOLOv8n` **NCNN (~2,3 FPS, 414–433 ms)** ([Ultralytics Docs](https://docs.ultralytics.com/guides/raspberry-pi/)) + Audio 5 dtk + `SQLite WAL`. Stabil & nol risiko *stuck* driver untuk tenggat Nov 2026. |
| **Real-Time MCU** | **`ESP32` (Standar)** *(via kabel USB Serial ke RPi 4)* | **Sudah Dimiliki** | Menutupi 3 batas GPIO `RPi 4` (0 pin ADC bawaan, hanya 2 kanal hardware PWM, pin 3,3V rawan 5V) sekaligus menjadi *safety watchdog*. |
| **Sasis & Penggerak** | **Kit Smart Chassis 4WD Akrilik + 4× Motor TT 1:48 + Roda 65 mm** | **Sudah Dimiliki** | Platform ***indoor PoC testbed*** (permukaan datar/simulasi). Beban total di atas sasis dijaga **≤800–1.000 gram**. |
| **Driver Motor** | **`TB6612FNG`** (MOSFET Dual H-Bridge) | Ready Tokped/Shopee *(Rp15–60 rb)* | Drop tegangan hanya **~0,5 V** (efisiensi >90%, tanpa heatsink), jauh lebih efisien dari `L298N` (drop 1,8–3,2 V) ([Datasheet TB6612FNG](https://cdn.sparkfun.com/datasheets/Robotics/TB6612FNG.pdf)). |
| **Optik, Servo & Audio** | **`Webcam USB`** + **1× `Servo` *Tilt*** + **LED Putih 5V** + **`Mikrofon USB`** | **Sudah Dimiliki** *(+LED)* | 1 webcam + 1 servo mencakup sudut feses (45°) & ayam (0–15°); jauh lebih tajam di *low-light* dibanding `ESP32-CAM` OV2640. |
| **Sensor Lingkungan** | • **Suhu & RH:** `SHT31` (I2C)<br>• **Tren Gas `NH₃`:** **`DFRobot SEN0567`** (MEMS `1–300 ppm`, `<20 mA`) | Ready Tokped *(SEN0567 Rp240–330 rb)* | Hemat daya dibanding `MQ-137` (~150 mA *heater*); output `SEN0567` dilabeli jujur sebagai **indikator tren kualitatif lonjakan `NH₃`** ([Wiki SEN0567](https://wiki.dfrobot.com/sen0567/)). |
| **Anti-Tabrak** | **`HC-SR04`** *(dengan voltage divider 3,3V)* / `VL53L0X` | Tambahan murah | Mencegah tabrakan objek saat demo meja/simulasi. |
| **Baterai (*Dual-Rail*)** | • **Rail 1 (`RPi 4` + Cam + Mic):** Powerbank 5V 3A `10.000 mAh` (~37 Wh)<br>• **Rail 2 (Motor + Servo + `ESP32`):** `2× 18650` (2S `7,4V` `2.500–3.000 mAh`) + **BMS 2S 10A** + *Buck 5V 3A* | **Wajib Benahi** *(ganti 4×AA)* | Memisahkan jalur daya mencegah `RPi 4` *brownout/reboot* saat motor *start*. Estimasi *runtime* PoC: **~1,5–2,5 jam**. |
| **Kabel & Proteksi** | *Perfboard* solder rapi + **Kabel Silikon `18 AWG`** (daya) + **`XT30` / `JST-XH`** + **Sekring `5A`** + Saklar Utama | Ready Tokped/Shopee | Menghindari kabel jumper DuPont tipis (26–28 AWG) yang longgar akibat getaran dan tidak kuat arus *stall* 4 motor. |
| **Node Pembanding (Opsional)** | **`ESP32-C3 Super Mini`** + sensor Suhu/RH statis | **Sudah Dimiliki** | Dipasang diam di tepi area simulasi untuk membandingkan pembacaan suhu/RH dinding vs pengukuran spasial `BROVER`. |

*(Catatan: `PC/Laptop ber-GPU` milik tim digunakan khusus untuk training model; `Raspberry Pi 3` dan `ESP32-CAM` disiapkan sebagai cadangan/kamera statis *dock*; `Arduino UNO` tidak digunakan karena fungsinya telah digantikan penuh oleh `ESP32`).*

---

## 8. Finalisasi (Rencana Final Komersial / *Field-Ready* — TKT 5–7+, Bootcamp Des 2026 – Feb 2027)

Fase **Finalisasi** dirancang khusus untuk lolos uji lapangan kandang broiler asli Indonesia (**sekam tebal 5–10 cm dengan kadar air hingga 46,42%, suhu 30–36°C, RH 80–96%, amonia hingga 20 ppm, debu bulu, dan keterjangkauan harga komersial bagi peternak rakyat**), memanfaatkan fasilitas **Lab Robotika/IoT/Manufaktur UNJ** dan potensi dukungan hardware *in-kind* **PT Edura Cipta Gemilang**.

![Analisis Efisiensi Komputasi & Keamanan Energi BROVER](./assets/05_komparasi_komputasi_dan_baterai_brover.png)
*`[DATA DATASHEET & BENCHMARK TERVERIFIKASI — VISUALISASI DISUSUN OLEH AI AGENT]` (A) Komparasi FPS YOLOv8n vs daya & harga global SBC yang menetapkan `Orange Pi 3B` (`RK3566` 0,8 TOPS, ~18 FPS, ~4W) sebagai sweet spot anti-over-spec; (B) Perbandingan keamanan termal & durasi operasi `LiFePO₄` vs `Li-Ion NMC`.*

### 8.1. Mengapa `Orange Pi 3B` + *Custom Carrier PCB* + `LiFePO₄`?
1. **Anti-*Over-Spec* Komputasi (`Orange Pi 3B` 4GB vs `Orange Pi 5`):** Karena 3 model AI berjalan **sekuensial (*time-sliced*)** pada kecepatan rover `≤0,1 m/s`, `Orange Pi 3B` (`Rockchip RK3566`, NPU `0,8 TOPS`, RAM 4GB, slot **eMMC**, daya `3,5–4,5 W`, ~16–22 FPS INT8) memotong biaya board hingga **~50%** dibanding `Orange Pi 5` (`6 TOPS`, harga lokal Rp4,8–7,9 jt untuk varian Pro/Plus) sekaligus jauh lebih aman terhadap *Out-of-Memory* dibanding `Luckfox Pico` (RAM hanya 256 MB).
2. **Wajib *Custom Carrier PCB* 2-Layer (Menurunkan Biaya & Menaikkan Keandalan Komersial):** Prosesor `Orange Pi 3B` dan modul `ESP32` tetap dibeli jadi (*off-the-shelf*), sementara seluruh jalur daya, *buck converter*, sekring, *watchdog*, driver motor, dan port sensor disatukan dalam **1 papan *Custom Carrier PCB* (desain KiCad, cetak ~Rp30–80 rb/pcs pada produksi batch kecil)** berlapis ***Conformal Coating*** — memangkas ongkos perakitan manual, tahan getaran sekam, dan kebal korosi uap `NH₃`/RH 96%.
3. **Keamanan Kebakaran Sekam (`LiFePO₄` 4S `12,8V 6Ah`):** Kandang broiler penuh sekam kering mudah terbakar pada suhu ambien 33–36°C. Ambang *thermal runaway* **`LiFePO₄` (`250–270°C`)** jauh lebih aman dibanding `Li-Ion NMC` (`180–210°C`) dengan umur pakai **`3.000–6.000+ siklus`**. Dengan beban rata-rata `~18–26 W` (efisiensi daya `Orange Pi 3B`), kapasitas `76,8 Wh` (`~65 Wh` efektif pada 85% DoD) menghasilkan durasi operasi **~3–4 jam kontinu** (cukup untuk **6–8 sesi inspeksi harian** dalam 1× pengisian daya).

### 8.2. Daftar Komponen Lengkap Versi Final Komersial (Terverifikasi Ketersediaan di Tokopedia/Shopee Indonesia)

`[DATA DATASHEET & AUDIT MARKETPLACE INDONESIA — DISUSUN OLEH AI AGENT]`

| Subsistem | Komponen Terpilih (Versi Final) | Status Pasar Lokal (Tokped/Shopee) | Estimasi Harga Lokal | Alasan Teknis & Keunggulan Lapangan |
| :--- | :--- | :---: | :--- | :--- |
| **Edge AI SBC** | **`Orange Pi 3B` (4GB RAM, `RK3566` NPU `0,8 TOPS`) + Modul `eMMC 32GB`** + *Heatsink* | **Ready** (Tokped/Shopee) | Rp900 rb – Rp2,0 jt *(tergantung RAM/eMMC)* | *Sweet spot* komersial (~18 FPS RKNN INT8, 3,5–4,5 W); eMMC tahan getaran & anti-korup OS. |
| **Real-Time MCU & PCB** | **`ESP32`** + ***Custom Carrier PCB* 2-Layer (KiCad)** + ***Conformal Coating*** | **Ready** (PCB cetak lokal/JLCPCB; coating ready Tokped) | ~Rp150–250 rb *(total modul + PCB/unit)* | Nol kabel jumper longgar, terlindungi dari kelembapan 96% & korosi gas `NH₃`. |
| **Sasis & Penggerak Medan Sekam** | • **Casing Tertutup IP54–IP65** (Rangka Aluminium + 3D-print **PETG/ASA** / **HDPE** bawah rata)<br>• **4× Motor DC *Metal-Gear* 12V + *Hall Encoder* (`JGB37-520`, 100–130 RPM)**<br>• **2× Driver MOSFET `BTS7960` (43A)**<br>• **Ban RC *Crawler* `110–120 mm` (+ *hex coupler* 12→6 mm) ATAU Kit *Rubber Track*** (*quick-release*) | **Ready Melimpah** (Tokped/Shopee) | Motor: Rp400–800 rb (4 pcs)<br>Driver: Rp100–240 rb (2 pcs)<br>Roda/Track + Casing: ~Rp600 rb–1,2 jt | Menjawab hukum torsi $F = \tau/r$ saat memperbesar roda, memberi ***ground clearance* ≥5–6 cm** agar tidak kandas di *wet litter* 46,4%, *Hall Encoder* melacak meter/zona, dan roda *quick-release* mudah disikat untuk sanitasi ookista *Eimeria*. |
| **Kamera, Servo & Pencahayaan** | • **Kamera USB *Low-Light* `Sony IMX291` (1080p UVC)** di balik kaca pelindung<br>• **Servo *Metal-Gear* Waterproof `DS3218`** (torsi 20 kg)<br>• **LED Bar Putih `5000K CRI >90`** + *diffuser* | **Ready** (Tokped/Shopee) | Kamera: ~Rp250–450 rb<br>Servo: Rp180–200 rb<br>LED: ~Rp50 rb | Sensor `IMX291` menangkap warna feses & postur ayam tajam dalam cahaya redup kandang; CRI >90 menstandarkan warna merah/hijau/putih feses. |
| **Audio Respirasi** | **Mikrofon MEMS Digital `INMP441` (I2S)** *(atau Mic USB)* + busa anti-debu & *splash-shield* menghadap bawah | **Ready Melimpah** (Tokped/Shopee) | ~Rp30–80 rb | Konsumsi daya mikro (`<0,1 W`), sensitif menangkap *rales*/ngorok radius 3–5 m saat *stop–mute–sample*. |
| **Sensor Mikroklimat & Gas** | • **Suhu & RH:** **`SHT31` Waterproof Probe (`FS304` stainless berfilter bawaan)**<br>• **Tren Gas `NH₃` (Standar Rakyat):** **`DFRobot SEN0567`** *(MEMS, 1–300 ppm, `<20 mA`)*<br>• *(Opsi Varian Pro/Korporasi:* **Sensor `NH₃` RS485 Modbus Industri + `MAX485`** — Rp1,5–3,2 jt lokal*)* | **Ready** (Tokped) | `SHT31 FS304`: ~Rp120–220 rb<br>`SEN0567`: **Rp240–330 rb** | Probe `FS304` langsung menggantikan membran ePTFE eceran yang langka di pasar lokal; pemilihan `SEN0567` menjaga BOM tetap terjangkau peternak rakyat tanpa *overclaim* (indikator tren kualitatif terkompensasi T/RH). |
| **Navigasi & Anti-Tabrak** | • **Ultrasonik IP67 `DFRobot A02YYUW`** (*blind zone* hanya **3 cm**, UART)<br>• **IMU `MPU6050`** + *Hall Encoder* roda | **Ready** (Tokped/Shopee) | `A02YYUW`: Rp350–395 rb<br>`MPU6050`: ~Rp25–45 rb | *Blind zone* 3 cm (`A02YYUW`, [Datasheet](https://www.dfrobot.com/product-1935.html)) mencegah sensor "buta" saat ayam mendekat di depan bumper; `MPU6050` menjaga arah lurus di sekam tidak rata. |
| **Baterai & Kelistrikan Industri** | • **`LiFePO₄` 4S `12,8V 6Ah` + Built-in BMS**<br>• **2× *Buck Converter* (`5V 5A` SBC & `6V 3A` Servo)**<br>• **Sensor Arus/Tegangan `INA219`**<br>• **Kabel Silikon `16–18 AWG`**, **`XT60`**, **Konektor `GX16`**, ***Blade Fuse* `15A`**, & ***Kill Switch* IP65** | **Ready Melimpah** (Tokped/Shopee) | Baterai LFP: Rp200–350 rb<br>Buck + INA219 + Kabel/Konektor: ~Rp250–400 rb | Aman terhadap risiko kebakaran sekam (`thermal runaway 250–270°C`), *runtime* 3–4 jam (6–8 sesi/hari), tahan getaran & mudah dirawat. |

> **Estimasi Total BOM Versi Final Rakyat (`Varian Standar` dengan `SEN0567`):** Sekitar **Rp3,9 – Rp6,2 juta/unit** (belum termasuk efisiensi harga grosir/batch produksi) — **jauh di bawah kerugian 1 kali wabah HPAI pada 3.000 ekor broiler (`−Rp53,89 s.d. −Rp57,35 juta`; Pramuwidyatama *et al.*, 2023) dan sebagian kecil dari harga robot komersial impor (`Rp100 juta+`)!**

---

## 9. Keberlanjutan (*Sustainability*, BMC, Roadmap TKT 3→9, & Strategi HKI)

![Roadmap Peningkatan TKT & Evolusi 2-Fase BROVER 2026–2027](./assets/06_roadmap_tkt_dan_evolusi_brover.png)
*`[SINTESIS ROADMAP TIM MBOYZ — DISUSUN OLEH AI AGENT]` Peta jalan terukur dari TKT 3–4 (Seleksi Nov 2026) → TKT 5–6 (Bootcamp Des 2026–Feb 2027) → TKT 6–7 (Demo Day & LoI Mar–Apr 2027) → TKT 7–9 (Pilot Testing, HKI & Komersialisasi Mei–Agu 2027+).*

### 9.1. Ringkasan *Business Model Canvas* (BMC — Rubrik Penilaian 15%)

`[SINTESIS MODEL BISNIS TIM MBOYZ — PERLU VALIDASI WAWANCARA MITRA]`

| Blok BMC | Strategi Komersialisasi `BROVER` |
| :--- | :--- |
| **1. *Customer Segments*** | (1) Peternak broiler mandiri & plasma skala menengah (3.000–20.000 ekor, *open* & *closed house*); (2) Perusahaan *agritech* & penyedia kandang lokal (seperti **PT Zara Propertifarm / KANOPIS** sebagai *add-on* paket kandang); (3) Koperasi peternak & inti kemitraan. |
| **2. *Value Propositions*** | Deteksi dini gejala penyakit endemik (CRD/IB/ND/Koksidiosis) berbasis audio + visual + mikroklimat *offline-first* pada fraksi biaya robot impor; membantu menekan kerugian 1× wabah (`Rp22–57 juta`); dokumentasi biosekuriti digital & ekspor bukti cepat ke TSO/Dokter Hewan. |
| **3. *Channels*** | B2B *bundling* bersama mitra konstruksi kandang (PT Zara/KANOPIS), kemitraan distributor/TSO obat hewan, koperasi/asosiasi peternak (PINSAR/GOPAN), dan kanal edukasi digital peternak. |
| **4. *Customer Relationships*** | Pendampingan instalasi & kalibrasi awal *dock*, pembaruan model AI berkala (*OTA update* dari data konfirmasi *"Benar/Bukan"*), serta dukungan teknis via WhatsApp & komunitas peternak. |
| **5. *Revenue Streams*** | (1) **Penjualan Unit Perangkat** (Varian Rakyat `SEN0567` vs Varian Pro `RS485 NH₃` Modbus); (2) **Langganan Software/Cloud Ringan (*SaaS*)** untuk histori lintas-siklus, notifikasi WA, & pembaruan *Triage Dictionary*; (3) **Skema *Rover-as-a-Service* (Sewa per Siklus)** bagi peternak kecil untuk menurunkan hambatan modal awal. |
| **6. *Key Resources*** | Tim TI (AI/CV/Audio, Embedded, Backend `Golang`, PWA), *Custom Carrier PCB* & desain mekanik 3D, dataset terkurasi + data *fine-tuning* lokal Indonesia, serta fasilitas Lab UNJ & jejaring mitra industri. |
| **7. *Key Activities*** | Kurasi & *fine-tuning* model AI pada kandang lokal, perakitan & uji ketahanan sasis/PCB, pengembangan aplikasi PWA & backend `Golang`, serta validasi *pilot testing* bersama dokter hewan/TSO. |
| **8. *Key Partnerships*** | **PT Zara Propertifarm Indonesia** (validasi lapangan 6 farm Bogor & *bundling* KANOPIS), **PT Edura Cipta Gemilang** (dukungan hardware *in-kind* & komersialisasi PTNBH UNJ), **Dosen/Lab UNJ** (pendampingan TKT & HKI), serta praktisi/dokter hewan lapangan. |
| **9. *Cost Structure*** | BOM hardware per unit (ditekan lewat `Orange Pi 3B`, `SEN0567`, & *Custom Carrier PCB*), biaya VPS cloud minimal berkat efisiensi **`Golang`**, biaya *pilot testing* & perakitan, serta pendaftaran HKI/Paten. |

### 9.2. Keberlanjutan Teknis, Strategi HKI/Lisensi, & Ekspansi Jangka Panjang

1. **Mitigasi Lisensi untuk HKI & Komersialisasi (TKT 7–9):**
   - Pada fase PoC/Hackathon, `Ultralytics YOLOv8n/11n` (lisensi `AGPL-3.0`) digunakan untuk mempercepat validasi akurasi. Untuk komersialisasi *closed-source* & pendaftaran HKI (Mei–Agu 2027), arsitektur deteksi direncanakan bermigrasi ke *backbone* berlisensi komersial bebas **`Apache-2.0`** (seperti **`YOLOX-Nano`**, **`RT-DETR`**, dan **`MobileNetV3`**), sedangkan dataset *Evet-Africa* (`AGPL-3.0`) bersifat cadangan/eksperimen dan digantikan data terbuka **`CC0`/CC-BY** + dataset primer lokal Tim MBOYZ.
   - Kepemilikan HKI (Hak Cipta software/desain sirkuit PCB & Paten Sederhana mekanisme integrasi triase biosekuriti) tetap milik **Tim Inovator / UNJ** sesuai ketentuan Buku Pedoman (`[Pedoman, Hal. 6]`).
2. **Keberlanjutan Ekonomi & Ekologis:**
   - Dengan mendeteksi gejala pernapasan & koksidiosis sejak dini dan mengarahkan peternak berkonsultasi ke TSO/Dokter Hewan (tanpa resep antibiotik otomatis), `BROVER` berkontribusi tidak langsung menekan penggunaan antibiotik profilaktik/sembarangan (AMR) dan menurunkan mortalitas panen — meningkatkan ketahanan pangan hewani nasional.
3. **Peta Ekspansi Produk Jangka Panjang (*Future Roadmap*):**
   - **Modul Rel/Kabel Gantung (*Overhead Track Kit*):** Kotak sensor & *Edge AI* `BROVER` yang sama dirancang modular agar pada generasi berikutnya dapat digantung pada kawat sling baja/rel plafon untuk melayani **kandang broiler penuh hingga hari ke-35 (kepadatan 30 kg/m²)** serta **kandang baterai bertingkat ayam petelur (*layer*)** tanpa mengubah *tech stack* AI maupun backend `Golang`.
4. **Pembagian Peran Tim MBOYZ (Kesiapan Eksekusi — Rubrik 10%):**
   - **4 Mahasiswa Teknologi Informasi:** dibagi fokus ke 4 pilar inti — (1) *AI/ML Engineer* (CV Feses, CV Fisik, & Audio Respirasi), (2) *Embedded & Robotics Engineer* (`ESP32`, *wiring*, *Carrier PCB*, & integrasi SBC), (3) *Backend & Cloud Engineer* (`Golang`, MQTT, PostgreSQL, Open-Meteo, Bot WA), (4) *Frontend & Product/BMC Lead* (`Next.js` PWA, *Disease Triage Dictionary*, UX peternak, & BMC).
   - **Slot Ke-5 — 1 Dosen Aktif UNJ *(Action Item Wajib Sebelum Pendaftaran Nov 2026)*:** Pembimbing metodologi riset, validasi peningkatan TKT/Katsinov (`≥80%`), akses Lab Robotika/IoT/Manufaktur UNJ, dan pendampingan pendaftaran HKI.

---

## 10. Kumpulan Dataset, GitHub / Hugging Face / Kaggle, & Model AI

Seluruh tautan di bawah ini telah diverifikasi aktif (`HTTP 200`) dari kurasi [05_Curated_Winners_And_Top_OpenSource](../05_Curated_Winners_And_Top_OpenSource/00_RINGKASAN_KURASI_DAN_ELIMINASI.md) dan audit langsung.

`[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

### A. Kumpulan Dataset Terverifikasi (CV Feses, CV Fisik/Mati, Audio Respirasi, & Mikroklimat)

| No | Jenis | Nama & Platform | Untuk Apa (Peran di `BROVER`) | Catatan Audit & Lisensi | Link Terverifikasi (`HTTP 200`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **Dataset CV Feses (PCR)** | **PCR-Annotated Poultry Disease Diagnostics** *(Zenodo 5801834)* | **Dataset Utama Model #1 (CV Feses):** 4 kelas terverifikasi uji PCR (*Coccidiosis, Salmonella, Newcastle Disease, Healthy*) + anotasi deteksi objek YOLO. | `36.265 downloads`; DOI permanen (`Machuve et al., 2022`); wajib ditambah foto sekam lokal Indonesia untuk *domain shift*. | [Zenodo 5801834](https://zenodo.org/records/5801834) |
| 2 | **Dataset CV Feses** | **Chicken Disease Image Classification** *(Kaggle — `allandclive`)* | Pengayaan data *training/validation* Model #1 (4 kelas feses unggas, 266 MB). | `9.211 downloads`, `85 upvotes`; *benchmark* standar komunitas. | [Kaggle Dataset](https://www.kaggle.com/datasets/allandclive/chicken-disease-1) |
| 3 | **Dataset CV Feses** | **Chicken Feces Baseline Clean** *(Hugging Face — `iagovarela`)* | Dataset citra feses bersih format HF untuk uji *baseline* cepat Model #1. | `562 downloads`; siap pakai di pipeline PyTorch/HF. | [Hugging Face Dataset](https://huggingface.co/datasets/iagovarela/poultry-disease-dataset) |
| 4 | **Dataset CV Fisik/Mati (ID)** | **Chicken Health Images Dataset — RGB & Thermal** *(Kaggle — `ekosupriyanto`)* | **Dataset Utama Model #2 (CV Ayam Sehat/Lesu/Mati):** Memanfaatkan cabang **RGB** berlabel *Healthy, Sick, Dead* buatan kontributor Indonesia. | **Lisensi `CC0 Public Domain`** (bebas komersial!); cabang termal tidak dipakai karena tanpa IR/thermogun. | [Kaggle Dataset](https://www.kaggle.com/datasets/ekosupriyanto/chicken-health-images-dataset-rgb-and-thermal) |
| 5 | **Dataset CV Perilaku Broiler** | **ChickenVerse: Detection, Segmentation & Behavior (2026)** *(Zenodo 20672799)* | Melatih Model #2 mengenali deteksi individu, postur abnormal, dan perilaku broiler di kandang nyata. | `3.228 downloads`; riset terbuka mutakhir 2026 (`DOI: 10.5281/zenodo.20672799`). | [Zenodo 20672799](https://zenodo.org/records/20672799) |
| 6 | **Dataset CV Broiler** | **PIO Broiler Detection Dataset** *(Zenodo 16686320)* | Pengayaan deteksi broiler & kerumunan/distribusi lantai (`1.435` gambar resolusi tinggi, `327.289` anotasi YOLO). | `3.875 downloads`; label fokus deteksi individu & distribusi (bukan label penyakit). | [Zenodo 16686320](https://zenodo.org/records/16686320) |
| 7 | **Dataset CV Gejala Eksternal *(Cadangan)*** | **Evet-Africa Poultry Disease Dataset** *(Hugging Face)* | Eksperimen sekunder Model #2 khusus **hanya 8 kelas gejala fisik luar** (*Torticollis, Facial Swelling, Oculonasal Discharge, Cyanotic comb*, dll.). | **Peringatan Audit:** `~18/26` kelas adalah organ dalam bedah bangkai (**wajib dibuang**); lisensi **`AGPL-3.0`** (opsi diganti data lain saat komersialisasi). | [Hugging Face Dataset](https://huggingface.co/datasets/Evet-Africa/poultry-disease-dataset) |
| 8 | **Dataset Audio Respirasi** | **SmartEars: Poultry Respiratory Monitoring Audio** *(Mendeley Data)* | **Dataset Utama Model #3 (Audio AI):** `6.000` segmen audio persis berdurasi **5 detik** (*Healthy, Sick/Respirasi, None/Derau Kipas*). | Sangat selaras dengan protokol *Zone-Scheduled Stop–Mute–Sample* 5 detik & memisahkan suara *blower closed house*. | [Mendeley Data](https://data.mendeley.com/datasets/dy6gtvt4mk/2) |
| 9 | **Dataset Audio Respirasi** | **Poultry Vocalization Signal Dataset** *(Mendeley Data)* | Pengayaan Model #3: `346` file `.wav` (*healthy, noise, unhealthy*) hasil rekaman longitudinal 65 hari. | DOI permanen (`10.17632/zp4nf2dxbh.1`); memperkuat generalisasi suara ngorok/bersin. | [Mendeley Data](https://data.mendeley.com/datasets/zp4nf2dxbh.1) |
| 10 | **Dataset Multimodal (ID/EN)** | **Chicken Health & Behavior Multimodal** *(Hugging Face — `IceKhoffi`)* | Pengayaan Model #2 & #3: mencakup folder `vision-object-detection` & `vocalization-dataset-for-early-disease-detection`. | `723 downloads`; bertag bahasa Indonesia & Inggris. | [Hugging Face Dataset](https://huggingface.co/datasets/IceKhoffi/chicken-health-behavior-multimodal) |
| 11 | **Dataset Mikroklimat** | **Environmental Monitoring of Broiler Chickens** *(Mendeley Data)* | Referensi kalibrasi & pengujian simulasi *Zone Risk Fusion* (`1.920` observasi Suhu, RH, `NH₃`, `CO₂`, & umur broiler). | DOI permanen (`10.17632/m9nsjhtsph.1`). | [Mendeley Data](https://data.mendeley.com/datasets/m9nsjhtsph.1) |

### B. Repositori GitHub & Proyek Pemenang Hackathon Referensi

| No | Jenis | Nama & Platform | Untuk Apa (Peran di `BROVER`) | Catatan Audit & Lisensi | Link Terverifikasi (`HTTP 200`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 12 | **GitHub + Devpost Winner** | **Henomaly (`RishitRai/Henomaly`)** | Referensi utama arsitektur *Edge AI* Raspberry Pi + *anomaly triage* feses/perilaku (bukan vonis medis) & studi kasus *cross-farm domain shift*. | Pemenang resmi AI Hackathon 2026; demo web [aremyhens.fit](https://aremyhens.fit/) aktif. | [GitHub](https://github.com/RishitRai/Henomaly) \| [Devpost](https://devpost.com/software/holy-crap) |
| 13 | **GitHub Riset CV Karkas** | **Broiler Carcass Candidate Detection (`jeongrubin`)** | Referensi algoritma membedakan **ayam mati vs ayam tidur** pada lantai broiler (Model #2). | Implementasi riset *YOLOv8s + U-Net + BiLSTM*. | [GitHub](https://github.com/jeongrubin/broiler-carcass-candidate-detection) |
| 14 | **GitHub Audio AI** | **CVC-Fusion (`CoderYLH/CVC-Fusion`)** | Referensi arsitektur *encoder* akustik ringan (*1D MobileNetV2 + spectrogram fusion*) untuk Model #3. | Implementasi paper riset vokalisasi ayam. | [GitHub](https://github.com/CoderYLH/CVC-Fusion) |
| 15 | **GitHub Audio AI** | **ChickenLanguageDataset (`zebular13`)** | Referensi skrip prapemrosesan & segmentasi rekaman vokalisasi ayam + derau latar. | `47 stars`, `9 forks`. | [GitHub](https://github.com/zebular13/ChickenLanguageDataset) |
| 16 | **GitHub Indonesia (SPK)** | **ChiRex (`januriawan/chirex`)** | Referensi struktur basis pengetahuan gejala penyakit ayam Indonesia untuk merancang ***Disease Triage Dictionary*** di PWA. | `96 stars`, `34 forks`; konteks lokal Indonesia. | [GitHub](https://github.com/januriawan/chirex) |
| 17 | **GitHub Indonesia (ESP32)** | **Poultry Vet Env Monitor (`MiftahulSN`)** | Referensi firmware C++ ESP32 Indonesia membaca Suhu + RH + Amonia `NH₃` + monitor baterai secara terpadu. | Merujuk jurnal *Animals* (`DOI: 10.3390/ani14040615`). | [GitHub](https://github.com/MiftahulSN/poultry-vet-decision-support-system) |
| 18 | **GitHub Indonesia (YOLO CH)** | **Perilaku Broiler *Closed House* (`Ruler02`)** | Referensi eksperimen YOLO perilaku broiler + suhu aktual pada kandang *closed house* di Indonesia. | Riset lapangan kandang *closed house* Indonesia. | [GitHub](https://github.com/Ruler02/Deteksi-dan-Klasifikasi-Perilaku-Ayam-Broiler-pada-Kandang-Close-House-Berbasis-YOLO-) |
| 19 | **GitHub MLOps Feses** | **Chicken Disease MLOps (`krishnaik06`)** | Referensi *pipeline* pelatihan, DVC, & *containerization* model klasifikasi feses ayam. | `90 stars`, `110 forks`, **MIT License**. | [GitHub](https://github.com/krishnaik06/Chicken-Disease-Classification-Projects) |
| 20 | **GitHub NPU Rockchip** | **Qengineering YOLO NPU (`RK3566/RK3588`)** | Referensi konversi & *deployment* C++ RKNN INT8 untuk **Orange Pi 3B (`RK3566`)** pada fase Finalisasi. | Benchmark terverifikasi RK3566/RK3588. | [GitHub YoloV5-NPU](https://github.com/Qengineering/YoloV5-NPU) \| [YoloV6-NPU](https://github.com/Qengineering/YoloV6-NPU) |
| 21 | **Hackathon Winner** | **PoultryGuard AI (`SIRAGU`)** & **Smart Coop 2.0 (`CodersCafeTech`)** | Referensi fitur *sensor fault diagnostics* (deteksi *drift* sensor) + desain *Custom Carrier PCB* + *Edge ONNX* + alert Telegram. | Terverifikasi pemenang resmi AnimalHack 2026 & Hackster Contest. | [SIRAGU GitHub](https://github.com/skarthik2745/SIRAGU-Poultry-Monitoring) \| [Smart Coop 2.0 GitHub](https://github.com/CodersCafeTech/Smart-Coop-V2) |

### C. Model AI *Pretrained*, Demo *Space*, & Arsitektur Target

| No | Jenis | Nama Model / Platform | Untuk Apa (Peran di `BROVER`) | Catatan Audit & Lisensi | Link Terverifikasi (`HTTP 200`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 22 | **Pretrained YOLO** | **Ultralytics `YOLOv8n` / `YOLO11n` → NCNN / RKNN** | *Backbone* utama PoC untuk **Model #1 (Feses)** dan **Model #2 (Ayam Lesu/Mati)** — berjalan ~2,3 FPS di `RPi 4` (NCNN) & ~18 FPS di `Orange Pi 3B` (RKNN INT8). | `AGPL-3.0` (migrasi ke `YOLOX-Nano` / `RT-DETR` `Apache-2.0` saat komersialisasi *closed-source*). | [Ultralytics Raspberry Pi Guide](https://docs.ultralytics.com/guides/raspberry-pi/) |
| 23 | **Pretrained HF Model** | **PoultryVision (`Williamsanderson/PoultryVision`)** | Bobot awal *pretrained* `YOLO11` unggas untuk percepatan *transfer learning* Model #2. | `171 downloads`; `AGPL-3.0`. | [Hugging Face Model](https://huggingface.co/Williamsanderson/PoultryVision) |
| 24 | **Pretrained HF Model** | **DETR ResNet-50 Chickens (`joe611/chickens`)** | *Teacher model* / pembanding akurasi deteksi ayam pada eksperimen *training* di PC GPU. | `2.247 downloads`; **Apache-2.0 License** (bebas komersial). | [Hugging Face Model](https://huggingface.co/joe611/chickens) |
| 25 | **Live Demo Space *(Referensi)*** | **Evet-Africa Poultry Disease Detector Space** *(Hugging Face)* | Pembanding *benchmark* inferensi visual cepat (khusus kelas gejala eksternal). | `RUNNING`; `AGPL-3.0` (jangan gunakan prediksi 18 kelas bedah bangkai untuk ayam hidup). | [HF Space](https://huggingface.co/spaces/Evet-Africa/poultry-disease-detector) |
| 26 | **Arsitektur Audio AI** | **`Log-Mel Spectrogram` + `MobileNetV3-Small` / `2D CNN`** | Arsitektur ringan **Model #3 (Audio Respirasi 5 detik)** — ukuran ~3–8 MB, inferensi `~20–50 ms` di CPU/NPU, bebas lisensi (`PyTorch/BSD/Apache-2.0`). | Dilatih dari dataset *SmartEars* + *Poultry Vocalization* + *IceKhoffi*. | [PyTorch TorchVision](https://pytorch.org/vision/stable/models/mobilenetv3.html) *(standar resmi)* |

---

## 11. Referensi Lengkap

Seluruh referensi berikut telah diverifikasi keasliannya (0 *preprint*, 0 tautan tidak aktif).

### A. Jurnal *Peer-Reviewed* Indonesia & Data Resmi Sektor Perunggasan
1. **Badan Pusat Statistik (BPS).** (2025). *Produksi Daging Ayam Ras Pedaging Menurut Provinsi*. [bps.go.id](https://www.bps.go.id/id/statistics-table/2/NDg4IzI=/produksi-daging-ayam-ras-pedaging-menurut-provinsi.html)
2. **Direktorat Jenderal Peternakan dan Kesehatan Hewan (Ditjen PKH), Kementerian Pertanian RI.** *Manual Penyakit Unggas*. [Manual Penyakit Unggas PDF (iSIKHNAS)](https://wiki.isikhnas.com/images/d/dd/Manual_Penyakit_Unggas.pdf)
3. **PT Medion Technical Education & Consultation (TEC).** (Januari 2026). *Overview of Poultry Disease Analysis 2025 & Disease Projection 2026*. [medion.co.id](https://www.medion.co.id/en/info-medion/overview-of-poultry-disease-analysis-2025-disease-projection-2026/)
4. **PT Medion.** *Closed House, Solusi Peningkatan Performa Ayam* (standar kepadatan *open house* 13–15 kg/m² vs *closed house* 25–30 kg/m²). [medion.co.id](https://www.medion.co.id/info-medion/closed-house-solusi-peningkatan-performa-ayam/)
5. **Sumiati, *et al.*** (2025). *Animal Bioscience* (Q1) — Tinjauan industri perunggasan Indonesia & *Heat Stress Index* (HSI) bulanan 2023. [DOI: 10.5713/ab.24.0678](https://doi.org/10.5713/ab.24.0678)
6. **Pramuwidyatama, M. G., *et al.*** (2023). *Preventive Veterinary Medicine* (Q1) — Pemodelan bio-ekonomi dampak wabah HPAI H5N1 pada broiler Sektor 3 Jawa Bagian Barat. [DOI: 10.1016/j.prevetmed.2022.105833](https://doi.org/10.1016/j.prevetmed.2022.105833)
7. **Anwar Sani, R., *et al.*** (2025). *Poultry Science* (Q1) — Evaluasi skor biosekuriti 6 dimensi pada 19 farm broiler (153 siklus) di Jawa Barat. [DOI: 10.1016/j.psj.2025.106010](https://doi.org/10.1016/j.psj.2025.106010)
8. **Hartady, T., *et al.*** (2026). *Veterinary Sciences* (Q1) — Studi kasus koinfeksi multifaktorial (AI H5/H9, IB, *M. gallisepticum*, koksidiosis) dan tekanan mikroklimat/NH₃ 20 ppm di Majalengka. [DOI: 10.3390/vetsci13040364](https://doi.org/10.3390/vetsci13040364)
9. **Wilcox, C. H., *et al.*** (2025). *Animal Welfare* (Q1) — Distribusi THI, RH (81,9%; maks 96%), amonia, dan lesi FPD (40%) pada 14 farm *closed/semi-closed house* Jawa Barat. [DOI: 10.1017/awf.2025.10052](https://doi.org/10.1017/awf.2025.10052)
10. **Mohammadi, *et al.*** (2026). *Advances in Animal and Veterinary Sciences* (Q3) — Beban panas kumulatif dan ambang ROC prediktor mortalitas broiler sore hari (`>32,8°C`; `THI >79`) di Jawa Tengah. [DOI: 10.17582/journal.aavs/2026/14.5.1100.1111](https://doi.org/10.17582/journal.aavs/2026/14.5.1100.1111)
11. **Hasibuan, *et al.*** (2021). *Jurnal Sain Peternakan Indonesia* (SINTA 2) — Variasi kadar air *litter* (`46,42%` dataran rendah) dan kadar `NH₃` lintas ketinggian wilayah di Jawa Tengah. [DOI: 10.31186/jspi.id.16.2.171-179](https://doi.org/10.31186/jspi.id.16.2.171-179)
12. **Rehman, S., *et al.*** (2023). *PeerJ* (Q1) — Survei tingkat pengetahuan *Avian Influenza* pada 200 pekerja kandang unggas di Indonesia. [DOI: 10.7717/peerj.14600](https://doi.org/10.7717/peerj.14600)
13. **Efendi, R., *et al.*** (2022). *Veterinary World* (Q1) — Pola penggunaan antibiotik profilaktik/*flushing* pada 132 peternak broiler Kabupaten Bogor. [DOI: 10.14202/vetworld.2022.707-713](https://doi.org/10.14202/vetworld.2022.707-713)
14. **Junaidi, *et al.*** (2023). *Journal of World's Poultry Research* (Q3) — Struktur biaya usaha broiler mandiri vs kontrak pada 180 farm di Banten. [DOI: 10.36380/jwpr.2023.25](https://doi.org/10.36380/jwpr.2023.25)
15. **Chapot, L., *et al.*** (2024). *PLOS ONE* (Q1) — Tantangan pencatatan data silo dan keputusan kesehatan pada 56 pemangku kepentingan perunggasan Indonesia. [DOI: 10.1371/journal.pone.0308379](https://doi.org/10.1371/journal.pone.0308379)
16. **TROBOS Livestock.** (Maret 2024). `[SUARA LAPANGAN DARING]` *Virus AI Terus Mengintai* — Wawancara Hari Farm (kasus wabah AI awalnya dikira snot). [troboslivestock.com](https://troboslivestock.com/virus-ai-terus-mengintai/)

### B. Jurnal *Peer-Reviewed* Robotika Unggas, AI Diagnostik, Biosekuriti, & Sensor
17. **Machuve, D., Nwankwo, E., Mduma, N., & Mbelwa, J.** (2022). Poultry diseases diagnostics models using deep learning. *Frontiers in Artificial Intelligence*. [DOI: 10.3389/frai.2022.733345](https://doi.org/10.3389/frai.2022.733345)
18. **Ren, G., Lin, T., & Ying, Y.** (2020). Agricultural robotics research applicable to poultry production: A review. *Computers and Electronics in Agriculture*. [DOI: 10.1016/j.compag.2020.105216](https://doi.org/10.1016/j.compag.2020.105216)
19. **Vroegindeweij, B. A., *et al.*** (2018). Evaluation of the performance of PoultryBot, an autonomous mobile robotic platform for poultry houses. *Biosystems Engineering*. [DOI: 10.1016/j.biosystemseng.2018.07.015](https://doi.org/10.1016/j.biosystemseng.2018.07.015)
20. **Animals (2024).** How Do Escape Distance Behavior of Broiler Chickens Change in Response to a Mobile Robot Moving at Two Different Speeds? (*RobôFrango*). [PMC11011048](https://pmc.ncbi.nlm.nih.gov/articles/PMC11011048/)
21. **Poultry Science (2026).** Research note: approach rather than avoidance: behavioral responses of broiler chicks repeatedly exposed to an autonomous robot (*AviSense*). [PMC13696172](https://pmc.ncbi.nlm.nih.gov/articles/PMC13696172/)
22. **Innovative prevention and control of coccidiosis (2024)** & **Frontiers (2026)** — Ketahanan dinding ookista *Eimeria* terhadap disinfektan kandang umum. [PMC11416347](https://pmc.ncbi.nlm.nih.gov/articles/PMC11416347/) \| [DOI: 10.3389/fcimb.2026.1756128](https://www.frontiersin.org/journals/cellular-and-infection-microbiology/articles/10.3389/fcimb.2026.1756128/full)
23. **Evaluation of cleaning and disinfection procedures on poultry farms (2025).** Pentingnya pembersihan mekanis/fisik materi organik sebelum disinfeksi. [PMC12414267](https://pmc.ncbi.nlm.nih.gov/articles/PMC12414267/)
24. **Persistence of non-typhoidal *Salmonella* (PMC13433518)** & **Prevalence of Newcastle Disease in Domestic Chickens (PLOS ONE, 2022)** — Bukti *subclinical/asymptomatic fecal shedding*. [PMC13433518](https://pmc.ncbi.nlm.nih.gov/articles/PMC13433518/) \| [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0264028)
25. **Molecular Investigation of *Eimeria* Species in Broiler Farms (2023).** Peran *fomites* (sepatu bot, roda, peralatan) dan biosekuriti pada 100 farm broiler. [PMC10144399](https://pmc.ncbi.nlm.nih.gov/articles/PMC10144399/)
26. **von Jasmund, N., *et al.*** (2022). Assessment of ammonia sensors and photoacoustic measurement systems using a gas calibration unit. *Computers and Electronics in Agriculture*, 194, 106744. [DOI: 10.1016/j.compag.2022.106744](https://doi.org/10.1016/j.compag.2022.106744)
27. **Damasceno, F. A., & Saraz, J. A. O.** Evaluasi performa modul sensor amonia (MQ-137 vs elektrokimia) pada lingkungan kandang terbuka. [SciELO Brazil](https://www.scielo.br/j/eagri/a/qKDrWtT4XvNDdTnMVkCJJJC/?lang=en)

### C. Panduan Manajemen Broiler, *Datasheet* Hardware, & Referensi Industri
28. **Aviagen (Ross).** *Ross Broiler Pocket Guide* (ketinggian *pan feeder* & *nipple drinker*). [Aviagen PDF](https://aviagen.com/assets/Tech_Center/Ross_Broiler/Aviagen-ROSS-Broiler-PocketGuide-EN.pdf)
29. **Cobb Genetics.** (2024). *Nipple Drinker Management Poster* (tata letak jalur & ruang ujung kandang). [Cobb PDF](https://www.cobbgenetics.com/assets/Cobb-Files/2024-Nipple-Drinker-Poster.pdf)
30. **Octopus Biosafety.** *FAQ: XO Broiler Robot* (kecepatan `0,04–0,12 m/s`, jendela operasi hari ke-5–23, pencucian roda). [octopusbiosafety.com](https://www.octopusbiosafety.com/en/faq/xo-en/)
31. **Big Dutchman / Faromatics.** *ChickenBoy Brochure* (pembanding robot rel plafon 24/7). [Big Dutchman PDF](https://cdn.bigdutchman.com/fileadmin/content/poultry/products/en/Poultry-growing-ChickenBoy-Big-Dutchman-en.pdf)
32. **Ultralytics Official Documentation.** *Raspberry Pi Deployment & NCNN Benchmarks*. [docs.ultralytics.com](https://docs.ultralytics.com/guides/raspberry-pi/)
33. **Orange Pi Official.** Spesifikasi Hardware [`Orange Pi 3B` (`RK3566`)](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) & [`Orange Pi 5` (`RK3588S`)](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html).
34. **Luckfox Official.** Spesifikasi Hardware [`Luckfox Pico Ultra` (`RV1106`)](https://www.luckfox.com/EN-Luckfox-Pico-Ultra?ci=502).
35. **DFRobot Official.** Wiki [`SEN0567` MEMS `NH₃`](https://wiki.dfrobot.com/sen0567/), Datasheet [`SEN0469` Electrochemical `NH₃`](https://www.dfrobot.com/product-2513.html), & Datasheet [`A02YYUW` IP67 Ultrasonic (3 cm blind zone)](https://www.dfrobot.com/product-1935.html).
36. **Toshiba / SparkFun.** *TB6612FNG Dual MOSFET Motor Driver Datasheet*. [TB6612FNG PDF](https://cdn.sparkfun.com/datasheets/Robotics/TB6612FNG.pdf)
37. **Open-Meteo.** *Free Open-Source Weather Forecast API*. [open-meteo.com](https://open-meteo.com/)
38. **Dokumen Internal Terverifikasi Hackathon UNJ 2026 (Tim MBOYZ):** [01_TEAM_AND_CONSTRAINTS.md](../01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md) | [02_HACKATHON_DFARM_RULES.md](../01_Context_Memory/02_HACKATHON_DFARM_RULES.md) | [04_MITRA_PT_ZARA_PROPERTIFARM.md](../01_Context_Memory/04_MITRA_PT_ZARA_PROPERTIFARM.md).
