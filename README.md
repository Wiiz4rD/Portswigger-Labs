# Portswigger-Labs
No professional version of BurpSuite? It doesn 't matter . I wrote scripts to solve their labs.

## user_enum_via_lock
Solve PortSwigger Lab 'Username enumeration via account lock' without BurpSuite Pro. 

How to use: Change target_url var to your lab url. This variable should have the form 'https://something.web-security-academy.net/login'

Run intruder.py

## 2FA_broken_auth
Solve PortSwigger Lab 'Lab: 2FA broken logic' without BurpSuite Pro. 

How to use: Change target_url and target_2fa var to your lab url. This variable should have the form 'https://something.web-security-academy.net/login' and 'https://something.web-security-academy.net/login2'

Check name and pass in username , password and target_user var.

Run bruteforce2FA.py

After brute force the 2fa code, the status of the laboratory will change to solved.

## 2FA_bypass_auth_brute

Solve PortSwigger Lab 'Lab: 2FA bypass using a brute-force attack' faster without BurpSuite Pro. 

How to use: Change target_url and target_2fa var to your lab url. This variable should have the form 'https://something.web-security-academy.net/login' and 'https://something.web-security-academy.net/login2'

Check name and pass in username var.

Run bypass_2fa_auth.py

After brute force the 2fa code, the status of the laboratory will change to solved.
