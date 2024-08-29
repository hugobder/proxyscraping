from bs4 import BeautifulSoup
import requests

def proxy_scraping():
    # Scrap proxy and take only the one working https
    url = "https://free-proxy-list.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    trs = table.find_all("tr")
    proxy_list = []
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) > 0:
            ip = tds[0].text
            port = tds[1].text
            https = tds[6].text
            if https == "yes":
                # Check if the proxy works on a certain website
                test_url = "https://www.google.com"
                proxies = {
                    "http": f"{ip}:{port}",
                    "https": f"{ip}:{port}"
                }
                try:
                    response = requests.get(test_url, proxies=proxies, timeout=5)
                    if response.status_code == 200:
                        print(f"{ip}:{port}", "The proxy is working and added to the proxy list")
                        proxy_list.append(f"{ip}:{port}")
                except requests.exceptions.RequestException:
                    print(f"{ip}:{port}", "The proxy is not working")
    return proxy_list


print(proxy_scraping())