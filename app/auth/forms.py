#coding=utf-8
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[Required(),Length(1, 64),Email()])
	password = PasswordField('Password', validators=[Required()])
	remeber_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
																					'Username must have only letters, '
																					'numbers, dots or underscores' )])
	password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[Required()]) 
	#EqualTo为什么放在第一个password上面
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')


class ChangePasswordForm(FlaskForm):
	old_password = PasswordField('Old password', validators=[Required()])
	password = PasswordField('New password', validators=[Required(), EqualTo('password2', message='Passwprds must match')])
	password2 = PasswordField('Confirm new password', validators=[Required()])
	submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('NEw Password', validators=[Required(), EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm password', validators=[Required()])
	submit = SubmitField('Reset Password')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first() is None:
			raise ValidationError('Unknown email address')


class ChangeEmailForm(FlaskForm):
	email = StringField('New Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Update Email Address')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Emai already registered.')

























