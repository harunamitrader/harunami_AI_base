import urllib.request, re

req = urllib.request.Request('https://github.com/trending', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req) as response: html = response.read().decode('utf-8')

repos = []
blocks = html.split('<article class="Box-row">')[1:]
for block in blocks:
    match = re.search(r'<h2 class="h3 lh-condensed">\s*<a href="/([^/]+/[^/"]+)"', block)
    if match:
        repos.append(match.group(1).strip())
    else:
        # Fallback if class has changed
        match2 = re.search(r'<a[^>]*href="/([^/]+/[^/"]+)"[^>]*data-hydro-click[^>]*"click_target":"REPOSITORY"', block)
        if match2:
            repos.append(match2.group(1).strip())

if not repos:
    # Just grab any first href="/a/b" in an h2
    for block in blocks:
        match3 = re.search(r'<h2[^>]*>.*?<a[^>]*href="/([^/]+/[^/"]+)"', block, flags=re.DOTALL)
        if match3:
            repos.append(match3.group(1).strip())

print("Found Repos:")
for i, r in enumerate(repos):
    print(f"{i+1}. {r}")
