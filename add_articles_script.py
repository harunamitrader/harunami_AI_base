import json
import os
import re
from datetime import datetime

base_dir = r"C:\Users\sgmxk\Desktop\AI\repos\github\harunamitrader\harunami_AI_base"

# New articles data
new_articles = [
    {
        "category": "ai-tool-log",
        "slug": "2026-04-09-openclaw-v2026-4-8",
        "title": "OpenClaw v2026.4.8: メディア生成機能の拡充とDreaming機能の進化",
        "dek": "動画・音楽生成ツールの追加や、3段階のDreaming（メモリ保守）機能が実装された大型アップデート。",
        "summary": "OpenClawの2026年4月のアップデート。メディア生成（動画・音楽）プロバイダーの追加、Dreaming機能の3フェーズ化、CLI強化などが実施されました。",
        "publishedAt": "2026-04-09",
        "createdAt": "2026-04-09T10:00:00+09:00",
        "toolName": "OpenClaw",
        "articleUrl": "./articles/tools/2026-04-09-openclaw-v2026-4-8.html",
        "serial": 999,
        "html_content": """<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>OpenClaw v2026.4.8: メディア生成機能の拡充とDreaming機能の進化</title>
    <link rel="stylesheet" href="../../styles.css" />
  </head>
  <body>
    <article class="article-shell">
      <div class="article-topline">
        <a class="article-back" href="../../ai-tools-monitor.html">AI Tools Monitor</a>
        <p class="eyebrow">Release Notes</p>
      </div>
      <h1 class="article-title">OpenClaw v2026.4.8: メディア生成機能の拡充とDreaming機能の進化</h1>
      <p class="article-dek">動画・音楽生成ツールの追加や、3段階のDreaming（メモリ保守）機能が実装された大型アップデート。</p>
      <div class="article-meta-grid">
        <div class="article-meta-item"><span class="meta-label">公開日</span><strong>2026-04-09</strong></div>
        <div class="article-meta-item"><span class="meta-label">ツール</span><strong>OpenClaw</strong></div>
      </div>
      <div class="article-body">
        <h2>メディア生成の強化</h2>
        <p>新しく `video_generate` および `music_generate` ツールが追加され、エージェントが動画や音楽を自律的に生成できるようになりました。ComfyUIやRunwayなどの複数プロバイダーに対応し、自動フォールバックも可能です。</p>
        <h2>Dreamingメモリ機能の進化</h2>
        <p>「Light」「Deep」「REM」の3フェーズにDreaming機能が再編され、バックグラウンドでの効率的なメモリ昇格とタグ付けが可能になりました。</p>
      </div>
    </article>
  </body>
</html>"""
    },
    {
        "category": "ai-tool-log",
        "slug": "2026-04-09-chatgpt-security-codex",
        "title": "ChatGPT: Windowsサンドボックスのセキュリティ強化とCodex CLI改善",
        "dek": "OSレベルのネットワーク出力制限の導入や、デバイスコードフローを用いたサインイン機能が追加されました。",
        "summary": "ChatGPTの最新アップデート。Windowsサンドボックスのセキュリティ強化、Codex CLIの標準入力対応、外部アプリ連携の強化などが行われました。",
        "publishedAt": "2026-04-09",
        "createdAt": "2026-04-09T10:05:00+09:00",
        "toolName": "ChatGPT",
        "articleUrl": "./articles/tools/2026-04-09-chatgpt-security-codex.html",
        "serial": 999,
        "html_content": """<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ChatGPT: Windowsサンドボックスのセキュリティ強化とCodex CLI改善</title>
    <link rel="stylesheet" href="../../styles.css" />
  </head>
  <body>
    <article class="article-shell">
      <div class="article-topline">
        <a class="article-back" href="../../ai-tools-monitor.html">AI Tools Monitor</a>
        <p class="eyebrow">Release Notes</p>
      </div>
      <h1 class="article-title">ChatGPT: Windowsサンドボックスのセキュリティ強化とCodex CLI改善</h1>
      <p class="article-dek">OSレベルのネットワーク出力制限の導入や、デバイスコードフローを用いたサインイン機能が追加されました。</p>
      <div class="article-meta-grid">
        <div class="article-meta-item"><span class="meta-label">公開日</span><strong>2026-04-09</strong></div>
        <div class="article-meta-item"><span class="meta-label">ツール</span><strong>ChatGPT</strong></div>
      </div>
      <div class="article-body">
        <h2>セキュリティと運用の強化</h2>
        <p>Windowsサンドボックスに対してOSレベルの出力ルールが導入され、プロキシ経由のみのネットワーク接続を強制できるようになりました。また、ブラウザベースのログインが困難な環境向けにデバイスコードフローによるサインインがサポートされました。</p>
      </div>
    </article>
  </body>
</html>"""
    },
    {
        "category": "ai-tool-log",
        "slug": "2026-04-09-claude-managed-agents",
        "title": "Claude Platform: Managed Agentsとant CLIのパブリックベータ公開",
        "dek": "自律型エージェントをサンドボックスで安全に実行するフルマネージド基盤と、API管理用CLIがリリースされました。",
        "summary": "Claude APIのアップデート。自律型エージェントのフルマネージド実行環境「Claude Managed Agents」と、新しいコマンドラインクライアント「ant CLI」が発表されました。",
        "publishedAt": "2026-04-09",
        "createdAt": "2026-04-09T10:10:00+09:00",
        "toolName": "Claude",
        "articleUrl": "./articles/tools/2026-04-09-claude-managed-agents.html",
        "serial": 999,
        "html_content": """<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Claude Platform: Managed Agentsとant CLIのパブリックベータ公開</title>
    <link rel="stylesheet" href="../../styles.css" />
  </head>
  <body>
    <article class="article-shell">
      <div class="article-topline">
        <a class="article-back" href="../../ai-tools-monitor.html">AI Tools Monitor</a>
        <p class="eyebrow">Platform News</p>
      </div>
      <h1 class="article-title">Claude Platform: Managed Agentsとant CLIのパブリックベータ公開</h1>
      <p class="article-dek">自律型エージェントをサンドボックスで安全に実行するフルマネージド基盤と、API管理用CLIがリリースされました。</p>
      <div class="article-meta-grid">
        <div class="article-meta-item"><span class="meta-label">公開日</span><strong>2026-04-09</strong></div>
        <div class="article-meta-item"><span class="meta-label">ツール</span><strong>Claude</strong></div>
      </div>
      <div class="article-body">
        <h2>Managed Agents (Public Beta)</h2>
        <p>自律型エージェントを安全なサンドボックス環境で実行するためのフルマネージド・ハーネスがリリースされました。APIを通じてエージェントの作成、コンテナ設定、セッション実行が可能です。</p>
        <h2>ant CLI と Bedrock 強化</h2>
        <p>APIリソースのYAML管理やClaude Codeとのネイティブ統合をサポートする新しいコマンドラインクライアント「ant CLI」が公開。また、Amazon Bedrockでの Messages API エンドポイントも利用可能になりました。</p>
      </div>
    </article>
  </body>
</html>"""
    }
]

# 1. Write HTML files
for art in new_articles:
    file_path = os.path.join(base_dir, "articles", "tools", art["slug"] + ".html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(art.pop("html_content"))

# 2. Update articles.json
json_path = os.path.join(base_dir, "data", "articles.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Generate serial (find max serial + 1)
max_serial = max([a.get("serial", 0) for a in data.get("articles", [])])
for art in reversed(new_articles):
    max_serial += 1
    art["serial"] = max_serial
    data["articles"].insert(0, art)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 3. Update ai-tools-monitor.html
html_path = os.path.join(base_dir, "ai-tools-monitor.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Update blocks function
def update_tool_block(html, tool_id, new_date, new_title, new_url, new_tag, new_version):
    # Update latest date in details tag
    html = re.sub(
        rf'(<details id="{tool_id}"[^>]*data-latest=")[^"]+(")',
        rf'\g<1>{new_date}\g<2>', html
    )
    # Update summary title and date
    html = re.sub(
        rf'(<details id="{tool_id}"[\s\S]*?<span class="tool-summary-date">)[^<]+(</span>\s*<span class="tool-summary-title">)[^<]+(</span>)',
        rf'\g<1>{new_date}\g<2>{new_title}\g<3>', html
    )
    # Add new li to the top of changelog-list
    new_li = f'<li class="changelog-item"><span class="changelog-date">{new_date}</span><a href="{new_url}">{new_title}</a></li>'
    html = re.sub(
        rf'(<ul class="changelog-list"(?: id="[^"]+")?>)',
        rf'\1\n                {new_li}', html, count=1 # Only first match for each tool? need to target specific tool block
    )
    
    # Target specific list
    # Split by tool_id and replace in the first part after it
    parts = html.split(f'id="{tool_id}"')
    if len(parts) > 1:
        ul_split = parts[1].split('<ul class="changelog-list"', 1)
        if len(ul_split) > 1:
            inner_split = ul_split[1].split('>', 1)
            parts[1] = ul_split[0] + '<ul class="changelog-list"' + inner_split[0] + '>\n                ' + new_li + inner_split[1]
        html = f'id="{tool_id}"'.join(parts)
        
    # Update latest tag inside tool-meta
    parts = html.split(f'id="{tool_id}"')
    if len(parts) > 1:
        meta_split = parts[1].split('<span class="latest-tag">Latest: ', 1)
        if len(meta_split) > 1:
            inner_split = meta_split[1].split('</span>', 1)
            new_inner = re.sub(r'<strong>.*?</strong>|<strong id="[^"]+">.*?</strong>', f'<strong>{new_tag}</strong>', inner_split[0])
            parts[1] = meta_split[0] + '<span class="latest-tag">Latest: ' + new_inner + '</span>' + inner_split[1]
        html = f'id="{tool_id}"'.join(parts)
        
    return html

# Apply updates for the 3 tools
html_content = update_tool_block(
    html_content, "tool-openclaw", "2026-04-09", 
    "v2026.4.8: メディア生成機能の拡充とDreaming機能の進化", 
    "./articles/tools/2026-04-09-openclaw-v2026-4-8.html", 
    "v2026.4.8", "v2026.4.8"
)

html_content = update_tool_block(
    html_content, "tool-chatgpt", "2026-04-09", 
    "Windowsサンドボックスのセキュリティ強化とCodex CLI改善", 
    "./articles/tools/2026-04-09-chatgpt-security-codex.html", 
    "Security & CLI", "Security & CLI"
)

html_content = update_tool_block(
    html_content, "tool-claude", "2026-04-09", 
    "Managed Agentsとant CLIのパブリックベータ公開", 
    "./articles/tools/2026-04-09-claude-managed-agents.html", 
    "Managed Agents", "Managed Agents"
)

# Update Verification Report for Others
current_time = datetime.now().strftime("%Y-%m-%d %H:%M JST")
html_content = re.sub(
    r'(<span id="report-others-date">)[^<]+(</span>)',
    rf'\g<1>{current_time}\g<2>', html_content
)
html_content = re.sub(
    r'(<li id="report-others-updates"><strong>)[^<]+(</strong>)[^<]+(</li>)',
    rf'\g<1>Updates Found (3):\g<2> OpenClaw (v2026.4.8), ChatGPT (Security & CLI), Claude (Managed Agents)\g<3>', html_content
)
html_content = re.sub(
    r'(<li id="report-others-no-updates"><strong>)[^<]+(</strong>)[^<]+(</li>)',
    rf'\g<1>No New Updates (5):\g<2> Gemini, Grok, NotebookLM, Obsidian, Perplexity\g<3>', html_content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Update completed successfully.")
