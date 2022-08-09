

# import numpy as np
# from flask import Flask, request, jsonify, render_template
# from sklearn.preprocessing import StandardScaler
# import pickle
# import pandas as pd

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     return render_template('index.html')

# @app.route("/predict_page", methods=['GET', 'POST'])
# def predict_page():
#     return render_template('main.html')

# @app.route('/predict',methods=['GET', 'POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     item = [x for x in request.form.values()]
#     thalassemia = request.form.get("thalassemia")
#     cp = request.form.get("cp")
#     c3p = request.form.get("c3p")
#     oldpeak = request.form.get("oldpeak")
#     restecg = request.form.get("restecg")
#     fbs = request.form.get("fbs")
#     sex = request.form.get("sex")
#     data = [thalassemia,cp,c3p,oldpeak,restecg,fbs,sex]

#     scaler2 = StandardScaler()
#     ##CHANGE THE INPUT TO NUMPY ARRAY
#     input_data_as_numpy_array = np.asarray(data)
#     #RESHAPE THE NUMPY ARRAY BECAUSE WE NEED TO PREDICT THE TARGET
#     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#     std_data = scaler2.fit_transform(input_data_reshaped)
#     prediction = model.predict(input_data_reshaped)
#     if prediction[0] == 0:
#         return render_template('main.html', prediction_text='The patient does not have Heart Disease' )
#     else:
#         return render_template('main.html', prediction_text='The patient has Heart Disease' )

        


    

# if __name__ == "__main__":
#     app.run(debug=True)


from attr import dataclass
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/login_page", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/predict_page", methods=['GET', 'POST'])
def predict_page():
    return render_template('main.html')

@app.route("/graph_page", methods=['GET', 'POST'])
def graph_page():
    return render_template('graph.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age = request.form.get("age")
    sex = request.form.get("sex")
    cp = request.form.get("cp")
    trestbps = request.form.get("trestbps")
    chol = request.form.get("chol")
    fbs = request.form.get("fbs")
    restecg = request.form.get("restecg")
    thalach = request.form.get("thalach")
    oldpeak = request.form.get("oldpeak")
    exang = request.form.get("exang")
    slope = request.form.get("slope")
    ca = request.form.get("ca")
    thal = request.form.get("thal")
    data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

    scaler2 = StandardScaler()
    ##CHANGE THE INPUT TO NUMPY ARRAY
    input_data_as_numpy_array = np.asarray(data)
    #RESHAPE THE NUMPY ARRAY BECAUSE WE NEED TO PREDICT THE TARGET
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    std_data = scaler2.fit_transform(input_data_reshaped)
    prediction = model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return render_template('main.html', prediction_text='The patient does not have Heart Disease' )
    else:
        return render_template('main.html', prediction_text='The patient has Heart Disease' )




        


    

if __name__ == "__main__":
    app.run(debug=True)