from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Decision_Tree_classifier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_new.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        
        #Gender Parameter
        gender = request.form['gender']
        if gender == 'Male':
            gender = 0
        elif gender == 'Female':
            gender = 1
        
        #Age Parameter
        age = int(request.form['age'])
        
        #Hypertension parameter:
        hypertension=(request.form['hypertension'])
        if hypertension == 'Yes':
            hypertension = 1
        elif hypertension == 'No':
            Hypertension = 0
        
        #Heart_Disease Parameter
        heart_disease=(request.form['heart_disease'])
        if heart_disease == 'Yes':
            heart_disease = 1
        elif heart_disease == 'No':
            heart_disease = 0
        
        #Ever_Married Parameter
        ever_married=request.form['ever_married']
        if(ever_married == 'Yes'):
            ever_married = 0
        elif(ever_married == 'No'):
            ever_married = 1
        
        #Work type parameter
        work_type=request.form['work_type']
        if(work_type =='Private'):
            work_type=0
        elif work_type == 'Self-employed':
            work_type=1
        elif work_type == 'children':
            work_type = 2
        elif work_type == 'Govt_job':
            work_type = 3
        elif work_type == 'Never_worked':
            work_type = 4
        
        #Residence Type Parameter
        Residence_type=request.form['Residence_type']
        if(Residence_type == 'Urban'):
            Residence_type = 0
        elif(Residence_type == 'Rural'):
            Residence_type = 1
            
         #Average glucose level Parameter
        avg_glucose_level = float(request.form['avg_glucose_level'])
        
        #Smoking Status parameter
        smoking_status=request.form['smoking_status']
        if(smoking_status=='never smoked'):
            smoking_status=0
        elif(smoking_status=='formerly smoked'):
            smoking_status=1
        elif(smoking_status=='smokes'):
            smoking_status=2
        elif (smoking_status=='Unknown'):
            smoking_status= 3

        prediction=model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, smoking_status]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index_new.html',prediction_texts="Congratulations! You don't have the risk of getting a stroke.")
        else:
            return render_template('index_new.html',prediction_text="I'm sorry, you have high risk of getting a stroke. Please modify your lifestyle asap and visit for annual doctor check up. All the best!".format(output))
    else:
        return render_template('index_new.html')

if __name__=="__main__":
    app.run(debug=True)
