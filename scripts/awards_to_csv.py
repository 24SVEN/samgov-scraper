#!/usr/bin/env python3
"""
sam_award_scraper.py  –  turnkey Award-Notice lead list
"""

import csv, time, requests, datetime as dt, os
from typing import Dict, List, Optional

# ───────── CONFIG ──────────────────────────────────────────────────────────
NAICS_SEARCH = "236220 237310 238210"          # search keywords
DAYS_BACK    = 30
PAGE_SIZE    = 100
PAUSE_LIST   = 0.35                            # seconds between list pages
PAUSE_DETAIL = 0.20                            # seconds between detail calls
# ───────────────────────────────────────────────────────────────────────────

LIST_URL   = "https://sam.gov/api/prod/sgs/v1/search/"
DETAIL_URL = "https://sam.gov/api/prod/opps/v2/opportunities/{}"
HEADERS    = {"User-Agent": "Mozilla/5.0"}

today = dt.date.today()
since = today - dt.timedelta(days=DAYS_BACK)

BASE_PARAMS = {
    "index"              : "opp",
    "size"               : PAGE_SIZE,
    "sort"               : "-modifiedDate",
    "mode"               : "search",
    "responseType"       : "json",
    "notice_type"        : "a",                 # Award Notice
    "q"                  : NAICS_SEARCH,
    "qMode"              : "ANY",
    "is_active"          : "true",
    "dateFilter"         : "modifiedDate",
    "modified_date.from" : since.strftime("%Y-%m-%d-04:00"),
    "modified_date.to"   : today.strftime("%Y-%m-%d-04:00"),
}

# ───────── helpers ─────────────────────────────────────────────────────────
def list_page(page: int) -> List[Dict]:
    r = requests.get(LIST_URL, params=BASE_PARAMS | {"page": page},
                     headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()["_embedded"]["results"]

def fetch_detail(opp_id: str) -> Optional[Dict]:
    r = requests.get(DETAIL_URL.format(opp_id), headers=HEADERS, timeout=20)
    if r.status_code != 200:
        return None
    j = r.json()
    return j.get("data2") or j.get("data") or j

def get_naics(payload: Dict) -> str:
    if payload.get("naics"):
        return ", ".join(
            code
            for blk in payload["naics"]
            for code in blk.get("code", [])
        )
    if payload.get("classificationCodes"):
        return payload["classificationCodes"][0].get("code", "")
    if payload.get("naicsCode"):
        return payload["naicsCode"]
    return ""

def get_id(payload: Dict) -> str:
    return (
        payload.get("opportunityId")
        or payload.get("id")
        or payload.get("_id")
        or payload.get("_links", {}).get("self", {}).get("href", "").split("/")[-1]
    )

# ───────── 1) pull all summaries ───────────────────────────────────────────
summaries, page = [], 0
while True:
    batch = list_page(page)
    if not batch:
        break
    summaries.extend(batch)
    if len(batch) < PAGE_SIZE:
        break
    page += 1
    time.sleep(PAUSE_LIST)

print("Summary rows:", len(summaries))

# ───────── 2) enrich with detail ───────────────────────────────────────────
rows = []
for s in summaries:
    base = {
        "title"  : s.get("title", ""),
        "company": s.get("award", {}).get("awardee", {}).get("name", ""),
        "amount" : s.get("award", {}).get("amount", ""),
        "naics"  : get_naics(s),
        "id"     : get_id(s),
    }

    # if amount or naics missing ⇒ call detail
    if not base["amount"] or not base["naics"]:
        d = fetch_detail(base["id"])
        if d:
            base["company"] = base["company"] or d.get("award", {}).get("awardee", {}).get("name", "")
            base["amount"]  = base["amount"]  or d.get("award", {}).get("amount", "")
            base["naics"]   = base["naics"]   or get_naics(d)
    rows.append(base)
    time.sleep(PAUSE_DETAIL)

print("Detail calls :", len([r for r in rows if not r['amount'] or not r['naics']]))

# ───────── 3) write CSV ────────────────────────────────────────────────────
# Get the absolute path to the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
csv_exports_dir = os.path.join(project_root, "csv_exports")

# Create csv_exports directory if it doesn't exist
os.makedirs(csv_exports_dir, exist_ok=True)

# Use absolute path for CSV file
csv_path = os.path.join(csv_exports_dir, "award_notices.csv")

with open(csv_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["title", "company", "amount", "naics", "url"])
    for r in rows:
        url = f"https://sam.gov/opp/{r['id']}/view" if r["id"] else ""
        w.writerow([r["title"], r["company"], r["amount"], r["naics"], url])

print(f"✅  {csv_path} ready — open it for enrichment & outreach")
