from flask import render_template, request
from database import User
import json

def register_routes(app, db):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            name = request.form["name"]
            age = int(request.form["age"])
            number_of_members = int(request.form["number_of_members"])
            days = int(request.form["days"])
            travel_with = request.form["travel_with"]
            type_of_group = request.form["type_of_group"]
            destination = request.form["destination"]
            file = {
                "name" : name,
                "age" : age,
                "number_of_members" : number_of_members,
                "days" : days,
                "travel_with" : travel_with,
                "type_of_group" : type_of_group,
                "destination" : destination
            }
            print(file)

            json_file = json.dumps(file, indent=4)
            from mainPlanner import handleData
            response = handleData(json_file)

            user = User(name = name, age = age, number_of_members = number_of_members, days = days, 
                        travel_with = travel_with, type_of_group = type_of_group, destination = destination, 
                        plan = response)
            
            db.session.add(user)
            db.session.commit()

            indiv = User.query.all()
            return render_template("default.html", indiv = indiv)
        elif request.method == "GET":
            return render_template("default.html")
