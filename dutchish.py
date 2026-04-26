import re

import pronouncing  # uses CMUdict-style pronunciations


ARPABET_TO_DUTCHISH = {
    # Vowels
    "AA": "a",    # father
    "AE": "e",    # cat, merged with EH
    "AH": "u",    # cup, schwa-like
    "AO": "o",    # law, caught
    "AW": "au",   # now
    "AY": "ai",   # time
    "EH": "e",    # set
    "ER": "ur",   # bird
    "EY": "ee",   # day
    "IH": "i",    # sit
    "IY": "ie",   # see
    "OW": "oo",   # go
    "OY": "oi",   # boy
    "UH": "oe",   # put
    "UW": "oe",   # food

    # Consonants
    "B": "b",
    "CH": "tj",
    "D": "d",
    "DH": "d",
    "F": "f",
    "G": "g",
    "HH": "h",
    "JH": "dj",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "NG": "ng",
    "P": "p",
    "R": "r",
    "S": "s",
    "SH": "sj",
    "T": "t",
    "TH": "th",
    "V": "v",
    "W": "w",
    "Y": "j",
    "Z": "z",
    "ZH": "zj",
}

CONTRACTION_OVERRIDES = {
    "aren't": "arnt",
    "can't": "kent",
    "couldn't": "koedunt",
    "didn't": "didunt",
    "doesn't": "duzunt",
    "don't": "doont",
    "hadn't": "hedunt",
    "hasn't": "hezunt",
    "haven't": "hevunt",
    "isn't": "izunt",
    "shouldn't": "sjoedunt",
    "wasn't": "wazunt",
    "weren't": "wurunt",
    "won't": "woont",
    "wouldn't": "woedunt",
}


def strip_stress(phone: str) -> str:
    """CMUdict vowels may have stress digits: EY1, AH0, IY2, etc."""
    return re.sub(r"\d$", "", phone)


def phones_to_dutchish(phones: str) -> str:
    """
    Convert an ARPABET phone string like
    'B IH0 HH EY1 V Y ER0'
    to our spelling.
    """
    out = []
    for phone in phones.split():
        base = strip_stress(phone)
        if base not in ARPABET_TO_DUTCHISH:
            raise ValueError(f"Unknown ARPABET phone: {phone}")
        out.append(ARPABET_TO_DUTCHISH[base])
    return "".join(out)


def match_case(original: str, converted: str) -> str:
    """Apply the original word's capitalization style to the converted word."""
    letters = re.sub(r"[^A-Za-z]", "", original)
    if not letters:
        return converted
    if len(letters) > 1 and letters.isupper():
        return converted.upper()
    if letters[0].isupper() and (len(letters) == 1 or letters[1:].islower()):
        return converted.capitalize()
    return converted


def normalize_apostrophes(word: str) -> str:
    """Use one apostrophe shape internally so straight and curly input match."""
    return word.replace("’", "'")


def contraction_to_dutchish(word: str) -> str | None:
    normalized = normalize_apostrophes(word.lower())
    if normalized in CONTRACTION_OVERRIDES:
        return match_case(word, CONTRACTION_OVERRIDES[normalized])

    if normalized.endswith("n't"):
        base = normalized[:-3]
        base_pronunciations = pronouncing.phones_for_word(base)
        if base_pronunciations:
            converted = phones_to_dutchish(base_pronunciations[0]) + "unt"
            return match_case(word, converted)

    return None


def word_to_dutchish(word: str) -> str:
    """
    Convert a single English word using the first CMUdict pronunciation.
    Unknown words are returned unchanged in square brackets.
    """
    contraction = contraction_to_dutchish(word)
    if contraction is not None:
        return contraction

    possessive = re.search(r"['’]s$", word.lower()) is not None
    lookup_word = re.sub(r"['’]s$", "", word.lower()) if possessive else word.lower()
    lookup = re.sub(r"[^a-z]", "", lookup_word)
    pronunciations = pronouncing.phones_for_word(lookup)

    if not pronunciations:
        return f"[{word}]"

    converted = phones_to_dutchish(pronunciations[0])
    if possessive:
        converted += "z"
    return match_case(word, converted)


def sentence_to_dutchish(sentence: str) -> str:
    """
    Converts a sentence word-by-word, preserving punctuation.
    """
    parts = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?|[^A-Za-z]+", sentence)
    converted = []

    for part in parts:
        if re.match(r"[A-Za-z]", part):
            converted.append(word_to_dutchish(part))
        else:
            converted.append(part)

    return "".join(converted)
