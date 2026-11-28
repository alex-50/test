"""Подсчёт базовой статистики текста: слова, символы, предложения."""
import argparse
import re

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)
SENTENCE_RE = re.compile(r"[.!?]+")


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def count_words(text):
    return len(WORD_RE.findall(text))


def count_chars(text):
    return len(text)


def count_sentences(text):
    return sum(1 for s in SENTENCE_RE.split(text) if s.strip())


def main():
    parser = argparse.ArgumentParser(description="Статистика текстового файла")
    parser.add_argument("path", help="Путь к текстовому файлу (UTF-8)")
    args = parser.parse_args()

    text = read_file(args.path)
    print(f"Символов: {count_chars(text)}")
    print(f"Слов: {count_words(text)}")
    print(f"Предложений: {count_sentences(text)}")


if __name__ == "__main__":
    main()