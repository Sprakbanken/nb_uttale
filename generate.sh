#!/usr/bin/env bash

# KONFIGURER INNDATA-FILSTI
DIR="data/input"

# GENERER UTTALELEKSIKA MED DIALEKTVARIASJONER
lexupdater -v \
    --database "${DIR}/nst_lexicon_bm.db" \
    --newword-files "${DIR}/newwords_2022.csv" \
    --dialects e_spoken \
        -d e_written \
        -d sw_spoken \
        -d sw_written \
        -d w_spoken \
        -d w_written \
        -d t_spoken \
        -d t_written \
        -d n_spoken \
        -d n_written \
    update \
        --rules-file "${DIR}/rules_v1.py" \
        --exemptions-file "${DIR}/exemptions_v1.py" \
        --output-dir "data/output" \
