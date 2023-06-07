from flask import Flask,request,render_template,jsonify
from src.pipeline.predection_pipeline import CustomData,PredictPipeline


app = Flask(__name__, template_folder='templets')



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    elif request.method=='POST':
        
        carat=float(request.form['carat'])       
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        cut = request.form['cut']
        color= request.form['color']
        clarity = request.form['clarity']
        
        data = CustomData(carat=carat,depth=depth,table=table,x=x,y=y,z=z,cut=cut,color=color,clarity=clarity)
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)

if __name__=="__main__":
    app.run(host='127.0.0.1',debug=True)




