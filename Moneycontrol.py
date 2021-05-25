from bs4 import BeautifulSoup as soup
import requests,csv,os
os.chdir("D:/scraping projects/project1/")

class MoneyControl():

    def __init__(self,file):
        self.file = file
    def csv_upload(self,data):
        write = csv.writer(self.file)
        write.writerow(data)

    def scrap(self):
        url = "https://www.moneycontrol.com/markets/indian-indices/"
        res = requests.get(url)
        bs = soup(res.content, 'html.parser')
        t_body = bs.find('tbody')
        t_row = t_body.find_all('tr')
        for i in t_row:
            col = i.find_all('td')
            col = [x.text.strip() for x in col]
            for j in range(1, 8):
                col[j] = float(col[j].replace(',', ''))
            self.csv_upload(col)
        self.file.close()

heading = ["Company", "LTP", "%CHANGE", "VOLUME", "BUY PRICE", "SELL PRICE", "BUY QTY", "SELL QTY"]
F = open("Moneycontrol.csv",'w')
write = csv.writer(F)
write.writerow(heading)
F.close()

F =  open("Moneycontrol.csv",'a',newline="")
Money = MoneyControl(F)
Money.scrap()
F.close()