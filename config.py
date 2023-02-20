"""Configure input parameters for the lexicon generation."""

DATABASE = "data/input/nst_lexicon_bm.db"
"""Path to the backend db"""

OUTPUT_DIR = "data/output"
"""Path to the output folder for the lexica"""

RULES_FILE = "data/input/rules.py"
"""Path to file with pronunciation replacement rulesets for dialect updates.

Note that multiple rules may affect the same  pronunciations,
and that the ordering of the rules may matter.

"areas" is the list of dialects which should be affected by the rule.
    Dialect names are specified in config.py.

"name" is the name of the ruleset.
    These should be unique, and are mapped to exemption words.

"rules" contains a list of replacement rules.
    Each rule consists of
    "pattern", which is a regex pattern for a certain transcription,
    "replacement" which is a string to replace the pattern with,
    and "constraints", an optional list of dicts constraining
    the replacement only to words with given metadata.
    In the constraints dicts,
        "field" gives the word metadata field (corresponding to fields in the
        NST lexicon),
        "pattern" is the pattern that should be matched in the field,
        either a regex or a literal,
        and "is_regex", which should be True if the pattern is a regex and
        False otherwise.

Note that multiple rules may affect the same pronunciations,
and that the ordering of the rules may be of importance for the result.
"""

EXEMPTIONS_FILE = "data/input/exemptions.py"
"""Path to file with exemptions:

List of dicts with words to be exempted from the specified rulesets.
"""

DIALECTS = [
    "e_spoken",
    "e_written",
    "sw_spoken",
    "sw_written",
    "w_spoken",
    "w_written",
    "t_spoken",
    "t_written",
    "n_spoken",
    "n_written",
]
"""List of dialects which update rules can target.

Corresponds to names of pronunciation temp tables created in the backend db.
"""

NEWWORDS_PATH = "data/input/newwords.csv"
"""A directory or file path to csv file(s) containing new words, their transcriptions + metadata."""
