from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np 
#ML packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import pickle

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    df= pd.read_csv("models/names_dataset.csv")
    # Features and Labels
    df_X = df.name

    # Vectorization
    #corpus = df_X
    cv = CountVectorizer()
    X = cv.fit_transform(df_X) 

    # Loading our ML Model
    sample_dbfile = open('models/naive_bayes_model.pkl', 'rb')      
    clf = pickle.load(sample_dbfile) 
    # Receives the input query from form
    if request.method == 'POST':
        namequery = request.form['namequery']
        data = [namequery]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('results.html',prediction = my_prediction,name = namequery)



if __name__ =='__main__':
    app.run(debug=True)