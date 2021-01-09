from flask import Flask, render_template, request, redirect,url_for
import csv
app = Flask(__name__, template_folder='templates')

app.debug = True
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about.html/')
def about_me():
    return render_template('about.html')

@app.route('/works.html/')
def my_works():
    return render_template('works.html')

@app.route('/contact.html/')
def my_contacts():
    return render_template('contact.html')

@app.route('/works.html/work.html/')
def work():
    return render_template('work.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database2.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/thankyou.html/')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit_form/', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('thankyou'))
        except:
            return 'something is wrong!!!'
    else:
        return 'something went wrong'



