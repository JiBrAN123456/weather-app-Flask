from flask import Flask, request , jsonify, render_template

app = Flask(__name__)

tasks = []

@app.route("/")
def hello():
    return render_template("todolist.html", tasks=tasks)

@app.route("/tasks", methods=["GET","POST"])
def task_handler():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
           tasks.append(task)
        return render_template("todolist.html", tasks=tasks)
    
@app.route("/tasks/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return render_template("todolist.html", tasks=tasks)
    
if __name__ == "__main__":
   app.run(debug=True)
