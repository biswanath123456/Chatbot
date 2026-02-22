# AI Chatbot Web Application 🤖💬

A modern, responsive chatbot web application powered by Google's Gemini AI. Built with Flask and vanilla JavaScript, featuring a clean UI with syntax-highlighted code blocks and real-time conversation.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎨 **Modern, Responsive UI** - Works seamlessly on desktop, tablet, and mobile devices
- 💬 **Real-time Chat** - Instant responses with typing indicators
- 🎯 **Syntax Highlighting** - Beautiful code blocks with copy-to-clipboard functionality
- 🔄 **Conversation Memory** - Maintains context throughout the chat session
- 🚀 **Fast & Lightweight** - Minimal dependencies, quick load times
- 🎭 **Session Management** - Separate conversation history for each user
- 📱 **Mobile Optimized** - Touch-friendly interface with responsive design

## 🖼️ Screenshots

### Desktop View
*Add a screenshot of your chatbot here*

### Mobile View
*Add a mobile screenshot here*

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/biswanath12345/ai-chatbot.git
   cd ai-chatbot
```

2. **Create a virtual environment**
```bash
   python -m venv env
   
   # On Windows:
   env\Scripts\activate
   
   # On Mac/Linux:
   source env/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up your API key**
   
   Create a `.env` file in the project root:
```
   GEMINI_API_KEY=your_api_key_here
```
   
   Get your free API key at: [Google AI Studio](https://aistudio.google.com/app/apikey)

5. **Run the application**
```bash
   python app.py
```

6. **Open your browser**
   
   Navigate to: `http://localhost:5000`

## 📁 Project Structure
```
ai-chatbot/
├── app.py                 # Flask web server
├── chatbot.py            # Chatbot logic and API integration
├── requirements.txt      # Python dependencies
├── .env                  # API keys (create this)
├── .gitignore           # Git ignore file
├── README.md            # This file
└── templates/
    └── index.html       # Web interface
```

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with gradient design
- **Code Highlighting**: Highlight.js
- **Markdown Parsing**: Python-Markdown with Pygments

## 💡 Usage

### Terminal Chat (Optional)
```bash
python chatbot.py
```

### Web Interface (Recommended)
```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

### Example Prompts

- "Write a Python function to calculate fibonacci numbers"
- "Explain how async/await works in JavaScript"
- "Create a REST API endpoint using Flask"
- "Help me debug this code: [paste your code]"

## 🎨 Customization

### Change AI Model

Edit `chatbot.py`:
```python
self.model_id = "models/gemini-2.5-flash"  # Change to gemini-2.5-pro for smarter responses
```

### Modify UI Colors

Edit `templates/index.html` - look for the gradient colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Adjust Response Length

Edit `chatbot.py` to add configuration:
```python
response = self.client.models.generate_content(
    model=self.model_id,
    contents=self.chat_history,
    config={'max_output_tokens': 2048}  # Adjust as needed
)
```

## 🔒 Security

- Never commit your `.env` file to version control
- Keep your API keys secret
- The `.gitignore` file already excludes `.env` and sensitive files
- For production deployment, use environment variables instead of `.env` files

## 🚀 Deployment

### Deploy to Railway

1. Create account at [Railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add environment variable: `GEMINI_API_KEY`
4. Deploy!

### Deploy to Heroku
```bash
# Install Heroku CLI, then:
heroku create your-app-name
heroku config:set GEMINI_API_KEY=your_key_here
git push heroku main
```

### Deploy to Render

1. Create account at [Render.com](https://render.com)
2. Connect repository
3. Add environment variable
4. Deploy as Web Service

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Flask framework for the web server
- Highlight.js for syntax highlighting
- The open-source community

## 📧 Contact

Biswanath - [@biswanath12345](https://github.com/biswanath12345)

Project Link: [https://github.com/biswanath12345/ai-chatbot](https://github.com/biswanath12345/ai-chatbot)

## 🐛 Known Issues

- None currently! Report issues [here](https://github.com/biswanath12345/ai-chatbot/issues)

## 🔮 Future Enhancements

- [ ] Add user authentication
- [ ] Save conversation history to database
- [ ] Support for image uploads
- [ ] Voice input/output
- [ ] Multiple AI model selection
- [ ] Export chat history
- [ ] Dark/Light theme toggle
- [ ] Multi-language support

---

**Star ⭐ this repo if you find it helpful!**
```

## Updated `LICENSE`:
```

Copyright (c) 2026 biswanath12345

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.