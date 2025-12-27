from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

print('client methods:')
print([name for name in dir(client) if not name.startswith('_')])

print('\nclient.models methods:')
print([name for name in dir(client.models) if not name.startswith('_')])

try:
    import inspect
    print('\nclient.generate_content signature:')
    print(inspect.signature(client.generate_content))
except Exception:
    pass
