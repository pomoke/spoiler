import requests
import random
import time
#from fake_useragent import UserAgent
#import ua_list

#proxy={'http':'socks5://127.0.0.1:9150','https':'socks5://127.0.0.1:9150'}
proxy={};
#target=({'url':'http://www.gfsteamtv.top/2017.php',
#    'post':[{'name':'u','type':'qq'},{'name':'p','type':'pass'}],
#    'ref':'http://gfsteamtv.top/'},
#	{'url':'http://www.gfdali.top/dnf.php',
#    'post':[{'name':'u','type':'qq'},{'name':'p','type':'pass'}],
#    'ref':'http://gfdali.top/'},
#    {'url':'http://kghfgdrgd.gq/mail1.php?user=hjg77987',
#    'post':[{'name':'u','type':'qq'},{'name':'p','type':'pass'}],
#    'ref':'http://kghfgdrgd.gq/you/20/index.php?user=hjg77987&ta=888652_hao&=uw579G7974FHd5H7t76542fe'},
#    )
target=({'url':'https://www.huanbeiloan.com/hbzc/a11/455?channel=bst09',
    'post':[{'name':'mobile','type':'mobile'},],
    'ref':'https://www.huanbeiloan.com/hbzc/a11/455?channel=bst09'},
    )
ua=('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/61.1 Safari/534.36',
        'Mozilla/5.0 (X11; Linux ppc64le; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 8.0;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQBrowser/20 Safari/533.23',)

def gen(param):
    out={}
    for p in param:
        if p['type']=='qq':
            out[p['name']]=str(random.randint(15000000,3000000000))
        elif p['type']=='pass':
            out[p['name']]=random.choice(pwddict).join(random.choice('abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for _ in range(random.randint(1,3)))
        elif p['type']=='email':
            out[p['name']]=random.choice(pwddict)+'@'+random.choice(['qq.com','163.com','outlook.com','126.com','vip.126.net','me.com','icloud.com'])
        elif p['type']=='mobile':
            #out[p['name']]=random.choice(['138','139','151','159','171','172','173'])+str(random.randint(10000000,99999999))
            out[p['name']]="13800000000"
        else :
            out[p['name']]=''.join(random.choice('abcdefghijklmnopqrstuvwxyz01234567890') for _ in range(random.randint(6,10)))
        print(p['type']+': '+out[p['name']])
    return out

print('Hello! C-c to break.')
print('Reading Dictionary...')

pwddict=[]
with open('dict.txt','r') as fd:
    for line in fd.readlines():
        pwddict.append(line.strip())
print('Done.')
#ua=UserAgent();
response=requests.get("http://ipv4.myip.dk/api/Info/IPv4Address",proxies=proxy)
print("IP: "+response.content.decode())

#Main loop
while True:
    for t in target:
        #info generator
        info=gen(t['post'])
        header={'User-Agent':random.choice(ua)}
        print('Requesting '+t['url']+' with '+header['User-Agent'])
        response=requests.post(t['url'],data=info,allow_redirects=False,timeout=None,headers=header,proxies=proxy)
        ts=random.randint(15,150)
        print("Content: "+response.content.decode())
        print('Got '+str(response.status_code)+'. Sleep for '+str(ts)+'s'+'\a')
        #print(response.content)
        time.sleep(ts)
