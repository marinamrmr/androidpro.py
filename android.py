import requests
from bs4 import BeautifulSoup

url = "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&filters%5Bcity%5D%5B0%5D=Alexandria&q=android%20developer"
page = requests.get(url)
bs = BeautifulSoup(page.content, "html.parser")

jtitle = []
cname = []
jtype = []

contains = bs.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
job_title = bs.find_all("h2", {"class": "css-m604qf"})
comp_name = bs.find_all("a", {"class": "css-17s97q8"})
job_type = bs.find_all("span", {"class": "css-1ve4b75 eoyjyou0"})

for j in range(len(job_title)):
    jtitle.append(job_title[j].text)
for c in range(len(comp_name)):
    cname.append(comp_name[c].text)
for t in range(len(job_type)):
    jtype.append(job_type[t].text)

for i in range(len(jtitle)):
    print(jtitle[i] + cname[i] + jtype[i])