import os, sys, re, json, requests, random, time
os.system("git pull")

FR = "\x1b[38;5;196m" # Merah
FG = "\x1b[38;5;46m"  # Hijau
FY = "\x1b[38;5;228m" # YELLOW
FB = "\x1b[38;5;86m" # BLUE
FRAN = random.choice([FR, FG, FY, FB])
FD = "\x1b[0;00m" # NEUTRAL

def Banner():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠂⢉⠤⠐⠋⠈⠡⡈⠉⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⢠⣤⠔⠁⢀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠈⠱⡤⣤⠄⣀⠀⠀⠀⠀⠀
⠀⠀⠰⠁⠀⣰⣿⠃⠀⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢞⣦⡀⠈⡇⠀⠀⠀
⠀⠀⠀⢇⣠⡿⠁⠀⢀⡃⠀⣈⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⢢⠰⠀⠀⢺⣧⢰⠀⠀⠀⠀
⠀⠀⠀⠈⣿⠁⡘⠀⡌⡇⠀⡿⠸⠀⠀⠀⠈⡕⡄⠀⠐⡀⠈⠀⢃⠀⠀⠾⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠇⡇⠃⢠⠀⠶⡀⡇⢃⠡⡀⠀⠀⠡⠈⢂⡀⢁⠀⡁⠸⠀⡆⠘⡀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⢸⠀⠘⡜⠀⣑⢴⣀⠑⠯⡂⠄⣀⣣⢀⣈⢺⡜⢣⠀⡆⡇⠀⢣⠀⠀⠀⠀
⠀⠀⠀⠇⠀⢸⠀⡗⣰⡿⡻⠿⡳⡅⠀⠀⠀⠀⠈⡵⠿⠿⡻⣷⡡⡇⡇⠀⢸⣇⠀⠀⠀
⠀⠀⢰⠀⠀⡆⡄⣧⡏⠸⢠⢲⢸⠁⠀⠀⠀⠀⠐⢙⢰⠂⢡⠘⣇⡇⠃⠀⠀⢹⡄⠀⠀
⠀⠀⠟⠀⠀⢰⢁⡇⠇⠰⣀⢁⡜⠀⠀⠀⠀⠀⠀⠘⣀⣁⠌⠀⠃⠰⠀⠀⠀⠈⠰⠀⠀
⠀⡘⠀⠀⠀⠀⢊⣤⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⢸⠃⠀⠀⠀⠀⠀⠃⠀
⢠⠁⢀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠸⠀
⠘⠸⠘⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠁⠀⠃⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⢠⠀⠀⡇
⠀⠇⢆⢃⠀⠀⠀⠀⠀⡏⢲⢤⢀⡀⠀⠀⠀⠀⠀⢀⣠⠄⡚⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀
⢰⠈⢌⢎⢆⠀⠀⠀⠀⠁⣌⠆⡰⡁⠉⠉⠀⠉⠁⡱⡘⡼⠇⠀⠀⠀⠀⢀⢬⠃⢠⠀⡆
⠀⢢⠀⠑⢵⣧⡀⠀⠀⡿⠳⠂⠉⠀⠀⠀⠀⠀⠀⠀⠁⢺⡀⠀⠀⢀⢠⣮⠃⢀⠆⡰⠀
⠀⠀⠑⠄⣀⠙⡭⠢⢀⡀⠀⠁⠄⣀⣀⠀⢀⣀⣀⣀⡠⠂⢃⡀⠔⠱⡞⢁⠄⣁⠔⠁⠀
⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀""")

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def Scrap():
    try:
        kukis = open('DATA/cookie.json','r').read()
        token = open('DATA/token.json','r').read()
    except (FileNotFoundError,IOError):
        clear();print('Cookie not found');time.sleep(3);Login()
    try:
        link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':kukis}).json()
        lol,lel,tit = link['name'],link['id'],link['birthday']
    except requests.exceptions.ConnectionError:exit('Not internet connection')
    print(f'{FY}Your information login account{FD}\nName     : {lol}\nUser ID  : {lel}\nBirthday : {tit}')

class Login:
    def __init__(self):
        self.rs = requests.Session()
        self.susu_ganyu()
    def susu_ganyu(self):
        try:clear();Banner();os.mkdir('DATA')
        except:pass
        print(f'{FY}\nif you want your main account to stay safe\nused this tool from second or dummy account\n{FD}')
        cookie = input(f' {FR}•{FD} Input cookie : {FG}')
        url    = "https://business.facebook.com/business_locations"
        head   = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
        cok    = {'cookie':cookie}
        try:
            data  = self.rs.get(url,headers=head,cookies=cok)
            token = re.search('(EAAG\w+)',data.text).group(1)
            open('DATA/cookie.json','w').write(cookie)
            open('DATA/token.json','w').write(token)
            print(f'\n{FD}Login {FG}success{FD}, run program again');time.sleep(3);exit()
            print()
        except Exception as e:
            print(f'{FR}Cookie invalid, try again with cookie from other account{FD}');time.sleep(3);Login()

class Menu:
    def __init__(self):
        self.susu_akeno()
    def susu_akeno(self):
        clear();Banner();Scrap()
        print('')
        print(f'{FR}• {FB}01 {FD}Auto Comment')
        print(f'{FR}• {FB}02 {FD}Auto Share')
        print(f'{FR}• {FB}03 {FD}Profile Guard')
        print(f'{FR}• {FB}00 {FD}Change cookies')
        pilih = input(f"{FR}• {FD}Choose : ")
        if pilih in [""]:print(f'{FR}\nWrong choice!{FD}');time.sleep(3);Menu()
        elif pilih in ["1","01"]:print(f"{FR}• unavailable{FD}")#susu_keqing()
        elif pilih in ["2","02"]:Share()
        elif pilih in ["3","03"]:Guard()
        elif pilih in ["0","00"]:os.system('rm DATA/cookie.json && rm DATA/token.json');print(f"Login information has been deleted, please login again.");time.sleep(5);exit()
        else:print(f'{FR}\nWrong choice!{FD}');time.sleep(3);Menu()

class Share:
    def __init__(self):
        self.rs = requests.Session()
        try:
            self.token = open("DATA/token.json","r").read()
            self.cok = open("DATA/cookie.json","r").read()
            self.cookie = {"cookie":self.cok}     
        except:
            print(f'{FR} • {FD}Cookie invalid')
            time.sleep(5);Login()
        self.susu_kagura()
    def susu_kagura(self):
        print(f'{FY}\nCopy & Paste here the link from your post want to share')
        link = input(f'{FR}•{FD} Link : {FG}')
        many = int(input(f'{FR}•{FD} How many wanna share? : {FG}'))
        print(f'{FY}The program is running, please wait{FD}\n')
        try:
            count = 0
            header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"}
            for x in range(many):
                count+=1
                post = self.rs.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={self.token}",headers=header, cookies=self.cookie).text
                data = json.loads(post)
                if "id" in post:
                    sys.stdout.write(f'\rin processing{FRAN} {count}{FD}')
                    sys.stdout.flush()
            print(f'\n\n{FD}Done {FB}{count} {FD}share!');os.system('exit')
        except requests.exceptions.ConnectionError:
            print(f'\n {FG}• {FR}Check ur connection{FD}\n!')

class Guard:
    def __init__(self):
        self.rs = requests.Session()
        self.cookie = {'cookie':open('DATA/cookie.json','r').read()}
        self.token  = open('DATA/token.json','r').read()
        self.susu_marin()
    def susu_marin(self):
        print('')
        print(f'{FR}• {FB}01 {FD}Enable Profile Guard')
        print(f'{FR}• {FB}02 {FD}Disabled Profile Guard')
        pilih = input(f"{FR}• {FD}Choose : ")
        print('')
        if pilih in ['1','01']:
            self.scrap1(True)
        else:
            self.scrap1(False)
    def get_id(self):
        id = self.rs.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie).json()['id']
        return(id)
    def scrap1(self,stat):
        id   = self.get_id()
        var  = {
            '0': {
                'is_shielded'        : stat,
                'session_id'         : '9b78191c-84fd-4ab6-b0aa-19b39f04a6bc',
                'actor_id'           : str(id),
                'client_mutation_id' : 'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
        data = {
            'variables'                : json.dumps(var),
            'method'                   : 'post',
            'doc_id'                   : '1477043292367183',
            'query_name'               : 'IsShieldedSetMutation',
            'strip_defaults'           : 'true',
            'strip_nulls'              : 'true',
            'locale'                   : 'en_US',
            'client_country_code'      : 'US',
            'fb_api_req_friendly_name' : 'IsShieldedSetMutation',
            'fb_api_caller_class'      : 'IsShieldedSetMutation'}
        head = {
            'Content-Type'  : 'application/x-www-form-urlencoded',
            'Authorization' : f'OAuth {self.token}'}
        url  = 'https://graph.facebook.com/graphql'
        req  = self.rs.post(url, data=data, headers=head, cookies=self.cookie)
        if '"is_shielded":true' in req.text:
            print(f'{FR}• {FD}Profile Guard {FG}Active{FD}')
        elif '"is_shielded":false' in req.text:
            print(f'{FR}• {FD}Profile Guard {FG}Disabled{FD}')
        else:
            print(f'{FR}• Error{FD}')

Menu()