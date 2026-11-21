# 03 — REPOSITORI GITHUB OPEN-SOURCE: MASALAH #2 (*HEAT STRESS* & INSTABILITAS MIKROKLIMAT TROPIS)

> **Cakupan:** Repositori GitHub non-kosong (*verified code/files*) khusus **Masalah #2** — mencakup deteksi *heat stress* & perilaku flok (CV/Thermal), kontrol cerdas (*Fuzzy Logic*, *Machine Learning*, pemodelan termal & optimasi kipas), pemantauan gas Amonia (`NH₃`) & *Heat Index*/THI, serta IoT mikroklimat kandang (*open house* & *closed house*, termasuk proyek lokal Indonesia).  
> **Anti-Duplikasi:** Seluruh entri unik dan tidak tumpang tindih dengan file `01`, `02`, maupun `05`.  
> `[DATA PRIMER TERVERIFIKASI — TABEL/VISUALISASI DISUSUN OLEH AI AGENT]`

---

## A. Deteksi *Heat Stress*, Suhu Tubuh & Perilaku Flok (Computer Vision & Thermal)

- [ ] **ChickenBot Multimodal Pipeline (`417steven/chickenbot`)** — `[#1 & #2]` `[CV RGB + Kamera Thermal + Korelasi Mikroklimat NH₃/CO₂/RH]`
  - **Ringkasan:** Pipeline analitik multimodal yang menggabungkan kamera ganda RGB + termal inframerah untuk menghitung aktivitas flok, dispersi spasial (*panting/huddling*), dan suhu inti tubuh ayam, lalu mengorelasikannya dengan data suhu, RH, `NH₃`, `CO₂`, dan log aktuator kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/417steven/chickenbot) *(HTTP 200)*

- [ ] **Deteksi Perilaku Ayam Broiler di *Closed House* (`Ruler02/Deteksi-dan-Klasifikasi-Perilaku-Ayam-Broiler-pada-Kandang-Close-House-Berbasis-YOLO-`)** — `[Masalah #2]` `[CV YOLO Perilaku Broiler + Data Suhu Closed House — Indonesia]`
  - **Ringkasan:** Proyek skripsi Indonesia yang menggunakan YOLO untuk mendeteksi dan mengklasifikasikan perilaku ayam broiler di kandang *closed house* dipadukan data suhu sebagai sistem pemantauan kenyamanan kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Ruler02/Deteksi-dan-Klasifikasi-Perilaku-Ayam-Broiler-pada-Kandang-Close-House-Berbasis-YOLO-) *(HTTP 200)*

- [ ] **Flock Stress Detection (`sohvasa/flock-stress-detection`)** — `[Masalah #2]` `[CV Deteksi Stres Flok Ayam — Python]`
  - **Ringkasan:** Implementasi *classifier* berbasis citra untuk mendeteksi indikasi stres pada flok ayam secara otomatis dari pengamatan visual kandang.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/sohvasa/flock-stress-detection) *(HTTP 200)*

- [ ] **Infrared Thermal Imaging Dataset & Preview (`lonlonago/Infrared-Thermal-Imaging-Image-Data-Set-for-Bird-and-Poultry-Detection`)** — `[Masalah #2]` `[Thermal Imaging Deteksi Unggas]`
  - **Ringkasan:** Repositori dokumentasi dan pratinjau citra termal inframerah (*IR thermal*) untuk pengembangan sistem deteksi unggas dan estimasi beban panas permukaan tubuh ayam.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/lonlonago/Infrared-Thermal-Imaging-Image-Data-Set-for-Bird-and-Poultry-Detection) *(HTTP 200)*

---

## B. Kontrol Cerdas Ventilasi, *Fuzzy Logic*, Machine Learning & Pemodelan Termal

- [ ] **Monitoring Gas Berbahaya Kandang Broiler Fuzzy Mamdani (`dryladen/Sistem-Monitoring-Gas-Berbahaya`)** — `[Masalah #2]` `[Fuzzy Logic Mamdani / Amonia NH₃ & Metana — Indonesia]`
  - **Ringkasan:** Sistem pemantauan dan prediksi tingkat bahaya gas amonia (`NH₃`) dan metana di kandang ayam broiler asal Indonesia menggunakan metode inferensi *Fuzzy Mamdani*.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/dryladen/Sistem-Monitoring-Gas-Berbahaya) *(HTTP 200)*

- [ ] **Poultry Farm Ventilation Controller (`bradadam/poultry-farm-ventilation-controller`)** — `[Masalah #2]` `[Fuzzy Logic Control / scikit-fuzzy Ventilasi Kandang]`
  - **Ringkasan:** Sistem kontrol ventilasi kandang ayam otomatis berbasis *Fuzzy Logic Control* (FLC) menggunakan Python dan `scikit-fuzzy` untuk mengatur laju pertukaran udara sesuai kondisi lingkungan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/bradadam/poultry-farm-ventilation-controller) *(HTTP 200)*

- [ ] **Poultry House Exhaust Fan Smart Prediction (`Mahmoudebrahim156/poultry-house-fan--Smart-prediction`)** — `[Masalah #2]` `[ML LightGBM/XGBoost/CatBoost Prediksi Exhaust Fan]`
  - **Ringkasan:** Model *gradient-boosted trees* (LightGBM, XGBoost, CatBoost) untuk memprediksi kebutuhan aktivasi *exhaust fan* kandang ayam secara multi-parameter dari pembacaan suhu, kelembapan, `CO₂`, dan amonia (`NH₃`).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Mahmoudebrahim156/poultry-house-fan--Smart-prediction) *(HTTP 200)*

- [ ] **Optimasi Energi Kipas Kandang Broiler (`hastaputrawildantara99/Optimasi-Penggunaan-Energi-Kipas-Kandang-Broiler-Berdasarkan-Suhu-dan-Kelembapan-Harian`)** — `[Masalah #2]` `[Optimasi Energi Kipas Berbasis Suhu & RH — Indonesia]`
  - **Ringkasan:** Kode eksperimen komputasional asal Indonesia (*Dynamic Programming*, *Greedy*, DFS/BFS) untuk mengoptimalkan penjadwalan dan konsumsi energi listrik kipas kandang broiler berdasarkan profil suhu dan kelembapan harian.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/hastaputrawildantara99/Optimasi-Penggunaan-Energi-Kipas-Kandang-Broiler-Berdasarkan-Suhu-dan-Kelembapan-Harian) *(HTTP 200)*

- [ ] **Cost-Efficient Thermal Regulation (`pradeepkumar2310/cost-efficient-thermal-regulation-poultry-farm`)** — `[Masalah #2]` `[ESP32 + Machine Learning Regulasi Termal Anti-Heat Stress]`
  - **Ringkasan:** Sistem kendali suhu kandang ayam berbiaya rendah berbasis ESP32 dan *Machine Learning* untuk meredam cekaman panas sekaligus menekan pemborosan daya listrik aktuator.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/pradeepkumar2310/cost-efficient-thermal-regulation-poultry-farm) *(HTTP 200)*

- [ ] **Poultry House Thermal & HVAC Model (`picknumber3mylord/Poultry-House-Thermal-Model`)** — `[Masalah #2]` `[Simulasi Fisika Termal & HVAC Kandang — MATLAB]`
  - **Ringkasan:** Kumpulan skrip MATLAB (`MainModel.m`, `MainModelValidation.m`, `MainModelWithHVAC.m`) untuk pemodelan termodinamika panas dan simulasi sistem HVAC/ventilasi di dalam kandang unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/picknumber3mylord/Poultry-House-Thermal-Model) *(HTTP 200)*

---

## C. IoT Pemantauan Gas Amonia (`NH₃`), *Heat Index* (THI) & Pendinginan Otomatis

- [ ] **Poultry Vet Environmental Monitor (`MiftahulSN/poultry-vet-decision-support-system`)** — `[#1 & #2]` `[ESP32-S3 / Suhu + RH + Amonia NH₃ + Debu PM2.5 — Indonesia]`
  - **Ringkasan:** Firmware mikrokontroler ESP32-S3 (C++) asal Indonesia untuk pemantauan multi-parameter kualitas udara kandang unggas meliputi suhu, kelembapan, gas amonia (`NH₃`), dan partikulat debu (`PM2.5`).
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/MiftahulSN/poultry-vet-decision-support-system) *(HTTP 200)*

- [ ] **Heat Index Monitoring & Automated Cooling (`ayayay555/Heat-Index-Monitoring-with-Automated-Cooling-System-for-Poultry-House`)** — `[Masalah #2]` `[ESP + Skematik / Perhitungan Heat Index + Pendingin Otomatis]`
  - **Ringkasan:** Solusi IoT lengkap dengan skematik rangkaian (`schematicESP.png`) dan kode `HeatIndex.ino` yang menghitung *Heat Index* dari suhu & RH lalu mengaktifkan sistem pendinginan otomatis saat ambang stres panas terlampaui.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/ayayay555/Heat-Index-Monitoring-with-Automated-Cooling-System-for-Poultry-House) *(HTTP 200)*

- [ ] **Smart Ammonia Monitoring Poultry Farm (`mugilan2045/SMART-AMMONIA-MONITORING-POULTRY-FARM`)** — `[Masalah #2]` `[IoT + ML LDA/QDA Klasifikasi Gas Amonia NH₃]`
  - **Ringkasan:** Sistem IoT dan *Machine Learning* (komparasi LDA & QDA) untuk memantau konsentrasi gas amonia (`NH₃`) dan parameter lingkungan kandang unggas serta mengklasifikasikan tingkat risiko udara.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/mugilan2045/SMART-AMMONIA-MONITORING-POULTRY-FARM) *(HTTP 200)*

- [ ] **AmmoniaSystems (`maanasvi999/AmmoniaSystems`)** — `[Masalah #2]` `[Arduino + Node-RED + Mobile App Deteksi NH₃]`
  - **Ringkasan:** Sistem deteksi kadar gas amonia kandang ayam berbasis Arduino (`Ammonia.ino`), alur pemrosesan Node-RED, serta purwarupa aplikasi mobile MIT App Inventor untuk peringatan kadar NH₃ tinggi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/maanasvi999/AmmoniaSystems) *(HTTP 200)*

- [ ] **Ammonia Prediction Model Poultry (`al-momen-pranta/ammonia_prediction_model_poultry`)** — `[Masalah #2]` `[ML Prediksi Konsentrasi Amonia + Web API Python]`
  - **Ringkasan:** Model prediktif berbasis Python dengan layanan antarmuka web (`app.py`, `export_weights.py`) untuk mengestimasi lonjakan konsentrasi amonia di dalam kandang unggas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/al-momen-pranta/ammonia_prediction_model_poultry) *(HTTP 200)*

- [ ] **Poultry Shed Environment & Ammonia Monitor (`Ashwin-rathinakumar/Poultry-Ammonia-and-temperature-monitor`)** — `[Masalah #2]` `[IoT Simulasi Suhu & Amonia Kandang]`
  - **Ringkasan:** Proyek simulasi IoT pemantauan suhu dan kadar amonia kandang ayam secara berkelanjutan untuk mendeteksi kondisi udara berbahaya dan memicu tindakan mitigasi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Ashwin-rathinakumar/Poultry-Ammonia-and-temperature-monitor) *(HTTP 200)*

- [ ] **Poultry Ammonia Firestore Monitor (`GitPrasanth05/poultryfarming`)** — `[Masalah #2]` `[IoT Amonia + Firebase Firestore Dashboard]`
  - **Ringkasan:** Antarmuka web pemantauan persentase gas amonia kandang unggas berbasis Firebase Firestore lengkap dengan pencatatan riwayat kadar gas.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/GitPrasanth05/poultryfarming) *(HTTP 200)*

---

## D. IoT Mikroklimat & Otomasi Kandang (*Open/Closed House* — Indonesia & Global)

- [ ] **SmartKandang IoT Dashboard (`alfaerujabadi/smartkandang-iot-dashboard`)** — `[Masalah #2]` `[React Dashboard Monitoring Mikroklimat — Indonesia]`
  - **Ringkasan:** Antarmuka *dashboard* web *real-time* berbasis React asal Indonesia (*SmartKandang*) untuk memantau metrik lingkungan kandang ayam berbasis IoT.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/alfaerujabadi/smartkandang-iot-dashboard) *(HTTP 200)*

- [ ] **Monitoring & Kontrol Lingkungan Kandang Broiler (`hafiztanjung/IOT`)** — `[Masalah #2]` `[NodeMCU + Skematik PCB Kontrol Lingkungan Broiler — Indonesia]`
  - **Ringkasan:** Repositori Indonesia berisi kode firmware NodeMCU (`PROGRAM NODEMCU.ino`) dan file skematik/layout papan sirkuit (`SCHEMATIK DAN BOARD.zip`) untuk pemantauan dan kontrol lingkungan kandang ayam broiler.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/hafiztanjung/IOT) *(HTTP 200)*

- [ ] **Monitoring Suhu Kandang Ayam Wokwi (`regamalik/monitoring-suhu-kandang-ayam`)** — `[Masalah #2]` `[ESP32 + Simulasi Wokwi Suhu Kandang — Indonesia]`
  - **Ringkasan:** Purwarupa pemantauan suhu kandang ayam berbasis mikrokontroler ESP32 (C++) asal Indonesia yang dilengkapi dokumentasi dan simulasi rangkaian Wokwi.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/regamalik/monitoring-suhu-kandang-ayam) *(HTTP 200)*

- [ ] **Kandang Ayam IoT Laravel (`nickyez/kandang-ayam`)** — `[Masalah #2]` `[ESP8266 + Laravel 8 Monitoring & Kontrol Suhu — Indonesia]`
  - **Ringkasan:** Sistem pemantauan dan pengendalian suhu kandang ayam asal Indonesia yang menghubungkan mikrokontroler ESP8266 dengan *backend* web Laravel 8.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/nickyez/kandang-ayam) *(HTTP 200)*

- [ ] **Smart Chicken Box Backend API (`Bagus-DevLab/PKL_PCB_BACKEND`)** — `[Masalah #2]` `[FastAPI Python Backend IoT Kandang Ayam — Indonesia]`
  - **Ringkasan:** Layanan *backend* API berbasis Python FastAPI asal Indonesia untuk menerima, menyimpan, dan melayani telemetri sensor dari perangkat IoT kandang ayam pintar.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/Bagus-DevLab/PKL_PCB_BACKEND) *(HTTP 200)*

- [ ] **ESP8266 Kontrol Suhu-RH & Pakan (`danuragilp/esp8266-chicken-feeder-temp-humidity`)** — `[Masalah #2]` `[NodeMCU ESP8266 + Blynk — Indonesia]`
  - **Ringkasan:** Sistem IoT Indonesia berbasis NodeMCU ESP8266 dan Blynk untuk pemantauan suhu–kelembapan serta kendali pakan otomatis kandang ayam, dilengkapi naskah dokumentasi proyek.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/danuragilp/esp8266-chicken-feeder-temp-humidity) *(HTTP 200)*

- [ ] **Smart Chicken Coop Telegram Alert (`kolarathadvaith/SMART-CHICKEN-COOP`)** — `[Masalah #2]` `[ESP32 Suhu–RH + Ventilasi Otomatis + Telegram Alert]`
  - **Ringkasan:** Sistem kandang pintar berbasis ESP32 yang memantau suhu dan kelembapan, mengaktifkan ventilasi secara otomatis, dan mengirim peringatan darurat ke Telegram.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/kolarathadvaith/SMART-CHICKEN-COOP) *(HTTP 200)*

- [ ] **eXtended Coop Controller (`RastoH/eXtended-Coop-Controller`)** — `[Masalah #2]` `[ESP8266 Kontrol Kipas, Pemanas, Lampu & Pintu]`
  - **Ringkasan:** Firmware ESP8266 matang untuk mengendalikan berbagai aktuator kandang ayam (kipas ventilasi, pemanas, pencahayaan, air, dan pintu otomatis) dengan mode manual maupun otomatis.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/RastoH/eXtended-Coop-Controller) *(HTTP 200)*

- [ ] **Omlet Smart Coop Fan ESPHome (`skolodziej/omlet-fan-esphome`)** — `[Masalah #2]` `[ESPHome + Home Assistant Kontrol Kipas Lokal]`
  - **Ringkasan:** Firmware ESPHome yang beroperasi 100% lokal (tanpa ketergantungan *cloud*) untuk mengintegrasikan kontrol kipas ventilasi kandang ayam pintar ke Home Assistant.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/skolodziej/omlet-fan-esphome) *(HTTP 200)*

- [ ] **Arduino Automated Chicken Coop (`sethpoly/chicken-coop-arduino`)** — `[Masalah #2]` `[Arduino Kontrol Kipas & Pemanas Berbasis Suhu–RH]`
  - **Ringkasan:** Skrip Arduino terpadu untuk mengatur kipas pendingin, lampu pemanas (*heatlamp*), serta pintu kandang secara otomatis berdasarkan pembacaan sensor suhu dan kelembapan.
  - **Tautan Terverifikasi:**
    - Sumber Utama: [GitHub](https://github.com/sethpoly/chicken-coop-arduino) *(HTTP 200)*
