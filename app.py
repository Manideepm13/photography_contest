from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    with sqlite3.connect("data.db") as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            participant_name TEXT NOT NULL,
            photo_path TEXT NOT NULL,
            score INTEGER DEFAULT 0
        );
        ''')
        conn.commit()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# View contest rules
@app.route('/rules')
def rules():
    return render_template('rules.html')

# Submit photo
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        participant_name = request.form['name']
        photo = request.files['photo']

        if photo:
            photo_path = f"static/{photo.filename}"
            photo.save(photo_path)

            # Insert into database
            with sqlite3.connect("data.db") as conn:
                conn.execute('''
                INSERT INTO submissions (title, description, participant_name, photo_path)
                VALUES (?, ?, ?, ?);
                ''', (title, description, participant_name, photo_path))
                conn.commit()

            return redirect(url_for('index'))
    return render_template('submit.html')

# Show all contest results
@app.route('/results')
def results():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.execute('SELECT * FROM submissions')
        submissions = cursor.fetchall()
    return render_template('results.html', submissions=submissions)

# Judge submission score
@app.route('/judge/<int:submission_id>', methods=['GET', 'POST'])
def judge(submission_id):
    if request.method == 'POST':
        score = request.form['score']
        with sqlite3.connect("data.db") as conn:
            conn.execute('UPDATE submissions SET score = ? WHERE id = ?', (score, submission_id))
            conn.commit()
        return redirect(url_for('results'))

    with sqlite3.connect("data.db") as conn:
        cursor = conn.execute('SELECT * FROM submissions WHERE id = ?', (submission_id,))
        submission = cursor.fetchone()

    return render_template('judge.html', submission=submission)

if __name__ == '__main__':
    init_db()  # Ensure the database is set up
    app.run(debug=True)
