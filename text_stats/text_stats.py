"""Подсчёт статистики текста: слова, символы, предложения, топ-слов."""
import argparse
import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)
SENTENCE_RE = re.compile(r"[.!?]+")


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except IsADirectoryError:
        raise IsADirectoryError(f"Указан путь к папке, а не к файлу: {path}")
    except PermissionError:
        raise PermissionError(f"Нет прав на чтение файла: {path}")
    except UnicodeDecodeError as e:
        raise ValueError(f"Не удалось прочитать файл как UTF-8: {e}")

    if not text.strip():
        raise ValueError(f"Файл пустой или содержит только пробелы: {path}")
    return text


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

    try:
        text = read_file(args.path)
    except (FileNotFoundError, IsADirectoryError,
            PermissionError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1

    print(f"Символов: {count_chars(text)}")
    print(f"Слов: {count_words(text)}")
    print(f"Предложений: {count_sentences(text)}")
    print(f"Топ-{args.top} слов:")
    for word, cnt in top_words(text, args.top):
        print(f"  {word}: {cnt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
