from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = 'Tony Mele'
    data = "[{'name': 'tony', 'age':'33'}]"
    return render_template("index.html", name=user, data=data)


if __name__ == '__main__':
    print("Updating Data on Startup")
    import modules.update_source_data
    import modules.data_preperation
    app.run(port=5454, debug=True)
