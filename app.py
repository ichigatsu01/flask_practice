# ..\flask_test\Scripts\activate 開始
# deactivate 終了
# http://localhost:8000/


from flask import Flask, render_template, request

app = Flask("helloapp")
# msg_lists = []
msg_lists = []
handle_rest = False

def rendering(msg):
    return render_template(
        'index.html',
        title = 'Hello',
        msg = msg,
        msg_lists = msg_lists
    )

#methodsでGETとPOSTを指定
@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST' :
        global msg_lists
        action = request.form['action']
        msg = request.form['msg']
        
        if action == "送信":
            msg_lists.append(msg)
            msg = 'You typed ' + msg
            return rendering(msg)
        else:
            msg_lists = []
            msg = 'テキストをクリアしました'
            return rendering(msg)
    else:
        msg = '入力した文字が追加されていきます。'
        return rendering(msg)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')