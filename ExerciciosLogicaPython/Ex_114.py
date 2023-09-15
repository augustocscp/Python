import urllib.request

try:
    url = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('Site indisponivel')
else:
    print('Site operacional')
