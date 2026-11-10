# Examples

Real output from RegexHelp, captured from actual runs.

## List all patterns

Command:

```bash
python3 regexhelp.py --list
```

Output:

```
email - An email address: a name, an @, a domain, and a top-level domain of at least two letters.
url - A web address starting with http:// or https://, with an optional path after the domain.
date - A date in YYYY-MM-DD format, with a real month (01-12) and day (01-31).
time - A 24-hour time in HH:MM format, from 00:00 to 23:59.
ipv4 - An IPv4 address: four numbers from 0 to 255 separated by dots.
hexcolor - A hex colour code: a # followed by 3 or 6 hex digits, like #fff or #1a2b3c.
phone-intl - An international phone number: a leading +, then 7 to 15 digits, with spaces allowed between digit groups.
username - A username: 3 to 16 characters, letters, digits and underscores only.
password-strong - A strong password: at least 8 characters, with an uppercase letter, a lowercase letter, a digit and a symbol.
slug - A URL slug: lowercase words and numbers joined by single hyphens.
```

## Show one pattern

Command:

```bash
python3 regexhelp.py email
```

Output:

```
Pattern: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
Explanation: An email address: a name, an @, a domain, and a top-level domain of at least two letters.
Example: a.b@example.com
```

## Test an email address

```bash
python3 regexhelp.py email --test "a.b@example.com"
```

```
MATCH: a.b@example.com
```

```bash
python3 regexhelp.py email --test "not-an-email"
```

```
NO MATCH
```

## Test a date (YYYY-MM-DD only)

```bash
python3 regexhelp.py date --test "2026-11-10"
```

```
MATCH: 2026-11-10
```

```bash
python3 regexhelp.py date --test "10-11-2026"
```

```
NO MATCH
```

## Test an IPv4 address (octets must be 0-255)

```bash
python3 regexhelp.py ipv4 --test "999.1.1.1"
```

```
NO MATCH
```

```bash
python3 regexhelp.py ipv4 --test "192.168.0.1"
```

```
MATCH: 192.168.0.1
```

## Test a password

```bash
python3 regexhelp.py password-strong --test "Str0ng!Pass"
```

```
MATCH: Str0ng!Pass
```

```bash
python3 regexhelp.py password-strong --test "weakpass"
```

```
NO MATCH
```

## Find a URL inside a sentence

The url pattern searches inside text instead of validating the whole string:

```bash
python3 regexhelp.py url --test "see https://example.com/page for details"
```

```
MATCH: https://example.com/page
```

## More tests

```bash
python3 regexhelp.py phone-intl --test "+356 9907 3556"
```

```
MATCH: +356 9907 3556
```

```bash
python3 regexhelp.py slug --test "my-first-post"
```

```
MATCH: my-first-post
```

## Unknown pattern name

```bash
python3 regexhelp.py bogus
```

Exits with code 2 and prints:

```
error: unknown pattern 'bogus'
Valid names: email, url, date, time, ipv4, hexcolor, phone-intl, username, password-strong, slug
```
