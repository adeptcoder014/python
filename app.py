from flask import Flask,render_template,request,url_for,json
import pandas
import plotly.express
from analysis import f

#Creating server
app=Flask(__name__)
# Extracting Data
data=pandas.read_csv("./static/least_affected.csv")
new_y=data["Eggs"]
graph=plotly.express.bar(data,x=data["Country"],y=new_y,  barmode='group')
graphJSON=json.dumps(graph,cls=plotly.utils.PlotlyJSONEncoder)

# nourishment=pandas.read_csv("./static/Nourishment.csv")
# graph1=plotly.express.bar(nourishment,x=nourishment["Nourishment"],y=nourishment["Albania"])
# graphJSON1=json.dumps(graph1,cls=plotly.utils.PlotlyJSONEncoder)


#Routing
@app.route("/", methods=["GET"])
def home():
 return render_template("index.html",graphJSON=graphJSON)

@app.route("/hello", methods=["GET","POST"])
def hello():
 d=request.form.get('Item_2')
 print(d)
 j=f(d)  
 graph3=plotly.express.bar(j,x=j.Covid,y=j.Deaths)
 graphJSON3=json.dumps(graph3,cls=plotly.utils.PlotlyJSONEncoder)
 return render_template("hello.html",graphJSON3=graphJSON3,data=j.Covid)



if __name__=="__main__":
    app.run(debug=True)