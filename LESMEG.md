# NB Uttale: Uttaleleksikon med dialektvariasjon

Med skriptet `generate.sh` i dette repoet kan du generere dialektspesifikke versjoner av [NST uttaleleksikon for bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-23/) fra Språkbankens [ressurskatalog](https://www.nb.no/sprakbanken/ressurskatalog/).

## Oppsett

- Forsikre deg om at du har python >= 3.8 installert ([last ned python her](https://www.python.org/downloads/))

- Installer `lexupdater`:

    ```shell
    python -m pip install lexupdater-0.7.5-py3-none-any.whl
    ```

- Last ned SQLite-databasefilen `nst_lexicon_bm.db` med NST uttaleleksikon:

    ```shell
    wget -P data/input https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db
    ```
Mer info om innholdet i databasefilen står [her](#databasefilen).

## Generer uttaleleksikon med dialektvariasjon

``` shell
./generate.sh
```

## Utdata

Utdata er 10 csv-filer som inneholder følgende felter:

| Felt | Beskrivelse |
| --- | --- |
| wordform | Ordform slik den forekommer i bokmålstekst, med `_` istedet for mellomrom |
| pos | Ordklasse (Part-of-speech) |
| feats | Morfologiske trekk |
| wordform_id | Identifikator for ordform. Samme ordform kan ha flere uttalemåter, da vil ID-en gjenta seg. Samme skrivemåte i tekst kan også være forskjellige ord (f.eks. verbet "(jeg) skriver" og substantivet "(en) skriver"), da vil ID-en være forskjellig |
| update_info | Ekstra informasjon om oppslagets kilde. Nyord som legges til her kommer enten fra [Målfrid](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-69/)-korpuset eller [Norsk Aviskorpus](https://www.nb.no/sprakbanken/ressurskatalog/oai-clarino-uib-no-avis-plain/) |
| nofabet_transcription | Uttaletranskripsjon med [NoFAbet](https://github.com/peresolb/g2p-no#transcription-standard)-notasjon |
| ipa_transcription | Uttaletranskripsjon med [IPA](https://no.wikipedia.org/wiki/Det_internasjonale_fonetiske_alfabetet)-notasjon |
| sampa_transcription | Uttaletranskripsjon med [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA)-notasjon |

Filstiene er `data/output/{DIALEKT}_pronunciation_lexicon.csv`, der DIALEKT er en av disse 10:

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

## Databasefilen

Databasefilen har to tabeller, som kan kobles sammen med feltet `unique_id`.

  1. `words`: Indeksen er feltet `word_id`. Inneholder bl.a. ordformer på bokmål (`wordform`), ordklasser (`pos`) og morfologiske trekk (`feats`), samt `unique_id`.
  2. `base`: Indeksen er feltet `pron_id`. Inneholder uttaletranskripsjoner (`nofabet`) på transkripsjonsstandarden NoFAbet. En konverteringstabell mellom [X-SAMPA](https://en.wikipedia.org/wiki/X-SAMPA) og NoFAbet er tilgjengelig [her](https://www.nb.no/sbfil/verktoy/nofa/NoFA-no-1_0.pdf). Har også `unique_id`, som peker til ordformene i `words` som transkripsjonene hører til.

## Kontakt

Har du spørsmål eller problemer med å kjøre koden? Opprett et [issue](https://github.com/Sprakbanken/nb_uttale/issues).
