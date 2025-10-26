from openai import OpenAI
import time
import os

def API(model,user_prompt,image_path=None):
    if(image_path is None):
        messages = [
             
                {
                    "role": "system", 
                    "content": [
                         {"type": "text", "text": "You are Sonar, a friendly and helpful AI chatbot. Your goal is to engage in natural, fun conversations with users on any topic. Be witty when it fits, empathetic, and informative. Keep responses concise unless more detail is asked for. Always end with a question to keep the chat going."}]
                },
                {   
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": user_prompt}
                    ]
                }
            ]
    
    else:
        messages = [
                {
                    "role": "system", 
                    "content": [
                         {"type": "text", "text": "extract the content from the image and return primary information in bold characters."}]
                },
                {
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": image_path}}
                    ]
                }
            ]
    
    if(model=="sonar"):
            client = OpenAI(api_key="Your_api_key", base_url="https://api.perplexity.ai")
            response_text = client.chat.completions.create(
            model="sonar",
            messages=messages
            )
            return response_text.choices[0].message.content

    elif(model=="sonar-pro"):
            client = OpenAI(api_key="Your_api_key", base_url="https://api.perplexity.ai")
            response_text = client.chat.completions.create(
            model="sonar-pro",
            messages=messages
            )
            return response_text.choices[0].message.content

    elif(model=="gemini-2.5-flash"):
        client = OpenAI(api_key="your_api_key", base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
        response_text = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages
            )
        return response_text.choices[0].message.content
        
    else:
        return "Model not supported."

    
