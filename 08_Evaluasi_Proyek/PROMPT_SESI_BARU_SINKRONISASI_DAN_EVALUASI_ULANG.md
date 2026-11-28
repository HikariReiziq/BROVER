# Prompt Sesi Baru: Sinkronisasi Dokumen BROVER dan Evaluasi Ulang

**Cara memakai:**
1. Buka sesi agent baru di folder `/home/reiziqzip/Programmer/Hackathon-UNJ`.
2. Salin seluruh isi mulai dari baris **PROMPT** di bawah sampai akhir berkas.
3. Prompt ini disusun pada 28 November 2026, dari hasil diskusi dan evaluasi yang tercatat di folder `08_Evaluasi_Proyek/`.

---

## PROMPT

### 1. Peran

Kamu adalah penelaah dan editor teknis independen untuk proyek **BROVER** milik Tim Asprak, peserta Hackathon Deep Tech UNJ 2026 jalur D-FARM.

- Jangan membela atau merasionalisasi keputusan dokumen lama buatan AI Agent sebelumnya.
- Setiap klaim harus cocok dengan sumber primernya.
- Bila ada klaim yang tidak bisa diverifikasi, tandai dengan jujur.
- Bekerja dan menulis dalam bahasa Indonesia yang lugas.

### 2. Tujuan

1. **Menyinkronkan** semua berkas di bagian 7 dengan keputusan final tim per 28 November 2026.
2. **Memperbaiki:**
   - inkonsistensi antarberkas;
   - gambar dan diagram yang isinya sudah tidak berlaku atau tidak muncul;
   - klaim yang sudah tidak valid.
3. **Menulis evaluasi ulang** di berkas baru `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md`, setelah sinkronisasi selesai.

### 3. Cara Kerja: Rencana Dulu

1. Baca semua bacaan wajib di bagian 4.
2. Susun rencana perubahan per berkas, termasuk daftar diagram yang akan dirender ulang.
3. **Minta persetujuan user** sebelum mengubah berkas apa pun.
4. Kerjakan bertahap sesuai urutan di bagian 11. Setiap satu kelompok berkas selesai, laporkan singkat apa yang berubah.
5. Bila ada keputusan yang belum dikunci, misalnya nama paket, harga final, atau jalur inferensi paket tanpa rover, tanyakan ke user. Jangan memutuskan sendiri.

### 4. Bacaan Wajib, Berurutan

1. `MEMORY.md` dan `HISTORY.md` di root repo. Keduanya memuat aturan repo dan template entri riwayat.
2. `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md`. **Ini sumber kebenaran keputusan dan bukti terbaru.** Isinya kartu empat fitur final, bukti amonia dan penyakit pernapasan, rekomendasi untuk peternak, fitur yang dihapus beserta alasannya, dan 78 tautan yang sudah diuji dua kali.
   - Ada empat keputusan yang lebih baru dari isi PETA_FITUR: peran ganda foto HP, servo tetap, rincian otomatisasi, dan dua paket langganan. Untuk keempatnya, ikuti bagian 5 prompt ini.
3. `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md`. Ini baseline temuan evaluasi pertama. Sebagian rekomendasinya sudah digantikan keputusan baru, lihat bagian 6.
4. Berkas target di bagian 7.
5. Memori otomatis proyek yang dimuat otomatis di sesi ini, yaitu `brover-feature-scope` dan `independent-critical-review`. Bila ada perbedaan, **prompt ini dan PETA_FITUR yang berlaku**.

### 5. Keputusan Final yang Terkunci

Keputusan ini tidak boleh diubah tanpa izin user.

1. **Judul:** BROVER: Sistem Inspeksi Multisensor Berbasis AI dan Edge-Cloud untuk Skrining Gejala Penyakit serta Pemantauan Mikroklimat Kandang Ayam Broiler.
   - Tanpa tanda kurung.
   - Kepanjangan merek *Broiler Inspection & Health Rover* hanya ditulis di bagian filosofi.
   - Pakai kata *skrining*. Jangan memakai *deteksi dini*, *deteksi penyakit*, *multi-modal*, atau *prediksi* sebagai klaim BROVER.
2. **Empat fitur final:**
   - **F1 Rover Inspeksi** membawa kamera feses. Pada prototipe, rover masih dikendalikan manual lewat web.
     - **Foto HP punya dua peran:** cadangan saat rover tidak bisa masuk pada paket rover, dan **jalur utama pada paket tanpa rover**. Lihat butir 9.
     - **Kamera USB UVC IMX291 dengan servo tahan air DS3218 tetap dipakai**, dengan dua posisi. Posisi depan sekitar 0 sampai 15 derajat untuk tampilan FPV saat operator menyetir, dan kelak untuk CV navigasi. Posisi bawah sekitar 45 derajat untuk foto feses. Lihat butir 11.
   - **F2 Sensor Mikroklimat di Rover:**
     - SHT31 dan SEN0567 dipasang di tiang setinggi ayam, jauh dari panas Orange Pi dan motor.
     - **Mode stasiun:** saat tidak berkeliling, yaitu malam hari, saat diisi daya, dan hari ke-0 sampai 6, rover parkir di dok di dalam kandang dan mencatat setiap menit.
     - Dok ditempatkan di area *brooding* atau tengah kandang, dan butuh stopkontak.
   - **F3 CV Feses** adalah satu-satunya AI.
     - Detektor berlisensi **Apache-2.0**, yaitu YOLOX atau RT-DETR, sejalan dengan TA feses user. Tetap jujur bahwa hasil TA belum ada.
     - Dikuantisasi INT8 untuk NPU Orange Pi 3B. Raspberry Pi 4 menjadi PoC.
     - Keluaran berbunyi *pola feses mirip koksidiosis, perlu konfirmasi dokter hewan*.
   - **F4 Dasbor:**
     - standar umur Cobb 500 dan Ross 308, serta THI;
     - tren amonia per zona pada jam yang sama, ditambah tren di dok;
     - tren deplesi, pakan, dan air harian dari catatan ABK;
     - triase dengan tiga tombol *Akan Saya Cek*, *Terlihat Normal*, dan *Laporkan ke Dokter Hewan*;
     - ceklis gejala pernapasan oleh ABK;
     - catatan vaksinasi;
     - laporan 1-klik ke dokter hewan;
     - cuaca dari BMKG adm4 dengan cadangan Open-Meteo;
     - **tanpa skor 0 sampai 100**.
3. **Dihapus dari MVP:**
   - AI audio, termasuk mikrofon INMP441, fitur *Cek Napas 15 detik*, dan *Stop-Mute-Sample*;
   - CV fisik dan perilaku ayam, yaitu Model #2;
   - deteksi bangkai;
   - node sensor tetap;
   - sensor CO2.
4. **Pengembangan lanjutan P2:**
   - modul CO2 untuk kandang berpemanas gas;
   - kamera termal untuk peta panas permukaan kelompok ayam, bukan suhu tubuh per ekor;
   - riset mikrofon tetap per kandang, dengan peluang kolaborasi data bersama penulis UGM;
   - **otomatisasi rover**, sementara prototipe tetap dikendalikan manual:
     - **CV navigasi:** deteksi ayam dan halangan di depan rover untuk menentukan kapan berhenti, melambat, atau berbelok. Data deteksi ayam seperti [PIO](https://zenodo.org/records/16686320), [YOLOv5-CBAM broiler di atas sekam](https://doi.org/10.1016/j.aiia.2023.08.002), dan [Big Broiler](https://github.com/decide-ugent/big-broiler-dataset) dipakai untuk navigasi, bukan untuk penyakit.
     - **Penjadwalan otomatis:** putaran terjadwal, ditambah putaran khusus saat THI atau amonia di dok melewati ambang.
     - **Rujukan:** [Marin dkk. 2024](https://doi.org/10.1016/j.psj.2024.103710) memakai robot navigasi otonom di kandang broiler. Rujukan lain: [PoultryBot 2018](https://doi.org/10.1016/j.biosystemseng.2018.07.015), serta [Octopus XO](https://www.octopusbiosafety.com/en/faq/xo-en/) yang memetakan lingkungan kandang.
5. **Operasi rover:**
   - setiap hari dari hari ke-7 sampai panen. Umur panen closed house Indonesia sekitar 27 sampai 35 hari;
   - 2 putaran per hari di MVP, yaitu pagi dan sore pukul 15.00 sampai 16.00. Menjadi 3 putaran setelah otomatisasi;
   - tidak berkeliling terus-menerus;
   - berhenti di titik zona tetap;
   - kecepatan awal 0,07 sampai 0,1 m/s;
   - bumper depan lunak;
   - sensor jarak memperlambat laju, tidak menghentikan total;
   - kriteria berhenti sesi: ayam tidak menyingkir, ada ayam terdorong jatuh atau terluka, atau suhu melewati ambang cekaman panas.
6. **Amonia:**
   - SEN0567 dikalibrasi terhadap alat acuan saat pilot;
   - ambang target di bawah 10 ppm, waspada sekitar 10 sampai 15 ppm, bahaya sekitar 25 ppm atau lebih;
   - tulis *amonia meningkatkan risiko penyakit pernapasan*, jangan *amonia menyebabkan CRD*.
7. **Penyakit pernapasan** ditangani lewat pencegahan, yaitu pemantauan amonia, kelembapan, dan suhu, ditambah ceklis ABK dan dokter hewan. Feses menjawab koksidiosis serta sebagian tanda ND dan salmonelosis.
8. **Latar belakang:**
   - Kasus Hari Farm adalah peternakan petelur. Di concept, ganti dengan kasus koinfeksi Hartady dkk. 2026 dan studi antibiotik Sunandar dkk. 2024.
   - Grafik PCR Medion diberi catatan bahwa isinya campuran broiler dan petelur.
   - Angka Rp22,89 sampai Rp57,35 juta ditulis sebagai simulasi margin kotor wabah HPAI, bukan kerugian umum semua penyakit.
9. **Bisnis: dua paket langganan**, supaya peternak kecil sampai besar bisa memakai BROVER.
   - **Paket tanpa rover:** akses CV skrining feses lewat foto HP. Sasarannya peternak kecil.
   - **Paket dengan rover:** rover lengkap dengan kamera, servo, sensor, dok, dan perangkat lainnya. Sasarannya peternak menengah dan besar.
   - Skema beli putus *All-In* tanpa langganan bulanan di concept **diganti** kedua paket ini. Bila ada alasan kuat mempertahankan opsi beli putus, ajukan ke user.
   - **Nama paket dan isi paket tanpa rover**, yaitu fitur dasbor mana yang ikut, diusulkan sesi baru lalu dikonfirmasi user.
   - **Harga** ditentukan lewat riset di bagian 7A. Jangan memakai angka tanpa sumber atau tanpa label asumsi.
   - Proyeksi ROI 498 persen dan grafik 5 tahun diganti **titik impas**:
     - untuk peternak: berapa ekor ayam yang harus terselamatkan per siklus agar biaya tiap paket tertutup;
     - untuk tim: berapa lama modal rover kembali lewat langganan.
   - **Langganan rover berlaku per kandang.** Saat kontrak berakhir dan unit dipindah ke peternakan lain, wajib ada protokol pembersihan dan disinfeksi berbasis bukti. Tanpa protokol itu, pemindahan bertentangan dengan SOP 1 unit untuk 1 kandang.
   - Sewa antarfarm jangka pendek, misalnya sewa per siklus yang berpindah-pindah, tetap dilarang.
   - BMC dan diagram 07 diperbarui sesuai kedua paket.
10. **Kalimat pembuka Ringkasan concept:**
    > BROVER memantau amonia, kelembapan, dan suhu setinggi ayam sebagai faktor pemicu penyakit pernapasan, menskrining tanda penyakit pencernaan pada feses dengan computer vision, dan meneruskan bukti ke dokter hewan, tanpa mengklaim diagnosis.
11. **Kamera terkunci: kamera USB UVC IMX291 dan servo tahan air DS3218**, sesuai BOM concept. Servo menggerakkan kamera antara posisi depan dan posisi bawah. Foto feses diambil saat rover berhenti, sehingga satu kamera yang dimiringkan servo sudah cukup. Opsi lain sudah dipertimbangkan dan tidak dipakai:
    - **Kamera PTZ CCTV**, misalnya Tapo C200. Firmware-nya tertutup, kendali putar lewat ONVIF tidak konsisten antarversi firmware, dan jeda video RTSP dilaporkan sekitar 1 detik atau lebih. Terlalu lambat untuk menyetir rover.
    - **Kit *pan-tilt* siap pakai**, misalnya Waveshare atau Arducam. Mahal, stok lokal sedikit, dirancang untuk ruangan bersih, dan kamera CSI-nya belum tentu cocok dengan Orange Pi 3B.
    - **Dua kamera USB tetap**, satu menghadap depan dan satu menghadap bawah, hanya dicatat sebagai cadangan bila servo bermasalah saat uji lapangan.

### 6. Rekomendasi dan Skema Lama yang Sudah Digantikan

| Rekomendasi atau Skema Lama | Keputusan yang Berlaku |
| :--- | :--- |
| Platform hibrida dengan node tetap dan aplikasi HP | Rover dengan foto HP cadangan dan mode stasiun |
| Node sensor tetap 2 sampai 4 titik | Dibatalkan. Sensor tetap di rover. |
| Batas operasi hari 5 sampai 23 | Hari ke-7 sampai panen |
| Model #2 diubah menjadi kandidat bangkai | Model #2 dan deteksi bangkai dihapus |
| Audio diturunkan menjadi rekam dan putar ulang | Audio dihapus seluruhnya |
| Usulan judul alternatif di Bab 2.3 | Judul final di bagian 5 |
| Saran PETA_FITUR menghapus servo atau memakai dudukan kamera tetap 45 derajat | Kamera USB IMX291 dengan servo DS3218 tetap dipakai |
| Foto HP hanya sebagai cadangan rover | Foto HP juga jalur utama paket tanpa rover |
| Skema beli putus *All-In* tanpa langganan bulanan di concept | Dua paket langganan: tanpa rover dan dengan rover |
| Semua bentuk sewa dilarang | Langganan rover per kandang boleh, asal ada protokol pemindahan unit. Sewa antarfarm jangka pendek tetap dilarang. |

Rekomendasi lain di evaluasi lama tetap berlaku bila tidak bertentangan dengan bagian 5. Contohnya koreksi fakta di bagian 9, koreksi tabel dataset, dan perumusan ulang keselarasan mitra PT Zara dan PT Edura.

### 7. Berkas dalam Lingkup dan Tugasnya

| Berkas | Tugas |
| :--- | :--- |
| `06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md` | **Sumber utama, kerjakan pertama.** Rincian tugas ada di bawah tabel. |
| `README.md` | **Jangan diedit manual.** Setelah concept selesai, jalankan `06_Project_Concept_BROVER/scripts/sync_readme.py`. Skrip ini menyalin concept dan mengubah path relatif. |
| `MEMORY.md` | Perbarui identitas, judul, empat fitur, arsitektur, *hard constraints*, status, dan langkah berikutnya. Rujuk PETA_FITUR dan evaluasi ulang. |
| `HISTORY.md` | Tambah **satu entri baru paling atas** sesuai template di berkasnya. Jangan mengubah entri lama. |
| `.agent/rules/hackathon-context.md` | Berkas ini selalu dibaca agen lain. Perbarui sorotan utama yang masih menulis *Deteksi Dini*, kapabilitas tim yang masih menulis *Audio AI*, dan tabel routing yang masih menulis *5 fitur*. |
| `01_Context_Memory/01_TEAM_AND_CONSTRAINTS.md` | Kapabilitas *Multi-Modal AI* menjadi CV feses ditambah IoT. Perbarui sorotan utama dan baris WOAH agar memakai *skrining*. |
| `01_Context_Memory/02_HACKATHON_DFARM_RULES.md`, `03_MITRA_PT_ECG_EDURA.md`, `04_MITRA_PT_ZARA_PROPERTIFARM.md` | Periksa saja. Ubah hanya bila ada fakta yang bertentangan. Pernyataan keselarasan mitra di concept harus cocok dengan isi berkas ini. |
| `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md` dan `.md.pdf` | Ini dokumen masalah, bukan solusi, jadi koreksinya minimal. Beri label petelur pada kasus Hari Farm. Verifikasi ulang angka Wilcox 62 persen *severe discomfort* dan skor Anwar Sani 0,28 ke sumber atau lampirannya. **Buat ulang PDF** dengan 37 gambar. |
| `03_Root_Cause_Analysis/ROOT_CAUSE_PENYAKIT_BIOSEKURITI_DAN_HEAT_STRESS.md` dan `.md.pdf` | Sama: label petelur pada Hari Farm dan verifikasi angka 0,28. **Buat ulang PDF** dengan 5 gambar. |
| `07_IoT_Hardware_Guide/01_PANDUAN_TAHAP1_ROVER_KONTROL_WEB.md`, `02_PANDUAN_TAHAP2_PROTOTYPE_LENGKAP_AI_SENSOR.md`, `03_PANDUAN_IOT_FINAL_FIELD_READY.md` | Rincian tugas ada di bawah tabel. |
| Diagram di `06_Project_Concept_BROVER/assets/` | Lihat bagian 8. |
| `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md` | Berkas baru. Lihat bagian 10. |

**Rincian tugas concept:**
- Ubah semua bab sesuai bagian 5, dan hapus Fitur 4 audio serta Model #2.
- Bab 3: latar belakang.
- Bab 4.1: F1 dengan dua peran foto HP dan servo dua posisi.
- Bab 4.3: tabel batasan. Baris WOAH dan klaim diagnosis memakai *skrining*.
- Bab 4.4: SOTA, kebaruan, dan KPI.
  - Talingan dari Indonesia tahun 2020 dan AvianAlert pemenang Cornell 2025 sudah memakai suara, jadi kebaruan BROVER tidak boleh bersandar pada fitur itu.
  - Hapus KPI audio.
- Bab 5: tech stack, dengan detektor Apache-2.0 dan tanpa pustaka audio.
  - Rancang jalur inferensi paket tanpa rover. Ajukan pilihan antara server cloud dan perangkat HP, dengan pertimbangan biaya, sinyal internet di desa, dan prinsip *offline-first*, lalu minta keputusan user.
- Bab 6: cara kerja, berisi jadwal putaran, titik zona, mode stasiun, unggah foto HP, dan catatan harian ABK.
- Bab 7: komponen PoC, tanpa mikrofon.
- Bab 8: BOM dan HPP.
  - Hapus INMP441, Rp45.000 eceran atau Rp36.000 grosir.
  - Hitung ulang subtotal dan HPP.
  - Tulis kebutuhan dok dan stopkontak.
  - Kamera USB IMX291 dan servo DS3218 tetap di BOM. Alasan tidak memakai kamera PTZ CCTV dan kit *pan-tilt* boleh dicatat singkat, sesuai bagian 5 butir 11.
- Bab 9:
  - dua paket langganan dengan hasil riset harga dari bagian 7A;
  - BMC, *unit economics*, dan titik impas;
  - protokol pemindahan unit rover;
  - *risk register* dan timeline.
- Bab 9.5 dan *future work*: CV navigasi dan penjadwalan otomatis.
- Bab 10: kesimpulan.
- Bab 11: dataset.
  - Hapus dataset audio, fisik, dan bangkai.
  - Koreksi Zenodo 5801834.
  - Pertimbangkan Mendeley 8pnbzpt2k9 dan Wang 2019.
  - Data deteksi ayam seperti PIO, YOLOv5-CBAM, dan Big Broiler ditempatkan di bagian riset lanjutan navigasi.
- Bab 12: referensi.
  - Tambah rujukan bukti baru dari PETA_FITUR.
  - Rujukan yang hanya dipakai fitur yang dihapus dipindah ke bagian riset lanjutan atau dihapus.
- Perbarui juga semua keterangan di bawah gambar.

**Rincian tugas panduan IoT:**
- Hapus semua bagian audio: INMP441, mikrofon USB, *Cek Napas*, dan *pipeline* audio.
- Hapus Model #2, serta data audio dan data fisik ayam.
- Tulis sensor di tiang rover, dok, dan mode stasiun.
- Koreksi tautan dataset. Zenodo 5801834 tidak punya label YOLO.
- Detektor memakai Apache-2.0: NCNN atau ONNX di Raspberry Pi 4 untuk PoC, dan RKNN di Orange Pi 3B untuk versi final.
- Hapus rujukan foto mikrofon. Servo, kamera, dan fotonya tetap.

**Jangan diubah:**
- folder `Proposal TA/`;
- `08_Evaluasi_Proyek/EVALUASI_OBJEKTIF_BROVER.md`, karena menjadi baseline;
- `08_Evaluasi_Proyek/PETA_FITUR_DAN_BUKTI_BROVER.md`. Pengecualiannya: bagian yang terdampak keputusan baru, yaitu servo, peran foto HP, otomatisasi, dan bisnis, boleh diperbarui supaya tetap menjadi sumber kebenaran. Kekeliruan faktual juga boleh diperbaiki. Catat setiap perubahannya di evaluasi ulang.

### 7A. Riset Harga Paket

Harga kedua paket ditentukan dari riset, bukan tebakan.

1. **Ekonomi peternak** dari sumber terverifikasi: margin per siklus, harga ayam hidup, biaya produksi per ekor, FCR, dan deplesi. Sebagian sudah ada di `02_Problem_Research/TOP_5_MASALAH_PETERNAKAN_UNGGAS_INDONESIA_V3_TRANSPARAN.md` dan lampirannya di `02_Problem_Research/assets_v3/lampiran_jurnal_asli/`.
2. **Pembanding harga layanan agritech di Indonesia**, misalnya Chickin, Pitik, dan BroilerX untuk unggas, serta eFishery sebagai analog.
   - Ini baru kandidat.
   - Setiap harga wajib diverifikasi ke laman resmi atau dokumen publik.
   - Harga yang gagal diverifikasi tidak dipakai.
3. **Biaya tim:** HPP rover dari BOM baru, biaya server, dukungan teknis, garansi, dan penggantian unit.
4. **Satuan harga:** pilih per bulan atau per siklus pemeliharaan, berdasarkan kebiasaan pembayaran peternak, dan tulis alasannya.
5. **Keluaran:**
   - rentang harga per paket;
   - titik impas peternak per paket, dalam jumlah ekor ayam per siklus;
   - lama balik modal rover bagi tim;
   - analisis sensitivitas, misalnya bila harga ayam hidup naik atau turun;
   - setiap asumsi diberi label asumsi.
6. **Harga final diputuskan user.**

### 8. Pembaruan Gambar dan Diagram, Wajib

Semua gambar dan diagram harus mencerminkan keputusan di bagian 5. Hasil pindaian teks SVG pada 28 November 2026:

| Diagram di `06_Project_Concept_BROVER/assets/` | Isi Lama | Isi Baru | Skrip Pembuat |
| :--- | :--- | :--- | :--- |
| `03_arsitektur_sistem_brover` | Judul *MULTI-MODAL AI*, *Mikrofon Pernapasan 15 dtk*, *Deteksi Dini*, feses dan fisik ayam, klip audio | Judul *Multisensor Berbasis AI dan Edge-Cloud*. **Dua jalur:** paket rover dengan kamera feses, servo, SHT31 dan SEN0567 di tiang, dok, mode stasiun, dan inferensi di *edge*; serta paket tanpa rover dengan foto HP dan jalur inferensi sesuai keputusan user. *Skrining*. Detektor Apache-2.0. | `scripts/generate_architecture_svg.py` |
| `04a_pola_jalur_inspeksi_rover` | 5 titik *Cek Napas 15 dtk*, *3×5 dtk* | Titik zona: foto feses dan baca suhu, RH, NH3; lokasi dok di dalam kandang; 2 putaran per hari; mode stasiun | `scripts/generate_workflow_svgs.py` |
| `04b_alur_4tahap_inspeksi_brover` | *ALUR KERJA INSPEKSI MULTI-MODAL*, ayam lesu dan mati, suara ngorok, *Audio SmartEars* | CV feses; status mikroklimat; ceklis ABK; triase 3 tombol; laporan dokter hewan | `scripts/generate_workflow_svgs.py` |
| `04c_user_flow_brover` | Tombol *Cek Napas*, kamera fisik, audio | Alur paket rover dan alur paket tanpa rover. Catatan harian ABK berisi deplesi, pakan, air, ceklis, dan vaksin. | `scripts/generate_business_timeline_svgs.py` |
| `05_komparasi_komputasi_dan_baterai_brover` | *3 model + audio* | Satu model CV feses | Fungsi `make_fig5_hardware_power` di `scripts/generate_concept_visuals.py` |
| `06_roadmap_tkt_dan_evolusi_brover` | *Skema beli sepaket & sewa peternak* | Tanpa sewa antarfarm. *Future work*: CV navigasi untuk berhenti, melambat, dan berbelok; penjadwalan otomatis; CO2; termal; dan audio sebagai riset. | `scripts/generate_business_timeline_svgs.py` |
| `07_business_model_canvas_brover` | *Deteksi Dini 3-in-1*, fisik ayam, suara ngorok, *Sewa per Siklus Rp550-650 ribu*, data audio | Dua paket langganan untuk segmen peternak kecil sampai besar. Proposisi nilai: skrining feses, mikroklimat dan amonia, laporan dokter hewan. Pendapatan dari langganan. Biaya dari BOM baru dan server. | `scripts/generate_business_timeline_svgs.py` |
| `08_project_timeline_brover` | Pola lama tidak terdeteksi | Tinjau isinya. Tambah set uji lokal feses, kalibrasi SEN0567, dan pilot mulai hari ke-7. Hapus tugas audio atau Model #2 bila ada. | `scripts/generate_business_timeline_svgs.py` |
| `09_proyeksi_keuntungan_5tahun_brover` | ROI 199, 498, dan 885 persen; skema sewa | Grafik **titik impas per paket** dan perbandingan harga kedua paket. Nama berkas boleh diganti, asal semua tautan ikut diperbarui. | `scripts/generate_business_timeline_svgs.py` |
| `04d_ilustrasi_rover_4wd_poc` | PNG, belum diperiksa | Lihat gambarnya. Bila ada mikrofon atau label lama, ganti atau beri catatan. | Tidak ada skrip |

**Aturan render:**
- `python3` bawaan sistem adalah versi 3.15 **tanpa** Playwright dan pustaka markdown. Jalankan skrip SVG dengan:
  ```bash
  uv run --python 3.13 --with playwright==1.63.0 python 06_Project_Concept_BROVER/scripts/<skrip>.py
  ```
- Browser Playwright sudah tersimpan di `~/.cache/ms-playwright`, yaitu `chromium-1243` dan `chromium_headless_shell-1243/1248`. Bila versinya tidak cocok, minta izin user sebelum mengunduh browser.
- **Jangan menjalankan `generate_concept_visuals.py` secara penuh.** Fungsi `main` di skrip itu juga memanggil `make_fig6_roadmap`, yang akan menimpa PNG roadmap 06 versi SVG dengan versi lama. Untuk diagram 05, panggil fungsinya saja, misalnya:
  ```bash
  uv run --python 3.13 --with matplotlib python -c "import sys; sys.path.insert(0,'06_Project_Concept_BROVER/scripts'); import generate_concept_visuals as g; g.make_fig5_hardware_power()"
  ```
- **Setelah render:**
  - buka setiap PNG untuk memastikan teks baru tampil dan tidak terpotong;
  - grep teks SVG untuk pola lama harus kosong;
  - jalankan `sync_readme.py` supaya README memakai gambar baru.

**Gambar lain:**
- **Panduan IoT:** hapus rujukan foto mikrofon `assets/poc/40_inmp441_i2s_mic.jpg`, `assets/poc/10_usb_microphone.jpg`, dan `assets/final/15_inmp441_i2s_mic.jpg`. Berkas fotonya boleh tetap ada di folder. Foto komponen diambil oleh `07_IoT_Hardware_Guide/scripts/fetch_component_images.py`.
- **TOP5 dan RCA** memuat gambar sisi masalah. Periksa secara visual, dan buat ulang hanya bila isinya keliru, misalnya Hari Farm tanpa label petelur.
  - Skrip pembuat hanya ada untuk diagram lingkaran setan RCA, yaitu `03_Root_Cause_Analysis/scripts/generate_vicious_cycle.py`, yang memakai matplotlib.
  - Fishbone RCA dan grafik TOP5 tidak punya skrip. Bila perlu diubah, buat skrip baru di folder `scripts/` masing-masing.

**PDF yang gambarnya hilang:**
- PDF TOP5 hanya memuat 6 dari 37 gambar, dan PDF RCA hanya 3 dari 5. Keduanya dibuat 20 November lewat Firefox dari berkas `*_tmp.html` yang memakai path `file:///` absolut, sebelum gambar lampiran ditambahkan pada 24 November.
- **Buat ulang PDF dengan nama yang sama**, yaitu `*.md.pdf`:
  - konversi markdown ke HTML, dengan tabel aktif dan path gambar yang benar;
  - cetak lewat Playwright Chromium `page.pdf` berukuran A4 dengan latar dicetak;
  - Firefox bisa menjadi cadangan cetak manual oleh user.
- Berkas `*_tmp.html` dan `*.md.pdf` terlacak git. Perbarui keduanya secara konsisten, atau **tanya user** sebelum menghapus `*_tmp.html`.
- Verifikasi dengan `pdfimages -list`: jumlah gambar di PDF TOP5 harus 37 dan di PDF RCA harus 5.

### 9. Fakta yang Wajib Dikoreksi

Semua fakta ini sudah diverifikasi di evaluasi lama. Tautannya ada di PETA_FITUR atau EVALUASI_OBJEKTIF.

| Klaim Lama | Fakta |
| :--- | :--- |
| AviSense sekitar 0,09 m/s | Sekitar 0,05 m/s, menurut PMC13696172 |
| Parajuli 2020: 0,1 m/s aman | Hanya menguji 0,2, 0,4, dan 0,6 m/s pada ayam umur 2 sampai 8 minggu |
| Octopus XO sekitar 80 kg | Bobot tidak tercantum di FAQ. Yang tercantum lebar robot 80 cm, hari ke-5 sampai sekitar 23, dan harga 20 sampai 34 ribu euro. |
| ChickenBoy di atas Rp100 juta dan memantau suara | Harga tidak tercantum di brosur. Yang ada hanya sensor tingkat kebisingan. |
| ISO 8373:2021 Pasal 4.16 | Nomor pasal tidak bisa diverifikasi dari sumber terbuka. Hapus nomor pasal, atau verifikasi dari dokumen resmi. |
| Ultralytics di Raspberry Pi 4 sekitar 2,3 FPS | Angka itu tidak lagi ada di laman dokumentasi. Hapus, atau ganti dengan hasil uji tim sendiri. |
| Tautan akar API BMKG | Akarnya 404. Pakai endpoint adm4 atau `data.bmkg.go.id`. |
| aremyhens.fit sebagai rujukan UX tanpa skor | Dasbornya menampilkan *Barn health 0/100*. Yang boleh dirujuk hanya tiga tombol tindakannya. |
| Zenodo 5801834 berisi label YOLO | Hanya arsip klasifikasi PCR, tanpa broiler |
| ChickenVerse untuk postur abnormal | 15 perilaku normal, lisensi nonkomersial. Sudah tidak relevan karena CV fisik dihapus. |
| Grafik PCR Medion | Campuran broiler dan petelur. Grafik klinis broiler terpisah. |
| Pramuwidyatama 2023 sebagai kerugian umum | Simulasi margin kotor khusus wabah HPAI |
| Kasus Hari Farm | Peternakan petelur sekitar 10 ribu ekor |
| Tabel RH Cobb | Berhenti di 70 persen. Aturan untuk RH tropis yang lebih tinggi perlu disusun bersama dokter hewan. |
| Tabel Ross 308 di Bab 4.2 | Perlu divalidasi ke dokumen resmi Aviagen |
| Wilcox 62 persen dan Anwar Sani 0,28 | Belum terverifikasi penuh. Cek ulang ke sumber atau lampiran lokal di `02_Problem_Research/assets_v3/lampiran_jurnal_asli/`. |
| SmartEars 44,1 kHz dan kelas None | Tidak relevan lagi karena audio dihapus. Pastikan tidak tersisa di bagian fitur. |

### 10. Spesifikasi Evaluasi Ulang

- **Berkas:** `08_Evaluasi_Proyek/EVALUASI_ULANG_BROVER.md`.
- **Isi minimal:**
  1. Ringkasan putusan dan peta prioritas.
  2. Tabel status **setiap temuan dan rekomendasi** di EVALUASI_OBJEKTIF: Selesai, Sebagian, Belum, atau Digantikan keputusan. Sertakan bukti lokasi di berkas.
  3. Audit konsistensi antarberkas: judul, fitur, angka BOM dan HPP, jadwal rover, dataset, model, dan rujukan.
  4. Kecocokan judul dengan isi concept, frasa demi frasa.
  5. Kartu fitur: apakah setiap klaim punya bukti.
  6. Bisnis: periksa riset harga, titik impas per paket, lama balik modal rover, konsistensi kedua paket langganan di semua berkas dan BMC, serta protokol pemindahan unit rover.
  7. Kesiapan per rubrik juri, yaitu Kebaruan 30 persen, Relevansi 25 persen, Kelayakan Teknis 20 persen, Bisnis 15 persen, dan Tim 10 persen, ditambah titik serangan juri beserta jawabannya.
  8. **Audit gambar dan diagram:** teks setiap diagram, rujukan gambar markdown, dan jumlah gambar di PDF.
  9. Sisa risiko dan daftar perbaikan berprioritas.
  10. Tabel seluruh tautan dengan **uji dua kali** dan catatan verifikasi isi.
- **Gaya ketat**, sama dengan evaluasi pertama:
  - tanpa em-dash, petik ganda, petik tunggal, atau apostrof;
  - tanpa simbol pasal;
  - tanpa tanda kurung di luar sintaks tautan `[teks](https://...)`;
  - tanpa kata klise seperti *revolusioner*, *holistik*, *krusial*, atau *lanskap*;
  - tanpa jargon *wahana*, *UAV*, *patroli*, *LAN-First*, atau *derau lingkungan*;
  - preprint seperti arXiv, bioRxiv, medRxiv, dan SSRN tidak boleh menjadi bukti utama.
- **Alat yang sudah disiapkan di `08_Evaluasi_Proyek/tools/`:**
  - `python3 -I 08_Evaluasi_Proyek/tools/check_style.py <berkas.md>` menghitung pelanggaran gaya. Targetnya TOTAL MASALAH 0.
  - `python3 -I 08_Evaluasi_Proyek/tools/check_links.py <berkas.md> <hasil.json>` menguji semua tautan dan mencocokkan judul DOI ke Crossref. Jalankan dua kali.
  - `python3 -I 08_Evaluasi_Proyek/tools/make_table.py <uji1.json> <uji2.json> <tabel.md> <ringkasan.md>` membuat tabel tautan dan ringkasan. Judul bab di keluarannya disesuaikan dengan nomor bab evaluasi ulang.
  - `notes.py` berisi kamus catatan verifikasi untuk 155 URL yang sudah dicek. Tambahkan catatan untuk setiap URL baru sebelum menjalankan `make_table.py`.

### 11. Urutan Kerja

1. Rencana per berkas, lalu minta persetujuan user.
2. Riset harga paket sesuai bagian 7A, lalu concept.
3. Diagram: perbarui teks skrip, render, lalu periksa secara visual.
4. `sync_readme.py` untuk README.
5. MEMORY, `.agent/rules/hackathon-context.md`, dan 01_Context_Memory.
6. Panduan IoT 01 sampai 03.
7. TOP5 dan RCA, lalu buat ulang PDF-nya.
8. Entri HISTORY.
9. Pemeriksaan konsistensi lintas berkas, sesuai bagian 13.
10. Evaluasi ulang.
11. Laporan akhir ke user.

### 12. Aturan dan Larangan

- ***Hard constraints* proyek:**
  - hanya jalur D-FARM dengan fokus ayam broiler;
  - tolak topik limbah dan sampah;
  - tidak memakai sensor suhu tubuh IR atau thermogun;
  - pengadaan 100 persen dari e-commerce dan distributor lokal Indonesia;
  - menurut WOAH, BROVER bukan alat biosekuriti dan bukan alat diagnosis otomatis, serta tidak meresepkan antibiotik;
  - tanpa skor 0 sampai 100;
  - SEN0567 dilaporkan sebagai indikator tren kualitatif;
  - preprint bukan bukti utama.
- **Verifikasi:** setiap klaim baru diverifikasi di sumber primer. Jangan mengarang angka. Tandai yang tidak bisa diverifikasi.
- **Berkas:**
  - jangan mengubah folder `Proposal TA/`;
  - jangan menghapus atau menimpa berkas tanpa melihat isinya. Untuk menghapus berkas yang terlacak git, minta izin user dulu;
  - PDF SmartEars di `08_Evaluasi_Proyek/` berhak cipta Elsevier. Jangan di-commit, dan tanya user sebelum memindahkannya atau mengubah `.gitignore`.
- **Git:**
  - jangan commit atau push tanpa perintah eksplisit user;
  - bila diminta commit: tulis entri HISTORY.md, selaraskan MEMORY.md, dan pakai Conventional Commits;
  - **DILARANG menyertakan `Co-Authored-By` atau atribusi AI maupun model apa pun.**
- **Gaya berkas proyek:**
  - pertahankan gaya penulisan yang sudah ada di masing-masing berkas;
  - istilah teknis bahasa Inggris dimiringkan;
  - hindari jargon *wahana*, *UAV*, *patroli*, *LAN-First*, dan *derau lingkungan*.

### 13. Pemeriksaan Akhir Sebelum Melapor

1. **Grep istilah lama** di semua berkas lingkup. Hasilnya hanya boleh muncul di konteks yang sah:

| Pola | Konteks yang Masih Boleh |
| :--- | :--- |
| `Multi-?Modal`, `multimodal` | Judul rujukan Baltrušaitis, nama dataset pihak lain, dan entri HISTORY lama |
| `Deteksi Dini` | Rumusan masalah di TOP5 dan RCA, serta entri HISTORY lama. Tidak boleh sebagai klaim BROVER. |
| `INMP441`, `mikrofon`, `audio`, `Cek Napas`, `Stop-Mute` | Bagian fitur yang dihapus atau riset lanjutan, serta entri HISTORY lama |
| `Model #2`, `CV fisik`, `carcass` | Hanya catatan penghapusan |
| `bangkai` | Hanya konteks pekerjaan harian ABK, bukan fitur AI |
| `hari ke-5` dengan 23 | Hanya konteks Octopus XO |
| `Hari Farm` | Hanya di TOP5 dan RCA dengan label petelur, serta entri HISTORY lama |
| `44,1 kHz`, `ROI 498` | Tidak boleh ada |
| `sewa per siklus`, `Rover-as-a-Service`, `sewa antarfarm` | Tidak boleh ada sebagai skema sewa yang berpindah antarpeternakan. Langganan rover per kandang dengan protokol pemindahan unit boleh. |
| `All-In`, `tanpa langganan bulanan` | Tidak boleh tersisa sebagai skema bisnis utama |
| `servo` | Tidak boleh dihapus dari BOM maupun panduan |
| `YOLOv8`, `YOLO11`, `Ultralytics` | Hanya sebagai pembanding lisensi |
| `node` sebagai komponen BROVER | Tidak boleh ada |

2. `sync_readme.py` melaporkan 0 tautan rusak.
3. Semua rujukan gambar di markdown mengarah ke berkas yang ada.
4. Grep teks SVG kosong dari pola lama, dan setiap PNG yang dibuat ulang sudah dilihat langsung.
5. `pdfimages -list` menunjukkan 37 gambar di PDF TOP5 dan 5 gambar di PDF RCA.
6. Evaluasi ulang: tautan diuji dua kali, dan `check_style.py` menghasilkan TOTAL MASALAH 0.
7. `git status` hanya menunjukkan berkas dalam lingkup, dan tidak ada commit.
8. **Laporan akhir ke user**, berisi:
   - ringkasan perubahan per berkas;
   - ringkasan evaluasi ulang;
   - hal yang masih butuh keputusan user, yaitu nama paket, isi paket tanpa rover, jalur inferensi paket tanpa rover, harga final, berkas `*_tmp.html`, dan PDF SmartEars.
