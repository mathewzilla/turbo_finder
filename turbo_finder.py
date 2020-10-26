from bs4 import BeautifulSoup
import requests
import re
import time
import beepy
import webbrowser

# banneton_site = [{'url': "https://www.bakerybits.co.uk/1kg-oval-waffle-pattern-brotform", 'search': 'Unfortunately'}]
trainer_sites = [{'name': 'kickr core', 'url': "https://uk.wahoofitness.com/devices/bike-trainers/kickr-core-indoor-smart-trainer-reconditioned-euuk", 'search': 'This product is out of stock', 'catch': 'There has been an error processing your request'}]
                #  {'name': 'kickr snap', 'url': "https://uk.wahoofitness.com/devices/bike-trainers/wahoo-kickr-snap-refurbished", 'search': 'This product is out of stock', 'catch': 'There has been an error processing your request'},   
                #  {'name': 'sigma tacx flux', 'url': "https://www.sigmasports.com/item/Tacx/FLUX-S-Smart-Turbo-Trainer-T2900S/K104", 'search': 'out of stock', 'catch': 'sigma dummy catch'},
                #  {'name': 'halfords elite direto OTS', 'url': "https://www.halfords.com/cycling/turbo-trainers/smart-turbo-trainers/elite-direto-ots-2-percent-turbo-trainer-732044.html", 'search': 'Unfortunately', 'catch': 'halfords dummy catch'},
                #  {'name': 'decathlon tacx flow', 'url': "https://www.decathlon.co.uk/flow-smart-t2240-turbo-trainer-800-watts-id_8345488.html", 'search': 'Product out of stock', 'catch': 'decathlon dummy catch'},
                #  {'name': 'wiggle tacx flux', 'url': "https://www.wiggle.co.uk/tacx-flux-s-direct-drive-smart-trainer/", 'search': 'Out of stock.', 'catch': 'The service is unavailable.'}]

while True:
    for s in trainer_sites:
        content = requests.get(s['url'])
        soup = BeautifulSoup(content.text, 'html.parser')
        catch = soup.find_all(text = re.compile(s['catch']))
        result = soup.find_all(text = re.compile(s['search']))
        if not result:
            if catch:
                print(soup)
                print(s['name']+' overloaded')
                # beepy.beep(sound='robot_error')
            else: 
                print('TRAINER HERE? '+s['url'])
                webbrowser.open(s['url'])
                # print(soup)
                for i in range(3):
                    beepy.beep(sound='coin')
        

    # for s in banneton_site:
    #     content = requests.get(s['url'])
    #     soup = BeautifulSoup(content.text, 'html.parser')
    #     result = soup.find_all(text = re.compile(s['search']))
    #     if not result:
    #         print('BANNETON HERE? '+s['url'])
    #         for i in range(3):
    #             beepy.beep(sound='ping')
    
    time.sleep(60)