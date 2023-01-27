from flask import Flask

app=Flask("_name_")
# @app.route("/")
# def kar():
#     return render_template('index.html')

@app.route("/")
def test():
    
    return "kaushik jentibhai ghumaliya"

app.run(debug=True)

