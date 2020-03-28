from bs4 import BeautifulSoup
import requests

print('Welcome to COVID-19 Chatbot')
while True :
    print('1. The COVID-19 situation in the area')
    print('2. What is COVID-19?')
    print("3. What's the symptoms after affected by COVID-19? ")
    print('4. How to protect my self from COVID-19?')
    print('5. Do we really need masks?')
    print("6. Quit the program" )
    ans = int(input('What do you want to know? (1-6): '))
    while ans<1 or ans>6:
        print('Only input 1-6!')
        ans = int(input('What do you want to know? (1-6): '))
    if ans == 1:
        con = input('Which country do you want know? : ')
        country = con
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
        message_indo = "Total terinfeksi = {}, Kasus Baru = {}, Total Kematian = {}, Kematian Baru = {}, Sembuh = {}, Kasus Aktif = {}, Keadaan Kritikal = {}".format(*data)
        message_en = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Recovered = {}, Active Case = {}, Serious Critical = {}".format(*data)
        print(message_en)
        print('')
    elif ans == 2:
        print('Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).')
        print('')
    elif ans == 3:
        print("The most common symptoms of COVID-19 are fever, tiredness, and dry cough. "
              "Some patients may have aches and pains, nasal congestion, runny nose, sore throat or diarrhea. ")

        print('')
    elif ans == 4:
        print("1. Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water.")
        print("2. Maintain at least 1 metre (3 feet) distance between yourself and anyone who is coughing or sneezing.")
        print("3. Avoid touching eyes, nose and mouth.")
        print("4. Make sure you, and the people around you, follow good respiratory hygiene. ")
        print("5. Stay home if you feel unwell. If you have a fever, cough and difficulty breathing, seek medical attention and call in advance. "
              "Follow the directions of your local health authority.")
        print("6. Keep up to date on the latest COVID-19 hotspots ")
        print('')
    elif ans == 5:
        print('Wearing a face mask is certainly not an iron-clad guarantee that you won’t get sick – '
              'viruses can also transmit through the eyes and tiny viral particles, known as aerosols, can penetrate masks.')
    elif ans == 6:
        print('Stay safe everyone! Remember to wash your hands and STAY AT HOME!!')
        print('Bye!')
        break



