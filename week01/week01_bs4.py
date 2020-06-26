import requests
from bs4 import BeautifulSoup 
import pandas as pd

url ='https://maoyan.com/films?showType=3'
header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
'host':'maoyan.com',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'uuid_n_v=v1; uuid=E9BA41F0B45111EAACB6BBD781D89938DF0B59FCC2E048AAA8CF7B842C9288D9; mojo-uuid=2732764aa91bb3b1219b9cf973f2924f; _lxsdk_cuid=172dab90d42c8-063f78b6e46902-31607402-1ea000-172dab90d42c8; _lxsdk=E9BA41F0B45111EAACB6BBD781D89938DF0B59FCC2E048AAA8CF7B842C9288D9; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=64706eaff01f10d32e7120aad0d6c73a54d8c0ed06bbc1a24b0f467610336b8c; mojo-session-id={"id":"22198546e2722589b02de9ad0c2c2cf4","time":1592835639039}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592809900,1592809935,1592810323,1592835639; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592835639; __mta=217993513.1592807462213.1592812014078.1592835639266.12; _lxsdk_s=172dc670713-90c-8f9-313%7C%7C3'}
rep =requests.get(url=url,headers=header)
soup = BeautifulSoup(rep.text,'html.parser')
# print(soup)
movie_list = []
for ttags in soup.find_all('div',attrs={'class':'movie-item-hover'})[:10]:

    dic = {}                
    dic['name'] = ttags.text.split()[0]

    if ttags.text.split()[1] == '类型:':
        dic['score'] ="0"
    else:
        dic['score'] = ttags.text.split()[1] 

    if ttags.text.split()[5] == '上映时间:':
        dic['actor'] = ttags.text.split()[4]
    else:
        dic['actor'] = ttags.text.split()[5]

    if len(ttags.text.split()) == 8:
        dic['time'] = ttags.text.split()[7]
    elif len(ttags.text.split()) == 7:
        dic['time'] = ttags.text.split()[6]
    else:
        dic['time'] = ttags.text.split()[5]

    if ttags.text.split()[3] == '主演:':
        dic['type'] = ttags.text.split()[2]
    else:
        dic['type'] = ttags.text.split()[3]
    
    movie_list.append(dic)
    
# print('movie_list：\n',movie_list)

df = pd.DataFrame(movie_list)
# for item in movie_list:
#     print(item)

df.to_csv('/Users/renpenghui/Python001-class01/week01/homework01.csv',encoding='utf_8_sig',index=False)
print('完成')

