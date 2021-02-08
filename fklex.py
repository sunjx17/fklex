import requests
import time
import random

def get_fans_0(headers):
    try:
        url='http://api.bilibili.com/x/web-interface/card'
        param={"mid":777536}
        P_get=requests.get(url,params=param,headers=headers,timeout=10).json()
        return P_get["data"]["follower"]
    except:
        return 0
    
def get_fans_1(headers):
    try:
        url='https://api.bilibili.com/x/relation/stat'
        param={"vmid":777536,"jsonp":"jsonp"}
        P_get=requests.get(url,params=param,headers=headers,timeout=10).json()
        return P_get["data"]["follower"]
    except:
        return 0
get_fans=[get_fans_1,get_fans_0]
headers=[
{
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "api.bilibili.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
},
{
    "Accept": "text/html,application/xhtml+xml,application/xml;",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "api.bilibili.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
},
{
    "Accept": "text/html,application/xhtml+xml,application/xml;",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "CURRENT_FNVAL=16; _uuid=D94A75D3-82B5-F357-8A23-16B617812E7D41930infoc; buvid3=BEEE2523-3F3F-40C7-AD9C-9085CE94F70D40935infoc",
    "DNT": "1",
    "Host": "api.bilibili.com",
    "Upgrade-Insecure-Requests": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"
}
]
f=open('fans.csv','a')
lt=0
fans0=0
time0=0
while 1:
    try:
        rfun=get_fans[random.randint(0,1)]
        rua=headers[random.randint(0,2)]
        fans=rfun(rua)
        t0=time.time()
        t=str(int(t0))
        tu=time.asctime( time.localtime(t0))
        if fans>0:
            minus=0
            
            s0=t+','+tu+','+str(fans)
            f.write(s0+'\n')
            if lt>0:
                minus=(-lt+fans)
                print(s0+","+str(minus)+','+str(fans-fans0)+','+str((fans-fans0)/(t0-time0))+"/s")
            else:
                fans0=fans
                time0=t0
                print(s0)
            lt=fans
        time.sleep(5+random.randint(0,10))
    except:
        f.close()
        exit(0)
