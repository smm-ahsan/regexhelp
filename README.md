# RegexHelp

Ready-made regular expressions for common jobs, each one explained in plain English and testable from the command line.

## Patterns

- **email** - an email address: a name, an @, a domain, and a top-level domain of at least two letters
- **url** - a web address starting with http:// or https://, with an optional path
- **date** - a date in YYYY-MM-DD format, with a real month (01-12) and day (01-31)
- **time** - a 24-hour time in HH:MM format, from 00:00 to 23:59
- **ipv4** - an IPv4 address: four numbers from 0 to 255 separated by dots
- **hexcolor** - a hex colour code: #RGB or #RRGGBB
- **phone-intl** - an international phone number: a leading +, then 7 to 15 digits, spaces allowed between digit groups
- **username** - a username: 3 to 16 characters, letters, digits and underscores only
- **password-strong** - a strong password: at least 8 characters with an uppercase letter, a lowercase letter, a digit and a symbol
- **slug** - a URL slug: lowercase words and numbers joined by single hyphens

## Requirements

- Python 3
- Standard library only (the `re` module). Nothing to install.

## Usage

List every pattern with its explanation:

```bash
python3 regexhelp.py --list
```

Show one pattern, its explanation and an example that matches:

```bash
python3 regexhelp.py email
```

Test a string against a pattern:

```bash
python3 regexhelp.py email --test "a.b@example.com"
# MATCH: a.b@example.com

python3 regexhelp.py email --test "not-an-email"
# NO MATCH

python3 regexhelp.py ipv4 --test "999.1.1.1"
# NO MATCH

python3 regexhelp.py ipv4 --test "192.168.0.1"
# MATCH: 192.168.0.1
```

Validation patterns (email, date, time, ipv4, hexcolor, username,
password-strong, slug) must match the whole string. Finder patterns
(url, phone-intl) match anywhere inside the string. An unknown pattern
name exits with code 2 and lists the valid names.

## License

MIT License - see [LICENSE](LICENSE).
