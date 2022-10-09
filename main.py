import pystyle
from pystyle import *
import requests
import sys
from colorama import Fore, Back, Style, init
import os
import random 
from random import randint
import time
init(convert=True)

sucess = 0
failed = 0
counter = 1
# -*- coding: ascii -*-

version = "V 7.8"
build = "TQcX" 


characters = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}'

def PrePairMSG(display, token, channel, message):
    
    global sucess
    global failed
    headers = {"Authorization": token}

    try:
        msg_return = requests.post(f'https://discordapp.com/api/v9/channels/{channel}/messages', headers=headers, json={'content': message})
        if display == 1:
            if msg_return.status_code == 200:
                print(Colorate.Horizontal(Colors.blue_to_green, f"[+] Message {counter} envoyés : {message}"))
                sucess+=1
            elif msg_return.status_code == 404:
                print(Colors.blue_to_green, "[-] Message {counter} n'a pas pu être envoyé | Raison : Désapprouvé")
                failed+=1
            else:
                print(Colors.blue_to_green, "[-] Message {counter} a fait faillite  | Requête : Inconnue")
                failed+=1
        
    except:
        print(Colors.blue_to_green, f"[-] Message {counter} a fait faillite  | Requête : Inconnue")
def random_string():
   return ''.join(random.choice(characters) for i in range(0, random.randint(6,75)))

def job_done():


    print(Fore.BLUE + "*")
    print()
    print()
    print(Colors.blue_to_green, f"[!] État : Fini")
    print(Colors.blue_to_green, f"[i] Messages envoyés: {sucess}")
    print(Colors.blue_to_green, f"[i] Messages fatalistes : {failed}")
    time.sleep(5)
    print()
    main()
    
    
def start_add(token, channel_id):

    start_msg = randint(1, 5)
    if start_msg == 1:
        PrePairMSG(0, token, channel_id, "Qazar RIPPER => ON")
        
    elif start_msg == 2:
        PrePairMSG(0, token, channel_id, "État : Enragé, Décapitant 👿")
        
    elif start_msg == 3:
        PrePairMSG(0, token, channel_id, "```Proxies``` => ON | ```UserAgents``` => ON | ```ImagesChocs``` => OFF")
        
    elif start_msg == 4:
        PrePairMSG(0, token, channel_id, "https://tenor.com/view/trollface-cursed-troll-cursed-trollface-cover-yourself-in-oil-gif-20514967")
        
    elif start_msg == 5:
        PrePairMSG(0, token, channel_id, "```Modules Activated``` => 5/30")
        
    time.sleep(2.1)
    PrePairMSG(0, token, channel_id, f"🇿🇲")
    time.sleep(1)
   
 
def main():
    global counter
    global sucess
    global failed
    
    counter = 1
    sucess = 0
    failed = 0

banner = """
       _____                                                
   ___\__   \_       _____        _____  ______       _____        ___________       
  /     /     \    /      |_     /    / /     /|    /      |_      \          \      
 /     /\     |   /         \   |     |/     / |   /         \      \    /\    \     
|     |  |    |  |     /\    \  |\____\\    / /   |     /\    \      |   \_\    |    
|     | /     |  |    |  |    \  \|___|/   / /    |    |  |    \     |      ___/     
|     |/     /|  |     \/      \    /     /_/____ |     \/      \    |      \  ____  
|\     \_   /_|_ |\      /\     \  /     /\      ||\      /\     \  /     /\ \/    \ 
| \_____\\______\| \_____\ \_____\/_____/ /_____/|| \_____\ \_____\/_____/ |\______| 
| |     |       || |     | |     ||    |/|     | || |     | |     ||     | | |     | 
 \|_____|_______| \|_____|\|_____||____| |_____|/  \|_____|\|_____||_____|/ \|_____| 
                                                                                     

"""


Write.Print(banner, Colors.blue_to_green, interval=0.000005)





print()


print(Colors.blue_to_green, "MODES : 1 => SPAM / 2 => DESPAM ")

print(Style.RESET_ALL)

print()






mode = int(input("MOD (1) : "))
token = input("[T] Colle ton token ici :")
channel_id = int(input("[C] Donne-moi l'ID du salon : "))
if mode == 1:
        file = input("Le nom du fichier (eg. debitage.txt) : ")
        num_lines = 0
        with open(file) as infp:
            for line in infp:
                if line.strip():
                    num_lines += 1
        #num_lines = sum(1 for line in open(file))
        print()
        print(Colors.blue_to_green, f"Si tu utilises le 1er MOD, merci d'entrer ce nombre \"{num_lines}\"")
        print(Style.RESET_ALL)
        msgsend =  int(input("Entre ton nombre : "))
        print()
        print(Colors.blue_to_green, f"Le chemin ou le nom du fichier : ")
        print(Style.RESET_ALL)

        
print(Style.RESET_ALL)
print()
print()
print(Colors.blue_to_green, f"TOKEN : {token}")
print(Colors.blue_to_green,f"CID : {channel_id}")
print(Colors.blue_to_green, f"QUANTITÉ : {msgsend}")
print()
print(Colors.blue_to_green, f"[x] Débute dans 3 secondes [x]")


     
start_add(token, channel_id)
if mode == 1:
        with open(file, "r") as a_file:
            for line in a_file:
                if counter < msgsend :
                    message = line.strip()
                    if(len(message) > 0):
                        PrePairMSG(1, token, channel_id, message)
                        counter+=1
                        time.sleep(2.1)
                    else:
                        print(Colors.blue_to_green, f"[-] Empty String! Skipping...")
                else:
                    job_done()
            else:
               job_done()

job_done()
            

            
if __name__ == '__main__':
    main()




