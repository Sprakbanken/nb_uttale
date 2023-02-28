# nb_uttale

Generer dialektspesifikke versjoner av det tidligere [NST uttaleleksikonet for bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-23/), tilgjengelig fra Språkbankens ressurskatalog.

## Installer `lexupdater`

- Åpne terminalen eller kommandolinjen
  - Krever at python>=3.8 er installert ([last ned python her](https://www.python.org/downloads/))
- Installer lexupdater fra git:

```shell
python -m pip install git+https://github.com/Sprakbanken/lexupdater.git
```

## Last ned databasefilen

- Last ned [`nst_lexicon_bm.db`](https://github.com/Sprakbanken/lexupdater/releases/download/v0.7.0/nst_lexicon_bm.db) fra lexupdater release [v0.7.0](https://github.com/Sprakbanken/lexupdater/releases/tag/v0.7.0)
- Lagre filen i [`data/input`](./data/input/)-mappen.


## Generer uttaleleksikon med dialektvariasjon

**OBS! lexupdater er under debugging.**

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
