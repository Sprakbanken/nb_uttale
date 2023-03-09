# NB Uttale: Pronunciation lexicon with dialectal variation for Norwegian

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
| update_info | Extra information about the data source. New words that are added here come from the [Målfrid corpus](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-69/) or the [Norwegian Newspaper Corpus Bokmål](https://www.nb.no/sprakbanken/en/resource-catalogue/oai-clarino-uib-no-avis-plain/) |
| nofabet_transcription | Transcription with the [NoFAbet](https://github.com/peresolb/g2p-no#transcription-standard)  notation |
| ipa_transcription | Transcription with the [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) notation |
| sampa_transcription | Transcription with the [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) notation |

## Parameterverdier

Skriptet definerer parameterverdier for inndata og hvilke prosesser leksikonet går gjennom med `lexupdater update`-kommandoen:

Parameter | Beskrivelse
--- | ---
`-v, -vv` | Ordrikhet (av eng. "verbosity") i loggen, som skrives til `data/output/log.txt`
`-db, --database` |  Databasefilen med NST-leksikonet.
`-n, --newwords-path` | Nyord legges til fra `data/input/newwords_2022.csv`-filen. Nyordene som Språkbanken har lagt til har prefikset "NB" foran løpenummeret i `"wordform_id"`. Nyordene er hentet fra Norsk Aviskorpus og Målfrid-korpuset. `"update_info"`-feltet indikerer hvilket korpus ordene kommer fra.
`-d, --dialects` | Uttalevariantene som transkripsjonene skal oppdateres for. Utdata er én fil per verdi som angis med dette flagget. Språkbanken har utviklet regler for 5 dialektområder (østnorsk (`e`), sørvestnorsk (`sw`), vestnorsk (`w`), trøndersk (`t`), nordnorsk (`n`) ) og to uttalevarianter per dialekt. Talenære (`spoken`) transkripsjoner ligner spontan tale på dialekten. Skriftnære (`written`) transkripsjoner ligner høytlesning av bokmålstekst på den gitte dialekten.
`-r, --rules-file` | python-fil med regelsett-`dict`-objekter. Dialektvariasjonen er generert med regex-mønstre og "søk-erstatt"-transformasjoner. Regelfilene `rules_v1.py` og `exemptions_v1.py` er utviklet av Språkbanken 2021-2022.
`-e, --exemptions-file` | python-fil med `dict`-objekter som angir hvilke ord et regelsett skal ignorere.

## Database file

Databasefilen har to tabeller, som kan kobles sammen med feltet `unique_id`.

  1. `words`: Indeksen er feltet `word_id`. Inneholder bl.a. ordformer på bokmål (`wordform`), ordklasser (`pos`) og morfologiske trekk (`feats`), samt `unique_id`.
  2. `base`: Indeksen er feltet `pron_id`. Inneholder uttaletranskripsjoner (`nofabet`) på transkripsjonsstandarden NoFAbet. En konverteringstabell mellom [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) og NoFAbet er tilgjengelig [her](https://www.nb.no/sbfil/verktoy/nofa/NoFA-no-1_0.pdf). Har også `unique_id`, som peker til ordformene i `words` som transkripsjonene hører til.

## Kontakt

Har du spørsmål eller problemer med å kjøre koden? Opprett et [issue](https://github.com/Sprakbanken/nb_uttale/issues).
