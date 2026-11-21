# 05 — VIDEO DEMO & TUTORIAL YOUTUBE (*OPEN-SOURCE* DENGAN KODE / SKEMATIK)

> **Kriteria Ketat:** Hanya video YouTube purwarupa/tutorial peternakan ayam yang **benar-benar menyertakan tautan *open-source* aktif (`HTTP 200`)** seperti GitHub, simulasi Wokwi, atau panduan rangkaian/skematik di deskripsi videonya.  
> **Anti-Duplikasi:** Sebanyak 13 video demo YouTube yang merupakan bagian dari proyek Devpost/DoraHacks/Hackster/Arduino Project Hub (seperti *PoultryGuard AI*, *FarmSeva*, *Henomaly*, *Chicken Saviour*, *Poultry Pulse*, *Smart Coop 2.0*, dan *$50 DIY AI Smart Coop*) **sudah digabung pada `01_HACKATHON_DAN_MAKER_PROJECTS.md`** dan tidak diulang di sini. Video tutorial yang tautan repositori GitHub-nya ternyata `404` saat diaudit telah dibuang.  
> `[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

---

## A. Demo IoT Mikroklimat & Otomasi Kandang Ayam (Masalah #2 & Biosekuriti Akses)

- [ ] **Monitoring Kandang Ayam ESP32 MQTT — Luthfi Yufajjiru (Indonesia)** — `[Masalah #2]` `[ESP32 + MQTT HiveMQ + Backend Golang + Simulasi Wokwi]`
  - **Ringkasan:** *Showcase* dan demonstrasi sistem pemantauan kondisi kandang ayam berbasis mikrokontroler ESP32 asal Indonesia yang terhubung ke broker MQTT HiveMQ, *backend* Golang, Web UI, serta dilengkapi simulasi rangkaian Wokwi yang dapat langsung dijalankan di browser.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=eWLETO-eHaY) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/luthfiyufajjiru/edspert-kandang-ayam) *(HTTP 200)*
    - Demo Live: [Wokwi Simulation](https://wokwi.com/projects/371880962232095745) *(HTTP 200)*

- [ ] **Affordable Automatic Chicken Coop Door using ESP32 — `esp32-coop`** — `[Masalah #1]` `[Biosekuriti Akses / ESP32 + 3D STL + Web App]`
  - **Ringkasan:** Demonstrasi perangkat *open-source* pengendali akses pintu kandang ayam berbasis ESP32 (anti-predator/intrusi malam hari) lengkap dengan file 3D cetak, dokumentasi GitHub (168 bintang), dan aplikasi konfigurasi web.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=ffOFzQwUqkg) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/ESP32-COOP/ESP32-COOP-DOC) *(HTTP 200)*
    - Demo Live: [Vercel Web App](https://coop-door.vercel.app) *(HTTP 200)*

- [ ] **Automatic Chicken Door ESP32 — BlazenDeveloper** — `[Masalah #1]` `[Biosekuriti Akses / ESP32 + 12V Worm Gear Motor]`
  - **Ringkasan:** Demo perangkat keras pintu kandang ayam otomatis berbasis ESP32 dan motor *worm gear* 12V dilengkapi skema 3D dan kode sumber firmware di GitHub.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=S-3rC9S5BCw) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/somerhanna/Automatic-Chicken-Door) *(HTTP 200)*

- [ ] **Chicken Coop Opener (Home Assistant + Wemos D1 Mini) — Martin Burns** — `[Masalah #1]` `[Biosekuriti Akses / ESP8266 + Home Assistant YAML]`
  - **Ringkasan:** Demonstrasi pengendali pintu kandang ayam otomatis berbasis Wemos D1 Mini (ESP8266), *motor driver* L298N, dan *encoder* yang terintegrasi penuh ke *dashboard* lokal Home Assistant.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=txGxSdKSX40) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/the-hydra/ChickenCoopOpener) *(HTTP 200)*

- [ ] **Smart Phone Operated Automatic Chicken Coop Door — CodeMakesItGo** — `[Masalah #1]` `[Biosekuriti Akses / Skematik Relai 12V/5V + Kode]`
  - **Ringkasan:** Video uji coba dan panduan skematik rangkaian relai pengendali pintu kandang ayam otomatis yang dapat dipantau lewat ponsel, disertai kode GitHub dan tutorial langkah-demi-langkah di Instructables.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://youtu.be/RmLc_RDQBD4) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/CodeMakesItGo/ChickenCoopDoor) *(HTTP 200)*
    - Dataset/Model: [Instructables Schematic Guide](https://www.instructables.com/Smart-Phone-Operated-Chicken-Coop-Door-/) *(HTTP 200)*

- [ ] **Automatic Chicken Coop Door Using ESP32 — Philipps Projects** — `[Masalah #1]` `[Biosekuriti Akses / ESP32 + Sinkronisasi Waktu + Skematik]`
  - **Ringkasan:** Demo rangkaian elektronik pengendali akses kandang berbasis ESP32 dengan sinkronisasi waktu otomatis yang seluruh diagram skematik dan kodenya dipublikasikan terbuka di Instructables.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=o5P4Rt5eJGE) *(HTTP 200)*
    - Kode: [Instructables Code & Schematic](https://www.instructables.com/Automatic-Chicken-Coop-Door/) *(HTTP 200)*

---

## B. Tutorial AI Deteksi Penyakit & Sistem Manajemen Flok Unggas (Masalah #1)

- [ ] **End-to-End Deep Learning Chicken Disease Classification (MLOps DVC + Docker) — Krish Naik** — `[Masalah #1]` `[CV Feses CNN + MLOps DVC/Docker/CI-CD]`
  - **Ringkasan:** Tutorial implementasi penuh (*end-to-end*) klasifikasi penyakit ayam dari citra feses menggunakan CNN, *Data Version Control* (DVC), Docker, dan pipeline *deployment* GitHub Actions beserta repositori GitHub resmi (90 bintang).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=p1bfK8ZJgkE) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/krishnaik06/Chicken-Disease-Classification-Projects) *(HTTP 200)*

- [ ] **Poultry Farm Management System with Python & Django (`demo-efarm`) — Peter Evance** — `[Masalah #1]` `[Sistem Manajemen Flok / Django Backend + Frontend]`
  - **Ringkasan:** Seri tutorial pembangunan aplikasi manajemen peternakan ayam presisi berbasis Python/Django untuk pencatatan sumber flok, kesehatan, dan pemantauan performa operasional dengan kode sumber lengkap di GitHub (25 bintang).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=_7XbQrQIzKA) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/peter-evance/demo-efarm) *(HTTP 200)*

- [ ] **Computerized Poultry Management System in C# & SQL Server — Iszzytech** — `[Masalah #1]` `[Desktop Recording Flok / C# + SQL Server]`
  - **Ringkasan:** Demonstrasi perangkat lunak desktop manajemen peternakan ayam (C# & SQL Server) untuk pencatatan populasi, mortalitas, dan catatan operasional harian kandang dengan *source code* terbuka di GitHub.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [YouTube](https://www.youtube.com/watch?v=Fnlyil9ettM) *(HTTP 200)*
    - Kode: [GitHub](https://github.com/Iszzytech/computerized-poultry) *(HTTP 200)*
