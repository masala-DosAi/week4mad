from flask import Flask
from flask import render_template
app=Flask(__name__)
from flask import request
import matplotlib.pyplot as plt

@app.route("/",methods=["GET","POST"])

def index():    
        if request.method=="GET":
                return render_template("index.html")

        elif request.method=="POST":          
               var = request.form["category"] 
               value = request.form['id_value']

               if var=="s_id" and value[0]=='1':
                        total=0
                        ls=[]
                        f= open("data.csv",'r')
                        hd=list(f.readline().split(','))


                        for x in f:
                                if list(x.split(', '))[0]==value:
                                         ls.append(list(x.split(', ')))
                                print(ls)
                                
                                for t in ls:
                                        total+=int(t[2])
                        f.close()                                    
                        return render_template("output.html.jinja2",data=ls,header ="Student details",headd=hd,total_marks=total)

               elif var=="c_id" and value[0]=='2':
                        ls=[]
                        f= open("data.csv",'r')
                        hd=list(f.readline().split(', '))
                        for x in f:
                                if list(x.split(', '))[1]==value:
                                                ls.append(int(list(x.split(', '))[2]))
                        print(ls)
                        f.close()
                        avg=sum(ls)/len(ls)
                        max_val=max(ls)


                        # Create and save the histogram
                        plt.hist(ls, bins=5, edgecolor='black')
                        plt.xlabel('Values')
                        plt.ylabel('Frequency')
                        plt.title('Histogram')

                        # Save the image
                        image_path = "histogram.png"
                        plt.savefig(image_path)
                        plt.close()


                        return render_template("outputc.jinja2",average=avg,maximum=max_val,header="Course Details",image_path="histogram.png")
               else:
                        return render_template("outputelse.jinja2")
        else:
                       return render_template("outputelse.jinja2")

               
                 

               


if __name__=="__main__":
        app.debug=True
        app.run()