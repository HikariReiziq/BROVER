#!/usr/bin/env python3
"""Generate publication-grade layperson-friendly SVG + high-res PNG architecture diagram for BROVER.

Design grounded in:
- C4 Model (Simon Brown): Level 1 System Context clarity with subtle Level 2 tech pill badges (Hybrid Opsi 1 + Opsi A)
- Paivio Dual Coding Theory & Mayer Multimedia Learning Principles: vector icons + concise plain-language phrases
- Elsevier / Springer Nature Graphical Abstract Guidelines: linear left-to-right flow (1 -> 2 -> 3 -> 4), clean whitespace
"""

import os
from html import escape
from playwright.sync_api import sync_playwright

BASE_DIR = "/home/reiziqzip/Programmer/Hackathon-UNJ/06_Project_Concept_BROVER"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SVG_PATH = os.path.join(ASSETS_DIR, "03_arsitektur_sistem_brover.svg")
PNG_PATH = os.path.join(ASSETS_DIR, "03_arsitektur_sistem_brover.png")

WIDTH = 1600
HEIGHT = 920


def pill(x: float, y: float, text: str, bg: str, fg: str, border: str = "none",
         font_size: float = 10.5, mono: bool = False, pad_x: float = 10, height: float = 24) -> tuple[str, float]:
    """Render a pill badge and return (svg_markup, total_width)."""
    char_w = font_size * (0.61 if mono else 0.56)
    w = max(44.0, len(text) * char_w + pad_x * 2)
    font_family = "'Source Code Pro', 'Liberation Mono', monospace" if mono else "'Open Sans', 'Noto Sans', sans-serif"
    stroke_attr = f'stroke="{border}" stroke-width="1"' if border != "none" else ""
    svg = (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{height:.1f}" rx="{height / 2:.1f}" '
        f'fill="{bg}" {stroke_attr}/>'
        f'<text x="{x + w / 2:.1f}" y="{y + height / 2 + font_size * 0.35:.1f}" '
        f'text-anchor="middle" font-family="{font_family}" font-size="{font_size}" '
        f'font-weight="600" fill="{fg}">{escape(text)}</text>'
    )
    return svg, w


def pill_row(start_x: float, y: float, items: list[str], bg: str, fg: str, border: str,
             font_size: float = 10.2, mono: bool = True, gap: float = 7.0) -> str:
    """Render a horizontal row of pill badges."""
    parts = []
    cx = start_x
    for item in items:
        markup, w = pill(cx, y, item, bg=bg, fg=fg, border=border, font_size=font_size, mono=mono, pad_x=9, height=23)
        parts.append(markup)
        cx += w + gap
    return "\n".join(parts)


def icon_rover(x: float, y: float) -> str:
    """Custom flat-vector 4WD BROVER inspection rover side-profile illustration (84x58)."""
    return f"""
    <g transform="translate({x},{y})">
      <!-- Ground line -->
      <line x1="2" y1="53" x2="82" y2="53" stroke="#99F6E4" stroke-width="2.2" stroke-linecap="round"/>
      <!-- Signal arcs above antenna -->
      <path d="M16 7 A10 10 0 0 1 28 7" fill="none" stroke="#0D9488" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M19 11 A6 6 0 0 1 25 11" fill="none" stroke="#0D9488" stroke-width="1.8" stroke-linecap="round"/>
      <!-- Antenna mast -->
      <line x1="22" y1="14" x2="22" y2="23" stroke="#0F766E" stroke-width="2.2" stroke-linecap="round"/>
      <!-- Main rover body -->
      <path d="M12 24 L54 24 L64 31 L64 41 L12 41 Z" fill="#CCFBF1" stroke="#0F766E" stroke-width="2.2" stroke-linejoin="round"/>
      <!-- Top stripe -->
      <rect x="16" y="27" width="32" height="5" rx="2.5" fill="#0D9488"/>
      <!-- Front tilted camera head -->
      <rect x="61" y="21" width="13" height="10" rx="2.5" fill="#0F172A" stroke="#0F172A" stroke-width="1.5"/>
      <circle cx="70.5" cy="26" r="2.8" fill="#38BDF8"/>
      <!-- Camera view cone -->
      <path d="M74 24 L83 18 L83 34 L74 28 Z" fill="#38BDF8" opacity="0.26"/>
      <!-- Under-body air sensor -->
      <rect x="35" y="41" width="10" height="4.5" rx="1.5" fill="#F59E0B"/>
      <!-- Rear & front rugged wheels -->
      <circle cx="22" cy="44" r="8.5" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
      <circle cx="22" cy="44" r="3.2" fill="#94A3B8"/>
      <circle cx="54" cy="44" r="8.5" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
      <circle cx="54" cy="44" r="3.2" fill="#94A3B8"/>
    </g>"""


def icon_camera(cx: float, cy: float, color: str = "#0F766E") -> str:
    return f"""
    <g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 8.5A2 2 0 0 1 5 6.5h2.2l1.4-2h6.8l1.4 2H19a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
      <circle cx="12" cy="13" r="3.6"/>
      <circle cx="17.5" cy="9.5" r="0.8" fill="{color}" stroke="none"/>
    </g>"""


def icon_mic(cx: float, cy: float, color: str = "#0F766E") -> str:
    return f"""
    <g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <rect x="7" y="3" width="6" height="10" rx="3"/>
      <path d="M4.5 11.5a5.5 5.5 0 0 0 11 0"/>
      <line x1="10" y1="17" x2="10" y2="21"/>
      <line x1="7" y1="21" x2="13" y2="21"/>
      <path d="M18 6.5a5 5 0 0 1 0 7"/>
      <path d="M20.5 4.5a8 8 0 0 1 0 11"/>
    </g>"""


def icon_thermo_air(cx: float, cy: float, color: str = "#0F766E") -> str:
    return f"""
    <g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8.5 13.8V5a2 2 0 0 0-4 0v8.8a3.6 3.6 0 1 0 4 0z"/>
      <circle cx="6.5" cy="16.8" r="1.4" fill="{color}" stroke="none"/>
      <path d="M13.5 7.5c1.5-1.2 3.2-1.2 4.5 0s3 1.2 4 0"/>
      <path d="M13.5 12c1.5-1.2 3.2-1.2 4.5 0s3 1.2 4 0"/>
      <path d="M13.5 16.5c1.5-1.2 3.2-1.2 4.5 0s3 1.2 4 0"/>
    </g>"""


def icon_ai_chip(cx: float, cy: float, color: str = "#6D28D9") -> str:
    return f"""
    <g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="6" y="6" width="12" height="12" rx="2.5"/>
      <path d="M9.5 14.5l1.6-5h1.8l1.6 5M10.1 13h3.8" stroke-width="1.6"/>
      <line x1="9" y1="2.5" x2="9" y2="6"/>
      <line x1="15" y1="2.5" x2="15" y2="6"/>
      <line x1="9" y1="18" x2="9" y2="21.5"/>
      <line x1="15" y1="18" x2="15" y2="21.5"/>
      <line x1="2.5" y1="9" x2="6" y2="9"/>
      <line x1="2.5" y1="15" x2="6" y2="15"/>
      <line x1="18" y1="9" x2="21.5" y2="9"/>
      <line x1="18" y1="15" x2="21.5" y2="15"/>
    </g>"""


def icon_shield_brake(cx: float, cy: float, color: str = "#047857") -> str:
    return f"""
    <g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3l7.5 3.2v5.4c0 4.8-3.2 8.2-7.5 9.6-4.3-1.4-7.5-4.8-7.5-9.6V6.2z"/>
      <path d="M8.8 12.2l2.2 2.2 4.4-4.6"/>
    </g>"""


def icon_wifi(cx: float, cy: float, color: str = "#0F766E") -> str:
    return f"""
    <g transform="translate({cx - 14},{cy - 14})" fill="none" stroke="{color}" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3.5 11.5a15 15 0 0 1 21 0"/>
      <path d="M7.2 15.6a10 10 0 0 1 13.6 0"/>
      <path d="M10.8 19.6a4.8 4.8 0 0 1 6.4 0"/>
      <circle cx="14" cy="23.2" r="1.8" fill="{color}" stroke="none"/>
    </g>"""


def icon_cloud_weather(cx: float, cy: float, color: str = "#1D4ED8") -> str:
    return f"""
    <g transform="translate({cx - 14},{cy - 14})" fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <!-- Subtle peeking sun -->
      <circle cx="20" cy="8.5" r="3" stroke="#F59E0B" fill="#FEF3C7"/>
      <line x1="20" y1="3" x2="20" y2="4.2" stroke="#F59E0B"/>
      <line x1="25.5" y1="8.5" x2="24.3" y2="8.5" stroke="#F59E0B"/>
      <line x1="23.9" y1="4.6" x2="23" y2="5.5" stroke="#F59E0B"/>
      <!-- Cloud body -->
      <path d="M7.5 22h12.2a4.3 4.3 0 0 0 .8-8.5 5.8 5.8 0 0 0-11.2-1.4A4.5 4.5 0 0 0 7.5 22z" fill="#EFF6FF"/>
      <!-- Upward sync arrow inside -->
      <line x1="13.5" y1="19.2" x2="13.5" y2="14"/>
      <path d="M11 16.2l2.5-2.5 2.5 2.5"/>
    </g>"""


def icon_devices(x: float, y: float) -> str:
    """Laptop + Smartphone flat-vector icon (74x54)."""
    return f"""
    <g transform="translate({x},{y})" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <!-- Laptop screen -->
      <rect x="4" y="6" width="50" height="33" rx="4" fill="#FFFBEB" stroke="#B45309" stroke-width="2.2"/>
      <!-- Screen mini dashboard widgets -->
      <rect x="9" y="11" width="18" height="10" rx="2" fill="#FDE68A"/>
      <rect x="30" y="11" width="19" height="10" rx="2" fill="#FED7AA"/>
      <rect x="9" y="24" width="40" height="10" rx="2" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>
      <path d="M13 31 L20 27 L27 30 L36 25.5 L44 28" stroke="#D97706" stroke-width="1.8"/>
      <!-- Laptop base -->
      <path d="M0 39 L58 39 L55 44 L3 44 Z" fill="#D97706"/>
      <!-- Smartphone overlapping bottom-right -->
      <rect x="48" y="18" width="21" height="33" rx="4" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2"/>
      <rect x="51.5" y="23" width="14" height="8" rx="1.5" fill="#10B981" opacity="0.28"/>
      <line x1="52" y1="35" x2="64" y2="35" stroke="#94A3B8" stroke-width="1.8"/>
      <line x1="52" y1="39.5" x2="61" y2="39.5" stroke="#CBD5E1" stroke-width="1.8"/>
      <circle cx="58.5" cy="46.5" r="1.4" fill="#0F172A"/>
    </g>"""


def icon_gauge(cx: float, cy: float, color: str = "#B45309") -> str:
    return f"""
    <g transform="translate({cx - 11},{cy - 11})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3.5 15.5a8.5 8.5 0 1 1 15 0"/>
      <line x1="11" y1="13" x2="15.5" y2="8.5"/>
      <circle cx="11" cy="13" r="1.6" fill="{color}"/>
      <line x1="6" y1="18" x2="16" y2="18"/>
    </g>"""


def icon_alert_scan(cx: float, cy: float, color: str = "#B45309") -> str:
    return f"""
    <g transform="translate({cx - 11},{cy - 11})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="10" cy="10" r="6.5"/>
      <line x1="14.8" y1="14.8" x2="19.5" y2="19.5"/>
      <line x1="10" y1="7" x2="10" y2="10.5"/>
      <circle cx="10" cy="13.2" r="0.9" fill="{color}" stroke="none"/>
    </g>"""


def icon_map_control(cx: float, cy: float, color: str = "#B45309") -> str:
    return f"""
    <g transform="translate({cx - 11},{cy - 11})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M11 2.8a6 6 0 0 1 6 6c0 4.4-6 10.4-6 10.4S5 13.2 5 8.8a6 6 0 0 1 6-6z"/>
      <circle cx="11" cy="8.8" r="2.2"/>
    </g>"""


def icon_clipboard(cx: float, cy: float, color: str = "#B45309") -> str:
    return f"""
    <g transform="translate({cx - 11},{cy - 11})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="4.5" y="4.5" width="13" height="15" rx="2"/>
      <path d="M8.5 3h5v3h-5z" fill="#FFFBEB"/>
      <path d="M8 12.2l2 2 4-4"/>
    </g>"""


def icon_farmer(cx: float, cy: float, color: str = "#047857") -> str:
    """Friendly modern caretaker / farmer bust with cap visor."""
    return f"""
    <g transform="translate({cx - 15},{cy - 15})" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <!-- Cap crown & visor -->
      <path d="M9.5 10.5c0-3.3 2.4-5.5 5.5-5.5s5.5 2.2 5.5 5.5z" fill="#A7F3D0"/>
      <line x1="7" y1="10.5" x2="23.5" y2="10.5"/>
      <!-- Head -->
      <path d="M10.5 10.8v1.2a4.5 4.5 0 0 0 9 0v-1.2" fill="#FFFFFF"/>
      <!-- Shoulders / collared shirt -->
      <path d="M6.2 25.5c.9-4.7 4.2-7.3 8.8-7.3s7.9 2.6 8.8 7.3" fill="#D1FAE5"/>
      <path d="M12.2 18.6l2.8 3.2 2.8-3.2"/>
    </g>"""


def icon_vet(cx: float, cy: float, color: str = "#BE123C") -> str:
    """Instantly recognizable veterinarian stethoscope icon."""
    return f"""
    <g transform="translate({cx - 15},{cy - 15})" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M7.5 5v5.8a5.5 5.5 0 0 0 11 0V5"/>
      <line x1="6" y1="5" x2="9" y2="5"/>
      <line x1="17" y1="5" x2="20" y2="5"/>
      <path d="M13 16.3v2.7a5 5 0 0 0 10 0v-2.2"/>
      <circle cx="23" cy="14.5" r="2.3" fill="#FFE4E6"/>
    </g>"""


def check_bullet(x: float, y: float, text: str, color: str, text_color: str = "#334155",
                 font_size: float = 12.0, second_line: str = "") -> str:
    """Clean check circle bullet with 1 or 2 crisp lines."""
    svg = (
        f'<circle cx="{x + 7}" cy="{y - 4}" r="6.5" fill="{color}" opacity="0.14"/>'
        f'<path d="M{x + 4.3} {y - 4} l1.9 2 3.5-3.8" fill="none" stroke="{color}" '
        f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<text x="{x + 21}" y="{y}" font-family="\'Open Sans\', \'Noto Sans\', sans-serif" '
        f'font-size="{font_size}" fill="{text_color}">{escape(text)}</text>'
    )
    if second_line:
        svg += (
            f'<text x="{x + 21}" y="{y + 16}" font-family="\'Open Sans\', \'Noto Sans\', sans-serif" '
            f'font-size="{font_size}" fill="{text_color}">{escape(second_line)}</text>'
        )
    return svg


def connector_arrow(x1: float, y: float, x2: float, color: str, label_top: str, label_bottom: str = "",
                    dashed: bool = False, bidir: bool = False, marker_end: str = "", marker_start: str = "") -> str:
    dash_attr = 'stroke-dasharray="6,4"' if dashed else ""
    m_end = f'marker-end="url(#{marker_end})"' if marker_end else ""
    m_start = f'marker-start="url(#{marker_start})"' if (bidir and marker_start) else ""
    mx = (x1 + x2) / 2
    parts = [
        f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" '
        f'stroke="{color}" stroke-width="2.6" {dash_attr} {m_end} {m_start}/>'
    ]
    if label_top:
        ly = y - (24 if label_bottom else 12)
        parts.append(
            f'<text x="{mx:.1f}" y="{ly:.1f}" text-anchor="middle" '
            f'font-family="\'Open Sans\', \'Noto Sans\', sans-serif" font-size="10.2" '
            f'font-weight="700" fill="{color}">{escape(label_top)}</text>'
        )
    if label_bottom:
        parts.append(
            f'<text x="{mx:.1f}" y="{y - 10:.1f}" text-anchor="middle" '
            f'font-family="\'Open Sans\', \'Noto Sans\', sans-serif" font-size="10.2" '
            f'font-weight="700" fill="{color}">{escape(label_bottom)}</text>'
        )
    return "\n".join(parts)


def build_svg() -> str:
    # Column coordinates (1600px width, 36px margins, 3 gaps of 66px)
    z1_x, z1_w = 36, 376    # 36..412
    z2_x, z2_w = 478, 324   # 478..802
    z3_x, z3_w = 868, 330   # 868..1198
    z4_x, z4_w = 1264, 300  # 1264..1564

    zone_y = 118
    zone_h = 720
    hdr_h = 54

    # Zone 1 sub-cards
    z1_in_x = z1_x + 16
    z1_in_w = z1_w - 32  # 344

    # Zone 2 sub-cards
    z2_in_x = z2_x + 16
    z2_in_w = z2_w - 32  # 292

    # Zone 3 sub-cards
    z3_in_x = z3_x + 16
    z3_in_w = z3_w - 32  # 298

    # Zone 4 sub-cards
    z4_in_x = z4_x + 16
    z4_in_w = z4_w - 32  # 268

    # Sensor rows in Zone 1
    sensor_specs = [
        (296, "Kamera AI (Depan)", "Pindai gejala pada feses & fisik ayam", icon_camera),
        (386, "Mikrofon Pernapasan (15 dtk)", "Rekam 3×5 dtk saat motor berhenti", icon_mic),
        (476, "Sensor Udara di Tinggi Ayam", "Ukur suhu, kelembapan & tren gas NH₃", icon_thermo_air),
    ]
    sensor_cards_svg = []
    for sy, stitle, sdesc, sicon_fn in sensor_specs:
        sensor_cards_svg.append(f"""
        <rect x="{z1_in_x}" y="{sy}" width="{z1_in_w}" height="78" rx="13" fill="#FFFFFF" stroke="#99F6E4" stroke-width="1.4" filter="url(#cardShadow)"/>
        <circle cx="{z1_in_x + 31}" cy="{sy + 39}" r="21" fill="#CCFBF1"/>
        {sicon_fn(z1_in_x + 31, sy + 39, "#0F766E")}
        <text x="{z1_in_x + 64}" y="{sy + 33}" font-family="'Montserrat', 'Open Sans', sans-serif" font-size="13" font-weight="700" fill="#0F172A">{escape(stitle)}</text>
        <text x="{z1_in_x + 64}" y="{sy + 54}" font-family="'Open Sans', 'Noto Sans', sans-serif" font-size="11.6" fill="#475569">{escape(sdesc)}</text>
        """)

    # Dashboard 4 panels in Zone 3
    panel_specs = [
        (296, "1. Udara vs Umur Ayam", "Status dingin, ideal, atau panas", "sesuai umur broiler + NH₃ & cuaca luar", icon_gauge),
        (416, "2. Temuan AI + 3 Tombol", "Foto feses/ayam & klip audio ngorok", "Pilih: Akan Dicek / Normal / Lapor", icon_alert_scan),
        (536, "3. Kendali Rover via Website", "Gerakkan Rover lewat browser HP,", "video langsung & peta Zona A, B, C, D", icon_map_control),
        (656, "4. Catatan ABK & Sanitasi", "Catat deplesi/FCR harian, panduan", "sanitasi roda & Laporan 1-Klik", icon_clipboard),
    ]
    panel_cards_svg = []
    for py, ptitle, pl1, pl2, picon_fn in panel_specs:
        panel_cards_svg.append(f"""
        <rect x="{z3_in_x}" y="{py}" width="{z3_in_w}" height="108" rx="13" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.4" filter="url(#cardShadow)"/>
        <circle cx="{z3_in_x + 29}" cy="{py + 54}" r="20" fill="#FEF3C7"/>
        {picon_fn(z3_in_x + 29, py + 54, "#B45309")}
        <text x="{z3_in_x + 60}" y="{py + 34}" font-family="'Montserrat', 'Open Sans', sans-serif" font-size="12.8" font-weight="700" fill="#0F172A">{escape(ptitle)}</text>
        <text x="{z3_in_x + 60}" y="{py + 56}" font-family="'Open Sans', 'Noto Sans', sans-serif" font-size="11.5" fill="#475569">{escape(pl1)}</text>
        <text x="{z3_in_x + 60}" y="{py + 74}" font-family="'Open Sans', 'Noto Sans', sans-serif" font-size="11.5" fill="#475569">{escape(pl2)}</text>
        """)

    # Tech stack footer pills (Opsi 1: subtle badges at bottom of each zone)
    z1_pills = pill_row(z1_in_x, 798, ["RPi 4 / Orange Pi 3B", "ESP32", "SHT31 & SEN0567"],
                        bg="#FFFFFF", fg="#0F766E", border="#5EEAD4", font_size=9.8, mono=True, gap=6)
    z2_pills = pill_row(z2_in_x, 798, ["Golang", "PostgreSQL", "BMKG + Open-Meteo"],
                        bg="#FFFFFF", fg="#1D4ED8", border="#93C5FD", font_size=9.5, mono=True, gap=5.5)
    z3_pills = pill_row(z3_in_x, 798, ["Next.js PWA", "Cobb 500 & Ross 308"],
                        bg="#FFFFFF", fg="#B45309", border="#FCD34D", font_size=9.7, mono=True, gap=7)
    z4_pills = pill_row(z4_in_x, 798, ["Human-in-the-Loop", "Deteksi Dini"],
                        bg="#FFFFFF", fg="#334155", border="#CBD5E1", font_size=10.0, mono=False, gap=8)

    # Small status badges inside Zone 2 cards
    offline_pill, _ = pill(z2_in_x + z2_in_w - 94, 200, "OFFLINE OK", bg="#DCFCE7", fg="#166534", border="#86EFAC", font_size=9.2, mono=False, pad_x=8, height=21)
    autosync_pill, _ = pill(z2_in_x + z2_in_w - 92, 512, "AUTO-SYNC", bg="#DBEAFE", fg="#1E40AF", border="#93C5FD", font_size=9.2, mono=False, pad_x=8, height=21)

    # Role pills inside Zone 4 cards
    farmer_pill, _ = pill(z4_in_x + 76, 232, "Aksi Cepat di Kandang", bg="#DCFCE7", fg="#166534", border="none", font_size=10.0, mono=False, pad_x=8, height=21)
    vet_pill, _ = pill(z4_in_x + 76, 502, "Eskalasi Klinis 1-Klik", bg="#FFE4E6", fg="#9F1239", border="none", font_size=10.0, mono=False, pad_x=8, height=21)

    # Arrows between zones
    arrows_svg = "\n".join([
        # Zone 1 -> Zone 2A (Wi-Fi Lokal)
        connector_arrow(z1_x + z1_w + 4, 320, z2_x - 4, "#0D9488", "Wi-Fi", "Nirkabel",
                        dashed=False, bidir=False, marker_end="arrowTeal"),
        # Zone 1 -> Zone 2B (Cloud Auto-Sync)
        connector_arrow(z1_x + z1_w + 4, 635, z2_x - 4, "#2563EB", "Auto-Sync", "(Internet)",
                        dashed=True, bidir=False, marker_end="arrowBlue"),
        # Zone 2A <-> Zone 3 (Bidirectional Live Video & Rover Control)
        connector_arrow(z2_x + z2_w + 6, 320, z3_x - 6, "#0D9488", "Kendali &", "Video",
                        dashed=False, bidir=True, marker_end="arrowTeal", marker_start="arrowTealStart"),
        # Zone 2B -> Zone 3 (Data & Alerts)
        connector_arrow(z2_x + z2_w + 4, 635, z3_x - 4, "#2563EB", "Data &", "Peringatan",
                        dashed=False, bidir=False, marker_end="arrowBlue"),
        # Zone 3 <-> Zone 4A (Farmer Action & Control)
        connector_arrow(z3_x + z3_w + 6, 312, z4_x - 6, "#059669", "Pantau &", "Aksi",
                        dashed=False, bidir=True, marker_end="arrowEmerald", marker_start="arrowEmeraldStart"),
        # Zone 3 -> Zone 4B (1-Click Vet Report)
        connector_arrow(z3_x + z3_w + 4, 582, z4_x - 4, "#E11D48", "Laporan", "1-Klik",
                        dashed=False, bidir=False, marker_end="arrowRose"),
    ])

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <filter id="cardShadow" x="-4%" y="-4%" width="108%" height="112%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="zoneShadow" x="-2%" y="-2%" width="104%" height="105%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.05"/>
    </filter>

    <!-- Arrowhead markers -->
    <marker id="arrowTeal" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#0D9488"/>
    </marker>
    <marker id="arrowTealStart" viewBox="0 0 10 10" refX="1.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 10 1.2 L 1 5 L 10 8.8 z" fill="#0D9488"/>
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#2563EB"/>
    </marker>
    <marker id="arrowEmerald" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#059669"/>
    </marker>
    <marker id="arrowEmeraldStart" viewBox="0 0 10 10" refX="1.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 10 1.2 L 1 5 L 10 8.8 z" fill="#059669"/>
    </marker>
    <marker id="arrowRose" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
      <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#E11D48"/>
    </marker>
    <marker id="arrowMutedDown" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8.5 5 L 0 8.5 z" fill="#3B82F6"/>
    </marker>
  </defs>

  <!-- Crisp White Background -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#FFFFFF"/>

  <!-- ================= HEADER ================= -->
  <rect x="556" y="16" width="488" height="24" rx="12" fill="#CCFBF1"/>
  <text x="800" y="32" text-anchor="middle" font-family="'Montserrat', 'Open Sans', sans-serif" font-size="10.5" font-weight="700" letter-spacing="0.7" fill="#0F766E">ARSITEKTUR SISTEM BROVER: MULTI-MODAL AI &amp; EDGE-CLOUD</text>
  <text x="800" y="70" text-anchor="middle" font-family="'Montserrat', 'Open Sans', sans-serif" font-size="25.5" font-weight="800" fill="#0F172A">Cara Kerja Sistem Inspeksi Kandang Ayam Broiler</text>
  <text x="800" y="96" text-anchor="middle" font-family="'Open Sans', 'Noto Sans', sans-serif" font-size="13.8" fill="#475569">Alur dari Rover di dalam kandang hingga tindakan cepat Peternak &amp; Dokter Hewan (tetap berjalan saat internet kandang mati)</text>

  <!-- ================= ZONE 1: ROVER DI KANDANG ================= -->
  <g filter="url(#zoneShadow)">
    <rect x="{z1_x}" y="{zone_y}" width="{z1_w}" height="{zone_h}" rx="18" fill="#F0FDFA" stroke="#5EEAD4" stroke-width="1.8"/>
    <path d="M{z1_x + 18} {zone_y} H{z1_x + z1_w - 18} Q{z1_x + z1_w} {zone_y} {z1_x + z1_w} {zone_y + 18} V{zone_y + hdr_h} H{z1_x} V{zone_y + 18} Q{z1_x} {zone_y} {z1_x + 18} {zone_y} Z" fill="#0D9488"/>
  </g>
  <circle cx="{z1_x + 28}" cy="{zone_y + 27}" r="14" fill="#FFFFFF"/>
  <text x="{z1_x + 28}" y="{zone_y + 32}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#0F766E">1</text>
  <text x="{z1_x + 52}" y="{zone_y + 25}" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">ROVER DI KANDANG</text>
  <text x="{z1_x + 52}" y="{zone_y + 42}" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#CCFBF1">1 Unit = 1 Kandang | Bebas kabel fisik</text>

  <!-- Zone 1 Rover Hero Card -->
  <rect x="{z1_in_x}" y="186" width="{z1_in_w}" height="96" rx="14" fill="#FFFFFF" stroke="#5EEAD4" stroke-width="1.5" filter="url(#cardShadow)"/>
  {icon_rover(z1_in_x + 12, 205)}
  <text x="{z1_in_x + 108}" y="216" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="700" fill="#0F172A">Rover Inspeksi Beroda</text>
  <text x="{z1_in_x + 108}" y="236" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">Gerak pelan (&#8804;0,1 m/s) menyusuri</text>
  <text x="{z1_in_x + 108}" y="253" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">lorong agar ayam tetap tenang</text>
  <rect x="{z1_in_x + 108}" y="260" width="168" height="17" rx="8.5" fill="#F0FDFA" stroke="#99F6E4" stroke-width="0.9"/>
  <text x="{z1_in_x + 192}" y="272" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.6" font-weight="600" fill="#0F766E">Jangkau hampir seluruh flok</text>

  <!-- Zone 1 Three Sensor Cards -->
  {''.join(sensor_cards_svg)}

  <!-- Zone 1 Local AI Brain + Auto Safety Brake Card -->
  <rect x="{z1_in_x}" y="570" width="{z1_in_w}" height="198" rx="14" fill="#FFFFFF" stroke="#A78BFA" stroke-width="1.6" filter="url(#cardShadow)"/>
  <!-- Row A: Local AI -->
  <circle cx="{z1_in_x + 31}" cy="609" r="21" fill="#EDE9FE"/>
  {icon_ai_chip(z1_in_x + 31, 609, "#6D28D9")}
  <text x="{z1_in_x + 64}" y="603" font-family="'Montserrat', sans-serif" font-size="13" font-weight="700" fill="#4C1D95">Otak AI Lokal (Offline-First)</text>
  <text x="{z1_in_x + 64}" y="622" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">Proses 3 model AI langsung di Rover</text>
  <text x="{z1_in_x + 64}" y="638" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">tanpa bergantung sinyal internet</text>

  <line x1="{z1_in_x + 16}" y1="655" x2="{z1_in_x + z1_in_w - 16}" y2="655" stroke="#E2E8F0" stroke-width="1.2"/>

  <!-- Row B: Safety Brake -->
  <circle cx="{z1_in_x + 31}" cy="693" r="21" fill="#D1FAE5"/>
  {icon_shield_brake(z1_in_x + 31, 693, "#047857")}
  <text x="{z1_in_x + 64}" y="687" font-family="'Montserrat', sans-serif" font-size="13" font-weight="700" fill="#065F46">Rem Aman Otomatis (500 ms)</text>
  <text x="{z1_in_x + 64}" y="706" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">Stop mendadak jika sinyal putus</text>
  <text x="{z1_in_x + 64}" y="722" font-family="'Open Sans', sans-serif" font-size="11.5" fill="#475569">atau sensor deteksi halangan depan</text>

  <!-- Transparency note inside Zone 1 -->
  <rect x="{z1_in_x + 12}" y="736" width="{z1_in_w - 24}" height="24" rx="7" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{z1_in_x + z1_in_w / 2}" y="751.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" font-weight="600" fill="#475569">Kini: kendali lewat Website | Future Work: otomatis terjadwal</text>

  <!-- Zone 1 Tech Pills -->
  <text x="{z1_in_x}" y="786" font-family="'Open Sans', sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.4" fill="#0F766E">PERANGKAT INTI:</text>
  {z1_pills}

  <!-- ================= ZONE 2: KONEKSI & SERVER ================= -->
  <g filter="url(#zoneShadow)">
    <rect x="{z2_x}" y="{zone_y}" width="{z2_w}" height="{zone_h}" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.8"/>
    <path d="M{z2_x + 18} {zone_y} H{z2_x + z2_w - 18} Q{z2_x + z2_w} {zone_y} {z2_x + z2_w} {zone_y + 18} V{zone_y + hdr_h} H{z2_x} V{zone_y + 18} Q{z2_x} {zone_y} {z2_x + 18} {zone_y} Z" fill="#2563EB"/>
  </g>
  <circle cx="{z2_x + 28}" cy="{zone_y + 27}" r="14" fill="#FFFFFF"/>
  <text x="{z2_x + 28}" y="{zone_y + 32}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#1D4ED8">2</text>
  <text x="{z2_x + 52}" y="{zone_y + 25}" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">KONEKSI &amp; SERVER</text>
  <text x="{z2_x + 52}" y="{zone_y + 42}" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#DBEAFE">Jalur lokal nirkabel + sinkron Cloud</text>

  <!-- Zone 2A: Wi-Fi Lokal Nirkabel -->
  <rect x="{z2_in_x}" y="186" width="{z2_in_w}" height="262" rx="14" fill="#FFFFFF" stroke="#2DD4BF" stroke-width="1.8" filter="url(#cardShadow)"/>
  <circle cx="{z2_in_x + 34}" cy="224" r="24" fill="#CCFBF1"/>
  {icon_wifi(z2_in_x + 34, 224, "#0F766E")}
  {offline_pill}
  <text x="{z2_in_x + 68}" y="224" font-family="'Montserrat', sans-serif" font-size="14" font-weight="700" fill="#0F172A">Wi-Fi Lokal</text>
  <text x="{z2_in_x + 68}" y="243" font-family="'Montserrat', sans-serif" font-size="14" font-weight="700" fill="#0F766E">Nirkabel</text>
  <text x="{z2_in_x + 16}" y="276" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="600" fill="#475569">Jalur langsung Rover ke HP/Laptop:</text>
  {check_bullet(z2_in_x + 16, 305, "Kendali Rover & video langsung", "#0D9488", font_size=11.6, second_line="100% tanpa kabel di lantai kandang")}
  {check_bullet(z2_in_x + 16, 354, "Tetap beroperasi penuh meski", "#0D9488", font_size=11.6, second_line="sinyal internet kandang mati total")}
  {check_bullet(z2_in_x + 16, 403, "Simpan data sementara di Rover", "#0D9488", font_size=11.6, second_line="hingga lebih dari 30 hari (SQLite)")}

  <!-- Bridge indicator between 2A and 2B -->
  <line x1="{z2_x + z2_w / 2}" y1="449" x2="{z2_x + z2_w / 2}" y2="493" stroke="#3B82F6" stroke-width="2" stroke-dasharray="4,3" marker-end="url(#arrowMutedDown)"/>
  <rect x="{z2_in_x + 28}" y="456" width="{z2_in_w - 56}" height="22" rx="11" fill="#DBEAFE" stroke="#93C5FD" stroke-width="1"/>
  <text x="{z2_x + z2_w / 2}" y="470.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="10.2" font-weight="700" fill="#1E40AF">Sinkron otomatis saat internet aktif</text>

  <!-- Zone 2B: Server Pusat (Cloud) -->
  <rect x="{z2_in_x}" y="498" width="{z2_in_w}" height="270" rx="14" fill="#FFFFFF" stroke="#60A5FA" stroke-width="1.8" filter="url(#cardShadow)"/>
  <circle cx="{z2_in_x + 34}" cy="536" r="24" fill="#DBEAFE"/>
  {icon_cloud_weather(z2_in_x + 34, 536, "#1D4ED8")}
  {autosync_pill}
  <text x="{z2_in_x + 68}" y="536" font-family="'Montserrat', sans-serif" font-size="14" font-weight="700" fill="#0F172A">Server Pusat</text>
  <text x="{z2_in_x + 68}" y="555" font-family="'Montserrat', sans-serif" font-size="14" font-weight="700" fill="#1D4ED8">&amp; Data Cuaca</text>
  <text x="{z2_in_x + 16}" y="588" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="600" fill="#475569">Analisis standar umur &amp; cuaca luar:</text>
  {check_bullet(z2_in_x + 16, 617, "Bandingkan suhu-RH otomatis", "#2563EB", font_size=11.5, second_line="standar broiler Cobb 500 / Ross 308")}
  {check_bullet(z2_in_x + 16, 666, "Cuaca luar (BMKG + Open-Meteo)", "#2563EB", font_size=11.5, second_line="cegah cekaman panas 1-7 hari")}
  {check_bullet(z2_in_x + 16, 715, "Susun arsip foto/audio ngorok &", "#2563EB", font_size=11.5, second_line="paket Laporan 1-Klik Dokter Hewan")}

  <!-- Zone 2 Tech Pills -->
  <text x="{z2_in_x}" y="786" font-family="'Open Sans', sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.4" fill="#1D4ED8">BACKEND &amp; DATA:</text>
  {z2_pills}

  <!-- ================= ZONE 3: DASBOR APLIKASI ================= -->
  <g filter="url(#zoneShadow)">
    <rect x="{z3_x}" y="{zone_y}" width="{z3_w}" height="{zone_h}" rx="18" fill="#FFFBEB" stroke="#FCD34D" stroke-width="1.8"/>
    <path d="M{z3_x + 18} {zone_y} H{z3_x + z3_w - 18} Q{z3_x + z3_w} {zone_y} {z3_x + z3_w} {zone_y + 18} V{zone_y + hdr_h} H{z3_x} V{zone_y + 18} Q{z3_x} {zone_y} {z3_x + 18} {zone_y} Z" fill="#D97706"/>
  </g>
  <circle cx="{z3_x + 28}" cy="{zone_y + 27}" r="14" fill="#FFFFFF"/>
  <text x="{z3_x + 28}" y="{zone_y + 32}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#B45309">3</text>
  <text x="{z3_x + 52}" y="{zone_y + 25}" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">DASBOR APLIKASI</text>
  <text x="{z3_x + 52}" y="{zone_y + 42}" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#FEF3C7">Tampilan jelas di HP &amp; Laptop</text>

  <!-- Zone 3 Device Hero Card -->
  <rect x="{z3_in_x}" y="186" width="{z3_in_w}" height="96" rx="14" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.5" filter="url(#cardShadow)"/>
  {icon_devices(z3_in_x + 14, 208)}
  <text x="{z3_in_x + 98}" y="218" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="700" fill="#0F172A">Web Aplikasi (PWA)</text>
  <text x="{z3_in_x + 98}" y="238" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#475569">Buka langsung dari browser</text>
  <text x="{z3_in_x + 98}" y="255" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#475569">HP Android maupun Laptop,</text>
  <text x="{z3_in_x + 98}" y="271" font-family="'Open Sans', sans-serif" font-size="11.4" font-weight="600" fill="#B45309">ringan di sinyal pedesaan</text>

  <!-- Zone 3 Four Dashboard Panel Cards -->
  {''.join(panel_cards_svg)}

  <!-- Zone 3 Tech Pills -->
  <text x="{z3_in_x}" y="786" font-family="'Open Sans', sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.4" fill="#B45309">ANTARMUKA &amp; ACUAN:</text>
  {z3_pills}

  <!-- ================= ZONE 4: TINDAKAN NYATA ================= -->
  <g filter="url(#zoneShadow)">
    <rect x="{z4_x}" y="{zone_y}" width="{z4_w}" height="{zone_h}" rx="18" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.8"/>
    <path d="M{z4_x + 18} {zone_y} H{z4_x + z4_w - 18} Q{z4_x + z4_w} {zone_y} {z4_x + z4_w} {zone_y + 18} V{zone_y + hdr_h} H{z4_x} V{zone_y + 18} Q{z4_x} {zone_y} {z4_x + 18} {zone_y} Z" fill="#1E293B"/>
  </g>
  <circle cx="{z4_x + 28}" cy="{zone_y + 27}" r="14" fill="#FFFFFF"/>
  <text x="{z4_x + 28}" y="{zone_y + 32}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#1E293B">4</text>
  <text x="{z4_x + 52}" y="{zone_y + 25}" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">TINDAKAN NYATA</text>
  <text x="{z4_x + 52}" y="{zone_y + 42}" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#CBD5E1">Pengguna utama &amp; manfaat</text>

  <!-- Zone 4A: Peternak / ABK -->
  <rect x="{z4_in_x}" y="186" width="{z4_in_w}" height="252" rx="14" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="1.8" filter="url(#cardShadow)"/>
  <circle cx="{z4_in_x + 38}" cy="227" r="25" fill="#D1FAE5"/>
  {icon_farmer(z4_in_x + 38, 227, "#047857")}
  <text x="{z4_in_x + 76}" y="222" font-family="'Montserrat', sans-serif" font-size="14" font-weight="700" fill="#0F172A">Peternak / ABK</text>
  {farmer_pill}
  {check_bullet(z4_in_x + 14, 286, "Langsung cek ayam sakit di", "#059669", font_size=11.5, second_line="zona temuan lebih awal")}
  {check_bullet(z4_in_x + 14, 336, "Atur kipas/tirai sebelum", "#059669", font_size=11.5, second_line="panas kandang memuncak")}
  {check_bullet(z4_in_x + 14, 386, "Kendalikan Rover lewat website", "#059669", font_size=11.5, second_line="& jalankan sanitasi roda di dock")}

  <!-- Zone 4B: Dokter Hewan / Dinas -->
  <rect x="{z4_in_x}" y="456" width="{z4_in_w}" height="248" rx="14" fill="#FFFFFF" stroke="#FDA4AF" stroke-width="1.8" filter="url(#cardShadow)"/>
  <circle cx="{z4_in_x + 38}" cy="497" r="25" fill="#FFE4E6"/>
  {icon_vet(z4_in_x + 38, 497, "#BE123C")}
  <text x="{z4_in_x + 76}" y="492" font-family="'Montserrat', sans-serif" font-size="12.8" font-weight="700" fill="#0F172A">Dokter Hewan / Dinas</text>
  {vet_pill}
  {check_bullet(z4_in_x + 14, 556, "Terima Laporan 1-Klik", "#E11D48", font_size=11.5, second_line="via WhatsApp atau PDF")}
  {check_bullet(z4_in_x + 14, 606, "Isi lengkap: foto, klip audio,", "#E11D48", font_size=11.5, second_line="grafik suhu/NH₃ & umur flok")}
  {check_bullet(z4_in_x + 14, 656, "Diagnosis klinis & terapi", "#E11D48", font_size=11.5, second_line="jauh lebih cepat & akurat")}

  <!-- Human-in-the-Loop Reassurance Banner -->
  <rect x="{z4_in_x}" y="716" width="{z4_in_w}" height="52" rx="12" fill="#EEF2FF" stroke="#A5B4FC" stroke-width="1.4"/>
  {icon_shield_brake(z4_in_x + 24, 742, "#4338CA")}
  <text x="{z4_in_x + 44}" y="737" font-family="'Montserrat', sans-serif" font-size="11.2" font-weight="700" fill="#312E81">Manusia Penentu Akhir</text>
  <text x="{z4_in_x + 44}" y="754" font-family="'Open Sans', sans-serif" font-size="10.2" fill="#4338CA">AI = skrining awal, bukan diagnosis</text>

  <!-- Zone 4 Footer Pills -->
  <text x="{z4_in_x}" y="786" font-family="'Open Sans', sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.4" fill="#334155">PRINSIP KLINIS:</text>
  {z4_pills}

  <!-- ================= CONNECTING ARROWS ================= -->
  {arrows_svg}

  <!-- ================= BOTTOM ATTRIBUTION FOOTER ================= -->
  <rect x="36" y="856" width="1528" height="44" rx="12" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1.2"/>
  <text x="800" y="882.5" text-anchor="middle" font-family="'Open Sans', 'Noto Sans', sans-serif" font-size="11.3" font-weight="600" fill="#475569">Tim Asprak (Teknologi Informasi ITS &amp; Biologi UNJ)  |  Multi-Modal AI, Kendali Website via Wi-Fi Lokal, Cuaca BMKG + Open-Meteo &amp; Standar Cobb 500 / Ross 308</text>
</svg>
"""
    return svg


def render_png(svg_path: str, png_path: str) -> None:
    """Render SVG to ultra-crisp 2x PNG (3200x1840 px) via local Playwright Chromium."""
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
    width: {WIDTH}px;
    height: {HEIGHT}px;
    background: #FFFFFF;
    overflow: hidden;
  }}
  svg {{
    display: block;
    width: {WIDTH}px;
    height: {HEIGHT}px;
  }}
</style>
</head>
<body>{svg_content}</body>
</html>"""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, device_scale_factor=2)
        page.set_content(html, wait_until="load")
        page.screenshot(path=png_path, full_page=False)
        browser.close()


def main() -> None:
    os.makedirs(ASSETS_DIR, exist_ok=True)
    svg = build_svg()
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    render_png(SVG_PATH, PNG_PATH)
    svg_kb = os.path.getsize(SVG_PATH) / 1024
    png_kb = os.path.getsize(PNG_PATH) / 1024
    print(f"GENERATED SVG: {SVG_PATH} ({svg_kb:.1f} KB)")
    print(f"RENDERED PNG:  {PNG_PATH} ({png_kb:.1f} KB)")


if __name__ == "__main__":
    main()
