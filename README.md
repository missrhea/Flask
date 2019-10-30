# Flask

This is a repository for Flask applications.

The virtual environment corresponds to the directory: flask_env
The command to activate the virtual environment: source flask_env/bin/activate

In each project directory, run the following command to start the Flask API,
python app.py
By default, flask will run on port 5000. Navigate to URL http://localhost:5000 on the browser.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
./hello-world
A simple hello world flask application. https://www.geeksforgeeks.org/flask-creating-first-simple-application/
--------------------------------------------------------------------------
--------------------------------------------------------------------------
./ML-App
Created a simple Linear Regression Model, using this dataset from Kaggle,
https://www.kaggle.com/andonians/random-linear-regression
The web app uses the form functionality from to take an input. The output is predicted with the pre-trained Linear Regression Model.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
./gender-classification-app
A web form interface to accept a name as input, and output the predicted gender using the pre-trained model. 
The model was trained on a dataset (names_dataset.csv in the ./gender-classification-app/models directory) of (name, sex) tuples. 
