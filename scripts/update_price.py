#!/usr/bin/env python3
import json, re, sys, html, datetime, urllib.request, pathlib

URL = "https://cac.bcr.com.ar/es"
OUT = pathlib.Path(__file__).resolve().parent.parent / "prices.json"


def fetch():
    req = urllib.request.Request(URL, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
        "Accept-Language": "es-AR,es;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def to_text(raw):
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw))


def parse(text):
    m = re.search(r"Pizarra\s+del\s+d[ií]a\s+(\d{1,2})/(\d{1,2})/(\d{4})", text, re.I)
    if not m:
        raise ValueError("No encontre el encabezado 'Precios Pizarra del dia'")
    d, mo, y = map(int, m.groups())
    date = datetime.date(y, mo, d).isoformat()
    rest = text[m.end():]
    s = re.search(r"\bSoja\b\s*\$\s*([\d.]+,\d{2})", rest)
    if not s:
        raise ValueError("No encontre el precio de la soja")
    price = float(s.group(1).replace(".", "").replace(",", "."))
    if not (50000 <= price <= 5000000):
        raise ValueError("Precio fuera de rango: %r" % price)
    return date, round(price)


def main():
    date, price = parse(to_text(fetch()))
    try:
        data = json.loads(OUT.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    by = data.get("byMonth") or {}
    by[date[:7]] = {"date": date, "pricePerTn": price}
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data.update({
        "product": "soja", "currency": "ARS", "pricePerTn": price, "priceDate": date,
        "checkedAt": now, "source": URL,
        "sourceName": "Camara Arbitral de Cereales (BCR), pizarra Rosario", "byMonth": by,
    })
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Soja %s: $%s/tn" % (date, price))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e, file=sys.stderr)
        sys.exit(1)
