import requests,re

class lke:
    
    def mencarilink(self):
        url = input("Masukkan Link : ")
        html = requests.get(url).text
        links = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', html)
        for link in links:
            print(link)