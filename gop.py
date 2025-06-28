import os
import sys
import time
import requests
from time import sleep
from colorama import Fore, init
from rich.console import Console

init(autoreset=True)
console = Console()

# ==================== AUTO UPDATE ====================

TOOL_URL = "https://raw.githubusercontent.com/Dangductuyen/gop/main/gop.py"
LOCAL_FILE = "gop.py"

def get_remote_code():
    try:
        response = requests.get(TOOL_URL, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Không thể tải file từ GitHub: {e}")
        return None

def get_local_code():
    try:
        with open(LOCAL_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def auto_update():
    print(f"{Fore.CYAN}[INFO] Đang kiểm tra cập nhật tool từ GitHub...")
    remote_code = get_remote_code()
    local_code = get_local_code()

    if remote_code is None:
        print(f"{Fore.YELLOW}[WARNING] Không thể kiểm tra cập nhật. Dùng phiên bản hiện tại.")
        return

    if remote_code.strip() != local_code.strip():
        print(f"{Fore.GREEN}[INFO] Có bản cập nhật mới. Đang cập nhật...")
        with open(LOCAL_FILE, "w", encoding="utf-8") as f:
            f.write(remote_code)
        print(f"{Fore.LIGHTGREEN_EX}[INFO] Cập nhật thành công! Khởi động lại tool...")
        sleep(1)
        os.execv(sys.executable, [sys.executable, LOCAL_FILE])
    else:
        print(f"{Fore.CYAN}[INFO] Tool đang ở phiên bản mới nhất.")

# ==================== HIỆU ỨNG ====================

def thanhngang(so):
    print("\033[1;31m" + "-" * so + "\033[0m")

def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def loading_bar(msg, speed=0.03):
    for i in range(1, 101):
        sys.stdout.write(f"\r{Fore.GREEN}{msg} [{i}% {'█' * (i // 2)}]")
        sys.stdout.flush()
        sleep(speed)

def check_internet_connection():
    try:
        requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# ==================== MAIN TOOL ====================

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    auto_update()

    xoss("\n\033[1;32mVui Lòng Chờ... ")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    loading_bar("ĐANG LOAD TOOL + GIT +")
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

    xoss('\n\033[1;32m[●] \033[93mĐang \033[96mLoad \033[95mAPI \033[94mTool...')
    xoss('\n\033[1;36m[●] \033[94mKiểm \033[93mtra \033[95msever \033[96mtool...')
    xoss('\n\033[1;33m[●] \033[96mKiểm \033[95mtra \033[94mbản \033[93mupdate...')
    xoss('\n\033[1;34m[●] \033[91mTiến \033[96mhành \033[94mvào \033[95mtool...')
    sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    import os
import sys
import time
import requests
from time import sleep
from colorama import Fore, init
from rich.console import Console

init(autoreset=True)
console = Console()

# ==================== AUTO UPDATE ====================

TOOL_URL = "https://raw.githubusercontent.com/Dangductuyen/gop/main/gop.py"
LOCAL_FILE = "gop.py"

def get_remote_code():
    try:
        response = requests.get(TOOL_URL, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Không thể tải file từ GitHub: {e}")
        return None

def get_local_code():
    try:
        with open(LOCAL_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def auto_update():
    print(f"{Fore.CYAN}[INFO] Đang kiểm tra cập nhật tool từ GitHub...")
    remote_code = get_remote_code()
    local_code = get_local_code()

    if remote_code is None:
        print(f"{Fore.YELLOW}[WARNING] Không thể kiểm tra cập nhật. Dùng phiên bản hiện tại.")
        return

    if remote_code.strip() != local_code.strip():
        print(f"{Fore.GREEN}[INFO] Có bản cập nhật mới. Đang cập nhật...")
        with open(LOCAL_FILE, "w", encoding="utf-8") as f:
            f.write(remote_code)
        print(f"{Fore.LIGHTGREEN_EX}[INFO] Cập nhật thành công! Khởi động lại tool...")
        sleep(1)
        os.execv(sys.executable, [sys.executable, LOCAL_FILE])
    else:
        print(f"{Fore.CYAN}[INFO] Tool đang ở phiên bản mới nhất.")

# ==================== HIỆU ỨNG ====================

def thanhngang(so):
    print("\033[1;31m" + "-" * so + "\033[0m")

def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def loading_bar(msg, speed=0.03):
    for i in range(1, 101):
        sys.stdout.write(f"\r{Fore.GREEN}{msg} [{i}% {'█' * (i // 2)}]")
        sys.stdout.flush()
        sleep(speed)

def check_internet_connection():
    try:
        requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# ==================== MAIN TOOL ====================

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    auto_update()

    xoss("\n\033[1;32mVui Lòng Chờ... ")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    loading_bar("ĐANG LOAD TOOL + GIT +")
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

    xoss('\n\033[1;32m[●] \033[93mĐang \033[96mLoad \033[95mAPI \033[94mTool...')
    xoss('\n\033[1;36m[●] \033[94mKiểm \033[93mtra \033[95msever \033[96mtool...')
    xoss('\n\033[1;33m[●] \033[96mKiểm \033[95mtra \033[94mbản \033[93mupdate...')
    xoss('\n\033[1;34m[●] \033[91mTiến \033[96mhành \033[94mvào \033[95mtool...')
    sleep(1)

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

    loading_bar("ĐANG LOAD MENU :", 0.003)
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print(f"""\033[1;32m
╔══════════════════════╗
║  Tool Hiện có        ║
╚══════════════════════╝"""
    )
    thanhngang(65)

    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m1\033[1;39m => Tool Buff View TikTok")
    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m2\033[1;39m => Tool Spam Sms")
    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m3\033[1;39m => Tool GoLike Twitter (X)")
    thanhngang(65)

    chon = input("\033[1;39m[\033[1;36m•_•\033[1;39m] => Nhập số tool cần chạy: \033[1;33m")

    os.system('cls' if os.name == 'nt' else 'clear')
    loading_bar("CHỜ ĐỢI LÀ HẠNH PHÚC:")
    sleep(1)

    if not check_internet_connection():
        print("\033[1;31mCheck Mạng Wifi Hoặc 4G! ")
        sleep(0.5)
        exit()

    if chon == "1":
        exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/view.py').text)
    elif chon == "2":
        exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/spam.py').text)
    elif chon == "3":
        exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/uhgcc/refs/heads/main/Ggttttttttttttttrtttfcvyu88ibb.py').text)
    else:
        print("\033[1;31m[!] Không hợp lệ!")

# ==================== CHẠY TOOL ====================
if __name__ == "__main__":
    main()

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.001)

    loading_bar("ĐANG LOAD MENU :", 0.003)
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print(f"""\033[1;32m
╔══════════════════════╗
║  Tool Hiện có        ║
╚══════════════════════╝"""
    )
    thanhngang(65)

    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m1\033[1;39m => Tool Buff View TikTok")
    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m2\033[1;39m => Tool Spam Sms")
    print(f"\033[1;39m[\033[1;36m•_•\033[1;39m] => \033[1;32mNhập \033[1;35m3\033[1;39m => Tool GoLike Twitter (X)")
    thanhngang(65)

    chon = input("\033[1;39m[\033[1;36m•_•\033[1;39m] => Nhập số tool cần chạy: \033[1;33m")

    os.system('cls' if os.name == 'nt' else 'clear')
    loading_bar("CHỜ ĐỢI LÀ HẠNH PHÚC:")
    sleep(1)

    if not check_internet_connection():
        print("\033[1;31mCheck Mạng Wifi Hoặc 4G! ")
        sleep(0.5)
        exit()

    if chon == "1":
        exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/view.py').text)
    elif chon == "2":
        exec(requests.get('https://raw.githubusercontent.com/Dangductuyen/view/refs/heads/main/spam.py').text)
    elif chon == "3":
        exec(requests.get('https://raw.githubusercontent.com/Phuocnifepkay/uhgcc/refs/heads/main/Ggttttttttttttttrtttfcvyu88ibb.py').text)
    else:
        print("\033[1;31m[!] Không hợp lệ!")

# ==================== CHẠY TOOL ====================
if __name__ == "__main__":
    main()
