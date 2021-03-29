from flask import Flask 



app = Flask(__name__)
app.debug = True


@app.route("/")
def test():
  return "hola"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

