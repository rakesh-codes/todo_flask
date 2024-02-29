Flask Todo App with Built-in MySQL Database
This is a simple Flask Todo application with a built-in MySQL database for storing tasks. Users can add new tasks, mark tasks as complete, update task descriptions, and delete tasks.

Setup Instructions
Follow these steps to set up and run the Flask Todo app with a built-in MySQL database:

Clone the Repository:

bash
Copy code
git clone <repository_url>
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Create MySQL Database:

Set up a MySQL database using a tool like phpMyAdmin or MySQL command line.
Update the MySQL configurations in app.py with your database details.
Run the Application:

bash
Copy code
python app.py
Access the Todo App:

Open your web browser and go to http://localhost:5000 to access the Todo app.

Functionality
Add Task: Enter a task description in the input field and click "Add Task" to add it to the list.
Update Task: Click the "Edit" button next to a task to update its description.
Delete Task: Click the "Delete" button next to a task to remove it from the list.
Technologies Used
Python
Flask
Flask-MySQLdb
HTML
CSS
MySQL
Project Structure
arduino

.
├── app.py
├── static
│   ├── styles.css
│   └── script.js
├── templates
│   └── index.html
└── README.md
License
This project is licensed under the MIT License. See the LICENSE file for details.

![image](https://github.com/rakesh-codes/todo_flask/assets/132572472/40621079-b4f8-4531-8af8-e9acd1ee9397)
