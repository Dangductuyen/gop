from time import sleep
import sys
from colorama import Fore, Back, Style
import random
import random
import sys
import os
import sys
import time
import json
import os
import sys
import time
import random
import requests
import subprocess
import uuid
import hashlib
from collections import defaultdict    
from datetime import datetime, timedelta, timezone 
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate   
from rich.columns import Columns
from rich.segment import Segment
from rich.measure import Measurement
import random
import string
import requests
import base64
import subprocess
import uuid
import hashlib
from collections import defaultdict    
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from colorama import init
from pystyle import Colors, Colorate
from time import sleep
from colorama import Fore, Back, Style
import random
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich import print as rprint
from rich.prompt import Prompt
from time import sleep
from colorama import Fore, Back, Style
import random
import sys
from time import sleep
from colorama import Fore, Back, Style
import requests
import json
from colorama import Fore, Style
from datetime import datetime, timedelta
from pytz import timezone
import requests
import time
import json
import sys
import random
import string
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import threading
from threading import BoundedSemaphore
import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from datetime import datetime, timedelta
import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    from colorama import init, Fore
    from rich.console import Console
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
# import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests
TOOL_URL = "https://raw.githubusercontent.com/Dangductuyen/gop/main/gop.py"
VERSION_FILE_URL = "https://raw.githubusercontent.com/Dangductuyen/gop/main/version.txt"
LOCAL_FILE = "gop.py"
LOCAL_VERSION_FILE = "version.txt"

def get_local_version():
    try:
        with open(LOCAL_VERSION_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

def get_remote_version():
    try:
        response = requests.get(VERSION_FILE_URL)
        if response.ok:
            return response.text.strip()
    except:
        pass
    return None

def update_tool():
    try:
        response = requests.get(TOOL_URL)
        version_response = requests.get(VERSION_FILE_URL)
        if response.ok and version_response.ok:
            with open(LOCAL_FILE, "wb") as f:
                f.write(response.content)
            with open(LOCAL_VERSION_FILE, "w") as f:
                f.write(version_response.text.strip())
            print("\033[1;32m✅ Đã cập nhật tool thành công! Đang khởi động lại...\n")
            sleep(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print("\033[1;31m❌ Không thể tải file cập nhật.")
    except Exception as e:
        print(f"\033[1;31mLỗi khi cập nhật: {e}")

def main():
    local_version = get_local_version()
    remote_version = get_remote_version()

    if remote_version and remote_version != local_version:
        print(f"\033[1;33m🔄 Có bản cập nhật mới: {remote_version} (hiện tại: {local_version})")
        input("Nhấn Enter để cập nhật...")
        update_tool()
    else:
        print(f"\033[1;32m✅ Đang dùng phiên bản mới nhất: {local_version}")
        # Gọi tool thật ở đây
        # Ví dụ: gọi hàm chính hoặc in hướng dẫn
        print("🚀 Tool đã sẵn sàng sử dụng!")

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
AQUA = "\033[96m"
LIME = "\033[92m"
xam='\033[1;30m'
black='\033[1;19m'
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"

def thanhngang(so):
    for i in range(so):
        print(trang+'\033[1;31m-',end ='')
    print('')
    
os.system('cls' if os.name == 'nt' else 'clear')
print(">> Loading...")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
xoss("\n\033[1;32mVui Lòng Chờ... ")
sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD}{LIME}ĐANG LOAD TOOL + GIT +: [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
sleep(1)
import os
os.system("cls" if os.name == "nt" else "clear")
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)
xoss('\n\033[1;32m[●] \033[93mĐang \033[96mLoad \033[95mAPI \033[94mTool...');time.sleep(0.10)
xoss('\n\033[1;36m[●] \033[94mkiểm \033[93mtra \033[95msever \033[96mtool...')
xoss('\n\033[1;33m[●] \033[96mkiểm \033[95mtra \033[94mbản \033[93mupdate.. ')
xoss('\n\033[1;34m[●] \033[91mTiến \033[96mhành \033[94mvào \033[95mtool...')
def Update():
    exit('\033[1;31m[●] Đang Tiến Hành Vào Tool...... ')

sleep(1)
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương 
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

os.system('cls' if os.name == 'nt' else 'clear')
banner = f"""\033[1;32m
▓█████▄  █    ██  ▄████▄  ▄▄▄█████▓ █    ██▓██   ██▓▓█████  ███▄    █ 
▒██▀ ██▌ ██  ▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒ ██  ▓██▒▒██  ██▒▓█   ▀  ██ ▀█   █ 
░██   █▌▓██  ▒██░▒▓█    ▄ ▒ ▓██░ ▒░▓██  ▒██░ ▒██ ██░▒███   ▓██  ▀█ ██▒
░▓█▄   ▌▓▓█  ░██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ▓▓█  ░██░ ░ ▐██▓░▒▓█  ▄ ▓██▒  ▐▌██▒
░▒████▓ ▒▒█████▓ ▒ ▓███▀ ░  ▒██▒ ░ ▒▒█████▓  ░ ██▒▓░░▒████▒▒██░   ▓██░
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░  ▒ ░░   ░▒▓▒ ▒ ▒   ██▒▒▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
 ░ ▒  ▒ ░░▒░ ░ ░   ░  ▒       ░    ░░▒░ ░ ░ ▓██ ░▒░  ░ ░  ░░ ░░   ░ ▒░
 ░ ░  ░  ░░░ ░ ░ ░          ░       ░░░ ░ ░ ▒ ▒ ░░     ░      ░   ░ ░ 
   ░       ░     ░ ░                  ░     ░ ░        ░  ░         ░ 
 ░               ░                          ░ ░                       
"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.001)

init(autoreset=True)
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD} \033[38;5;155mĐANG LOAD MENU : [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.003)  # Điều chỉnh thời gian chờ nếu cần
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print(f"""\033[1;32m
╔══════════════════════╗
║  Tool Hiện có        ║
╚══════════════════════╝"""
)
thanhngang(65)

print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m1\033[1;39m]\033[1;32m Tool Buff View TikTok \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Proxy Nhanh Die \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m2\033[1;39m]\033[1;32m Tool Spam Sms \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Spam Tin Nhắn Rác \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m3\033[1;39m]\033[1;32m Tool Golike Twitter ( X ) \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Cookie VIP \033[1;39m]"
)
thanhngang(65)

chon = input("\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[32;5;245m\033[1m\033[38;5;39mNhập \033[1;33mSố \033[1;34mTool \033[38;5;204mMà \033[38;5;155mBạn \033[1;35mCần \033[1;36mChạy : \033[38;5;204m")  

os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD} \033[38;5;204mCHỜ ĐỢI LÀ HẠNH PHÚC: [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)  # Điều chỉnh thời gian chờ nếu cần
  


# hàm chống bug mạng tránh mấy a bug lỏd 🤟
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;31mCheck Mạng Wifi Hoặc 4G! ")
    sleep(0.5)
    exit()

if chon == "1":
    exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/view.py').text)
if chon == "2":
     exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/spam.py').text)
if chon == "3":
	exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/uhgcc/refs/heads/main/Ggttttttttttttttrtttfcvyu88ibb.py').text)
# if chon == 

    
