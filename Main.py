from flask import Flask

app = Flask(__name__)

@app.route("/<int:surface>")
def home(surface):
    return {"surface": 1}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)