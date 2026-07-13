from rapidfuzz import process


COMMON_WORDS = [
    "library",
    "dorm",
    "dormitory",
    "admission",
    "registration",
    "student",
    "email",
    "wifi",
    "internet",
    "ict"
]


def correct_word(word):

    result = process.extractOne(
        word,
        COMMON_WORDS
    )

    if result:

        match, score, _ = result

        if score >= 70:
            return match

    return word