from flask import Flask, render_template, url_for, request,redirect
import csv
import os
app = Flask(__name__)  # main


@app.route('/')
def home(username="Unknown User", post_id=None):
    return render_template('index.html', name=username, id=post_id)
    # flask automatically look at templates folder


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        messages = data["messages"]
        file = database.write(f'\n{email},{subject},{messages}')

# csv : comma separated values
def write_to_csv(data):
    script_dir = os.path.dirname(__file__)
    rel_path = "/database.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open('./database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        messages = data["messages"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,messages])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/submit_response.html')
        except:
            return 'did not save to database'
    return 'Something went wrong. Try again!'
