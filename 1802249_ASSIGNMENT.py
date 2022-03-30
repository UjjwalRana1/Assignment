'''flask: to make flask application
   request: to make http requests
   jsonify: to get the json object as an output
   BeautifulSoup: to scrapping the data from http://time.com
   '''
from flask import Flask,request,jsonify
import requests
from bs4 import BeautifulSoup
app=Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route("/getTimeStories",methods=["GET"])
def dosomething():
	import requests
	from bs4 import BeautifulSoup
	#first send http request to get the data from url
	x = requests.get('https://time.com')
	#making data to BeautifulSoup object to get the desire tag
	html = BeautifulSoup(x.text, 'html.parser')
	GetDiv=html.find('div',class_="partial latest-stories")
	links=[]
	title=[]

	for link in GetDiv.find_all('a', href=True):
		links.append("https://time.com"+link['href'])
		title.append(link.h3.text)
	#TOP 5 TITLES
	h1,h2,h3,h4,h5=title[0],title[1],title[2],title[3],title[4]
	#TOP 5 LINKS
	l1,l2,l3,l4,l5=links[0],links[1],links[2],links[3],links[4]
	lis=[{"title":h1,"link":l1},{"title":h2,"link":l2},{"title":h3,"link":l3},{"title":h4,"link":l4},{"title":h5,"link":l5}]
	#RETURNING JSON OBJECT ARRAY AS AN OUTPUT 
	return jsonify(lis)
  
 

if __name__=="__main__":
  #GET THE APP STARTED
  app.run(debug=True)


'''Student ID:1802249
   Name:Ujjwal Rana
   college:CGC Landran
   
   Thank You!!
'''























































#for i in j:
#	print(i.text)
	