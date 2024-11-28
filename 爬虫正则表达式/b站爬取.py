import requests
import re
import json
import pprint
from bs4 import BeautifulSoup
url='https://www.bilibili.com/video/BV1sj421S7w3/'

# print(ans1.text)
headers={
'Referer':'https://www.bilibili.com/video/BV1vm4y1L7id/?spm_id_from=autoNext&vd_source=7b87ad42b1bb8f7ebd714ba85a8f4bd9',
'Cookie':'buvid3=15DC27FC-CE65-3362-93E6-B5FA440C936811200infoc; b_nut=1693323811; i-wanna-go-back=-1; b_ut=7; _uuid=CBE58F8B-D8AD-7818-2C8F-9CDFDCB10B6E396594infoc; buvid4=A7EDE336-6FEB-A452-9747-D7DA6F42A75212447-023082923-Mk4wjKcJQ44RQmCoHoa%2FsJL15r6ofXJQBmpW3AHmbuGn12jWUjZgyg%3D%3D; header_theme_version=CLOSE; rpdid=0zbfAHNTGy|RaRWTBja|275|3w1QB0SQ; DedeUserID=1697874662; DedeUserID__ckMd5=86494cf60154e172; buvid_fp_plain=undefined; hit-new-style-dyn=1; hit-dyn-v2=1; enable_web_push=DISABLE; LIVE_BUVID=AUTO4717086959789788; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; PVID=2; fingerprint=b9b90a94d0159846f3095b9fc7bda4e0; buvid_fp=b9b90a94d0159846f3095b9fc7bda4e0; home_feed_column=4; is-2022-channel=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc2NTY0MzQsImlhdCI6MTcxNzM5NzE3NCwicGx0IjotMX0.f8lCwdngUNiIztxI0JV6m3mHEAJjeQQYJurYwnPnASQ; bili_ticket_expires=1717656374; SESSDATA=e6eda821%2C1732949235%2Cf1c28%2A62CjA95d_6Hg1zqpNc6RpmeXsmporpXIHlK-zWNME_SebhzaabLIhpHsai1Wl6V-RQ5UwSVm9wQW5sUXkyMlkzNERKRlRkQTNxMWE4aDlmUExjbV8tVlRfVi1ST3JWWEFabHlCM215RUtTd0t4c1RwYkZEeEFKMURncjZIdmI3WUZvY0hRbGdMWnJRIIEC; bili_jct=d23a34eef46ae5fe0c0224e96b714e30; bp_t_offset_1697874662=938742613832368185; b_lsid=C86353FF_18FDE842DE9; bsource=search_bing; browser_resolution=713-616; sid=5rd7sgpl',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
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
