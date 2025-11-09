from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<form method="post">
  名前を入力してね：<input name="username">
  <input type="submit" value="挨拶する">
</form>
{% if submitted %}
  <div style="color: green;">登録が完了しました！</div>
{% endif %}
{% if name %}
  <h2>こんにちは、{{ name }}さん！🌟</h2>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    submitted = False
    if request.method == "POST":
        name = request.form["username"]
        submitted = True
    return render_template_string(HTML, name=name, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)
