from flask import Flask, jsonify,request
import time
import json
import requests


app = Flask(__name__)

# 全局配置变量
proxyusernm = "jinyuegg"        # 代理帐号
proxypasswd = "qwe@123456.COM"        # 代理密码
ip_url = "http://jinyuegg.user.xiecaiyun.com/api/proxies?action=getText&key=NP239018F9&count=1&word=&rand=false&norepeat=false&detail=false&ltime=&idshow=false"
webkey = "spidertools.cn"
token2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1bmFtZSI6ImFpMTAyNGJpdCIsInBlcm1pc3Npb25zIjpbInNlbXJ1c2guZ3VydSIsInNpbWlsYXJ3ZWIiLCJ1c2VyIl0sImlhdCI6MTc0MjE0NjQ3NCwiZXhwIjoxNzQyNDA1Njc0fQ.ImFjzELH-mH_CLcodjcjTSk4HXrQ2jngnziJRXbvfCaJljidCFO4jbUkVMgAKfD7KhXvdgWMHi_w0SEEj5hqO1ssa5tr20KzgeJ04QYGaUA031Hegug85UVVHF7ll_q-BOLnlyzzEX4cK-i3l9eJrlvZpjik1DBDE1nU7M20rNH3u1oCq0ZmOq4xUH6I-NEdtBz9L4O8x3yNL_jx2QETT_5j41eJwOf-tiu_dUBUEyxAglM81UmFh7PjoCnc3PQ5dWeDZrpP8g-csHat5F17OoLPURcLz86gDBJpdeVv-J1LAQczMJ_qZcDMitadMvOpZ1zbIoN5xWEKY_7j0TZosQ"

# 创建会话对象
session = requests.Session()

# 设置请求头
headers = {
    "sec-ch-ua-platform": "Windows",
    "Referer": "https://sim.3ue.com/",
    "sec-ch-ua": "Not(A:Brand;v=99, Microsoft",
    "x-sw-page": f"https://pro.similarweb.com/#/organicsearch/pageAnalysis/website-keyword-v2/*/999/1m?key={webkey}&pageFilter=%5B%7B%22url%22%3A%22{webkey}%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Total",
    "sec-ch-ua-mobile": "?0",
    "x-sw-page-view-id": "c47b90dd-9419-49fb-91aa-5e26dae3d1e4",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "accept": "application/json",
    "content-type": "application/json; charset=utf-8"
}

# 请求参数
url = "https://sim.3ue.com/widgetApi/WebsiteAnalysisV2/WebsiteAnalysis/Table"


# 设置会话 cookie
session.cookies.update({
    "cookie": 'GMITM_lang=zh-Hans; GMITM_config={"semrush":{"node":"16","lang":"zh"},"similarweb":{"node":"2","lang":"zh-cn"}}; GMITM_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1bmFtZSI6ImFpMTAyNGJpdCIsInBlcm1pc3Npb25zIjpbInNlbXJ1c2guZ3VydSIsInNpbWlsYXJ3ZWIiLCJ1c2VyIl0sImlhdCI6MTc0MjE0NjQ3NCwiZXhwIjoxNzQyNDA1Njc0fQ.ImFjzELH-mH_CLcodjcjTSk4HXrQ2jngnziJRXbvfCaJljidCFO4jbUkVMgAKfD7KhXvdgWMHi_w0SEEj5hqO1ssa5tr20KzgeJ04QYGaUA031Hegug85UVVHF7ll_q-BOLnlyzzEX4cK-i3l9eJrlvZpjik1DBDE1nU7M20rNH3u1oCq0ZmOq4xUH6I-NEdtBz9L4O8x3yNL_jx2QETT_5j41eJwOf-tiu_dUBUEyxAglM81UmFh7PjoCnc3PQ5dWeDZrpP8g-csHat5F17OoLPURcLz86gDBJpdeVv-J1LAQczMJ_qZcDMitadMvOpZ1zbIoN5xWEKY_7j0TZosQ"; GMITM_uname=ai1024bit; visit_first@semrush.com=1740210326509; sgID@similarweb.com=cfd9de59-e1d6-4813-a614-2a85f09f0fd2; aws-waf-token@sim.similarweb.com=ecac0d03-7f75-44e4-9d91-cdb98e8746c6:AgoAmcg8YeMUAAAA:A88bRC2GBZno+Pb4oQOJZ46CTO/E1r04i+iIc2HZVMkzcVzuvXNVLqcgd4lgXj/zfnP31SsJoBq1LeuzIdJ3g0sMzdZUNFRzXn6z15qBWyTGCdKgt60vKCzEApYd0LbJL/gIM4IIP3JSLfugpe8Ygln4HN/2Jo4/EBwz+3sW0cjN/ZzGs3Z4DyhtewwRI4EBRJIBCGVcXiHzGt5KYIC8WaOoNWKTPu150bUWeA==; locale@similarweb.com=zh-cn; _dd_s@pro.similarweb.com=rum=0&expire=1740362939447; aws-waf-token@pro.similarweb.com=d5693e13-90ae-4c0e-8dc5-1034d11195d7:AAoArS4Lys48AAAA:7ynskcIU+U+uV4ACj3aRIk9+dpWAiCQ/BAcDOOKTHtauzlL+faI7ZhbfWIQKV1/sCA0MHcvz7DbjHFr7v9NCEgObyVqceKPeZbsK3OE5efIHTZiRuOg5pPb2V5uusSDXurIdCaKo9X2e2OayYRD5Am7YuSTilybYs38XmBWDoNRgbjAjaJVSZFtQmTefUsh5std5VseDH0pGbOHBvYVDb7P4XJ/wlx2eHCokZYFgS/YJE/PbLqKTI9BKFB9CvViHDLY='
})

def send_request(page,name):
    max_attempts = 3
    result = {"status": "error", "message": "未知错误", "data": None}
    params = {
        "country": "999",
        "to": "2025|03|13",
        "from": "2025|02|14",
        "isWindow": "true",
        "isDaily": "false",
        "latest": "28d",
        "isDurationChanged": "false",
        "ignoreFilterConsistency": "false",
        "keys": name if name else webkey,  # 如果 name 为空，则使用默认 webkey
        "pageFilterJson": f'[{{"url":"{name if name else webkey}","searchType":"domain"}}]',
        "includeSubDomains": "true",
        "IncludeNoneBranded": "false",
        "IncludeBranded": "false",
        "page": str(page) if page else "1",  # 如果 page 为空，则默认 "1"
        "pageSize": "100",
        "timeGranularity": "Monthly",
        "sort": "Share",
        "asc": "false",
        "webSource": "Total",
        "sourceType": "all"
    }
    for attempt in range(max_attempts):
        try:
            # 动态获取代理 IP 和端口
            proxy_response = requests.get(ip_url, timeout=5)
            proxy_data = proxy_response.text.strip().split('\r\n')[0]
            ip, port = proxy_data.split(":")

            print(f"尝试使用代理: {ip}:{port}")
            proxyurl = f"http://{proxyusernm}:{proxypasswd}@{ip}:{port}"
            proxies = {"http": proxyurl, "https": proxyurl}

            # 发送请求
            response = session.post(url, headers=headers, params=params, proxies=proxies, timeout=20,verify=False)
            response.raise_for_status()  # 检查是否成功
            print(response.text)
            # 成功后更新结果
            result["status"] = "success"
            result["message"] = "请求成功"
            result["data"] = response.json()  # 假设返回的是 JSON 数据
            break

        except requests.exceptions.RequestException as e:
            print(f"请求失败，错误信息：{e}")
            if attempt < max_attempts - 1:
                print("将在 2 秒后尝试新 IP...")
                time.sleep(2)
            else:
                result["message"] = "所有尝试均失败，请检查网络或代理来源"
                break

    return result

@app.route('/api/fetch_data', methods=['GET'])
def fetch_data():
    """通过 GET 请求触发数据抓取，接收 page 和 name 参数"""
    page = request.args.get('page', default=None, type=str)  # 获取 page 参数，默认 None
    name = request.args.get('name', default=None, type=str)  # 获取 name 参数，默认 None
    print(page,name)
    result = send_request(page, name)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
