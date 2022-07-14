from email import header
import importlib
import requests
requests.packages.urllib3.disable_warnings()
import sys
from colorama import Fore, Back, Style
import os

fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN
fy	=	Fore.YELLOW	
fb	=	Fore.BLUE										
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT


kepala = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "en,en-US;q=0.9",
	"cache-control": "max-age=0",
	"dnt": "1",
	"sec-ch-ua-mobile": "?0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "none",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
	}

def banner():

	print("""
	__ __  ___  ___  ___  
	|  \  \| . |/ __>/ __> 
	|     ||   |\__ \\__ \ 
	|_|_|_||_|_|<___/<___/ 
	___   _  ___          
	/  _> | ||_ _|         
	| <_/\| | | |          
	`____/|_| |_|  

	Abdi Pranata
	https://fb.me/abdi.dot.id        
                      
	""")

def scan():

	list = sys.argv[1]

	file = open(list, 'r', encoding="utf8").read().splitlines()

	for yaa in file :

		if '://' not in yaa :
			webnya = 'http://' + yaa
		else:
			webnya = yaa
		
		r = requests.get('{}/.git/HEAD'.format(webnya), verify=False, headers=kepala)

		if r.status_code == 200 :
			print('{}[INFO] {}{} {} -> GIT FOUND'.format(fc, fw, webnya, fg))
		if 'refs/heads/master' in r.text :
			print('{}[INFO] {}{} {} -> GIT FOUND'.format(fc, fw, webnya, fg))
		else:
			print('{}[INFO] {}{} {} -> NOT FOUND'.format(fc, fw, webnya, fr))

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	scan()
