import requests
from bs4 import BeautifulSoup


url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
user = 'admin'
password = '123456aA'

def func1():
    payload = {'log':user,'pwd':password}
    with requests.session() as session:
        re = session.post(url,payload)
        soup = BeautifulSoup(re.content,"html.parser")
        a = soup.find("span",class_="display-name").text
        print("user name:",a)

if __name__ == '__main__':
    func1()
