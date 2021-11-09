from flask import Flask,send_file ,redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import string
import random
from Key_generation import Key




app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')



# @app.route("/download", methods=['GET','POST'])
# def download_file():
# 	global path1
# 	path1 = os.getcwd()
# 	path1 = path1+"/static/files"
# 	if request.method == 'POST':
# 		global f
# 		f = request.form["myname"]
# 		if f in os.listdir("static/files"):         
# 			return render_template("download.html")
# 		else:
# 			return "NO file"


@app.route("/public", methods=['GET','POST'])
def public():
	if request.method == 'POST':
		global public
		public = request.form["public"]
		k1 = Key("temp")
		f,p,pr,d=k1.load_data()
		if public in p: 
			idx = p.index(public)
			return render_template("public.html", r = f[idx])
		else:
			return "NO file"
		

@app.route("/download1",methods=["POST"])
def download_file1():
	global path1
	path1 = os.getcwd()
	path1 = path1+"/static/files"
	if request.method == "POST":
		private = request.form['private']
		k1 = Key("temp")
		f,p,pr,d=k1.load_data()
		idx1 = p.index(public)
		if private == pr[idx1]:
			return send_file(path1+"/"+f[idx1],as_attachment=True)
		else:
			return "Wrong private key"
        


@app.route('/agaya', methods=['POST'])
def agaya():
	if request.method == 'POST':
		file = request.files["filename"]
		print(type(file))
		
	if file:
		temp_folder = "static/files/"
		lists = os.listdir(temp_folder)
		alpha =  list(string.ascii_lowercase)
		p  = random.sample(alpha,5)
		code = "".join(p)
		code_c = code+".jpg"
		k= Key(code_c)
		public_k,private_k = k.generate()
		if  code_c not in lists:
			file_path = os.path.join(temp_folder+ code+".jpg")
			file.save(file_path)
			return "Your Public Key: \n{}\n Your Private Key: \n{}".format(public_k,private_k) #send_file(file_path,as_attachment=True)  
		else:
			return "file is already availaible"
		    
	else:
		return "File nahi ai "


	


if __name__ == "__main__":
	app.run(debug=True)


