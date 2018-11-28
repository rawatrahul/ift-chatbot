from nmt_chatbot.inference import inference
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)


@app.route("/query", methods = ['POST'])
@cross_origin()
def query():
    response = {'answer': "Sorry i did not understand that, please try again."}
    try:
        print("Received POST request for /query with data: ", request.data)
        loaded_json = json.loads(request.data)
        q = loaded_json['query']
        a = inference(q)
        # loaded_json = json.loads(a['answers'])
        t = a['answers']
        i = a['best_index']
        print(t[i])
        response = {'answer': t[i]}
    except :
        print("Error occured")
    return jsonify(response)

if __name__ == "__main__":
    print(inference("Hello"))
    app.run()