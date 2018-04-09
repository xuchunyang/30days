from flask import Flask
app = Flask(__name__)

# http://127.0.0.1:5000/powers/3
@app.route("/powers/<int:n>")
def powers(n=10):
    return ", ".join(str(2**i) for i in range(n))
