# NB Uttale: Pronunciation lexicon with dialectal variation for Norwegian

[![lang-button](https://img.shields.io/badge/-Norsk-blue)](https://github.com/Sprakbanken/nb_uttale/blob/main/LESMEG.md) [![lang-button](https://img.shields.io/badge/-English-grey)](https://github.com/Sprakbanken/nb_uttale/blob/main/README.md)

This repo contains a script and data to generate pronunication lexica with dialect variation for spoken Norwegian, and with wordforms in the bokmål written standard.

The base lexicon is [NST Pronunciation Lexicon for Norwegian Bokmål](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-23/) from the Norwegian Language Bank's [resource catalogue](https://www.nb.no/sprakbanken/en/resource-catalogue/).

## Requirements

- Ensure you have python >= 3.8 installed ([download python here](https://www.python.org/downloads/))

- Install `lexupdater`:

    ```shell
    python -m pip install lexupdater-0.7.5-py3-none-any.whl
    ```

- Download the SQLite database file `nst_lexicon_bm.db`:

    ```shell
    wget -P data/input https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db
    ```

For more info on the database file, see [here](#database-file).

## Generate pronunciation lexica

``` shell
./generate.sh
```

In case you get "Permission denied" to run the script, change your user permissions:

```shell
chmod 700 generate.sh
```

## Output

The script writes 10 csv files to file paths `data/output/{DIALECT}_pronunciation_lexicon.csv`, where DIALECT is one of the following 10:

- e_spoken
- e_written
- n_spoken
- n_written
- sw_spoken
- sw_written
- t_spoken
- t_written
- w_spoken
- w_written

The files contain these columns:

| Column | Description |
| --- | --- |
| wordform | Wordform as it appears in bokmål text. Underscore (`_`) replaces whitespaces in multiword expressions |
| pos | Part-of-speech |
| feats | Morphological features |
| wordform_id | Wordform identificator. When the same wordform has several possible transcriptions, the wordform_id is repeated. When a wordform is repeated and represent different grammatical/lexical concepts, the wordform_id is different. E.g. the verb "jeg skriver" (_I write_) vs. the noun "en skriver" (_a printer_) |
| update_info | Reference to the data source. |
| nofabet_transcription | Transcription with the [NoFAbet](https://github.com/peresolb/g2p-no#transcription-standard)  notation |
| ipa_transcription | Transcription with the [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) notation |
| sampa_transcription | Transcription with the [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) notation |

The conversion from NoFAbet to the other transcription standards is done with code from [Sprakbanken/convert_nofabet](https://github.com/Sprakbanken/convert_nofabet).

## Parameters

The script explicitly sets input arguments and flags to configure the process that the lexicon is going through with the `lexupdater update` command:

Parameter | Description
--- | ---
`-v, -vv` | Verbosity of the output log written to `stdout`. `-v` includes `INFO` messages, and `-vv` includes `DEBUG` messages. All logging messages are written to `data/output/log.txt` regardless of this flag.
`-db, --database` |  File path to the SQLite database file with the NST lexicon.
`-n, --newwords-path` | File path to a csv file with new word records to add. Each new word (row) in the file gets a `wordform_id` with the prefix "NB" and a count number.
`-d, --dialects` | Categories of pronunciation variation that the transcriptions are updated for. The command writes 1 csv file for each argument given by this flag.
`-r, --rules-file` | Python file with ruleset `dict` objects. The dialectal variation is generated with regex patterns and replacement strings, as well as constraints.
`-e, --exemptions-file` | Python file with `dict`-objects indicating words that should be ignored by a given ruleset.


## Files in `data/input`

These files have been developed by linguists in the Norwegian Language Bank 2021-2022.

Filename | Description
--- | ---
`newwords_2022.csv` | Each row contains the wordform (`token`), an East Norwegian `transcription`, up to 3 `alternative_transcription`s, the `pos`-tag and `morphology` features of the word. These words come from the [Målfrid corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-69/) or the [Norwegian Newspaper Corpus Bokmål](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-clarino-uib-no-avis-plain/), which is indicated in the `update_info` field.
`rules_v1.py` | The Norwegian Language Bank has developed transformation rules for 5 Norwegian dialectal areas: East (`e`), South-West (`sw`), West (`w`), Trøndelag (`t`), North (`n`). There are 2 variants per dialect: `spoken` transcriptions are close to spontaneous speech in the given dialect, and `written` transcriptions are closer to the pronunciation of a bokmål manuscript being read out loud in the given dialect.
`exemptions_v1.py` | Specific words that should be ignored by rulesets defined in `rules_v1.py`. The ruleset `name` values map to the exemption `ruleset` values.

## Database file

The SQLite file has two tables, which can be joined with the `unique_id` field.

Table | Description
--- | ---
`words` | The index is `word_id`. Contains wordforms in bokmål (`wordform`), part-of-speech (`pos`), and morphological features (`feats`), as well as `unique_id`, and more.
`base` | The index is `pron_id`. Contains pronunciation transcriptions for East Norwegian (`nofabet`). A mapping between the [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) transcription standard and the NoFAbet notation can be found [here](https://www.nb.no/sbfil/verktoy/nofa/NoFA-en-1_0.pdf). Values in `unique_id` maps to the transcription's written wordform in `words`.

## Contact

If you have questions, suggestions or problems running the code, please [create an issue](https://github.com/Sprakbanken/nb_uttale/issues).
