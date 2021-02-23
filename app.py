from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg', method=['GET'])
def respond():
    name = request.args.get("name", None)
    
    print(f"got name {name}")

    response = {}

    if not name:
        response["ERROR"] = "no name found, please send a name."
    elif str(name).isdigit():
        response["ERROR"] = "name can't be a numeric"
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!!"
    
    return jsonify(response)

@app.route('/post/', method=['POST'])
def post_something():
    param = request.from.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            "METHOD" : "POST"
        })
    esle:
        return jsonify({
            "ERROR": "no name fount, please send a name."
        })


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.run()