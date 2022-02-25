from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route('/')
def hello():
    try:
        return render_template("index.html")
    except:
        print("ERROR! index.html file location is incorrect. Follow the following steps to resolve this issue: \n1)run `docker exec` and enter to your continer.\n2)run `mv index.html templates/index.html` and try to refresh your browser.")
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')