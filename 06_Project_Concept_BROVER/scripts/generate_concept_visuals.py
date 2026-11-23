import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BASE_DIR = "/home/reiziqzip/Programmer/Hackathon-UNJ/06_Project_Concept_BROVER"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#CBD5E1"
plt.rcParams["axes.linewidth"] = 0.8

NAVY = "#0F172A"
SLATE = "#334155"
MUTED = "#64748B"
TEAL = "#0D9488"
BLUE = "#2563EB"
AMBER = "#D97706"
CRIMSON = "#DC2626"
EMERALD = "#059669"
PURPLE = "#7C3AED"


def add_box(ax, x, y, w, h, title, body, fc="#FFFFFF", ec="#2563EB", title_color="#0F172A", lw=1.6, title_size=9.5, body_size=7.8, title_pad=0.022, body_pad=0.060):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.010,rounding_size=0.016",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h - title_pad, title, ha="center", va="top",
            fontsize=title_size, fontweight="bold", color=title_color, zorder=4)
    if body:
        ax.text(x + w / 2, y + h - body_pad, body, ha="center", va="top",
                fontsize=body_size, color=SLATE, linespacing=1.35, zorder=4)


def add_arrow(ax, x1, y1, x2, y2, label="", color="#475569", rad=0.0, lw=1.7, lx=None, ly=None):
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2),
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>,head_length=6.5,head_width=4",
        color=color, linewidth=lw, zorder=5
    )
    ax.add_patch(arr)
    if label:
        tx = lx if lx is not None else (x1 + x2) / 2
        ty = ly if ly is not None else (y1 + y2) / 2
        ax.text(tx, ty, label, ha="center", va="center", fontsize=7.2,
                fontweight="bold", color=color,
                bbox=dict(boxstyle="round,pad=0.18", fc="#FFFFFF", ec="none", alpha=0.95), zorder=6)


# ==============================================================================
# FIGURE 3: Arsitektur Sistem BROVER (Multi-Modal AI & Edge-Cloud, Tim Asprak)
# ==============================================================================
def make_fig3_architecture():
    fig, ax = plt.subplots(figsize=(14.5, 8.3), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.968, "ARSITEKTUR SISTEM BROVER (MULTI-MODAL AI & EDGE-CLOUD OFFLINE-FIRST)",
            ha="center", va="top", fontsize=13.5, fontweight="bold", color=NAVY)
    ax.text(0.5, 0.932, "Broiler Inspection & Health Rover — Real-Time MCU (ESP32) + Edge AI SBC + Backend Golang + Dashboard Standar Umur Cobb 500",
            ha="center", va="top", fontsize=9.2, color=MUTED)

    z1 = FancyBboxPatch((0.02, 0.10), 0.565, 0.79, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#F0FDFA", edgecolor=TEAL, linewidth=1.6, linestyle="--", zorder=1)
    z2 = FancyBboxPatch((0.615, 0.46), 0.365, 0.43, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#EFF6FF", edgecolor=BLUE, linewidth=1.6, linestyle="--", zorder=1)
    z3 = FancyBboxPatch((0.615, 0.10), 0.365, 0.32, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#FFFBEB", edgecolor=AMBER, linewidth=1.6, linestyle="--", zorder=1)
    ax.add_patch(z1)
    ax.add_patch(z2)
    ax.add_patch(z3)

    ax.text(0.302, 0.876, "ROVER INSPEKSI DI KANDANG (1 UNIT = 1 KANDANG | WI-FI LOKAL NIRKABEL)",
            ha="center", va="top", fontsize=8.8, fontweight="bold", color=TEAL, zorder=2)
    ax.text(0.798, 0.876, "SERVER PUSAT (CLOUD / VPS EFISIEN)",
            ha="center", va="top", fontsize=9.0, fontweight="bold", color=BLUE, zorder=2)
    ax.text(0.74, 0.408, "DASHBOARD & ESKALASI DOKTER HEWAN",
            ha="center", va="top", fontsize=8.8, fontweight="bold", color=AMBER, zorder=2)

    add_box(ax, 0.035, 0.65, 0.242, 0.188,
            "1. Optik & Audio (USB/I2S)",
            "• Kamera USB (PoC) / IMX291 (Final)\n• 1x Servo Tilt (45° Feses / 10° Ayam)\n• LED Putih 5000K CRI >90 (Detail)\n• Mic USB / INMP441 (Cek Napas 5s)",
            fc="#FFFFFF", ec=TEAL, title_color=TEAL, title_size=8.8, body_size=7.5)

    add_box(ax, 0.035, 0.40, 0.242, 0.215,
            "2. Sensor Lingkungan & Aman",
            "• Suhu & RH: SHT31 / FS304 Probe\n• Tren Gas NH3: DFRobot SEN0567\n• Anti-Tabrak: HC-SR04 / A02YYUW IP67\n• INA219 Monitor Tegangan & Arus\n• Pinout Encoder/IMU (Future Work)",
            fc="#FFFFFF", ec=TEAL, title_color=TEAL, title_size=8.8, body_size=7.5)

    add_box(ax, 0.035, 0.13, 0.242, 0.235,
            "3. Penggerak & Sistem Daya",
            "• PoC: Dual-Rail (PB 5V3A + 18650 2S)\n  TB6612FNG + Kit 4WD TT 65mm\n• Final: LiFePO4 12,8V 6Ah + BMS\n  Custom Carrier PCB + Conformal Coat\n  BTS7960 + 4x JGB37-520 + Off-Road",
            fc="#FFFFFF", ec=SLATE, title_color=NAVY, title_size=8.8, body_size=7.3)

    add_box(ax, 0.320, 0.525, 0.250, 0.313,
            "EDGE AI BRAIN (SBC Linux)",
            "PoC: Raspberry Pi 4 (NCNN ~2,3 FPS)\nFinal: Orange Pi 3B RK3566 (RKNN ~18 FPS)\n\n• Model #1: CV Feses (3-5 Frame Voting)\n• Model #2: CV Fisik / Ayam Lesu & Mati\n• Model #3: Audio 5 dtk (Normal / Ngorok\n  / Suara Bising Kandang)\n• WebRTC/MJPEG Wi-Fi Lokal (Nirkabel)\n• SQLite WAL Offline (>30 hr) | Py/Go",
            fc="#FFFFFF", ec=PURPLE, title_color=PURPLE, lw=2.0, title_size=8.8, body_size=7.3)

    add_box(ax, 0.320, 0.13, 0.250, 0.315,
            "REAL-TIME MCU (ESP32 C++)",
            "• Kendali Kecepatan Pelan <=0,1 m/s\n• Dead-Man's Switch 500 ms (Rem Aman)\n• Anti-Tabrak Otomatis & Stall Proteksi\n• Stop-Mute-Sample (Matikan Motor/Fan)\n• Kontrol Servo Tilt & LED 5000K\n• Akuisisi SHT31, SEN0567, A02YYUW\n• Buzzer & LED Alert Fisik (Saat Offline)\n• Low-Power Mode Saat PLN Blackout",
            fc="#FFFFFF", ec=EMERALD, title_color=EMERALD, lw=2.0, title_size=8.8, body_size=7.3)

    add_box(ax, 0.635, 0.665, 0.325, 0.178,
            "Backend API & Broker (GOLANG)",
            "• Fiber/Gin REST API + Paho MQTT Go\n• Hemat RAM (~15-30 MB / VPS Murah)\n• Mosquitto Broker + PostgreSQL (pgx)\n• MinIO/S3 Storage (Foto & Audio 5 dtk)",
            fc="#FFFFFF", ec=BLUE, title_color=BLUE, lw=1.9, title_size=8.8, body_size=7.5)

    add_box(ax, 0.635, 0.485, 0.325, 0.145,
            "Mesin Standar Umur & Cuaca",
            "• Evaluasi Matriks Suhu-RH Cobb 500 (Hari ke-N)\n• Open-Meteo API (Prakiraan 3-7 Hari + Cache)\n• Generator Laporan 1-Klik WA/PDF Dokter Hewan",
            fc="#FFFFFF", ec=BLUE, title_color=BLUE, title_size=8.8, body_size=7.4)

    add_box(ax, 0.635, 0.125, 0.325, 0.250,
            "Dashboard Next.js PWA (4 Panel)",
            "• Panel 1: Mikroklimat vs Standar Umur Cobb 500\n• Panel 2: Temuan AI + 3 Tombol Aksi Manusia\n  (Akan Dicek / Normal / Lapor Dokter Hewan)\n• Panel 3: Pengingat Fase Pakan & Target Bobot\n• Panel 4: Log ABK (Deplesi/FCR) + Laporan 1-Klik\n• Halaman Kendali Rover Wi-Fi Lokal & Log Roda",
            fc="#FFFFFF", ec=AMBER, title_color=AMBER, lw=1.9, title_size=8.8, body_size=7.3)

    add_arrow(ax, 0.277, 0.745, 0.320, 0.745, "USB/I2S", color=TEAL, lx=0.298, ly=0.775)
    add_arrow(ax, 0.277, 0.495, 0.320, 0.345, "I2C/ADC\nUART", color=EMERALD, lx=0.295, ly=0.445)
    add_arrow(ax, 0.320, 0.23, 0.277, 0.23, "PWM", color=SLATE, lx=0.298, ly=0.195)

    add_arrow(ax, 0.395, 0.525, 0.395, 0.445, "", color=NAVY, lw=1.8)
    add_arrow(ax, 0.415, 0.445, 0.415, 0.525, "", color=NAVY, lw=1.8)
    ax.text(0.492, 0.485, "UART Serial\n(Cmd + Watchdog)", ha="center", va="center",
            fontsize=7.2, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.18", fc="#FFFFFF", ec="#CBD5E1", lw=0.7), zorder=6)

    add_arrow(ax, 0.570, 0.745, 0.635, 0.745, "MQTT/HTTPS\n(Auto-Sync)", color=BLUE, lx=0.602, ly=0.792)
    add_arrow(ax, 0.798, 0.665, 0.798, 0.630, "", color=BLUE)
    add_arrow(ax, 0.905, 0.485, 0.905, 0.375, "REST API\n& Alert", color=AMBER, lx=0.905, ly=0.434)

    ax.text(0.5, 0.035,
            "[SINTESIS ARSITEKTUR REKAYASA TIM ASPRAK — DISUSUN OLEH AI AGENT | BERBASIS SPESIFIKASI DATASHEET & STANDAR COBB 500]",
            ha="center", va="center", fontsize=7.9, fontweight="bold", color=MUTED,
            bbox=dict(boxstyle="round,pad=0.35", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(pad=0.4)
    plt.savefig(os.path.join(ASSETS_DIR, "03_arsitektur_sistem_brover.png"), dpi=300)
    plt.close()


# ==============================================================================
# FIGURE 4: Pola Jalur Inspeksi & Alur Kerja 4-Tahap BROVER (Tim Asprak)
# ==============================================================================
def make_fig4_workflow():
    fig = plt.figure(figsize=(14.5, 8.3), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.35], wspace=0.06)

    ax1 = fig.add_subplot(gs[0])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 12)
    ax1.axis("off")

    ax1.text(5.0, 11.78, "A. Pola Jalur Inspeksi Rover di Kandang Broiler",
             ha="center", va="top", fontsize=11.3, fontweight="bold", color=NAVY)
    ax1.text(5.0, 11.28, "Saat ini: kendali web Wi-Fi lokal | Future Work: otomatis terjadwal & setup jalur",
             ha="center", va="top", fontsize=7.9, color=MUTED)

    barn = FancyBboxPatch((0.6, 1.2), 8.8, 9.6, boxstyle="round,pad=0.05,rounding_size=0.2",
                          facecolor="#FEFCE8", edgecolor="#854D0E", linewidth=2.2, zorder=1)
    ax1.add_patch(barn)
    ax1.text(5.0, 10.52, "RUANG PUTAR UJUNG KANDANG (3-4 meter | Cobb/Ross Standard)",
             ha="center", va="center", fontsize=7.5, fontweight="bold", color="#92400E",
             bbox=dict(boxstyle="round,pad=0.2", fc="#FEF3C7", ec="#F59E0B", lw=0.8), zorder=3)
    ax1.text(5.0, 1.55, "RUANG PUTAR & CLEANING DOCK (Zona Dalam — 1 Unit = 1 Kandang)",
             ha="center", va="center", fontsize=7.5, fontweight="bold", color="#0F766E",
             bbox=dict(boxstyle="round,pad=0.2", fc="#CCFBF1", ec=TEAL, lw=0.9), zorder=3)

    for x, lbl, col in [(1.7, "Nipple", "#2563EB"), (3.9, "Pan Feeder", "#EA580C"),
                        (6.1, "Nipple", "#2563EB"), (8.3, "Pan Feeder", "#EA580C")]:
        ax1.plot([x, x], [2.45, 9.20], color=col, linewidth=3.2, zorder=2)
        ax1.text(x, 9.35, lbl, ha="center", va="bottom", fontsize=7.2, fontweight="bold", color=col,
                 bbox=dict(boxstyle="round,pad=0.1", fc="#FEFCE8", ec="none", alpha=0.9), zorder=5)
        if lbl == "Pan Feeder":
            for py in np.linspace(2.9, 8.8, 7):
                circ = plt.Circle((x, py), 0.21, fc="#FDBA74", ec="#C2410C", lw=1.0, zorder=3)
                ax1.add_patch(circ)
        else:
            for py in np.linspace(2.7, 9.0, 11):
                ax1.plot(x, py, "o", markersize=3.4, color="#1D4ED8", zorder=3)

    path_x = [1.25, 2.80, 2.80, 5.0, 5.0, 7.20, 7.20, 8.85]
    path_y = [2.12, 2.12, 10.02, 10.02, 2.12, 2.12, 10.02, 10.02]
    ax1.plot(path_x, path_y, color=TEAL, linewidth=2.6, linestyle="--", zorder=4)

    add_arrow(ax1, 2.80, 3.6, 2.80, 4.9, "", color=TEAL, lw=2.2)
    add_arrow(ax1, 2.80, 7.0, 2.80, 8.3, "", color=TEAL, lw=2.2)
    add_arrow(ax1, 5.0, 8.1, 5.0, 6.7, "", color=TEAL, lw=2.2)
    add_arrow(ax1, 7.20, 3.8, 7.20, 5.1, "", color=TEAL, lw=2.2)

    zone_pts = [
        (2.80, 4.3, "left", 0.16, "Zona A1\nCek Napas 5s"),
        (2.80, 7.9, "left", 0.16, "Zona A2\nCek Napas 5s"),
        (5.00, 7.9, "left", 0.16, "Zona B2\nCek Napas 5s"),
        (5.00, 4.3, "left", 0.16, "Zona B1\nCek Napas 5s"),
        (7.20, 6.7, "right", -0.16, "Zona C1\nCek Napas 5s"),
    ]
    for sx, sy, ha_side, dx, zlbl in zone_pts:
        ax1.plot(sx, sy, "s", markersize=8.5, color=PURPLE, mec="#FFFFFF", mew=1.2, zorder=6)
        ax1.text(sx + dx, sy, zlbl, ha=ha_side, va="center", fontsize=6.4,
                 fontweight="bold", color=PURPLE,
                 bbox=dict(boxstyle="round,pad=0.14", fc="#F5F3FF", ec=PURPLE, lw=0.6, alpha=0.95), zorder=7)

    ax1.plot(5.0, 5.85, "X", markersize=11, color=CRIMSON, mec="#FFFFFF", mew=1.0, zorder=7)
    ax1.text(5.18, 5.85, "Temuan Feses\n(Stop 30cm ->\nAnalisis Detail)", ha="left", va="center",
             fontsize=6.4, fontweight="bold", color=CRIMSON,
             bbox=dict(boxstyle="round,pad=0.14", fc="#FEF2F2", ec=CRIMSON, lw=0.8), zorder=8)

    dock = FancyBboxPatch((0.8, 1.85), 0.95, 0.54, boxstyle="round,pad=0.04", fc="#0F766E", ec=NAVY, lw=1.2, zorder=6)
    ax1.add_patch(dock)
    ax1.text(1.275, 2.12, "DOCK", ha="center", va="center", fontsize=7.0, fontweight="bold", color="#FFFFFF", zorder=7)

    ax1.text(5.0, 0.68,
             "Batas Jujur: Kecepatan <=0,1 m/s | Dead-Man's Switch 500 ms | Fase lantai Hari ke-5 s.d. ~23\n"
             "(sebelum kepadatan 25-30 kg/m² minggu 4-5 membatasi ruang gerak lantai)",
             ha="center", va="center", fontsize=7.3, color=SLATE,
             bbox=dict(boxstyle="round,pad=0.3", fc="#F8FAFC", ec="#CBD5E1"))

    ax2 = fig.add_subplot(gs[1])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")

    ax2.text(0.5, 0.98, "B. Alur 4-Tahap Inspeksi Multi-Modal & Pelaporan Dokter Hewan",
             ha="center", va="top", fontsize=11.2, fontweight="bold", color=NAVY)
    ax2.text(0.5, 0.935, "Evaluasi berbasis standar umur Cobb 500 (tanpa skor 0-100) & bebas klaim diagnosis otomatis",
             ha="center", va="top", fontsize=8.0, color=MUTED)

    add_box(ax2, 0.05, 0.755, 0.90, 0.140,
            "TAHAP 1 — Setup Chick-In & Inspeksi Rover via Wi-Fi Lokal Nirkabel",
            "• Input Tanggal Chick-In (Strain Cobb 500/Ross 308) -> sistem hitung Umur Hari ke-N otomatis.\n"
            "• Rover menyusuri lorong (<=0,1 m/s, Tag Zona A/B/C/D): tekan 'Cek Napas 5 Detik' (Stop-Mute-\n"
            "  Sample) & 'Analisis Detail' (LED 5000K + 3-5 frame CV feses/fisik) tanpa melindas temuan.",
            fc="#F0FDFA", ec=TEAL, title_color=TEAL, title_size=8.8, body_size=7.4)

    add_box(ax2, 0.05, 0.545, 0.90, 0.155,
            "TAHAP 2 — Evaluasi Standar Umur Cobb 500 & Deteksi Multi-Modal AI",
            "• Mikroklimat (SHT31) dibanding otomatis ke Matriks Suhu-RH Umur Cobb 500 (Dingin/Ideal/Panas)\n"
            "  + THI (>79 waspada) + Indikator Tren NH3 (SEN0567) + Prakiraan Cuaca 3-7 hari (Open-Meteo).\n"
            "• Audio 5 dtk diklasifikasi: Pernapasan Normal / Indikasi Ngorok (CRD-IB-ND) / Suara Bising Kandang.\n"
            "• Dashboard tampilkan daftar temuan prioritas + pengingat fase pakan & target bobot Cobb 500.",
            fc="#FEF2F2", ec=CRIMSON, title_color=CRIMSON, title_size=8.8, body_size=7.3)

    add_box(ax2, 0.05, 0.330, 0.90, 0.160,
            "TAHAP 3 — Triase Human-in-the-Loop (3 Tombol) & Laporan 1-Klik Vet",
            "• Setiap temuan disertai 3 tombol keputusan ala aremyhens.fit: [1] Akan Saya Cek | [2] Terlihat\n"
            "  Normal (perbaiki data AI) | [3] Laporkan ke Dokter Hewan + Kamus Gejala (validasi Dr. drh. Atin).\n"
            "• Klik 'Laporkan' -> kirim paket WA/PDF lengkap: Umur Flok + Catatan Deplesi/FCR ABK + Foto\n"
            "  + Audio 5 dtk + Grafik Suhu/RH/NH3 ke Dokter Hewan / TSO / Medik Veteriner Dinas Peternakan.",
            fc="#FFFBEB", ec=AMBER, title_color=AMBER, title_size=8.8, body_size=7.3)

    add_box(ax2, 0.05, 0.115, 0.90, 0.160,
            "TAHAP 4 — SOP Sanitasi Roda Veteriner di Cleaning Dock (1 Unit = 1 Kandang)",
            "• Sesuai WOAH, BROVER adalah alat inspeksi (bukan alat biosekuriti); kontaminasi silang dicegah\n"
            "  lewat kebijakan 1 unit/kandang & tidak mengklaim roda steril pasca-inspeksi.\n"
            "• Karena ookista Eimeria kebal disinfektan biasa (PMC11416347): (1) Sikat mekanis sekam di ban\n"
            "  (PMC12414267) -> (2) Semprot disinfektan -> (3) Keringkan penuh -> Centang Log Digital.",
            fc="#EFF6FF", ec=BLUE, title_color=BLUE, title_size=8.8, body_size=7.3)

    add_arrow(ax2, 0.50, 0.755, 0.50, 0.700, "", color=NAVY, lw=1.8)
    add_arrow(ax2, 0.50, 0.545, 0.50, 0.490, "", color=NAVY, lw=1.8)
    add_arrow(ax2, 0.50, 0.330, 0.50, 0.275, "", color=NAVY, lw=1.8)

    fig.text(0.5, 0.025,
             "[SINTESIS ALUR OPERASIONAL TIM ASPRAK — DISUSUN OLEH AI AGENT | MERUJUK WOAH, COBB 500, OCTOPUS XO, HENOMALY & PMC11416347]",
             ha="center", va="center", fontsize=7.8, fontweight="bold", color=MUTED,
             bbox=dict(boxstyle="round,pad=0.32", fc="#F1F5F9", ec="#CBD5E1"))

    plt.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.07)
    plt.savefig(os.path.join(ASSETS_DIR, "04_alur_kerja_4lapis_biosekuriti.png"), dpi=300)
    plt.close()


# ==============================================================================
# FIGURE 5: Komparasi Hardware Komputasi & Keamanan Baterai (Zero overlaps!)
# ==============================================================================
def make_fig5_hardware_power():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.4, 6.6), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")

    boards = [
        "Raspberry Pi 4\n(PoC Eksisting\nNCNN CPU)",
        "Luckfox Pico Ultra\n(RV1106 0,5-1T\nRAM 256MB*)",
        "Orange Pi 3B\n(FINAL SWEET SPOT\nRK3566 0,8T 4GB)",
        "Orange Pi 5\n(RK3588S 6T\nOver-Spec)",
    ]
    fps_vals = [2.3, 8.5, 18.2, 53.1]
    watts = [6.8, 1.8, 4.0, 7.5]
    prices_usd = [55, 20, 35, 80]
    colors_a = ["#64748B", "#F59E0B", TEAL, "#3B82F6"]

    x = np.arange(len(boards))
    bars = ax1.bar(x, fps_vals, width=0.52, color=colors_a, edgecolor=NAVY, linewidth=0.8, zorder=3)
    ax1.axhline(5.0, color=CRIMSON, linestyle="--", linewidth=1.4, zorder=4)

    ax1.annotate("Batas Nyaman Rover <=0,1 m/s (~5 FPS)",
                 xy=(1.55, 5.0), xytext=(0.15, 34.0),
                 fontsize=8.0, fontweight="bold", color=CRIMSON,
                 bbox=dict(boxstyle="round,pad=0.3", fc="#FEF2F2", ec=CRIMSON, lw=0.9),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON, lw=1.3, connectionstyle="arc3,rad=0.18"),
                 zorder=6)

    for b, f, w, p in zip(bars, fps_vals, watts, prices_usd):
        y_txt = max(f + 1.6, 6.4)
        ax1.text(b.get_x() + b.get_width() / 2, y_txt,
                 f"{f:.1f} FPS\n({w:.1f}W | ~${p})",
                 ha="center", va="bottom", fontsize=7.9, fontweight="bold", color=NAVY, zorder=7)

    ax1.set_xticks(x)
    ax1.set_xticklabels(boards, fontsize=8.0, fontweight="bold", color=SLATE)
    ax1.set_ylabel("Performa Inferensi YOLOv8n 640x640 (FPS)", fontsize=9.2, fontweight="bold", color=NAVY)
    ax1.set_ylim(0, 66)
    ax1.grid(axis="y", linestyle=":", alpha=0.6, zorder=0)
    ax1.set_title("A. Performa YOLOv8n vs Daya & Harga Global SBC",
                  fontsize=10.8, fontweight="bold", color=NAVY, pad=10)
    ax1.text(0.5, -0.23, "*Luckfox 256MB RAM berisiko OOM untuk 3 model + audio + SQLite offline.",
             transform=ax1.transAxes, ha="center", fontsize=7.4, style="italic", color=MUTED)

    cats = [
        "Ambang Thermal Runaway (°C)\n[Lebih Tinggi = Aman di Sekam]",
        "Umur Pakai Baterai\n(Jumlah Siklus / 100)",
        "Estimasi Durasi Operasi\n(Menit / Cas — PoC vs Final 6Ah)",
    ]
    y = np.arange(len(cats))
    h = 0.34
    b1 = ax2.barh(y + h / 2, [195, 15, 120], height=h, label="Fase PoC: Li-Ion NMC 18650 + PB", color="#94A3B8", edgecolor=NAVY, lw=0.8, zorder=3)
    b2 = ax2.barh(y - h / 2, [260, 45, 210], height=h, label="Fase Final: LiFePO4 4S 12,8V 6Ah", color=EMERALD, edgecolor=NAVY, lw=0.8, zorder=3)

    lbls_nmc = ["180-210°C (Rentan api)", "1.000-2.000 siklus", "~90-150 mnt (~2 jam)"]
    lbls_lfp = ["250-270°C (Aman sekam)", "3.000-6.000+ siklus", "~180-240 mnt (3-4 jam)"]
    for bar, txt in zip(b1, lbls_nmc):
        ax2.text(bar.get_width() + 7, bar.get_y() + bar.get_height() / 2, txt,
                 va="center", ha="left", fontsize=7.7, color=SLATE, fontweight="bold")
    for bar, txt in zip(b2, lbls_lfp):
        ax2.text(bar.get_width() + 7, bar.get_y() + bar.get_height() / 2, txt,
                 va="center", ha="left", fontsize=7.7, color="#065F46", fontweight="bold")

    ax2.set_yticks(y)
    ax2.set_yticklabels(cats, fontsize=8.0, fontweight="bold", color=SLATE)
    ax2.set_xlim(0, 440)
    ax2.set_xlabel("Nilai Skala Pembanding (Lihat Label Satuan Masing-Masing Baris)", fontsize=8.3, fontweight="bold", color=NAVY)
    ax2.grid(axis="x", linestyle=":", alpha=0.6, zorder=0)
    ax2.legend(loc="center right", bbox_to_anchor=(0.98, 0.50), frameon=True,
               facecolor="#FFFFFF", edgecolor="#CBD5E1", fontsize=8.0)
    ax2.set_title("B. Keamanan Termal & Kapasitas Daya (Li-Ion NMC vs LiFePO4)",
                  fontsize=10.8, fontweight="bold", color=NAVY, pad=10)

    fig.suptitle("ANALISIS EFISIENSI KOMPUTASI & KEAMANAN ENERGI BROVER (ANTI-OVER-SPEC)",
                 fontsize=13, fontweight="bold", color=NAVY, y=0.975)
    fig.text(0.5, 0.018,
             "[DATA DATASHEET & BENCHMARK TERVERIFIKASI — TIM ASPRAK | ULTRALYTICS DOCS, ORANGE PI, LUCKFOX & LITERATUR LFP]",
             ha="center", va="center", fontsize=7.7, fontweight="bold", color=MUTED,
             bbox=dict(boxstyle="round,pad=0.3", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(rect=[0.01, 0.06, 0.99, 0.93])
    plt.savefig(os.path.join(ASSETS_DIR, "05_komparasi_komputasi_dan_baterai_brover.png"), dpi=300)
    plt.close()


# ==============================================================================
# FIGURE 6: Roadmap TKT 3->9 & Evolusi BROVER + Future Work (Tim Asprak)
# ==============================================================================
def make_fig6_roadmap():
    fig, ax = plt.subplots(figsize=(14.4, 5.9), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.96, "ROADMAP PENINGKATAN TKT & EVOLUSI BROVER (TIM ASPRAK | 2026 - 2027+)",
            ha="center", va="top", fontsize=13.2, fontweight="bold", color=NAVY)
    ax.text(0.5, 0.905, "Dari PoC Kendali Wi-Fi Lokal (TKT 3-4) -> Field-Ready (TKT 5-7) -> Future Work Otomatisasi Jadwal & Jalur (TKT 8-9)",
            ha="center", va="top", fontsize=8.8, color=MUTED)

    ax.plot([0.10, 0.90], [0.74, 0.74], color="#CBD5E1", linewidth=5.0, zorder=1)
    ax.plot([0.10, 0.90], [0.74, 0.74], color=TEAL, linewidth=2.5, zorder=2)

    stages = [
        (0.13, "TAHAP 1\nNov 2026", "TKT 3 - 4", "Seleksi & PoC Awal",
         "• Kit 4WD + RPi 4 + ESP32\n• Kendali Wi-Fi Lokal Nirkabel\n  + Dead-Man's Switch 500 ms\n• Webcam + Servo + Mic 5 dtk\n• SHT31 + SEN0567 NH3\n• Model Awal (NCNN)\n• Dashboard Standar Cobb 500\n• Uji Simulasi Meja / Lab",
         "#64748B", "#F8FAFC"),
        (0.377, "TAHAP 2\nDes 2026 - Feb 2027", "TKT 5 - 6", "Bootcamp & Field Prototype",
         "• Orange Pi 3B + eMMC\n• Custom Carrier PCB\n  + Conformal Coating\n• LiFePO4 12,8V 6Ah\n• JGB37-520 + Off-Road\n• Casing Tertutup IP54+\n• Fine-Tuning Data Lokal\n  (Validasi Dr. drh. Atin)",
         TEAL, "#F0FDFA"),
        (0.623, "TAHAP 3\nMar - Apr 2027", "TKT 6 - 7", "Demo Day & Business Match",
         "• Uji Lapangan Kandang\n  Mitra (PT Zara / Bogor)\n• Validasi CV, Audio 5 dtk,\n  Cobb 500 & Laporan Vet\n• Validasi SOP Sanitasi Roda\n• Penyempurnaan BMC\n• Demo Day & Inisiasi LoI\n  dengan Mitra Industri",
         BLUE, "#EFF6FF"),
        (0.87, "TAHAP 4\nMei - Agu 2027+", "TKT 7 - 9", "Pilot, HKI & Future Work",
         "• Pilot 1-2 Siklus (Hr 5-23)\n• HKI / Paten (Apache-2.0)\n• Varian Rakyat vs Pro\n• FUTURE WORK UTAMA:\n  Otomatisasi Jadwal Rutin\n  & Setup Jalur Otomatis\n• Ekspansi: Modul Rel Plafon",
         PURPLE, "#F5F3FF"),
    ]

    for cx, period, tkt, title, body, col, bg in stages:
        ax.scatter([cx], [0.74], s=320, color=col, edgecolors="#FFFFFF", linewidths=2.5, zorder=4)
        ax.text(cx, 0.83, period, ha="center", va="center", fontsize=8.4, fontweight="bold", color=NAVY)
        ax.text(cx, 0.655, tkt, ha="center", va="center", fontsize=8.3, fontweight="bold", color="#FFFFFF",
                bbox=dict(boxstyle="round,pad=0.25", fc=col, ec="none"), zorder=5)
        add_box(ax, cx - 0.106, 0.135, 0.212, 0.455, title, body,
                fc=bg, ec=col, title_color=col, lw=1.7, title_size=8.8, body_size=7.6,
                title_pad=0.024, body_pad=0.070)

    for x_mid in [0.2535, 0.500, 0.7465]:
        add_arrow(ax, x_mid - 0.012, 0.365, x_mid + 0.012, 0.365, "", color=MUTED, lw=1.8)

    ax.text(0.5, 0.042,
            "[SINTESIS ROADMAP TIM ASPRAK (4 TI + DR. DRH. ATIN SUPIYANI, M.SI.) | BERDASARKAN BUKU PEDOMAN HACKATHON DEEP TECH UNJ 2026]",
            ha="center", va="center", fontsize=7.8, fontweight="bold", color=MUTED,
            bbox=dict(boxstyle="round,pad=0.32", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(pad=0.4)
    plt.savefig(os.path.join(ASSETS_DIR, "06_roadmap_tkt_dan_evolusi_brover.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    make_fig3_architecture()
    make_fig4_workflow()
    make_fig5_hardware_power()
    make_fig6_roadmap()
    print("REGENERATED ALL 4 VISUALS FOR TIM ASPRAK SUCCESSFULLY")
