import httplib2
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer

def predict(orgno):
        http = httplib2.Http()
        status, response = http.request('https://summerofcode.withgoogle.com/archive/2018/organizations/')
        a = []
        b = []
        x = 0
        
        for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                a.append(link['href'])
                if x >= 3 and x <= 214:
                    b.append(((a[x]).split('/'))[4])
                x = x+1

        x = int(orgno)
        i = 0
        c = {'organization': [], 'link': [],'description': [], 'technology': []}
        for i in range(len(b)):
                if(x == int(b[i])):
                        URL = "https://summerofcode.withgoogle.com/archive/2018/organizations/" + str(x)+"/"
                        r = requests.get(URL)
                        soup = BeautifulSoup(r.text, 'html5lib')

                        nameOfOrganization = soup.find('h3', class_="banner__title")
                        nameOfOrganization = nameOfOrganization.text
                        nameOfOrganization = re.sub("\s+", ' ', nameOfOrganization)
                        c['organization'].append(nameOfOrganization)

                        linkOfOrganization = soup.find('a', class_="org__link")
                        linkOfOrganization = linkOfOrganization.text
                        linkOfOrganization = re.sub("\s+", ' ', linkOfOrganization)
                        c['link'].append(linkOfOrganization)

                        descOfOrganization = soup.find('h4', class_="org__tagline")
                        descOfOrganization = descOfOrganization.text
                        descOfOrganization = re.sub("\s+", ' ', descOfOrganization)
                        c['description'].append(descOfOrganization)

                        techOfOrganization = soup.find('ul', class_="org__tag-container")
                        techOfOrganization = techOfOrganization.text
                        techOfOrganization = re.sub("\s+", ',', techOfOrganization)
                        c['technology'].append(techOfOrganization)

        return c

if __name__ == "__main__":
    print(predict(input("Enter the input: ")))