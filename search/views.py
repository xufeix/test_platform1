from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.

'''
django框架中的核心文件，控制输出的内容以及处理用户的交互逻辑
    登录账号  支付
'''


# 视图函数
def indext(request):
    return HttpResponse('恭喜小飞飞，啦啦啦啦啦啦')


def login(request):
    return render(request, 'login.html')


def login_submit(request):
    return HttpResponse('恭喜小飞飞，啦啦啦啦啦啦')


def index(request):
    return render(request, 'creat_data.html')


def index_html(request):
    return render(request, 'creat_data.html')


def add_case(request):
    return render(request, 'addcase.html')


def maga_login(phone):
    headers = {
        'Accept-Language': 'zh-CN',
        'ZYP': 'mid=33816367',
        'debug': '1',
        'X-Xc-Agent': 'av=1.43.0.414,dt=0',
        'User-Agent': 'okhttp/3.12.2 maga/1.43.0.414 (Android/29)',
        'Request-Type': 'text/json',
        'Host': 'magatest.icocofun.com',
    }
    json_data = {
        "region_code": "86",
        "phone": str(phone),
        "code": "8867",
        "login_type": 1,
        "from": "mypage",
        "cur_page": "login",
        "from_page": "myprofile",
        "h_av": "1.42.0.410",
        "h_dt": 0,
        "h_mf": "vivo",
        "h_ch": "google",
        "h_model": "vivo Xplay6",
        "h_nt": 1,
        "h_os": 25,
        "h_ts": 1653014944569,
        "h_app": "maga",
        "h_pkg": "us",
        "h_lang": "en",
        "h_tz": "Asia\/Shanghai",
        "gps_adid": "59a7af14-5382-4f75-88c6-c9e8bfca605f",
        "h_did": "610268b9430d427630d78e9e",
        "h_aid": "61ee6e50430d423c3383574a",
    }
    params = {
        'sign': '358012500b287fbef30afeeb3499a5ba',
    }

    data = json.dumps(json_data)
    # data = data.replace("\\\\","\\")
    # print(data)
    response = requests.post('http://magatest.icocofun.com/account/login_by_verify_code', params=params,
                             headers=headers, data=data)
    print(response.text)
    res = response.text
    print(type(response))
    # dic = ast.literal_eval(response)
    res = json.loads(res)
    # res = dic['data']['token']
    # aaa = res.json()
    # print(aaa)
    # res = json.dumps(response)
    print(res['data']['token'])
    return res['data']['token'], res['data']['user_info']['_id'], res['data']['aid']


def creat_data(request):
    body = request.body
    print(body)
    json_result = json.loads(body)
    # print(json_result["phone"])
    phone = json_result["phone"]
    print(phone)
    tid = json_result["tid"]
    time = json_result['time']
    print(time)
    # phone = request.POST.get("phone")
    # print(phone+"===================")
    token, h_m, h_aid = maga_login(phone)
    # tid = request.POST.get("tid")
    # print(tid)
    # print(type(tid))
    leixing = json_result['leixing']
    print(type(leixing))
    print(leixing)

    text = 'text'
    img = 'img'
    video = 'video'
    if leixing == text:
        for i in range(time):
            create_post(h_aid, h_m, token, tid, i)
    elif leixing == img:
        for i in range(time):
            create_post_img(h_aid, h_m, token, tid, i)
    elif leixing == video:
        for i in range(time):
            create_post_video(h_aid, h_m, token, tid, i)
    # return render(request, 'creat_data.html')
    return HttpResponse('创建成功')


# 发文本
def create_post(h_aid, h_m, token, tid, i):
    headers = gen_header(h_m)
    params = gen_params()
    json_data = gen_atom(h_aid, h_m, token, tid)
    json_data["content"] = "xxufei" + str(i)
    data = json.dumps(json_data)
    data = data.replace("\\\\", "\\")
    print(data)
    response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)
    # return HttpResponse('查询成功')
    print(response.text)


# 发图片
def create_post_img(h_aid, h_m, token, tid, i):
    headers = gen_header(h_m)
    params = gen_params()
    json_data = gen_atom(h_aid, h_m, token, tid)
    json_data["content"] = "maga" + str(i)
    json_data['imgs'] = [256075166]
    data = json.dumps(json_data)
    data = data.replace("\\\\", "\\")
    print(data)
    response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)
    # return HttpResponse('查询成功')
    print(response.text)


# 发视频
def create_post_video(h_aid, h_m, token, tid, i):
    headers = gen_header(h_m)
    params = gen_params()
    json_data = gen_atom(h_aid, h_m, token, tid)
    json_data["content"] = "xxufei" + str(i)
    json_data['imgs'] = [256075168]
    json_data['videos'] = [256075168]
    data = json.dumps(json_data)
    data = data.replace("\\\\", "\\")
    print(data)
    response = requests.post('http://magatest.icocofun.com/post/create', params=params, headers=headers, data=data)
    # return HttpResponse('查询成功')
    print(response.text)


def gen_params():
    params = {
        'sign': '358012500b287fbef30afeeb3499a5ba',
    }
    return params


def gen_atom(h_aid, h_m, token, tid):
    json_data = {
        "localid": 1654411504514,
        "tid": tid,
        "c_type": 1,
        "topic_name": "Joker",
        "cur_page": "login",
        "from_page": "main",
        "h_av": "1.43.0.415",
        "h_dt": 0,
        "h_mf": "vivo",
        "h_ch": "google",
        "h_model": "vivo Xplay6",
        "h_nt": 1,
        "h_os": 25,
        "h_ts": 1654411504519,
        "h_app": "maga",
        "h_pkg": "us",
        "h_lang": "en",
        "h_tz": "Asia\/Shanghai",
        "gps_adid": "59a7af14-5382-4f75-88c6-c9e8bfca605f",
        "h_did": "610268b9430d427630d78e9e",
        "h_aid": h_aid,
        "token": token,
        "h_m": h_m
    }
    # print('-----'+tid)
    return json_data


def gen_header(h_m):
    headers = {
        'Accept-Language': 'zh-CN',
        'ZYP': 'mid=' + str(h_m),
        'debug': '1',
        'X-Xc-Agent': 'av=1.43.0.414,dt=0',
        'User-Agent': 'okhttp/3.12.2 maga/1.43.0.414 (Android/29)',
        'Request-Type': 'text/json',
        'Host': 'magatest.icocofun.com',
    }
    return headers

# creat_data()
