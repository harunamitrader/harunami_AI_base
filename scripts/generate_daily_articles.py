import json
import os
import re
from datetime import datetime

base_dir = r'C:\Users\sgmxk\Desktop\AI\repos\github\harunamitrader\harunami_AI_base'
articles_json_path = os.path.join(base_dir, 'data', 'articles.json')

with open(articles_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define new posts
new_posts = [
    {
        'rank': 8,
        'repoName': 'topoteretes/cognee',
        'repoUrl': 'https://github.com/topoteretes/cognee',
        'starCount': 15749,
        'title': 'cognee',
        'slug': '2026-04-17-topoteretes-cognee',
        'dek': 'わずか6行のコードでAIエージェントに自律的な「長期記憶（グラフ構造）」を組み込めるオープンソースのナレッジエンジン。',
        'summary': 'cogneeは、LLMアプリやAIエージェント向けのオープンソース・ナレッジエンジンです。グラフデータベースによる構造化記憶を用いることでハルシネーションを抑え、エージェントが過去の対話やインプットから自己学習して知識を整理・永続化する「記憶基盤」をわずか6行で提供します。',
        'genre': 'ナレッジ管理・RAG解析',
        'features': ['グラフとベクトルを組み合わせたハイブリッドな記憶構造', '数行で導入可能なシンプルなAPI', 'ローカルLLMを含む多様なモデルとの統合', 'エージェントの自律学習と知識更新'],
        'time': '2026-04-17T06:10:00+09:00',
        'serial': 241
    },
    {
        'rank': 7,
        'repoName': 'steipete/wacli',
        'repoUrl': 'https://github.com/steipete/wacli',
        'starCount': 1641,
        'title': 'wacli',
        'slug': '2026-04-17-steipete-wacli',
        'dek': 'WhatsApp をターミナルから完全にコントロール。メッセージの送受信やメディア操作が可能な軽量CLIクライアント。',
        'summary': 'wacli は、WhatsApp をコマンドラインから操作するための非公式CLIクライアントです。QRコード認証によりデバイスと連携し、プレーンテキストから画像・動画までターミナル内で送受信可能。自動化スクリプトやAIエージェントの通知基盤としても応用が利くツールです。',
        'genre': 'AI基盤・データ基盤・業務アプリ',
        'features': ['ターミナルからのWhatsAppメッセージ送受信', 'QRコードでの安全かつ手軽なログイン', '自動化や通知ツールとしての活用が容易', 'メディア（画像、動画など）の転送対応'],
        'time': '2026-04-17T06:15:00+09:00',
        'serial': 242
    },
    {
        'rank': 6,
        'repoName': 'google/magika',
        'repoUrl': 'https://github.com/google/magika',
        'starCount': 14645,
        'title': 'magika',
        'slug': '2026-04-17-google-magika',
        'dek': 'Googleが開発した、ディープラーニング駆動による超高速・高精度なファイルタイプ（MIME）判定ツール。',
        'summary': 'magikaは、Googleが社内プロジェクトとして開発しオープンソース化したAIベースのファイル判定ツールです。従来のシグネチャベースよりも高速かつ精緻にファイルのコンテンツタイプを識別し、セキュリティ製品のマルウェア解析や、大規模データレイクでの前処理を劇的に加速させます。',
        'genre': 'AI基盤・データ基盤・業務アプリ',
        'features': ['ディープラーニングを用いた高精度なファイル種別推論', 'ミリ秒クラスの超高速判定', 'シグネチャマッチでは見抜けないヘッダ偽装も検知', 'Python/JSおよびCLIツールとしての提供'],
        'time': '2026-04-17T06:20:00+09:00',
        'serial': 243
    },
    {
        'rank': 5,
        'repoName': 'vercel-labs/open-agents',
        'repoUrl': 'https://github.com/vercel-labs/open-agents',
        'starCount': 3133,
        'title': 'open-agents',
        'slug': '2026-04-17-vercel-labs-open-agents',
        'dek': 'Vercel社が提供する、クラウド環境でスケーラブルなAIエージェントを構築するためのオープンソーステンプレート。',
        'summary': 'open-agents は、Vercel Labs が公開したクラウドネイティブな AI エージェントの基礎テンプレートです。Next.js や Vercel AI SDK の知見を活かし、状態管理や並行処理、ストリーミングレスポンスを初めから備えた実践的なマルチエージェント基盤を迅速にスケールさせることができます。',
        'genre': 'AIエージェント (自律基盤・特化アプリ)',
        'features': ['最新の Web アーキテクチャに最適化されたエージェント設計', 'Vercel 環境へのゼロコンフィギュレーション・デプロイ', '状態管理とストリーミングによるシームレスな対話 UX', '開発者が拡張しやすいモジュール構造'],
        'time': '2026-04-17T06:25:00+09:00',
        'serial': 244
    },
    {
        'rank': 3,
        'repoName': 'lsdefine/GenericAgent',
        'repoUrl': 'https://github.com/lsdefine/GenericAgent',
        'starCount': 2690,
        'title': 'GenericAgent',
        'slug': '2026-04-17-lsdefine-genericagent',
        'dek': '3.3K行の「種」から自らのスキルツリーを成長させ、トークン消費を1/6に抑えつつOSを完全支配する自己進化エージェント。',
        'summary': 'GenericAgent は、実行時の経験から新たな関数（スキル）を自動生成して自らを拡張し続けるAIエージェントです。初期状態の小さなコードベースからタスクごとに最適なツール群を学習・保持することで、プロンプトに頼らずとも高度なシステム操作を最小のトークンコストで達成します。',
        'genre': 'AIエージェント (自律基盤・特化アプリ)',
        'features': ['経験からスキルセットを動的に成長させる自己進化機構', '他モデル比較で6倍のトークン効率', 'システム操作や複数タスクをまたぐナレッジの蓄積', '小規模なコアコード（3.3K行）による高い保守性'],
        'time': '2026-04-17T06:30:00+09:00',
        'serial': 245
    }
]

html_template = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | harunami AI base</title>
  <meta name="description" content="{dek}">
  <link rel="stylesheet" href="../../../css/index.css">
  <link rel="stylesheet" href="../../../css/article.css">
</head>
<body class="article-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="../../../index.html" class="site-title">harunami AI base</a>
    </div>
  </header>

  <main class="main-content">
    <article class="article-container">
      <div class="article-header">
        <span class="eyebrow">GitHub Watcher</span>
        <h1 class="article-title">{title}</h1>
        <p class="article-dek">{dek}</p>
        
        <div class="article-meta-grid">
          <div class="meta-item">
            <span class="meta-label">分析日</span>
            <span class="meta-value">2026-04-17</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Trending順位</span>
            <span class="meta-value">#{rank}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">対象リポジトリ</span>
            <span class="meta-value"><a href="{repoUrl}" target="_blank" rel="noopener noreferrer">{repoName}</a></span>
          </div>
          <div class="meta-item">
            <span class="meta-label">GitHub Stars</span>
            <span class="meta-value">{starCount:,}</span>
          </div>
        </div>
      </div>

      <div class="article-body">
        <h2>概要</h2>
        <p>{summary}</p>

        <h2>主な機能</h2>
        <ul>
          <li><strong>{f1}</strong></li>
          <li><strong>{f2}</strong></li>
          <li><strong>{f3}</strong></li>
          <li><strong>{f4}</strong></li>
        </ul>

        <h2>ターゲット層</h2>
        <p>AIシステムの運用者、データアナリスト、OSS開発者、自動化による業務改善を目指すエンジニア全般。</p>

        <h2>リスクと注意点</h2>
        <p>オープンソースの特性上、プロダクション環境への導入前には十分なセキュリティ検証と依存関係の確認が必要です。</p>

        <h2>今後の影響</h2>
        <p>このツールや基盤が普及することで、より高度な自動化とエージェント技術の民主化が加速するでしょう。</p>

        <div class="source-links">
          <h3>参考リンク</h3>
          <ul>
            <li><a href="{repoUrl}" target="_blank" rel="noopener noreferrer">GitHub - {repoName}</a></li>
          </ul>
        </div>
      </div>
    </article>
  </main>
</body>
</html>'''

for p in new_posts:
    html_content = html_template.format(
        title=p['title'],
        dek=p['dek'],
        rank=p['rank'],
        repoUrl=p['repoUrl'],
        repoName=p['repoName'],
        starCount=p['starCount'],
        summary=p['summary'],
        f1=p['features'][0],
        f2=p['features'][1],
        f3=p['features'][2],
        f4=p['features'][3]
    )
    html_path = os.path.join(base_dir, 'articles', 'github', 'daily', p['slug'] + '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # insert into data
    entry = {
        'category': 'github-trending',
        'slug': p['slug'],
        'title': p['title'],
        'dek': p['dek'],
        'publishedAt': '2026-04-17',
        'createdAt': p['time'],
        'repoName': p['repoName'],
        'repoUrl': p['repoUrl'],
        'starCount': p['starCount'],
        'articleUrl': f'./articles/github/daily/{p["slug"]}.html',
        'rank': p['rank'],
        'serial': p['serial'],
        'originType': 'trending',
        'genre': p['genre']
    }
    data['articles'].insert(0, entry)

# Generate Update Report
report_time = '2026-04-17T06:35:00+09:00'
report_serial = 19
report_slug = '2026-04-17-update-report'
report_title = '2026-04-17 アップデートレポート'
report_dek = '本日調査したGitHubトレンドの全順位と、新規作成された記事のまとめ'

report_html_template = '''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | harunami AI base</title>
  <meta name="description" content="{dek}">
  <link rel="stylesheet" href="../../../css/index.css">
  <link rel="stylesheet" href="../../../css/article.css">
</head>
<body class="article-page">
  <header class="site-header">
    <div class="header-inner">
      <a href="../../../index.html" class="site-title">harunami AI base</a>
    </div>
  </header>

  <main class="main-content">
    <article class="article-container">
      <div class="article-header">
        <span class="eyebrow">Update Report</span>
        <h1 class="article-title">{title}</h1>
        <p class="article-dek">{dek}</p>
      </div>

      <div class="article-body">
        <h2>本日の調査ランキング（全件）</h2>
        <ol>
          <li>✅ 記事作成済み: <a href="../daily/2026-04-16-forrestchang-andrej-karpathy-skills.html">forrestchang/andrej-karpathy-skills</a></li>
          <li>✅ 記事作成済み: <a href="../daily/2026-04-15-claude-mem.html">thedotmack/claude-mem</a></li>
          <li>✨ 新規追加: <a href="../daily/2026-04-17-lsdefine-genericagent.html">lsdefine/GenericAgent</a></li>
          <li>✅ 記事作成済み: <a href="../daily/2026-04-14-jamiepine-voicebox.html">jamiepine/voicebox</a></li>
          <li>✨ 新規追加: <a href="../daily/2026-04-17-vercel-labs-open-agents.html">vercel-labs/open-agents</a></li>
          <li>✨ 新規追加: <a href="../daily/2026-04-17-google-magika.html">google/magika</a></li>
          <li>✨ 新規追加: <a href="../daily/2026-04-17-steipete-wacli.html">steipete/wacli</a></li>
          <li>✨ 新規追加: <a href="../daily/2026-04-17-topoteretes-cognee.html">topoteretes/cognee</a></li>
          <li>未作成 (z-lab/dflash)</li>
          <li>✅ 記事作成済み: <a href="../daily/2026-04-16-lordog-dive-into-llms.html">Lordog/dive-into-llms</a></li>
          <li>未作成 (openai/openai-agents-python)</li>
          <li>未作成 (EvoMap/evolver)</li>
          <li>✅ 記事作成済み: <a href="../daily/2026-04-16-simoneavogadro-android-reverse-engineering-skill.html">SimoneAvogadro/android-reverse-engineering-skill</a></li>
          <li>未作成 (BasedHardware/omi)</li>
        </ol>

        <h2>今後の展望</h2>
        <p>本日はAIエージェントの基本インフラや運用・記憶機能のOSSを中心に記事を追加しました。特にナレッジ管理とフルオートメーションに興味を持つ開発者におすすめの実装が揃っています。</p>
      </div>
    </article>
  </main>
</body>
</html>'''

report_html_content = report_html_template.format(
    title=report_title,
    dek=report_dek
)

report_path = os.path.join(base_dir, 'articles', 'github', 'reports', f'{report_slug}.html')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_html_content)

report_entry = {
    'category': 'github-update-report',
    'slug': report_slug,
    'title': report_title,
    'dek': report_dek,
    'summary': 'GitHub Trending の全順位を確認し、cognee, wacli, magika, open-agents, GenericAgent の5件を新規に記事化。',
    'publishedAt': '2026-04-17',
    'createdAt': report_time,
    'articleUrl': f'./articles/github/reports/{report_slug}.html',
    'serial': report_serial
}

# Add report at the top of the dataset properly sorted or just insert
data['articles'].insert(0, report_entry)

# sorting function just to make sure createdAt is strictly descending
def get_dt(x):
    if 'createdAt' in x: return datetime.fromisoformat(x['createdAt'])
    else: return datetime.fromisoformat(x['publishedAt'] + 'T00:00:00+09:00')

data['articles'].sort(key=get_dt, reverse=True)

with open(articles_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
