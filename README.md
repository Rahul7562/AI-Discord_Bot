# AI-Discord_Bot

# AI API Wrapper

A flexible Python wrapper for multiple AI APIs including Perplexity Sonar and Google Gemini models. This wrapper provides a unified interface for making text and vision-based queries across different AI providers.

## Features

- **Multi-Model Support**: Seamlessly switch between Perplexity Sonar, Sonar-Pro, and Google Gemini 2.5 Flash
- **Vision Capability**: Support for image-based queries (vision models)
- **Unified Interface**: Single function call works across all supported models
- **OpenAI-Compatible**: Uses OpenAI SDK format for easy integration
- **Simple API**: Minimal setup with straightforward function calls

## Supported Models

| Model | Provider | Vision Support | Use Case |
|-------|----------|----------------|----------|
| `sonar` | Perplexity | ✅ | Fast web-grounded responses |
| `sonar-pro` | Perplexity | ✅ | Advanced reasoning with web access |
| `gemini-2.5-flash` | Google | ✅ | Fast multimodal responses |

## Installation

```bash
pip install openai
```

## Setup

1. **Get API Keys**:
   - **Perplexity API Key**: Visit [Perplexity AI Settings](https://www.perplexity.ai/settings/api) to generate your API key
   - **Google Gemini API Key**: Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to get your key

2. **Update API Keys in Code**:
   Replace `"Your-API-Key"` placeholders in `AI_API.py` with your actual API keys

## Usage

### Basic Text Query

```python
from AI_API import API

# Using Perplexity Sonar
API("sonar", "What are the latest developments in quantum computing?")

# Using Perplexity Sonar Pro
API("sonar-pro", "Explain the implications of recent AI regulations")

# Using Google Gemini
API("gemini-2.5-flash", "Summarize the current state of renewable energy")
```

### Vision Query (with Image)

```python
from AI_API import API

# Analyze an image with text prompt
API(
    model="sonar-pro",
    user_prompt="What objects are in this image?",
    image_path="https://example.com/image.jpg"  # Can be URL or local path
)
```

### Interactive Mode

Run the script directly for interactive prompting:

```bash
python AI_API.py
```

## Function Reference

### `API(model, user_prompt, image_path=None)`

Main function to query AI models.

**Parameters**:
- `model` (str): Model identifier - `"sonar"`, `"sonar-pro"`, or `"gemini-2.5-flash"`
- `user_prompt` (str): Your text query or instruction
- `image_path` (str, optional): URL or file path to image for vision queries

**Returns**:
- Prints the model's response directly to console

## Security Best Practices

⚠️ **Important**: Never commit API keys to version control!

### Recommended: Use Environment Variables

Create a `.env` file:

```env
PERPLEXITY_API_KEY=your-perplexity-key-here
GEMINI_API_KEY=your-gemini-key-here
```

Update code to use environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Replace hardcoded keys with:
api_key=os.getenv("PERPLEXITY_API_KEY")  # for Perplexity
api_key=os.getenv("GEMINI_API_KEY")      # for Gemini
```

Install `python-dotenv`:
```bash
pip install python-dotenv
```

---

## 🚀 Future Integration: Discord Bot

This API wrapper is designed for seamless Discord bot integration. Here's what's planned:

### Planned Features

- **Slash Commands**: `/ask` command for quick AI queries
- **Mention Support**: Ask questions by mentioning the bot
- **Image Analysis**: Upload images directly in Discord for vision queries
- **Model Selection**: Switch between models with command flags
- **Thread Support**: Maintain conversation context in Discord threads
- **Rate Limiting**: Built-in cooldowns to prevent API abuse
- **Error Handling**: User-friendly error messages for Discord

### Discord Bot Integration Example

```python
import discord
from discord.ext import commands
from AI_API import API

# Setup bot with required intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected!')
    await bot.tree.sync()  # Sync slash commands

# Slash command for AI queries
@bot.tree.command(name="ask", description="Ask the AI a question")
async def ask_command(interaction: discord.Interaction, prompt: str, model: str = "sonar-pro"):
    """
    Ask AI a question
    
    Parameters:
    - prompt: Your question
    - model: AI model (sonar, sonar-pro, gemini-2.5-flash)
    """
    await interaction.response.defer()  # Bot is "thinking"
    
    try:
        # Call AI API (need to modify API function to return response instead of print)
        response = API(model, prompt)
        
        # Send response in Discord
        await interaction.followup.send(f"**{model.upper()}**: {response}")
    except Exception as e:
        await interaction.followup.send(f"Error: {str(e)}")

# Image analysis command
@bot.tree.command(name="analyze", description="Analyze an image with AI")
async def analyze_command(interaction: discord.Interaction, prompt: str, image: discord.Attachment):
    """Analyze image with AI vision"""
    await interaction.response.defer()
    
    if not image.content_type.startswith('image/'):
        await interaction.followup.send("Please upload a valid image!")
        return
    
    try:
        response = API("sonar-pro", prompt, image_path=image.url)
        await interaction.followup.send(f"**Analysis**: {response}")
    except Exception as e:
        await interaction.followup.send(f"Error: {str(e)}")

# Mention-based interaction
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    # Respond when bot is mentioned
    if bot.user.mentioned_in(message):
        query = message.content.replace(f'<@{bot.user.id}>', '').strip()
        if query:
            async with message.channel.typing():
                response = API("sonar-pro", query)
                await message.reply(response)
    
    await bot.process_commands(message)

bot.run("YOUR_DISCORD_BOT_TOKEN")
```

### Required Modifications for Discord Integration

To use this API with Discord, modify the `API()` function to **return** the response instead of printing:

```python
# Current: print(response_text.choices[0].message.content)
# Modified: return response_text.choices[0].message.content
return response_text.choices[0].message.content
```

### Discord Bot Setup Checklist

- [ ] Install discord.py: `pip install discord.py`
- [ ] Create bot in [Discord Developer Portal](https://discord.com/developers/applications)
- [ ] Enable "Message Content Intent" in Bot settings
- [ ] Get bot token from Developer Portal
- [ ] Modify `API()` function to return responses
- [ ] Set up rate limiting and error handling
- [ ] Add response truncation (Discord has 2000 char limit)
- [ ] Test in development server before production

### Advanced Discord Features (Planned)

- **Conversation History**: Use Discord threads to maintain context
- **Embed Formatting**: Rich embeds with model info and timestamps
- **Permission System**: Restrict certain models to specific roles
- **Usage Analytics**: Track API calls per user/server
- **Caching**: Cache frequent queries to reduce API costs
- **Async Optimization**: Non-blocking API calls for better performance

## API Costs & Limits

Be aware of usage costs and rate limits for each provider:

- **Perplexity**: Check [Perplexity Pricing](https://docs.perplexity.ai/docs/pricing) for current rates
- **Google Gemini**: Review [Gemini Pricing](https://ai.google.dev/pricing) for API costs

## Error Handling

The wrapper includes basic error handling:
- Invalid model names return "Model not supported"
- API errors are raised by the OpenAI SDK
- Network errors are handled by underlying HTTP client

## Contributing

Contributions welcome! Future improvements:
- Async support for concurrent requests
- Response caching
- Token usage tracking
- Streaming responses
- Additional model support

## License

MIT License - feel free to use and modify as needed.

## Resources

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)

---

**Note**: This wrapper is in active development. Discord bot integration coming soon!
