import sys
import json

data = json.load(sys.stdin)

if 'error' in data:
    print('❌ Gemini API Error: ' + data['error'].get('message', 'Unknown error'))
    sys.exit(1)

if 'candidates' not in data or not data['candidates']:
    print('❌ No response from Gemini. Raw response: ' + str(data))
    sys.exit(1)

print(data['candidates'][0]['content']['parts'][0]['text'])