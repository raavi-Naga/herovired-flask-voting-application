from flask import Flask, jsonify, request
voterslist ={}
app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to the App"

@app.get("/health")
def health():
    return "App is running"
@app.get("/vote/<name>")
def vote(name):
    if name in voterslist:
        voterslist[name] = voterslist[name] + 1
    else:
        voterslist[name] = 1
    return {"message": f"Vote recorded for {name}", "votes": voterslist[name]}
@app.get('/results')
def results():
    return voterslist
if __name__ == '__main__':
    app.run(debug=True) 