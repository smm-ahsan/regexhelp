#!/usr/bin/env python3
"""RegexHelp - ready-made regular expressions, explained and testable.

A small library of common validation and matching patterns. Each pattern
comes with a plain-English explanation and an example that matches, and
you can test any string against any pattern from the command line.

Usage:
    python3 regexhelp.py --list
    python3 regexhelp.py email
    python3 regexhelp.py email --test "a.b@example.com"

Standard library only (re).
"""

import re
import sys

# One IPv4 octet: 0-255.
_OCTET = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

# name -> (pattern, explanation, example, mode)
# mode "fullmatch": the whole string must match (validation patterns).
# mode "search":    the pattern may appear anywhere in the string.
PATTERNS = {
    "email": (
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "An email address: a name, an @, a domain, and a top-level "
        "domain of at least two letters.",
        "a.b@example.com",
        "fullmatch",
    ),
    "url": (
        r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?",
        "A web address starting with http:// or https://, with an "
        "optional path after the domain.",
        "https://example.com/page",
        "search",
    ),
    "date": (
        r"[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])",
        "A date in YYYY-MM-DD format, with a real month (01-12) "
        "and day (01-31).",
        "2026-11-10",
        "fullmatch",
    ),
    "time": (
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]",
        "A 24-hour time in HH:MM format, from 00:00 to 23:59.",
        "14:30",
        "fullmatch",
    ),
    "ipv4": (
        _OCTET + r"(?:\." + _OCTET + r"){3}",
        "An IPv4 address: four numbers from 0 to 255 separated by dots.",
        "192.168.0.1",
        "fullmatch",
    ),
    "hexcolor": (
        r"#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})",
        "A hex colour code: a # followed by 3 or 6 hex digits, "
        "like #fff or #1a2b3c.",
        "#1a2b3c",
        "fullmatch",
    ),
    "phone-intl": (
        r"\+[0-9](?: ?[0-9]){6,14}",
        "An international phone number: a leading +, then 7 to 15 "
        "digits, with spaces allowed between digit groups.",
        "+356 9907 3556",
        "search",
    ),
    "username": (
        r"[A-Za-z0-9_]{3,16}",
        "A username: 3 to 16 characters, letters, digits and "
        "underscores only.",
        "cool_user99",
        "fullmatch",
    ),
    "password-strong": (
        r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}",
        "A strong password: at least 8 characters, with an uppercase "
        "letter, a lowercase letter, a digit and a symbol.",
        "Str0ng!Pass",
        "fullmatch",
    ),
    "slug": (
        r"[a-z0-9]+(?:-[a-z0-9]+)*",
        "A URL slug: lowercase words and numbers joined by "
        "single hyphens.",
        "my-first-post",
        "fullmatch",
    ),
}


def main(argv):
    args = argv[1:]

    if not args or "--list" in args:
        for name, (_, explanation, _, _) in PATTERNS.items():
            print(f"{name} - {explanation}")
        return 0

    name = args[0]
    if name not in PATTERNS:
        print(f"error: unknown pattern '{name}'", file=sys.stderr)
        print("Valid names: " + ", ".join(PATTERNS), file=sys.stderr)
        return 2

    pattern, explanation, example, mode = PATTERNS[name]

    if "--test" in args:
        idx = args.index("--test")
        if idx + 1 >= len(args):
            print("error: --test needs a string to test", file=sys.stderr)
            return 2
        text = args[idx + 1]
        regex = re.compile(pattern)
        if mode == "fullmatch":
            match = regex.fullmatch(text)
        else:
            match = regex.search(text)
        if match:
            print(f"MATCH: {match.group(0)}")
        else:
            print("NO MATCH")
        return 0

    print(f"Pattern: {pattern}")
    print(f"Explanation: {explanation}")
    print(f"Example: {example}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
