from openai import OpenAI
import time
import os

def API(model,user_prompt,image_path=None):
    if(image_path is None):
        messages = [
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
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": image_path}}
                    ]
                }
            ]
    
    if(model=="sonar"):
            client = OpenAI(api_key="Your-API-Key", base_url="https://api.perplexity.ai")
            response_text = client.chat.completions.create(
            model="sonar",
            messages=messages
            )
            print(response_text.choices[0].message.content)

    elif(model=="sonar-pro"):
            client = OpenAI(api_key="Your-API-Key", base_url="https://api.perplexity.ai")
            response_text = client.chat.completions.create(
            model="sonar-pro",
            messages=messages
            )
            print(response_text.choices[0].message.content)

    elif(model=="gemini-2.5-flash"):
        client = OpenAI(api_key="Your-API-Key", base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
        response_text = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages
            )
        print(response_text.choices[0].message.content)
        
    else:
        print("Model not supported.")


if __name__ == "__main__":
    API("sonar-pro",input("Enter Prompt"))
