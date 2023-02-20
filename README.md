# nb_uttale

Generer dialektspesifikke versjoner av det tidligere [NST uttaleleksikonet for bokmål](https://www.nb.no/sprakbanken/ressurskatalog/oai-nb-no-sbr-23/), tilgjengelig fra Språkbankens ressurskatalog.

# Installer nødvendige verktøy

Lexupdater

```shell
python -m pip install lexupdater@git+https://github.com/Sprakbanken/lexupdater.git
```


# Kjør produksjonsskriptet

1. Legg til nyord fra `newwords.csv`
2. Generer dialektvariasjon i uttaletranskripsjonene med regelfiler: `rules.py` og `exemptions.py`
3. Skriv ut dialektspesifikke uttaleleksikon, med to varianter: talenær (uttaletranskripsjoner som ligner spontan tale på dialekten) og skriftnær (for bokmål, dvs. uttaletranskripsjon som ligner høytlesning av bokmålstekst på den gitte dialekten).

