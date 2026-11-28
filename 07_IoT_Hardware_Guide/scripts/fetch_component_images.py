#!/usr/bin/env python3
"""
Download and normalize clean, verified product photos (.jpg) for BROVER IoT Hardware Guides
from official electronics catalogs (Adafruit, Pololu, DFRobot Wiki, Wikimedia Commons, Orange Pi).
Produces uniform 480x360 white-background JPEGs + visual QA contact sheets.
"""

import concurrent.futures
import io
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

BASE_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = BASE_DIR.parent
POC_DIR = BASE_DIR / "assets" / "poc"
FINAL_DIR = BASE_DIR / "assets" / "final"
QA_DIR = Path("/home/reiziqzip/.gemini/antigravity/brain/ffd17c72-881e-40a0-8df5-7a52a98eb8d6/scratch")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}
WIKI_HEADERS = {
    "User-Agent": "BROVER-IoT-Hardware-Guide/1.0 (https://github.com/HikariReiziq/BROVER; educational)"
}

CTX = ssl._create_unverified_context()


def normalize_to_jpg(img_bytes: bytes, out_path: Path, size=(480, 360)) -> bool:
    try:
        im = Image.open(io.BytesIO(img_bytes))
        im.load()
        if im.width < 120 or im.height < 120:
            return False
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
            im = Image.alpha_composite(bg, im.convert("RGBA")).convert("RGB")
        else:
            im = im.convert("RGB")

        im = ImageOps.contain(im, (size[0] - 24, size[1] - 24), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", size, (255, 255, 255))
        canvas.paste(im, ((size[0] - im.width) // 2, (size[1] - im.height) // 2))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(out_path, format="JPEG", quality=88, optimize=True)
        return out_path.stat().st_size > 3500
    except Exception:
        return False


def download_bytes(url: str, headers=None) -> bytes:
    req = urllib.request.Request(url, headers=headers or HEADERS)
    with urllib.request.urlopen(req, timeout=12, context=CTX) as r:
        return r.read(8_000_000)


def search_adafruit(query: str, index: int = 0) -> list[str]:
    url = f"https://www.adafruit.com/search?q={urllib.parse.quote_plus(query)}"
    body = download_bytes(url).decode("utf-8", "ignore")
    thumbs = list(dict.fromkeys(re.findall(r'https://cdn-shop\.adafruit\.com/310x233/[0-9]+-[0-9]+\.jpg', body)))
    if not thumbs:
        thumbs = list(dict.fromkeys(re.findall(r'https://cdn-shop\.adafruit\.com/(?:970x728|640x480|310x233)/[^\s"\'<>]+\.jpg', body)))
    hd = [u.replace("/310x233/", "/970x728/") for u in thumbs]
    if index < len(hd):
        hd = [hd[index]] + hd[:index] + hd[index + 1:]
    return hd[:5]


def search_pololu(query: str, index: int = 0) -> list[str]:
    url = f"https://www.pololu.com/search?query={urllib.parse.quote_plus(query)}"
    body = download_bytes(url).decode("utf-8", "ignore")
    thumbs = list(dict.fromkeys(re.findall(r'https://a\.pololu-files\.com/picture/0J[0-9]+\.[0-9]+\.(?:jpg|png)', body)))
    hd = [re.sub(r'\.\d+\.(jpg|png)$', r'.600.\1', u) for u in thumbs]
    if index < len(hd):
        hd = [hd[index]] + hd[:index] + hd[index + 1:]
    return hd[:5]


def search_wikimedia(query: str, index: int = 0) -> list[str]:
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrnamespace": "6",
        "gsrsearch": query,
        "gsrlimit": "8",
        "prop": "imageinfo",
        "iiprop": "url|mime",
        "iiurlwidth": "600",
        "format": "json",
    })
    url = f"https://commons.wikimedia.org/w/api.php?{params}"
    data = json.loads(download_bytes(url, headers=WIKI_HEADERS).decode("utf-8", "ignore"))
    pages = data.get("query", {}).get("pages", {})
    # Sort by search index
    ordered = sorted(pages.values(), key=lambda p: p.get("index", 999))
    urls = []
    for p in ordered:
        title = (p.get("title") or "").lower()
        if any(bad in title for bad in ("pinout", "diagram", "schematic", "logo", "icon", "svg")):
            continue
        for info in p.get("imageinfo", []):
            mime = info.get("mime", "")
            if mime in ("image/jpeg", "image/png", "image/webp"):
                u = info.get("thumburl") or info.get("url")
                if u:
                    urls.append(u)
    if index < len(urls):
        urls = [urls[index]] + urls[:index] + urls[index + 1:]
    return urls[:5]


# Each entry: (filename, list_of_(source_type, value, optional_index))
POC_SPECS = [
    ("01_esp32_devkit_v1_30pin.jpg", [("wikimedia", "ESP32 DevKit V1 DOIT", 0), ("adafruit", "ESP32-WROOM-32", 0)]),
    ("02_raspberry_pi_4.jpg", [("adafruit", "Raspberry Pi 4 Model B 4GB", 0), ("wikimedia", "Raspberry Pi 4 Model B", 0)]),
    ("03_chassis_4wd_acrylic_tt_motor.jpg", [("local", str(REPO_ROOT / "06_Project_Concept_BROVER/assets/04d_ilustrasi_rover_4wd_poc.png"), 0)]),
    ("04_tb6612fng_motor_driver.jpg", [("adafruit", "TB6612 1.2A DC Stepper Motor Driver Breakout", 0), ("pololu", "TB6612FNG", 0)]),
    ("05_esp32_c3_super_mini.jpg", [("wikimedia", "ESP32-C3 SuperMini", 0), ("adafruit", "QT Py ESP32-C3", 0)]),
    ("06_webcam_usb.jpg", [("wikimedia", "Logitech USB webcam", 0), ("adafruit", "USB webcam", 0)]),
    ("07_servo_sg90_mg90s.jpg", [("adafruit", "Micro Servo MG90S", 0), ("pololu", "micro servo metal gear", 0)]),
    ("08_led_strip_5v_5000k.jpg", [("adafruit", "5V white COB LED strip", 0), ("adafruit", "white LED strip 5V", 0)]),
    ("09_mosfet_switch_module.jpg", [("pololu", "MOSFET power switch", 0), ("adafruit", "MOSFET driver", 0)]),
    ("11_sht31_i2c_sensor.jpg", [("adafruit", "Sensirion SHT31-D Temperature Humidity", 0)]),
    ("12_dfrobot_sen0567_nh3.jpg", [("direct", "https://dfimg.dfrobot.com/enshop/SEN0567/SEN0567_Main_01_1200x630.jpg.webp", 0)]),
    ("13_hc_sr04_ultrasonic.jpg", [("adafruit", "HC-SR04 Ultrasonic", 0), ("pololu", "HC-SR04", 0)]),
    ("14_powerbank_5v_3a.jpg", [("adafruit", "USB battery pack 10000mAh", 0), ("wikimedia", "power bank USB", 0)]),
    ("15_usb_c_cable_3a.jpg", [("adafruit", "USB-C cable", 0)]),
    ("16_battery_18650.jpg", [("wikimedia", "18650 lithium ion battery Samsung", 0), ("adafruit", "18650 battery", 0)]),
    ("17_holder_18650_2s.jpg", [("pololu", "2-cell 18650 battery holder", 0), ("adafruit", "18650 battery holder", 0)]),
    ("18_bms_2s_10a.jpg", [("wikimedia", "BMS 2S 18650", 0), ("adafruit", "Li-Ion battery protection board", 0)]),
    ("19_buck_xl4015_5a.jpg", [("wikimedia", "buck converter DC-DC step down", 0), ("pololu", "5V 5A step-down voltage regulator", 0)]),
    ("20_charger_18650_liitokala.jpg", [("wikimedia", "LiitoKala 18650 charger", 0), ("adafruit", "18650 battery charger", 0)]),
    ("21_silicone_wire_18awg.jpg", [("adafruit", "silicone cover stranded core wire 18AWG", 0), ("pololu", "18 AWG silicone wire", 0)]),
    ("22_jumper_wires_dupont.jpg", [("adafruit", "premium jumper wires", 0), ("pololu", "jumper wires", 0)]),
    ("23_resistor_kit.jpg", [("adafruit", "through-hole resistors kit", 0), ("wikimedia", "metal film resistor", 0)]),
    ("24_electrolytic_capacitor.jpg", [("adafruit", "electrolytic capacitor 470uF", 0), ("wikimedia", "electrolytic capacitor", 0)]),
    ("25_ceramic_capacitor_100nf.jpg", [("adafruit", "0.1uF ceramic capacitor", 0), ("wikimedia", "ceramic capacitor 104", 0)]),
    ("26_perfboard_pcb.jpg", [("adafruit", "perma-proto perfboard", 0), ("wikimedia", "perfboard PCB", 0)]),
    ("27_pin_header_terminal_block.jpg", [("adafruit", "female header 2.54mm", 0), ("pololu", "terminal block 2-pin", 0)]),
    ("28_xt30_jst_xh_connector.jpg", [("pololu", "XT30 connector", 0), ("adafruit", "JST XH connector", 0)]),
    ("29_fuse_5a_holder.jpg", [("pololu", "blade fuse holder", 0), ("wikimedia", "inline blade fuse holder", 0)]),
    ("30_rocker_switch_10a.jpg", [("adafruit", "mini panel mount rocker switch", 0), ("pololu", "rocker switch", 0)]),
    ("31_heatshrink_standoff_m3.jpg", [("adafruit", "heat shrink pack", 0), ("pololu", "M3 brass standoff", 0)]),
    ("32_soldering_iron.jpg", [("adafruit", "adjustable soldering iron", 0)]),
    ("33_solder_tin_wire.jpg", [("adafruit", "rosin core solder spool", 0)]),
    ("34_solder_flux_paste.jpg", [("adafruit", "no-clean flux", 0)]),
    ("35_desoldering_pump.jpg", [("adafruit", "solder sucker", 0)]),
    ("36_digital_multimeter.jpg", [("adafruit", "digital multimeter", 0)]),
    ("37_wire_stripper_cutter.jpg", [("adafruit", "wire stripper", 0)]),
    ("38_breadboard_830.jpg", [("adafruit", "full sized breadboard", 0)]),
]

FINAL_SPECS = [
    ("01_orange_pi_3b.jpg", [("wikimedia", "Orange Pi 3B", 0), ("wikimedia", "Orange Pi 3", 0)]),
    ("02_wifi_antenna_24ghz.jpg", [("adafruit", "2.4GHz SMA antenna uFL", 0), ("pololu", "2.4GHz antenna SMA", 0)]),
    ("03_esp32_wroom32.jpg", [("wikimedia", "ESP32 DevKit V1 DOIT", 0), ("adafruit", "ESP32-WROOM-32", 0)]),
    ("04_custom_carrier_pcb.jpg", [("wikimedia", "printed circuit board green KiCad", 0), ("adafruit", "custom PCB breakout", 0)]),
    ("05_conformal_coating.jpg", [("wikimedia", "conformal coating PCB", 0), ("adafruit", "MG Chemicals silicone conformal coating", 0)]),
    ("06_jgb37_520_motor.jpg", [("pololu", "37D metal gearmotor 12V", 0)]),
    ("07_motor_bracket_37mm.jpg", [("pololu", "37D metal gearmotor bracket", 0)]),
    ("08_bts7960_motor_driver.jpg", [("direct", "https://deepbluembedded.com/wp-content/uploads/2024/01/BTS7960-DC-Motor-Driver.jpg", 0), ("pololu", "high power motor driver 40A", 0)]),
    ("09_rc_crawler_wheels_120mm.jpg", [("pololu", "120mm wheel 12mm hex", 0), ("wikimedia", "RC crawler wheel tire", 0)]),
    ("10_ip65_enclosure_box.jpg", [("adafruit", "waterproof enclosure box IP65", 0), ("wikimedia", "junction box IP65 waterproof", 0)]),
    ("11_petg_3d_print.jpg", [("adafruit", "PETG 3D printer filament", 0), ("wikimedia", "PETG filament 3D printing", 0)]),
    ("12_imx291_usb_camera.jpg", [("adafruit", "USB camera module 1080p", 0), ("wikimedia", "USB camera module board", 0)]),
    ("13_ds3218_waterproof_servo.jpg", [("pololu", "high torque waterproof metal gear servo", 0), ("adafruit", "high torque metal gear servo", 0)]),
    ("14_cob_led_5v.jpg", [("adafruit", "5V white COB LED", 0), ("adafruit", "white LED backlight module", 0)]),
    ("16_fs304_sht31_probe.jpg", [("adafruit", "SHT-30 mesh-protected weather-proof temperature humidity sensor", 0)]),
    ("17_dfrobot_sen0567_nh3.jpg", [("direct", "https://dfimg.dfrobot.com/enshop/SEN0567/SEN0567_Main_01_1200x630.jpg.webp", 0)]),
    ("18_dfrobot_a02yyuw_ip67.jpg", [("direct", "https://dfimg.dfrobot.com/enshop/SEN0311/SEN0311_Main_01_1200x630.jpg.webp", 0)]),
    ("19_lifepo4_4s_12v_6ah.jpg", [("wikimedia", "LiFePO4 12V battery", 0), ("adafruit", "LiFePO4 battery", 0)]),
    ("20_lifepo4_charger_146v.jpg", [("wikimedia", "lithium battery charger adapter 12V", 0), ("pololu", "12V power adapter charger", 0)]),
    ("21_xl4015_buck_5a.jpg", [("pololu", "5V 5A step-down voltage regulator", 0), ("wikimedia", "buck converter DC-DC step down", 0)]),
    ("22_ina219_current_sensor.jpg", [("adafruit", "INA219 High Side DC Current Sensor", 0)]),
    ("23_xt60_gx16_cable_gland.jpg", [("adafruit", "waterproof cable gland PG7", 0), ("pololu", "XT60 connector", 0)]),
    ("24_fuse_15a_kill_switch_ip65.jpg", [("adafruit", "emergency stop switch mushroom", 0), ("wikimedia", "emergency stop button red", 0)]),
    ("25_cleaning_dock_brush_sprayer.jpg", [("wikimedia", "pressure sprayer garden bottle", 0), ("wikimedia", "scrub brush cleaning", 0)]),
]


def fetch_spec(out_dir: Path, filename: str, sources: list) -> tuple[str, bool, str]:
    out_path = out_dir / filename
    for stype, val, idx in sources:
        try:
            if stype == "local":
                data = Path(val).read_bytes()
                if normalize_to_jpg(data, out_path):
                    return (filename, True, f"local:{Path(val).name}")
            elif stype == "direct":
                data = download_bytes(val)
                if normalize_to_jpg(data, out_path):
                    return (filename, True, val)
            elif stype == "adafruit":
                for u in search_adafruit(val, idx):
                    try:
                        if normalize_to_jpg(download_bytes(u), out_path):
                            return (filename, True, u)
                    except Exception:
                        continue
            elif stype == "pololu":
                for u in search_pololu(val, idx):
                    try:
                        if normalize_to_jpg(download_bytes(u), out_path):
                            return (filename, True, u)
                    except Exception:
                        continue
            elif stype == "wikimedia":
                for u in search_wikimedia(val, idx):
                    try:
                        if normalize_to_jpg(download_bytes(u, headers=WIKI_HEADERS), out_path):
                            return (filename, True, u)
                    except Exception:
                        continue
        except Exception:
            continue
    return (filename, False, "all sources failed")


def make_contact_sheet(folder: Path, specs: list, out_file: Path, cols: int = 5):
    thumb_w, thumb_h = 260, 220
    rows = (len(specs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * thumb_h), (240, 244, 248))
    draw = ImageDraw.Draw(sheet)
    for idx, (fname, _) in enumerate(specs):
        r, c = divmod(idx, cols)
        x0, y0 = c * thumb_w, r * thumb_h
        draw.rectangle([x0 + 4, y0 + 4, x0 + thumb_w - 4, y0 + thumb_h - 4], fill=(255, 255, 255), outline=(200, 210, 220))
        p = folder / fname
        if p.exists():
            im = Image.open(p)
            im = ImageOps.contain(im, (thumb_w - 20, thumb_h - 44), Image.Resampling.LANCZOS)
            sheet.paste(im, (x0 + (thumb_w - im.width) // 2, y0 + 8 + (thumb_h - 44 - im.height) // 2))
        else:
            draw.text((x0 + 20, y0 + 80), "MISSING", fill=(220, 38, 38))
        draw.text((x0 + 10, y0 + thumb_h - 28), fname.replace(".jpg", "")[:32], fill=(15, 23, 42))
    out_file.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_file, format="JPEG", quality=85)


def main():
    POC_DIR.mkdir(parents=True, exist_ok=True)
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    tasks = [(POC_DIR, f, s) for f, s in POC_SPECS] + [(FINAL_DIR, f, s) for f, s in FINAL_SPECS]
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(fetch_spec, d, f, s) for d, f, s in tasks]
        for fut in concurrent.futures.as_completed(futs):
            res = fut.result()
            results.append(res)
            print(f"[{'OK' if res[1] else 'FAIL'}] {res[0]} -> {res[2][:95]}")

    ok = sum(1 for r in results if r[1])
    fail = [r for r in results if not r[1]]
    print(f"\nSUMMARY: {ok}/{len(results)} succeeded, {len(fail)} failed.")
    if fail:
        print("FAILED:", fail)

    make_contact_sheet(POC_DIR, POC_SPECS[:20], QA_DIR / "qa_poc_part1.jpg", cols=5)
    make_contact_sheet(POC_DIR, POC_SPECS[20:], QA_DIR / "qa_poc_part2.jpg", cols=5)
    make_contact_sheet(FINAL_DIR, FINAL_SPECS, QA_DIR / "qa_final.jpg", cols=5)
    print("Contact sheets saved to", QA_DIR)


if __name__ == "__main__":
    main()
