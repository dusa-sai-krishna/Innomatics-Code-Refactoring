
from flask import Flask, redirect, render_template, request, url_for, session
import collections

app = Flask(__name__)
app.secret_key="key"

data=collections.defaultdict(list)

@app.route('/')
def load_login():
    return render_template('login.html')

@app.route('/home',methods=['POST','GET'])
def authentication():
    if request.method!='POST':
        return redirect(url_for("load_login"))
    username=request.form.get("username")
    if username not in data.keys():
        session['username']=username
    notes=data[session.get('username')]
    return render_template('home.html',notes=notes,count=len(notes))



@app.route('/addnote',methods=['POST','GET'])
def add_note():
    if request.method!='POST':
        return redirect(url_for("load_login"))
    note = request.form.get("note")
    notes=data[session.get('username')]
    count=len(notes)
    print(notes,note,count)
    if (count==0 and note not in [None,'']) or (count>0 and notes[-1]!=note and note not in [None,'']):
        notes.append(note)
        count+=1
    data[session.get('username')]=notes
    return render_template('home.html',notes=notes,count=len(notes))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)