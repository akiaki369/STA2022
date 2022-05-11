from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="数を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    field = int(request.args.get("field", ""))
    if field % 2 == 0:
        result="偶数"
    else:
        result="奇数"
    return render_template('result.html', message="{}は{}です。".format(field, result))

@app.route('/result', methods=["POST"])
def result_post():
    field = int(request.form["field"])

    for k in range(2, field):
        if field % k == 0:
            result = "素数ではありません"
            break
        else:
            result = "素数です"
        
    return render_template('result.html', message="{}は{}。".format(field, result))

if __name__ == '__main__':
    app.run()
