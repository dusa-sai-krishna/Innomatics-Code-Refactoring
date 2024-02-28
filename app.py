from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/')
def load_home():
    return render_template('home.html',notes=notes,count=len(notes))

@app.route('/addnote',methods=['POST'])
def add_note():
    note = request.form.get("note")
    count=len(notes)
    print(notes,note,count)
    if (count==0 and note not in [None,'']) or (count>0 and notes[-1]!=note and note not in [None,'']):
        notes.append(note)
        count+=1
    return render_template('home.html',notes=notes,count=len(notes))


if __name__ == '__main__':
    app.run(debug=True)