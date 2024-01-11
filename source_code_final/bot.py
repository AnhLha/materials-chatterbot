from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from flask import Flask, jsonify, request, jsonify, make_response
from flask_cors import CORS, cross_origin
app = Flask(__name__)

# CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app)

CORPUS_FILE = ".\source_code_final\\chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

# @app.route("/")

@app.route('/message', methods=['POST'])
@cross_origin("*")
def post_message():
    content = request.json
    print("content", content)
    message = content["message"]
    print("message", message)
    res = chatbot.get_response(message)
    # return str(res)
    return jsonify({
        "status": 200,
        "data":{
            "message": str(res),
            "role":"admin"
            }
        })

if __name__ == '__main__':
    print("hello main")
    app.run()