from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data-Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs 1,00,000'
    },
    {
        'id':2,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    },
    {
        'id':3,
        'title':'Data-Scientist',
        'location':'Delhi, India',
        'salary':'Rs 2,00,000'
    },
    {
        'id':4,
        'title':'Frontend Engineer',
        'location':'Hyderabad, India',
        'salary':'Rs 1,50,000'
    }
]

@app.route('/')
def hello():
    return render_template('index.html',jobs=JOBS)

@app.route("/api/jobs")
def json():
    return jsonify(JOBS)

app.run(host='0.0.0.0',debug=True)
