# Optional ONLY if you include the config information in the script

import base64

def generate_config():
    """Generate obfuscated config"""
    print("="*60)
    print("Telegram Breach Checker - Config Generator")
    print("="*60)
    
    api_id = input("\nEnter your API_ID: ").strip()
    api_hash = input("Enter your API_HASH: ").strip()
    phone = input("Enter your PHONE (with +): ").strip()
    bot_username = input("Enter BOT USERNAME (with @): ").strip()
    
    # Encode to base64
    encoded_id = base64.b64encode(api_id.encode()).decode()
    encoded_hash = base64.b64encode(api_hash.encode()).decode()
    encoded_phone = base64.b64encode(phone.encode()).decode()
    encoded_bot = base64.b64encode(bot_username.encode()).decode()
    
    print("\n" + "="*60)
    print("Copy this into your telebreach.py file:")
    print("="*60)
    print(f"""
_c0nf1g = {{
    'a': base64.b64decode('{encoded_id}').decode(),
    'b': base64.b64decode('{encoded_hash}').decode(),
    'c': base64.b64decode('{encoded_phone}').decode(),
    'd': base64.b64decode('{encoded_bot}').decode()
}}
""")
    print("="*60)

if __name__ == "__main__":
    generate_config()
