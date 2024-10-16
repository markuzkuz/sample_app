from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Route to render the survey form
@app.route('/')
def survey():
    return render_template('encuesta.html')

# Route to handle form submission
import os
import csv

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    experience = request.form['experience']
    havies = request.form['havies']
    aniras = request.form['aniras']
    comments = request.form.get('comments', '')

    # Check if the file exists to add headers only once
    file_exists = os.path.isfile('survey_results.csv')

    # Save data to a CSV file
    with open('survey_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file is new
        if not file_exists:
            writer.writerow(['nom', 'edat','genere', 'valoració', 'havies', 'aniras', 'comentaris'])  # Headers
        
        # Write the user data
        writer.writerow([name, age, gender, experience, havies, aniras, comments])

    return redirect('/thanks')


# Route to thank the user after submission
@app.route('/thanks')
def thanks():
    return 'Gràcies per la teves respostes, les tindrem en compte!'

if __name__ == '__main__':
    app.run(debug=True)
