import json
import time
import requests

headers = {
    'Accept-Language': 'zh-CN',
    'ZYP': 'mid=33816416',
    'debug': '1',
    'X-Xc-Agent': 'av=1.43.0.415,dt=0',
    'User-Agent': 'okhttp/3.12.2 maga/1.43.0.415 (Android/25)',
    'Request-Type': 'text/json',
    'Content-Type': 'application/json; charset=utf-8',
    'Host': 'magatest.icocofun.com',
}

params = {
    'sign': '358012500b287fbef30afeeb3499a5ba',
}

json_data = {
    'localid': 1654411504514,
    'tid': 3,
    'content': 'hhhh',
    'c_type': 1,
    'topic_name': 'Joker',
    'cur_page': 'login',
    'from_page': 'main',
    'h_av': '1.43.0.415',
    'h_dt': 0,
    'h_mf': 'vivo',
    'h_ch': 'google',
    'h_model': 'vivo Xplay6',
    'h_nt': 1,
    'h_os': 25,
    'h_ts': 1654411504519,
    'h_app': 'maga',
    'h_pkg': 'us',
    'h_lang': 'en',
    'h_tz': 'Asia/Shanghai',
    'gps_adid': '59a7af14-5382-4f75-88c6-c9e8bfca605f',
    'h_did': '610268b9430d427630d78e9e',
    'h_aid': '61028f8c430d427630d791a5',
    'token': 'TeKaNYqvKud3JUE5Hu3yoUJJax4GecM3HOzjNmdHEvZnbH6nnDif6cuBvKB1fi5wGQa_TUPD2MUI8VHttoKcJqDkyvXEaSERljEj3zWPGH2d3tV9Bx1TaV8v30wM-AUS1MNLr',
    'h_m': 33816416,
}
data = json.dumps(json_data)
data = data.replace("\\\\", "\\")

response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"localid":1654411504514,"tid":3,"content":"hhhh","c_type":1,"topic_name":"Joker","cur_page":"login","from_page":"main","h_av":"1.43.0.415","h_dt":0,"h_mf":"vivo","h_ch":"google","h_model":"vivo Xplay6","h_nt":1,"h_os":25,"h_ts":1654411504519,"h_app":"maga","h_pkg":"us","h_lang":"en","h_tz":"Asia\\/Shanghai","gps_adid":"59a7af14-5382-4f75-88c6-c9e8bfca605f","h_did":"610268b9430d427630d78e9e","h_aid":"61028f8c430d427630d791a5","token":"TeKaNYqvKud3JUE5Hu3yoUJJax4GecM3HOzjNmdHEvZnbH6nnDif6cuBvKB1fi5wGQa_TUPD2MUI8VHttoKcJqDkyvXEaSERljEj3zWPGH2d3tV9Bx1TaV8v30wM-AUS1MNLr","h_m":33816416}'
#response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)

# for i in range(3):
#     response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)
#     time.sleep(1)
#     i += 1
#     print(response.text)
