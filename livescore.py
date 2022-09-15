from playsound import playsound
from time import sleep
import requests
import pandas as pd
import datetime
yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y%m%d")
today = (datetime.datetime.now()).strftime("%Y%m%d")
url = f"https://prod-public-api.livescore.com/v1/api/react/date/soccer/{today}/0.00?MD=1"
scores_1 = [None, None]
scores_2 = [None, None]
fav_team = input("Favourite Team: ")
while True:
    matches = requests.get(url).json()
    for stage in matches["Stages"]:
        for event in stage["Events"]:
            try:
#                 print('no')
                time = datetime.datetime.strptime(str(event['Esd']),"%Y%m%d%H%M%S" )
                time_string = time.strftime('%Y-%m-%d  %H:%M')
                if(event['T2'][0]['Nm'].lower() == fav_team.lower() or event['T1'][0]['Nm'].lower() == fav_team.lower()):
                    if(scores_1 == [None, None] and scores_2 == [None, None]):
                        scores_1 = [event['Tr1'], event['Tr2']]
                        scores_2 = [event['Tr1'], event['Tr2']]
#                         print('none')
                    else:
                        if(scores_2 == [event['Tr1'], event['Tr2']]):
                            pass
                        else:
#                             print('hi')
                            playsound('E:\\livescore\\assets\\mixkit-bell-notification-933.wav')
                            scores_2 = [event['Tr1'], event['Tr2']]
                            scores_1 = scores_2
                            
                    print(time_string, event['T1'][0]['Nm'], event['Tr1'], event['Tr2'], event['T2'][0]['Nm'], event['Eps'], )
            except:
                continue
    sleep(10)