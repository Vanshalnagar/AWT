from flask import Flask, render_template, request, redirect, url_for, flash
import json, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')


def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def next_id(students):
    return max((s['id'] for s in students), default=0) + 1


@app.route('/', methods=['GET', 'POST'])
def index():
    students = read_data()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            students.append({
                'id': next_id(students),
                'name': request.form['name'],
                'email': request.form['email'],
                'age': int(request.form['age']),
                'department': request.form['department']
            })
            write_data(students)
            flash('Student added successfully!', 'success')

        elif action == 'update':
            sid = int(request.form['id'])
            for s in students:
                if s['id'] == sid:
                    s.update({
                        'name': request.form['name'],
                        'email': request.form['email'],
                        'age': int(request.form['age']),
                        'department': request.form['department']
                    })
                    break
            write_data(students)
            flash('Student updated successfully!', 'success')

        elif action == 'delete':
            sid = int(request.form['id'])
            students = [s for s in students if s['id'] != sid]
            write_data(students)
            flash('Student deleted!', 'danger')

        return redirect(url_for('index'))

    edit_id = request.args.get('edit_id', type=int)
    edit_student = next((s for s in students if s['id'] == edit_id), None)
    return render_template('index.html', students=students, edit_student=edit_student)


if __name__ == '__main__':
    app.run(debug=True)
