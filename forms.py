from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email




class Form (FlaskForm):
	name=StringField("Name", validators=[DataRequired("please fill in this field😔!")])
	email=StringField("Email", validators=[DataRequired("please fill in this field😔!"), Email("This email is invalid😕", "danger")])
	pic=StringField("ig_pic_url", validators=[DataRequired("please fill in this field😔!")])
	message=TextAreaField("What is on your mind")
	password=PasswordField("Password", validators=[DataRequired("please fill in this field😔!")])
	remember=BooleanField("Remember me😊", validators=[DataRequired("please fill in this field😔!")])
	submit=SubmitField("Add👤")
	
class Next (FlaskForm):
	submit=SubmitField("Add👤")
	