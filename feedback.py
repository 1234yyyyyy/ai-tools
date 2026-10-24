#!/usr/bin/env python3
"""讀 GitHub not-important issues -> /workspace/ai-tools/not_interested.json（冪等，以 link 去重；分類/主題從 index.html 卡片補）"""
import json, re, subprocess, os, html
D = "/workspace/ai-tools"; REPO = "1234yyyyyy/ai-tools"; OUT = f"{D}/not_interested.json"
src = open(f"{D}/index.html", encoding="utf-8").read()
lib = {}
for m in re.finditer(r'<a class="c" href="([^"]+)" data-cat="([^"]*)".*?<div class="n">\d+\. (.*?)</div>.*?<span class="k">(.*?)</span>', src, re.S):
    lib[html.unescape(m.group(1))] = {"category": html.unescape(m.group(2)), "title": html.unescape(m.group(3)), "tags": html.unescape(m.group(4))}
STOP = set("the a an of to and in on for with is are by from at ai 的 了 和 與 在 是".split())
def kw(t):
    ws = re.findall(r"[A-Za-z][A-Za-z0-9.+-]{1,}|[\u4e00-\u9fff]{2,}", t)
    return [w for w in dict.fromkeys(w.lower() for w in ws) if w not in STOP][:30]
js = json.loads(subprocess.check_output(["gh","issue","list","-R",REPO,"--label","not-important","--state","all","--limit","500","--json","number,title,body,createdAt,state"]))
rows = {r["link"]: r for r in json.load(open(OUT, encoding="utf-8"))["items"]} if os.path.exists(OUT) else {}
for iss in js:
    for line in (iss.get("body") or "").splitlines():
        m = re.search(r"https?://\S+", line)
        if not m: continue
        link = m.group(0).rstrip(").,")
        mm = re.match(r"\s*-\s*\[([^\]]*)\]\s*(.*?)\s*\|\s*https?://", line)
        cat, title = (mm.group(1), mm.group(2)) if mm else ("", "")
        L = lib.get(link, {})
        title = title or L.get("title", ""); cat = cat or L.get("category", "")
        tags = L.get("tags", "")
        rows.setdefault(link, {"date": iss["createdAt"][:10], "title": title, "link": link, "category": cat,
            "hashtags": re.findall(r"#\S+", tags), "keywords": kw(title + " " + re.sub(r"#\S+", "", tags)), "issue": iss["number"]})
items = sorted(rows.values(), key=lambda r: r["date"])
json.dump({"updated_from": REPO, "count": len(items), "categories": sorted({r["category"] for r in items}), "items": items},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(items)} not-interested items -> {OUT}; open issues: {[i['number'] for i in js if i['state']=='OPEN']}")
