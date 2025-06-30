import os
import re
import sys
import time
import json
import uuid
import base64
import socket
import string
import random
import threading
import subprocess
from time import sleep
from datetime import datetime, timedelta
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from pytz import timezone
from colorama import Fore, Back, Style, init
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box, print as rprint
from rich.prompt import Prompt
from rich.table import Table
from rich.columns import Columns
from rich.segment import Segment
from rich.measure import Measurement
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except ImportError:
    os.system('pip install Faker')
    os.system('pip install pycryptodome')
    os.system('pip install requests')
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
os.system("cls" if os.name == "nt" else "clear")
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠤⠶⠴⢶⣶⣤⣤⣤⣕⣶⣼⣿⡀⠀⠀⠀⠀⠀⠀⠀⣿⣏⣶⣶⣤⣤⣤⣶⡶⠦⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢤⣾⣿⣿⣿⡿⣿⣻⣿⠏⠀⠀⠀⢀⡀⠀⠀⠀⢹⣿⢟⣿⢿⣿⣿⣿⣷⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠀⢀⣠⣤⣾⣿⣿⠿⠟⣫⣥⣤⣍⣶⣽⡿⡄⠀⠀⢰⣿⣿⡄⠀⠀⢠⢏⣏⣾⣹⣤⣬⣝⠻⠿⠿⠿⣷⣤⣀⡀⠀⣄⠀⠀
⠀⠀⣸⣿⣿⣿⣷⣶⣿⣿⠻⡏⢢⣤⣼⣿⣿⣿⣓⠿⣷⣄⡀⢹⣏⢀⣠⡴⢿⣊⣿⣿⣿⣧⣤⡔⢹⠟⣿⣷⣶⣾⣿⣿⣿⣏⠀⠀
⠀⢠⢿⣿⡿⢟⣿⣿⣿⣟⡛⠾⣿⡏⠙⢙⢛⢻⣿⣷⣿⣿⣷⣻⣟⣿⣿⣷⣾⢿⡟⠉⣋⠋⢹⣿⡶⢛⣻⣿⣿⣿⡛⢿⣿⡿⡄⠀
⠠⣯⣾⣿⣤⣿⣍⣤⣤⠔⠓⢶⣾⣿⣿⣶⣿⣿⣄⠀⢹⣿⣿⣿⣿⣿⣿⣏⠁⣰⣿⣿⣷⣿⣿⣷⡶⠂⠠⢤⣤⣽⣿⣦⣿⣷⣜⠀
⢰⣼⣿⠀⣻⡿⢟⡏⢀⠴⠚⢛⣻⣿⣿⣿⣿⣿⣿⣦⣌⡙⣿⣿⣿⣿⢋⣡⣴⣿⣿⣿⣿⣿⣿⣟⡛⠓⠦⡀⢻⡻⢿⣟⠀⣿⣧⡄
⢨⢻⣿⢰⡏⣴⡿⠱⠁⢀⠴⠋⣽⣿⣿⣿⣿⣿⡅⠈⠻⠭⣿⣿⣿⣷⠼⠟⠁⢨⣿⣿⣿⣿⣿⣮⡙⠦⡀⠈⠎⢿⡦⠙⡆⣿⡟⡀
⠈⣧⡙⣷⣄⣸⠆⠀⢠⠋⠀⡜⡽⢻⣿⣿⣿⣿⣿⣆⣀⣀⣸⣿⣿⣇⣀⣀⣰⣿⣿⣿⣿⣿⡟⢮⢣⠀⠘⡄⠀⠐⣇⣠⣾⢋⡼⠁
⠀⠀⠘⠻⣿⣇⠀⠀⠀⠀⠀⣇⠁⠟⠟⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠻⠿⠈⣼⠀⠀⠀⠀⠀⣸⡿⠗⠋⠀⠀
⠀⠀⠀⠀⠘⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣷⠘⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠃⣾⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⢹⡏⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠋⠀⢸⡇⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⢸⠁⢀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣾⣷⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⡿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣀⣃⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⠀⡅⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣶⣷⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
  sys.stdout.write(f"\r{BOLD} \033[38;5;155mDang Tải : [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.003)
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print(f"""\033[1;32m
╔══════════════════════╗
║  Version demo        ║
╚══════════════════════╝"""
)
thanhngang(65)

print(f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m1\033[1;39m]\033[1;32m Tool Buff View \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Proxy Lỏ Thì Buff Ít \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m2\033[1;39m]\033[1;32m Tool Spam Sms \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Spam Tin Nhắn Rác \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m3\033[1;39m]\033[1;32m Tool Get Proxy \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Get 9999 Proxy dạng HTTP \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m4\033[1;39m]\033[1;32m Tool Scan Proxy \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Scan Speed \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m5\033[1;39m]\033[1;32m Tool Spam Ngl \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Spam Max Vip \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m6\033[1;39m]\033[1;32m Tool Buff View V2 \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Khá Ổn, Vip Hơn V1 \033[1;39m]\n"
      f"[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;39m[\033[1;35m7\033[1;39m]\033[1;32m Tool Xâm Nhập Website \033[1;39m[\033[32;5;245m\033[1m\033[38;5;39m Deface Website \033[1;39m]"
)
thanhngang(65)
print(f"[\033[1;36mVersion 1.0.0")
chon = input("\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[32;5;245m\033[1m\033[38;5;39mNhập \033[1;33mSố \033[1;34mTool \033[38;5;204mMà \033[38;5;155mBạn \033[1;35mCần \033[1;36mChạy : \033[38;5;204m")  

os.system('cls' if os.name == 'nt' else 'clear')
for i in range(1, 101):
  sys.stdout.write(f"\r{BOLD} \033[38;5;204mVui Lòng Chờ : [{i}% {'█' * (i // 2)}]{RESET}")
  sys.stdout.flush()
  sleep(0.03)
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\033[1;31m31mlỗi kết nối ! ")
    sleep(0.5)
    exit()

if chon == "1":
    exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/view.py').text)
if chon == "2":
     exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/spam.py').text)
if chon == "3":
	exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/scaner.py').text)
if chon == "4":
	exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/checker.py').text)
if chon == "5":
	exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/ngl.py').text)
if chon == "6":
	exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/viewv2.py').text)
if chon == "7":
	exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/gop/refs/heads/main/viewv2.py').text)
