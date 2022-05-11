from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="数を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    field = int(request.args.get("field", ""))

    for k in range(2, field):
        if field % 2 == 0:
            result = "素数ではありません"
            break
        else:
            result = "素数です"
        
    return render_template('result.html', message="{}は{}。".format(field, result))

if __name__ == '__main__':
    app.run()