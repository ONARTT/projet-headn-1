from flask import Flask, render_template, request, redirect, url_for
import random
from etudiant import Etudiant


app = Flask(__name__)


list_etudiants = [
            Etudiant("Olivier",22), 
            Etudiant("Mathis",22), 
            Etudiant("Quentin",24)
            ]

for i in range (0,3) :
    for p in range (0, 5):
        list_etudiants[i].addNote(random.randint(0,20))


@app.route('/', methods=["GET", "POST"])

def index():

    if request.method == "POST" :
        name = request.form["name"]
        age = request.form["age"]
    

        etudiant = Etudiant(name,age)
        list_etudiants.append(etudiant)

        return redirect(url_for("index"))

    etuds_dicts = [etudiant.to_dict() for etudiant in list_etudiants]

    return render_template('index.html', etuds_dicts=etuds_dicts)




@app.route('/etudiant/<int:etudiant_id>', methods=["GET", "POST"])

def display_etud(etudiant_id):
    
    etudiant = next((etd for etd in list_etudiants if etd.id == etudiant_id), None)
    if etudiant :
      
        return render_template('etudiant.html', etudiant=etudiant.to_dict())
    else :
        "Etudiant non trouvé", 404
    return



@app.route('/etudiant/edit/<int:etudiant_id>', methods=["GET", "POST"])

def edit(etudiant_id):

    etudiant = next((etd for etd in list_etudiants if etd.id == etudiant_id), None)
    if etudiant :
        if request.method == "POST" :
            name = request.form["name"]
            age = request.form["age"]

            etudiant.setName(name)
            etudiant.setAge(age)



            return redirect(url_for("edit", etudiant_id=etudiant_id))
    
    return render_template('edit.html', etudiant=etudiant.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
