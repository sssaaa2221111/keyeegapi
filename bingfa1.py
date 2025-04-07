import requests

session = requests.Session()
headers = {
    "sec-ch-ua-platform": "\\Windows",
    "Referer": "https://sim.3ue.com/",
    "sec-ch-ua": "\\Chromium;v=\\134, \\Not:A-Brand;v=\\24, \\Microsoft",
    "x-sw-page": "https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=toolify.ai&pageFilter=%5B%7B%22url%22%3A%22toolify.ai%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic",
    "sec-ch-ua-mobile": "?0",
    "x-sw-page-view-id": "89047eb4-005a-40f6-8b23-1b25db0741c0",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "accept": "application/json",
    "content-type": "application/json; charset=utf-8"
}
url = "https://sim.3ue.com/api/websiteOrganicLandingPagesV2"
params = {
    "country": "999",
    "to": "2025|03|17",
    "from": "2025|02|18",
    "isWindow": "true",
    "webSource": "Total",
    "key": "toolify.ai",
    "pageFilterJson": '[{"url":"toolify.ai","searchType":"domain"}]',
    "sort": "ClicksShare",
    "asc": "false",
    "sourceType": "organic",
    "includeSubDomains": "true",
    "latest": "28d"
}
data = '[]'.encode('unicode_escape')
session.cookies.update({"cookie": 'GMITM_lang=zh-Hans; GMITM_config={"semrush":{"node":"16","lang":"zh"},"similarweb":{"node":"2","lang":"zh-cn"}}; GMITM_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1bmFtZSI6ImFpMTAyNGJpdCIsInBlcm1pc3Npb25zIjpbInNlbXJ1c2guZ3VydSIsInNpbWlsYXJ3ZWIiLCJ1c2VyIl0sImlhdCI6MTc0MjQ2MzA3OSwiZXhwIjoxNzQyNzIyMjc5fQ.dzL8xF9GcbGgddzoxjCcr1O42ELIjujvp-wd4JNAMRVTXyoUKTxWCHW--rx9nCM8WDQz_3svaeZaSKzBTimekk9Q8-ln2FpmBqdk4Z0dAL9omoojM-pDsuGqduKg7yq3g29e78V2hEECJk5NJQ_-1qCt_9yZWDUQqDNgdIZXBeyf3hYjCc2_xLYHJqL7JQ5bo_iaqsPVfy6FWvXjY8GprY8XlutNkYV0HIIQxXrEO8AD5ylRJdwnh-MIBCQ9ulgkd0cRGrFQeSgX5gX3I8YyD86-d4L3O5ExuHw9tsD4TqG0-Hi9mVYxKDLNJQkItm40T8FW245DeAelwxpGf9Z3sA"; GMITM_uname=ai1024bit; visit_first@semrush.com=1740210326509; sgID@similarweb.com=cfd9de59-e1d6-4813-a614-2a85f09f0fd2; aws-waf-token@sim.similarweb.com=ecac0d03-7f75-44e4-9d91-cdb98e8746c6:AgoAmcg8YeMUAAAA:A88bRC2GBZno+Pb4oQOJZ46CTO/E1r04i+iIc2HZVMkzcVzuvXNVLqcgd4lgXj/zfnP31SsJoBq1LeuzIdJ3g0sMzdZUNFRzXn6z15qBWyTGCdKgt60vKCzEApYd0LbJL/gIM4IIP3JSLfugpe8Ygln4HN/2Jo4/EBwz+3sW0cjN/ZzGs3Z4DyhtewwRI4EBRJIBCGVcXiHzGt5KYIC8WaOoNWKTPu150bUWeA==; locale@similarweb.com=zh-cn; _dd_s@pro.similarweb.com=rum=0&expire=1740362939447; aws-waf-token@pro.similarweb.com=d5693e13-90ae-4c0e-8dc5-1034d11195d7:AAoArS4Lys48AAAA:7ynskcIU+U+uV4ACj3aRIk9+dpWAiCQ/BAcDOOKTHtauzlL+faI7ZhbfWIQKV1/sCA0MHcvz7DbjHFr7v9NCEgObyVqceKPeZbsK3OE5efIHTZiRuOg5pPb2V5uusSDXurIdCaKo9X2e2OayYRD5Am7YuSTilybYs38XmBWDoNRgbjAjaJVSZFtQmTefUsh5std5VseDH0pGbOHBvYVDb7P4XJ/wlx2eHCokZYFgS/YJE/PbLqKTI9BKFB9CvViHDLY='})

response = session.post(url, headers=headers, params=params)

print(response.text)
print(response)