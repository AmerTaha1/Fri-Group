from flask import Flask,render_template,request
from helpers.dic import *
import joblib

app=Flask(__name__)

model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')


@app.route('/',methods=['Get'])
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    Distance_driven=float(all_data['Distance_driven'])
    transmission=int(all_data['transmission'])
    year=int(all_data['year'])
    mmr=float(all_data["mmr"])
    condition=int(all_data['condition'])
    new_make=make_dic[all_data['new_make']]
    new_model=model_dic[all_data['new_model']]

    data=[year, transmission, condition, mmr,Distance_driven,new_model,new_make]
    pred = model.predict(scaler.transform([data]))

    return render_template('index.html',x=pred)

if __name__=='__main__':
    app.run()