import re,requests


class maill:
    
    def mencarudata(self):
        link = input("Masukkan Link : ")
        data = requests.get(link).text
        mm = re.findall(r'[\w\.-]+@[\w\.-]+', data)
        for mm in mm:
            print(mm)