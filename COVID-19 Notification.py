from win10toast import ToastNotifier
from bs4 import BeautifulSoup
import requests
import time

country = 'Indonesia'
notification_duration = 50 #in seconds
refresh_time = 1 #in minutes
data_check = []

def data_cleanup(array):
    L = []
    for i in array:
        i = i.replace("+"," ")
        i = i.replace("-"," ")
        i = i.replace(",",".")
        if i == "":
            i = "0"
        L.append(i.strip())
    return L
while True:
    html_page = requests.get("https://www.worldometers.info/coronavirus/")
    bs = BeautifulSoup(html_page.content, 'html.parser')

    search = bs.select("div tbody tr td")
    start = -1
    for i in range(len(search)):
        if search[i].get_text().find(country) != -1:
            start = i
            break
    data = []
    for i in range(1,8):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]

    data = data_cleanup(data)
    message = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Recovered = {}, Active Case = {}, Serious Critical = {}".format(*data)

    if data_check != data:
        data_check = data
        toaster = ToastNotifier()
        toaster.show_toast("Coronavirus Update {}".format(country), message, duration= notification_duration, icon_path="C:/Users/asus liberty/Pictures/Medium/virus.ico")
    else:
        time.sleep(refresh_time*5)
        break
