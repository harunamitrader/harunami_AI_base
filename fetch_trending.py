import urllib.request, re, json

req = urllib.request.Request('https://github.com/trending', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    repos = []
    pattern = re.compile(r'<h2 class="h3 lh-condensed">\s*<a href="/([^"]+)"', re.DOTALL)
    for match in pattern.finditer(html):
        repo = match.group(1).strip()
        if not repo.startswith('trending/') and '/' in repo:
            repos.append(repo)

    print('Found repos:')
    for i, r in enumerate(repos):
        print(f'{i+1}. {r}')
        
    with open('trending_temp.json', 'w') as f:
        json.dump(repos, f)
except Exception as e:
    print('Failed:', e)
