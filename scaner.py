import requests
import concurrent.futures
import os

GET_URLS = [
    'https://www.proxyscan.io/api/proxy?format=txt&type=http',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt'
]

OUTPUT_FILE = 'proxy.txt'
TEST_URL = 'http://httpbin.org/ip'
TIMEOUT = 5
MAX_THREADS = 100

live_proxies = set()

def fetch_proxies():
    proxies = set()
    print('[INFO] Fetching proxies...')
    for url in GET_URLS:
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                fetched = res.text.strip().splitlines()
                proxies.update(p.strip() for p in fetched if p.strip())
                print(f'[+] {len(fetched)} proxies from {url}')
        except Exception as e:
            print(f'[ERROR] Failed to fetch from {url}: {e}')
    print(f'[INFO] Total fetched: {len(proxies)} proxies\n')
    return proxies

def is_proxy_alive(proxy):
    try:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
        res = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
        if res.status_code == 200:
            print(f'[LIVE] {proxy}')
            return proxy
    except:
        pass
    return None

def check_proxies(proxies):
    print('[INFO] Checking proxies...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = list(executor.map(is_proxy_alive, proxies))
    live = [p for p in results if p]
    return list(set(live))  # Loại bỏ proxy trùng

def save_to_file(proxies):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
    print(f'\n[SAVED] {len(proxies)} live proxies saved to "{OUTPUT_FILE}"')

def main():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    all_proxies = fetch_proxies()
    alive_proxies = check_proxies(all_proxies)
    save_to_file(alive_proxies)
    print('\n[FINISHED] Proxy scan done.')

if __name__ == '__main__':
    main()
