import requests


headers = {
    "sec-ch-ua-platform": "\\Windows",
    "Referer": "https://sim.3ue.com/",
    "sec-ch-ua": "\\Chromium;v=\\134, \\Not:A-Brand;v=\\24, \\Microsoft",
    "x-sw-page": "https://pro.similarweb.com/#/organicsearch/pageAnalysis/landing-pages-v2/*/999/28d?key=toolify.ai&pageFilter=%5B%7B%22url%22%3A%22toolify.ai%22%2C%22searchType%22%3A%22domain%22%7D%5D&webSource=Total&selectedPageTab=Organic",
    "sec-ch-ua-mobile": "?0",
    "x-sw-page-view-id": "97de55b1-22f1-46ec-b12b-9b04cb22ddfb",
    "x-requested-with": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "accept": "application/json",
    "content-type": "application/json; charset=utf-8"
}
url = "https://sim.3ue.com/api/websiteOrganicLandingPagesV2/GetTableDrillDown"
params = {
    "country": "999",
    "webSource": "Total",
    "includeSubDomains": "true",
    "to": "2025|03|17",
    "from": "2025|02|18",
    "isWindow": "true",
    "landingPage": "toolify.ai",
    "rowsPerPage": "50",
    "key": "toolify.ai",
    "sort": "ClicksShare",
    "asc": "false",
    "sourceType": "organic",
    "latest": "28d"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)