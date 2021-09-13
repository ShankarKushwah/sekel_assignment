import json
from collections import OrderedDict
from itertools import islice

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_text():
    url = 'http://www.mocky.io/v2/5cdd110c3000007825e23470'
    resp = requests.get(url)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        return soup.text

def index(request):
    text = json.loads(get_text())
    d = {}
    for i in text:
        if i.split(":")[0] in d:
            d[i.split(":")[0]] += 1
        else:
            d[i.split(":")[0]] = 1
    data = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    res = OrderedDict(reversed(list(data.items())))
    top_5 = dict(islice(res.items(), 5))
    print(top_5)
    return render(request, 'index.html', {"data": top_5})