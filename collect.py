# collect.py
import re, json, time, html, sys
from datetime import datetime, timezone
from urllib.parse import urlparse, urlunparse
import requests, feedparser
import feeds
USER_AGENT="RamsNewsBot/1.0"; TIMEOUT=12; MAX_ITEMS=60
def http_head_then_get(url):
  try: return requests.get(url,allow_redirects=True,timeout=TIMEOUT,headers={"User-Agent":USER_AGENT}).url
  except: return url
def canonicalize(u):
  try: u=http_head_then_get(u);p=urlparse(u);path=re.sub(r"/+$","",p.path);return urlunparse((p.scheme,p.netloc.lower(),path,"","",""))
  except: return u
def normalize_title(t): return re.sub(r"\s+"," ",re.sub(r"\s+[–—-]\s+[^|]+$","",html.unescape(t or "").strip()))
def extract_source(e,feed): return (feed or "Unknown")[:60]
def ts_from_entry(e):
  for k in ("published_parsed","updated_parsed"):
    if getattr(e,k,None):
      try: return time.mktime(getattr(e,k))
      except: pass
  return time.time()
def allow_item(t,s): blob=f"{t} {s}".lower(); return any(k.lower() in blob for k in feeds.TEAM_KEYWORDS) and any(s.lower() in blob for s in feeds.SPORT_TOKENS) and not any(b.lower() in blob for b in feeds.EXCLUDE_TOKENS)
def fetch_feed(feed):
  d=feedparser.parse(feed["url"]);out=[]
  for e in d.entries:
    title=normalize_title(getattr(e,"title",""));link=getattr(e,"link","")
    if not title or not link: continue
    out.append({"title":title,"url":canonicalize(link),"source":extract_source(e,feed["name"]),"summary":html.unescape(getattr(e,"summary","")or""),"published":datetime.fromtimestamp(ts_from_entry(e),tz=timezone.utc).isoformat()})
  return out
def dedupe(items): seen=set();out=[]; [out.append(i) for i in items if not (i["title"].lower(),i["url"]) in seen and not seen.add((i["title"].lower(),i["url"]))]; return out
def main():
  all_items=[]; [all_items.extend(fetch_feed(f)) for f in feeds.FEEDS]
  f2=dedupe([i for i in all_items if allow_item(i["title"],i.get("summary",""))])
  f2.sort(key=lambda x:x.get("published",""),reverse=True); f2=f2[:MAX_ITEMS];sources=sorted({i["source"] for i in f2})
  payload={"team":{"name":feeds.TEAM_NAME,"slug":feeds.TEAM_SLUG},"updated_at":datetime.now(timezone.utc).isoformat(),"static_links":feeds.STATIC_LINKS,"items":f2,"sources":sources}
  open("items.json","w").write(json.dumps(payload,indent=2))
if __name__=="__main__": main()