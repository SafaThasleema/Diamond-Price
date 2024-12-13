from flask import Flask,render_template,request
import pickle
import numpy as np


# 1.created object for class Flask
app=Flask(__name__)

# loading model--model should contain only numbers
with open("diamond.pkl","rb")as f:
    random_regressor=pickle.load(f)

#7.
def predict_price(carat=1.50,cut=2,color=5,clarity=3,depth=62.9,table=54.0,x=5.56,y=8.25,z=3.43):
    temp_array = list()
        
    temp_array=temp_array+[carat]
    temp_array=temp_array+[cut]
    temp_array=temp_array+[color]
    temp_array=temp_array+[clarity]
    temp_array=temp_array+[depth]
    temp_array=temp_array+[table]
    temp_array=temp_array+[x]
    temp_array=temp_array+[y]
    temp_array=temp_array+[z]

    #converting into numpy array
    temp_array= np.array([temp_array])
    print(temp_array)

    #prediction
    return int(random_regressor.predict(temp_array))



# 3.creating router
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html') 

# 4.
@app.route("/predict",methods=['POST','GET'])
#5. we have to check wheter form.get is string or number
def predict():
    if request.method=='POST':
        carat=float(request.form.get('carat'))
        cut=int(request.form.get('cut'))
        color=str(request.form.get('color'))
        clarity=int(request.form.get('clarity'))
        depth=float(request.form.get('depth'))
        table=float(request.form.get('table'))
        x=float(request.form.get('x'))
        y=float(request.form.get('y'))
        z=float(request.form.get('z'))
        
        price=final_price=predict_price(carat=1.50,cut=2,color=5,clarity=3,depth=62.9,table=54.0,x=5.56,y=8.25,z=3.43)
        print(price)
        return render_template('result.html',prediction=price)


    return render_template('predict.html') 

@app.route("/contact")
def contact():
    return render_template('contact.html') 










#2. to create main function
if __name__=='__main__':
    # running server
    app.run(debug=True)

