from proxyUtil import *

def checkURL(url):
    try:
        r = requests.head(url, timeout=3)
    except:
        return False
    return r.status_code//100 == 2

output = []
with open("README.md") as file:
    cnt = 0
    while line := file.readline():
        line = line.rstrip()
        if line.startswith("|"):
            if cnt>1 :
                url = line.split('|')[-2]
                for _ in range(3):
                    if status := checkURL(url):
                        break
                if status :
                    count = len(ScrapURL(url))
                    line = re.sub(r'^\|+?(.*?)\|+?(.*?)\|+?', f'| ✅ | {count} |', line, count=1)
                else:
                    line = re.sub(r'^\|+?(.*?)\|+?(.*?)\|+?', f'| ❌ | - |', line, count=1)
            cnt+=1
        output.append(line)

with open("README.md", "w") as f:
    f.write('\n'.join(output))
