from words import get_words
from armenian_alphabet import get_armenian_alphabet_map


def get_letter_info(armenian_word, armenian_lookup):
    english_sound = []
    pronunciation = []
    english_sound_description = []
    for letter in armenian_word:
        if letter == '–':
            # skip there are for words that are added to others and is a special case that i need to handle
            continue
        try:
            english_sound.append(armenian_lookup[letter][0])
            pronunciation.append(armenian_lookup[letter][1])
            english_sound_description.append(armenian_lookup[letter][2])
        except KeyError:
            # TODO: handle this
            # print(f"We couldn't translate the armenian word: {armenian_word} due to letter {letter}")
            return None

    return f"{''.join(pronunciation)} ({armenian_word}) [{' '.join(english_sound_description)}]"


def generate_quizlet_table():
    words_dict = get_words()
    armenian_lookup = get_armenian_alphabet_map()
    total_words_analyzed = 0
    for english_word, armenian_word in words_dict.items():
        front_of_card = english_word
        back_of_card = get_letter_info(armenian_word, armenian_lookup)
        if back_of_card:
            total_words_analyzed += 1
            print(f"{front_of_card}, {back_of_card}")
        else:
            continue

    print(f"Total words analyzed: {total_words_analyzed}")


if __name__ == '__main__':
    generate_quizlet_table()
