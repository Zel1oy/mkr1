import re


def count_words_and_sentences(filename: object):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Розділяємо текст на слова
    words = re.findall(r'\b\w+\b', text)

    # Розділяємо текст на речення за символами-розподілювачами та закінченнями речень
    sentences = re.split(r'[\.\?!]+', text)

    # Видаляємо порожні рядки зі списку речень (наприклад, якщо речення закінчується кількома знаками пунктуації підряд)
    sentences = [sentence for sentence in sentences if sentence.strip()]

    return len(words), len(sentences)
