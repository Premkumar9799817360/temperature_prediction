import numpy as np
from flask import Flask,render_template
import joblib
from flask import request

app = Flask(__name__)
model = joblib.load("tempreture_prediction.pkl")


#copy from streamlit for deployment testing
import streamlit as st

st.session_state['answer'] = ''

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)

@app.route('/')
def prem():
    return render_template('homes.html')

@app.route('/',methods=["POST"])
def home1():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
    data14 = request.form['n']
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14]],dtype= float)
    pred = model.predict(arr)
    # return render_template('homes.html',prediction_text = f"{pred[0]}")
    return render_template('homes.html',prediction_text = "{:.2f}°C".format(pred[0]))
    # "{:.2f}".format(a)

if __name__ == "__main__":
    app.run(debug=True)
