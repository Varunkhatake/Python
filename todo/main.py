from flask import Flask, Blueprint, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ToDo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class To_do(db.Model):
    Srno = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String, nullable=False)
    Description = db.Column(db.String, nullable=False)
    Date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.Srno} - {self.Title}"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        Title = request.form["Title"]
        Description = request.form["Description"]
        todo = To_do(Title=Title, Description=Description)
        db.session.add(todo)
        db.session.commit()
    alltodo = To_do.query.all()
    return render_template("index.html", alltodo=alltodo)

@app.route("/delete/<int:Srno>")
def delete(Srno):
    todo = To_do.query.filter_by(Srno=Srno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:Srno>", methods=["GET", "POST"])
def update(Srno):
    todo = To_do.query.get_or_404(Srno)

    if request.method == "POST":
        todo.Title = request.form["Title"]
        todo.Description = request.form["Description"]
        db.session.commit()
        return redirect("/")
    
    return render_template("update.html", todo=todo)


# Run the application
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
