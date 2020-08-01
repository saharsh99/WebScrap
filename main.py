import requests
import bs4

url = input("Enter URL ")

response = requests.get(url)

filename = "temp.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()

with open(filename,"w+") as f:
    f.write(formatted_text)


list_imgs = bs.find_all('img')
#print(list_imgs)

no_of_imgs = len(list_imgs)

list_as = bs.find_all('a')

no_of_as = len(list_as)

print("number of img tags",no_of_imgs)
print("number of anchor tags",no_of_as)
