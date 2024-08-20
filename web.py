import os
from LINK.link import lke
from MAL.maile import maill
from CAPG.scapig import sca



class AsepYusup:
    
    def menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("1. mencari link web")
        print("2. scraping")
        print("3. mencari email web")
        men = input("\nmaukan pilihan : ")
        if men == "1":
            lke().mencarilink()
        elif men == "2":
            sca().scraping()
        elif men == "3":
            maill().mencarudata()
        else:
            print("yang bener")
        
            
        
        
        
AsepYusup().menu()
        