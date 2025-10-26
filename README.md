# AI-Powered Discord Bot

A simple Discord bot that uses AI models (Perplexity Sonar and Google Gemini) to answer questions with text and image inputs. Perfect for anyone who wants an intelligent chatbot in their Discord server!

## 🌟 What Does This Do?

This bot allows you to ask questions in your Discord server and get AI-powered responses. You can ask questions with just text or include images for the AI to analyze. The bot uses powerful AI models like Perplexity's Sonar and Google's Gemini to provide intelligent answers.

## 📋 Features

- **Text-based Questions**: Ask any question and get intelligent responses
- **Image Analysis**: Send images along with questions to extract information from pictures
- **Multiple AI Models**: Supports Perplexity Sonar, Sonar Pro, and Google Gemini 2.5 Flash
- **Easy to Use**: Simple Discord commands anyone can use
- **Friendly Chatbot Personality**: Engaging and conversational responses

## 🛠️ What You'll Need

Before you start, make sure you have:

1. **Python 3.7 or newer** installed on your computer
   - Download from [python.org](https://www.python.org/downloads/)
   
2. **A Discord Account** and a server where you can add bots

3. **API Keys** (free to get):
   - **Perplexity API Key**: Sign up at [Perplexity AI](https://www.perplexity.ai/)
   - **Google Gemini API Key**: Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **Discord Bot Token**: Create a bot at [Discord Developer Portal](https://discord.com/developers/applications)

## 📦 Installation

### Step 1: Download the Project

Download or clone this project to your computer and save it in a folder.

### Step 2: Install Required Packages

Open your terminal or command prompt, navigate to the project folder, and run:

```bash
pip install openai discord.py
```

This installs the necessary libraries for the bot to work.

### Step 3: Set Up Your API Keys

Open the files and add your API keys:

**In `AI_API.py`:**
- Find `"Your_api_key"` (appears twice for Perplexity)
- Replace it with your actual Perplexity API key
- Find `"your_api_key"` (for Gemini)
- Replace it with your actual Google Gemini API key

**In `bot_api.py`:**
- Find `"your_discord_bot_token_here"`
- Replace it with your Discord bot token

### Step 4: Create Your Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under "TOKEN", click "Copy" to get your bot token (paste this in `bot_api.py`)
5. Enable "MESSAGE CONTENT INTENT" under Privileged Gateway Intents
6. Go to "OAuth2" → "URL Generator"
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Read Messages/View Channels`
9. Copy the generated URL and open it in your browser to add the bot to your server

## 🚀 How to Run

1. Open your terminal or command prompt
2. Navigate to the project folder
3. Run the bot with:

```bash
python bot_api.py
```

4. You should see a message: `YourBotName has connected to Discord!`

## 💬 How to Use the Bot

Once your bot is online in your Discord server, you can interact with it using commands:

### Basic Command Format

```
-ask [image_path] [your question]
```

### Examples

**Ask a text-only question:**
```
-ask none What is the capital of France?
```

**Ask a question with an image:**
```
-ask https://example.com/image.jpg What's in this image?
```

The bot will:
1. Respond with "Processing your request..."
2. Send the AI's response to your question

## 🔧 How It Works

### AI_API.py
This file contains the main AI function that:
- Connects to AI models (Perplexity Sonar or Google Gemini)
- Sends your questions (with or without images) to the AI
- Returns the AI's response

**Supported Models:**
- `sonar` - Perplexity's standard model (great for general questions)
- `sonar-pro` - Perplexity's advanced model (more detailed responses)
- `gemini-2.5-flash` - Google's Gemini Flash model (fast and efficient)

### bot_api.py
This file runs the Discord bot that:
- Listens for commands in your Discord server
- Takes your question and passes it to the AI
- Sends back the AI's response in Discord

## 🎯 Project Structure

```
project-folder/
│
├── AI_API.py          # AI model integration
├── bot_api.py         # Discord bot main file
└── README.md          # This file (documentation)
```

## ⚠️ Important Notes

- **Keep Your API Keys Secret**: Never share your API keys or bot token publicly
- **API Limits**: Free API tiers have usage limits. Check your provider's documentation
- **Image URLs**: When using images, make sure the URL is publicly accessible
- **Internet Required**: The bot needs an active internet connection to work

## 🐛 Troubleshooting

**Bot doesn't respond:**
- Make sure the bot is online (check Discord server member list)
- Verify "MESSAGE CONTENT INTENT" is enabled in Discord Developer Portal
- Check that your command starts with `-ask`

**"Model not supported" error:**
- Check that you're using one of the three supported models in the code

**API errors:**
- Verify your API keys are correct
- Check if you've exceeded your free tier limits
- Ensure you have an active internet connection

## 🔐 Security Tips

- Never commit API keys to GitHub or public repositories
- Use environment variables for storing sensitive information in production
- Regularly rotate your API keys and bot tokens

## 📝 Customization

You can customize the bot by editing `AI_API.py`:
- Change the chatbot personality by modifying the system prompt
- Adjust response styles (concise vs. detailed)
- Add more AI models by following the existing pattern

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project and make improvements! Suggestions and pull requests are welcome.

## 💡 Need Help?

If you run into issues:
1. Double-check all API keys are correctly set
2. Verify all required packages are installed
3. Check the Discord bot has proper permissions
4. Review error messages in your terminal for clues

---

**Enjoy your AI-powered Discord bot! 🤖✨**
