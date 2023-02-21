#!/usr/bin/env bash


# KONFIGURER PARAMETERVERDIER
DIR="data/input"
UTDIR="data/output"
DB="${DIR}/nst_lexicon_bm.db"
NYORD="${DIR}/newwords_2022.csv"
DIALEKTER="e_spoken,e_written,sw_spoken,sw_written,w_spoken,w_written,t_spoken,t_written,n_spoken,n_written"
REGLER="${DIR}/rules_v1.py"
UNNTAK="${DIR}/exemptions_v1.py"
UTPREFIKS="nb_uttale_bm"
TRANSKRIPSJONSSTANDARDER="ipa,sampa,nofabet"

# GENERER UTTALELEKSIKA MED DIALEKTVARIASJONER
lexupdater -v -db $DB -o $UTDIR \
    insert -n $NYORD \
    update -d $DIALEKTER -r $REGLER -e $UNNTAK -op $UTPREFIKS \
    #convert --standard=$TRANSKRIPSJONSSTANDARDER
