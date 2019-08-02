from flask import Flask, render_template, request
from predict import predict_value
app = Flask(__name__)

@app.route('/')
def show_predictor_form():
    return render_template('predictorform.html')

@app.route('/result', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        input = request.form['input'] 
        prediction = predict_value(input)	
        #classifier = pickle.load(open('../Model/pickled-model', 'rb'))
        #x = pd.read_csv('unseen.csv')
        return render_template('result.html', input=input, prediction=prediction)

if __name__ == '__main__': 
   #app.run(host="0.0.0.0", port=80)
   app.run("localhost", "9999", debug=True)
