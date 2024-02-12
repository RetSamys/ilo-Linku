# Generated from the JSON schema of sona Linku


from typing import Dict, List, Literal, Required, TypedDict, Union

Words = Dict[str, "_WordsAdditionalproperties"]
"""
A raw data object containing dictionary info about Toki Pona words

propertyNames:
  minLength: 1
"""


class _WordsAdditionalproperties(TypedDict, total=False):
    """General info on a Toki Pona word"""

    author_verbatim: Required[str]
    """
    The author's original definition, taken verbatim in their words

    Required property
    """

    author_verbatim_source: Required[str]
    """
    Where the author's original definition is located (usually Discord)

    Required property
    """

    book: Required["_WordsAdditionalpropertiesBook"]
    """
    Which official Toki Pona book was this word featured in, if any.

    Required property
    """

    coined_era: Required["_WordsAdditionalpropertiesCoinedEra"]
    """
    When this word was coined (relative to the publication dates of the official Toki Pona books, if known)

    Aggregation type: anyOf

    Required property
    """

    coined_year: Required[str]
    """
    The year when this word was coined (if known)

    Required property
    """

    creator: Required[List[str]]
    """
    The person who created this word (if known)

    Required property
    """

    ku_data: Dict[str, "_WordsAdditionalpropertiesKuDataAdditionalproperties"]
    """
    The usage data of the word as described in ku (the official Toki Pona dictionary)

    propertyNames:
      minLength: 1
    """

    see_also: Required[List[str]]
    """
    A list of related words

    Required property
    """

    sona_pona: str
    """
    A link to the word's page on sona.pona.la, a Toki Pona wiki. May redirect for words with references but no dedicated page.

    format: uri
    """

    representations: Required["_WordsAdditionalpropertiesRepresentations"]
    """
    Ways of representing this word in the real world, via text/computers

    Required property
    """

    source_language: Required[str]
    """
    The language this word originated from

    Required property
    """

    usage_category: Required["_WordsAdditionalpropertiesUsageCategory"]
    """
    The word's usage category, according to a survey performed by the Linku Project

    Required property
    """

    word: Required[str]
    """
    The word's actual text, in case of a word with multiple definitions (like "we")

    Required property
    """

    etymology: Required[List["_WordsAdditionalpropertiesEtymologyItem"]]
    """
    Unlocalized etymological values regarding this word's origin

    Required property
    """

    audio: Required[List["_WordsAdditionalpropertiesAudioItem"]]
    """ Required property """

    pu_verbatim: "_WordsAdditionalpropertiesPuVerbatim"
    """ The original definition of the word in pu, the first official Toki Pona book """

    usage: Required[Dict[str, "_WordsAdditionalpropertiesUsageAdditionalproperties"]]
    """
    The percentage of people in the Toki Pona community who use this word, according to surveys performed by the Linku Project

    propertyNames:
      pattern: ^20\d{2}-(0[1-9]|1[0-2])$

    Required property
    """

    translations: Required[
        Dict[str, "_WordsAdditionalpropertiesTranslationsAdditionalproperties"]
    ]
    """ Required property """


class _WordsAdditionalpropertiesAudioItem(TypedDict, total=False):
    """Audio files of the words pronounced out loud"""

    author: Required[str]
    """
    The author of the audio file in `link`.

    Required property
    """

    link: Required[str]
    """
    A link to the audio file for the word, pronounced by `author`.

    format: uri

    Required property
    """


_WordsAdditionalpropertiesBook = Union[
    Literal["pu"], Literal["ku suli"], Literal["ku lili"], Literal["none"]
]
""" Which official Toki Pona book was this word featured in, if any. """
_WORDSADDITIONALPROPERTIESBOOK_PU: Literal["pu"] = "pu"
"""The values for the 'Which official Toki Pona book was this word featured in, if any' enum"""
_WORDSADDITIONALPROPERTIESBOOK_KU_SULI: Literal["ku suli"] = "ku suli"
"""The values for the 'Which official Toki Pona book was this word featured in, if any' enum"""
_WORDSADDITIONALPROPERTIESBOOK_KU_LILI: Literal["ku lili"] = "ku lili"
"""The values for the 'Which official Toki Pona book was this word featured in, if any' enum"""
_WORDSADDITIONALPROPERTIESBOOK_NONE: Literal["none"] = "none"
"""The values for the 'Which official Toki Pona book was this word featured in, if any' enum"""


_WordsAdditionalpropertiesCoinedEra = Union[
    "_WordsAdditionalpropertiesCoinedEraAnyof0", Literal[""]
]
"""
When this word was coined (relative to the publication dates of the official Toki Pona books, if known)

Aggregation type: anyOf
"""


_WordsAdditionalpropertiesCoinedEraAnyof0 = Union[
    Literal["pre-pu"], Literal["post-pu"], Literal["post-ku"]
]
_WORDSADDITIONALPROPERTIESCOINEDERAANYOF0_PRE_PU: Literal["pre-pu"] = "pre-pu"
"""The values for the '_WordsAdditionalpropertiesCoinedEraAnyof0' enum"""
_WORDSADDITIONALPROPERTIESCOINEDERAANYOF0_POST_PU: Literal["post-pu"] = "post-pu"
"""The values for the '_WordsAdditionalpropertiesCoinedEraAnyof0' enum"""
_WORDSADDITIONALPROPERTIESCOINEDERAANYOF0_POST_KU: Literal["post-ku"] = "post-ku"
"""The values for the '_WordsAdditionalpropertiesCoinedEraAnyof0' enum"""


class _WordsAdditionalpropertiesEtymologyItem(TypedDict, total=False):
    word: str
    """ One of the root words of this word, as written out in its language of origin """

    alt: str
    """ A latinized representation of the "word" field """


_WordsAdditionalpropertiesKuDataAdditionalproperties = Union[int, float]
"""
The percentage of ku survey respondents who report this translation as accurate to their usage.

minimum: 0
maximum: 100
"""


class _WordsAdditionalpropertiesPuVerbatim(TypedDict, total=False):
    """The original definition of the word in pu, the first official Toki Pona book"""

    en: Required[str]
    """
    The original definition in the English version of pu

    Required property
    """

    fr: Required[str]
    """
    The original definition in the French version of pu

    Required property
    """

    de: Required[str]
    """
    The original definition in the German version of pu

    Required property
    """

    eo: Required[str]
    """
    The original definition in the Esperanto version of pu

    Required property
    """


class _WordsAdditionalpropertiesRepresentations(TypedDict, total=False):
    """Ways of representing this word in the real world, via text/computers"""

    sitelen_emosi: Required["_WordsAdditionalpropertiesRepresentationsSitelenEmosi"]
    """
    The sitelen emosi representation of this word, a script for writing Toki Pona using emoji

    Aggregation type: anyOf

    Required property
    """

    sitelen_pona: Required[List[str]]
    """
    A list of sitelen Lasina representations of this word, to be converted into sitelen pona glyphs

    Required property
    """

    sitelen_sitelen: Required["_WordsAdditionalpropertiesRepresentationsSitelenSitelen"]
    """
    A URL pointing to an image of this word's sitelen sitelen hieroglyphic block

    Aggregation type: anyOf

    Required property
    """

    ucsur: Required["_WordsAdditionalpropertiesRepresentationsUcsur"]
    """
    The word's UCSUR codepoint, as defined in https://www.kreativekorp.com/ucsur/charts/sitelen.html

    Aggregation type: anyOf

    Required property
    """


_WordsAdditionalpropertiesRepresentationsSitelenEmosi = Union[
    "_WordsAdditionalpropertiesRepresentationsSitelenEmosiAnyof0", Literal[""]
]
"""
The sitelen emosi representation of this word, a script for writing Toki Pona using emoji

Aggregation type: anyOf
"""


_WordsAdditionalpropertiesRepresentationsSitelenEmosiAnyof0 = str
""" pattern: ^(\p{Extended_Pictographic}|\p{Emoji_Component})+$ """


_WordsAdditionalpropertiesRepresentationsSitelenSitelen = Union[
    "_WordsAdditionalpropertiesRepresentationsSitelenSitelenAnyof0", Literal[""]
]
"""
A URL pointing to an image of this word's sitelen sitelen hieroglyphic block

Aggregation type: anyOf
"""


_WordsAdditionalpropertiesRepresentationsSitelenSitelenAnyof0 = str
""" format: uri """


_WordsAdditionalpropertiesRepresentationsUcsur = Union[
    "_WordsAdditionalpropertiesRepresentationsUcsurAnyof0", Literal[""]
]
"""
The word's UCSUR codepoint, as defined in https://www.kreativekorp.com/ucsur/charts/sitelen.html

Aggregation type: anyOf
"""


_WordsAdditionalpropertiesRepresentationsUcsurAnyof0 = str
""" pattern: ^U\+[\da-fA-F]{4,6}$ """


class _WordsAdditionalpropertiesTranslationsAdditionalproperties(
    TypedDict, total=False
):
    commentary: Required[str]
    """ Required property """

    definitions: Required[str]
    """
    minLength: 1

    Required property
    """

    etymology: Required[
        List["_WordsAdditionalpropertiesTranslationsAdditionalpropertiesEtymologyItem"]
    ]
    """ Required property """

    sp_etymology: Required[str]
    """ Required property """


class _WordsAdditionalpropertiesTranslationsAdditionalpropertiesEtymologyItem(
    TypedDict, total=False
):
    definition: str
    """ The localized definition of the root word in its origin language """

    language: Required[str]
    """
    The localized name of the language this word originated from

    Required property
    """


_WordsAdditionalpropertiesUsageAdditionalproperties = Union[int, float]
"""
minimum: 0
maximum: 100
"""


_WordsAdditionalpropertiesUsageCategory = Union[
    Literal["core"],
    Literal["widespread"],
    Literal["common"],
    Literal["uncommon"],
    Literal["rare"],
    Literal["obscure"],
]
""" The word's usage category, according to a survey performed by the Linku Project """
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_CORE: Literal["core"] = "core"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_WIDESPREAD: Literal["widespread"] = "widespread"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_COMMON: Literal["common"] = "common"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_UNCOMMON: Literal["uncommon"] = "uncommon"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_RARE: Literal["rare"] = "rare"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
_WORDSADDITIONALPROPERTIESUSAGECATEGORY_OBSCURE: Literal["obscure"] = "obscure"
"""The values for the 'The word's usage category, according to a survey performed by the Linku Project' enum"""
