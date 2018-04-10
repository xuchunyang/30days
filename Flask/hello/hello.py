# 教程：
# http://flask.pocoo.org/docs/0.12/quickstart
#
# 运行：
# $ FLASK_DEBUG=1 FLASK_APP=hello.py flask run

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hi")
@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % username

@app.route("/post/<post_id>")
def show_post(post_id):
    return "Post %s" % post_id

# ------------  URL Building --------------#
with app.test_request_context():
    print(url_for("index"))

#-------------- HTTP Methods ---------------#
# ~ $ curl -X POST http://127.0.0.1:5000/login
# ~ $ curl -X GET http://127.0.0.1:5000/login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "TODO do_the_login()"
    else:
        return "TODO show_the_login_form()"

#----------------- Static Files -------------#

# url_for("static", filename="style.css")

#-----------  Rendering Templates -----------#

from flask import render_template

@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)

#-------------- Accessing Request Data --------#

from flask import request

# $ curl -X POST -d username=foo http://127.0.0.1:5000/login
@app.route('/login2', methods=['POST', 'GET'])
def login2():
    error = None
    if request.method == 'POST':
        return "TODO log_the_user_in {}".format(request.form['username'])
    return "TODO GET login page"

# --------------- File Uploads ----------------#
from flask import request

# curl -X POST -F 'the_file=@/etc/shells' http://127.0.0.1:5000/upload
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/tmp/uploaded_file.txt')
    return "TODO show the upload page"

# ----------------- Cookies ---------------------#

# ----------------- Redirect and Errors ---------#

from flask import abort, redirect, url_for

@app.route('/foo')
def foo():
    return redirect(url_for("bar"))

@app.route('/bar')
def bar():
    abort(401)
    1 / 0 + "this is never executed"

    
# ------------------ Logging ---------------------#
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
