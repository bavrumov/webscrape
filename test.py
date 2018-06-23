# import libraries
from bs4 import BeautifulSoup
import urllib2

# sample page URLs
sample_one = "http://imgsrc.ru/9174337478/58977632.html"
sample_two = "http://imgsrc.ru/cambryd/a1985268.html"
sample_three = "http://imgsrc.ru/9174337478/60088742.html?"

# query the site and store html in 'page'
page = urllib2.urlopen(sample_one)

# parse the html in 'page'
soup = BeautifulSoup(page, 'html.parser')

# locate anchor tag of central image
central_image_anchor = soup.find("a", id="next_url")
print(central_image_anchor.prettify())

# store the image tag
central_image_tag = soup.find("img", class_="big")
#central_image_tag = central_image_anchor.next_element

#print the contents of the src attribute
print(central_image_tag['src'])

if("user" in central_image_anchor['href']):
	print("End of album")

