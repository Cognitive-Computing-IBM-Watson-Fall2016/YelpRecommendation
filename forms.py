from flask_wtf import Form
from wtforms import RadioField, SubmitField

class QuestionForm(Form):
	question1 = RadioField('Question 1', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	question2 = RadioField('Question 2', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	question3 = RadioField('Question 3', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	question4 = RadioField('Question 4', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	question5 = RadioField('Question 5', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
