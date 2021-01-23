# -- coding: utf-8 --
from urllib import request
import urllib.request
import bs4 as bs
import re
import json, re

webUrl = ""
strinGi = ""
finalarr = []



def saveData():
    save = input("Save the List? Y/N: ").lower()
    if (save == "y"):
        with open('endata.json', 'w', encoding="utf-8", errors="ignore") as f:
            json.dump(finalarr, f,ensure_ascii=False)
            f.write("Testi")
        print("Data Saved")
    print("Thank You")

while (True):
    try:
        webUrl = urllib.request.urlopen("https://www.vocabulary.com/lists/52473").read()
    except:
        print("Could not Open url, please use http:// at the beginning")
        
    soup = bs.BeautifulSoup(webUrl,'html.parser')

    collectedWords = []
    allAs = soup.find_all("a")
    tables = soup.find_all("td")
    myAs = []

    result = soup.find_all("div", {"class":"definition"})
    for e in result:
        myAs.append(e)

    result = soup.find_all("div", {"class":"example"})
    for e in result:
        myAs.append(e)
    
        
    
    #Get tables
    for elem in allAs:
        string = re.sub(r"[\d\t\r\n\(\)\.\?]+|[\d\t\r\n\s\(\)\.]+$","",elem.text)
        stringspace = re.sub(r"[\s]+"," ",string)
        collectedWords.append(stringspace.lower().strip())
        #stringspace = re.sub(r"[\s]+"," ",string)
        
    
    #Get other tags
    for elem in myAs:
                string = re.sub(r"[\d\t\r\n\(\)\.\?]+|[\d\t\r\n\s\(\)\.]+$","",elem.text) 
                stringspace = re.sub(r"[\s]+"," ",string)  
                collectedWords.append(stringspace.lower().strip())

    
    for val in collectedWords:
        if 3<len(val.strip()) < 15:
            finalarr.append(val.lower().strip())
       
    print(finalarr)
    
    break
    reply = input("Wanna add more? Y/N: ").lower()
    if (reply == "n"):
        break

saveData()