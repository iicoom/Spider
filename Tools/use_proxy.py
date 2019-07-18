import requests

PROXY_POOL_URL = "http://127.0.0.1:5555/random"


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.ConnectionError:
        # print("没有获取到代理ip，请检查代理池内部")
        return None


proxy = get_proxy()
proxies = {
    "http": "http://" + proxy,
    "https": "https://" + proxy,
}
try:
    response = requests.get("http://httpbin.org/get", proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
