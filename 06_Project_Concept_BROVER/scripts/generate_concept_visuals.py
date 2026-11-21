import os
import shutil
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
        ax.text(tx, ty, label, ha="center", va="center", fontsize=7.3,
                fontweight="bold", color=color,
                bbox=dict(boxstyle="round,pad=0.18", fc="#FFFFFF", ec="none", alpha=0.95), zorder=6)


# ==============================================================================
# FIGURE 3: Arsitektur Sistem Hybrid Edge-Cloud BROVER (Fixed spacing & labels)
# ==============================================================================
def make_fig3_architecture():
    fig, ax = plt.subplots(figsize=(14.5, 8.2), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.968, "ARSITEKTUR SISTEM BROVER (HYBRID EDGE-CLOUD & OFFLINE-FIRST)",
            ha="center", va="top", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(0.5, 0.932, "Integrasi Real-Time MCU (ESP32) + Edge AI SBC (RPi 4 PoC / Orange Pi 3B Final) + Backend Golang + PWA Peternak",
            ha="center", va="top", fontsize=9.5, color=MUTED)

    z1 = FancyBboxPatch((0.02, 0.10), 0.565, 0.79, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#F0FDFA", edgecolor=TEAL, linewidth=1.6, linestyle="--", zorder=1)
    z2 = FancyBboxPatch((0.615, 0.45), 0.365, 0.44, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#EFF6FF", edgecolor=BLUE, linewidth=1.6, linestyle="--", zorder=1)
    z3 = FancyBboxPatch((0.615, 0.10), 0.365, 0.31, boxstyle="round,pad=0.008,rounding_size=0.02",
                        facecolor="#FFFBEB", edgecolor=AMBER, linewidth=1.6, linestyle="--", zorder=1)
    ax.add_patch(z1)
    ax.add_patch(z2)
    ax.add_patch(z3)

    ax.text(0.302, 0.876, "UNIT ROVER DI KANDANG (1 UNIT = 1 KANDANG | OFFLINE-FIRST)",
            ha="center", va="top", fontsize=9.2, fontweight="bold", color=TEAL, zorder=2)
    ax.text(0.798, 0.876, "SERVER PUSAT (CLOUD / VPS EFISIEN)",
            ha="center", va="top", fontsize=9.2, fontweight="bold", color=BLUE, zorder=2)
    ax.text(0.74, 0.398, "ANTARMUKA PENGGUNA & ESKALASI",
            ha="center", va="top", fontsize=9.0, fontweight="bold", color=AMBER, zorder=2)

    add_box(ax, 0.035, 0.65, 0.242, 0.188,
            "1. Optik & Audio (USB/I2S)",
            "• Kamera USB (PoC) / IMX291 (Final)\n• 1x Servo Tilt (45° Feses / 10° Ayam)\n• LED Putih 5000K CRI >90 (Pause)\n• Mic USB / INMP441 (Stop-Mute-Sample)",
            fc="#FFFFFF", ec=TEAL, title_color=TEAL, title_size=9.0, body_size=7.6)

    add_box(ax, 0.035, 0.40, 0.242, 0.215,
            "2. Sensor Lingkungan & Navigasi",
            "• Suhu & RH: SHT31 / FS304 Probe\n• Tren Gas NH3: DFRobot SEN0567\n• Anti-Tabrak: HC-SR04 / A02YYUW IP67\n• Hall Encoder Roda + IMU MPU6050\n• INA219 Monitor Tegangan & Arus",
            fc="#FFFFFF", ec=TEAL, title_color=TEAL, title_size=9.0, body_size=7.6)

    add_box(ax, 0.035, 0.13, 0.242, 0.235,
            "3. Penggerak & Sistem Daya",
            "• PoC: Dual-Rail (PB 5V3A + 18650 2S)\n  TB6612FNG + Kit 4WD TT 65mm\n• Final: LiFePO4 12,8V 6Ah + BMS\n  Custom Carrier PCB + Conformal Coat\n  BTS7960 + 4x JGB37-520 + Off-Road",
            fc="#FFFFFF", ec=SLATE, title_color=NAVY, title_size=9.0, body_size=7.4)

    add_box(ax, 0.320, 0.525, 0.250, 0.313,
            "EDGE AI BRAIN (SBC Linux)",
            "PoC: Raspberry Pi 4 (NCNN ~2,3 FPS)\nFinal: Orange Pi 3B RK3566 (RKNN ~18 FPS)\n\n• Model #1: CV Feses (3-5 Frame Voting)\n• Model #2: CV Ayam Lesu / Mati\n• Model #3: Audio Respirasi (5 dtk)\n• Zone Risk Fusion (Hijau/Kuning/Merah)\n• SQLite WAL Ring-Buffer (Offline >30 hr)\n• Edge Daemon: Python (PoC) / Go (Final)",
            fc="#FFFFFF", ec=PURPLE, title_color=PURPLE, lw=2.0, title_size=9.0, body_size=7.5)

    add_box(ax, 0.320, 0.13, 0.250, 0.315,
            "REAL-TIME MCU (ESP32 C++)",
            "• Kendali Kecepatan Pelan <=0,1 m/s\n• Hardware Watchdog (Cutoff >1 dtk hang)\n• Stall Protection (Encoder + Arus)\n• Eksekusi Soft Pause, Mundur & Hindar\n• Kontrol Servo Tilt & LED 5000K\n• Akuisisi SHT31, SEN0567, A02YYUW\n• Buzzer & LED Alert Fisik (Saat Offline)\n• Low-Power Mode Saat PLN Blackout",
            fc="#FFFFFF", ec=EMERALD, title_color=EMERALD, lw=2.0, title_size=9.0, body_size=7.5)

    add_box(ax, 0.635, 0.655, 0.325, 0.185,
            "Backend API & Broker (GOLANG)",
            "• Fiber/Gin REST API + Paho MQTT Go\n• Super Hemat RAM (~15-30 MB / VPS Murah)\n• Mosquitto Broker + PostgreSQL (pgx)\n• MinIO/S3 Storage (Foto Bukti & Audio 5 dtk)",
            fc="#FFFFFF", ec=BLUE, title_color=BLUE, lw=1.9, title_size=9.0, body_size=7.6)

    add_box(ax, 0.635, 0.475, 0.325, 0.145,
            "Integrasi Cuaca & Alert Engine",
            "• Open-Meteo API (Prakiraan 3-7 Hari + Cache)\n• Rekomendasi Preventif Heat Stress & NH3\n• Bot Notifikasi WhatsApp / Telegram",
            fc="#FFFFFF", ec=BLUE, title_color=BLUE, title_size=9.0, body_size=7.6)

    add_box(ax, 0.635, 0.125, 0.325, 0.240,
            "Next.js PWA (HP Android & Web)",
            "• Peta Zona Kandang (Hijau / Kuning / Merah)\n• Galeri Foto + Audio + Konfirmasi Benar/Bukan\n• Grafik Suhu, RH, THI & Tren NH3 + Cuaca\n• Disease Triage Dictionary (Kementan/Medion)\n• Ekspor 1-Klik Bukti ke WA TSO / Dokter Hewan\n• Checklist Digital SOP Sanitasi Roda & Kandang",
            fc="#FFFFFF", ec=AMBER, title_color=AMBER, lw=1.9, title_size=9.0, body_size=7.5)

    add_arrow(ax, 0.277, 0.745, 0.320, 0.745, "USB/I2S", color=TEAL, lx=0.298, ly=0.775)
    add_arrow(ax, 0.277, 0.495, 0.320, 0.345, "I2C/ADC\nUART", color=EMERALD, lx=0.295, ly=0.445)
    add_arrow(ax, 0.320, 0.23, 0.277, 0.23, "PWM", color=SLATE, lx=0.298, ly=0.195)

    # Bidirectional UART Serial clearly separated from text
    add_arrow(ax, 0.395, 0.525, 0.395, 0.445, "", color=NAVY, lw=1.8)
    add_arrow(ax, 0.415, 0.445, 0.415, 0.525, "", color=NAVY, lw=1.8)
    ax.text(0.492, 0.485, "UART Serial\n(Cmd + Heartbeat)", ha="center", va="center",
            fontsize=7.3, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.18", fc="#FFFFFF", ec="#CBD5E1", lw=0.7), zorder=6)

    add_arrow(ax, 0.570, 0.745, 0.635, 0.745, "MQTT/HTTPS\n(Auto-Sync)", color=BLUE, lx=0.602, ly=0.790)
    add_arrow(ax, 0.798, 0.655, 0.798, 0.620, "", color=BLUE)
    # Arrow from Integrasi Cuaca down to PWA positioned cleanly on right side away from zone header
    add_arrow(ax, 0.905, 0.475, 0.905, 0.365, "Push Alert\n& REST API", color=AMBER, lx=0.905, ly=0.425)

    ax.text(0.5, 0.035,
            "[SINTESIS ARSITEKTUR REKAYASA TIM MBOYZ — DISUSUN OLEH AI AGENT | BERBASIS SPESIFIKASI DATASHEET TERVERIFIKASI]",
            ha="center", va="center", fontsize=8.0, fontweight="bold", color=MUTED,
            bbox=dict(boxstyle="round,pad=0.35", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(pad=0.4)
    plt.savefig(os.path.join(ASSETS_DIR, "03_arsitektur_sistem_brover.png"), dpi=300)
    plt.close()


# ==============================================================================
# FIGURE 4: Alur Kerja 4-Lapis Biosekuriti + Pola Navigasi (Zero overlaps)
# ==============================================================================
def make_fig4_workflow():
    fig = plt.figure(figsize=(14.5, 8.2), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.35], wspace=0.06)

    ax1 = fig.add_subplot(gs[0])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 12)
    ax1.axis("off")

    ax1.text(5.0, 11.75, "A. Pola Navigasi Huruf U di Kandang Broiler",
             ha="center", va="top", fontsize=11.5, fontweight="bold", color=NAVY)
    ax1.text(5.0, 11.25, "Menyusuri celah antar-baris Pan Feeder & Nipple (putar di ujung 3-4 m)",
             ha="center", va="top", fontsize=8.2, color=MUTED)

    barn = FancyBboxPatch((0.6, 1.2), 8.8, 9.6, boxstyle="round,pad=0.05,rounding_size=0.2",
                          facecolor="#FEFCE8", edgecolor="#854D0E", linewidth=2.2, zorder=1)
    ax1.add_patch(barn)
    ax1.text(5.0, 10.52, "RUANG PUTAR UJUNG KANDANG (3-4 meter | Cobb/Ross Standard)",
             ha="center", va="center", fontsize=7.6, fontweight="bold", color="#92400E",
             bbox=dict(boxstyle="round,pad=0.2", fc="#FEF3C7", ec="#F59E0B", lw=0.8), zorder=3)
    ax1.text(5.0, 1.55, "RUANG PUTAR & CLEANING DOCK (Zona Dalam — 1 Unit = 1 Kandang)",
             ha="center", va="center", fontsize=7.6, fontweight="bold", color="#0F766E",
             bbox=dict(boxstyle="round,pad=0.2", fc="#CCFBF1", ec=TEAL, lw=0.9), zorder=3)

    # Pipes stop at y=9.25 so label sits cleanly at y=9.45 BELOW turning path y=10.05
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

    # Scheduled audio zone stops cleanly placed without colliding with feeders
    zone_pts = [
        (2.80, 4.3, "left", 0.16, "Zona A1\nAudio 5s"),
        (2.80, 7.7, "left", 0.16, "Zona A2\nAudio 5s"),
        (5.00, 7.7, "left", 0.16, "Zona B2\nAudio 5s"),
        (5.00, 4.3, "left", 0.16, "Zona B1\nAudio 5s"),
        (7.20, 7.7, "right", -0.16, "Zona C1\nAudio 5s"),
    ]
    for sx, sy, ha_side, dx, zlbl in zone_pts:
        ax1.plot(sx, sy, "s", markersize=8.5, color=PURPLE, mec="#FFFFFF", mew=1.2, zorder=6)
        ax1.text(sx + dx, sy, zlbl, ha=ha_side, va="center", fontsize=6.6,
                 fontweight="bold", color=PURPLE,
                 bbox=dict(boxstyle="round,pad=0.14", fc="#F5F3FF", ec=PURPLE, lw=0.6, alpha=0.95), zorder=7)

    ax1.plot(5.0, 5.85, "X", markersize=11, color=CRIMSON, mec="#FFFFFF", mew=1.0, zorder=7)
    ax1.text(5.18, 5.85, "Feses Abnormal\n(Stop 30cm ->\nMundur & Alert)", ha="left", va="center",
             fontsize=6.5, fontweight="bold", color=CRIMSON,
             bbox=dict(boxstyle="round,pad=0.14", fc="#FEF2F2", ec=CRIMSON, lw=0.8), zorder=8)

    dock = FancyBboxPatch((0.8, 1.85), 0.95, 0.54, boxstyle="round,pad=0.04", fc="#0F766E", ec=NAVY, lw=1.2, zorder=6)
    ax1.add_patch(dock)
    ax1.text(1.275, 2.12, "DOCK", ha="center", va="center", fontsize=7.0, fontweight="bold", color="#FFFFFF", zorder=7)

    ax1.text(5.0, 0.68,
             "Batas Operasional Jujur: Kecepatan <=0,1 m/s | Fase lantai optimal Hari ke-5 s.d. ~23\n"
             "(sebelum kepadatan 25-30 kg/m² minggu 4-5 memblokir ruang gerak lantai)",
             ha="center", va="center", fontsize=7.5, color=SLATE,
             bbox=dict(boxstyle="round,pad=0.3", fc="#F8FAFC", ec="#CBD5E1"))

    ax2 = fig.add_subplot(gs[1])
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis("off")

    ax2.text(0.5, 0.98, "B. Alur 4-Lapis Biosekuriti & Zone-Scheduled Multi-Modal Triage",
             ha="center", va="top", fontsize=11.5, fontweight="bold", color=NAVY)
    ax2.text(0.5, 0.935, "Mencegah false alarm, tidak melindas feses klinis segar, & bebas klaim diagnosis otomatis",
             ha="center", va="top", fontsize=8.2, color=MUTED)

    add_box(ax2, 0.05, 0.755, 0.90, 0.140,
            "LAPIS 1 — Inspeksi Terjadwal & Verifikasi 2-Tahap",
            "• Saat jalan (<=0,1 m/s): CV feses aktif ringan (3-5 FPS); Audio MATI (hindari bising motor)\n"
            "• Tiap 5-10 m (Zone-Scheduled) ATAU kandidat feses 30-50 cm -> SOFT PAUSE 5 detik (motor mati)\n"
            "• Rekam Audio 5 dtk (CRD/IB/ND) + LED 5000K + Voting 3-5 frame CV + SHT31 (THI) & SEN0567 (NH3)",
            fc="#F0FDFA", ec=TEAL, title_color=TEAL, title_size=9.0, body_size=7.6)

    add_box(ax2, 0.05, 0.545, 0.90, 0.155,
            "LAPIS 2 — Multi-Modal Zone Risk Fusion & Respon Berjenjang",
            "• HIJAU (0-39): Normal -> log rutin -> lanjut inspeksi.\n"
            "• KUNING (40-69): 1 anomali conf. 60-79% -> simpan foto & koordinat (Passive Log) -> hindari & lanjut.\n"
            "• MERAH (70-100): Conf. >=80% / feses berdarah / klaster >=3 titik / Audio ngorok positif ->\n"
            "  JANGAN melindas -> mundur aman 20-30 cm -> kirim Push Alert + Foto + Audio + Peta Zona!",
            fc="#FEF2F2", ec=CRIMSON, title_color=CRIMSON, title_size=9.0, body_size=7.5)

    add_box(ax2, 0.05, 0.330, 0.90, 0.160,
            "LAPIS 3 — Human-in-the-Loop Triage & Disease Dictionary",
            "• Peternak cek foto & klip audio di PWA -> langsung menuju radius 2-3 m sesuai koordinat zona.\n"
            "• Cek ayam lesu/menyendiri berpanduan Disease Triage Dictionary (Manual Penyakit Unggas Kementan RI\n"
            "  & Medion) lengkap dengan peringatan kemiripan gejala (mis. AI vs Snot) -> isolasi awal non-obat.\n"
            "• Tombol Ekspor 1-Klik bukti lengkap (foto + audio + grafik THI/NH3) ke WhatsApp TSO / Dokter Hewan.",
            fc="#FFFBEB", ec=AMBER, title_color=AMBER, title_size=9.0, body_size=7.5)

    add_box(ax2, 0.05, 0.115, 0.90, 0.160,
            "LAPIS 4 — Protokol Sanitasi Roda Berbasis Sains Veteriner (Di Cleaning Dock)",
            "• Prinsip 1 Unit = 1 Kandang (mengakui risiko subclinical shedding; tidak klaim roda 100% steril).\n"
            "• Karena ookista Eimeria KEBAL disinfektan biasa (PMC11416347), SOP wajib 3 langkah:\n"
            "  (1) Sikat fisik/mekanis buang sekam di ban (PMC12414267) -> (2) Semprot disinfektan spektrum luas\n"
            "  -> (3) Keringkan penuh -> Centang Log Kepatuhan Biosekuriti di Aplikasi.",
            fc="#EFF6FF", ec=BLUE, title_color=BLUE, title_size=9.0, body_size=7.5)

    add_arrow(ax2, 0.50, 0.755, 0.50, 0.700, "", color=NAVY, lw=1.8)
    add_arrow(ax2, 0.50, 0.545, 0.50, 0.490, "", color=NAVY, lw=1.8)
    add_arrow(ax2, 0.50, 0.330, 0.50, 0.275, "", color=NAVY, lw=1.8)

    fig.text(0.5, 0.025,
             "[SINTESIS ALUR OPERASIONAL TIM MBOYZ — DISUSUN OLEH AI AGENT | MERUJUK COBB/ROSS, OCTOPUS XO, HENOMALY, PMC11416347 & PMC12414267]",
             ha="center", va="center", fontsize=7.9, fontweight="bold", color=MUTED,
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

    # Clean annotation box for threshold line well above bars on left-center
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
    # Place legend cleanly in wide open middle-right area (around y=1, x=210..430)
    ax2.legend(loc="center right", bbox_to_anchor=(0.98, 0.50), frameon=True,
               facecolor="#FFFFFF", edgecolor="#CBD5E1", fontsize=8.0)
    ax2.set_title("B. Keamanan Termal & Kapasitas Daya (Li-Ion NMC vs LiFePO4)",
                  fontsize=10.8, fontweight="bold", color=NAVY, pad=10)

    fig.suptitle("ANALISIS EFISIENSI KOMPUTASI & KEAMANAN ENERGI BROVER (ANTI-OVER-SPEC)",
                 fontsize=13, fontweight="bold", color=NAVY, y=0.975)
    fig.text(0.5, 0.018,
             "[DATA DATASHEET & BENCHMARK TERVERIFIKASI — VISUALISASI DISUSUN OLEH AI AGENT | ULTRALYTICS DOCS, ORANGE PI, LUCKFOX & LITERATUR LFP]",
             ha="center", va="center", fontsize=7.7, fontweight="bold", color=MUTED,
             bbox=dict(boxstyle="round,pad=0.3", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(rect=[0.01, 0.06, 0.99, 0.93])
    plt.savefig(os.path.join(ASSETS_DIR, "05_komparasi_komputasi_dan_baterai_brover.png"), dpi=300)
    plt.close()


# ==============================================================================
# FIGURE 6: Roadmap TKT 3->9 & Evolusi 2-Fase BROVER (Tighter, bolder cards)
# ==============================================================================
def make_fig6_roadmap():
    fig, ax = plt.subplots(figsize=(14.4, 5.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.96, "ROADMAP PENINGKATAN TKT & EVOLUSI 2-FASE BROVER (2026 - 2027)",
            ha="center", va="top", fontsize=13.5, fontweight="bold", color=NAVY)
    ax.text(0.5, 0.905, "Diselaraskan dengan Jadwal Resmi Hackathon Deep Tech UNJ 2026 (Jalur D-FARM) & Strategi Hilirisasi Mitra",
            ha="center", va="top", fontsize=9.0, color=MUTED)

    ax.plot([0.10, 0.90], [0.74, 0.74], color="#CBD5E1", linewidth=5.0, zorder=1)
    ax.plot([0.10, 0.90], [0.74, 0.74], color=TEAL, linewidth=2.5, zorder=2)

    stages = [
        (0.13, "TAHAP 1\nNov 2026", "TKT 3 - 4", "Seleksi & PoC Awal",
         "• Kit 4WD Akrilik + RPi 4\n• ESP32 + TB6612FNG\n• Webcam + Servo + Mic\n• SHT31 + SEN0567 NH3\n• Dual-Rail PB + 18650\n• Model Awal (NCNN)\n• Backend Go + PWA\n• Uji Simulasi Meja/Lab",
         "#64748B", "#F8FAFC"),
        (0.377, "TAHAP 2\nDes 2026 - Feb 2027", "TKT 5 - 6", "Bootcamp & Field Prototype",
         "• Orange Pi 3B + eMMC\n• Custom Carrier PCB\n  + Conformal Coating\n• LiFePO4 12,8V 6Ah\n• JGB37-520 + Off-Road\n• Casing Tertutup IP54+\n• Fine-Tuning Data Lokal\n• Dukungan PT Edura/UNJ",
         TEAL, "#F0FDFA"),
        (0.623, "TAHAP 3\nMar - Apr 2027", "TKT 6 - 7", "Demo Day & Business Match",
         "• Uji Lapangan Kandang\n  Mitra (PT Zara / Bogor)\n• Validasi Akurasi CV,\n  Audio 5 dtk & THI/NH3\n• Validasi SOP Sanitasi\n• Penyempurnaan BMC\n• Demo Day & Inisiasi LoI\n  dengan Mitra Industri",
         BLUE, "#EFF6FF"),
        (0.87, "TAHAP 4\nMei - Agu 2027+", "TKT 7 - 9", "Pilot Testing, HKI & Komersial",
         "• Pilot 1-2 Siklus Penuh\n  (Hari ke-5 s.d. ~23)\n• Pendaftaran HKI / Paten\n  (Migrasi Apache-2.0)\n• Varian Rakyat vs Pro\n• Ekspansi Masa Depan:\n  Modul Rel/Kabel Layer\n• Siap Komersialisasi",
         PURPLE, "#F5F3FF"),
    ]

    for cx, period, tkt, title, body, col, bg in stages:
        ax.scatter([cx], [0.74], s=320, color=col, edgecolors="#FFFFFF", linewidths=2.5, zorder=4)
        ax.text(cx, 0.83, period, ha="center", va="center", fontsize=8.5, fontweight="bold", color=NAVY)
        ax.text(cx, 0.655, tkt, ha="center", va="center", fontsize=8.4, fontweight="bold", color="#FFFFFF",
                bbox=dict(boxstyle="round,pad=0.25", fc=col, ec="none"), zorder=5)
        add_box(ax, cx - 0.106, 0.145, 0.212, 0.445, title, body,
                fc=bg, ec=col, title_color=col, lw=1.7, title_size=8.9, body_size=7.9,
                title_pad=0.025, body_pad=0.072)

    # Arrows between stage cards
    for x_mid in [0.2535, 0.500, 0.7465]:
        add_arrow(ax, x_mid - 0.012, 0.37, x_mid + 0.012, 0.37, "", color=MUTED, lw=1.8)

    ax.text(0.5, 0.045,
            "[SINTESIS ROADMAP TIM MBOYZ — DISUSUN OLEH AI AGENT | BERDASARKAN BUKU PEDOMAN HACKATHON DEEP TECH UNJ 2026]",
            ha="center", va="center", fontsize=8.0, fontweight="bold", color=MUTED,
            bbox=dict(boxstyle="round,pad=0.32", fc="#F1F5F9", ec="#CBD5E1"))

    plt.tight_layout(pad=0.4)
    plt.savefig(os.path.join(ASSETS_DIR, "06_roadmap_tkt_dan_evolusi_brover.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    make_fig3_architecture()
    make_fig4_workflow()
    make_fig5_hardware_power()
    make_fig6_roadmap()
    print("REGENERATED ALL 4 VISUALS SUCCESSFULLY")
