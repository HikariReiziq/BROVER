import re
import sys

LINK = re.compile(r"\[[^\]]*\]\(https?://[^)\s]+\)")

SYMBOLS = {
    "em-dash U+2014": chr(0x2014),
    "en-dash U+2013": chr(0x2013),
    "horizontal bar U+2015": chr(0x2015),
    "petik ganda lurus U+0022": chr(0x22),
    "petik ganda kiri U+201C": chr(0x201C),
    "petik ganda kanan U+201D": chr(0x201D),
    "petik ganda bawah U+201E": chr(0x201E),
    "petik tunggal lurus atau apostrof U+0027": chr(0x27),
    "petik tunggal kiri U+2018": chr(0x2018),
    "petik tunggal kanan U+2019": chr(0x2019),
    "petik sudut U+00AB": chr(0xAB),
    "petik sudut U+00BB": chr(0xBB),
    "aksen grave U+0060 tidak dihitung": None,
    "simbol pasal U+00A7": chr(0xA7),
}

BANNED_WORDS = [
    "wahana", "uav", "patroli", "lan-first", "derau",
    "revolusioner", "game-changer", "game changer", "holistik", "sinergi luar biasa",
    "menjembatani kesenjangan", "lanskap", "terobosan besar", "sangat krusial",
    "mengubah paradigma", "krusial",
]
PATTERNS = [
    r"tidak hanya\b.{0,80}\bmelainkan juga",
    r"bukan hanya\b.{0,80}\btetapi juga",
    r"tidak hanya\b.{0,80}\btetapi juga",
]


def main(path):
    text = open(path, encoding="utf-8").read()
    problems = 0
    for name, ch in SYMBOLS.items():
        if ch is None:
            continue
        n = text.count(ch)
        print("{:<40} {}".format(name, n))
        problems += n
        if n:
            for i, line in enumerate(text.splitlines(), 1):
                if ch in line:
                    print("   baris", i, ":", line.strip()[:140])
    stripped = LINK.sub("", text)
    for ch, name in (("(", "kurung buka di luar tautan"), (")", "kurung tutup di luar tautan")):
        n = stripped.count(ch)
        print("{:<40} {}".format(name, n))
        problems += n
        if n:
            for i, line in enumerate(stripped.splitlines(), 1):
                if ch in line:
                    print("   baris", i, ":", line.strip()[:140])
    for ch, name in (("[", "kurung siku di luar tautan"), ("]", "kurung siku tutup di luar tautan")):
        n = stripped.count(ch)
        print("{:<40} {}".format(name, n))
        problems += n
    low = text.lower()
    for w in BANNED_WORDS:
        n = len(re.findall(r"\b" + re.escape(w) + r"\b", low))
        if n:
            print("kata terlarang", w, n)
            problems += n
    for p in PATTERNS:
        n = len(re.findall(p, low, flags=re.S))
        if n:
            print("pola terlarang", p, n)
            problems += n
    urls_all = re.findall(r"https?://[^\s)\]|]+", text)
    urls_linked = re.findall(r"\]\((https?://[^)\s]+)\)", text)
    print("url total kemunculan", len(urls_all), "| url di sintaks tautan", len(urls_linked),
          "| url bebas di luar tautan", len(urls_all) - len(urls_linked))
    problems += len(urls_all) - len(urls_linked)
    print("TOTAL MASALAH", problems)
    return problems


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
