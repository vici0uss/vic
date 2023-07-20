# vic
spam report discord
import requests
token=input("TOKEN ->")
channel_ID=input("channel ID ->")
Guild_ID=input("Server ID ->")
Massage_ID=input("Massage ID ->")
print ("""/ ____\___________   ____ |  |__ |__|    ______ ___.__. 
\   __\/ __ \_  __ \_/ ___\|  |  \|  |    \____ <   |  | 
 |  | \  ___/|  | \/\  \___|   Y  \  |    |  |_> >___  | 
 |__|  \___  >__|    \___  >___|  /__| /\ |   __// ____| 
           \/            \/     \/     \/ |__|   \/      "")


print("""
-----------------------------------------------------
|      Contenue illégal              |       0       |
|      Harcelement                  |       1       |
|      Spam ou lien malvéillant       |       2       |
|      Contenue pornographique                   |       3       |
|      violation liscence                 |       4       |
-----------------------------------------------------
""")
Reason=input("Reason (0-4)->")

header={
    "authorization": token,
    "content-type": "application/json"
}

payload={
    "channel_id": channel_ID,
    "guild_id": Guild_ID,
    "message_id": Massage_ID,
    "reason": Reason
}

url='https://discord.com/api/v9/report'

r=requests.post(url=url, headers=header, json=payload)

print(r.content)

i=1
