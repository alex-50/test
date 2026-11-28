#!/usr/bin/env python3
"""Подсчёт статистики текста: слова, символы, предложения, топ-слов."""
import argparse
import re
from collections import Counter

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


def top_words(text, n=5):
    words = [w.lower() for w in WORD_RE.findall(text)]
    return Counter(words).most_common(n)


def main():
    parser = argparse.ArgumentParser(description="Статистика текстового файла")
    parser.add_argument("path", help="Путь к текстовому файлу (UTF-8)")
    parser.add_argument("--top", type=int, default=5,
                        help="Сколько топ-слов выводить (по умолчанию 5)")
    args = parser.parse_args()

    text = read_file(args.path)
    print(f"Символов: {count_chars(text)}")
    print(f"Слов: {count_words(text)}")
    print(f"Предложений: {count_sentences(text)}")
    print(f"Топ-{args.top} слов:")
    for word, cnt in top_words(text, args.top):
        print(f"  {word}: {cnt}")


if __name__ == "__main__":
    main()
