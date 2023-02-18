import requests

from bs4 import BeautifulSoup as bs
github_user= input('input the Github user name: ')
url='https://github.com/'+github_user
r =requests.get(url)
soup = bs(r.content,'html.parser')
pi = soup.find('img',{'alt':'Avatar'})['src']
print(pi)
