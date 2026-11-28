#!/usr/bin/env python3
"""Generate 2 separate, clean, to-the-point vector SVG + high-res PNG diagrams for Section 6 of BROVER:
- 04a_pola_jalur_inspeksi_rover.svg / .png : Top-down broiler barn inspection path (U-turn pattern)
- 04b_alur_4tahap_inspeksi_brover.svg / .png : 4-stage multisensor screening & vet escalation flow

Zero em-dashes, clean vector icons & arrows, rendered at 2x scale via local Playwright Chromium.
"""

import os
from html import escape
from playwright.sync_api import sync_playwright

BASE_DIR = "/home/reiziqzip/Programmer/Hackathon-UNJ/06_Project_Concept_BROVER"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SVG_4A = os.path.join(ASSETS_DIR, "04a_pola_jalur_inspeksi_rover.svg")
PNG_4A = os.path.join(ASSETS_DIR, "04a_pola_jalur_inspeksi_rover.png")
SVG_4B = os.path.join(ASSETS_DIR, "04b_alur_4tahap_inspeksi_brover.svg")
PNG_4B = os.path.join(ASSETS_DIR, "04b_alur_4tahap_inspeksi_brover.png")


def render_svg_to_png(svg_path: str, png_path: str, width: int, height: int) -> None:
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  html, body {{
    margin: 0;
    padding: 0;
    width: {width}px;
    height: {height}px;
    background: #FFFFFF;
    overflow: hidden;
  }}
  svg {{
    display: block;
    width: {width}px;
    height: {height}px;
  }}
</style>
</head>
<body>{svg_content}</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=2)
        page.set_content(html, wait_until="load")
        page.screenshot(path=png_path, full_page=False)
        browser.close()


# ==============================================================================
# DIAGRAM 4A: Pola Jalur Inspeksi Rover di Kandang Broiler (1280 x 840)
# ==============================================================================
def icon_drop(cx: float, cy: float, color: str = "#2563EB") -> str:
    return f"""
    <g transform="translate({cx - 9},{cy - 9})" fill="{color}" opacity="0.9">
      <path d="M9 1.5C9 1.5 3.5 8 3.5 12a5.5 5.5 0 0 0 11 0C14.5 8 9 1.5 9 1.5z"/>
    </g>"""


def icon_mic_small(cx: float, cy: float, color: str = "#7C3AED") -> str:
    return f"""
    <g transform="translate({cx - 8},{cy - 8})" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="5.5" y="1.8" width="5" height="7.5" rx="2.5" fill="#EDE9FE"/>
      <path d="M3.5 8.5a4.5 4.5 0 0 0 9 0"/>
      <line x1="8" y1="13" x2="8" y2="15"/>
    </g>"""


def icon_zone_small(cx: float, cy: float, color: str = "#7C3AED") -> str:
    """Titik zona tetap: tempat rover berhenti untuk foto feses dan baca udara."""
    return f"""
    <g fill="none" stroke="{color}" stroke-width="1.9">
      <circle cx="{cx}" cy="{cy}" r="7.2"/>
      <circle cx="{cx}" cy="{cy}" r="2.6" fill="{color}"/>
    </g>"""


def icon_cam_alert(cx: float, cy: float, color: str = "#DC2626") -> str:
    return f"""
    <g transform="translate({cx - 9},{cy - 9})" fill="none" stroke="{color}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
      <path d="M2 6.5A1.8 1.8 0 0 1 3.8 4.7h1.8l1.1-1.6h4.6l1.1 1.6h1.8A1.8 1.8 0 0 1 16 6.5v6.7a1.8 1.8 0 0 1-1.8 1.8H3.8A1.8 1.8 0 0 1 2 13.2z" fill="#FEE2E2"/>
      <circle cx="9" cy="9.8" r="2.6"/>
    </g>"""


def icon_rover_topdown(cx: float, cy: float) -> str:
    """Crisp top-down BROVER rover facing UP (north) along the aisle."""
    return f"""
    <g transform="translate({cx - 22},{cy - 28})">
      <!-- Camera FOV cone pointing UP -->
      <path d="M16 4 L4 -18 L40 -18 L28 4 Z" fill="#38BDF8" opacity="0.28"/>
      <!-- 4 Wheels -->
      <rect x="0" y="7" width="6" height="13" rx="2.5" fill="#0F172A"/>
      <rect x="38" y="7" width="6" height="13" rx="2.5" fill="#0F172A"/>
      <rect x="0" y="34" width="6" height="13" rx="2.5" fill="#0F172A"/>
      <rect x="38" y="34" width="6" height="13" rx="2.5" fill="#0F172A"/>
      <!-- Chassis body -->
      <rect x="6" y="4" width="32" height="46" rx="8" fill="#0D9488" stroke="#0F766E" stroke-width="2"/>
      <!-- Inner top deck -->
      <rect x="11" y="12" width="22" height="30" rx="4" fill="#CCFBF1"/>
      <!-- Front camera head -->
      <rect x="15" y="2" width="14" height="7" rx="2.5" fill="#0F172A"/>
      <circle cx="22" cy="5.5" r="2.2" fill="#38BDF8"/>
      <!-- Direction chevron on top -->
      <path d="M17 29 L22 22 L27 29" fill="none" stroke="#0F766E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>"""


def build_svg_4a() -> str:
    w, h = 1280, 840

    # Barn floorplan bounds
    bx, by, bw, bh = 44, 112, 872, 676

    # 4 vertical equipment line X positions
    x_nip1 = 132
    x_pan1 = 374
    x_nip2 = 616
    x_pan2 = 842

    # 3 inspection aisle center X positions
    x_a1 = 253   # between Nipple 1 (132) & Pan Feeder 1 (374)
    x_a2 = 495   # between Pan Feeder 1 (374) & Nipple 2 (616)
    x_a3 = 729   # between Nipple 2 (616) & Pan Feeder 2 (842)

    # Nipple lines (blue pipes + nipple ticks)
    nipples_svg = []
    for nx in (x_nip1, x_nip2):
        nipples_svg.append(
            f'<line x1="{nx}" y1="226" x2="{nx}" y2="690" stroke="#2563EB" stroke-width="4" stroke-linecap="round"/>'
        )
        for ny in range(256, 680, 44):
            nipples_svg.append(
                f'<circle cx="{nx}" cy="{ny}" r="4.5" fill="#FFFFFF" stroke="#2563EB" stroke-width="2"/>'
            )
        # Header badge
        nipples_svg.append(
            f'<rect x="{nx - 52}" y="190" width="104" height="28" rx="14" fill="#DBEAFE" stroke="#93C5FD" stroke-width="1.2"/>'
            f'{icon_drop(nx - 36, 204, "#2563EB")}'
            f'<text x="{nx + 7}" y="208.5" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="11.5" font-weight="700" fill="#1D4ED8">Nipple</text>'
        )

    # Pan feeder lines (amber pipe + circular pans)
    pans_svg = []
    for px in (x_pan1, x_pan2):
        pans_svg.append(
            f'<line x1="{px}" y1="226" x2="{px}" y2="690" stroke="#EA580C" stroke-width="3.2" stroke-linecap="round"/>'
        )
        for py in range(258, 680, 74):
            pans_svg.append(
                f'<circle cx="{px}" cy="{py}" r="14.5" fill="#FDBA74" stroke="#C2410C" stroke-width="2.2"/>'
                f'<circle cx="{px}" cy="{py}" r="5" fill="#EA580C" opacity="0.65"/>'
            )
        pans_svg.append(
            f'<rect x="{px - 56}" y="190" width="112" height="28" rx="14" fill="#FFEDD5" stroke="#FDBA74" stroke-width="1.2"/>'
            f'<circle cx="{px - 39}" cy="204" r="6" fill="#F97316"/>'
            f'<text x="{px + 8}" y="208.5" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="11.5" font-weight="700" fill="#C2410C">Pan Feeder</text>'
        )

    # Fixed zone stop markers (clean pills offset slightly to right/left so zero overlap!)
    zone_points = [
        (x_a1, 515, "Zona A1", "Foto + T/RH/NH₃", "right"),
        (x_a1, 315, "Zona A2", "Foto + T/RH/NH₃", "right"),
        (x_a2, 315, "Zona B2", "Foto + T/RH/NH₃", "right"),
        (x_a2, 622, "Zona B1", "Foto + T/RH/NH₃", "right"),
        (x_a3, 420, "Zona C1", "Foto + T/RH/NH₃", "right"),
    ]
    zones_svg = []
    for zx, zy, ztitle, zsub, side in zone_points:
        bx_card = zx + 20 if side == "right" else zx - 156
        # Avoid colliding with Pan/Nipple lines: center pill directly around the dot cleanly!
        # Wait: width between x_a1 (253) and x_pan1 (374) is 121px! Placing a 132px box centered on zx (zx-66..zx+66)
        # gives 55px margin to both neighboring lines (121 - 66 = 55px -> ZERO collision!).
        card_w = 138
        cx_box = zx - card_w / 2
        zones_svg.append(f"""
        <g filter="url(#softShadow)">
          <rect x="{cx_box:.1f}" y="{zy - 24}" width="{card_w}" height="48" rx="11" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="1.8"/>
          <circle cx="{cx_box + 20:.1f}" cy="{zy}" r="13" fill="#EDE9FE"/>
          {icon_zone_small(cx_box + 20, zy, "#7C3AED")}
          <text x="{cx_box + 39:.1f}" y="{zy - 4}" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="700" fill="#4C1D95">{escape(ztitle)}</text>
          <text x="{cx_box + 39:.1f}" y="{zy + 13}" font-family="'Open Sans', sans-serif" font-size="10.2" font-weight="600" fill="#6D28D9">{escape(zsub)}</text>
        </g>""")

    # Red finding callout on Aisle 2 (y = 472, perfectly centered between B2 at 315 and B1 at 622!)
    fx, fy = x_a2, 472
    fcard_w = 166
    fx_box = fx - fcard_w / 2
    finding_svg = f"""
    <g filter="url(#softShadow)">
      <rect x="{fx_box:.1f}" y="{fy - 30}" width="{fcard_w}" height="60" rx="12" fill="#FEF2F2" stroke="#DC2626" stroke-width="2.2"/>
      <circle cx="{fx_box + 22:.1f}" cy="{fy}" r="14.5" fill="#FEE2E2"/>
      {icon_cam_alert(fx_box + 22, fy, "#DC2626")}
      <text x="{fx_box + 43:.1f}" y="{fy - 6}" font-family="'Montserrat', sans-serif" font-size="11.2" font-weight="800" fill="#991B1B">Temuan Feses</text>
      <text x="{fx_box + 43:.1f}" y="{fy + 10}" font-family="'Open Sans', sans-serif" font-size="10.0" font-weight="600" fill="#B91C1C">Ditandai model CV</text>
      <text x="{fx_box + 43:.1f}" y="{fy + 23}" font-family="'Open Sans', sans-serif" font-size="10.0" font-weight="600" fill="#B91C1C">Masuk daftar triase</text>
    </g>"""

    # Legend items on right panel (x: 944..1236, w = 292)
    lx, lw = 944, 292

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="softShadow" x="-6%" y="-6%" width="114%" height="118%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <marker id="pathArrow" viewBox="0 0 10 10" refX="7.5" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto">
      <path d="M 0 1.2 L 8.5 5 L 0 8.8 z" fill="#0D9488"/>
    </marker>
  </defs>

  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <!-- ================= HEADER ================= -->
  <rect x="486" y="16" width="308" height="24" rx="12" fill="#CCFBF1"/>
  <text x="640" y="32" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="700" letter-spacing="0.7" fill="#0F766E">DENAH OPERASI KANDANG BROILER</text>
  <text x="640" y="69" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="25" font-weight="800" fill="#0F172A">Pola Jalur Inspeksi Rover di Kandang Broiler</text>
  <text x="640" y="95" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="13.5" fill="#475569">Rover berhenti di titik zona tetap, 2 putaran per hari (pagi &amp; 15.00–16.00); hari 0–6 dan di luar putaran parkir di dok sebagai mode stasiun</text>

  <!-- ================= BARN FLOORPLAN ================= -->
  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="22" fill="#FFFBEB" stroke="#B45309" stroke-width="2.6" filter="url(#softShadow)"/>

  <!-- Top Turning Space clean pill -->
  <rect x="260" y="130" width="440" height="32" rx="16" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.3"/>
  <text x="480" y="150.5" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="700" fill="#92400E">Ruang Putar Ujung Kandang (3-4 m | Standar Cobb &amp; Ross)</text>

  <!-- Equipment lines -->
  {''.join(nipples_svg)}
  {''.join(pans_svg)}

  <!-- ================= U-TURN ROVER PATH ================= -->
  <!-- Leg 0: Out of dock to Aisle 1 -->
  <path d="M 198 738 L {x_a1} 738 L {x_a1} 668" fill="none" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#pathArrow)"/>
  <!-- Leg 1: Up Aisle 1 -->
  <line x1="{x_a1}" y1="600" x2="{x_a1}" y2="412" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" marker-end="url(#pathArrow)"/>
  <line x1="{x_a1}" y1="412" x2="{x_a1}" y2="174" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7"/>
  <!-- Turn 1 (Top U-Turn Aisle 1 -> Aisle 2) -->
  <path d="M {x_a1} 174 L {x_a2} 174 L {x_a2} 254" fill="none" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#pathArrow)"/>
  <!-- Leg 2: Down Aisle 2 -->
  <line x1="{x_a2}" y1="254" x2="{x_a2}" y2="412" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" marker-end="url(#pathArrow)"/>
  <line x1="{x_a2}" y1="412" x2="{x_a2}" y2="738" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7"/>
  <!-- Turn 2 (Bottom U-Turn Aisle 2 -> Aisle 3) -->
  <path d="M {x_a2} 738 L {x_a3} 738 L {x_a3} 570" fill="none" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#pathArrow)"/>
  <!-- Leg 3: Up Aisle 3 & continue right -->
  <path d="M {x_a3} 570 L {x_a3} 174 L 882 174" fill="none" stroke="#0D9488" stroke-width="4" stroke-dasharray="10,7" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#pathArrow)"/>

  <!-- Dock inside the house (Start/Finish, station mode) -->
  <g filter="url(#softShadow)">
    <rect x="68" y="704" width="132" height="62" rx="13" fill="#0F766E" stroke="#115E59" stroke-width="2"/>
    <text x="134" y="732" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">DOK</text>
    <text x="134" y="751" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="10.8" font-weight="600" fill="#CCFBF1">Area brooding</text>
  </g>

  <!-- Top-Down Rover Icon on Aisle 1 -->
  {icon_rover_topdown(x_a1, 626)}

  <!-- Zone Markers & Finding Event -->
  {''.join(zones_svg)}
  {finding_svg}

  <!-- ================= RIGHT LEGEND PANEL ================= -->
  <rect x="{lx}" y="{by}" width="{lw}" height="{bh}" rx="20" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.8" filter="url(#softShadow)"/>
  <path d="M{lx + 20} {by} H{lx + lw - 20} Q{lx + lw} {by} {lx + lw} {by + 20} V{by + 54} H{lx} V{by + 20} Q{lx} {by} {lx + 20} {by} Z" fill="#1E293B"/>
  <text x="{lx + lw / 2}" y="{by + 33}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">KETERANGAN SIMBOL</text>

  <!-- Legend Item 1: Rover Path -->
  <rect x="{lx + 16}" y="186" width="{lw - 32}" height="74" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.3"/>
  <line x1="{lx + 28}" y1="223" x2="{lx + 68}" y2="223" stroke="#0D9488" stroke-width="3.5" stroke-dasharray="7,4" marker-end="url(#pathArrow)"/>
  <text x="{lx + 84}" y="213" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="700" fill="#0F172A">Jalur Putaran (Huruf U)</text>
  <text x="{lx + 84}" y="232" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">0,07–0,1 m/s, 2 putaran/hari:</text>
  <text x="{lx + 84}" y="247" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">pagi &amp; pukul 15.00–16.00</text>

  <!-- Legend Item 2: Nipple & Pan Feeder -->
  <rect x="{lx + 16}" y="274" width="{lw - 32}" height="80" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.3"/>
  <circle cx="{lx + 42}" cy="300" r="8" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="{lx + 62}" y="304" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#1D4ED8">Baris Nipple (Minum)</text>
  <circle cx="{lx + 42}" cy="332" r="9.5" fill="#FDBA74" stroke="#C2410C" stroke-width="2"/>
  <text x="{lx + 62}" y="336" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#C2410C">Baris Pan Feeder (Pakan)</text>

  <!-- Legend Item 3: Fixed zone stop -->
  <rect x="{lx + 16}" y="368" width="{lw - 32}" height="82" rx="12" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.4"/>
  <circle cx="{lx + 44}" cy="409" r="17" fill="#EDE9FE"/>
  {icon_zone_small(lx + 44, 409, "#7C3AED")}
  <text x="{lx + 72}" y="397" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="700" fill="#4C1D95">Titik Zona Tetap</text>
  <text x="{lx + 72}" y="416" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#475569">Berhenti: foto feses + LED</text>
  <text x="{lx + 72}" y="432" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#475569">+ baca suhu, RH &amp; tren NH&#8323;</text>

  <!-- Legend Item 4: Visual Finding -->
  <rect x="{lx + 16}" y="464" width="{lw - 32}" height="82" rx="12" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.4"/>
  <circle cx="{lx + 44}" cy="505" r="17" fill="#FEE2E2"/>
  {icon_cam_alert(lx + 44, 505, "#DC2626")}
  <text x="{lx + 72}" y="493" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="700" fill="#991B1B">Temuan Feses Abnormal</text>
  <text x="{lx + 72}" y="512" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#7F1D1D">Masuk daftar triase</text>
  <text x="{lx + 72}" y="528" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#7F1D1D">3 tombol di dasbor</text>

  <!-- Legend Item 5: Dock -->
  <rect x="{lx + 16}" y="560" width="{lw - 32}" height="74" rx="12" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1.4"/>
  <rect x="{lx + 28}" y="582" width="34" height="30" rx="7" fill="#0F766E"/>
  <text x="{lx + 45}" y="601" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="8.5" font-weight="800" fill="#FFFFFF">DOK</text>
  <text x="{lx + 74}" y="588" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="700" fill="#0F766E">Dok di Dalam Kandang</text>
  <text x="{lx + 74}" y="606" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#334155">Mode stasiun: catat per menit,</text>
  <text x="{lx + 74}" y="621" font-family="'Open Sans', sans-serif" font-size="11.1" fill="#334155">isi daya &amp; sanitasi roda</text>

  <!-- Compact Mode Info Strip -->
  <rect x="{lx + 16}" y="654" width="{lw - 32}" height="114" rx="14" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.4"/>
  <text x="{lx + 32}" y="680" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="#1E40AF">MODE PENGENDALIAN</text>
  <text x="{lx + 32}" y="704" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="700" fill="#0F172A">Saat Ini:</text>
  <text x="{lx + 32}" y="721" font-family="'Open Sans', sans-serif" font-size="11.3" fill="#334155">Disetir lewat web (Wi-Fi lokal)</text>
  <text x="{lx + 32}" y="743" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="700" fill="#0F172A">Kelak:</text>
  <text x="{lx + 32}" y="760" font-family="'Open Sans', sans-serif" font-size="11.3" fill="#334155">CV navigasi + jadwal otomatis</text>

  <!-- Footer -->
  <rect x="44" y="800" width="1192" height="28" rx="8" fill="#F1F5F9"/>
  <text x="640" y="818.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11" font-weight="600" fill="#64748B">Tim Asprak (Teknologi Informasi ITS &amp; Biologi UNJ)  |  Tata Letak Jalur Mengacu Standar Kandang Cobb 500 &amp; Ross 308</text>
</svg>
"""
    return svg


# ==============================================================================
# DIAGRAM 4B: Alur 4-Tahap Inspeksi Multisensor & Pelaporan Dokter Hewan (1600 x 760)
# ==============================================================================
def hero_icon_stage1(cx: float, cy: float) -> str:
    """Rover + Phone control icon (for Stage 1)."""
    return f"""
    <g transform="translate({cx - 24},{cy - 22})" fill="none" stroke="#0F766E" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Rover body -->
      <path d="M2 22 L28 22 L34 27 L34 34 L2 34 Z" fill="#CCFBF1"/>
      <rect x="29" y="18" width="9" height="7" rx="2" fill="#0F172A" stroke="#0F172A" stroke-width="1.2"/>
      <circle cx="35.5" cy="21.5" r="1.8" fill="#38BDF8" stroke="none"/>
      <circle cx="10" cy="36" r="5" fill="#1E293B" stroke="#0F172A"/>
      <circle cx="27" cy="36" r="5" fill="#1E293B" stroke="#0F172A"/>
      <!-- Signal wave to phone -->
      <path d="M12 12 a8 8 0 0 1 11 0" stroke="#0D9488"/>
      <path d="M14.5 15.5 a4.5 4.5 0 0 1 6 0" stroke="#0D9488"/>
      <!-- Mini phone top right -->
      <rect x="33" y="2" width="14" height="21" rx="3" fill="#FFFFFF" stroke="#0F766E" stroke-width="2"/>
      <circle cx="40" cy="19.5" r="1" fill="#0F766E" stroke="none"/>
    </g>"""


def hero_icon_stage2(cx: float, cy: float) -> str:
    """AI Chip + sensor waves icon (for Stage 2)."""
    return f"""
    <g transform="translate({cx - 22},{cy - 22})" fill="none" stroke="#6D28D9" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="11" y="11" width="22" height="22" rx="5" fill="#EDE9FE"/>
      <text x="22" y="26.5" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#5B21B6" stroke="none">AI</text>
      <line x1="16" y1="5" x2="16" y2="11"/>
      <line x1="28" y1="5" x2="28" y2="11"/>
      <line x1="16" y1="33" x2="16" y2="39"/>
      <line x1="28" y1="33" x2="28" y2="39"/>
      <line x1="5" y1="16" x2="11" y2="16"/>
      <line x1="5" y1="28" x2="11" y2="28"/>
      <line x1="33" y1="16" x2="39" y2="16"/>
      <line x1="33" y1="28" x2="39" y2="28"/>
    </g>"""


def hero_icon_stage3(cx: float, cy: float) -> str:
    """Human-in-the-loop verification icon (for Stage 3)."""
    return f"""
    <g transform="translate({cx - 22},{cy - 22})" fill="none" stroke="#B45309" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="17" cy="13" r="6" fill="#FEF3C7"/>
      <path d="M6 34c1-6.5 5-10 11-10s10 3.5 11 10" fill="#FEF3C7"/>
      <circle cx="33" cy="28" r="8.5" fill="#FFFFFF" stroke="#059669" stroke-width="2.2"/>
      <path d="M29.3 28.2l2.5 2.5 5-5.2" stroke="#059669" stroke-width="2.3"/>
    </g>"""


def hero_icon_stage4(cx: float, cy: float) -> str:
    """Vet Report + Wheel Hygiene Shield icon (for Stage 4)."""
    return f"""
    <g transform="translate({cx - 22},{cy - 22})" fill="none" stroke="#1D4ED8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="6" y="5" width="22" height="30" rx="4" fill="#DBEAFE"/>
      <line x1="11" y1="13" x2="23" y2="13"/>
      <line x1="11" y1="19" x2="23" y2="19"/>
      <line x1="11" y1="25" x2="18" y2="25"/>
      <!-- Medical cross badge -->
      <circle cx="32" cy="29" r="9" fill="#FFE4E6" stroke="#E11D48" stroke-width="2.2"/>
      <line x1="32" y1="25" x2="32" y2="33" stroke="#E11D48" stroke-width="2.4"/>
      <line x1="28" y1="29" x2="36" y2="29" stroke="#E11D48" stroke-width="2.4"/>
    </g>"""


def bullet_item(x: float, y: float, title: str, desc1: str, desc2: str, color: str) -> str:
    parts = [
        f'<circle cx="{x + 9}" cy="{y - 4}" r="8" fill="{color}" opacity="0.14"/>',
        f'<path d="M{x + 5.5} {y - 4} l2.3 2.4 4.2-4.6" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        f'<text x="{x + 25}" y="{y}" font-family="\'Montserrat\', sans-serif" font-size="12.6" font-weight="700" fill="#0F172A">{escape(title)}</text>',
        f'<text x="{x + 25}" y="{y + 19}" font-family="\'Open Sans\', sans-serif" font-size="11.8" fill="#475569">{escape(desc1)}</text>',
    ]
    if desc2:
        parts.append(
            f'<text x="{x + 25}" y="{y + 36}" font-family="\'Open Sans\', sans-serif" font-size="11.8" fill="#475569">{escape(desc2)}</text>'
        )
    return "\n".join(parts)


def build_svg_4b() -> str:
    w, h = 1600, 760

    # 4 equal cards across 1600px: margin=36, 3 gaps of 56px -> 1528 - 168 = 1360 -> w = 340px each!
    cw = 340
    gap = 56
    xs = [36 + i * (cw + gap) for i in range(4)]  # 36, 432, 828, 1224
    cy_top = 128
    ch = 556

    stages_meta = [
        (xs[0], "1", "TAHAP 1", "Setup & Pengambilan Data", "#0D9488", "#F0FDFA", "#5EEAD4", "#0F766E", hero_icon_stage1),
        (xs[1], "2", "TAHAP 2", "Skrining Feses & Udara", "#7C3AED", "#F5F3FF", "#C4B5FD", "#5B21B6", hero_icon_stage2),
        (xs[2], "3", "TAHAP 3", "Verifikasi Manusia (Triase)", "#D97706", "#FFFBEB", "#FCD34D", "#B45309", hero_icon_stage3),
        (xs[3], "4", "TAHAP 4", "Laporan 1-Klik & Sanitasi", "#2563EB", "#EFF6FF", "#93C5FD", "#1D4ED8", hero_icon_stage4),
    ]

    cards_bg = []
    for sx, num, label, title, main_col, tint_bg, border_col, dark_col, icon_fn in stages_meta:
        cards_bg.append(f"""
        <g filter="url(#cardShadow)">
          <rect x="{sx}" y="{cy_top}" width="{cw}" height="{ch}" rx="20" fill="{tint_bg}" stroke="{border_col}" stroke-width="2"/>
          <path d="M{sx + 20} {cy_top} H{sx + cw - 20} Q{sx + cw} {cy_top} {sx + cw} {cy_top + 20} V{cy_top + 56} H{sx} V{cy_top + 20} Q{sx} {cy_top} {sx + 20} {cy_top} Z" fill="{main_col}"/>
        </g>
        <circle cx="{sx + 30}" cy="{cy_top + 28}" r="15" fill="#FFFFFF"/>
        <text x="{sx + 30}" y="{cy_top + 33.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14.5" font-weight="800" fill="{dark_col}">{num}</text>
        <text x="{sx + 55}" y="{cy_top + 24}" font-family="'Montserrat', sans-serif" font-size="10.2" font-weight="700" letter-spacing="0.8" fill="#FFFFFF" opacity="0.9">{label}</text>
        <text x="{sx + 55}" y="{cy_top + 43}" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">{escape(title)}</text>

        <!-- Hero icon circle -->
        <circle cx="{sx + cw / 2}" cy="{cy_top + 106}" r="36" fill="#FFFFFF" stroke="{border_col}" stroke-width="2" filter="url(#cardShadow)"/>
        {icon_fn(sx + cw / 2, cy_top + 106)}
        """)

    # Big directional arrows between cards
    arrow_y = cy_top + 278
    arrows_svg = []
    arrow_colors = ["#0D9488", "#7C3AED", "#D97706"]
    marker_ids = ["arr1", "arr2", "arr3"]
    for i in range(3):
        ax1 = xs[i] + cw + 7
        ax2 = xs[i + 1] - 7
        arrows_svg.append(
            f'<line x1="{ax1}" y1="{arrow_y}" x2="{ax2}" y2="{arrow_y}" stroke="{arrow_colors[i]}" stroke-width="4" marker-end="url(#{marker_ids[i]})"/>'
        )

    # Inner white content panel per stage (y: cy_top + 158 .. cy_top + 494 -> h = 336)
    py_in = cy_top + 158
    ph_in = 336

    # Stage 1 body
    s1_x = xs[0] + 16
    s1_w = cw - 32
    stage1_body = f"""
    <rect x="{s1_x}" y="{py_in}" width="{s1_w}" height="{ph_in}" rx="14" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.4"/>
    {bullet_item(s1_x + 14, py_in + 36, "Setup 1× Saat Chick-In", "Pilih bibit Cobb 500 / Ross 308", "untuk hitung umur otomatis", "#0D9488")}
    {bullet_item(s1_x + 14, py_in + 126, "Putaran Rover 2×/Hari", "Pagi & 15.00–16.00, berhenti", "di titik zona (0,07–0,1 m/s)", "#0D9488")}
    {bullet_item(s1_x + 14, py_in + 216, "Foto Feses & Udara", "Kamera 45° + LED, suhu, RH,", "tren NH₃; Saku: foto HP", "#0D9488")}
    <rect x="{s1_x}" y="{cy_top + 506}" width="{s1_w}" height="32" rx="16" fill="#FFFFFF" stroke="#5EEAD4" stroke-width="1.4"/>
    <text x="{xs[0] + cw / 2}" y="{cy_top + 526}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="700" fill="#0F766E">Rem Aman 500 ms  |  Tetap Jalan Offline</text>
    """

    # Stage 2 body
    s2_x = xs[1] + 16
    s2_w = cw - 32
    stage2_body = f"""
    <rect x="{s2_x}" y="{py_in}" width="{s2_w}" height="{ph_in}" rx="14" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.4"/>
    {bullet_item(s2_x + 14, py_in + 36, "Cek Udara vs Umur Ayam", "Normal, Waspada, atau Bahaya", "vs Cobb 500 / Ross 308 + THI", "#7C3AED")}
    {bullet_item(s2_x + 14, py_in + 126, "Prakiraan Cuaca Luar", "Hibrida BMKG + Open-Meteo", "antisipasi cekaman panas sore", "#7C3AED")}
    {bullet_item(s2_x + 14, py_in + 216, "1 Model CV Feses (Edge)", "Tandai feses abnormal; foto", "Saku diproses di server", "#7C3AED")}
    <rect x="{s2_x}" y="{cy_top + 506}" width="{s2_w}" height="32" rx="16" fill="#FFFFFF" stroke="#C4B5FD" stroke-width="1.4"/>
    <text x="{xs[1] + cw / 2}" y="{cy_top + 526}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="700" fill="#5B21B6">Evaluasi Objektif  |  Tanpa Skor 0-100</text>
    """

    # Stage 3 body (Visual 3 Decision Buttons!)
    s3_x = xs[2] + 16
    s3_w = cw - 32
    stage3_body = f"""
    <rect x="{s3_x}" y="{py_in}" width="{s3_w}" height="{ph_in}" rx="14" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.4"/>
    {bullet_item(s3_x + 14, py_in + 34, "Tinjau Bukti & Ceklis", "Foto feses, grafik udara, &", "ceklis gejala pernapasan ABK", "#D97706")}
    <text x="{s3_x + 16}" y="{py_in + 114}" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="#92400E">PILIH 1 DARI 3 TOMBOL AKSI:</text>

    <!-- Button 1: Akan Saya Cek -->
    <rect x="{s3_x + 14}" y="{py_in + 128}" width="{s3_w - 28}" height="52" rx="11" fill="#ECFDF5" stroke="#10B981" stroke-width="1.6"/>
    <circle cx="{s3_x + 36}" cy="{py_in + 154}" r="11" fill="#10B981"/>
    <path d="M{s3_x + 31.5} {py_in + 154} l3 3 5.5-5.5" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="{s3_x + 56}" y="{py_in + 150}" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" fill="#065F46">Akan Saya Cek</text>
    <text x="{s3_x + 56}" y="{py_in + 167}" font-family="'Open Sans', sans-serif" font-size="10.6" fill="#047857">ABK cek langsung + Kamus Gejala</text>

    <!-- Button 2: Terlihat Normal -->
    <rect x="{s3_x + 14}" y="{py_in + 190}" width="{s3_w - 28}" height="52" rx="11" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.6"/>
    <circle cx="{s3_x + 36}" cy="{py_in + 216}" r="11" fill="#64748B"/>
    <line x1="{s3_x + 31}" y1="{py_in + 216}" x2="{s3_x + 41}" y2="{py_in + 216}" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>
    <text x="{s3_x + 56}" y="{py_in + 212}" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" fill="#1E293B">Terlihat Normal</text>
    <text x="{s3_x + 56}" y="{py_in + 229}" font-family="'Open Sans', sans-serif" font-size="10.6" fill="#475569">Tandai salah deteksi (perbaiki AI)</text>

    <!-- Button 3: Laporkan ke Dokter Hewan -->
    <rect x="{s3_x + 14}" y="{py_in + 252}" width="{s3_w - 28}" height="52" rx="11" fill="#FFF1F2" stroke="#F43F5E" stroke-width="1.6"/>
    <circle cx="{s3_x + 36}" cy="{py_in + 278}" r="11" fill="#E11D48"/>
    <path d="M{s3_x + 32} {py_in + 278} h8 M{s3_x + 36.5} {py_in + 274} l3.5 4-3.5 4" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="{s3_x + 56}" y="{py_in + 274}" font-family="'Montserrat', sans-serif" font-size="12" font-weight="700" fill="#9F1239">Laporkan Dokter Hewan</text>
    <text x="{s3_x + 56}" y="{py_in + 291}" font-family="'Open Sans', sans-serif" font-size="10.6" fill="#BE123C">Kirim bukti klinis 1-Klik (WA/PDF)</text>

    <rect x="{s3_x}" y="{cy_top + 506}" width="{s3_w}" height="32" rx="16" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.4"/>
    <text x="{xs[2] + cw / 2}" y="{cy_top + 526}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="700" fill="#B45309">Human-in-the-Loop  |  Bukan Diagnosis AI</text>
    """

    # Stage 4 body (2 clear outcome blocks: 1-Click Vet Report + 3-Step Wheel Hygiene)
    s4_x = xs[3] + 16
    s4_w = cw - 32
    stage4_body = f"""
    <!-- Block A: 1-Click Report -->
    <rect x="{s4_x}" y="{py_in}" width="{s4_w}" height="162" rx="14" fill="#FFFFFF" stroke="#FDA4AF" stroke-width="1.6"/>
    <rect x="{s4_x + 12}" y="{py_in + 12}" width="{s4_w - 24}" height="28" rx="8" fill="#FFE4E6"/>
    <text x="{xs[3] + cw / 2}" y="{py_in + 30.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="#9F1239">LAPORAN 1-KLIK DOKTER HEWAN</text>
    {bullet_item(s4_x + 14, py_in + 66, "Paket Bukti via WA / PDF", "Umur flok, deplesi, foto feses,", "ceklis gejala & grafik udara", "#E11D48")}
    <text x="{s4_x + 39}" y="{py_in + 132}" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#BE123C">Siap dikirim ke Dokter Hewan / Dinas</text>

    <!-- Block B: Wheel Sanitation SOP -->
    <rect x="{s4_x}" y="{py_in + 174}" width="{s4_w}" height="162" rx="14" fill="#FFFFFF" stroke="#5EEAD4" stroke-width="1.6"/>
    <rect x="{s4_x + 12}" y="{py_in + 186}" width="{s4_w - 24}" height="28" rx="8" fill="#CCFBF1"/>
    <text x="{xs[3] + cw / 2}" y="{py_in + 204.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="#0F766E">SOP SANITASI RODA DI DOK</text>
    <text x="{xs[3] + cw / 2}" y="{py_in + 234}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">Wajib 3 langkah setelah kembali ke dok:</text>

    <!-- 3 mini step pills with arrows -->
    <rect x="{s4_x + 12}" y="{py_in + 248}" width="84" height="44" rx="9" fill="#F0FDFA" stroke="#2DD4BF" stroke-width="1.4"/>
    <text x="{s4_x + 54}" y="{py_in + 266}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="800" fill="#0F766E">1. Sikat</text>
    <text x="{s4_x + 54}" y="{py_in + 282}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" fill="#334155">Buang sekam</text>
    <text x="{s4_x + 104}" y="{py_in + 274}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#0D9488">&#8594;</text>

    <rect x="{s4_x + 112}" y="{py_in + 248}" width="84" height="44" rx="9" fill="#F0FDFA" stroke="#2DD4BF" stroke-width="1.4"/>
    <text x="{s4_x + 154}" y="{py_in + 266}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="800" fill="#0F766E">2. Semprot</text>
    <text x="{s4_x + 154}" y="{py_in + 282}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" fill="#334155">Disinfektan</text>
    <text x="{s4_x + 204}" y="{py_in + 274}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13" font-weight="800" fill="#0D9488">&#8594;</text>

    <rect x="{s4_x + 212}" y="{py_in + 248}" width="84" height="44" rx="9" fill="#F0FDFA" stroke="#2DD4BF" stroke-width="1.4"/>
    <text x="{s4_x + 254}" y="{py_in + 266}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="800" fill="#0F766E">3. Kering</text>
    <text x="{s4_x + 254}" y="{py_in + 282}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" fill="#334155">+ Log Digital</text>

    <text x="{xs[3] + cw / 2}" y="{py_in + 318}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="10.8" font-weight="600" fill="#0F766E">Cegah kontaminasi silang antar-siklus</text>

    <rect x="{s4_x}" y="{cy_top + 506}" width="{s4_w}" height="32" rx="16" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.4"/>
    <text x="{xs[3] + cw / 2}" y="{cy_top + 526}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="700" fill="#1D4ED8">SOP 1 Unit = 1 Kandang + Protokol Pindah</text>
    """

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="cardShadow" x="-4%" y="-4%" width="108%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0D9488"/>
    </marker>
    <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#7C3AED"/>
    </marker>
    <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#D97706"/>
    </marker>
  </defs>

  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <!-- ================= HEADER ================= -->
  <rect x="572" y="16" width="456" height="24" rx="12" fill="#EDE9FE"/>
  <text x="800" y="32" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="700" letter-spacing="0.7" fill="#5B21B6">ALUR KERJA INSPEKSI MULTISENSOR BROVER</text>
  <text x="800" y="70" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="25.5" font-weight="800" fill="#0F172A">4 Tahap Inspeksi Kandang hingga Pelaporan Dokter Hewan</text>
  <text x="800" y="98" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="13.6" fill="#475569">Dari putaran rover atau foto HP, skrining feses dan udara terhadap standar umur, triase 3 tombol, hingga laporan dokter hewan</text>

  <!-- ================= 4 STAGE CARDS ================= -->
  {''.join(cards_bg)}
  {stage1_body}
  {stage2_body}
  {stage3_body}
  {stage4_body}

  <!-- ================= DIRECTIONAL ARROWS ================= -->
  {''.join(arrows_svg)}

  <!-- ================= FOOTER ================= -->
  <rect x="36" y="706" width="1528" height="36" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="728.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.4" font-weight="600" fill="#475569">Tim Asprak (Teknologi Informasi ITS &amp; Biologi UNJ)  |  Standar Cobb 500 &amp; Ross 308, 1 Model CV Feses Apache-2.0, Cuaca BMKG + Open-Meteo &amp; Pedoman WOAH</text>
</svg>
"""
    return svg


def main() -> None:
    os.makedirs(ASSETS_DIR, exist_ok=True)
    svg4a = build_svg_4a()
    with open(SVG_4A, "w", encoding="utf-8") as f:
        f.write(svg4a)
    render_svg_to_png(SVG_4A, PNG_4A, 1280, 840)

    svg4b = build_svg_4b()
    with open(SVG_4B, "w", encoding="utf-8") as f:
        f.write(svg4b)
    render_svg_to_png(SVG_4B, PNG_4B, 1600, 760)

    print(f"GENERATED 4A: {PNG_4A} ({os.path.getsize(PNG_4A)/1024:.1f} KB)")
    print(f"GENERATED 4B: {PNG_4B} ({os.path.getsize(PNG_4B)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
