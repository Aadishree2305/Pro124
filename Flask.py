from flask import Flask,jsonify,request

app=Flask(__name__)

task=[
    {
        'id':1,
        'title':u'Buy Grocery',
        'discription':u'Milk,Pizza,Cheese,Fruits,Tylio1',
        'done':False
    },
    {
        'id':2,
        'title':u'Learn Python',
        'description':u'You Need to find a good tutorial on Website',
        'done':False
    },
]


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data",
        },4000)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('desciption',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task add successfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)