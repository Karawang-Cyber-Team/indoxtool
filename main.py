#!/usr/bin/python
# importing socket library
import socket, psutil
import os, time, sys, random, string, collections, shutil, argparse, subprocess, requests, re
import hashlib
import rich
import requests as rq
import json
from pytube import YouTube
from bs4 import BeautifulSoup
from pynotifier import Notification
from calendar import isleap
from gtts import gTTS
os.system('clear');(0.003)

# COLOR
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
IP = requests.get('https://api.ipify.org').text
def indo():
  print(f"""{M}
╔══╦═╦╦══╦═╦═╦╦═╦══╦══╦══╗╔╗╔╗╔══╦═╦═╦╗
╚║║╣║║╠╗╗║║║║║║╦╣══╬║║╣╔╗║╚╗╔╝╚╗╔╣║║║║║
{P}╔║║╣║║╠╩╝║║║║║║╩╬══╠║║╣╠╣║╔╝╚╗─║║║║║║║╚╗
╚══╩╩═╩══╩═╩╩═╩═╩══╩══╩╝╚╝╚╝╚╝─╚╝╚═╩═╩═╝
{P}[{M}•{P}]---------------------------------------------------{P}[{M}•{P}]
{P}[{M}•{P}] Author    : {M}TrueFalse                             {P}[{M}•{P}]
{P}[{M}•{P}] Github    : {M}github.com/TrueFalseID                {P}[{M}•{P}]
{P}[{M}•{P}] FB        : {M}True False                            {P}[{M}•{P}]
{P}[{M}•{P}] Team      : {M}Karawang Cyber Team                   {P}[{M}•{P}]
{P}[{M}•{P}] Your IP   : {M}{IP}                         {P}[{M}•{P}]
{P}[{M}•{P}]---------------------------------------------------{P}[{M}•{P}]
  """)
# MENU
def main():
  indo()
  print(f'{P}[{M}01{P}] {P}Ip Addres Tracker    (Your-IP)');(0.03)
  print(f'{P}[{M}02{P}] {P}Ip Addres Checker    (Lacak-IP)');(0.03)
  print(f'{P}[{M}03{P}] {P}Yt video information (Coming Soon)');(0.03)
  print(f'{P}[{M}04{P}] {P}Yt video downloader  (Py-Api)');(0.03)
  print(f'{P}[{M}05{P}] {P}Json To Csv          (Coming Soon)');(0.03)
  print(f'{P}[{M}06{P}] {P}Password Generator   (Random Pass)');(0.03)
  print(f'{P}[{M}07{P}] {P}Search String in files');(0.03)
  print(f'{P}[{M}08{P}] {P}Fetch link from webpage');(0.03)
  print(f'{P}[{M}09{P}] {P}Batery Notification');(0.03)
  print(f'{P}[{M}10{P}] {P}Calculate Age');(0.03)
  print(f'{P}[{M}11{P}] {P}Text file analysis');(0.03)
  print(f'{P}[{M}12{P}] {P}Hostname IPaddres');(0.03)
  print(f'{P}[{M}13{P}] {P}Get wifi password    (windows)');(0.03)
  print(f'{P}[{M}14{P}] {P}Create password hash');(0.03)
  print(f'{P}[{M}15{P}] {P}Text To Spech');(0.03)
  print(f'{P}[{M}16{P}] {P}Convert cookie To token (FB)');(0.03)
  print(f'{P}[{M}rm{P}] {P}Exit\n');(0.03)
  kasep = input(f'{P}[{M}><{P}] CHOICE : ')
  if kasep == '':
    print(f'\n{M}Your Input Invalid!');time.sleep(3);os.system('clear');main()
  if kasep == '01':
    track()
  if kasep == '02':
    checker()
  if kasep == '03':
    print(f'\n{M}Coming Soon bro!!!');time.sleep(3);os.system('clear');exit()
  if kasep == '04':
    ytdwnd()
  if kasep == '05':
    print(f'\n{M}Coming Soon bro!!!');time.sleep(3);os.system('clear');exit()
  if kasep == '06':
    gnrt()
  if kasep == '07':
    file()
  if kasep == '08':
    webpage()
  if kasep == '09':
    nft()
  if kasep == '10':
    age()
  if kasep == '11':
    anyl()
  if kasep == '12':
    ip()
  if kasep == '13':
    wfi()
  if kasep == '14':
    enx()
  if kasep == '15':
    spech()
  if kasep == '16':
    get()
  if kasep == 'rm':
    print(f'\n{M}Thanxs Using My tools bro!');time.sleep(1);exit()
    
def track():
  os.system('clear')
  indo()
  iprequest = requests.get(f"http://ip-api.com/json")
  if iprequest.status_code == 200:
    ipdata = json.loads(iprequest.text)
    if ipdata["status"] == "success":
      for key in ipdata:
        print(f"{key.capitalize()} : {ipdata[key]}")
        if key == "lon":
          lat = ipdata["lat"]
          lon = ipdata["lon"]
          maps = (f"https://www.google.com/maps/@{lat},{lon},9z")
          print(f"Maps : {maps}")
          
def checker():
  os.system('clear')
  indo()
  ipaddres = input(f'{P} Input Check IP :')
  iprequest = requests.get(f"http://ip-api.com/json/{ipaddres}")
  if iprequest.status_code == 200:
    ipdata = json.loads(iprequest.text)
    if ipdata["status"] == "success":
      for key in ipdata:
        print(f"{key.capitalize()} : {ipdata[key]}")
        if key == "lon":
          lat = ipdata["lat"]
          lon = ipdata["lon"]
          maps = (f"https://www.google.com/maps/@{lat},{lon},9z")
          print(f"Maps : {maps}")

def ytdwnd():
  os.system('clear')
  indo()
  url = input(f"{P}Enter YouTube video url: ")
  # Example url: https://www.youtube.com/watch?v=x2sjEj8TClM&t=
  yt = YouTube(url)
  video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
  try:
      video.first().download()
      print("Download complete for: ", yt.title)
  except Exception as e:
      print("Download failed due to: ", e)

#def csv():
 # os.system('clear');os.system('pip install json')
#  indo()  try:
   # with open('input.json', 'r') as f:
   #   data = json.loads(f.read())
  #   output = ','.join([*data[0]])
     # for obj in data:
   #     output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
    #    with open('output.csv', 'w') as f:
         # f.write(output)
        #except Exception as ex:
            #print(f'Error: {str(ex)}')

def gnrt():
  time.sleep(3);os.system('clear')
  indo()
  lower = 'abcdefghijklmnovqrstuvwxyz'
  upper = 'ABCDEFGHIJKLMNOVQRSTUVWXYZ'
  number = '0123456789'
  symbol = '@$#?!:()<>{}[{&_%~\|`'
  string = lower + upper + number + symbol
  length = 15 
  password = "".join(random.sample(string,length))
  print(f'{P}YOUR PASSWORD NEW IS : {H}{password}{P}')

def file():
  os.system('clear');indo()
  text = input("input text : ")
  path = input("path       : ") 
  # os.chdir(path)
  def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    # print(files)
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, "r")
            if text in f.read():
                f = 1
                print(text + " found in ")
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True
                if f == 1:
                  print(text + " not found! ")
                  return False
                  getfiles(path)

def webpage():
  os.system('clear');indo()
  url = input("Enter Link: ")
  if ("https" or "http") in url:
    data = rq.get(url)
  else:
    data = rq.get("https://" + url)
    soup = BeautifulSoup(data.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
      links.append(link.get("href"))
      # Writing the output to a file (myLinks.txt) instead of to stdout
      # You can change 'a' to 'w' to overwrite the file each time
      with open("myLinks.txt", 'a') as saved:
        print(links[:10], file=saved)

def nft():
  os.system('clear');indo()
  battery = psutil.sensors_battery()
  plugged = battery.power_plugged
  percent = battery.percent
  if percent <= 30 and plugged!=True:
    Notification(
      title="Battery Low",
      description=str(percent) + "% Battery remain!!",
      duration=5,
      ).send()

def age():
  # judge the leap year
  def judge_leap_year(year):
      if isleap(year):
          return True
      else:
          return False
  
  
  # returns the number of days in each month
  def month_days(month, leap_year):
      if month in [1, 3, 5, 7, 8, 10, 12]:
          return 31
      elif month in [4, 6, 9, 11]:
          return 30
      elif month == 2 and leap_year:
          return 29
      elif month == 2 and (not leap_year):
          return 28
  os.system('clear');indo()
  name = input("input your name: ")
  age = input("input your age: \n")
  localtime = time.localtime(time.time())
  
  year = int(age)
  month = year * 12 + localtime.tm_mon
  day = 0
  
  begin_year = int(localtime.tm_year) - year
  end_year = begin_year + year
  
  # calculate the days
  for y in range(begin_year, end_year):
      if (judge_leap_year(y)):
          day = day + 366
      else:
          day = day + 365
  
  leap_year = judge_leap_year(localtime.tm_year)
  for m in range(1, localtime.tm_mon):
      day = day + month_days(m, leap_year)
  
  day = day + localtime.tm_mday
  print("%s's age is %d years or " % (name, year), end="")
  print("%d months or %d days" % (month, day))

def anyl():
  script_name = sys.argv[0]
  
  res = {
      "total_lines":"",
      "total_characters":"",
      "total_words":"",
      "unique_words":"",
      "special_characters":""
  }
  
  try:
      textfile = sys.argv[1]
      with open(textfile, "r", encoding = "utf_8") as f:
  
          data = f.read()
          res["total_lines"] = data.count(os.linesep)
          res["total_characters"] = len(data.replace(" ","")) - res["total_lines"]
          counter = collections.Counter(data.split())
          d = counter.most_common()
          res["total_words"] = sum([i[1] for i in d])
          res["unique_words"] = len([i[0] for i in d])
          special_chars = string.punctuation
          res["special_characters"] = sum(v for k, v in collections.Counter(data).items() if k in special_chars)
  
  except IndexError:
      print('Usage: %s TEXTFILE' % script_name)
  except IOError:
      print('"%s" cannot be opened.' % textfile)
  
  print(res)
  
def ip():
  os.system('clear');indo()
  def get_hostname_IP():
      hostname = input("Please enter website address(URL) :")
      try:
          print (f'\n{P}Hostname: {H}{hostname}')
          print (f'{P}IP: {H}{socket.gethostbyname(hostname)}{P}')
      except socket.gaierror as error:
          print (f'{M}Invalid Hostname, error raised is {error}')
  
  get_hostname_IP()

def wfi():
  data = (
      subprocess.check_output(["netsh", "wlan", "show", "profiles"])
      .decode("utf-8")
      .split("\n")
  )
  profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
  for i in profiles:
      results = (
          subprocess
          .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
          .decode("utf-8")
          .split("\n")
      )
      results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
      try:
          print("{:<30}|  {:<}".format(i, results[0]))
      except IndexError:
          print("{:<30}|  {:<}".format(i, ""))

def enx():
  parser = argparse.ArgumentParser(description='hashing given password')
  parser.add_argument('password', help='input password you want to hash')
  parser.add_argument('-t', '--type', default='sha256',choices=['sha256', 'sha512', 'md5'] )
  args = parser.parse_args() 
  
  # hashing given password
  password = args.password
  hashtype = args.type
  m = getattr(hashlib,hashtype)()
  m.update(password.encode())
  
  # output
  print("< hash-type : " + hashtype + " >")
  print(m.hexdigest())

def spech():
  os.system('clear');indo()
  spet = input(f'{P}Enter Text To Spech : ')
  speech = gTTS(text=spet, lang='id', slow=False)
  speech.save('voice.mp3')
  print(f'\n{H}Success file saved!{P}')
    
def get():
  os.system('clear');indo()
  print(f'{P}< {M}GET FB ACCESS TOKEN FROM COOKIE {P}>')
  cookie = input(f'\n{P}[{M}^^{P}] Cookie : ')
  try:
      data = requests.get('https://business.facebook.com/business_locations', headers = {
          'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
          'referer'                   : 'https://www.facebook.com/',
          'host'                      : 'business.facebook.com',
          'origin'                    : 'https://business.facebook.com',
          'upgrade-insecure-requests' : '1',
          'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
          'cache-control'             : 'max-age=0',
          'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'content-type'              : 'text/html; charset=utf-8'
      }, cookies = {
          'cookie'                    : cookie # KUEH
      })
      find_token = re.search('(EAAG\w+)', data.text)
      results    = f'\n{M}Fail : maybe your cookie invalid !!' if (find_token is None) else f'\n{P}Your fb access token : {H}' + find_token.group(1)
  except requests.exceptions.ConnectionError:
      results    = f'\n{M}Fail : no connection here !!'
  except:
      results    = f'\n{M}Fail : unknown errors, please try again !!'
  
  print(results)
  
if __name__ == '__main__':
  main()