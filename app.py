from flask import Flask,render_template,request
import pickle as pk
from smtplib import SMTP

app=Flask(__name__)

@app.route("/home")
def home():
    print(list)
    return render_template("main_html.html")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        city=str(request.form["city"])
        venue=str(request.form["venue"])
        team1=str(request.form["team1"])
        team2=str(request.form["team2"])
        toss_winner=str(request.form["toss_winner"])
        toss_decision=str(request.form["toss_decision"])
        date=request.form["date"]
        list=[]
        for i in range(0,84):
            list.append(0)
  
        def city_(city):
            if city=="Banglore":
                list[2]=1
            elif city=="Mohali":
                list[7]=1
            elif city=="Delhi":
                list[10]=1
            elif city=="Mumbai":
                list[21]=1
            elif city=="Jaipur":
                list[17]=1
            elif city=="Chennai":
                list[8]=1
            elif city=="Kolkata":
                list[20]=1
            elif city=="Ahmedabad":
                list[1]=1
            elif city=="Dharamsala":
                list[11]=1
            elif city=="Hyderabad":
                list[15]=1
            elif city=="Ranchi":
                list[25]=1
            else:
                list[16]=1


        def venue_(venue):
            if venue=="M Chinnaswamy Stadium":
                list[41]=1
            elif venue=="Punjab Cricket Association Stadium, Mohali":
                list[47]=1
            elif venue=="Feroz Shah Kotla":
                list[36]=1
            elif venue=="Wankhede Stadium":
                list[57]=1
            elif venue=="Sawai Mansingh Stadium":
                list[50]=1
            elif venue=="MA Chidambaram Stadium, Chepauk":
                list[42]=1
            elif venue=="Eden Gardens":
                list[35]=1
            elif venue=="Dr DY Patil Sports Academy":
                list[32]=1
            elif venue=="Sardar Patel Stadium, Motera":
                list[49]=1
            elif venue=="Himachal Pradesh Cricket Association Stadium":
                list[37]=1
            elif venue=="Subrata Roy Sahara Stadium":
                list[55]=1
            elif venue=="Rajiv Gandhi International Stadium, Uppal":
                list[48]=1
            elif venue=="Shaheed Veer Narayan Singh International Stadium":
                list[51]=1
            elif venue=="JSCA International Stadium Complex":
                list[39]=1
            elif venue=="Barabati Stadium":
                list[28]=1
            elif venue=="Maharashtra Cricket Association Stadium":
                list[43]=1
            elif venue=="Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium":
                list[33]=1
            else:
                list[38]=1

        def team1_(team1):
            if team1=="Royal Challengers Bangalore":
                list[64]=1
            elif team1=="Punjab King":
                list[62]=1
            elif team1=="Delhi Capitals":
                list[59]=1
            elif team1=="Mumbai Indians":
                list[61]=1
            elif team1=="Rajasthan Royals":
                list[63]=1
            elif team1=="Chennai Super Kings":
                list[66]=1
            elif team1=="Kolkata Knight Riders":
                list[68]=1
            else:
                list[65]=1
        
        def team2_(team2):
            if team2=="Royal Challengers Bangalore":
                list[72]=1
            elif team2=="Punjab King":
                list[70]=1
            elif team2=="Delhi Capitals":
                list[67]=1
            elif team2=="Mumbai Indians":
                list[69]=1
            elif team2=="Rajasthan Royals":
                list[71]=1
            elif team2=="Chennai Super Kings":
                list[66]=1
            elif team2=="Kolkata Knight Riders":
                list[68]=1
            else:
                list[73]=1
        
        def toss_(toss_winner):
            if toss_winner=="Royal Challengers Bangalore":
                list[80]=1
            elif toss_winner=="Punjab King":
                list[78]=1
            elif toss_winner=="Delhi Capitals":
                list[75]=1
            elif toss_winner=="Mumbai Indians":
                list[77]=1
            elif toss_winner=="Rajasthan Royals":
                list[79]=1
            elif toss_winner=="Chennai Super Kings":
                list[74]=1
            elif toss_winner=="Kolkata Knight Riders":
                list[76]=1
            else:
                list[81]=1
 
        def toss_decision_(toss_decision):
            if toss_decision=="Bat":
                list[82]=1
            else:
                list[83]=1
        
        with open("my_model","rb") as file:
            model=pk.load(file)
        city_(city)
        venue_(venue)
        team1_(team1)
        team2_(team2)
        toss_(toss_winner)
        toss_decision_(toss_decision)
        result=model.predict([list])
        #df=pd.DataFrame({"Date":pd.Series(date),"City":pd.Series(city),"Venue":Pd.Series(venue),"team1":pd.Series(team1),"team2":pd.Series(team2),"Toss Winner":pd.Series(toss_winner),"Toss Decision":pd.Series(toss_decision),"Winner":pd.Series(result)})
        
        
        
        return render_template("main_html.html",data=[date,city,venue,team1,team2,toss_winner,toss_decision,result[0]])
    
        
    
    else:
        return ("something went wrong")
        
if __name__=="__main__":
    app.run(host="localhost",debug=True,use_reloader=False,port="4060")