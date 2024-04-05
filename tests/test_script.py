import string
import pytest

from src.script import count_words_and_sentences


@pytest.fixture
def sample_text_file(tmp_path: string):
    content = "Це тестовий файл. Він містить декілька речень. Це речення один! Це речення два. І ще одне речення три..."
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    return file_path


@pytest.mark.parametrize("expected_word_count, expected_sentence_count", [(18, 5)])
def test_count_words_and_sentences(sample_text_file: object, expected_word_count: int,
                                   expected_sentence_count: int):
    word_count, sentence_count = count_words_and_sentences(sample_text_file)
    assert word_count == expected_word_count
    assert sentence_count == expected_sentence_count
