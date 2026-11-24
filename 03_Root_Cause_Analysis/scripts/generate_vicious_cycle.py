import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_PATH = "/home/reiziqzip/Programmer/Hackathon-UNJ/03_Root_Cause_Analysis/assets/03_vicious_cycle_mikroklimat_dan_penyakit.png"
os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"

NAVY = "#0F172A"
SLATE = "#334155"
MUTED = "#64748B"

# Source badge palette (replaces verbose inline bracket tags)
COL_RI = "#0D9488"       # Teal: Data Lapangan Indonesia
COL_BIO = "#2563EB"      # Blue: Mekanisme Biologis Umum
COL_MIX = "#7C3AED"      # Purple: Integrasi Data RI & Biologis Umum
COL_FIELD = "#D97706"    # Amber: Bukti Lapangan Daring RI


def draw_stage_card(ax, x, y, w, h, step_num, title, bullets, header_col, bg_col, badge_text, badge_col):
    # Main card
    card = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.006,rounding_size=0.018",
        facecolor=bg_col, edgecolor=header_col, linewidth=2.0, zorder=3
    )
    ax.add_patch(card)

    # Top header strip
    hdr_h = 0.052
    hdr = FancyBboxPatch(
        (x + 0.008, y + h - hdr_h - 0.008), w - 0.016, hdr_h,
        boxstyle="round,pad=0.002,rounding_size=0.010",
        facecolor=header_col, edgecolor="none", zorder=4
    )
    ax.add_patch(hdr)

    # Step number + concise title
    ax.text(x + 0.018, y + h - hdr_h / 2 - 0.008, f"{step_num}. {title}",
            ha="left", va="center", fontsize=9.8, fontweight="bold", color="#FFFFFF", zorder=5)

    # Small clean source badge on top-right of header
    ax.text(x + w - 0.016, y + h - hdr_h / 2 - 0.008, badge_text,
            ha="right", va="center", fontsize=7.4, fontweight="bold", color=header_col,
            bbox=dict(boxstyle="round,pad=0.20", fc="#FFFFFF", ec="none", alpha=0.95), zorder=6)

    # Only 2 concise, high-readability bullet points
    body_text = "\n".join([f"•  {b}" for b in bullets])
    ax.text(x + 0.022, y + h - hdr_h - 0.032, body_text,
            ha="left", va="top", fontsize=9.8, color=NAVY, linespacing=1.65, zorder=5)


def draw_curved_arrow(ax, p1, p2, label, col, rad=-0.12, lx=None, ly=None):
    arr = FancyArrowPatch(
        p1, p2,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>,head_length=8.5,head_width=5.5",
        color=col, linewidth=2.6, zorder=6
    )
    ax.add_patch(arr)
    tx = lx if lx is not None else (p1[0] + p2[0]) / 2
    ty = ly if ly is not None else (p1[1] + p2[1]) / 2
    ax.text(tx, ty, label, ha="center", va="center", fontsize=8.8, fontweight="bold", color=col,
            bbox=dict(boxstyle="round,pad=0.26", fc="#FFFFFF", ec=col, lw=1.0, alpha=0.98), zorder=7)


def main():
    fig, ax = plt.subplots(figsize=(14.4, 8.2), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Clean, concise journal-style title (zero em-dash, zero clutter)
    ax.text(0.5, 0.965, "Siklus Umpan Balik Negatif (Vicious Cycle): Mikroklimat Tropis dan Wabah Penyakit",
            ha="center", va="top", fontsize=14.5, fontweight="bold", color=NAVY)
    ax.text(0.5, 0.922, "Ringkasan 6 tahap keterkaitan instabilitas mikroklimat (Masalah #2) dengan kerentanan infeksi unggas (Masalah #1)",
            ha="center", va="top", fontsize=9.8, color=MUTED)

    # Center core hub
    hub = FancyBboxPatch(
        (0.365, 0.415), 0.270, 0.165,
        boxstyle="round,pad=0.008,rounding_size=0.022",
        facecolor=NAVY, edgecolor="#DC2626", linewidth=2.4, zorder=4
    )
    ax.add_patch(hub)
    ax.text(0.50, 0.535, "KAUSALITAS SILANG", ha="center", va="center",
            fontsize=11.5, fontweight="bold", color="#FFFFFF", zorder=5)
    ax.text(0.50, 0.468, "Ketidakstabilan mikroklimat (#2)\nmelemahkan imunitas ternak dan\nmemperbesar risiko wabah (#1)",
            ha="center", va="center", fontsize=9.2, color="#E2E8F0", linespacing=1.4, zorder=5)

    # Card dimensions (generous whitespace, large readable font)
    cw, ch = 0.315, 0.175

    # Stage 1: Top-Left
    draw_stage_card(
        ax, 0.035, 0.695, cw, ch, 1,
        "Panas & RH Ekstrem",
        ["Suhu 33-36°C; RH dalam CH 82-93%", "70,3% titik ukur CH di zona THI berat"],
        "#EA580C", "#FFF7ED", "Data RI", COL_RI
    )

    # Stage 2: Top-Right
    draw_stage_card(
        ax, 0.650, 0.695, cw, ch, 2,
        "Panting & Litter Basah",
        ["Panting & minum tinggi picu feses encer", "Kadar air litter 46,4% (pH 7,6-8,1)"],
        "#D97706", "#FFFBEB", "Biologis + RI", COL_MIX
    )

    # Stage 3: Mid-Right
    draw_stage_card(
        ax, 0.665, 0.410, cw, ch, 3,
        "Gas NH3 & Stres Kronis",
        ["Litter basah-basa melepas NH3 13-20 ppm", "Stres panas memicu kortikosteron tinggi"],
        "#B45309", "#FEFCE8", "Biologis + RI", COL_MIX
    )

    # Stage 4: Bottom-Right
    draw_stage_card(
        ax, 0.650, 0.125, cw, ch, 4,
        "Kerusakan Trakea & Imun",
        ["NH3 >=15-20 ppm + RH rusak silia trakea", "Involusi limfoid & penurunan antibodi"],
        "#DC2626", "#FEF2F2", "Biologis Umum", COL_BIO
    )

    # Stage 5: Bottom-Left
    draw_stage_card(
        ax, 0.035, 0.125, cw, ch, 5,
        "Koinfeksi & Gagal Vaksin",
        ["Invasi ganda AI, IB, CRD, dan E. coli", "Lesi FPD (40%) picu infeksi sekunder"],
        "#991B1B", "#FEF2F2", "Data RI", COL_RI
    )

    # Stage 6: Mid-Left
    draw_stage_card(
        ax, 0.020, 0.410, cw, ch, 6,
        "Respons Terlambat",
        ["Gejala mirip memicu terapi tidak tepat", "Buka tirai & jual dini perluas penularan"],
        "#7C3AED", "#F5F3FF", "Lapangan RI", COL_FIELD
    )

    # Clockwise arrows with crisp 2-word transition labels
    draw_curved_arrow(ax, (0.355, 0.785), (0.645, 0.785), "Beban termal tinggi", "#EA580C", rad=-0.08, lx=0.50, ly=0.822)
    draw_curved_arrow(ax, (0.825, 0.690), (0.835, 0.590), "Fermentasi litter", "#D97706", rad=-0.15, lx=0.902, ly=0.640)
    draw_curved_arrow(ax, (0.835, 0.405), (0.825, 0.305), "Toksisitas & stres", "#B45309", rad=-0.15, lx=0.902, ly=0.355)
    draw_curved_arrow(ax, (0.645, 0.210), (0.355, 0.210), "Pertahanan melemah", "#DC2626", rad=-0.08, lx=0.50, ly=0.172)
    draw_curved_arrow(ax, (0.175, 0.305), (0.165, 0.405), "Gejala tumpang tindih", "#991B1B", rad=-0.15, lx=0.086, ly=0.355)
    draw_curved_arrow(ax, (0.165, 0.590), (0.175, 0.690), "Umpan balik stres", "#7C3AED", rad=-0.15, lx=0.086, ly=0.640)

    # Concise footer provenance note (detail citations remain in report text)
    ax.text(
        0.5, 0.036,
        "[SINTESIS ANALITIS AI AGENT: PERLU VALIDASI PENELITI]  Ringkasan visual berbasis data Indonesia (Sumiati 2025; Wilcox 2025; Hasibuan 2021; Hartady 2026) & fisiologi unggas (Wang 2022; Zhou 2021; Huang 2024). Detail lengkap pada Bab 4.",
        ha="center", va="center", fontsize=8.0, color=SLATE,
        bbox=dict(boxstyle="round,pad=0.36", fc="#F1F5F9", ec="#CBD5E1")
    )

    plt.tight_layout(pad=0.3)
    plt.savefig(OUT_PATH, dpi=300)
    plt.close()
    print(f"GENERATED CONCISE VICIOUS CYCLE: {OUT_PATH}")


if __name__ == "__main__":
    main()
