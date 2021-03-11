from nsetools import  Nse 
from flask import Flask 
from fuzzywuzzy import process


nse = Nse()
app = Flask(__name__)

@app.route('/')
def root():
	return "working"

@app.route('/getlasttradedprice/<id>')
def getLastTradedPrice(id):
	return str(nse.get_quote(id)['lastPrice']);


@app.route('/getmatchingcompanies/<pattern>')
def getMatcingCompanies(pattern):
	get_all_stocks = nse.get_stock_codes()
	get_all_stocks = {v : k for k,v in get_all_stocks.items()}
	temp = get_all_stocks.keys();
	ratio = process.extract(pattern,temp,limit=10)
	return ";".join([i[0] for i in ratio])


if __name__ == '__main__':
	app.run()


