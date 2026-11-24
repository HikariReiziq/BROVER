#!/usr/bin/env python3
"""Generate 5 layperson-friendly, publication-grade vector SVG + high-res PNG visuals for BROVER:
- 04c_user_flow_brover.svg / .png              : 3-swimlane User Flow (Peternak, Website+Rover, Dokter Hewan)
- 06_roadmap_tkt_dan_evolusi_brover.svg / .png : Ascending Staircase TKT Roadmap (Permenristekdikti 42/2016 + peer-reviewed)
- 07_business_model_canvas_brover.svg / .png   : Clean 9-block Osterwalder BMC (100% RI, All-In Opsi 2, jargon-free)
- 08_project_timeline_brover.svg / .png        : Clean 10-month Gantt Timeline (2026/2027 strip, Nov-Agu, W1-W4, 1-line tasks)
- 09_proyeksi_keuntungan_5tahun_brover.svg/.png: Clean 5-year Investor Profit Projection (With vs Without BROVER)

All SVGs are 100% self-contained, zero em-dashes, zero double-escapes, zero Alibaba, rendered at 2x scale via Playwright Chromium.
"""

import os
from html import escape
from playwright.sync_api import sync_playwright

BASE_DIR = "/home/reiziqzip/Programmer/Hackathon-UNJ/06_Project_Concept_BROVER"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SVG_4C = os.path.join(ASSETS_DIR, "04c_user_flow_brover.svg")
PNG_4C = os.path.join(ASSETS_DIR, "04c_user_flow_brover.png")
SVG_06 = os.path.join(ASSETS_DIR, "06_roadmap_tkt_dan_evolusi_brover.svg")
PNG_06 = os.path.join(ASSETS_DIR, "06_roadmap_tkt_dan_evolusi_brover.png")
SVG_07 = os.path.join(ASSETS_DIR, "07_business_model_canvas_brover.svg")
PNG_07 = os.path.join(ASSETS_DIR, "07_business_model_canvas_brover.png")
SVG_08 = os.path.join(ASSETS_DIR, "08_project_timeline_brover.svg")
PNG_08 = os.path.join(ASSETS_DIR, "08_project_timeline_brover.png")
SVG_09 = os.path.join(ASSETS_DIR, "09_proyeksi_keuntungan_5tahun_brover.svg")
PNG_09 = os.path.join(ASSETS_DIR, "09_proyeksi_keuntungan_5tahun_brover.png")


def render_svg(svg_path: str, png_path: str, width: int, height: int) -> None:
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  html, body {{
    margin: 0; padding: 0;
    width: {width}px; height: {height}px;
    background: #FFFFFF; overflow: hidden;
  }}
  svg {{ display: block; width: {width}px; height: {height}px; }}
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
# SHARED VECTOR ICONS
# ==============================================================================
def ic_farmer(cx: float, cy: float, col: str = "#047857") -> str:
    return f"""<g transform="translate({cx - 14},{cy - 14})" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 10c0-3 2.2-5 5-5s5 2 5 5z" fill="#A7F3D0"/>
      <line x1="6.5" y1="10" x2="21.5" y2="10"/>
      <path d="M10 10.5v1a4 4 0 0 0 8 0v-1" fill="#FFFFFF"/>
      <path d="M6 24c.8-4.5 3.8-6.8 8-6.8s7.2 2.3 8 6.8" fill="#D1FAE5"/>
    </g>"""


def ic_rover_web(cx: float, cy: float, col: str = "#1D4ED8") -> str:
    return f"""<g transform="translate({cx - 14},{cy - 14})" fill="none" stroke="{col}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="5" width="22" height="14" rx="2.5" fill="#DBEAFE"/>
      <line x1="8" y1="23" x2="20" y2="23"/>
      <line x1="14" y1="19" x2="14" y2="23"/>
      <circle cx="14" cy="12" r="3" fill="#2563EB" stroke="none"/>
    </g>"""


def ic_vet(cx: float, cy: float, col: str = "#BE123C") -> str:
    return f"""<g transform="translate({cx - 14},{cy - 14})" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M7 4.5v5.5a5 5 0 0 0 10 0V4.5"/>
      <line x1="5.5" y1="4.5" x2="8.5" y2="4.5"/>
      <line x1="15.5" y1="4.5" x2="18.5" y2="4.5"/>
      <path d="M12 15v2.5a4.5 4.5 0 0 0 9 0v-2"/>
      <circle cx="21" cy="13.8" r="2.2" fill="#FFE4E6"/>
    </g>"""


def ic_handshake(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M2 11l4-4 4 2 4-2 4 4"/>
      <path d="M6 15l3 3 3-2 3 2 5-5"/>
      <path d="M2 11l4 4"/>
    </g>"""


def ic_checklist(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/>
      <path d="M8.5 12.2l2.4 2.4 4.8-5"/>
    </g>"""


def ic_layers(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <polygon points="12 3 21 7.8 12 12.6 3 7.8 12 3"/>
      <polyline points="3 12.6 12 17.4 21 12.6"/>
      <polyline points="3 17.2 12 22 21 17.2"/>
    </g>"""


def ic_bulb(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 18h6M10 21h4"/>
      <path d="M12 3a6.5 6.5 0 0 0-4.2 11.4c.7.6 1.2 1.5 1.2 2.6h6c0-1.1.5-2 1.2-2.6A6.5 6.5 0 0 0 12 3z"/>
    </g>"""


def ic_chat(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M21 11.5a8.5 8.5 0 0 1-12.3 7.6L3 20.5l1.5-5.3A8.5 8.5 0 1 1 21 11.5z"/>
    </g>"""


def ic_truck(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="2" y="6" width="13" height="10" rx="1.5"/>
      <path d="M15 9h4l3 3.5V16h-7z"/>
      <circle cx="6.5" cy="18" r="2"/>
      <circle cx="18" cy="18" r="2"/>
    </g>"""


def ic_users(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="9.5" cy="8.5" r="3.5"/>
      <path d="M3 19.5c.8-3.8 3.2-5.5 6.5-5.5s5.7 1.7 6.5 5.5"/>
      <circle cx="17" cy="9.5" r="2.5"/>
      <path d="M16.5 14.3c2.3.4 4 1.9 4.5 5.2"/>
    </g>"""


def ic_receipt(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 3h14v18l-2.5-1.8L14 21l-2-1.8L10 21l-2.5-1.8L5 21z"/>
      <line x1="8.5" y1="8.5" x2="15.5" y2="8.5"/>
      <line x1="8.5" y1="12.5" x2="15.5" y2="12.5"/>
      <line x1="8.5" y1="16" x2="12.5" y2="16"/>
    </g>"""


def ic_coin(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/>
      <path d="M14.8 9.2c-.5-1-1.5-1.5-2.8-1.5-1.6 0-2.7.8-2.7 2s1.1 1.7 2.8 2.1c1.7.4 2.9 1 2.9 2.3s-1.2 2.2-3 2.2c-1.4 0-2.5-.6-3-1.6"/>
      <line x1="12" y1="6" x2="12" y2="7.7"/>
      <line x1="12" y1="16.3" x2="12" y2="18"/>
    </g>"""


def ic_flask(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M9 3h6M10 3v5.5L5.2 17a2.5 2.5 0 0 0 2.2 3.7h9.2a2.5 2.5 0 0 0 2.2-3.7L14 8.5V3"/>
      <line x1="7.5" y1="15" x2="16.5" y2="15"/>
    </g>"""


def ic_wrench(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M14.7 6.3a4 4 0 0 0-5.4 5.4l-5.3 5.3a1.8 1.8 0 0 0 2.6 2.6l5.3-5.3a4 4 0 0 0 5.4-5.4l-2.3 2.3-2.6-2.6 2.3-2.3z"/>
    </g>"""


def ic_barn(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 10.5L12 4l9 6.5"/>
      <path d="M5 9.5V20h14V9.5"/>
      <rect x="9.2" y="13.5" width="5.6" height="6.5"/>
    </g>"""


def ic_rocket(cx: float, cy: float, col: str) -> str:
    return f"""<g transform="translate({cx - 12},{cy - 12})" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3c3.5 1.8 5.5 5.4 5.5 9.5l-2.5 2.5H9l-2.5-2.5C6.5 8.4 8.5 4.8 12 3z"/>
      <circle cx="12" cy="9.5" r="1.8"/>
      <path d="M9 15l-2 3.5h3.5M15 15l2 3.5h-3.5"/>
    </g>"""


# ==============================================================================
# DIAGRAM 4C: User Flow Ramah Awam (3 Swimlanes, 1600 x 760)
# ==============================================================================
def uf_node(x: float, y: float, w: float, h: float, step: str, title: str, l1: str, l2: str,
            border: str, badge_bg: str, badge_fg: str, bg: str = "#FFFFFF") -> str:
    return f"""
    <g filter="url(#softShadow)">
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{bg}" stroke="{border}" stroke-width="1.8"/>
      <circle cx="{x + 22}" cy="{y + 24}" r="12.5" fill="{badge_bg}"/>
      <text x="{x + 22}" y="{y + 28.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="{badge_fg}">{escape(step)}</text>
      <text x="{x + 42}" y="{y + 28}" font-family="'Montserrat', sans-serif" font-size="12.4" font-weight="700" fill="#0F172A">{escape(title)}</text>
      <text x="{x + 16}" y="{y + 54}" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#475569">{escape(l1)}</text>
      <text x="{x + 16}" y="{y + 72}" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#475569">{escape(l2)}</text>
    </g>"""


def build_svg_4c() -> str:
    w, h = 1600, 760
    lane_x, role_w, lane_w = 36, 186, 1528
    l1_y, l1_h = 122, 186
    l2_y, l2_h = 324, 186
    l3_y, l3_h = 526, 166
    cx = [248, 512, 776, 1040, 1304]
    nw, nh = 232, 94
    y_l1, y_l2, y_l3 = l1_y + 46, l2_y + 46, l3_y + 36

    nodes = "\n".join([
        uf_node(cx[0], y_l1, nw, nh, "1", "Buka Website & Setup",
                "Pilih bibit Cobb 500/Ross 308", "& tanggal masuk DOC (1×)",
                "#10B981", "#059669", "#FFFFFF"),
        uf_node(cx[1], y_l1, nw, nh, "2", "Gerakkan Rover di HP",
                "Arahkan pelan lewat Website", "& tekan Cek Napas (15 dtk)",
                "#10B981", "#059669", "#FFFFFF"),
        uf_node(cx[3], y_l1, nw, nh, "5", "Pilih 1 dari 3 Tombol",
                "Akan Saya Cek / Terlihat Normal", "/ Laporkan ke Dokter Hewan",
                "#F59E0B", "#D97706", "#FFFFFF", bg="#FFFBEB"),
        uf_node(cx[4], y_l1, nw, nh, "6", "Selesai & Bersih Roda",
                "Kembali ke Dock: Sikat →", "Disinfeksi → Kering + Log",
                "#10B981", "#059669", "#FFFFFF"),
        uf_node(cx[1], y_l2, nw, nh, "3", "Rover Pindai Kandang",
                "Kamera feses/fisik + audio 3×5", "dtk + suhu/RH/NH₃ (Offline OK)",
                "#0D9488", "#0F766E", "#FFFFFF"),
        uf_node(cx[2], y_l2, nw, nh, "4", "Evaluasi & Tampil Bukti",
                "Bandingkan ke umur broiler +", "cuaca BMKG/Open-Meteo + AI",
                "#2563EB", "#1D4ED8", "#FFFFFF"),
        uf_node(cx[3], y_l2, nw, nh, "5b", "Kemas Laporan 1-Klik",
                "Otomatis gabung foto, klip audio,", "grafik suhu/NH₃ & deplesi",
                "#2563EB", "#1D4ED8", "#FFFFFF"),
        uf_node(cx[3], y_l3, nw, nh, "7", "Terima Bukti Lengkap",
                "Buka paket WA / PDF berisi", "umur flok, foto, audio & grafik",
                "#F43F5E", "#E11D48", "#FFFFFF"),
        uf_node(cx[4], y_l3, nw, nh, "8", "Saran Medis Tepat",
                "Verifikasi klinis lebih cepat,", "hindari obat/antibiotik salah",
                "#F43F5E", "#E11D48", "#FFFFFF"),
    ])

    arrows = f"""
    <line x1="{cx[0] + nw + 2}" y1="{y_l1 + nh/2}" x2="{cx[1] - 4}" y2="{y_l1 + nh/2}" stroke="#059669" stroke-width="3" marker-end="url(#arrGreen)"/>
    <line x1="{cx[1] + nw/2}" y1="{y_l1 + nh + 2}" x2="{cx[1] + nw/2}" y2="{y_l2 - 4}" stroke="#0D9488" stroke-width="3" marker-end="url(#arrTeal)"/>
    <rect x="{cx[1] + nw/2 + 8}" y="{l1_y + l1_h - 6}" width="92" height="20" rx="6" fill="#CCFBF1"/>
    <text x="{cx[1] + nw/2 + 54}" y="{l1_y + l1_h + 7.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" font-weight="700" fill="#0F766E">Wi-Fi Lokal</text>
    <line x1="{cx[1] + nw + 2}" y1="{y_l2 + nh/2}" x2="{cx[2] - 4}" y2="{y_l2 + nh/2}" stroke="#2563EB" stroke-width="3" marker-end="url(#arrBlue)"/>
    <path d="M {cx[2] + nw/2} {y_l2 - 2} L {cx[2] + nw/2} {y_l1 + nh/2} L {cx[3] - 4} {y_l1 + nh/2}" fill="none" stroke="#D97706" stroke-width="3" stroke-linejoin="round" marker-end="url(#arrAmber)"/>
    <rect x="{cx[2] + nw/2 - 58}" y="{y_l1 + nh/2 - 28}" width="116" height="20" rx="6" fill="#FEF3C7"/>
    <text x="{cx[2] + nw/2}" y="{y_l1 + nh/2 - 14.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" font-weight="700" fill="#B45309">Peringatan &amp; Bukti</text>
    <line x1="{cx[3] + nw + 2}" y1="{y_l1 + nh/2}" x2="{cx[4] - 4}" y2="{y_l1 + nh/2}" stroke="#059669" stroke-width="3" marker-end="url(#arrGreen)"/>
    <rect x="{(cx[3] + nw + cx[4])/2 - 22}" y="{y_l1 + nh/2 - 28}" width="44" height="17" rx="5" fill="#DCFCE7"/>
    <text x="{(cx[3] + nw + cx[4])/2}" y="{y_l1 + nh/2 - 16.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="8.8" font-weight="700" fill="#047857">Selesai</text>
    <line x1="{cx[3] + nw/2}" y1="{y_l1 + nh + 2}" x2="{cx[3] + nw/2}" y2="{y_l2 - 4}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    <rect x="{cx[3] + nw/2 + 8}" y="{l1_y + l1_h - 6}" width="106" height="20" rx="6" fill="#FFE4E6"/>
    <text x="{cx[3] + nw/2 + 61}" y="{l1_y + l1_h + 7.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" font-weight="700" fill="#BE123C">Klik Laporkan</text>
    <line x1="{cx[3] + nw/2}" y1="{y_l2 + nh + 2}" x2="{cx[3] + nw/2}" y2="{y_l3 - 4}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    <rect x="{cx[3] + nw/2 + 8}" y="{l2_y + l2_h - 4}" width="84" height="20" rx="6" fill="#FFE4E6"/>
    <text x="{cx[3] + nw/2 + 50}" y="{l2_y + l2_h + 9.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.8" font-weight="700" fill="#BE123C">WA / PDF</text>
    <line x1="{cx[3] + nw + 2}" y1="{y_l3 + nh/2}" x2="{cx[4] - 4}" y2="{y_l3 + nh/2}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    """

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="softShadow" x="-4%" y="-4%" width="110%" height="114%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <marker id="arrGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#059669"/></marker>
    <marker id="arrTeal" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#0D9488"/></marker>
    <marker id="arrBlue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#2563EB"/></marker>
    <marker id="arrAmber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#D97706"/></marker>
    <marker id="arrRose" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.2" markerHeight="6.2" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#E11D48"/></marker>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <rect x="598" y="16" width="404" height="24" rx="12" fill="#DCFCE7"/>
  <text x="800" y="32" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="700" letter-spacing="0.7" fill="#166534">USER FLOW SISTEM INSPEKSI BROVER</text>
  <text x="800" y="69" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="25" font-weight="800" fill="#0F172A">Alur Penggunaan Harian: Peternak, Sistem &amp; Dokter Hewan</text>
  <text x="800" y="96" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="13.5" fill="#475569">Memisahkan jelas langkah yang diklik pengguna (Peternak &amp; Dokter Hewan) vs proses otomatis di Rover &amp; Website</text>
  <rect x="{lane_x}" y="{l1_y}" width="{lane_w}" height="{l1_h}" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="1.8"/>
  <path d="M{lane_x + 18} {l1_y} H{lane_x + role_w} V{l1_y + l1_h} H{lane_x + 18} Q{lane_x} {l1_y + l1_h} {lane_x} {l1_y + l1_h - 18} V{l1_y + 18} Q{lane_x} {l1_y} {lane_x + 18} {l1_y} Z" fill="#059669"/>
  <circle cx="{lane_x + role_w/2}" cy="{l1_y + 68}" r="26" fill="#FFFFFF"/>
  {ic_farmer(lane_x + role_w/2, l1_y + 68, "#047857")}
  <text x="{lane_x + role_w/2}" y="{l1_y + 120}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">PETERNAK / ABK</text>
  <text x="{lane_x + role_w/2}" y="{l1_y + 140}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#D1FAE5">Operator &amp; Penentu</text>
  <text x="{lane_x + role_w/2}" y="{l1_y + 156}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#D1FAE5">Tindakan di Kandang</text>
  <rect x="{lane_x}" y="{l2_y}" width="{lane_w}" height="{l2_h}" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.8"/>
  <path d="M{lane_x + 18} {l2_y} H{lane_x + role_w} V{l2_y + l2_h} H{lane_x + 18} Q{lane_x} {l2_y + l2_h} {lane_x} {l2_y + l2_h - 18} V{l2_y + 18} Q{lane_x} {l2_y} {lane_x + 18} {l2_y} Z" fill="#2563EB"/>
  <circle cx="{lane_x + role_w/2}" cy="{l2_y + 68}" r="26" fill="#FFFFFF"/>
  {ic_rover_web(lane_x + role_w/2, l2_y + 68, "#1D4ED8")}
  <text x="{lane_x + role_w/2}" y="{l2_y + 120}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">ROVER &amp; WEBSITE</text>
  <text x="{lane_x + role_w/2}" y="{l2_y + 140}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#DBEAFE">Pemindaian AI Lokal</text>
  <text x="{lane_x + role_w/2}" y="{l2_y + 156}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#DBEAFE">&amp; Evaluasi Otomatis</text>
  <rect x="{lane_x}" y="{l3_y}" width="{lane_w}" height="{l3_h}" rx="18" fill="#FFF1F2" stroke="#FDA4AF" stroke-width="1.8"/>
  <path d="M{lane_x + 18} {l3_y} H{lane_x + role_w} V{l3_y + l3_h} H{lane_x + 18} Q{lane_x} {l3_y + l3_h} {lane_x} {l3_y + l3_h - 18} V{l3_y + 18} Q{lane_x} {l3_y} {lane_x + 18} {l3_y} Z" fill="#E11D48"/>
  <circle cx="{lane_x + role_w/2}" cy="{l3_y + 58}" r="25" fill="#FFFFFF"/>
  {ic_vet(lane_x + role_w/2, l3_y + 58, "#BE123C")}
  <text x="{lane_x + role_w/2}" y="{l3_y + 108}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">DOKTER HEWAN</text>
  <text x="{lane_x + role_w/2}" y="{l3_y + 128}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#FFE4E6">Eskalasi Klinis &amp;</text>
  <text x="{lane_x + role_w/2}" y="{l3_y + 144}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#FFE4E6">Diagnosis Resmi</text>
  <rect x="{cx[0]}" y="{y_l3 + 14}" width="496" height="66" rx="12" fill="#FFFFFF" stroke="#FECDD3" stroke-width="1.4"/>
  <text x="{cx[0] + 18}" y="{y_l3 + 40}" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#9F1239">Prinsip Privasi &amp; Kendali Penuh Peternak:</text>
  <text x="{cx[0] + 18}" y="{y_l3 + 60}" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#475569">Data kandang hanya dikirim ke Dokter Hewan bila peternak menekan tombol Laporkan.</text>
  {nodes}
  {arrows}
  <rect x="36" y="708" width="1528" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="729.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.3" font-weight="600" fill="#475569">User Flow BROVER  |  Tim Asprak (Teknologi Informasi ITS &amp; Biologi UNJ)  |  Human-in-the-Loop &amp; Kebijakan 1 Unit = 1 Kandang</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 06: Peta Jalan Kesiapan Teknologi (TKT) BROVER (1600 x 920)
# Ascending Staircase SVG — Layperson-friendly, grounded in Permenristekdikti 42/2016 + Peer-Reviewed
# ==============================================================================
def build_svg_06() -> str:
    w, h = 1600, 920
    cw = 348
    gap = 40
    x0 = 44  # 44 + 4*348 + 3*40 = 44 + 1392 + 120 = 1556 (44px right margin)
    xs = [x0 + i * (cw + gap) for i in range(4)]
    ys = [248, 198, 148, 98]   # Ascending staircase steps (-50px each)
    ch = 394                   # Compact, zero wasted empty bottom space
    axis_y = 708               # Official TKT 1-9 scale bar

    steps = [
        {
            "tkt": "TKT 3-4",
            "score": 4,
            "title": "Purwarupa Awal",
            "period": "Nov 2026",
            "hdr": "#0D9488",
            "tint": "#F0FDFA",
            "border": "#5EEAD4",
            "pill_bg": "#CCFBF1",
            "pill_fg": "#0F766E",
            "icon": ic_flask,
            "meaning_1": "Pembuktian konsep & uji fungsi di lab",
            "meaning_2": "(Permenristekdikti No. 42 Tahun 2016)",
            "bullets": [
                "Rakit rover uji awal & sensor udara",
                "Kendali lewat website tanpa internet",
                "Uji deteksi AI pada simulasi meja",
            ],
            "proof": "Video alat berjalan & uji fungsi dasar",
        },
        {
            "tkt": "TKT 5-6",
            "score": 6,
            "title": "Purwarupa Siap Kandang",
            "period": "Des 2026 - Feb 2027",
            "hdr": "#2563EB",
            "tint": "#EFF6FF",
            "border": "#93C5FD",
            "pill_bg": "#DBEAFE",
            "pill_fg": "#1D4ED8",
            "icon": ic_wrench,
            "meaning_1": "Uji purwarupa penuh di simulasi nyata",
            "meaning_2": "(Mankins, Acta Astronautica, 2009)",
            "bullets": [
                "Casing tertutup tahan debu & gas",
                "Roda tangguh sekam & baterai aman",
                "Latih ulang AI dengan data lokal RI",
            ],
            "proof": "Lolos uji bak sekam & presentasi juri",
        },
        {
            "tkt": "TKT 7",
            "score": 7,
            "title": "Uji Kandang Mitra",
            "period": "Mar - Jun 2027",
            "hdr": "#7C3AED",
            "tint": "#F5F3FF",
            "border": "#C4B5FD",
            "pill_bg": "#EDE9FE",
            "pill_fg": "#6D28D9",
            "icon": ic_barn,
            "meaning_1": "Demonstrasi langsung di kandang asli",
            "meaning_2": "(Rowe et al., Animals Q1, 2019)",
            "bullets": [
                "Uji siklus penuh di kandang mitra",
                "Validasi gejala bersama Dokter Hewan",
                "Uji prosedur kebersihan roda harian",
            ],
            "proof": "Alat terbukti stabil di kandang komersial",
        },
        {
            "tkt": "TKT 8-9",
            "score": 9,
            "title": "Produk Siap Pasar",
            "period": "Jul 2027+",
            "hdr": "#059669",
            "tint": "#ECFDF5",
            "border": "#6EE7B7",
            "pill_bg": "#DCFCE7",
            "pill_fg": "#047857",
            "icon": ic_rocket,
            "meaning_1": "Sistem lengkap, terdaftar HKI & siap jual",
            "meaning_2": "(Permenristekdikti No. 42 Tahun 2016)",
            "bullets": [
                "Pendaftaran HKI & paten sederhana",
                "Skema beli sepaket & sewa peternak",
                "Lanjutan: jalur otomatis & aplikasi HP",
            ],
            "proof": "HKI terdaftar & siap adopsi peternak",
        },
    ]

    cards_svg = []
    connectors_svg = []

    for i, st in enumerate(steps):
        x = xs[i]
        y = ys[i]
        cx = x + cw / 2

        # 9-segment visual TKT scale bar inside card
        seg_w = 24
        seg_gap = 4.5
        seg_x0 = x + 18
        seg_y = y + 86
        segs = []
        for s in range(9):
            sx = seg_x0 + s * (seg_w + seg_gap)
            fill_s = st["hdr"] if s < st["score"] else "#E2E8F0"
            segs.append(f'<rect x="{sx:.1f}" y="{seg_y}" width="{seg_w}" height="10" rx="3" fill="{fill_s}"/>')

        bul_svg = []
        for bi, btxt in enumerate(st["bullets"]):
            by = y + 236 + bi * 28
            bul_svg.append(
                f'<circle cx="{x + 30}" cy="{by - 4}" r="4" fill="{st["hdr"]}"/>'
                f'<text x="{x + 42}" y="{by}" font-family="\'Open Sans\', sans-serif" font-size="12.0" fill="#1E293B">{escape(btxt)}</text>'
            )

        cards_svg.append(f"""
        <g filter="url(#cardShadow)">
          <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="18" fill="{st['tint']}" stroke="{st['border']}" stroke-width="2"/>
          <path d="M{x + 18} {y} H{x + cw - 18} Q{x + cw} {y} {x + cw} {y + 18} V{y + 68} H{x} V{y + 18} Q{x} {y} {x + 18} {y} Z" fill="{st['hdr']}"/>
        </g>
        <circle cx="{x + 34}" cy="{y + 34}" r="20" fill="#FFFFFF" opacity="0.96"/>
        {st['icon'](x + 34, y + 34, st['hdr'])}
        <rect x="{x + 64}" y="{y + 12}" width="78" height="21" rx="10" fill="#FFFFFF" opacity="0.22"/>
        <text x="{x + 103}" y="{y + 26.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.2" font-weight="800" fill="#FFFFFF">{escape(st['tkt'])}</text>
        <text x="{x + 64}" y="{y + 54}" font-family="'Montserrat', sans-serif" font-size="15.8" font-weight="800" fill="#FFFFFF">{escape(st['title'])}</text>

        <!-- Visual 1-9 TKT Progress Bar -->
        {''.join(segs)}
        <text x="{x + cw - 18}" y="{seg_y + 9}" text-anchor="end" font-family="'Montserrat', sans-serif" font-size="10.8" font-weight="700" fill="{st['pill_fg']}">{st['score']}/9</text>

        <!-- Arti Resmi Box -->
        <rect x="{x + 16}" y="{y + 112}" width="{cw - 32}" height="66" rx="11" fill="#FFFFFF" stroke="{st['border']}" stroke-width="1.2"/>
        <text x="{x + 28}" y="{y + 132}" font-family="'Montserrat', sans-serif" font-size="10.2" font-weight="800" fill="{st['pill_fg']}">ARTI TINGKAT KESIAPAN</text>
        <text x="{x + 28}" y="{y + 150}" font-family="'Open Sans', sans-serif" font-size="11.8" font-weight="600" fill="#0F172A">{escape(st['meaning_1'])}</text>
        <text x="{x + 28}" y="{y + 167}" font-family="'Open Sans', sans-serif" font-size="10.4" fill="#64748B">{escape(st['meaning_2'])}</text>

        <!-- Fokus BROVER Box -->
        <rect x="{x + 16}" y="{y + 190}" width="{cw - 32}" height="122" rx="11" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2"/>
        <text x="{x + 28}" y="{y + 211}" font-family="'Montserrat', sans-serif" font-size="10.2" font-weight="800" fill="#475569">FOKUS PENGEMBANGAN BROVER</text>
        {''.join(bul_svg)}

        <!-- Bukti Lulus Pill -->
        <rect x="{x + 16}" y="{y + 324}" width="{cw - 32}" height="54" rx="11" fill="{st['pill_bg']}" stroke="{st['border']}" stroke-width="1.2"/>
        <text x="{x + 28}" y="{y + 344}" font-family="'Montserrat', sans-serif" font-size="10.0" font-weight="800" fill="{st['pill_fg']}">BUKTI KELULUSAN</text>
        <text x="{x + 28}" y="{y + 364}" font-family="'Open Sans', sans-serif" font-size="11.8" font-weight="700" fill="#0F172A">{escape(st['proof'])}</text>
        """)

        # Vertical anchor stem + period pill down to official TKT 1-9 bar
        card_bot = y + ch
        pill_y = axis_y - 42
        connectors_svg.append(
            f'<line x1="{cx:.1f}" y1="{card_bot}" x2="{cx:.1f}" y2="{axis_y - 4}" stroke="{st["hdr"]}" stroke-width="2" stroke-dasharray="4,4"/>'
            f'<circle cx="{cx:.1f}" cy="{axis_y}" r="6.5" fill="{st["hdr"]}" stroke="#FFFFFF" stroke-width="2.2"/>'
            f'<rect x="{cx - 76:.1f}" y="{pill_y}" width="152" height="24" rx="12" fill="{st["pill_bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>'
            f'<text x="{cx:.1f}" y="{pill_y + 16}" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="10.8" font-weight="700" fill="{st["pill_fg"]}">{escape(st["period"])}</text>'
        )

        # Horizontal-upward arrow to next card
        if i < 3:
            ax1 = x + cw + 3
            ay1 = y + 185
            ax2 = xs[i + 1] - 5
            ay2 = ys[i + 1] + 215
            connectors_svg.append(
                f'<path d="M {ax1} {ay1} L {ax2} {ay2}" fill="none" stroke="{steps[i + 1]["hdr"]}" stroke-width="3.2" marker-end="url(#arrStep{i})"/>'
            )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.07"/>
    </filter>
    <marker id="arrStep0" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#2563EB"/></marker>
    <marker id="arrStep1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#7C3AED"/></marker>
    <marker id="arrStep2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto"><path d="M 0 1 L 9 5 L 0 9 z" fill="#059669"/></marker>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <!-- CLEAN TITLE (No badge pill, no verbose subtitle, no Tahap numbers) -->
  <text x="800" y="56" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="27" font-weight="800" fill="#0F172A">Peta Jalan Kesiapan Teknologi (TKT) BROVER</text>

  <!-- 4 ASCENDING STAIRCASE CARDS -->
  {''.join(cards_svg)}

  <!-- OFFICIAL PERMENRISTEKDIKTI 42/2016 3-GROUP SCALE BAR -->
  <rect x="44" y="{axis_y + 12}" width="348" height="32" rx="8" fill="#CCFBF1" stroke="#5EEAD4" stroke-width="1.2"/>
  <text x="218" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#0F766E">RISET DASAR &amp; LAB (TKT 1-4)</text>

  <rect x="404" y="{axis_y + 12}" width="388" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="1.2"/>
  <text x="598" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#1D4ED8">RISET TERAPAN &amp; SIMULASI (TKT 5-6)</text>

  <rect x="804" y="{axis_y + 12}" width="752" height="32" rx="8" fill="#DCFCE7" stroke="#6EE7B7" stroke-width="1.2"/>
  <text x="1180" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#047857">PENGEMBANGAN LAPANGAN &amp; KOMERSIALISASI (TKT 7-9)</text>

  <!-- Horizontal baseline line -->
  <line x1="44" y1="{axis_y}" x2="1556" y2="{axis_y}" stroke="#CBD5E1" stroke-width="3" stroke-linecap="round"/>
  {''.join(connectors_svg)}

  <!-- PEER-REVIEWED RATIONALE BANNER -->
  <rect x="44" y="770" width="1512" height="72" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="44" y="770" width="8" height="72" rx="4" fill="#0F766E"/>
  <text x="68" y="797" font-family="'Montserrat', sans-serif" font-size="12.6" font-weight="800" fill="#0F172A">Mengapa Peningkatan TKT BROVER Dilakukan Bertahap?</text>
  <text x="68" y="821" font-family="'Open Sans', sans-serif" font-size="12.2" fill="#334155">Tinjauan atas 260+ studi teknologi unggas (Rowe et al., 2019) membuktikan mayoritas alat berhenti di TKT 3-4 karena langsung melompat tanpa uji lingkungan kandang</text>
  <text x="68" y="837" font-family="'Open Sans', sans-serif" font-size="11.8" fill="#475569">nyata; uji bertahap lab → simulasi sekam → kandang mitra memastikan integrasi alat dan ketahanan lingkungan tervalidasi sebelum dipasarkan (Mankins, 2009; Olechowski et al., 2020).</text>

  <!-- CLEAN FOOTER -->
  <rect x="44" y="862" width="1512" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="883.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Acuan Resmi &amp; Peer-Reviewed: Permenristekdikti No. 42/2016, Mankins (2009), Rowe et al. (2019), &amp; Olechowski et al. (2020)</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 07: Business Model Canvas (Clean Title, 100% RI, All-In Opsi 2, Jargon-Free)
# ==============================================================================
def bmc_block(x: float, y: float, w: float, h: float, title: str, subtitle: str,
              bullets: list[tuple[str, str]], hdr_bg: str, tint: str, border: str,
              dot_col: str, icon_fn) -> str:
    hdr_h = 54
    parts = [f"""
    <g filter="url(#cardShadow)">
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{tint}" stroke="{border}" stroke-width="1.8"/>
      <path d="M{x + 16} {y} H{x + w - 16} Q{x + w} {y} {x + w} {y + 16} V{y + hdr_h} H{x} V{y + 16} Q{x} {y} {x + 16} {y} Z" fill="{hdr_bg}"/>
    </g>
    <circle cx="{x + 28}" cy="{y + 27}" r="16" fill="#FFFFFF" opacity="0.95"/>
    {icon_fn(x + 28, y + 27, hdr_bg)}
    <text x="{x + 54}" y="{y + 24}" font-family="'Montserrat', sans-serif" font-size="13.2" font-weight="800" fill="#FFFFFF">{escape(title)}</text>
    <text x="{x + 54}" y="{y + 42}" font-family="'Open Sans', sans-serif" font-size="10.6" fill="#FFFFFF" opacity="0.92">{escape(subtitle)}</text>
    """]

    avail_h = h - hdr_h - 20
    n = len(bullets)
    step_y = avail_h / max(1, n)
    cur_y = y + hdr_h + 24
    for btitle, bdesc in bullets:
        parts.append(f"""
        <circle cx="{x + 22}" cy="{cur_y - 4}" r="4.5" fill="{dot_col}"/>
        <text x="{x + 36}" y="{cur_y}" font-family="'Montserrat', sans-serif" font-size="11.9" font-weight="700" fill="#0F172A">{escape(btitle)}</text>
        <text x="{x + 36}" y="{cur_y + 17}" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">{escape(bdesc)}</text>
        """)
        cur_y += step_y
    return "\n".join(parts)


def build_svg_07() -> str:
    w, h = 1600, 940
    m, gap = 36, 14
    col_w = (w - 2 * m - 4 * gap) / 5
    xs = [m + i * (col_w + gap) for i in range(5)]

    top_y = 74
    top_h = 568
    half_h = (top_h - gap) / 2
    bot_y = top_y + top_h + gap
    bot_h = 218
    bot_w = (w - 2 * m - gap) / 2

    blocks = "\n".join([
        bmc_block(xs[0], top_y, col_w, top_h, "Key Partners", "Mitra Strategis Utama", [
            ("PT Zara Propertifarm", "Uji lapangan 6 farm & paket kandang"),
            ("PT Edura (PTNBH UNJ)", "Dukungan alat & komersialisasi"),
            ("Lab & Biologi UNJ", "Riset klinis, lab & pengajuan HKI"),
            ("Dokter Hewan & Dinas", "Validasi gejala & saluran laporan"),
            ("Pemasok E-Commerce RI", "Tokopedia, Shopee, Lazada & Blibli"),
        ], "#0F766E", "#F0FDFA", "#5EEAD4", "#0D9488", ic_handshake),

        bmc_block(xs[1], top_y, col_w, half_h, "Key Activities", "Kegiatan Inti Tim", [
            ("Pelatihan Model AI", "Data foto & audio kandang lokal RI"),
            ("Perakitan Rover", "Casing tertutup tahan debu & gas"),
            ("Pengembangan Website", "Kendali alat, dasbor & info cuaca"),
            ("Uji Lapangan & HKI", "Uji kandang mitra & paten sederhana"),
        ], "#2563EB", "#EFF6FF", "#93C5FD", "#2563EB", ic_checklist),

        bmc_block(xs[1], top_y + half_h + gap, col_w, half_h, "Key Resources", "Aset & Tim Inti", [
            ("Tim Multidisiplin Asprak", "4 TI ITS + 1 Dokter Hewan UNJ"),
            ("Desain Sirkuit & Rangka", "Rancangan elektronik & casing rover"),
            ("Dataset & 3 Model AI", "Data terkurasi & model siap pakai"),
            ("Fasilitas Lab UNJ", "Lab Robotika, IoT & Manufaktur"),
        ], "#0284C7", "#F0F9FF", "#7DD3FC", "#0284C7", ic_layers),

        bmc_block(xs[2], top_y, col_w, top_h, "Value Propositions", "Nilai Utama bagi Peternak", [
            ("Deteksi Dini 3-in-1", "Feses, fisik ayam & suara ngorok"),
            ("Standar Umur Resmi", "Cobb 500 & Ross 308 + cuaca BMKG"),
            ("Tetap Jalan Offline", "Kendali lewat Website via Wi-Fi lokal"),
            ("Sepaket Tanpa Tagihan", "Beli sekali, bebas langganan bulanan"),
            ("Laporan 1-Klik Dokter", "Kirim foto, audio & grafik (WA/PDF)"),
        ], "#D97706", "#FFFBEB", "#FCD34D", "#D97706", ic_bulb),

        bmc_block(xs[3], top_y, col_w, half_h, "Customer Relations", "Hubungan Pelanggan", [
            ("Pendampingan Pasang", "Setup awal dock & profil umur ayam"),
            ("Layanan Suku Cadang", "Ganti sensor & baterai tiap 2-3 tahun"),
            ("Dukungan WhatsApp", "Grup peternak & panduan gejala"),
        ], "#7C3AED", "#F5F3FF", "#C4B5FD", "#7C3AED", ic_chat),

        bmc_block(xs[3], top_y + half_h + gap, col_w, half_h, "Channels", "Saluran Distribusi", [
            ("Paket Kandang Mitra", "Tambahan paket kandang PT Zara"),
            ("Koperasi & Asosiasi", "PINSAR, GOPAN & inti kemitraan"),
            ("Jejaring Dokter Hewan", "Demo langsung di sentra broiler Jawa"),
        ], "#6366F1", "#EEF2FF", "#A5B4FC", "#6366F1", ic_truck),

        bmc_block(xs[4], top_y, col_w, top_h, "Customer Segments", "Target Pengguna Utama", [
            ("Kandang Menengah-Besar", "Skala 10.000-20.000 ekor (Beli Putus)"),
            ("Peternak Rakyat Kecil", "Skala 3.000-5.000 ekor (Sewa/Koperasi)"),
            ("Penyedia Kandang Lokal", "PT Zara / KANOPIS & agritech lokal"),
            ("Dokter Hewan & TSO", "Penerima laporan klinis terstruktur"),
        ], "#059669", "#ECFDF5", "#6EE7B7", "#059669", ic_users),

        bmc_block(m, bot_y, bot_w, bot_h, "Cost Structure", "Struktur Biaya Nyata (100% Pengadaan Dalam Negeri)", [
            ("Biaya Produksi Satuan (~Rp8,23 jt): Belanja komponen lokal + ongkos rakit & uji kualitas", "Basis pengadaan satuan di Tokopedia, Shopee, Lazada & Blibli"),
            ("Biaya Produksi Grosir (~Rp6,75 jt): Diskon distributor lokal (≥20 unit) & dukungan PT Edura", "Hemat ~18% di dalam negeri tanpa risiko proses impor awal"),
            ("Cadangan Server 3 Tahun (~Rp900 rb/unit) & Pendaftaran HKI", "Sudah masuk harga jual agar pembeli bebas tagihan bulanan"),
        ], "#BE123C", "#FFF1F2", "#FDA4AF", "#E11D48", ic_receipt),

        bmc_block(m + bot_w + gap, bot_y, bot_w, bot_h, "Revenue Streams", "Sumber Pendapatan Murni Sepaket (Tanpa Langganan Bulanan)", [
            ("Penjualan Unit Sepaket: Rp11,50 juta/unit (termasuk Website, Server 3 thn & Dock)", "Untung kotor Rp2,37 jt (satuan) hingga Rp3,85 jt/unit (33,5%, grosir RI)"),
            ("Sewa per Siklus: Rp550-650 ribu/siklus (sepaket tanpa biaya bulanan terpisah)", "Solusi bebas modal awal bagi peternak rakyat skala 3.000-5.000 ekor"),
            ("Paket Suku Cadang & Kalibrasi (~Rp1,5 jt tiap 2-3 tahun): Sensor & baterai awet", "Pendapatan berulang alami mengikuti umur pakai sensor di kandang"),
        ], "#047857", "#ECFDF5", "#6EE7B7", "#059669", ic_coin),
    ])

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="cardShadow" x="-2%" y="-2%" width="105%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3.5" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <text x="800" y="48" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="27" font-weight="800" fill="#0F172A">Business Model Canvas</text>

  {blocks}

  <rect x="36" y="892" width="1528" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="913.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Berbasis Data BPS 2025, Mitra PT Zara / PT Edura, &amp; Wawancara Praktisi Peternak Broiler (Edufarmers × PecahTelur)</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 08: Clean Project Timeline (Opsi A + Opsi A: No Milestones, Year Strip,
#             Clean Month Names, Week 1-4, 1-line Jargon-Free Tasks, 1920 x 840)
# ==============================================================================
def build_svg_08() -> str:
    w, h = 1920, 840

    tx, ty = 28, 76
    tw = 1864
    col_no_w = 46
    col_task_w = 398
    gantt_x = tx + col_no_w + col_task_w  # 472
    ww = 30
    mw = ww * 4        # 120px per month
    gantt_w = mw * 10  # 1200px -> 472..1672
    out_x = gantt_x + gantt_w  # 1672
    col_out_w = tw - col_no_w - col_task_w - gantt_w  # 220px -> 1672..1892

    months = ["Nov", "Des", "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu"]

    # Clean phase headers WITHOUT phase numbers
    phase_bands = [
        (0, 1, "SELEKSI", "#0D9488"),
        (1, 3, "BOOTCAMP & PROTOTYPING", "#2563EB"),
        (4, 1, "DEMO DAY", "#D97706"),
        (5, 1, "MATCHING", "#7C3AED"),
        (6, 4, "PILOT TESTING & HILIRISASI", "#059669"),
    ]

    # Year strip (Opsi A: thin 2026 | 2027 row)
    year_bands = [
        (0, 2, "2026"),
        (2, 8, "2027"),
    ]

    # 11 clean 1-line jargon-free tasks (start_week, end_week in [0..40])
    tasks = [
        ("1", "Penyusunan Proposal, BMC & Purwarupa Awal", 0, 3, "#0D9488", "Berkas & video purwarupa"),
        ("2", "Seleksi Administrasi & Substansi", 2, 4, "#0F766E", "Lolos tahap finalis"),
        ("3", "Bootcamp & Mentoring", 4, 16, "#2563EB", "Validasi bisnis & teknologi"),
        ("4", "Desain Papan Sirkuit, Casing & Rangka Rover", 4, 11, "#1D4ED8", "Unit fisik siap uji"),
        ("5", "Pengumpulan Data Kandang & Pelatihan AI", 5, 14, "#3B82F6", "Model AI terlatih"),
        ("6", "Pengembangan Website & Sistem Kendali", 4, 14, "#0284C7", "Website & kendali siap uji"),
        ("7", "Integrasi Sistem & Uji Simulasi Kandang", 11, 16, "#1E40AF", "Purwarupa berfungsi penuh"),
        ("8", "Persiapan Presentasi, Demo Alat & Penghargaan", 16, 20, "#D97706", "Demonstrasi di depan juri"),
        ("9", "Pendampingan HKI & Pertemuan Mitra Industri", 20, 24, "#7C3AED", "Komitmen kerja sama mitra"),
        ("10", "Uji Coba Lapangan di Kandang Mitra", 24, 36, "#059669", "Alat teruji di kandang asli"),
        ("11", "Pendaftaran HKI & Laporan Akhir", 28, 40, "#047857", "HKI & produk siap pasar"),
    ]

    hdr_h1 = 30  # Phase row
    hdr_h2 = 22  # Year strip (2026 | 2027)
    hdr_h3 = 26  # Month names (Nov..Agu)
    hdr_h4 = 22  # Week 1..4
    hdr_tot = hdr_h1 + hdr_h2 + hdr_h3 + hdr_h4  # 100px
    row_h = 48
    total_table_h = hdr_tot + len(tasks) * row_h  # 100 + 528 = 628 -> y = 76..704

    phase_svg = []
    for s_idx, span, plabel, pcol in phase_bands:
        px = gantt_x + s_idx * mw
        pw = span * mw
        phase_svg.append(f"""
        <rect x="{px}" y="{ty}" width="{pw}" height="{hdr_h1}" fill="{pcol}" stroke="#FFFFFF" stroke-width="1.2"/>
        <text x="{px + pw / 2}" y="{ty + 19.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.8" font-weight="800" fill="#FFFFFF">{escape(plabel)}</text>
        """)

    year_svg = []
    for s_idx, span, ylabel in year_bands:
        yx = gantt_x + s_idx * mw
        yw = span * mw
        year_svg.append(f"""
        <rect x="{yx}" y="{ty + hdr_h1}" width="{yw}" height="{hdr_h2}" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1"/>
        <text x="{yx + yw / 2}" y="{ty + hdr_h1 + 15}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="800" fill="#334155">{escape(ylabel)}</text>
        """)

    month_svg = []
    week_svg = []
    grid_svg = []
    for m_i, mname in enumerate(months):
        mx = gantt_x + m_i * mw
        month_svg.append(f"""
        <rect x="{mx}" y="{ty + hdr_h1 + hdr_h2}" width="{mw}" height="{hdr_h3}" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <text x="{mx + mw / 2}" y="{ty + hdr_h1 + hdr_h2 + 17.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.6" font-weight="800" fill="#0F172A">{escape(mname)}</text>
        """)
        grid_svg.append(f'<line x1="{mx}" y1="{ty + hdr_tot}" x2="{mx}" y2="{ty + total_table_h}" stroke="#94A3B8" stroke-width="1.15"/>')

        for w_i in range(4):
            wx = mx + w_i * ww
            week_svg.append(f"""
            <rect x="{wx}" y="{ty + hdr_h1 + hdr_h2 + hdr_h3}" width="{ww}" height="{hdr_h4}" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9"/>
            <text x="{wx + ww / 2}" y="{ty + hdr_h1 + hdr_h2 + hdr_h3 + 15}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="10.2" font-weight="700" fill="#475569">{w_i + 1}</text>
            """)
            if w_i > 0:
                grid_svg.append(f'<line x1="{wx}" y1="{ty + hdr_tot}" x2="{wx}" y2="{ty + total_table_h}" stroke="#E2E8F0" stroke-width="0.85"/>')

    rows_svg = []
    bars_svg = []
    for idx, (no, title, sw, ew, col, out_txt) in enumerate(tasks):
        ry = ty + hdr_tot + idx * row_h
        row_bg = "#FFFFFF" if idx % 2 == 0 else "#F8FAFC"
        rows_svg.append(f"""
        <rect x="{tx}" y="{ry}" width="{tw}" height="{row_h}" fill="{row_bg}"/>
        <line x1="{tx}" y1="{ry + row_h}" x2="{tx + tw}" y2="{ry + row_h}" stroke="#E2E8F0" stroke-width="1"/>
        <circle cx="{tx + col_no_w / 2}" cy="{ry + row_h / 2}" r="13" fill="{col}" opacity="0.14"/>
        <text x="{tx + col_no_w / 2}" y="{ry + row_h / 2 + 4.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.5" font-weight="800" fill="{col}">{no}</text>
        <text x="{tx + col_no_w + 14}" y="{ry + row_h / 2 + 4.5}" font-family="'Montserrat', sans-serif" font-size="12.6" font-weight="700" fill="#0F172A">{escape(title)}</text>
        <text x="{out_x + 14}" y="{ry + row_h / 2 + 4.5}" font-family="'Open Sans', sans-serif" font-size="11.6" font-weight="600" fill="#334155">{escape(out_txt)}</text>
        """)

        bx1 = gantt_x + sw * ww + 2
        bw = max(20.0, (ew - sw) * ww - 4)
        by_bar = ry + 10
        bh_bar = 28
        bars_svg.append(f'<rect x="{bx1:.1f}" y="{by_bar}" width="{bw:.1f}" height="{bh_bar}" rx="6" fill="{col}" filter="url(#barShadow)"/>')

    # Clean Legend Strip (NO year numbers, NO milestone diamond)
    leg_y = 724
    legend_items = [
        ("#0D9488", "Seleksi"),
        ("#2563EB", "Bootcamp & Prototyping"),
        ("#D97706", "Demo Day"),
        ("#7C3AED", "Business Matching"),
        ("#059669", "Pilot Testing & Hilirisasi"),
    ]
    # Center legend nicely across 1864px bar
    total_leg_w = sum(len(t) * 7.6 + 68 for _, t in legend_items) - 36
    lx_cur = (w - total_leg_w) / 2
    leg_svg = []
    for lcol, ltxt in legend_items:
        leg_svg.append(f'<rect x="{lx_cur:.1f}" y="{leg_y + 11}" width="16" height="16" rx="4" fill="{lcol}"/>')
        leg_svg.append(f'<text x="{lx_cur + 24:.1f}" y="{leg_y + 23.5}" font-family="\'Open Sans\', sans-serif" font-size="12.6" font-weight="600" fill="#334155">{escape(ltxt)}</text>')
        lx_cur += len(ltxt) * 7.6 + 68

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="tableShadow" x="-2%" y="-2%" width="104%" height="105%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="barShadow" x="-4%" y="-10%" width="108%" height="130%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="1.6" flood-color="#0F172A" flood-opacity="0.16"/>
    </filter>
    <clipPath id="tableClip">
      <rect x="{tx}" y="{ty}" width="{tw}" height="{total_table_h}" rx="14"/>
    </clipPath>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <!-- CLEAN TITLE ONLY (No pill badge, no subtitle, no date/week range) -->
  <text x="960" y="50" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="27" font-weight="800" fill="#0F172A">Jadwal Pelaksanaan Proyek BROVER</text>

  <g filter="url(#tableShadow)">
    <rect x="{tx}" y="{ty}" width="{tw}" height="{total_table_h}" rx="14" fill="#FFFFFF"/>
  </g>
  <g clip-path="url(#tableClip)">
    <rect x="{tx}" y="{ty}" width="{col_no_w}" height="{hdr_tot}" fill="#1E293B"/>
    <text x="{tx + col_no_w / 2}" y="{ty + 55}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#FFFFFF">No</text>

    <rect x="{tx + col_no_w}" y="{ty}" width="{col_task_w}" height="{hdr_tot}" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="{tx + col_no_w + 16}" y="{ty + 55}" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Tahapan Kegiatan</text>

    <rect x="{out_x}" y="{ty}" width="{col_out_w}" height="{hdr_tot}" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="{out_x + 14}" y="{ty + 55}" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Target / Output Kunci</text>

    {''.join(phase_svg)}
    {''.join(year_svg)}
    {''.join(month_svg)}
    {''.join(week_svg)}
    {''.join(rows_svg)}

    <line x1="{tx + col_no_w}" y1="{ty + hdr_tot}" x2="{tx + col_no_w}" y2="{ty + total_table_h}" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="{gantt_x}" y1="{ty + hdr_tot}" x2="{gantt_x}" y2="{ty + total_table_h}" stroke="#94A3B8" stroke-width="1.4"/>
    {''.join(grid_svg)}
    <line x1="{out_x}" y1="{ty + hdr_tot}" x2="{out_x}" y2="{ty + total_table_h}" stroke="#94A3B8" stroke-width="1.4"/>

    {''.join(bars_svg)}
  </g>
  <rect x="{tx}" y="{ty}" width="{tw}" height="{total_table_h}" rx="14" fill="none" stroke="#94A3B8" stroke-width="1.6"/>

  <rect x="28" y="{leg_y}" width="1864" height="38" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  {''.join(leg_svg)}

  <rect x="28" y="778" width="1864" height="36" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="960" y="800.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Kolom 1-4 Menunjukkan Minggu ke-1 s.d. Minggu ke-4 Setiap Bulan  |  Acuan Jadwal: Buku Pedoman Hackathon UNJ 2026</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 09: Proyeksi Keuntungan 5 Tahun (Clean Title, Jargon-Free, 1600 x 848)
# ==============================================================================
def build_svg_09() -> str:
    w, h = 1600, 848

    px0, px1 = 124, 916
    py_top, py_bot = 176, 680  # shifted cleanly up by 48px (no pill/subtitle clutter!)

    def x_yr(yr: float) -> float:
        return px0 + (yr / 5.0) * (px1 - px0)

    def y_val(val: float) -> float:
        return py_bot - ((val - (-50.0)) / 720.0) * (py_bot - py_top)

    yrs = [0, 1, 2, 3, 4, 5]
    no_brover = [0.0, 149.4, 184.3, 333.7, 368.6, 518.0]
    yes_cons  = [-11.5, 138.8, 191.8, 340.6, 393.5, 543.8]
    yes_mod   = [-11.5, 139.7, 210.8, 360.4, 431.5, 582.7]
    yes_opt   = [-11.5, 140.6, 235.4, 386.0, 480.9, 633.0]

    def poly_str(vals: list[float]) -> str:
        return " ".join(f"{x_yr(yr):.1f},{y_val(v):.1f}" for yr, v in zip(yrs, vals))

    band_pts = (
        " ".join(f"{x_yr(yr):.1f},{y_val(v):.1f}" for yr, v in zip(yrs, yes_opt))
        + " "
        + " ".join(f"{x_yr(yr):.1f},{y_val(v):.1f}" for yr, v in zip(reversed(yrs), reversed(yes_cons)))
    )

    y_grid = []
    for tick in [0, 100, 200, 300, 400, 500, 600]:
        yy = y_val(tick)
        col_g = "#94A3B8" if tick == 0 else "#E2E8F0"
        sw_g = "1.4" if tick == 0 else "1.0"
        y_grid.append(f'<line x1="{px0}" y1="{yy:.1f}" x2="{px1}" y2="{yy:.1f}" stroke="{col_g}" stroke-width="{sw_g}"/>')
        y_grid.append(f'<text x="{px0 - 12}" y="{yy + 4:.1f}" text-anchor="end" font-family="\'Open Sans\', sans-serif" font-size="11.2" font-weight="600" fill="#64748B">Rp{tick} jt</text>')

    x_grid = []
    x_labels = [
        ("Thn 0", "Beli Alat"),
        ("Thn 1", "6 Siklus"),
        ("Thn 2", "12 Siklus*"),
        ("Thn 3", "18 Siklus"),
        ("Thn 4", "24 Siklus*"),
        ("Thn 5", "30 Siklus"),
    ]
    for yr, (xl1, xl2) in zip(yrs, x_labels):
        xx = x_yr(yr)
        x_grid.append(f'<line x1="{xx:.1f}" y1="{py_top}" x2="{xx:.1f}" y2="{py_bot}" stroke="#F1F5F9" stroke-width="1"/>')
        x_grid.append(f'<text x="{xx:.1f}" y="{py_bot + 22}" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="11.8" font-weight="700" fill="#0F172A">{xl1}</text>')
        x_grid.append(f'<text x="{xx:.1f}" y="{py_bot + 38}" text-anchor="middle" font-family="\'Open Sans\', sans-serif" font-size="10.2" fill="#64748B">{xl2}</text>')

    ob_bands = ""
    for ob_yr in [2, 4]:
        ox = x_yr(ob_yr)
        ob_bands += f'<rect x="{ox - 24:.1f}" y="{py_top}" width="48" height="{py_bot - py_top}" fill="#FEE2E2" opacity="0.38"/>'

    dots_svg = []
    for yr, vno, vyes in zip(yrs, no_brover, yes_mod):
        dots_svg.append(f'<circle cx="{x_yr(yr):.1f}" cy="{y_val(vno):.1f}" r="5" fill="#FFFFFF" stroke="#DC2626" stroke-width="2.6"/>')
        dots_svg.append(f'<circle cx="{x_yr(yr):.1f}" cy="{y_val(vyes):.1f}" r="5.8" fill="#059669" stroke="#FFFFFF" stroke-width="2.2"/>')

    x5 = x_yr(5)
    y5_no = y_val(518.0)
    y5_mod = y_val(582.7)
    y5_opt = y_val(633.0)

    rx, rw = 1020, 544

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="2.5" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>

  <!-- CLEAN TITLE ONLY (No pill badge, no long subtitle) -->
  <text x="800" y="48" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="26.5" font-weight="800" fill="#0F172A">Proyeksi Keuntungan 5 Tahun: Dengan vs Tanpa BROVER</text>

  <!-- LEFT PANEL: 5-YEAR LINE CHART -->
  <rect x="36" y="70" width="960" height="712" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.6" filter="url(#cardShadow)"/>
  <text x="64" y="104" font-family="'Montserrat', sans-serif" font-size="16" font-weight="800" fill="#0F172A">Laba Kumulatif 5 Tahun (30 Siklus | Kandang 15.000 Ekor)</text>
  <text x="64" y="126" font-family="'Open Sans', sans-serif" font-size="11.8" fill="#475569">Sudah memotong harga beli sepaket (Rp11,5 jt) &amp; ganti sensor/baterai Tahun ke-3 (Rp1,5 jt)</text>

  <!-- Legend inside chart header -->
  <line x1="64" y1="151" x2="94" y2="151" stroke="#059669" stroke-width="3.6"/>
  <text x="102" y="155" font-family="'Open Sans', sans-serif" font-size="11.4" font-weight="700" fill="#065F46">Dengan BROVER (Moderat 30%)</text>

  <rect x="320" y="144" width="22" height="14" rx="3" fill="#10B981" opacity="0.22"/>
  <text x="348" y="155" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#047857">Rentang Skenario (15%-50%)</text>

  <line x1="538" y1="151" x2="568" y2="151" stroke="#DC2626" stroke-width="3" stroke-dasharray="7,5"/>
  <text x="576" y="155" font-family="'Open Sans', sans-serif" font-size="11.4" font-weight="700" fill="#B91C1C">Tanpa BROVER</text>

  <rect x="698" y="144" width="16" height="14" rx="3" fill="#FEE2E2"/>
  <text x="720" y="155" font-family="'Open Sans', sans-serif" font-size="11.0" fill="#991B1B">*Simulasi wabah (Thn 2 &amp; 4)</text>

  {ob_bands}
  {''.join(x_grid)}
  {''.join(y_grid)}

  <polygon points="{band_pts}" fill="#10B981" opacity="0.16"/>
  <polyline points="{poly_str(yes_opt)}" fill="none" stroke="#10B981" stroke-width="1.4" stroke-dasharray="4,4"/>
  <polyline points="{poly_str(yes_cons)}" fill="none" stroke="#10B981" stroke-width="1.4" stroke-dasharray="4,4"/>

  <polyline points="{poly_str(no_brover)}" fill="none" stroke="#DC2626" stroke-width="3.2" stroke-dasharray="8,5"/>
  <polyline points="{poly_str(yes_mod)}" fill="none" stroke="#059669" stroke-width="4.2"/>
  {''.join(dots_svg)}

  <!-- Thn 0 Purchase -->
  <rect x="{px0 + 14}" y="{y_val(-11.5) - 24:.1f}" width="174" height="24" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="{px0 + 101}" y="{y_val(-11.5) - 8.5:.1f}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="10.2" font-weight="700" fill="#991B1B">Thn 0: Beli Sepaket (-Rp11,5 jt)</text>

  <!-- Thn 2 BEP Callout -->
  <line x1="{x_yr(2):.1f}" y1="406" x2="{x_yr(2):.1f}" y2="{y_val(210.8) - 8:.1f}" stroke="#059669" stroke-width="1.6" stroke-dasharray="4,3"/>
  <rect x="{x_yr(2) - 96:.1f}" y="366" width="192" height="40" rx="8" fill="#ECFDF5" stroke="#34D399" stroke-width="1.5"/>
  <text x="{x_yr(2):.1f}" y="383" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.6" font-weight="800" fill="#065F46">Titik Balik Modal (BEP)</text>
  <text x="{x_yr(2):.1f}" y="398" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.9" fill="#047857">Thn 2: +Rp26,5 jt vs Tanpa Alat</text>

  <!-- Thn 3 Maintenance Callout -->
  <line x1="{x_yr(3):.1f}" y1="276" x2="{x_yr(3):.1f}" y2="{y_val(360.4) - 8:.1f}" stroke="#D97706" stroke-width="1.5" stroke-dasharray="4,3"/>
  <rect x="{x_yr(3) - 52:.1f}" y="236" width="202" height="40" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.4"/>
  <text x="{x_yr(3) + 49:.1f}" y="253" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.2" font-weight="700" fill="#92400E">Thn 3: Ganti Sensor &amp; Baterai</text>
  <text x="{x_yr(3) + 49:.1f}" y="268" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="9.7" fill="#B45309">Sudah dipotong jujur (-Rp1,5 jt)</text>

  <!-- Year 5 End Labels -->
  <text x="{x5 + 10:.1f}" y="{y5_opt + 4:.1f}" font-family="'Open Sans', sans-serif" font-size="10.4" font-weight="700" fill="#047857">633 jt (Opt)</text>
  <text x="{x5 + 10:.1f}" y="{y5_mod + 4:.1f}" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="800" fill="#065F46">582,7 jt</text>
  <text x="{x5 + 10:.1f}" y="{y5_no + 4:.1f}" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="800" fill="#B91C1C">518,0 jt</text>

  <!-- Big Delta Highlight Badge -->
  <rect x="148" y="190" width="380" height="74" rx="14" fill="#ECFDF5" stroke="#10B981" stroke-width="2" filter="url(#cardShadow)"/>
  <text x="170" y="215" font-family="'Montserrat', sans-serif" font-size="11.2" font-weight="700" fill="#047857">SELISIH UNTUNG BERSIH 5 TAHUN (MODERAT)</text>
  <text x="170" y="246" font-family="'Montserrat', sans-serif" font-size="23.5" font-weight="800" fill="#065F46">+Rp64,7 Juta  (ROI 498%)</text>

  <!-- Chart footnote -->
  <text x="64" y="746" font-family="'Open Sans', sans-serif" font-size="10.4" fill="#64748B">Dasar data primer: Margin Rp1.760/ekor/siklus &amp; rugi wabah batas bawah Rp7.630/ekor (Pramuwidyatama et al., Prev. Vet. Med. Q1, 2023).</text>
  <text x="64" y="762" font-family="'Open Sans', sans-serif" font-size="10.4" fill="#64748B">Rentang 5 tahun dipilih sesuai umur pakai wajar perangkat elektronik di kandang tropis (bukan proyeksi 10 tahun tanpa ganti alat).</text>

  <!-- RIGHT PANEL: JARGON-FREE INVESTOR CARDS -->
  <!-- CARD 1 -->
  <rect x="{rx}" y="70" width="{rw}" height="258" rx="18" fill="#F8FAFC" stroke="#93C5FD" stroke-width="1.8" filter="url(#cardShadow)"/>
  <path d="M{rx + 18} 70 H{rx + rw - 18} Q{rx + rw} 70 {rx + rw} 88 V118 H{rx} V88 Q{rx} 70 {rx + 18} 70 Z" fill="#1D4ED8"/>
  <text x="{rx + 22}" y="99" font-family="'Montserrat', sans-serif" font-size="13.8" font-weight="800" fill="#FFFFFF">1. Rincian Biaya &amp; Untung Tim (100% Lokal RI)</text>

  <rect x="{rx + 18}" y="134" width="246" height="82" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.3"/>
  <text x="{rx + 32}" y="157" font-family="'Open Sans', sans-serif" font-size="10.8" font-weight="700" fill="#64748B">BIAYA PRODUKSI SATUAN</text>
  <text x="{rx + 32}" y="184" font-family="'Montserrat', sans-serif" font-size="19" font-weight="800" fill="#0F172A">Rp8,23 Juta</text>
  <text x="{rx + 32}" y="204" font-family="'Open Sans', sans-serif" font-size="10.4" fill="#475569">Komponen lokal + rakit &amp; uji</text>

  <rect x="{rx + 278}" y="134" width="248" height="82" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.3"/>
  <text x="{rx + 292}" y="157" font-family="'Open Sans', sans-serif" font-size="10.8" font-weight="700" fill="#0F766E">BIAYA GROSIR LOKAL (≥20 UNIT)</text>
  <text x="{rx + 292}" y="184" font-family="'Montserrat', sans-serif" font-size="19" font-weight="800" fill="#0F766E">~Rp6,75 Juta</text>
  <text x="{rx + 292}" y="204" font-family="'Open Sans', sans-serif" font-size="10.4" fill="#475569">Distributor RI + dukungan PT Edura</text>

  <rect x="{rx + 18}" y="228" width="{rw - 36}" height="84" rx="12" fill="#EFF6FF" stroke="#60A5FA" stroke-width="1.6"/>
  <text x="{rx + 34}" y="252" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="800" fill="#1E3A8A">Harga Jual Sepaket:  Rp11,50 Juta / Unit</text>
  <text x="{rx + 34}" y="273" font-family="'Open Sans', sans-serif" font-size="11.4" fill="#1E40AF">Sudah termasuk cadangan server 3 thn (Rp900 rb) &amp; bebas tagihan bulanan.</text>
  <text x="{rx + 34}" y="295" font-family="'Montserrat', sans-serif" font-size="12.0" font-weight="800" fill="#047857">Untung Kotor Tim: Rp2,37 jt (satuan) → Rp3,85 jt/unit (33,5%, grosir)</text>

  <!-- CARD 2 -->
  <rect x="{rx}" y="344" width="{rw}" height="206" rx="18" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="1.8" filter="url(#cardShadow)"/>
  <path d="M{rx + 18} 344 H{rx + rw - 18} Q{rx + rw} 344 {rx + rw} 362 V390 H{rx} V362 Q{rx} 344 {rx + 18} 344 Z" fill="#059669"/>
  <text x="{rx + 22}" y="372" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">2. Perkiraan Untung Peternak 5 Tahun (15.000 Ekor)</text>

  <rect x="{rx + 18}" y="404" width="{rw - 36}" height="40" rx="9" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{rx + 32}" y="428" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#334155">Konservatif (15% cegah rugi)</text>
  <text x="{rx + rw - 32}" y="428" text-anchor="end" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#0F766E">+Rp25,9 Juta  |  ROI 199%</text>

  <rect x="{rx + 18}" y="452" width="{rw - 36}" height="42" rx="9" fill="#ECFDF5" stroke="#10B981" stroke-width="1.6"/>
  <text x="{rx + 32}" y="477" font-family="'Montserrat', sans-serif" font-size="12.2" font-weight="800" fill="#065F46">Moderat (30% cegah rugi)</text>
  <text x="{rx + rw - 32}" y="477" text-anchor="end" font-family="'Montserrat', sans-serif" font-size="13.2" font-weight="800" fill="#059669">+Rp64,7 Juta  |  ROI 498%</text>

  <rect x="{rx + 18}" y="502" width="{rw - 36}" height="38" rx="9" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{rx + 32}" y="525" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#334155">Optimistis (50% cegah rugi)</text>
  <text x="{rx + rw - 32}" y="525" text-anchor="end" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#047857">+Rp115,0 Juta  |  ROI 885%</text>

  <!-- CARD 3 -->
  <rect x="{rx}" y="566" width="{rw}" height="216" rx="18" fill="#FFFBEB" stroke="#FCD34D" stroke-width="1.8" filter="url(#cardShadow)"/>
  <path d="M{rx + 18} 566 H{rx + rw - 18} Q{rx + rw} 566 {rx + rw} 584 V612 H{rx} V584 Q{rx} 566 {rx + 18} 566 Z" fill="#D97706"/>
  <text x="{rx + 22}" y="594" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">3. Strategi Penjualan Menurut Ukuran Kandang</text>

  <rect x="{rx + 18}" y="626" width="{rw - 36}" height="64" rx="11" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.4"/>
  <text x="{rx + 32}" y="648" font-family="'Montserrat', sans-serif" font-size="12.0" font-weight="800" fill="#065F46">Target Utama Beli Putus: 10.000 - 20.000 Ekor</text>
  <text x="{rx + 32}" y="667" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">Harga Rp11,5 jt setara ~44% margin 1 siklus (atau ~10% rugi 1× wabah).</text>
  <text x="{rx + 32}" y="682" font-family="'Open Sans', sans-serif" font-size="10.8" font-weight="600" fill="#047857">Cocok dipaketkan bersama kandang mitra PT Zara / peternak besar.</text>

  <rect x="{rx + 18}" y="700" width="{rw - 36}" height="68" rx="11" fill="#FFFFFF" stroke="#FDE68A" stroke-width="1.4"/>
  <text x="{rx + 32}" y="722" font-family="'Montserrat', sans-serif" font-size="12.0" font-weight="800" fill="#92400E">Target Skema Sewa / Koperasi: 3.000 - 5.000 Ekor</text>
  <text x="{rx + 32}" y="741" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">Beli putus 5 thn tetap untung (+Rp13,1 jt, ROI 101%), namun modal awal</text>
  <text x="{rx + 32}" y="757" font-family="'Open Sans', sans-serif" font-size="11.2" fill="#475569">jauh lebih ringan lewat Sewa Rp550-650 rb/siklus atau milik koperasi.</text>

  <!-- CLEAN FOOTER -->
  <rect x="36" y="798" width="1528" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="819.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Sumber Data: Pramuwidyatama et al. (2023), Data 6 Farm PT Zara, &amp; Audit Harga E-Commerce Indonesia</text>
</svg>
"""


def main() -> None:
    os.makedirs(ASSETS_DIR, exist_ok=True)
    for svg_content, svg_p, png_p, w, h, tag in [
        (build_svg_4c(), SVG_4C, PNG_4C, 1600, 760, "04c User Flow"),
        (build_svg_06(), SVG_06, PNG_06, 1600, 920, "06 Roadmap TKT (Staircase SVG)"),
        (build_svg_07(), SVG_07, PNG_07, 1600, 940, "07 BMC (Clean RI Opsi 2)"),
        (build_svg_08(), SVG_08, PNG_08, 1920, 840, "08 Timeline (Clean W1-W4)"),
        (build_svg_09(), SVG_09, PNG_09, 1600, 848, "09 5-Year ROI (Clean)"),
    ]:
        with open(svg_p, "w", encoding="utf-8") as f:
            f.write(svg_content)
        render_svg(svg_p, png_p, w, h)
        print(f"GENERATED {tag}: {png_p} ({os.path.getsize(png_p)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
