from pprint import pprint
from config import phone_number
import requests
url= "https://api-ssl.bitly.com/v4/user"


tokeen="fe9acb6db9a23074432d30ed34d4ccf57132506d"



headers = {
 "Authorization": f"Bearer {tokeen}",
 "Content-Type": "application/json"
}






while True:
    print("программа работ со ссылками бitly")
    print("1) Получить инвормацию о профиле")
    print("2) Сократить ссылку")
    print("3) выход")
    print("4) донат")
    x=input("виберите функцию: ")

    
    if x=="1":
        response = requests.get(url,headers=headers)    
        response.raise_for_status() 
        pprint(response.json())
    if x=="2":
        user_url=input("введите ссылку для сокращения: " )
        url = "https://api-ssl.bitly.com/v4/shorten"
        params={
            "long_url" : user_url
        }
    

        response = requests.post(url,json=params,headers=headers)
        try:
            response.raise_for_status()
            pprint(response.json())
        except:
            print("напишите правильную ссылку")
    if x=="3":
        exit()
    if x=="4":
        print(phone_number)





