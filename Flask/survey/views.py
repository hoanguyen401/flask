from flask import render_template
from flask import request
from survey import app, db
from survey.models import Question


#from scrapy.utils.template import render_templatefile
#from ansible.module_utils.netapp import request


@app.route('/', methods=['GET'])
def home():
    qs = Question.query.all()
    context = {'Questions': qs, 'Number_of_question': len(qs)}
    return render_template('index.html', **context)
    
@app.route('/question', methods=['POST'])
def add():
    if request.form['text'].strip() != '':
        newQ = Question(question_text = request.form['text'])
        db.session.add(newQ)
        db.session.commit()
        message = "Question is created"
    else:
        message = "Pool question is full"    
    context = {"questions": Question.query.all(), "Message": message}
    return render_template('index.html', **context)

@app.route('/newquestion', methods=['GET'])
def newQuestion():
    return render_template('new.html')
        
        
    
