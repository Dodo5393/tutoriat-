from flask import Flask, render_template ,request

app =  Flask(__name__)


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

        return render_template('formula_r.html',imie=imie , nazwisko=nazwisko, wiek=wiek,gender=gender,
                               gender_info=type_g.get_by_code(gender))  
    
if __name__ == '__main__':
    app.run()