import requests

# Set the API endpoint and your API key
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=your gemini api key'
headers = {
    'Content-Type': 'application/json',
}
data = {
    "contents": [
        {
            "parts": [
                {
                }
            ]
        }
    ]
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)
result = response.json()

# Check if 'candidates' key exists in the response
if 'candidates' in result:
    # Extract the answer, remove newlines, and make sure it's in one line
    answer = " ".join(result['candidates'][0]['content']['parts'][0]['text'].split())
    
    # Extract the token count
    token_count = result['usageMetadata']['totalTokenCount']
    
    # Print the filtered output
    print(f"Answer: {answer}")
    print(f"Token Count: {token_count}")
else:
    print(f"Error: 'candidates' key not found in the response. Full response: {result}")
