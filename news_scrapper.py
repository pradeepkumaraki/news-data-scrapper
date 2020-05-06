import requests
import json
from datetime import date, timedelta
no_of_days = 15
start_date = str(date.today() - timedelta(days=no_of_days))
API_KEY = "API KEY"
#print(type(start_date))
def get_news_for_query(query="ysrcp",start_date = start_date):
	url="https://newsapi.org/v2/everything?q="+query+"&from="+start_date+"&sortBy=publishedAt&apiKey="+API_KEY
	response = requests.get(url)
	json_file = open("newsapi_data/"+query+".json","w")
	json_file.write(json.dumps(response.json()))
	json_file.close()
	return response.json()


def get_headlines(country="in",category="politics"):
	url="https://newsapi.org/v2/top-headlines?country="+country+"&category="+category+"&apiKey="+API_KEY
	response = requests.get(url)
	json_file = open("newsapi_data/"+"headlines.json","w")
	json_file.write(json.dumps(response.json()))
	json_file.close()
	return response.json()

def get_news_from_domain(domain = "cnn.com"):
	url = "https://newsapi.org/v2/everything?domains="+domain+"&apiKey="+API_KEY
	response = requests.get(url)
	json_file = open("newsapi_data/"+domain.split(".")[0]+".json","w")
	json_file.write(json.dumps(response.json()))
	json_file.close()
	return response.json()

#get_news_for_query()
#get_headlines()
#get_news_from_domain()
