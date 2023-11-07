import re

from pytest import mark

url = "https://twitter.com/kip"

username = re.sub(r"^(http?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

