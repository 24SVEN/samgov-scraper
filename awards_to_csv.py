#!/usr/bin/env python3
import csv, time, requests, datetime as dt
from typing import List, Dict

NAICS = "236220 237310 238210"   # keywords
DAYS  = 30
SIZE  = 100

LIST_URL = "https://sam.gov/api/prod/sgs/v1/search/"
HEADERS  = {"User-Agent": "Mozilla/5.0"}

today  = dt.date.today()
since  = today - dt.timedelta(days=DAYS)

PARAMS = {
    "index": "opp",
    "size": SIZE,
    "sort": "-modifiedDate",
    "mode": "search",
    "responseType": "json",
    "q": NAICS,
    "qMode": "ANY",
    "is_active": "true",
    "notice_type": "a",
    "dateFilter": "modifiedDate",
    "modified_date.from": since.strftime("%Y-%m-%d-04:00"),
    "modified_date.to"  : today.strftime("%Y-%m-%d-04:00")
}

def list_page(page: int) -> List[Dict]:
    r = requests.get(LIST_URL, params=PARAMS | {"page": page},
                     headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()["_embedded"]["results"]

rows, pg = [], 0
while True:
    batch = list_page(pg)
    if not batch:
        break
    rows.extend(batch)
    if len(batch) < SIZE:
        break
    pg += 1
    time.sleep(0.3)

print("Rows pulled:", len(rows))

with open("award_notices.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["title", "company", "amount", "naics", "url"])
    for r in rows:
        title   = r.get("title")
        company = r.get("award", {}).get("awardee", {}).get("name")
        amount  = r.get("award", {}).get("amount")
        naics   = r.get("type", {}).get("value") or ""   # fallback
        row_naics = r.get("typeOfSetAsideDescription") \
                     or r.get("naics", [{}])[0].get("code")
        nid     = r.get("_id")              # record id used by UI
        url     = f"https://sam.gov/opp/{nid}/view" if nid else ""
        w.writerow([title, company, amount, row_naics, url])

print("✅  award_notices.csv ready – open it for your outreach list")
