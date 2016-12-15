from flask_wtf import Form
from wtforms import RadioField, SubmitField

class QuestionForm(Form):
	question = RadioField('Questions', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
