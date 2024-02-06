# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask , render_template , redirect, url_for
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('main_page.html')

@app.route('/emiCalculator')
def emiCalculator():
      return render_template('emical2.html')

@app.route('/pricePredictor')
def pricePredictor():
      return render_template('predictor.html')

@app.route('/main')
# ‘/’ URL is bound with hello_world() function.
def main():
    return redirect(url_for('hello_world'))

@app.route('/temp')
# ‘/’ URL is bound with hello_world() function.
def temp():
    return render_template( '')

@app.route('/carListingForm')
# ‘/’ URL is bound with hello_world() function.
def carListingForm():
    return render_template( 'carListingForm.html')

@app.route('/whyUs')
# ‘/’ URL is bound with hello_world() function.
def whyUs():
    return render_template( 'whyUs.html')
 
@app.route('/aboutUs')
# ‘/’ URL is bound with hello_world() function.
def aboutUs():
    return render_template( 'aboutUs.html')


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run( debug=True , port=8000)


