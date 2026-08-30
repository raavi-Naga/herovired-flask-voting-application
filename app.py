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
    if not voterslist:
        return {"message": "No votes recorded"}
    total = sum(voterslist.values())
    return {"message": f"Total votes recorded: {total}", "voters": voterslist}
@app.get('/reset')
def reset():
    voterslist.clear()
    return {"message": "Votes count have been reset successfully!"}
if __name__ == '__main__':
    app.run(debug=True) 