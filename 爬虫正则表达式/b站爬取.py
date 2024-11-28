import requests
import re
import json
import pprint
from bs4 import BeautifulSoup
url='https://www.bilibili.com/video/BV1sj421S7w3/'

# print(ans1.text)
headers={
}
# print(headers)
res=requests.get(url=url,headers=headers)
print(res.status_code)
get_text=res.text
# print(get_text)
res_title=re.findall('<title data-vue-meta="true">(.*?)</title>',get_text)
# print(get_text)
for i in res_title:
    print(i)
video_info=re.findall('<script>window.__playinfo__=(.*?)</script>', get_text)[0]
print(video_info)
video_info_process=json.loads(video_info)
print(video_info_process)
pprint.pprint(video_info_process)
audio_url=video_info_process['data']['dash']['audio'][0]['base_url']
video_url=video_info_process['data']['dash']['video'][0]['base_url']
audio_info=requests.get(url=audio_url,headers=headers).content
video_info=requests.get(url=video_url,headers=headers).content
with open('video\\'+res_title[0]+'.mp3',mode='wb') as f1:
    f1.write(audio_info)
with open('video\\' + res_title[0] + '.mp4', mode='wb') as f2:
    f2.write(video_info)
