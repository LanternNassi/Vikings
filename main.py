from flask import Flask, render_template, redirect, url_for, flash
from forms import Form
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 
import os


app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)

key = os.urandom(45)
app.config["SECRET_KEY"] = key
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///vikings.db"

class Vi_db(db.Model):
	id = db.Column(db.Integer, primary_key=True )
	name = db.Column(db.String())
	email = db.Column(db.String())
	pic = db.Column(db.String())
	message = db.Column (db.String())
	
	def __repr__ (self):
		return f"Vi_db('{self.name}', '{self.email}', '{self.pic}', {'self.message'})"

@app.route('/')
def home ():
	students=Vi_db.query.all()
	return render_template("home.html", students=students, title="#SHACK_Vikings*_*2018-2022")


@app.route('/new', methods=["GET","POST"])
def new ():
	form=Form()
	added=Vi_db(name = form.name.data,
	 email = form.email.data,
	 pic = form.pic.data, 
	 message = form.message.data)
	if form.validate_on_submit() and form.password.data=="password is password":
		db.session.add(added)
		db.session.commit()
		flash(f"{form.name.data} was added",'info')
		return redirect(url_for ("home"))
	elif form.password.data != "password is password" :
		flash(f"Post not added due to incorrect password password⚠️", 'danger')
	return render_template ('new.html', form=form, title='add👤')

if __name__=="__main__":
	app.run(debug=False)