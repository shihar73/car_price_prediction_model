from flask import *
import requests
import numpy as np

app = Flask(__name__)
app.secret_key ="helloo"

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    Year = int(request.form['Year'])
    Present_Price=float(request.form['Present_Price'])
    Kms_Driven=int(request.form['Kms_Driven'])
    Kms_Driven2=np.log(Kms_Driven)
    Owner=int(request.form['Owner'])
    Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
    if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=="Diesel"):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
    Year=2020-Year
    Seller_Type_Individual=request.form['Seller_Type_Individual']
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	
    Transmission_Mannual=request.form['Transmission_Mannual']
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0
    
    print("Present_Price",Present_Price,"Kms_Driven2",Kms_Driven2,"Owner",Owner,"Year",Year,"Fuel_Type_Diesel",Fuel_Type_Diesel,"Fuel_Type_Petrol",Fuel_Type_Petrol,"Seller_Type_Individual",Seller_Type_Individual,"Transmission_Mannual",Transmission_Mannual)
    flash("dgdsfgsdf")
    return redirect(url_for("Home"))



if __name__=="__main__":
    app.run(debug=True)
