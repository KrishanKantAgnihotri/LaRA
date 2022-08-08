import pickle 
from flask import Flask,render_template,request,redirect
import numpy as np 
from store import df
app = Flask(__name__) 
pipe = pickle.load(open('./model/pipe.pkl','rb'))
data = pickle.load(open('./model/data.pkl','rb'))
@app.route('/',methods=['POST','GET'])
def index():
    pred2 =0
    obj2 = ''
    if request.method == 'POST':
    
        ram = request.form['ram']
        # weight = request.form['weight']
        company = request.form['company']
        typename= request.form['typename']
        os = request.form['opsys']
        cpu = request.form['cpuname']
        screen = request.form['scr']
        resol = request.form['resolution']
        hdd = request.form['hdd']
        ssd = request.form['ssd']
        gpu = request.form['gpuname']
        ts = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')
        fact = 1
        if ram=='': 
            ram ='2'
        if company=='': 
            company ='acer'
        if typename=='':
            typename ='gaming'
        if cpu=='':
            cpu='intelcorei3'
        if resol=='':
            resol='1920X1080'
        if hdd=='':
            hdd='0'
        if ssd=='':
            ssd='128'
        if os=='':
            os='windows'
        if gpu=='':
            gpu='intel'
        if cpu=='intelcorei3' and ram=='8':
            fact = 2
        if company=='apple':
            fact = 0.83
        x = int(resol.split('X')[0])
        y = int(resol.split('X')[1])
        screen = float(screen)
        if screen == 0.0:
            screen = 14
        ppi= ((x**2 + y**2)**(0.5))/screen
        cp = data['Company'].unique()
        typnm = data['TypeName'].unique()
        cpupro = data['CpuProcessor'].unique()
        ops = data['OS'].unique()
        gpuname = data['GpuName'].unique()
        # print(typnm)
        for item in cp:
            if item.lower() == company:
                company = item
        mark = False
        for item in typnm:
            if item.lower() == typename:
                typename = item
                mark = True
        if mark==False:
            typename = '2 in 1 Convertible'
        weight = 1.73
        for item in cpupro:
            new = item.split(' ')
            new = ''.join([str(it) for it in new])
            if new.lower() == cpu:
                cpu = item
        if os == 'windows':
            os = 'Windows'
        elif os == 'mac':
            os = 'Mac'
        else:
            os = "Others/No OS/Linux" 
        for item in gpuname:
            if item.lower() == gpu:
                gpu = item
        # print(type(ram),type(weight),type(company),type(typename),type(os),type(cpu),type(ppi),type(hdd),type(ssd),type(gpu),ts,ips) 
        query = np.array([company,typename,ram,weight,len(ts),len(ips),ppi,cpu,hdd,ssd,gpu,os])
        query = query.reshape(1,12)
        # print(query)
        
        pred = pipe.predict(query)
        pred = np.exp(pred)*80
        pred = pred/fact
        pred = int(pred)
        # pred = 0
        print(pred)
        p = pred
        #convert p in query form 
        if p <=50000:
            p = '30'
        elif p>=50001 and p<=70000:
            p ='60'
        elif p>=70001 and p<=100000:
            p ='90'
        elif p>=100001 and p<=150000:
            p ='130'
        elif p>=150001 and p<=200000:
            p ='180'
        elif p>=200001 and p<=300000:
            p = '200'
        else:
            p = '300'
        
        obj = df[p]     
        # print(obj)
        return render_template("index.html",pred_value=pred,obj=obj)
    return render_template("index.html",pred_value = pred2,obj =obj2)


if(__name__=='__main__'):
    app.run(debug=True)