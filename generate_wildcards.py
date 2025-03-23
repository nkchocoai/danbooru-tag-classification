import csv
from collections import defaultdict


def classify_csv(input_file):
    categories = defaultdict(list)

    # CSVを読み取る
    with open(input_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                word, category = row
                categories[category].append(word)

    # カテゴリごとにファイルを作成し、単語を記述
    for category, words in categories.items():
        with open(f"wildcards/{category}.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(words) + "\n")


if __name__ == "__main__":
    classify_csv("classification.csv")
