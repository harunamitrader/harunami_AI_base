import json
import os
from datetime import datetime

base_url = "https://harunamitrader.github.io/harunami_AI_base" # 推定URL
json_path = "data/articles.json"
rss_path = "feed.xml"

def generate_rss():
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    articles = sorted(data["articles"], key=lambda x: x["publishedAt"], reverse=True)[:20]

    now = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    rss_items = []
    for a in articles:
        # 相対パスを絶対URLに変換
        link = f"{base_url}/{a['articleUrl'].lstrip('./')}"
        pub_date = datetime.strptime(a["publishedAt"], "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 GMT")
        
        item = f"""    <item>
      <title><![CDATA[{a['title']}]]></title>
      <link>{link}</link>
      <guid isPermaLink="true">{link}</guid>
      <category>{a['category']}</category>
      <pubDate>{pub_date}</pubDate>
      <description><![CDATA[{a.get('dek') or a.get('summary') or ''}]]></description>
    </item>"""
        rss_items.append(item)

    rss_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>harunami AI base</title>
    <link>{base_url}</link>
    <description>AI関連の情報を集約するポータルサイトの更新情報</description>
    <language>ja</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml" />
{chr(10).join(rss_items)}
  </channel>
</rss>"""

    with open(rss_path, "w", encoding="utf-8") as f:
        f.write(rss_template)
    
    print(f"Successfully generated {rss_path}")

if __name__ == "__main__":
    generate_rss()
