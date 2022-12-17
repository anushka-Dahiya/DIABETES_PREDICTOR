from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)


def Predictor(input_list):
    model = pickle.load(open("model.pkl", "rb"))
    y = model.predict(input_list)
    return y[0]


@app.route("/", methods =["GET", "POST"])
def home():
    if request.method=="POST":
        age=request.form.get("age")
        Glucose=request.form.get("Glucose")
        Pregnancies=request.form.get("Pregnancies")
        Insulin=request.form.get("Insulin")
        BloodPressure=request.form.get("BloodPressure")
        # Gender=request.form["gender"]
        BMI=request.form.get("BMI")
        DiabetesPedigreeFunction=request.form.get("DiabetesPedigreeFunction")
        input_list=[[]]
        input_list[0].append(int(Pregnancies))
        input_list[0].append(float(Glucose))
        input_list[0].append(float(BloodPressure))
        input_list[0].append(float(Insulin))
        input_list[0].append(float(BMI))
        input_list[0].append(float(DiabetesPedigreeFunction))
        input_list[0].append(float(age))
        print(input_list)
        predicted=Predictor(input_list)
        return render_template("result.html" , result=int(predicted)) 
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)    
    