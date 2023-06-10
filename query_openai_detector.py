import json
import requests
import numpy as np

def query_openaidetector(text, token):
    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Authorization': token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://platform.openai.com',
        'Referer': 'https://platform.openai.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        }
    data = {
        'prompt': text + "».\n<|disc_score|>",
        'max_tokens': 1,
        'temperature': 1,
        'top_p': 1,
        'n': 1,
        'logprobs': 5,
        'stop': '\n',
        'stream': False,
        'model': 'model-detect-v2',
        }
    response = requests.post('https://api.openai.com/v1/completions', headers=header, json=data)
    return response


def translate_openai_output(response):
    possible_classes = ['very unlikely', 'unlikely', 'unclear if it is', 'possibly', 'likely']
    class_max = [10, 45, 90, 98, 99]
    
    choices = response['choices'][0]
    logprobs = choices['logprobs']['top_logprobs'][0]
    key_prob = logprobs.get("!", -10)
    
    final_prob = 100 * (1 - np.e ** key_prob)
    
    for index, value in enumerate(class_max):
        if final_prob <= value:
            return final_prob, possible_classes[index]
    return final_prob, possible_classes[-1]


if __name__ == "__main__":
    # Credit: https://github.com/promptslab/openai-detector
    # Go to https://platform.openai.com/ai-text-classifier
    # Hit F12 to access the Developer tools
    # Select the Network Tab
    # Select nearly any POST Operation (paste text into detection box and click on submit)
    # Find your current Bearer token in the Request Headers
    # Paste your token below
    bearer_token = "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    # Assuming list_of_text contains the text you want to run through OpenAI's detector
    for text in list_of_text:
        try:
            resp = query_openaidetector(text, bearer_token)
            if resp.status_code == 200:
                resp_json = resp.json()
                print(translate_openai_output(resp_json))
            else:
                error_msg = resp.status_code
                print(f"Error: {error_msg}")
        except Exception as e:
            error_msg = str(e)
            print(f"Error: {error_msg}")
