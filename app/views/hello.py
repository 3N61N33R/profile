from app import app

# test route
@app.route("/hello")
def hello():
    return "Hello, World!"
