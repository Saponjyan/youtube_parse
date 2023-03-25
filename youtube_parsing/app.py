from youtubesearchpython import ChannelsSearch
from flask import Flask, render_template, redirect,url_for, request



#############################################################################

#############################################################################

app=Flask(__name__)

#app.config['SECRET_KEY'] = 'xernya'


@app.route('/', methods=["GET","POST"])
@app.route('/index.html', methods=["GET","POST"])
def index():
    if request.method=='POST':
        a=request.form.get('name')
        b = (int)(request.form['in'])
        
      

        channelsSearch = ChannelsSearch(a,limit =100)
        div=channelsSearch.result()

        ind=[]
        for i in range(0,100):
            try:

                sil=div['result'][i]['link']
                name=f"<a href='{sil}'>"+'  канал  '+div['result'][i]['title']
                kol=div['result'][i]['videoCount']
                
                ti=div['result'][i]['subscribers'][-13]
                #print(ti)
                if ti=='K':
                    tiv=div['result'][i]['subscribers'][0:-13]
                    tiz=int(float(tiv)*1000)
                    if b < tiz:
                        ind.append([i,name,kol,tiz,'<br>'])
                elif ti=='M':
                    tiv=div['result'][i]['subscribers'][0:-13]
                    tiz=int(float(tiv)*1000000)
                    if b < tiz:
                        ind.append([i,name,kol,tiz,'<br>'])
                    #print(tiz)
                else:
                    tiv=div['result'][i]['subscribers'][0:-12]
                    tiz=tiv
                    if b < tiz:
                        ind.append([i,name,kol,tiz,'<br>'])
            except:
                pass


        return f'<div class="gallery-item"><h4>{ind} </h4></div>'
        
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=False)
