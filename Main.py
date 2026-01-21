from flask import Flask

app = Flask(_name_)

@app.route("/<int:surface>")
def home(surface):
    return {"surface": 1}

if _name_ == "_main_":
    app.run(debug=True)