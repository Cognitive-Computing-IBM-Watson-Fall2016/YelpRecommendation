from flask_wtf import Form
from wtforms import RadioField, SubmitField

class QuestionForm(Form):
        qstn=dict()
        qstn["q1"]={"text":"You are seated very close to a wailing baby and her mother on a flight. Your thoughts?","options":["Annoyed and Irritated, you have a drink to try and sleep through this","You offer to help the mother in any way you can","You ask the air hostess if any other seat is available","You hear someone else complain and you disagree with them"]}
        qstn["q2"]={"text":"You have a free weekend with nothing to do, which would you prefer?","options":["Volunteer for a child literacy program","Hangout with your friends","Sleep!!","Help a friend who is moving"]}
        qstn["q3"]={"text":"You are attending a social party, which one defines you?","options":["You are in a polite,passionate argument with someone of an opposite view","You are the life of the party filled with bubbly energy","You are busy gobbling food","You are by yourself willing for this thing to end"]}
        qstn["q4"]={"text":"Which one of this is you?","options":["At a buffet full of great food, you plan and start eating","You make long term plans to complete tasks and achieve milestone","You plan before you start learning a new skill, language etc.","You like to have company wheb you are about to learn new things","None of these"]}
        qstn["q5"]={"text":"You are working on a group project, what role will you play?","options":["The one who does not work yet shows up to take credit :p","You just go along the flow- whatever!","You are the leader- kind, generous and fair","You do your part, nothing more or less"]}

        ops=qstn.get("q1").get("options")
        question1 = RadioField(qstn.get("q1").get("text"), choices=[(1,ops[0]), (2,ops[1]), (3,ops[2]), (4,ops[3])], default=1)
        ops=qstn.get("q2").get("options")
	question2 = RadioField(qstn.get("q2").get("text"), choices=[(1,ops[0]), (2,ops[1]), (3,ops[2]), (4,ops[3])], default=1)
	ops=qstn.get("q3").get("options")
	question3 = RadioField(qstn.get("q3").get("text"), choices=[(1,ops[0]), (2,ops[1]), (3,ops[2]), (4,ops[3])], default=1)
	ops=qstn.get("q4").get("options")
	question4 = RadioField(qstn.get("q4").get("text"), choices=[(1,ops[0]), (2,ops[1]), (3,ops[2]), (4,ops[3]),(5,ops[4])], default=1)
	ops=qstn.get("q5").get("options")
	question5 = RadioField(qstn.get("q5").get("text"), choices=[(1,ops[0]), (2,ops[1]), (3,ops[2]), (4,ops[3])], default=1)


##	question1 = RadioField('Question 1', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
##	question2 = RadioField('Question 2', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
##	question3 = RadioField('Question 3', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
##	question4 = RadioField('Question 4', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
##	question5 = RadioField('Question 5', choices=[(1,'Answer 1'), (2,'Answer 2'), (3,'Answer 3'), (4,'Answer 4')], default=1)
	submit = SubmitField('Submit')

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
