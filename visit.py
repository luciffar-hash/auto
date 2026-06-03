# v1.0.0
import time
import random
import urllib.request

def visit_sites():
    print("開始執行自動訪問程式 v1.0.0")
    try:
        with open('urls.txt', 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        
        for url in urls:
            try:
                # 隨機等待 10 到 60 秒，避免被偵測為機器人
                sleep_time = random.uniform(10, 60)
                print(f"準備訪問: {url}，等待 {sleep_time:.2f} 秒")
                time.sleep(sleep_time)
                
                # 發送請求
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response:
                    if response.status == 200:
                        print(f"成功訪問: {url}")
                    else:
                        print(f"訪問狀態碼異常: {response.status}")
            except Exception as e:
                print(f"訪問 {url} 失敗: {e}")
                
    except FileNotFoundError:
        print("錯誤：找不到 urls.txt 檔案")

if __name__ == "__main__":
    visit_sites()
