# NB Uttale: Uttaleleksikon med dialektvariasjon

[![lang-button](https://img.shields.io/badge/-Norsk-grey)](https://github.com/Sprakbanken/nb_uttale/blob/main/LESMEG.md) [![lang-button](https://img.shields.io/badge/-English-blue)](https://github.com/Sprakbanken/nb_uttale/blob/main/README.md)

Dette repoet inneholder skript og data for å generere dialektspesifikke versjoner av [NST uttaleleksikon for bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-23/) fra Språkbankens [ressurskatalog](https://www.nb.no/sprakbanken/ressurskatalog/).

## Oppsett

- Opprett et virtuelt miljø i python og installer konverteringsverktøyet `lexupdater`, f.eks. med `uv` eller `pdm`:

    ```shell
    # UV
    uv sync

    # PDM
    pdm install
    ```

- Last ned SQLite-databasefilen [`nst_lexicon_bm.db`](https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db) med NST uttaleleksikon:

    ```shell
    wget -P data/input https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db
    ```

Mer info om innholdet i databasefilen står [her](#databasefilen).

## Generer uttaleleksikon med dialektvariasjon

``` shell
./generate.sh
```

Hvis du får "Permission denied" til å kjøre skriptet, endre brukertillatelsene dine og prøv igjen:

```shell
chmod 700 generate.sh
```

## Utdata

Utdata er 10 csv-filer som heter `data/output/{DIALEKT}_pronunciation_lexicon.csv`, der DIALEKT er en av disse 10 (Se [her](#inndatafilene-i-datainput) for mer info om dialektene):

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


Filene inneholder følgende felter:

| Felt | Beskrivelse |
| --- | --- |
| wordform | Ordform slik den forekommer i bokmålstekst, med `_` i stedet for mellomrom |
| pos | Ordklasse (Part-of-speech) |
| feats | Morfologiske trekk |
| wordform_id | Identifikator for ordform. Samme ordform kan ha flere uttalemåter, da vil ID-en gjenta seg. Samme skrivemåte i tekst kan også være forskjellige ord (f.eks. verbet "(jeg) skriver" og substantivet "(en) skriver"), da vil ID-en være forskjellig |
| update_info | Ekstra informasjon om oppslagets kilde |
| nofabet_transcription | Uttaletranskripsjon med [NoFAbet](https://github.com/peresolb/g2p-no#transcription-standard)-notasjon |
| ipa_transcription | Uttaletranskripsjon med [IPA](https://no.wikipedia.org/wiki/Det_internasjonale_fonetiske_alfabetet)-notasjon |
| sampa_transcription | Uttaletranskripsjon med [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA)-notasjon |

Konverteringen fra NoFAbet til de andre transkripsjonsstandardene er gjort med kode fra [Sprakbanken/convert_nofabet](https://github.com/Sprakbanken/convert_nofabet).


## Parameterverdier

Skriptet definerer parameterverdier for inndata og hvilke prosesser leksikonet går gjennom med `lexupdater update`-kommandoen:

Parameter | Beskrivelse
--- | ---
`-v, -vv` | Ordrikhet (av eng. "verbosity") i loggen som skrives til terminalen. Alle logg-meldinger skrives til `data/output/log.txt` uansett.
`-db, --database` |  Databasefilen med NST-leksikonet.
`-n, --newwords-path` | En CSV-fil med nyord, én eller flere transkripsjoner, samt ordklasse og morfologiske trekk. Nyord som legges til får en `"wordform_id"` i utdata med prefikset "NB" og et løpenummer.
`-d, --dialects` | Uttalevariantene som transkripsjonene skal oppdateres for. Utdata er én fil per verdi som angis med dette flagget.
`-r, --rules-file` | python-fil med regelsett-`dict`-objekter. Dialektvariasjonen er generert med regex-mønstre og "søk-erstatt"-transformasjoner.
`-e, --exemptions-file` | python-fil med `dict`-objekter som angir hvilke ord et regelsett skal ignorere.

## Inndatafilene i [`data/input/`](https://github.com/Sprakbanken/nb_uttale/tree/main/data/input)

Filene med inndata brukes til å oppdatere bokmålsordlisten og de østnorske transkripsjonene i [databasefilen](#databasefilen). De har blitt utviklet av lingvister i [Språkbanken](https://www.nb.no/sprakbanken/) ved Nasjonalbiblioteket 2021-2022.

Filnavn | Beskrivelse
--- | ---
`newwords_2022.csv` | Nyordene er hentet fra [Målfrid-korpuset](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-69/) og [Norsk Aviskorpus](https://www.nb.no/sprakbanken/ressurskatalog/oai-clarino-uib-no-avis-plain/).
`rules_v1.py` | Transkripsjonsoppdateringene er utviklet for 5 dialektområder: østnorsk (`e`), sørvestnorsk (`sw`), vestnorsk (`w`), trøndersk (`t`), nordnorsk (`n`). I tillegg har hvert dialektområde 2 uttalevarianter. Talenære (`spoken`) transkripsjoner ligner spontan tale på dialekten. Skriftnære (`written`) transkripsjoner ligner høytlesning av bokmålstekst på den gitte dialekten.
`exemptions_v1.py` | Ordlister som er unntak fra transformasjonsreglene.

## Databasefilen

`nst_lexicon_bm.db` har to tabeller, som kan kobles sammen med feltet `unique_id`.

Tabell | Beskrivelse
---  | ---
`words` | Indeksen er feltet `word_id`. Inneholder bl.a. ordformer på bokmål (`wordform`), ordklasser (`pos`) og morfologiske trekk (`feats`), samt `unique_id`.
`base` | Indeksen er feltet `pron_id`. Inneholder uttaletranskripsjoner (`nofabet`) på transkripsjonsstandarden NoFAbet. En konverteringstabell mellom [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) og NoFAbet er tilgjengelig [her](https://www.nb.no/sbfil/verktoy/nofa/NoFA-no-1_0.pdf). Har også `unique_id`, som peker til ordformene i `words` som transkripsjonene hører til.

Tilbake til [Oppsett](#oppsett).

## Kontakt

Har du spørsmål eller problemer med å kjøre koden? [Opprett et issue](https://github.com/Sprakbanken/nb_uttale/issues/new)