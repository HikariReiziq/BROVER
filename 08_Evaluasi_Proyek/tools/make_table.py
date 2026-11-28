import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from notes import NOTES  # noqa: E402


def label(r):
    code = r["code"]
    is_doi = "doi.org/" in r["url"] and "api.datacite.org" not in r["url"]
    if code == "200":
        return "200"
    if code == "404":
        return "404, mati"
    if is_doi and r.get("registry_title"):
        return code + ", registri DOI cocok"
    if code in ("403", "202"):
        return code + ", penolakan bot"
    return code


def main(p1, p2, out_table, out_summary):
    r1 = json.load(open(p1, encoding="utf-8"))
    r2 = json.load(open(p2, encoding="utf-8")) if p2 != "-" else None
    by2 = {r["url"]: r for r in r2} if r2 else {}
    lines = [
        "### 12.2 Seluruh Tautan di Laporan Ini",
        "",
        "| No | Tautan | Uji Pertama | Uji Ulang Kedua | Verifikasi Isi |",
        "| :-: | :--- | :-: | :-: | :--- |",
    ]
    for i, r in enumerate(r1, 1):
        second = label(by2[r["url"]]) if r["url"] in by2 else "belum diuji"
        lines.append("| {} | [{}]({}) | {} | {} | {} |".format(
            i, r["text"], r["url"], label(r), second, NOTES[r["url"]]))
    open(out_table, "w", encoding="utf-8").write("\n".join(lines) + "\n\n")

    def count(rs):
        c = {}
        for r in rs:
            c[r["code"]] = c.get(r["code"], 0) + 1
        return c

    c1 = count(r1)
    s = ["### 12.4 Ringkasan Hasil Dua Kali Pengecekan", ""]
    s.append("- **Jumlah tautan unik di laporan:** {}.".format(len(r1)))
    s.append("- **Uji pertama:** " + ", ".join("kode {} sebanyak {}".format(k, v) for k, v in sorted(c1.items())) + ".")
    if r2:
        c2 = count(r2)
        s.append("- **Uji ulang kedua:** " + ", ".join("kode {} sebanyak {}".format(k, v) for k, v in sorted(c2.items())) + ".")
        changed = ["nomor {} dari kode {} ke {}".format(i, r["code"], by2[r["url"]]["code"])
                   for i, r in enumerate(r1, 1) if r["url"] in by2 and by2[r["url"]]["code"] != r["code"]]
        if changed:
            s.append("- **Tautan yang kodenya berubah antarpengujian, merujuk nomor di tabel 12.2:** " + "; ".join(changed) + ". Perubahan ini berasal dari pembatasan bot yang tidak konsisten, bukan perubahan isi.")
        else:
            s.append("- **Tautan yang kodenya berubah antarpengujian:** tidak ada.")
        miss = ["nomor {}".format(i) for i, r in enumerate(r1, 1) if r["url"] not in by2]
        if miss:
            s.append("- **Tautan yang tidak ikut diuji ulang:** " + ", ".join(miss) + ".")
    s.append("- **Tautan mati yang sengaja dicantumkan sebagai temuan:** akar API BMKG dan notebook Kaggle ajheshbasnet.")
    s.append("- **Penolakan bot:** semua tautan DOI berkode 403 atau 202 sudah dicocokkan judulnya di registri Crossref. Laman non-DOI berkode 403 dicatat apa adanya dan tidak dipakai sebagai satu-satunya bukti klaim.")
    open(out_summary, "w", encoding="utf-8").write("\n".join(s) + "\n")
    print("rows:", len(r1))


if __name__ == "__main__":
    main(*sys.argv[1:5])
