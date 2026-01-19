from telethon.sync import TelegramClient
import asyncio
import re
import json
import argparse
import sys
import os
import base64

# ASCII Art Banner
BANNER = """
\033[91m⠀⠀⠀⠀⢀⣤⣶⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⢸⣇⣀⣨⣇⣀⣨⡇⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣛⣛⣿⣿⠃⠀⠀⠀
⠀⠀⢀⣠⣽⣿⣿⣿⣿⣿⣄⣀⠀⠀
⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⠘⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋\033[0m

\033[96mCredentials Thief\033[0m \033[90m(ethically ofc)\033[0m
\033[93m════════════════════════════════════════\033[0m
"""

# Obfuscated configuration
_c0nf1g = {
    'a': base64.b64decode('WU9VUl9BUElfSUQ=').decode(),  # YOUR_API_ID (base64)
    'b': base64.b64decode('WU9VUl9BUElfSEFTSA==').decode(),  # YOUR_API_HASH (base64)
    'c': base64.b64decode('K1lPVVJfUEhPTkU=').decode(),  # +YOUR_PHONE (base64)
    'd': base64.b64decode('QGJvdF91c2VybmFtZQ==').decode()  # @bot_username (base64)
}

def _d3c0d3(k):
    """Decode config values"""
    return _c0nf1g.get(k, '')

def _g3t_cr3d3nt14ls():
    """Get credentials from obfuscated config"""
    try:
        _id = _d3c0d3('a')
        _hash = _d3c0d3('b')
        _ph = _d3c0d3('c')
        _bot = _d3c0d3('d')
        return _id, _hash, _ph, _bot
    except:
        return None, None, None, None

class TelegramBreachChecker:
    def __init__(self, _x1, _x2, _x3, _x4, session_name='breach_session'):
        self._x1 = _x1  # api_id
        self._x2 = _x2  # api_hash
        self._x3 = _x3  # phone
        self._x4 = _x4  # bot_username
        self.session_name = session_name
        self.client = None
        self.results = []
    
    async def start(self):
        """Start Telegram client with persistent session"""
        self.client = TelegramClient(self.session_name, self._x1, self._x2)
        
        await self.client.connect()
        
        if not await self.client.is_user_authorized():
            print("\033[93m[*] First time login - you'll need to verify once\033[0m")
            await self.client.start(phone=self._x3)
            print("\033[92m[+] Session saved! No phone verification needed next time.\033[0m")
        else:
            print("\033[92m[+] Connected using saved session (no phone verification needed)\033[0m")
    
    async def check_email(self, email, wait_time=10):
        """Check email via Telegram bot"""
        try:
            import datetime
            sent_time = datetime.datetime.now(datetime.timezone.utc)
            
            await self.client.send_message(self._x4, email)
            print(f"\033[94m[*] Querying target...\033[0m")
            print(f"\033[90m[*] Waiting {wait_time} seconds for response...\033[0m")
            
            await asyncio.sleep(wait_time)
            
            messages = await self.client.get_messages(self._x4, limit=20)
            
            bot_response = None
            for msg in messages:
                if msg.out:
                    continue
                
                if msg.date > sent_time:
                    if "Here are the results" in msg.text or email.lower() in msg.text.lower():
                        bot_response = msg.text
                        break
            
            if not bot_response:
                return {
                    'email': email,
                    'status': 'no_response',
                    'error': 'Bot did not respond in time'
                }
            
            parsed = self._parse_response(bot_response, email)
            parsed['email'] = email
            parsed['raw_response'] = bot_response
            
            self.results.append(parsed)
            return parsed
            
        except Exception as e:
            return {
                'email': email,
                'status': 'error',
                'error': str(e)
            }
    
    def _parse_response(self, response, email):
        """Parse bot response to extract breach data"""
        result = {
            'status': 'unknown',
            'entries': [],
            'total_found': 0
        }
        
        if "Here are the results" in response:
            result['status'] = 'found'
            
            pattern = rf'{re.escape(email)}:([^\n]+)'
            matches = re.findall(pattern, response, re.IGNORECASE)
            
            for match in matches:
                data = match.strip()
                parts = data.split(':')
                password = parts[0] if parts else data
                
                result['entries'].append({
                    'email': email,
                    'password': password
                })
            
            result['total_found'] = len(result['entries'])
        
        elif "not found" in response.lower() or "no results" in response.lower():
            result['status'] = 'clean'
        
        return result
    
    async def check_multiple_emails(self, emails, delay=10):
        """Check multiple emails with delay"""
        results = []
        
        for idx, email in enumerate(emails, 1):
            print(f"\n\033[93m{'='*60}\033[0m")
            print(f"\033[96m[{idx}/{len(emails)}] Checking: {email}\033[0m")
            print(f"\033[93m{'='*60}\033[0m")
            
            result = await self.check_email(email, wait_time=delay)
            results.append(result)
            
            if result['status'] == 'found':
                print(f"\033[91m[!] FOUND {result['total_found']} entries!\033[0m")
                for entry in result['entries'][:5]:
                    print(f"\033[93m    Password: {entry['password']}\033[0m")
            elif result['status'] == 'clean':
                print(f"\033[92m[+] Clean - No breaches found\033[0m")
            else:
                print(f"\033[91m[!] {result.get('error', 'Unknown status')}\033[0m")
            
            if idx < len(emails):
                print(f"\n\033[90m[*] Waiting {delay} seconds before next request...\033[0m")
                await asyncio.sleep(delay)
        
        return results
    
    def print_summary(self):
        """Print detailed summary"""
        print("\n\033[96m" + "="*70 + "\033[0m")
        print("\033[96mTELEGRAM BOT BREACH CHECK - DETAILED SUMMARY\033[0m")
        print("\033[96m" + "="*70 + "\033[0m")
        
        for result in self.results:
            email = result.get('email')
            status = result.get('status')
            
            print(f"\n\033[94m📧 Email: {email}\033[0m")
            print("\033[90m" + "-" * 70 + "\033[0m")
            
            if status == 'found':
                total = result.get('total_found', 0)
                print(f"\033[91m  🔴 STATUS: COMPROMISED ({total} entries found)\033[0m")
                print(f"\n\033[93m  Leaked Credentials:\033[0m")
                
                for idx, entry in enumerate(result['entries'], 1):
                    print(f"\n\033[92m    [{idx}] Password: {entry['password']}\033[0m")
                
            elif status == 'clean':
                print(f"\033[92m  ✅ STATUS: CLEAN (No breaches found)\033[0m")
            
            elif status == 'no_response':
                print(f"\033[93m  ⚠️  STATUS: No response from bot\033[0m")
                print(f"\033[90m  Error: {result.get('error')}\033[0m")
            
            elif status == 'error':
                print(f"\033[91m  ❌ ERROR: {result.get('error')}\033[0m")
            
            if result.get('raw_response'):
                print(f"\n\033[90m  📄 Raw Bot Response:\033[0m")
                print("\033[90m  " + "-" * 66 + "\033[0m")
                for line in result['raw_response'].split('\n')[:15]:
                    print(f"\033[90m  {line}\033[0m")
                if len(result['raw_response'].split('\n')) > 15:
                    print(f"\033[90m  ... ({len(result['raw_response'].split('\n')) - 15} more lines)\033[0m")
    
    def save_results(self, filename='telegram_breach_results.json'):
        """Save results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n\033[92m[+] Results saved to {filename}\033[0m")
    
    def export_passwords_txt(self, filename='found_passwords.txt'):
        """Export all found passwords to text file"""
        with open(filename, 'w') as f:
            for result in self.results:
                if result['status'] == 'found':
                    email = result['email']
                    f.write(f"\n{'='*60}\n")
                    f.write(f"Email: {email}\n")
                    f.write(f"{'='*60}\n")
                    
                    for entry in result['entries']:
                        f.write(f"{email}:{entry['password']}\n")
        
        print(f"\033[92m[+] Passwords exported to {filename}\033[0m")
    
    async def close(self):
        """Close Telegram connection"""
        if self.client:
            await self.client.disconnect()
            print("\n\033[92m[+] Disconnected from Telegram\033[0m")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Telegram Breach Checker - Query breach databases via Telegram bot',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -e test@example.com
  %(prog)s -e email1@test.com -e email2@test.com
  %(prog)s -e test@example.com -w 15
  %(prog)s -f emails.txt
        """
    )
    
    parser.add_argument('-e', '--email', action='append', dest='emails',
                        help='Email address to check (can be used multiple times)')
    
    parser.add_argument('-f', '--file', type=str,
                        help='File containing email addresses (one per line)')
    
    parser.add_argument('-w', '--wait', type=int, default=10,
                        help='Wait time in seconds for bot response (default: 10)')
    
    parser.add_argument('-o', '--output', type=str, default='telegram_breach_results.json',
                        help='Output JSON file (default: telegram_breach_results.json)')
    
    return parser.parse_args()

def load_emails_from_file(filename):
    """Load emails from file"""
    try:
        with open(filename, 'r') as f:
            emails = [line.strip() for line in f if line.strip()]
        return emails
    except FileNotFoundError:
        print(f"\033[91m[!] Error: File '{filename}' not found\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\033[91m[!] Error reading file: {e}\033[0m")
        sys.exit(1)

async def main():
    print(BANNER)
    
    args = parse_arguments()
    
    emails = []
    
    if args.emails:
        emails.extend(args.emails)
    
    if args.file:
        emails.extend(load_emails_from_file(args.file))
    
    if not emails:
        print("\033[91m[!] Error: No emails provided. Use -e or -f option.\033[0m")
        print("\033[90mUsage: python3 telebreach.py -e email@example.com\033[0m")
        print("\033[90m       python3 telebreach.py -f emails.txt\033[0m")
        sys.exit(1)
    
    emails = list(set(emails))
    
    print(f"\033[96m[*] Loaded {len(emails)} email(s) to check\033[0m")
    
    # Get obfuscated credentials
    _id, _hash, _ph, _bot = _g3t_cr3d3nt14ls()
    
    if not all([_id, _hash, _ph, _bot]):
        print("\033[91m[!] Configuration error\033[0m")
        sys.exit(1)
    
    checker = TelegramBreachChecker(_id, _hash, _ph, _bot)
    
    try:
        await checker.start()
        await checker.check_multiple_emails(emails, delay=args.wait)
        checker.print_summary()
        checker.save_results(args.output)
        checker.export_passwords_txt()
        
    except KeyboardInterrupt:
        print("\n\033[93m[!] Interrupted by user\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")
    finally:
        await checker.close()

if __name__ == "__main__":
    asyncio.run(main())
