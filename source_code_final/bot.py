from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
from flask import Flask, jsonify, request
app = Flask(__name__)

CORPUS_FILE = ".\source_code_final\\chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


@app.route('/message', methods=['POST'])
def post_message():
    res = chatbot.get_response("Hi Martin, Philipp here!")
    return str(res)

if __name__ == '__main__':
    print("hello main")
    app.run()