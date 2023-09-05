from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/', methods=['POST'])
def get_value():
    pays = request.form['pays']
    province = request.form['province']
    ville = request.form['ville']
    adresse = str(pays) + ' ' + str(province) + ' ' + str(ville)

    if 'saisie1' in request.form:
        adresse = adresse + ' ' + request.form['saisie1']
    if 'saisie2' in request.form:
        adresse = adresse + ' ' + request.form['saisie2']
    if 'saisie3' in request.form:
        adresse = adresse + ' ' + request.form['saisie3']



    
 	
    try:
        geolocator = Nominatim(user_agent='babatundearemu22gmail.com')
        location = geolocator.geocode(str(adresse))
        valide_adresse = location.address
        return render_template('valide_adresse.html',valide_adresse = valide_adresse)
    except:
        return render_template('adresse_not_valide.html')	

if __name__ == '__main__':
    app.run()
