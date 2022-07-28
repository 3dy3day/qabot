from flask import render_template, request, jsonify
from __init__ import app
import search_docs

chatlog = []

@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/chat', methods=['POST', 'GET'])
def other2():
    return render_template('app/chat_interface.html')

@app.route('/ai_intereact', methods=['POST'])
def ai_intereact():
    if request.method == 'POST':
        try:
            print("---------------------")
            keyword1 = request.form["keyword1"]
            keyword2 = request.form["keyword2"]
            print("keyword1:", keyword1, "keyword2:", keyword2)
            # response, emo = chatbot.main(message)
            response = search_docs.main(keyword1, keyword2)
            print("Response:", response)
            print("---------------------")
        except:
            response = "申し訳ございません、該当するシナリオが見つかりませんでした。"
        dict = {"who": "ai", "message": str(response)}
        
    return jsonify(dict)

@app.route('/contact')
def other1():
    return render_template('app/contact.html')