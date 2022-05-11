from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="数を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    field = request.args.get("field", "")
    if int(field) % 2 == 0:
        result="偶数"
    else:
        result="奇数"
    return render_template('result.html', message="{}は{}です。".format(field, result))

if __name__ == '__main__':
    app.run()