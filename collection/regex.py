import re

# match strings that consist of repeating substrings

t = [
    "asdfasdfasdf",
    "axax",
    "xxxxz",
    "yy"
]


matches = [re.search(r"^(.+)\1+$", r) for r in t]
for m in matches:
    if m:
        print(m.group())

