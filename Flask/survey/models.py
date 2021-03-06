from survey import  app, db


class Question(db.Model):
    def __init__(self, question_text, nu_yes=0, nu_no=0 , nu_maybe = 0):
        self.text = question_text
        self.nu_maybe = nu_maybe
        self.nu_no = nu_no
        self.nu_yes = nu_yes
    # Flask - ORM
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(40))
    nu_yes = db.Column(db.Integer, default = 0)
    nu_no = db.Column(db.Integer, default = 0)
    nu_maybe = db.Column(db.Integer, default = 0)
    
    def vote(self, votetpe):
        if votetpe == 'yes':
            self.nu_yes += 1
        elif votetpe == 'no':
            self.nu_no += 1
        elif votetpe== 'maybe':
            self.nu_maybe +=1
        else:
            raise Exception('Invalid vote')
            
         
            
