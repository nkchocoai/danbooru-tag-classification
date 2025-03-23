# usage: python extract_general.py > general.txt

import csv

tags = []
# danbooru_20241109.csv : https://github.com/DominikDoom/a1111-sd-webui-tagcomplete/blob/6ffeeafc49256106266922989ffe8b6b5ef4981f/tags/danbooru.csv
with open("danbooru_20241109.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        tag, type_, count, alias = row
        if type_ == "0":
            tags.append(tag)

print("\n".join(tags))
