from flask import Flask, render_template, request
from etudiant import Etudiant


app = Flask(__name__)


list_etudiants = [
            Etudiant("Olivier",22), 
            Etudiant("Mathis",22), 
            Etudiant("Quentin",24)
            ]

@app.route('/', methods=["POST"])

def index():

    name = request.form["name"]
    age = request.form["age"]

    etudiant = Etudiant(name,age)
    list_etudiants.append(etudiant)

    etuds_dicts = [etudiant.to_dict() for etudiant in list_etudiants]

    return render_template('index.html', etuds_dicts=etuds_dicts)





if __name__ == '__main__':
    app.run(debug=True)
