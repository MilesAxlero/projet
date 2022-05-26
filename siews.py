from flask import Flask, request, render_template
nomen = []
app = Flask(__name__)   

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def index():
    return render_template("wow.html")

@app.route('/ajouter', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        nom = request.form.get("nomm")
        # getting input with name = lname in HTML form 
        num = request.form.get("numm") 
      
        return affich(nom, num)
    return render_template("form.html")

@app.route('/affichage')
def affich(nom, num):
    nom = str(nom)
    if (nom not in nomen):  
        ajout = nom.capitalize() + ":" + num
        with open("repertoire.txt","a") as f:
                f.write(str(ajout))
                f.write("\n")
        nomen.append(nom)
        mssg= "On a bien ajouté le numéro de téléphone: " + num
        return render_template('display.html', num=mssg)
    else: 
        return render_template('nonexistent.html', phs="Le numero est deja existant")

@app.route('/recherch', methods =["GET", "POST"])
def lecture():
    if request.method == "POST":
        demnom = request.form.get("nom2")  

        return rechdisp(demnom)     
    return render_template("rechercher.html")

@app.route('/montrer')
def rechdisp(demnom):
    with open("repertoire.txt","r") as f:
        for ligne in f:
            colonnes = ligne.split(":")
            noms, nums = colonnes[0],colonnes[1]                
            if str(demnom).lower() == noms.lower(): 
                return render_template('resultat.html', numr=nums, nomr=demnom)
        else:
            reponse = f"Le nom {demnom} est inconnu"
            return render_template('nonexistent.html', phs=reponse)




  
if __name__=='__main__':
   app.run()

