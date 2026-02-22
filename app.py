from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot
import markdown  # Add this import

app = Flask(__name__)

bots = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    if session_id not in bots:
        bots[session_id] = ChatBot()
    
    bot = bots[session_id]
    
    try:
        response = bot.send_message(user_message)
        
        # Convert markdown to HTML
        html_response = markdown.markdown(response, extensions=['nl2br', 'fenced_code'])
        
        return jsonify({
            'success': True,
            'response': html_response
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/reset', methods=['POST'])
def reset():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    if session_id in bots:
        bots[session_id].reset_conversation()
    
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    