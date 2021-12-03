from flask import Flask, render_template, request, redirect, jsonify
from egao import Egao

app = Flask(__name__)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        date = request.form['date']
        photo = request.files['photo'].read()
        ega = Egao(photo, date)
        encoded_img_data = ega._editor()
        return {'success':True, 'text':'file uploaded successfully', 'image':encoded_img_data.decode('utf-8')}
    else:
        return redirect('/')

@app.route('/')
def index():
    return render_template('/index.html')
    
@app.route('/')
def google_verif():
    return render_template('/googlef3bd9b0ca627d401.html')

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template('not-found.html')
    
if __name__ == '__main__':
    app.run(debug = True)
