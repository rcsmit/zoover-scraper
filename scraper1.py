# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:23:09 2018

@author: rcxsm
"""

# import libraries
from urllib.request import urlopen #python3
from bs4 import BeautifulSoup
import sys


def parsepagina (url, t):
    if t<3:     #PREVENTING AN ENDLESS LOOP OF EMPTY PAGES (zoover.nl)   
        url3=""  
        page =  urlopen(url) 
        
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser') 
    
        #SCRAPING THE REACTIONS ON THE REVIEWS
        # ENTER HERE THE THING YOU WANT TO SCRAPE
        search1 = soup.find_all('div', attrs={'class':'reaction-2H2OG'})
        if not search1 is None:
            for search2 in search1:
                search3 = search2.text
                print (search3)
                print ('----')
        else:
            print ('NO answers found')
            sys.exit()
        
        #GOING TO THE NEXT PAGE
        #ENTER HERE THE LINK TO THE NEXT PAGE
        link=soup.find('a', attrs={'data-qa':'BasicLink-page-next'})
        if not link is None:
           url3= 'https://www.zoover.nl' + link.get('href')
           print ( '--- ' + str(t)  +  ' ------------------------------------------------------------------------------')
           t=t+1
           parsepagina (url3,t)
        else:
            print ('READY')
            sys.exit()
    else:
        print ('TWENTY REACHED')
        sys.exit()
        
def main():
    #url0 = 'https://www.zoover.nl/italie/lazio-latium/rome/village-fabulous/camping'
    url0='https://www.tripadvisor.nl/Hotel_Review-g187892-d238045-Reviews-Hotel_Villa_Schuler-Taormina_Province_of_Messina_Sicily.html'
    parsepagina (url0, 1)

main()

