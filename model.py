import httplib2
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer

def predict():
        http = httplib2.Http()
        status, response = http.request('https://summerofcode.withgoogle.com/archive/2018/organizations/')

        a=[]
        b=[]
        x = 0
        for link in BeautifulSoup(response,'html.parser', parse_only=SoupStrainer('a')):
                if link.has_attr('href'):
                        a.append(link['href'])
                        if x >=3 and x<= 214:
                                                                #             print(((a[x]).split('/'))[4])
                                b.append(((a[x]).split('/'))[4])
                        x = x+1
                                                                #         print (link['href'])
                print(len(b))

                x = int(input('Enter your organization number '))
                i = 0 
                c=[]
                for i in range(len(b)):
                        if(x == int(b[i])):
                                URL = "https://summerofcode.withgoogle.com/archive/2018/organizations/" + str(x)+"/"
                                r = requests.get(URL) 
                                soup = BeautifulSoup(r.text, 'html5lib') 
                                
                                nameOfOrganization = soup.find('h3',class_= "banner__title")
                                nameOfOrganization = nameOfOrganization.text
                                nameOfOrganization  = re.sub("\s+",' ', nameOfOrganization)
                                c.append(nameOfOrganization)
                                
                                linkOfOrganization = soup.find('a',class_= "org__link")
                                linkOfOrganization = linkOfOrganization.text
                                linkOfOrganization = re.sub("\s+",' ',linkOfOrganization)
                                c.append(linkOfOrganization)

                                descOfOrganization = soup.find('h4',class_= "org__tagline")
                                descOfOrganization = descOfOrganization.text
                                descOfOrganization = re.sub("\s+",' ',descOfOrganization)
                                c.append(descOfOrganization)

                                techOfOrganization = soup.find('ul',class_= "org__tag-container")
                                techOfOrganization = techOfOrganization.text
                                techOfOrganization = re.sub("\s+",',',techOfOrganization)
                                c.append(techOfOrganization)

        print(c)
        return c