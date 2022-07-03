import pickle
import numpy as np
import sklearn
from flask  import Flask,render_template,request
data=sklearn
model = pickle.load(open('BotsonModel.pkl', 'rb'))

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        rm = float(request.form['rm'])
        ptratio = float(request.form['ptratio'])
        lstat = float(request.form['lstat'])        
        data = np.array([[rm,ptratio,lstat]])
        my_prediction = model.predict(data) 
        return render_template('result.html', price=round(my_prediction[0],2))
if __name__ =='__main__':
    app.run(debug=True,port=8000)