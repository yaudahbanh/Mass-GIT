from concurrent.futures import thread
from email import header
import importlib
import requests
requests.packages.urllib3.disable_warnings()
import sys
from colorama import Fore, Back, Style
import os
from multiprocessing.dummy import Pool

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

def scan(web):

	try:

		if '://' not in web :
			webnya = 'http://' + web
		else:
			webnya = web
		
		r = requests.get('{}/.git/HEAD'.format(webnya), verify=False, headers=kepala)

		if 'refs/heads/' not in r.text :
			print('{}[INFO] {}{} {} -> NOT FOUND'.format(fc, fw, webnya, fr))
		else:
			print('{}[INFO] {}{} {} -> GIT FOUND'.format(fc, fw, webnya, fg))
			open('gitfound.txt', 'a').write(webnya+'\n')

	except Exception :
		pass


if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()

	list = sys.argv[1]
	threadnya = sys.argv[2]

	file = open(list, 'r', encoding="utf8").read().splitlines()

	p = Pool(int(threadnya))
	p.map(scan, file)
