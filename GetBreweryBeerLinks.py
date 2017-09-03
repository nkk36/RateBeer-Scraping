"""
FUNCTION DESCRIPTION

Inputs: 
Outputs: 
"""

def GetBreweryBeerLinks(links,j):
    
    #Import packages
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re

    #Get url and scrape data
    url = links["link"][j]
    page = requests.get(url, verify = False)
    soup = BeautifulSoup(page.text, "lxml")
    
    #Get number of breweries
    numRegex = re.compile(r"\d{1,4}")
    numactive = int(numRegex.search(soup.find_all("a", href = "#active")[0].text).group())
    
    #Get links to each brewery                                              
    BreweryLinks = soup.find_all("a", href = True)
    linkRegex = re.compile(r"/brewers/([\D])+(/)([0-9])+")
    
    links = []
    for link in BreweryLinks:
        if linkRegex.search(str(link)) is not None:
            links.append(linkRegex.search(str(link)).group())
        else:
            pass
    
    #Get true links
    tlinks = []
    for i in range(0,numactive,1):
        tlinks.append("https://www.ratebeer.com" + links[i] + "/")
    
    tlinks = pd.DataFrame(tlinks, columns = ["link"])
    return(tlinks)
        