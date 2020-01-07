import json
import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup



def post_req (target = 'http://httpbin.org/post', data = {'UserId':'Dmitrii', 'Status':'On'}):
    #Ф-ция отправляет post запрос на target, далее проверяет статус запроса
    post_request = requests.post(target, data)
    if post_request.status_code == 200:
        print("Success")
    else:
        print("Something going wrong")

def simple_parser(target = "https://www.chess.com/" ):
    #Ф-ция возвращает кол-во партий, кол-во игроков на сайте target
    response = requests.get(target)
    out=[]
    if response.status_code == 200:
        data = BeautifulSoup(response.text, features = "lxml")  
    else:
        print("Error")
        return None   
    games_q_ty = data.body.div.findAll('li', {"class" : "guest-infographic-item"})
    for information in games_q_ty:
        data_to_out = str(information.text).strip()
        out.append(data_to_out)
    return out
    

post_req()
print(simple_parser())
    