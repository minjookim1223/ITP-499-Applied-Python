import requests
from flask import Flask, render_template, request

country_flag = 'https://www.countryflags.io/{}/flat/64.png'
country_url = 'https://restcountries.eu/rest/v2/name/{}'
people = {}

app = Flask(__name__)

@app.route('/personView/<string:fullname>', methods=['GET', 'POST'])
def viewPerson(fullname):
    person = people[fullname]
    
    try:
        countryResponse = requests.get(country_url.format(person['country']))
        countryJsonResponse = countryResponse.json()[0]
        person['result'] = {
            'capital': countryJsonResponse['capital'],
            'country': countryJsonResponse['name'],
            'code': countryJsonResponse['alpha2Code'],
            'continent': countryJsonResponse['region'],
            'pop': countryJsonResponse['population']
        }
        
    except:
        print("Country was not found in sources, defaulting to values")
        person['result'] = {'capital': 'unknown capital', 'country': 'unknown country', 'code': 'US',
                                 'continent': 'unknown continent', 'pop': 0}

    return render_template('viewPerson.html', flag_url=country_flag.format(person['result']['code']), person=person)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form['fname'] + " " + request.form['lname']
        people[name] = {}
        people[name]['fname'] = request.form['fname']
        people[name]['lname'] = request.form['lname']
        people[name]['bday'] = request.form['bday']
        people[name]['country'] = request.form['country']
        return render_template('home.html', names=people)
    else:
        return render_template('home.html', names=people)

@app.route('/addform')
def add_name():
    return render_template('addform.html')


if __name__ == "__main__":
    app.run(debug=True)