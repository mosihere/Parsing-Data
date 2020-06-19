# A little program to read car data from Bama.ir and save them in a file.
 
# import Requests and Beautiful soap module
import requests
from bs4 import BeautifulSoup 

def getInfoFromBama(productUrl):
    import re
    response = requests.get(productUrl)

    soup = BeautifulSoup(response.text, 'html.parser')

    data = soup('a', attrs={'itemtype':'http://schema.org/Car'})
    # data = soup.select('#adlist > ul > li:nth-child(3) > a')
    f = open('carData.txt', 'w+')
    for carData in data:
        f.write(re.sub(r'\s+', ' ',carData.text))
        f.write('\n')
        f.write('\n')

getInfoFromBama('https://bama.ir/car/all-brands/all-models/all-trims?price=100-130')  # You can change the price here(change the numbers)
# Tip --> we also can use selector method of bs4 to select css by right click on element in web pages and "copy css"