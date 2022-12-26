from flask import Flask,render_template;
# import flask as fl;
#from flask import render_template;
app = Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    #return render_template('index.html')
    return render_template('index.html')

# @app.route("/alpesh")
# def products():
#     return 'hey'

# @app.route("/home")
# def home():
#     return "Jay hind"
if __name__=="__main__":
    app.run(debug=True)