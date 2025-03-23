import csv


def add_classification(danbooru_file, classification_file, output_file):
    classification_dict = {}
    with open(classification_file, newline="", encoding="utf-8") as classfile:
        reader = csv.reader(classfile)
        for row in reader:
            if len(row) == 2:
                classification_dict[row[0]] = row[1]

    with open(danbooru_file, newline="", encoding="utf-8") as danboorifile, open(
        output_file, "w", newline="", encoding="utf-8"
    ) as outputfile:
        reader = csv.reader(danboorifile)
        writer = csv.writer(outputfile)

        for row in reader:
            if row:
                category = classification_dict.get(row[0], "")
                writer.writerow(row + [category])


if __name__ == "__main__":
    # danbooru_20241109.csv : https://github.com/DominikDoom/a1111-sd-webui-tagcomplete/blob/6ffeeafc49256106266922989ffe8b6b5ef4981f/tags/danbooru.csv
    add_classification(
        "danbooru_20241109.csv",
        "classification.csv",
        "danbooru_20241109_with_classification.csv",
    )
