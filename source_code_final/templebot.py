# from email import message
# from urllib import request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
# from flask import Flask, jsonify, request
# app = Flask(__name__)

CORPUS_FILE = ".\source_code_final\\chat.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")

# ###################





# @app.route('/message', methods=['POST'])
# def post_message():
#     # print(" request body: ", {request.args.get})
#     # userMessage = request.args.get('message')
#     # print( "userMessage " + {userMessage} )
#     res = chatbot.get_response("Hi Martin, Philipp here!")
#     # message = request.json[res]
#     # return jsonify({'message': message})
#     return str(res)

# # @app.route('/cal', methods=['GET'])
# # def get_cal():
# #     result = subprocess.check_output(['cal']).decode('utf-8')
# #     return jsonify({'calendar': result.strip()})

# # @app.route('/docker', methods=['GET'])
# # def get_docker():
# #     result = subprocess.check_output(['docker', 'ps']).decode('utf-8')
# #     return jsonify({'docker': result.strip()})

# # @app.route('/cls', methods=['GET'])
# # def get_cls():
# #     result = subprocess.check_output(['cls']).decode('utf-8')
# #     return jsonify({'cls': result.strip()})

# if __name__ == '__main__':
#     print("hello main")
#     app.run()