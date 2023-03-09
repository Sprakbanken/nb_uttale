# nb_uttale

Generer dialektspesifikke versjoner av det tidligere [NST uttaleleksikonet for bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-23/), tilgjengelig fra Språkbankens ressurskatalog.

## Installer `lexupdater`

- Åpne terminalen eller kommandolinjen
  - Krever at python>=3.8 er installert ([last ned python her](https://www.python.org/downloads/))
- Installer lexupdater fra git:

```shell
python -m pip install git+https://github.com/Sprakbanken/lexupdater.git
```

## Databasefilen

NST uttaleleksikon er lastet inn i en SQLite databasefil (`nst_lexicon_bm.db`) med en ordtabell (`words`) og en uttaletabell (`base`).

Last filen ned her, og flytt filen inn i [`data/input`](./data/input/)-mappen:
https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db



Evt. kan du laste ned fila til direkte til mappen via terminalen:

```shell
wget -P data/input https://www.nb.no/sbfil/uttaleleksikon/nst_lexicon_bm.db
```


## Generer uttaleleksikon med dialektvariasjon

``` shell
./generate.sh
```

Skriptet definerer parameterverdier og hvilke prosesser leksikonet går gjennom:

1. Nyord legges til, fra `newwords_2022.csv`-filen i `data/input`.
    - Nyordene som Språkbanken har lagt til har prefikset "NB" foran løpenummeret i `"wordform_id"`
    - Nyordene er hentet fra Norsk Aviskorpus og Målfrid-korpuset. `"update_info"`-feltet indikerer hvilket korpus ordene kommer fra.
2. Dialektvariasjon i uttaletranskripsjonene genereres med regel- og unntaksfiler.
    - Regelfilene `rules_v1.py` og `exemptions_v1.py` er utviklet av Språkbanken 2021-2022.
    - Dialektvariasjonen er generert med regex-mønstre.
3. 10 uttaleleksikon skrives ut: 5 dialektområder med to uttalevarianter per dialekt (talenær og skriftnær).
    - 5 dialektområder: østnorsk (`e`), sørvestnorsk (`sw`), vestnorsk (`w`), trøndersk (`t`), nordnorsk (`n`).
    - Talenær (`spoken`): uttaletranskripsjoner som ligner spontan tale på dialekten
    - Skriftnær (`written`): Uttaletranskripsjoner som ligner høytlesning av bokmålstekst på den gitte dialekten.
