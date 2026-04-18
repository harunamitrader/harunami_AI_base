import urllib.request, json
repos = ['EvoMap/evolver', 'BasedHardware/omi', 'Donchitos/Claude-Code-Game-Studios', 'lukilabs/craft-agents-oss', 'Tracer-Cloud/opensre']

for r in repos:
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{r}', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode())
            print(f"Repo: {r} | Stars: {data.get('stargazers_count')} | Desc: {data.get('description')}")
    except Exception as e:
        print(f'Error fetching {r}: {e}')
