from flask import Flask, render_template ,request,g
import sqlite3

app_info = {
    'app_file' : r'C:\Users\domin\OneDrive\Documents\project\udemi\flask2\tutoriat-\data\engrams.db'
}

app =  Flask(__name__)


def get_db():
    if not hasattr(g,'sqlite_db'):
        conn = sqlite3.connect(app_info['app_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db =  conn
    return  g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite3_db'):
        g.sqlite_db.close()

class Gender:
    def __init__(self, code, name, symbol):

        self.code = code 
        self.name = name
        self.symbol = symbol 

    def __repr__(self) -> str:
        return '<Gender- {}>'.format(self.code)
    
class GenderType:
    def __init__(self):
        self.genders=[]

    def load_gender(self):
        self.genders.append(Gender('Woman','female','female.png'))
        self.genders.append(Gender('Man','male','male.png'))
    def get_by_code(self, code):
        for gender in self.genders:
            if gender.code == code:
                return gender
            

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/formula',methods=['GET','POST'])
def formula():

    type_g = GenderType()
    type_g.load_gender()

    if request.method == 'GET':
    
        return render_template('formula.html',type_g=type_g)
    else: 

        if 'imie' in request.form:
            imie = request.form['imie'] 
            if imie == '':
                imie = 'none'
            
        if 'nazwisko' in request.form:
            nazwisko = request.form['nazwisko']
            if nazwisko == '':
                nazwisko = 'none'
        if 'wiek' in request.form:
            wiek = request.form['wiek']
            if wiek == '':
                wiek = 'none'
        if 'gender' in request.form:
            gender = request.form['gender']


        db = get_db()
        sql_comand = 'insert into ofengrams(name, sname, old) values(?,?,?)'
        db.execute(sql_comand, [imie , nazwisko, wiek])
        db.commit()
        return render_template('formula_r.html',imie=imie , nazwisko=nazwisko, wiek=wiek,gender=gender,
                               gender_info=type_g.get_by_code(gender))  
    
@app.route('/history')
def history():
    db=get_db()
    sqlite3
if __name__ == '__main__':
    app.run()