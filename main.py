from flask import Flask,url_for,request,render_template,redirect
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "<h1>HI THIS IS G.V.MADHURANGAN<h1>"

if __name__=="__main__":
    app.run()