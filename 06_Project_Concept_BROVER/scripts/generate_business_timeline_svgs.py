#!/usr/bin/env python3
"""Generate layperson-friendly vector SVG + high-res PNG visuals for BROVER:
- 04c_user_flow_brover.svg / .png                  : 3-swimlane user flow for BROVER Kandang (rover) and BROVER Saku (phone photo)
- 06_roadmap_tkt_dan_evolusi_brover.svg / .png     : TKT staircase roadmap (Permenristekdikti 42/2016 definitions)
- 07_business_model_canvas_brover.svg / .png       : 9-block BMC with two subscription packages and a buy-out option
- 08_project_timeline_brover.svg / .png            : 10-month Gantt timeline (Nov 2026 - Aug 2027, weeks 1-4 per month)
- 08b_jadwal_purwarupa_3_bulan_brover.svg / .png   : 12-week prototype schedule (Dec 2026 - Feb 2027) with milestones M1-M3
- 09_titik_impas_paket_brover.svg / .png           : farmer break-even per package vs normal mortality, plus price comparison

All SVGs are self-contained and rendered at 2x scale via Playwright Chromium. Old versions live in assets/history/.
"""

import os
import re
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
SVG_08B = os.path.join(ASSETS_DIR, "08b_jadwal_purwarupa_3_bulan_brover.svg")
PNG_08B = os.path.join(ASSETS_DIR, "08b_jadwal_purwarupa_3_bulan_brover.png")
SVG_09 = os.path.join(ASSETS_DIR, "09_titik_impas_paket_brover.svg")
PNG_09 = os.path.join(ASSETS_DIR, "09_titik_impas_paket_brover.png")


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
    w, h = 1720, 772
    lane_x, role_w = 36, 178
    lane_w = w - 2 * lane_x
    l1_y, l1_h = 122, 190
    l2_y, l2_h = 328, 190
    l3_y, l3_h = 534, 176
    nw, nh, pad = 210, 94, 18
    gap = (lane_w - role_w - 2 * pad - 6 * nw) / 5
    x0 = lane_x + role_w + pad
    cx = [x0 + i * (nw + gap) for i in range(6)]
    y_l1, y_l2, y_l3 = l1_y + 48, l2_y + 48, l3_y + 40
    m1, m2, m3 = y_l1 + nh / 2, y_l2 + nh / 2, y_l3 + nh / 2
    green = ("#10B981", "#059669", "#FFFFFF")
    blue = ("#2563EB", "#1D4ED8", "#FFFFFF")
    rose = ("#F43F5E", "#E11D48", "#FFFFFF")

    nodes = "\n".join([
        uf_node(cx[0], y_l1, nw, nh, "1", "Setup Awal Siklus",
                "Pilih paket, bibit Cobb/Ross,", "& tanggal DOC masuk (1×)", *green),
        uf_node(cx[1], y_l1, nw, nh, "2", "Ambil Data 2×/Hari",
                "Kandang: setir rover via web", "Saku: foto feses dari HP", *green),
        uf_node(cx[2], y_l1, nw, nh, "3", "Isi Catatan Harian",
                "Deplesi, pakan, air, vaksin", "& ceklis gejala pernapasan", *green),
        uf_node(cx[4], y_l1, nw, nh, "6", "Triase 3 Tombol",
                "Akan Saya Cek, Terlihat", "Normal, atau Laporkan",
                "#F59E0B", "#D97706", "#FFFFFF", bg="#FFFBEB"),
        uf_node(cx[5], y_l1, nw, nh, "7", "Selesai & Sanitasi",
                "Kandang: rover ke dok lalu", "sikat, disinfeksi, keringkan", *green),
        uf_node(cx[1], y_l2, nw, nh, "4", "Skrining Feses (CV)",
                "Kandang: di Orange Pi, luring", "Saku: antre, lalu ke server",
                "#0D9488", "#0F766E", "#FFFFFF"),
        uf_node(cx[2], y_l2, nw, nh, "5", "Evaluasi & Bukti",
                "Udara vs standar umur, cuaca", "BMKG & catatan harian ABK", *blue),
        uf_node(cx[4], y_l2, nw, nh, "6b", "Kemas Laporan 1-Klik",
                "Gabung foto feses, ceklis,", "grafik udara & deplesi", *blue),
        uf_node(cx[4], y_l3, nw, nh, "8", "Terima Paket Bukti",
                "WA / PDF: umur flok, foto,", "ceklis gejala & grafik", *rose),
        uf_node(cx[5], y_l3, nw, nh, "9", "Pemeriksaan Klinis",
                "Diagnosis & resep obat", "tetap di dokter hewan", *rose),
    ])

    def tag(x: float, y: float, wd: float, text: str, fill: str, ink: str) -> str:
        return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{wd}" height="20" rx="6" fill="{fill}"/>'
                f'<text x="{x + wd / 2:.1f}" y="{y + 13.5:.1f}" text-anchor="middle" font-family="\'Open Sans\', sans-serif" '
                f'font-size="9.8" font-weight="700" fill="{ink}">{escape(text)}</text>')

    def vx(i: int) -> float:
        return cx[i] + nw / 2

    arrows = f"""
    <line x1="{cx[0] + nw + 2:.1f}" y1="{m1}" x2="{cx[1] - 4:.1f}" y2="{m1}" stroke="#059669" stroke-width="3" marker-end="url(#arrGreen)"/>
    <line x1="{cx[1] + nw + 2:.1f}" y1="{m1}" x2="{cx[2] - 4:.1f}" y2="{m1}" stroke="#059669" stroke-width="3" marker-end="url(#arrGreen)"/>
    <line x1="{vx(1):.1f}" y1="{y_l1 + nh + 2}" x2="{vx(1):.1f}" y2="{y_l2 - 4}" stroke="#0D9488" stroke-width="3" marker-end="url(#arrTeal)"/>
    {tag(vx(1) + 8, l1_y + l1_h - 6, 128, "Wi-Fi lokal / unggah", "#CCFBF1", "#0F766E")}
    <line x1="{vx(2):.1f}" y1="{y_l1 + nh + 2}" x2="{vx(2):.1f}" y2="{y_l2 - 4}" stroke="#2563EB" stroke-width="3" marker-end="url(#arrBlue)"/>
    {tag(vx(2) + 8, l1_y + l1_h - 6, 86, "Data harian", "#DBEAFE", "#1D4ED8")}
    <line x1="{cx[1] + nw + 2:.1f}" y1="{m2}" x2="{cx[2] - 4:.1f}" y2="{m2}" stroke="#2563EB" stroke-width="3" marker-end="url(#arrBlue)"/>
    <path d="M {cx[2] + nw + 2:.1f} {m2} L {vx(3):.1f} {m2} L {vx(3):.1f} {m1} L {cx[4] - 4:.1f} {m1}" fill="none" stroke="#D97706" stroke-width="3" stroke-linejoin="round" marker-end="url(#arrAmber)"/>
    {tag(vx(3) - 62, m1 - 32, 124, "Peringatan & bukti", "#FEF3C7", "#B45309")}
    <line x1="{cx[4] + nw + 2:.1f}" y1="{m1}" x2="{cx[5] - 4:.1f}" y2="{m1}" stroke="#059669" stroke-width="3" marker-end="url(#arrGreen)"/>
    <line x1="{vx(4):.1f}" y1="{y_l1 + nh + 2}" x2="{vx(4):.1f}" y2="{y_l2 - 4}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    {tag(vx(4) + 8, l1_y + l1_h - 6, 106, "Klik Laporkan", "#FFE4E6", "#BE123C")}
    <line x1="{vx(4):.1f}" y1="{y_l2 + nh + 2}" x2="{vx(4):.1f}" y2="{y_l3 - 4}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    {tag(vx(4) + 8, l2_y + l2_h - 6, 84, "WA / PDF", "#FFE4E6", "#BE123C")}
    <line x1="{cx[4] + nw + 2:.1f}" y1="{m3}" x2="{cx[5] - 4:.1f}" y2="{m3}" stroke="#E11D48" stroke-width="3" marker-end="url(#arrRose)"/>
    """

    def lane(y: float, hh: float, tint: str, stroke: str, solid: str, icon: str,
             title: str, s1: str, s2: str, sub_ink: str, icon_dy: float) -> str:
        cxr = lane_x + role_w / 2
        return f"""
  <rect x="{lane_x}" y="{y}" width="{lane_w}" height="{hh}" rx="18" fill="{tint}" stroke="{stroke}" stroke-width="1.8"/>
  <path d="M{lane_x + 18} {y} H{lane_x + role_w} V{y + hh} H{lane_x + 18} Q{lane_x} {y + hh} {lane_x} {y + hh - 18} V{y + 18} Q{lane_x} {y} {lane_x + 18} {y} Z" fill="{solid}"/>
  <circle cx="{cxr}" cy="{y + icon_dy}" r="26" fill="#FFFFFF"/>
  {icon}
  <text x="{cxr}" y="{y + icon_dy + 52}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">{escape(title)}</text>
  <text x="{cxr}" y="{y + icon_dy + 72}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="{sub_ink}">{escape(s1)}</text>
  <text x="{cxr}" y="{y + icon_dy + 88}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" fill="{sub_ink}">{escape(s2)}</text>"""

    cxr = lane_x + role_w / 2
    lanes = (
        lane(l1_y, l1_h, "#ECFDF5", "#6EE7B7", "#059669", ic_farmer(cxr, l1_y + 66, "#047857"),
             "PETERNAK / ABK", "Operator & Penentu", "Tindakan di Kandang", "#D1FAE5", 66)
        + lane(l2_y, l2_h, "#EFF6FF", "#93C5FD", "#2563EB", ic_rover_web(cxr, l2_y + 66, "#1D4ED8"),
               "SISTEM BROVER", "Kandang: Orange Pi", "Saku: Server Pusat", "#DBEAFE", 66)
        + lane(l3_y, l3_h, "#FFF1F2", "#FDA4AF", "#E11D48", ic_vet(cxr, l3_y + 58, "#BE123C"),
               "DOKTER HEWAN", "Pemeriksaan Klinis &", "Keputusan Pengobatan", "#FFE4E6", 58)
    )

    pb_x, pb_y = cx[0], y_l3 - 4
    pb_w = cx[2] + nw - cx[0]
    body = "font-family=\"'Open Sans', sans-serif\" font-size=\"11.4\" fill=\"#475569\""
    privacy = f"""
  <rect x="{pb_x:.1f}" y="{pb_y}" width="{pb_w:.1f}" height="104" rx="12" fill="#FFFFFF" stroke="#FECDD3" stroke-width="1.4"/>
  <text x="{pb_x + 18:.1f}" y="{pb_y + 26}" font-family="'Montserrat', sans-serif" font-size="11.8" font-weight="700" fill="#9F1239">Privasi, Persetujuan &amp; Batas Peran AI:</text>
  <text x="{pb_x + 18:.1f}" y="{pb_y + 48}" {body}>Data kandang hanya dikirim ke dokter hewan bila peternak menekan tombol Laporkan.</text>
  <text x="{pb_x + 18:.1f}" y="{pb_y + 67}" {body}>Foto BROVER Saku disimpan di server hanya dengan persetujuan peternak.</text>
  <text x="{pb_x + 18:.1f}" y="{pb_y + 86}" {body}>AI hanya skrining, bukan diagnosis; dasbor tidak pernah menampilkan resep atau dosis antibiotik.</text>"""

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
  <rect x="{w / 2 - 202}" y="16" width="404" height="24" rx="12" fill="#DCFCE7"/>
  <text x="{w / 2}" y="32" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="10.5" font-weight="700" letter-spacing="0.7" fill="#166534">USER FLOW SISTEM INSPEKSI BROVER</text>
  <text x="{w / 2}" y="69" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="25" font-weight="800" fill="#0F172A">Alur Penggunaan Harian: Peternak, Sistem &amp; Dokter Hewan</text>
  <text x="{w / 2}" y="96" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="13.5" fill="#475569">BROVER Kandang mengambil data dengan rover, BROVER Saku dengan foto HP; keduanya memakai evaluasi, triase 3 tombol &amp; laporan yang sama</text>
  {lanes}
  {privacy}
  {nodes}
  {arrows}
  <rect x="36" y="{h - 48}" width="{w - 72}" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{w / 2}" y="{h - 26.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.3" font-weight="600" fill="#475569">User Flow BROVER  |  Tim Asprak (Teknologi Informasi ITS &amp; Biologi UNJ)  |  Skrining, Bukan Diagnosis  |  Human-in-the-Loop &amp; SOP 1 Unit = 1 Kandang</text>
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
            "tkt": "TKT 3–4",
            "score": 4,
            "title": "Purwarupa Awal",
            "period": "Nov 2026 (Saat Ini)",
            "hdr": "#0D9488",
            "tint": "#F0FDFA",
            "border": "#5EEAD4",
            "pill_bg": "#CCFBF1",
            "pill_fg": "#0F766E",
            "icon": ic_flask,
            "meaning_1": "Pembuktian konsep & uji fungsi di lab",
            "meaning_2": "(Permenristekdikti No. 42 Tahun 2016)",
            "bullets": [
                "Rover Tahap 1 dirakit & lulus uji jalan",
                "Kendali web Wi-Fi lokal & rem 500 ms",
                "Dasbor web versi awal berjalan",
            ],
            "proof": "Video uji jalan rover & dasbor awal",
        },
        {
            "tkt": "TKT 5–6",
            "score": 6,
            "title": "Purwarupa Siap Kandang",
            "period": "Des 2026 – Feb 2027",
            "hdr": "#2563EB",
            "tint": "#EFF6FF",
            "border": "#93C5FD",
            "pill_bg": "#DBEAFE",
            "pill_fg": "#1D4ED8",
            "icon": ic_wrench,
            "meaning_1": "Uji purwarupa di lingkungan relevan",
            "meaning_2": "(Mankins, Acta Astronautica, 2009)",
            "bullets": [
                "Servo kamera, tiang sensor & dok",
                "Uji bak sekam & baterai ≥3 jam",
                "Model CV feses RKNN INT8 + set uji lokal",
            ],
            "proof": "M3: purwarupa terintegrasi, KPI terukur",
        },
        {
            "tkt": "TKT 7",
            "score": 7,
            "title": "Uji Kandang Mitra",
            "period": "Mei – Agu 2027",
            "hdr": "#7C3AED",
            "tint": "#F5F3FF",
            "border": "#C4B5FD",
            "pill_bg": "#EDE9FE",
            "pill_fg": "#6D28D9",
            "icon": ic_barn,
            "meaning_1": "Demonstrasi sistem di kandang sebenarnya",
            "meaning_2": "(Permenristekdikti No. 42 Tahun 2016)",
            "bullets": [
                "Pilot 1–2 siklus mulai hari ke-7",
                "Validasi skrining bersama dokter hewan",
                "Kalibrasi SEN0567 & SOP sanitasi roda",
            ],
            "proof": "Laporan pilot & kesepakatan uji tertulis",
        },
        {
            "tkt": "TKT 8–9",
            "score": 9,
            "title": "Produk Siap Pasar",
            "period": "Setelah Agu 2027",
            "hdr": "#059669",
            "tint": "#ECFDF5",
            "border": "#6EE7B7",
            "pill_bg": "#DCFCE7",
            "pill_fg": "#047857",
            "icon": ic_rocket,
            "meaning_1": "Sistem lengkap, teruji & terbukti dipakai",
            "meaning_2": "(Permenristekdikti No. 42 Tahun 2016)",
            "bullets": [
                "HKI terdaftar & produksi batch kecil",
                "Lanjutan: CV navigasi & jadwal otomatis",
                "Riset: CO₂, kamera termal, mikrofon tetap",
            ],
            "proof": "Paket Saku & Kandang dipakai peternak",
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

  <!-- Test-environment scale bar per TKT definitions (Permenristekdikti 42/2016) -->
  <rect x="44" y="{axis_y + 12}" width="348" height="32" rx="8" fill="#CCFBF1" stroke="#5EEAD4" stroke-width="1.2"/>
  <text x="218" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#0F766E">ANALITIS &amp; LABORATORIUM (TKT 3–4)</text>

  <rect x="404" y="{axis_y + 12}" width="388" height="32" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="1.2"/>
  <text x="598" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#1D4ED8">LINGKUNGAN RELEVAN (TKT 5–6)</text>

  <rect x="804" y="{axis_y + 12}" width="752" height="32" rx="8" fill="#DCFCE7" stroke="#6EE7B7" stroke-width="1.2"/>
  <text x="1180" y="{axis_y + 32.5}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="11.4" font-weight="800" fill="#047857">LINGKUNGAN SEBENARNYA (TKT 7–9)</text>

  <!-- Horizontal baseline line -->
  <line x1="44" y1="{axis_y}" x2="1556" y2="{axis_y}" stroke="#CBD5E1" stroke-width="3" stroke-linecap="round"/>
  {''.join(connectors_svg)}

  <!-- PEER-REVIEWED RATIONALE BANNER -->
  <rect x="44" y="770" width="1512" height="72" rx="14" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="44" y="770" width="8" height="72" rx="4" fill="#0F766E"/>
  <text x="68" y="797" font-family="'Montserrat', sans-serif" font-size="12.6" font-weight="800" fill="#0F172A">Mengapa Peningkatan TKT BROVER Dilakukan Bertahap?</text>
  <text x="68" y="821" font-family="'Open Sans', sans-serif" font-size="12.2" fill="#334155">Tinjauan sistematis atas 264 publikasi peternakan presisi unggas (Rowe et al., 2019) menyimpulkan teknologi ini belum menjadi kenyataan komersial yang luas.</text>
  <text x="68" y="837" font-family="'Open Sans', sans-serif" font-size="11.8" fill="#475569">Karena itu BROVER diuji bertahap: lab → bak sekam (lingkungan relevan; Mankins, 2009) → kandang mitra, dengan integrasi antarsubsistem sebagai tantangan utama (Olechowski et al., 2020).</text>

  <!-- CLEAN FOOTER -->
  <rect x="44" y="862" width="1512" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="800" y="883.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Definisi TKT: Permenristekdikti No. 42/2016 (Riset Dasar 1–3, Riset Terapan 4–6, Riset Pengembangan 7–9)  |  Mankins (2009), Rowe et al. (2019), Olechowski et al. (2020)</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 07: Business Model Canvas (two subscription packages + buy-out option)
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
        bmc_block(xs[0], top_y, col_w, top_h, "Key Partners", "Mitra Strategis (Calon)", [
            ("PT Zara Propertifarm", "Calon mitra bundling KANOPIS"),
            ("PT Edura Cipta Gemilang", "Dukungan in-kind alat & rakit"),
            ("Lab & Biologi UNJ", "Riset klinis, lab & pengajuan HKI"),
            ("Dinas Pangan & Pertanian", "Kota Cimahi: rencana uji lapangan"),
            ("Dokter Hewan & Pemasok RI", "Validasi gejala; komponen lokal"),
        ], "#0F766E", "#F0FDFA", "#5EEAD4", "#0D9488", ic_handshake),

        bmc_block(xs[1], top_y, col_w, half_h, "Key Activities", "Kegiatan Inti Tim", [
            ("Rakit & QC Unit Rover", "Kamera, servo, tiang sensor & dok"),
            ("Latih & Perbarui Model", "CV feses, set uji foto rover & HP"),
            ("Dukungan Lapangan", "Pasang dok, ganti sensor & baterai"),
            ("Pilot & Protokol Pindah", "Uji kandang mitra & SOP sanitasi"),
        ], "#2563EB", "#EFF6FF", "#93C5FD", "#2563EB", ic_checklist),

        bmc_block(xs[1], top_y + half_h + gap, col_w, half_h, "Key Resources", "Aset & Tim Inti", [
            ("Tim Multidisiplin Asprak", "4 TI ITS + 1 Dokter Hewan UNJ"),
            ("Model CV Feses Apache-2.0", "Set uji lokal berlabel dokter hewan"),
            ("Armada Unit Rover Tim", "Modal unit untuk paket langganan"),
            ("Desain PCB & Server Pusat", "Carrier PCB, casing & VPS lokal"),
        ], "#0284C7", "#F0F9FF", "#7DD3FC", "#0284C7", ic_layers),

        bmc_block(xs[2], top_y, col_w, top_h, "Value Propositions", "Nilai Utama bagi Peternak", [
            ("Skrining Feses", "Foto rover berstandar atau foto HP"),
            ("Udara vs Standar Umur", "Suhu, RH & tren NH₃ vs Cobb/Ross"),
            ("Catatan Harian & Triase", "Deplesi, pakan, air + 3 tombol"),
            ("Laporan 1-Klik Dokter", "Foto, ceklis & grafik (WA/PDF)"),
            ("Bayar Setelah Panen", "Saku Rp75 rb, Kandang Rp750 rb/siklus"),
        ], "#D97706", "#FFFBEB", "#FCD34D", "#D97706", ic_bulb),

        bmc_block(xs[3], top_y, col_w, half_h, "Customer Relations", "Hubungan Pelanggan", [
            ("Pendampingan Pasang", "Instalasi dok & onboarding"),
            ("Dukungan WhatsApp", "Grup peternak & kamus gejala"),
            ("Kunjungan Lapangan", "Ganti sensor, baterai & update model"),
        ], "#7C3AED", "#F5F3FF", "#C4B5FD", "#7C3AED", ic_chat),

        bmc_block(xs[3], top_y + half_h + gap, col_w, half_h, "Channels", "Saluran Distribusi", [
            ("Demo Bersama Dinas", "Uji lapangan Kota Cimahi (rencana)"),
            ("Bundling Kandang", "Mitra pembangun kandang (rencana)"),
            ("TSO, Koperasi & Komunitas", "Poultry shop & grup peternak daring"),
        ], "#6366F1", "#EEF2FF", "#A5B4FC", "#6366F1", ic_truck),

        bmc_block(xs[4], top_y, col_w, top_h, "Customer Segments", "Target Pengguna Utama", [
            ("Peternak Kecil", "3.000–5.000 ekor → BROVER Saku"),
            ("Peternak Menengah–Besar", "≥10.000 ekor → BROVER Kandang"),
            ("Mitra B2B Kandang", "PT Zara / KANOPIS → beli putus"),
            ("Dokter Hewan, TSO & Dinas", "Penerima laporan terstruktur"),
        ], "#059669", "#ECFDF5", "#6EE7B7", "#059669", ic_users),

        bmc_block(m, bot_y, bot_w, bot_h, "Cost Structure", "Struktur Biaya (100% Pengadaan Dalam Negeri)", [
            ("HPP Unit Rover: Rp8,18 jt (eceran) atau ~Rp6,71 jt (grosir + dukungan in-kind PT Edura)", "Modal armada unit langganan; komponen dari e-commerce & distributor lokal RI"),
            ("Biaya Variabel ~Rp171 rb per Siklus per Unit BROVER Kandang", "Dukungan teknis (asumsi Rp100 rb), cadangan sensor & baterai, dok, bagi beban server"),
            ("Server, Pilot & HKI", "VPS ~Rp139 rb/bulan dibagi banyak peternak; biaya pilot & pendaftaran HKI"),
        ], "#BE123C", "#FFF1F2", "#FDA4AF", "#E11D48", ic_receipt),

        bmc_block(m + bot_w + gap, bot_y, bot_w, bot_h, "Revenue Streams", "Dua Paket per Siklus + Opsi Beli Putus", [
            ("BROVER Saku: Rp75.000/siklus, ditagih setelah panen, tanpa perangkat", "Titik impas peternak setara 2,1–3,3 ekor ayam terselamatkan per siklus"),
            ("BROVER Kandang: Rp750.000/siklus, kontrak minimal 6 siklus", "Titik impas peternak 21–33 ekor; modal unit kembali dalam 11,6–14,1 siklus"),
            ("Beli Putus: usulan Rp11,5 jt/unit, termasuk cloud 6 siklus pertama", "Lalu iuran cloud opsional Rp75 rb/siklus; ganti sensor & baterai oleh pemilik"),
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
  <text x="800" y="913.5" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Berbasis Data BPS 2025, Calon Mitra PT Zara / PT Edura / Dinas Pangan dan Pertanian Kota Cimahi, &amp; Riset Harga 28 November 2026</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 08: Clean Project Timeline (no milestone diamonds, year strip, month names,
#             weeks 1-4, one-line tasks; Dec-Feb detail lives in 08b)
# ==============================================================================
def build_svg_08() -> str:
    w = 1920

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

    # 13 one-line tasks (start_week, end_week in [0..40], end exclusive); Dec-Feb rows match Bab 9.7
    tasks = [
        ("1", "Proposal, BMC & Video Purwarupa Tahap 1", 0, 3, "#0D9488", "Berkas & video purwarupa"),
        ("2", "Seleksi Administrasi & Substansi", 2, 4, "#0F766E", "Lolos tahap finalis"),
        ("3", "Bootcamp 4 Modul & Mentoring 3 Pilar", 4, 16, "#2563EB", "Validasi bisnis & teknologi"),
        ("4", "Rover Tahap 2–3: Servo, Tiang Sensor, Dok", 4, 14, "#1D4ED8", "Unit fisik siap uji"),
        ("5", "Model CV Feses Apache-2.0 → RKNN INT8", 4, 14, "#3B82F6", "Model ONNX & RKNN INT8"),
        ("6", "Set Uji Lokal Foto Rover & HP Berpasangan", 7, 14, "#0369A1", "Data berlabel dokter hewan"),
        ("7", "Dasbor Web, Catatan ABK & Laporan 1-Klik", 4, 14, "#0284C7", "Dasbor siap uji"),
        ("8", "Uji Bak Sekam & Kalibrasi SEN0567", 11, 15, "#1E40AF", "Traksi & sensor teruji"),
        ("9", "Jalur Server BROVER Saku & Integrasi KPI", 13, 16, "#1E3A8A", "Purwarupa terintegrasi (M3)"),
        ("10", "Pitch Deck, Demo Alat & Demo Day", 14, 20, "#D97706", "Demonstrasi di depan juri"),
        ("11", "Business Matching, LoI & Pendampingan HKI", 20, 24, "#7C3AED", "Kesepakatan uji tertulis"),
        ("12", "Pilot Mulai Hari ke-7 di Kandang Mitra", 24, 40, "#059669", "Data 1–2 siklus penuh"),
        ("13", "Pendaftaran HKI & Laporan Akhir", 28, 40, "#047857", "Draf HKI & laporan pilot"),
    ]

    hdr_h1 = 30  # Phase row
    hdr_h2 = 22  # Year strip (2026 | 2027)
    hdr_h3 = 26  # Month names (Nov..Agu)
    hdr_h4 = 22  # Week 1..4
    hdr_tot = hdr_h1 + hdr_h2 + hdr_h3 + hdr_h4  # 100px
    row_h = 42
    total_table_h = hdr_tot + len(tasks) * row_h

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
        bh_bar = 26
        by_bar = ry + (row_h - bh_bar) / 2
        bars_svg.append(f'<rect x="{bx1:.1f}" y="{by_bar}" width="{bw:.1f}" height="{bh_bar}" rx="6" fill="{col}" filter="url(#barShadow)"/>')

    # Clean Legend Strip (NO year numbers, NO milestone diamond)
    leg_y = ty + total_table_h + 20
    foot_y = leg_y + 54
    h = foot_y + 36 + 20
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

  <rect x="28" y="{foot_y}" width="1864" height="36" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="960" y="{foot_y + 22.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Kolom 1-4 = Minggu ke-1 s.d. ke-4 Setiap Bulan  |  Rincian Desember–Februari: Gambar 08b (Bab 9.7)  |  Acuan Jadwal: Buku Pedoman Hackathon UNJ 2026, Hal. 4</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 08b: 12-week prototype schedule (Dec 2026 - Feb 2027) with milestones M1-M3
# ==============================================================================
def build_svg_08b() -> str:
    w = 1920
    tx, ty, tw = 28, 76, 1864
    col_no_w, col_task_w, col_pj_w = 46, 610, 200
    gantt_x = tx + col_no_w + col_task_w + col_pj_w
    ww = (tw - col_no_w - col_task_w - col_pj_w) / 12
    hdr_h1, hdr_h2 = 30, 26
    hdr_tot = hdr_h1 + hdr_h2
    row_h, ms_h = 38, 46
    MENTOR, HW, AI, SW = "#94A3B8", "#2563EB", "#0D9488", "#D97706"
    INK, INK2 = "#0F172A", "#334155"

    # (no, task, person in charge, first week, last week inclusive, workstream colour); mirrors Bab 9.7
    tasks = [
        ("1", "Pendampingan: 4 modul bootcamp & mentoring 3 pilar", "Seluruh tim", 1, 12, MENTOR),
        ("2", "Rover Tahap 2: Raspberry Pi 4, servo kamera dua posisi, LED, tiang sensor", "Ahmad", 1, 3, HW),
        ("3", "Firmware: perlambatan sensor jarak, jadwal putaran, mode stasiun", "Ahmad", 2, 6, HW),
        ("4", "CV feses: bersihkan data, latih detektor Apache-2.0, ekspor ONNX, uji RPi 4", "Arya", 1, 6, AI),
        ("5", "Dasbor: standar umur, catatan ABK, ceklis, vaksin, triase, laporan 1-klik", "Aditya", 1, 10, SW),
        ("6", "Mekanik Tahap 3: motor, driver, baterai, ban, casing, carrier PCB", "Ahmad", 3, 8, HW),
        ("7", "Set uji lokal: foto rover & HP berpasangan, label dokter hewan, OPG", "Dr. drh. Atin, Arya", 4, 10, AI),
        ("8", "Migrasi Orange Pi 3B & RKNN INT8", "Arya", 7, 10, AI),
        ("9", "Uji bak sekam lembap", "Ahmad, Arya", 8, 9, HW),
        ("10", "Dok, mode stasiun & uji baterai ≥3 jam", "Ahmad", 9, 10, HW),
        ("11", "Kalibrasi SEN0567 terhadap alat acuan", "Ahmad, Dr. drh. Atin", 9, 11, HW),
        ("12", "Jalur server BROVER Saku (setelah inferensi rover berjalan)", "Arya, Aditya", 10, 12, SW),
        ("13", "Integrasi, uji KPI & sesi pendek di kandang mitra", "Seluruh tim", 10, 12, SW),
        ("14", "Pitch deck, BMC final, video demo & persiapan Demo Day", "Hikari, Aditya", 11, 12, SW),
    ]
    milestones = [(4, "M1"), (8, "M2"), (12, "M3")]
    table_h = hdr_tot + len(tasks) * row_h + ms_h
    ms_y = ty + hdr_tot + len(tasks) * row_h

    hdr = []
    for label, s in [("DESEMBER 2026", 0), ("JANUARI 2027", 4), ("FEBRUARI 2027", 8)]:
        mx = gantt_x + s * ww
        hdr.append(f'<rect x="{mx:.1f}" y="{ty}" width="{4 * ww:.1f}" height="{hdr_h1}" fill="#334155" stroke="#FFFFFF" stroke-width="1.2"/>'
                   f'<text x="{mx + 2 * ww:.1f}" y="{ty + 19.5}" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="11.2" font-weight="800" letter-spacing="0.6" fill="#FFFFFF">{label}</text>')
    for i in range(12):
        wx = gantt_x + i * ww
        hdr.append(f'<rect x="{wx:.1f}" y="{ty + hdr_h1}" width="{ww:.1f}" height="{hdr_h2}" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="0.9"/>'
                   f'<text x="{wx + ww / 2:.1f}" y="{ty + hdr_h1 + 17.5}" text-anchor="middle" font-family="\'Open Sans\', sans-serif" font-size="11" font-weight="700" fill="#475569">{i + 1}</text>')

    grid = []
    for i in range(1, 12):
        gx = gantt_x + i * ww
        strong = i % 4 == 0
        grid.append(f'<line x1="{gx:.1f}" y1="{ty + hdr_tot}" x2="{gx:.1f}" y2="{ty + table_h}" stroke="{"#94A3B8" if strong else "#E2E8F0"}" stroke-width="{1.2 if strong else 0.85}"/>')

    rows, bars = [], []
    for idx, (no, title, pj, s, e, col) in enumerate(tasks):
        ry = ty + hdr_tot + idx * row_h
        bg = "#FFFFFF" if idx % 2 == 0 else "#F8FAFC"
        rows.append(f'<rect x="{tx}" y="{ry}" width="{tw}" height="{row_h}" fill="{bg}"/>'
                    f'<line x1="{tx}" y1="{ry + row_h}" x2="{tx + tw}" y2="{ry + row_h}" stroke="#E2E8F0" stroke-width="1"/>'
                    f'<circle cx="{tx + col_no_w / 2}" cy="{ry + row_h / 2}" r="12" fill="{col}" opacity="0.18"/>'
                    f'<text x="{tx + col_no_w / 2}" y="{ry + row_h / 2 + 4.2}" text-anchor="middle" font-family="\'Montserrat\', sans-serif" font-size="11" font-weight="800" fill="{INK2}">{no}</text>'
                    f'<text x="{tx + col_no_w + 14}" y="{ry + row_h / 2 + 4.4}" font-family="\'Montserrat\', sans-serif" font-size="11.8" font-weight="700" fill="{INK}">{escape(title)}</text>'
                    f'<text x="{tx + col_no_w + col_task_w + 14}" y="{ry + row_h / 2 + 4.4}" font-family="\'Open Sans\', sans-serif" font-size="11.6" font-weight="600" fill="{INK2}">{escape(pj)}</text>')
        bx = gantt_x + (s - 1) * ww + 3
        bw = (e - s + 1) * ww - 6
        bars.append(f'<rect x="{bx:.1f}" y="{ry + 9}" width="{bw:.1f}" height="{row_h - 18}" rx="4" fill="{col}"/>')

    ms = [f'<rect x="{tx}" y="{ms_y}" width="{tw}" height="{ms_h}" fill="#F1F5F9"/>',
          f'<text x="{tx + col_no_w + 14}" y="{ms_y + ms_h / 2 + 4.5}" font-family="\'Montserrat\', sans-serif" font-size="12.2" font-weight="800" fill="{INK}">Milestone (akhir bulan)</text>',
          f'<text x="{tx + col_no_w + col_task_w + 14}" y="{ms_y + ms_h / 2 + 4.4}" font-family="\'Open Sans\', sans-serif" font-size="11.6" font-weight="600" fill="{INK2}">Seluruh tim</text>']
    for wk, lab in milestones:
        mx = gantt_x + wk * ww - 18
        cy = ms_y + ms_h / 2
        ms.append(f'<line x1="{mx:.1f}" y1="{ty + hdr_tot}" x2="{mx:.1f}" y2="{cy - 12:.1f}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4,4" opacity="0.45"/>')
        ms.append(f'<path d="M {mx:.1f} {cy - 10:.1f} L {mx + 10:.1f} {cy:.1f} L {mx:.1f} {cy + 10:.1f} L {mx - 10:.1f} {cy:.1f} Z" fill="{INK}"/>')
        ms.append(f'<text x="{mx - 16:.1f}" y="{cy + 4.5:.1f}" text-anchor="end" font-family="\'Montserrat\', sans-serif" font-size="12" font-weight="800" fill="{INK}">{lab}</text>')

    leg_y = ty + table_h + 18
    items = [(MENTOR, "Pendampingan bootcamp"), (HW, "Rover, sensor & firmware"),
             (AI, "Model CV feses & data uji"), (SW, "Dasbor, server, integrasi & demo")]
    widths = [len(txt) * 7.4 + 60 for _, txt in items] + [len("Milestone") * 7.4 + 60]
    lx = (w - sum(widths) + 36) / 2
    leg = []
    for (col, txt), wd in zip(items, widths):
        leg.append(f'<rect x="{lx:.1f}" y="{leg_y + 11}" width="16" height="16" rx="4" fill="{col}"/>'
                   f'<text x="{lx + 24:.1f}" y="{leg_y + 23.5}" font-family="\'Open Sans\', sans-serif" font-size="12.6" font-weight="600" fill="{INK2}">{escape(txt)}</text>')
        lx += wd
    leg.append(f'<path d="M {lx + 8:.1f} {leg_y + 10} L {lx + 16:.1f} {leg_y + 19} L {lx + 8:.1f} {leg_y + 28} L {lx:.1f} {leg_y + 19} Z" fill="{INK}"/>'
               f'<text x="{lx + 24:.1f}" y="{leg_y + 23.5}" font-family="\'Open Sans\', sans-serif" font-size="12.6" font-weight="600" fill="{INK2}">Milestone</text>')

    box_y = leg_y + 54
    bw3 = (tw - 2 * 16) / 3
    ms_desc = [
        ("M1 · Akhir Desember 2026", "Purwarupa Tahap 2 lulus uji meja: servo dua posisi, sensor",
         "di tiang tampil di dasbor, model baseline berjalan di Raspberry Pi 4"),
        ("M2 · Akhir Januari 2027", "Unit Tahap 3 melintasi bak sekam lembap tanpa kandas; model",
         "RKNN INT8 berjalan di Orange Pi 3B; set uji lokal mulai terkumpul"),
        ("M3 · Akhir Februari 2027", "Purwarupa terintegrasi diuji di lingkungan relevan; KPI Bab 4.4 B",
         "terukur; runtime ≥3 jam; jalur BROVER Saku berjalan bila siap"),
    ]
    boxes = []
    for i, (ttl, l1, l2) in enumerate(ms_desc):
        bx = tx + i * (bw3 + 16)
        boxes.append(f'<rect x="{bx:.1f}" y="{box_y}" width="{bw3:.1f}" height="74" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.3"/>'
                     f'<path d="M {bx + 22:.1f} {box_y + 12} L {bx + 30:.1f} {box_y + 20} L {bx + 22:.1f} {box_y + 28} L {bx + 14:.1f} {box_y + 20} Z" fill="{INK}"/>'
                     f'<text x="{bx + 40:.1f}" y="{box_y + 25}" font-family="\'Montserrat\', sans-serif" font-size="12.4" font-weight="800" fill="{INK}">{escape(ttl)}</text>'
                     f'<text x="{bx + 16:.1f}" y="{box_y + 46}" font-family="\'Open Sans\', sans-serif" font-size="11.4" fill="#475569">{escape(l1)}</text>'
                     f'<text x="{bx + 16:.1f}" y="{box_y + 63}" font-family="\'Open Sans\', sans-serif" font-size="11.4" fill="#475569">{escape(l2)}</text>')

    foot_y = box_y + 74 + 16
    h = foot_y + 34 + 20

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="tableShadow" x="-2%" y="-2%" width="104%" height="105%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <clipPath id="tableClip08b">
      <rect x="{tx}" y="{ty}" width="{tw}" height="{table_h}" rx="14"/>
    </clipPath>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <text x="{w / 2}" y="50" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="27" font-weight="800" fill="#0F172A">Jadwal Pengembangan Purwarupa 3 Bulan (Desember 2026 – Februari 2027)</text>

  <g filter="url(#tableShadow)">
    <rect x="{tx}" y="{ty}" width="{tw}" height="{table_h}" rx="14" fill="#FFFFFF"/>
  </g>
  <g clip-path="url(#tableClip08b)">
    <rect x="{tx}" y="{ty}" width="{col_no_w + col_task_w + col_pj_w}" height="{hdr_tot}" fill="#1E293B"/>
    <text x="{tx + col_no_w / 2}" y="{ty + 34}" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="12.5" font-weight="800" fill="#FFFFFF">No</text>
    <text x="{tx + col_no_w + 14}" y="{ty + 34}" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Kegiatan</text>
    <text x="{tx + col_no_w + col_task_w + 14}" y="{ty + 34}" font-family="'Montserrat', sans-serif" font-size="13.5" font-weight="800" fill="#FFFFFF">Penanggung Jawab</text>
    {''.join(hdr)}
    {''.join(rows)}
    {''.join(ms)}
    <line x1="{tx + col_no_w}" y1="{ty + hdr_tot}" x2="{tx + col_no_w}" y2="{ty + table_h}" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="{tx + col_no_w + col_task_w}" y1="{ty + hdr_tot}" x2="{tx + col_no_w + col_task_w}" y2="{ty + table_h}" stroke="#CBD5E1" stroke-width="1.2"/>
    <line x1="{gantt_x}" y1="{ty + hdr_tot}" x2="{gantt_x}" y2="{ty + table_h}" stroke="#94A3B8" stroke-width="1.4"/>
    {''.join(grid)}
    {''.join(bars)}
  </g>
  <rect x="{tx}" y="{ty}" width="{tw}" height="{table_h}" rx="14" fill="none" stroke="#94A3B8" stroke-width="1.6"/>

  <rect x="{tx}" y="{leg_y}" width="{tw}" height="38" rx="10" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>
  {''.join(leg)}
  {''.join(boxes)}

  <rect x="{tx}" y="{foot_y}" width="{tw}" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{w / 2}" y="{foot_y + 21.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.5" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Kolom 1–12 = Minggu ke-1 s.d. ke-12 Masa Bootcamp &amp; Prototyping  |  Tanggal Modul Mengikuti Pengumuman Panitia  |  Acuan: Buku Pedoman Hackathon UNJ 2026, Hal. 4</text>
</svg>
"""


# ==============================================================================
# DIAGRAM 09: Farmer break-even per package vs normal mortality + price comparison
# ==============================================================================
def build_svg_09() -> str:
    w, h = 1600, 820
    KAND, SAKU, TRACK = "#2563EB", "#D97706", "#CBD5E1"
    INK, INK2, MUTE = "#0F172A", "#334155", "#64748B"
    v_low, v_high = 22_700, 36_200      # Rp per saved bird (Bab 9.2 D)
    lp_x, lp_y, lp_w, lp_h = 36, 92, 960, 664
    lab_x = lp_x + 28
    x0 = lp_x + 300
    x1 = lp_x + lp_w - 70
    vmax = 500.0

    def sx(v: float) -> float:
        return x0 + v / vmax * (x1 - x0)

    # colour, package line, house line, normal deaths (drawn), deaths label, package price, BE label, share label
    rows = [
        (KAND, "BROVER Kandang · Rp750 rb", "Kandang tertutup 10.000 ekor", 247.0, "247 ekor", 750_000, "21–33 ekor", "8,4–13,4%"),
        (KAND, "BROVER Kandang · Rp750 rb", "Kandang tertutup 15.000 ekor", 370.5, "370 ekor", 750_000, "21–33 ekor", "5,6–8,9%"),
        (KAND, "BROVER Kandang · Rp750 rb", "Kandang tertutup 20.000 ekor", 494.0, "494 ekor", 750_000, "21–33 ekor", "4,2–6,7%"),
        (SAKU, "BROVER Saku · Rp75 rb", "Kandang terbuka 3.000 ekor", 136.2, "136 ekor", 75_000, "2,1–3,3 ekor", "1,5–2,4%"),
        (SAKU, "BROVER Saku · Rp75 rb", "Kandang terbuka 5.000 ekor", 227.0, "227 ekor", 75_000, "2,1–3,3 ekor", "0,9–1,5%"),
    ]
    first_yc, step = lp_y + 168, 88
    bar_h = 20
    plot = []
    axis_y = first_yc + (len(rows) - 1) * step + 34
    for tick in range(0, 501, 100):
        gx = sx(tick)
        plot.append(f'<line x1="{gx:.1f}" y1="{first_yc - 44}" x2="{gx:.1f}" y2="{axis_y}" stroke="#E2E8F0" stroke-width="1"/>'
                    f'<text x="{gx:.1f}" y="{axis_y + 18}" text-anchor="middle" font-family="\'Open Sans\', sans-serif" font-size="11" font-weight="600" fill="{MUTE}">{tick}</text>')
    plot.append(f'<line x1="{x0}" y1="{axis_y}" x2="{x1}" y2="{axis_y}" stroke="#94A3B8" stroke-width="1.2"/>')
    plot.append(f'<text x="{(x0 + x1) / 2:.1f}" y="{axis_y + 38}" text-anchor="middle" font-family="\'Open Sans\', sans-serif" font-size="11.4" font-weight="700" fill="{INK2}">Ekor ayam per siklus</text>')

    for i, (col, pkg, house, deaths, deaths_lbl, price, be_lbl, share_lbl) in enumerate(rows):
        yc = first_yc + i * step
        by = yc - bar_h / 2
        be_min, be_max = price / v_high, price / v_low
        x_min = max(sx(be_min), x0 + 2.5)
        x_max = max(sx(be_max), x_min + 1.5)
        plot.append(
            f'<circle cx="{lab_x + 6}" cy="{yc - 10}" r="6" fill="{col}"/>'
            f'<text x="{lab_x + 20}" y="{yc - 6}" font-family="\'Montserrat\', sans-serif" font-size="12.4" font-weight="800" fill="{INK}">{escape(pkg)}</text>'
            f'<text x="{lab_x + 20}" y="{yc + 13}" font-family="\'Open Sans\', sans-serif" font-size="11.6" fill="{INK2}">{escape(house)}</text>'
            f'<text x="{x0}" y="{by - 8}" font-family="\'Open Sans\', sans-serif" font-size="11.4" fill="{INK2}">Titik impas <tspan font-weight="800" fill="{INK}">{escape(be_lbl)}</tspan> = {escape(share_lbl)} dari kematian normal</text>'
            f'<rect x="{x0}" y="{by}" width="{sx(deaths) - x0:.1f}" height="{bar_h}" rx="4" fill="{TRACK}"/>'
            f'<rect x="{x0}" y="{by}" width="{x_max - x0:.1f}" height="{bar_h}" rx="4" fill="{col}" opacity="0.45"/>'
            f'<rect x="{x0}" y="{by}" width="{x_min - x0:.1f}" height="{bar_h}" rx="4" fill="{col}"/>'
            f'<rect x="{x_max:.1f}" y="{by}" width="2" height="{bar_h}" fill="#FFFFFF"/>'
            f'<text x="{sx(deaths) + 8:.1f}" y="{yc + 4.5}" font-family="\'Montserrat\', sans-serif" font-size="12" font-weight="800" fill="{INK}">{deaths_lbl}</text>'
        )

    leg_y = lp_y + 98
    legend = (
        f'<rect x="{lab_x}" y="{leg_y - 11}" width="14" height="14" rx="3" fill="{KAND}"/>'
        f'<text x="{lab_x + 20}" y="{leg_y}" font-family="\'Open Sans\', sans-serif" font-size="11.4" font-weight="600" fill="{INK2}">BROVER Kandang</text>'
        f'<rect x="{lab_x + 142}" y="{leg_y - 11}" width="14" height="14" rx="3" fill="{SAKU}"/>'
        f'<text x="{lab_x + 162}" y="{leg_y}" font-family="\'Open Sans\', sans-serif" font-size="11.4" font-weight="600" fill="{INK2}">BROVER Saku</text>'
        f'<rect x="{lab_x + 268}" y="{leg_y - 11}" width="14" height="14" rx="3" fill="{KAND}" opacity="0.45"/>'
        f'<text x="{lab_x + 288}" y="{leg_y}" font-family="\'Open Sans\', sans-serif" font-size="11.4" font-weight="600" fill="{INK2}">Warna pucat: rentang sampai nilai ayam terendah</text>'
        f'<rect x="{lab_x + 610}" y="{leg_y - 11}" width="14" height="14" rx="3" fill="{TRACK}"/>'
        f'<text x="{lab_x + 630}" y="{leg_y}" font-family="\'Open Sans\', sans-serif" font-size="11.4" font-weight="600" fill="{INK2}">Kematian normal per siklus</text>'
    )

    rx, rw = 1020, 544
    c1_y, c1_h = 92, 214
    c2_y, c2_h = 322, 270
    c3_y, c3_h = 608, 148

    def card(y: float, hh: float, head: str, title: str, tint: str, border: str) -> str:
        return (f'<rect x="{rx}" y="{y}" width="{rw}" height="{hh}" rx="18" fill="{tint}" stroke="{border}" stroke-width="1.8" filter="url(#cardShadow)"/>'
                f'<path d="M{rx + 18} {y} H{rx + rw - 18} Q{rx + rw} {y} {rx + rw} {y + 18} V{y + 46} H{rx} V{y + 18} Q{rx} {y} {rx + 18} {y} Z" fill="{head}"/>'
                f'<text x="{rx + 22}" y="{y + 29}" font-family="\'Montserrat\', sans-serif" font-size="13.6" font-weight="800" fill="#FFFFFF">{escape(title)}</text>')

    def txt(x: float, y: float, s: str, size: float = 11.4, weight: int = 400, fill: str = INK2, anchor: str = "start", font: str = "Open Sans") -> str:
        return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="\'{font}\', sans-serif" font-size="{size}" '
                f'font-weight="{weight}" fill="{fill}">{escape(s)}</text>')

    c1 = (card(c1_y, c1_h, "#0F766E", "Nilai 1 Ekor Ayam Terselamatkan", "#FFFFFF", "#5EEAD4")
          + txt(rx + 22, c1_y + 84, "Rp22.700 – Rp36.200 per ekor", 22, 800, INK, font="Montserrat")
          + txt(rx + 22, c1_y + 112, "= bobot panen 2,0 kg × harga ayam hidup Rp19.500–25.000/kg", 11.6, 600)
          + txt(rx + 22, c1_y + 132, "− sisa pakan ~1,73 kg × harga pakan Rp8.000–9.400/kg", 11.6, 600)
          + txt(rx + 22, c1_y + 158, "Ayam terselamatkan hari ke-21 (0,925 kg); FCR grower–finisher 1,61", 10.6, 400, MUTE)
          + txt(rx + 22, c1_y + 175, "(Zulfan et al., 2025). Harga ayam: Kementan 2026 dan Perbadan 6/2024.", 10.6, 400, MUTE)
          + txt(rx + 22, c1_y + 192, "Harga pakan: asumsi tim dari pernyataan asosiasi peternak di media.", 10.6, 400, MUTE))

    def price_row(y: float, dot: str, ring: bool, name: str, price: str, desc: str) -> str:
        mark = (f'<circle cx="{rx + 30}" cy="{y - 4}" r="6" fill="#FFFFFF" stroke="{dot}" stroke-width="2.4"/>' if ring
                else f'<circle cx="{rx + 30}" cy="{y - 4}" r="6" fill="{dot}"/>')
        return (mark + txt(rx + 44, y, name, 12.4, 800, INK, font="Montserrat")
                + txt(rx + rw - 22, y, price, 12.6, 800, INK, anchor="end", font="Montserrat")
                + txt(rx + 44, y + 19, desc, 11, 400, "#475569"))

    c2 = (card(c2_y, c2_h, "#1D4ED8", "Harga Paket BROVER", "#FFFFFF", "#93C5FD")
          + price_row(c2_y + 78, SAKU, False, "BROVER Saku", "Rp75.000 / siklus", "Foto HP, tanpa perangkat, tanpa kontrak minimum")
          + f'<line x1="{rx + 22}" y1="{c2_y + 110}" x2="{rx + rw - 22}" y2="{c2_y + 110}" stroke="#E2E8F0" stroke-width="1"/>'
          + price_row(c2_y + 138, KAND, False, "BROVER Kandang · Langganan", "Rp750.000 / siklus", "Rover per kandang, minimal 6 siklus, perawatan oleh tim")
          + f'<line x1="{rx + 22}" y1="{c2_y + 170}" x2="{rx + rw - 22}" y2="{c2_y + 170}" stroke="#E2E8F0" stroke-width="1"/>'
          + price_row(c2_y + 198, KAND, True, "BROVER Kandang · Beli Putus", "Usulan Rp11,5 jt / unit", "Termasuk cloud 6 siklus, lalu iuran opsional Rp75 rb/siklus")
          + txt(rx + 22, c2_y + 250, "Ditagih setelah panen, saat RHPP terbit (Amam & Harsita, 2024).", 10.6, 400, MUTE))

    c3 = (card(c3_y, c3_h, "#047857", "Langganan vs Beli Putus selama 3 Tahun (18 Siklus)", "#FFFFFF", "#6EE7B7")
          + txt(rx + 22, c3_y + 76, "Langganan", 12.4, 800, INK, font="Montserrat")
          + txt(rx + rw - 22, c3_y + 76, "Rp13,5 jt", 12.6, 800, INK, anchor="end", font="Montserrat")
          + txt(rx + 22, c3_y + 94, "Rp750 rb × 18 siklus, tanpa modal awal, perawatan oleh tim", 11, 400, "#475569")
          + txt(rx + 22, c3_y + 120, "Beli putus", 12.4, 800, INK, font="Montserrat")
          + txt(rx + rw - 22, c3_y + 120, "~Rp13,3 jt", 12.6, 800, INK, anchor="end", font="Montserrat")
          + txt(rx + 22, c3_y + 138, "Rp11,5 jt + iuran cloud Rp0,9 jt + ganti sensor & baterai ~Rp0,9 jt", 11, 400, "#475569"))

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="cardShadow" x="-3%" y="-3%" width="106%" height="108%">
      <feDropShadow dx="0" dy="2.5" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" fill="#FFFFFF"/>
  <text x="{w / 2}" y="46" text-anchor="middle" font-family="'Montserrat', sans-serif" font-size="26.5" font-weight="800" fill="#0F172A">Titik Impas Paket BROVER bagi Peternak</text>
  <text x="{w / 2}" y="72" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="13.2" fill="#475569">Berapa ekor ayam yang harus terselamatkan per siklus agar biaya paket tertutup? Ini hipotesis pilot, bukan klaim manfaat.</text>

  <rect x="{lp_x}" y="{lp_y}" width="{lp_w}" height="{lp_h}" rx="18" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.6" filter="url(#cardShadow)"/>
  <text x="{lab_x}" y="{lp_y + 34}" font-family="'Montserrat', sans-serif" font-size="16" font-weight="800" fill="{INK}">Titik Impas vs Kematian Normal per Siklus</text>
  <text x="{lab_x}" y="{lp_y + 56}" font-family="'Open Sans', sans-serif" font-size="11.6" fill="#475569">Titik impas = harga paket ÷ nilai 1 ekor ayam terselamatkan (Rp22.700–36.200).</text>
  <text x="{lab_x}" y="{lp_y + 74}" font-family="'Open Sans', sans-serif" font-size="11.6" fill="#475569">Kematian normal: deplesi 2,47% kandang tertutup dan 4,54% kandang terbuka (Zulfan et al., 2025).</text>
  {legend}
  {''.join(plot)}
  <text x="{lab_x}" y="{lp_y + lp_h - 34}" font-family="'Open Sans', sans-serif" font-size="11" fill="{MUTE}">Cara baca: bagian berwarna adalah ayam yang harus terselamatkan agar biaya paket tertutup; abu-abu adalah kematian normal satu siklus.</text>
  <text x="{lab_x}" y="{lp_y + lp_h - 16}" font-family="'Open Sans', sans-serif" font-size="11" fill="{MUTE}">Pengaruh BROVER terhadap kematian belum diukur; pilot membandingkan deplesi dan FCR antarflok bersama dokter hewan.</text>

  {c1}
  {c2}
  {c3}

  <rect x="36" y="{h - 50}" width="{w - 72}" height="34" rx="10" fill="#F1F5F9" stroke="#E2E8F0" stroke-width="1"/>
  <text x="{w / 2}" y="{h - 28.5}" text-anchor="middle" font-family="'Open Sans', sans-serif" font-size="11.2" font-weight="600" fill="#475569">Tim Asprak (ITS &amp; UNJ)  |  Riset Harga 28 November 2026  |  Sumber: Zulfan et al. (2025), Kementan via detikFinance (7 Jul 2026), Perbadan 6/2024  |  Hipotesis Pilot, Bukan Klaim Manfaat</text>
</svg>
"""


def svg_size(svg: str) -> tuple[int, int]:
    m = re.search(r'<svg[^>]*\swidth="(\d+)"\s+height="(\d+)"', svg)
    return int(m.group(1)), int(m.group(2))


def main() -> None:
    os.makedirs(ASSETS_DIR, exist_ok=True)
    for builder, svg_p, png_p, tag in [
        (build_svg_4c, SVG_4C, PNG_4C, "04c User Flow (Kandang & Saku)"),
        (build_svg_06, SVG_06, PNG_06, "06 Roadmap TKT"),
        (build_svg_07, SVG_07, PNG_07, "07 BMC (Saku & Kandang)"),
        (build_svg_08, SVG_08, PNG_08, "08 Timeline 10 Bulan"),
        (build_svg_08b, SVG_08B, PNG_08B, "08b Jadwal Purwarupa 3 Bulan"),
        (build_svg_09, SVG_09, PNG_09, "09 Titik Impas Paket"),
    ]:
        svg_content = builder()
        w, h = svg_size(svg_content)
        with open(svg_p, "w", encoding="utf-8") as f:
            f.write(svg_content)
        render_svg(svg_p, png_p, w, h)
        print(f"GENERATED {tag}: {png_p} ({w}x{h}, {os.path.getsize(png_p)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
