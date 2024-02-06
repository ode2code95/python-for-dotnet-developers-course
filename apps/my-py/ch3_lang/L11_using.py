import json


def main():
    data = {
        "name": "Stanley",
        "language": "Python",
    }

    with open('file.json', 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=True)

    print("Saved to local file: file.json")


if __name__ == '__main__':
    main()
