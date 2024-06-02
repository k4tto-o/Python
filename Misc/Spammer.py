import requests
import time

payload = {
    'content': 'busco dragon perma, md'
}
header = {
    'authorization': 'MTA5MTQyNjczNDg0ODYyMjcyNA.GZj3hj.d67MYph3BSG_MKiPZl3ULz4gi7ew_Yp0r3MkDY'
}
while True:
    time.sleep(31)
    r = requests.post('https://discord.com/api/v9/channels/858002947529900032/messages', data=payload, headers=header)