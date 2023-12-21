import requests
import pyttsx3,time
from bs4 import BeautifulSoup

reservation_date = input("输入想预定的日期，格式类似于20231231，按下回车：")
requests.packages.urllib3.disable_warnings()

def visithalla():

    pt = pyttsx3.init()
    url = 'https://visithalla.jeju.go.kr/reservation/status.do'

    response = requests.get(url,verify=False)

    soup = BeautifulSoup(response.content,'html.parser')

    content = soup.find('td',id='TD_'+reservation_date).a.get_text()
    content_list = content.split('\t')
    content_list2 = [x for x in content_list if x!='']
    content_list3 = [x for x in content_list2 if x!='\r\n']
    if content_list3[3].strip() == '금일예약불가':
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),'无位置')
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '有位置！！！')
        for i in range(4):
            pt.say('有位置!!!')
            pt.runAndWait()

while True:
    x = visithalla()
    time.sleep(30)

