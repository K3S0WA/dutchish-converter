import argparse

from dutchish import sentence_to_dutchish


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert English text into a Dutch-ish phonetic spelling."
    )
    parser.add_argument(
        "sentence",
        nargs="*",
        help="English sentence to convert. If omitted, you will be prompted.",
    )
    args = parser.parse_args()

    sentence = " ".join(args.sentence)
    if not sentence:
        sentence = input("English sentence: ")

    print(sentence_to_dutchish(sentence))


if __name__ == "__main__":
    main()
