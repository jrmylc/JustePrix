from flask import Flask, render_template, request, response
import requests, json, random

app = Flask(__name__)

randNumb = random.randint(0,9)


url = "https://api.cdiscount.com/OpenApi/json/Search"
params = {
    "ApiKey": "bdd9830a-51f0-4787-959b-faffed2f7ba6",
    "SearchRequest": {
        "Keyword": "TV",
        "SortBy": "relevance",
        "Pagination": {
            "ItemsPerPage": 10,
            "PageNumber": 3
        },
        "Filters": {
            "Price": {
                "Min": 0,
                "Max": 0
            },
            "Navigation": "",
            "IncludeMarketPlace": "false",
            "Condition": None
        }
    }
}


response = requests.post(url, data=json.dumps(params))
print(response.json()['Products'][0]['Name'])
print(response.json()['Products'][0]['BestOffer']['SalePrice'])


@app.route("/", methods="POST")
def main():

    if request.method == 'POST':
        guess = request.form['price']
        print(guess)
        if float(guess) < response['product']['price']:
            result = "C'est plus ! essaye encore"
        elif float(guess) > response['product']['price']:
            result = "C'est moins ! essaye encore"
        elif float(guess) == response['product']['price']:
            result = "Nice"
        return render_template('main.html', result=result, product=response['product'], lastguess=guess)
    else:
        return render_template('main.html', result="", product=response['product'], lastguess="")
