from bs4 import BeautifulSoup
import requests
from lxml import html
from time import sleep
# insert username and password @#1
# insert bot api thing @2
# insert chat id @3


def login():
    session = requests.session()
    url = "https://qis.hs-albsig.de/qisserver/rds?state=user&type=0"
    session.get(url)
    url = "https://qis.hs-albsig.de/qisserver/rds?state=user&type=1&category=auth.login&startpage=portal.vm"
    payload = {"asdf": "USERNAME", "submit": "Ok", "fdsa": "PASSWORD"} #1
    session.post(url, params=payload)
    return session


def getGrades(session):
    url = "https://qis.hs-albsig.de/qisserver/rds?state=change&type=1&moduleParameter=studyPOSMenu&nextdir="
    url += "change&next"
    url += "=menu.vm&subdir=applications&xml=menu&purge=y&navigationPosition=functions%2CstudyPOSMenu&breadcrumb=study"
    url += "POSMenu&topitem=functions&subitem=studyPOSMenu"
    res = session.get(url)
    bs = BeautifulSoup(res.content, features='lxml')
    p = bs.find('a', text="Notenspiegel")
    p = str(p)
    for i in p.split(" "):
        if "href" in i:
            for j in i.split('"'):
                if "https" in j:
                    url1 = j
    session.get(url1)
    for i in url1.split("&"):
        if "asi" in i:
            for j in i.split(";"):
                if "asi" in j:
                    asi = j
    url2 = "https://qis.hs-albsig.de/qisserver/rds?state=notenspiegelStudent&nex"
    url2 += "t=list.vm&nextdir=qispos/notenspiegel/student&createInfos=Y&struct=auswahlBaum&nodeID=auswahlBaum%7"
    url2 += "Cabschluss%3Aabschl%3D84%2Cstgnr%3D1&expand=0&"
    url2 += asi
    response = session.get(url2)
    session.close()
    return response


def makeGradesFile(response):
    c = 0
    file = open("grades.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("grades.txt", "a+")
    soup = BeautifulSoup(response.content, features='lxml')
    items = soup.findAll('table', border='0')
    courses = items[5].findAll('tr')
    for i in courses:
        if "vorhanden" not in i.text:
            names = i.findAll('b')
            if (len(names) > 3) and ((names[1].text + names[3].text + "\n") not in lines):
                c += 1
                stri = names[1].text + names[3].text
                file.write(stri)
                file.write("\n")
                lines.append(names[1].text + names[3].text + "\n")
                sendMessage(names[1].text + ": " + names[3].text)
    file.close()


def sendMessage(nachricht):
    se = requests.session()
    url = "https://api.telegram.org/YOUR bot token goes here" #2
    url += "sendMessage?chat_id=INSERT your messageID &text=" + nachricht #3
    se.get(url)
    se.close()


while(True):
    s = login()
    res = getGrades(s)
    makeGradesFile(res)
    sleep(3600) # U might want to adjust this waiting time depending on your needs
