from flask import Flask, render_template, request, flash
from form import ContactForm

app = Flask(__name__, template_folder='/home/behien/eclipse-workspace/Flask/survey')
app.secret_key = 'development key'

@app.route('/contact', methods=['GET','POST'])
def contact():
        f = ContactForm()
        if request.method == 'POST':
            if f.validated() == False:
                flash('All field required')
                return render_template('contact-old.html', form = f)
            else:
                return render_template('sucess.html')
        elif request.method == 'GET':
                return render_template('contact-old.html', form = f)

if __name__ == '__main__':
    app.run(debug= True)
