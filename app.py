from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'to_do'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    # Fetch tasks from the database
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    cursor.close()
    return render_template('base.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        if not task_name:
            return "Task name cannot be empty!"
        try:
            # Insert task into the database using parameterized query
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO task (Task_name) VALUES (%s)", (task_name,))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        except Exception as e:
            return "An error occurred while adding the task."

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if request.method == 'POST':
        try:
            # Delete task from the database using parameterized query
            cursor = mysql.connection.cursor()
            cursor.execute(f"DELETE FROM task WHERE id = {task_id}")
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        except Exception as e:
            return "An error occurred while deleting the task."

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        new_task_name = request.form['new_task_name']
        if not new_task_name:
            return "New task name cannot be empty!"
        try:
            # Update task in the database
            cursor = mysql.connection.cursor()
            cursor.execute (f"UPDATE task SET Task_name = '{new_task_name}' WHERE id = '{task_id}'")
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        except Exception as e:
            return f"An error occurred while updating the task: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
