# 🕷️ TeleBreach - Telegram Breach Checker

<div align="center">

```
⠀⠀⠀⠀⢀⣤⣶⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⢸⣇⣀⣨⣇⣀⣨⡇⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣛⣛⣿⣿⠃⠀⠀⠀
⠀⠀⢀⣠⣽⣿⣿⣿⣿⣿⣄⣀⠀⠀
⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⠘⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋
```

**Automated credential breach checker using Telegram bots**

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Telethon](https://img.shields.io/badge/Telethon-1.24+-green.svg)](https://github.com/LonamiWebs/Telethon)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Examples](#-examples)
- [Output](#-output)
- [Legal Disclaimer](#-legal-disclaimer)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

TeleBreach is an automated reconnaissance tool that leverages Telegram bots to check if email addresses have been compromised in data breaches. It automates the process of querying breach checker bots and parsing their responses to extract credentials.

**Use Case**: Security researchers, penetration testers, and bug bounty hunters can use this tool during the reconnaissance phase to identify compromised credentials associated with target domains (with proper authorization).

---

## ✨ Features

- 🤖 **Automated Telegram Bot Interaction** - No manual querying needed
- 📧 **Batch Email Checking** - Check multiple emails in one run
- 💾 **Persistent Sessions** - Login once, use forever (no repeated 2FA)
- 🎨 **Colored Output** - Easy-to-read terminal output
- 📊 **Multiple Export Formats** - JSON and TXT output files
- ⚡ **Rate Limiting** - Configurable delays to avoid bot rate limits
- 🔒 **Config Obfuscation** - Credentials stored in encoded format
- 📝 **Detailed Logging** - Complete breach information and raw responses

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following:

1. **Python 3.7+** installed
2. **Telegram Account** with phone number
3. **Telegram API Credentials** (API ID and API Hash)
4. **Access to a breach checker Telegram bot**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/telebreach.git
cd telebreach
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**:
```
telethon>=1.24.0
```

Or install manually:
```bash
pip install telethon
```

---

## ⚙️ Configuration

### Step 1: Get Telegram API Credentials

1. Visit [https://my.telegram.org](https://my.telegram.org)
2. Login with your phone number
3. Go to **"API development tools"**
4. Create a new application:
   - **App title**: `TeleBreach` (or any name)
   - **Short name**: `telebreach`
   - **Platform**: `Desktop`
5. Copy your `api_id` and `api_hash`

### Step 2: Generate Obfuscated Config

Run the configuration generator:

```bash
python3 config_generator.py
```

Enter your credentials when prompted:
```
Enter your API_ID: 12345678
Enter your API_HASH: abcdef1234567890abcdef
Enter your PHONE (with +): +212612345678
Enter BOT USERNAME (with @): @your_breach_bot
```

### Step 3: Update telebreach.py

Copy the generated config output and replace the `_c0nf1g` dictionary in `telebreach.py`:

```python
_c0nf1g = {
    'a': base64.b64decode('YOUR_ENCODED_ID').decode(),
    'b': base64.b64decode('YOUR_ENCODED_HASH').decode(),
    'c': base64.b64decode('YOUR_ENCODED_PHONE').decode(),
    'd': base64.b64decode('YOUR_ENCODED_BOT').decode()
}
```

---

## 🚀 Usage

### Basic Usage

Check a single email:
```bash
python3 telebreach.py -e target@example.com
```

### Advanced Usage

```bash
# Check multiple emails
python3 telebreach.py -e email1@test.com -e email2@test.com -e email3@test.com

# Check emails from a file
python3 telebreach.py -f emails.txt

# Custom wait time (useful for slow bots)
python3 telebreach.py -e test@example.com -w 15

# Custom output file
python3 telebreach.py -e test@example.com -o results.json

# Combine options
python3 telebreach.py -f emails.txt -w 20 -o custom_results.json
```

### Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--email` | `-e` | Email address to check (repeatable) | None |
| `--file` | `-f` | File containing emails (one per line) | None |
| `--wait` | `-w` | Wait time for bot response (seconds) | 10 |
| `--output` | `-o` | Output JSON filename | `telegram_breach_results.json` |
| `--help` | `-h` | Show help message | - |

---

## 💡 Examples

### Example 1: Single Email Check

```bash
$ python3 telebreach.py -e john.doe@company.com
```

**Output**:
```
⠀⠀⠀⠀⢀⣤⣶⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
⠀⠀⠀⢸⣇⣀⣨⣇⣀⣨⡇⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣛⣛⣿⣿⠃⠀⠀⠀
⠀⠀⢀⣠⣽⣿⣿⣿⣿⣿⣄⣀⠀⠀
⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⠘⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋

Credentials Thief (ethically ofc)
════════════════════════════════════════

[*] Loaded 1 email(s) to check
[+] Connected using saved session (no phone verification needed)

============================================================
[1/1] Checking: john.doe@company.com
============================================================
[*] Querying target...
[*] Waiting 10 seconds for response...
[!] FOUND 3 entries!
    Password: P@ssw0rd123
    Password: Summer2020!
    Password: Welcome123
```

### Example 2: Batch Check from File

Create `targets.txt`:
```
admin@target.com
info@target.com
support@target.com
contact@target.com
```

Run:
```bash
python3 telebreach.py -f targets.txt -w 12
```

### Example 3: Multiple Email Arguments

```bash
python3 telebreach.py \
  -e admin@company1.com \
  -e admin@company2.com \
  -e security@company3.com \
  -w 15
```

---

## 📤 Output

TeleBreach generates two output files:

### 1. JSON Report (`telegram_breach_results.json`)

```json
[
  {
    "email": "john.doe@example.com",
    "timestamp": "2024-01-20 15:30:45",
    "status": "found",
    "entries": [
      {
        "email": "john.doe@example.com",
        "password": "P@ssw0rd123"
      },
      {
        "email": "john.doe@example.com",
        "password": "Summer2020!"
      }
    ],
    "total_found": 2,
    "raw_response": "Here are the results for your request:\njohn.doe@example.com:P@ssw0rd123\n..."
  }
]
```

### 2. Password List (`found_passwords.txt`)

```
============================================================
Email: john.doe@example.com
============================================================
john.doe@example.com:P@ssw0rd123
john.doe@example.com:Summer2020!
john.doe@example.com:Welcome123
```

---

## 🔧 Troubleshooting

### Issue: "Bot did not respond in time"

**Solution**: Increase wait time with `-w` flag:
```bash
python3 telebreach.py -e test@example.com -w 20
```

### Issue: Session keeps asking for phone code

**Solution**: 
1. Delete existing session: `rm breach_session.session`
2. Run again and complete verification
3. Check file permissions: `chmod 600 breach_session.session`

### Issue: "Configuration error"

**Solution**: 
1. Verify your config is properly base64 encoded
2. Run `config_generator.py` again
3. Ensure all values in `_c0nf1g` dict are correctly copied

### Issue: Rate limiting / Too many requests

**Solution**: 
- Increase delay between requests: `-w 15` or higher
- Add longer pauses between batch runs
- Some bots have daily limits

---

## 📁 Project Structure

```
telebreach/
│
├── telebreach.py           # Main script
├── config_generator.py     # Config generation helper
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
│
├── breach_session.session # Generated session file (gitignored)
├── telegram_breach_results.json  # Output JSON (gitignored)
└── found_passwords.txt    # Output passwords (gitignored)
```

---

## ⚠️ Legal Disclaimer

**THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED SECURITY RESEARCH ONLY**

- ✅ Use ONLY on systems/emails you have **explicit permission** to test
- ✅ Obtain proper **authorization** before security assessments
- ✅ Follow responsible disclosure practices
- ✅ Comply with applicable laws and regulations

**Unauthorized access to computer systems is illegal.**

The authors and contributors are not responsible for misuse or damage caused by this tool. Users are solely responsible for their actions and must ensure compliance with all applicable laws.

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/telebreach.git
cd telebreach
pip install -r requirements.txt
```

---

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)

---

## 📝 TODO

- [ ] Add support for multiple breach checker bots
- [ ] Implement proxy support for anonymity
- [ ] Add CSV export format
- [ ] Create web interface
- [ ] Add password strength analysis
- [ ] Implement threading for faster batch checks
- [ ] Add support for domain-wide email enumeration
- [ ] Integration with other OSINT tools

---

## 🌟 Acknowledgments

- [Telethon](https://github.com/LonamiWebs/Telethon) - Telegram MTProto API library
- Telegram breach checker bot developers
- Security research community

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

Made with ❤️ by security researchers, for security researchers

</div>
```

```
MIT License

Copyright (c) 2024 H1sok444

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
