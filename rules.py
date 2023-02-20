# Replace non-word-initial EH0 with AX0
# B AE2 R EH0 EH3 V N AX0 --> B AE2 R AX0 EH3 V N AX0
errorfix_eh0 = {
    'name': 'errorfix_eh0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'(?<!^)(?<!_) EH0',
        'replacement': r' AX0',
        'constraints': [],
    },
    ]
}

# Replace RNX0 AX0 with R AX0 N AX0
# B AX0 KJ YH1 M RNX0 AX0 --> B AX0 KJ YH1 M R AX0 N AX0
errorfix_rnx0_ax0 = {
    'name': 'errorfix_rnx0_ax0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'(?<!R\w )(?<!(?:A[AE]|EE|II|O[AEO]|UU|YY)\d )R([LN])X0 AX0( S)?$',
        'replacement': r'R AX0 \1 AX0\2',
        'constraints': [
            {
            'field': 'pos',
            'pattern': r'JJ|VB',
            'is_regex': True
            },
        ],
    },
    ]
}

# Replace RNX0 with RN
# B AA2 K AX0 RNX0 --> B AA2 K AX0 RN
errorfix_nasal = {
    'name': 'errorfix_nasal',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(M|NG)( AX0)? RNX0\b',
        'replacement': r'\1 AX0 RN',
        'constraints': [],
    },
    {
        'pattern': r'\bAX0 RNX0( AX0| S| AX0 S)?$',
        'replacement': r'AX0 RN\1',
        'constraints': [],
    },
    ]
}

# Replace AX0 RN AX0 with R AX0 N AX0 for certain words in w and sw
# F IH3 NG AX0 RN AX0 --> F IH3 NG R AX0 N AX0
dialect_nasal_w_sw = {
    'name': 'dialect_nasal_w_sw',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(M|NG) AX0 RN\b',
        'replacement': r'\1 R AX0 N',
        'constraints': [ 
            {
            'field': 'wordform',
            'pattern': r'(fingrene|hamrene|kamrene|numrene|somrene|symrene?|timrene)s?$',
            'is_regex': True
            },
        ],
    },
    ]
}

# Fix transcriptions for "brunsj" and "punch"
# B R OEH1 RN RS --> B R OEH1 N SJ
errorfix_brunsj = {
    'name': 'errorfix_brunsj',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(B R|P) OEH([1-3]) RN SJ\b',
        'replacement': r'\1 OEH\2 N SJ',
        'constraints': [],
    },
    ]
}

# Replace S L with SJ L in "fengsel"
# F EH1 NG S LX0 ---> F EH1 NG SJ LX0
dialect_fengsel = {
    'name': 'dialect_fengsel',
    'areas': ['e_spoken'],
    'rules': [
    {
        'pattern': r'\bF EH([1-3]) N( )?G S( AX0)? L',
        'replacement': r'F EH\1 NG SJ\3 L',
        'constraints': [],
    },
    ]
}

# Replace M AH0 RS J with M AH0 RS
# AH2 N M AH3 RS J --> AH2 N M AH3 RS
errorfix_marsj = {
    'name': 'errorfix_marsj',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bM AH([0-3]) RS J\b',
        'replacement': r'M AH\1 RS',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'rsj',
            'is_regex': True
            },
        ],
    },
    ]
}

# Replace RS with R RS
# R RS is changed to R SJ in w and sw and RS in e, n, and t
# F OAH0 RS OE1 V --> F OAH0 R RS OE1 V
errorfix_rs_to_r_rs = {
    'name': 'errorfix_rs_to_r_rs',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    # Match strings that end with RS
    {
        'pattern': r'(?<!R\w )(?<!R )RS$',
        'replacement': r'R RS',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'rsjs?$',
            'is_regex': True
            },
        ],
    },
    # Match strings with word-medial RS
    {
        'pattern': r'(?<!R\w )(?<!R )RS( \w{2,3}[0-3]| S)',
        'replacement': r'R RS\1',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'rs(c?h|k[iy]|[ks]?j)',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'N AX0 (?:RS|SJ) II([0-3])',
        'replacement': r'N AX0 R RS II\1',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'energi',
            'is_regex': True
            },
        ],
    },
    ]
}

# Replace RS with SJ
# RS EE2 F AX0 RS --> SJ EE2 F AX0 RS
errorfix_rs_to_sj = {
    'name': 'errorfix_rs_to_sj',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b([DFGKLMNPSTV]|NG|NX0) RS\b',
        'replacement': r'\1 SJ',
        'constraints': [],
    },
    {
        'pattern': r'^RS\b',
        'replacement': r'SJ',
        'constraints': [],
    },
    {
        'pattern': r'\bRS L\b',
        'replacement': r'SJ L',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'ssl',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'\b(RT )?RS RS\b',
        'replacement': r'\1RS SJ',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'sk[ijy]|sjou|ssj',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'\bRT RS\b(?! (R\w|SJ))',
        'replacement': r'RT SJ',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'ts(j|kj)',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'(?<!R\w )(?<!R )RS (?!R\w)(\w{2,3}[0-3])',
        'replacement': r'SJ \1',
        'constraints': [
            # Match strings that contain but don't start with "skj"
            {
            'field': 'wordform',
            'pattern': r'(?<!^)skj',
            'is_regex': True
            },
            # Skip all strings with "verseskjema"
            {
            "field": 'wordform',
            "pattern": r'^((?!verseskjema).)*$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace R T with RT
# S AE2 R T R EH3 K --> S AE2 RT R EH3 K
errorfix_rt_r = {
    'name': 'errorfix_rt_r',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR T R\b',
        'replacement': r'RT R',
        'constraints': [],
    },
    ]
}

# Replace N with NX0
# J UH1 NG AX0 L N --> J UH1 NG AX0 L NX0
errorfix_nx0 = {
    'name': 'errorfix_nx0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(AX|EH)([0-3]) L N( S)?$',
        'replacement': r'\1\2 L NX0\3',
        'constraints': [],
    },
    {
        'pattern': r'\b(AA3|OO1) L N$',
        'replacement': r'\1 L NX0',
        'constraints': [],
    },
    ]
}

# Replace RN with RNX0
# F UH2 RT RN RT SJ --> F UH2 RT RNX0 RT SJ
errorfix_rnx0 = {
    'name': 'errorfix_rnx0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bRT RN RT\b',
        'replacement': r'RT RNX0 RT',
        'constraints': [],
    },
    ]
}

# Replace R D with RD
# T AX0 AA1 T AX0 R V AEH3 R D RNX0 --> T AX0 AA1 T AX0 R V AEH3 RD RNX0
errorfix_r_d_rnx0 = {
    'name': 'errorfix_r_d_rnx0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR D RNX0\b',
        'replacement': r'RD RNX0',
        'constraints': [],
    },
    ]
}

# Replace SJ P/T with RS P/RT
# M OO1 T OH0 SJ T OAH3 P --> M OO1 T OH0 RS RT OAH3 P
errorfix_sj_t = {
    'name': 'errorfix_sj_t',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(?:R )?SJ P\b',
        'replacement': r'RS P',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'rs',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'\b(?:R )?SJ T\b',
        'replacement': r'RS RT',
        'constraints': [
            {
            'field': 'wordform',
            'pattern': r'rs',
            'is_regex': True
            },
        ],
    },
    ]
}

# Remove R before RD/RL/RT
# M IH1 N D R AX0 V AEH3 R RD IH0 --> M IH1 N D R AX0 V AEH3 RD IH0
errorfix_r_retro_rd_rl_rt = {
    'name': 'errorfix_r_retro_rd_rl_rt',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR R([DLT])\b',
        'replacement': r'R\1',
        'constraints': [],
    },
    ]
}

# Remove D in feminine definite
# F R II1 T II3 D AH0 --> F R II1 T II3 AH0
errorfix_ida = {
    'name': 'errorfix_ida',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bII3 D AH0( S)?$',
        'replacement': r'II3 AH0\1',
        'constraints': [
            {
            'field': 'feats',
            'pattern': r'FEM',
            'is_regex': True
            },
        ],
    },
    ]
}

# Remove RS in certain transcriptions
# OAH1 RD RNX0 RS RS M EH3 N AX0 S K AX0 --> OAH1 RD RNX0 RS M EH3 N AX0 S K AX0
errorfix_ordensm = {
    'name': 'errorfix_ordensm',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bOAH1 RD RNX0 RS RS M\b',
        'replacement': r'OAH1 RD RNX0 RS M',
        'constraints': [],
    },
    ]
}

# Replace OA with OO
# B II2 L H OA3 RN AH0 --> B II2 L H OO3 RN AH0
errorfix_bilhorn = {
    'name': 'errorfix_bilhorn',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'B II2 L H OA3 RN\b',
        'replacement': r'B II2 L H OO3 RN',
        'constraints': [],
    },
    ]
}

# Replace AEJ with EE G for "veg"
# AEJ is kept for written variants to maintain variation
# B AA2 K V AEJ3 --> B AA2 K V EE3 G
errorfix_veg = {
    'name': 'errorfix_veg',
    'areas': [
        'e_spoken',
        'n_spoken',
        'sw_spoken',
        't_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'\bV AEJ([0-3])\b',
        'replacement': r'V EE\1 G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'veg',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace OEJ with OE G for "høg"
# OEJ is kept for written variants to maintain variation
# H OEJ2 L YH3 T --> H OE2 G L YH3 T
errorfix_hoeg = {
    'name': 'errorfix_hoeg',
    'areas': [
        'e_spoken',
        'n_spoken',
        'sw_spoken',
        't_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'\bH OEJ([0-3])\b',
        'replacement': r'H OE\1 G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'høg',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace RS with SJ
# B AX0 R M UU1 D AH0 RS OA3 RT RS --> B AX0 R M UU1 D AH0 SJ OA3 RT RS
errorfix_shorts = {
    'name': 'errorfix_shorts',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bRS OA3 RT RS\b',
        'replacement': r'SJ OA3 RT RS',
        'constraints': [],
    },
    ]
}

# Replace RNX0 AX0 with AX0 N AX0
# F UU2 R RNX0 AX0 --> F UU2 R AX0 N AX0
errorfix_r_lx0_nx0_rnx0 = {
    'name': 'errorfix_r_lx0_nx0_rnx0',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR RNX0 AX0\b',
        'replacement': r'R AX0 N AX0',
        'constraints': [],
    },
    ]
}

# Replace R RN with RN and RN SJ with RN RS
# UU2 AX0 R RN SJ --> UU2 AX0 RN RS
dialect_r_rn_sj_retro = {
    'name': 'dialect_r_rn_sj_retro',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        't_spoken',
        't_written'],
    'rules': [
    {
        'pattern': r'\bR RN (RS|SJ)$',
        'replacement': r'RN RS',
        'constraints': [],
    },
    {
        'pattern': r'\bR RN AX0 S$',
        'replacement': r'RN AX0 S',
        'constraints': [],
    },
    ]
}

# Replace R RN RS/SJ with R AX0 N S and R RN with R AX0 N
# UU2 AX0 R RN SJ --> UU2 AX0 R AX0 N S
dialect_r_rn_sj = {
    'name': 'dialect_r_rn_sj',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR RN (RS|SJ)$',
        'replacement': r'R AX0 N S',
        'constraints': [],
    },
    {
        'pattern': r'\bR RN AX0 S$',
        'replacement': r'R N AX0 S',
        'constraints': [],
    },
    ]
}

# Replace SJ with RS
# S M OA2 B AA0 RN SJ AH3 L D AX0 RN --> S M OA2 B AA0 RN RS AH3 L D AX0 RN
errorfix_retro_sj = {
    'name': 'errorfix_retro_sj',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\b(R[NT]) SJ NX0\b',
        'replacement': r'\1 RS RNX0',
        'constraints': [],
    },
    {
        'pattern': r'\bRT RN SJ\b',
        'replacement': r'RT RNX0 RS',
        'constraints': [],
    },
    {
        'pattern': r'\bRN SJ ([BDFGJKMNPRV]|SJ?)\b',
        'replacement': r'RN RS \1',
        'constraints': [],
    },
    {
        'pattern': r'\bRN SJ (A[AHX])([0-3])\b',
        'replacement': r'RN RS \1\2',
        'constraints': [
            {
            'field': 'pos',
            'pattern': r'JJ|NN',
            'is_regex': True
            },
        ],
    },
    {
        'pattern': r'\bRN SJ (EH|IH|O(?:A?H|O)|U[HU])([0-3])\b',
        'replacement': r'RN RS \1\2',
        'constraints': [],
    },
    {
        'pattern': r'\bRN SJ AEJ([0-3]) L\b',
        'replacement': r'RN RS AEJ\1 L',
        'constraints': [],
    },
    {
        'pattern': r'\bRN SJ T\b',
        'replacement': r'RN RS RT',
        'constraints': [],
    },
    {
        'pattern': r'\b(R[DLNST]|R[LN]X0) SJ$',
        'replacement': r'\1 RS',
        'constraints': [],
    },
    {
        'pattern': r'\bRNX0 SJ\b',
        'replacement': r'RNX0 RS',
        'constraints': [],
    },
    {
        'pattern': r'\bF J A(EH?|X)([0-3]) RN SJ Y([HY])([0-3]) N\b',
        'replacement': r'F J A\1\2 RN RS Y\3\4 N',
        'constraints': [],
    },
    {
        'pattern': r'\bF AX0 RD SJ LX0\b',
        'replacement': r'F AX0 RD RS LX0',
        'constraints': [],
    },
    {
        'pattern': r'\bRD SJ P IH3 L\b',
        'replacement': r'RD RS P IH3 L',
        'constraints': [],
    },
    {
        'pattern': r'\bSJ RNX0\b',
        'replacement': r'SJ NX0',
        'constraints': [],
    },
    {
        'pattern': r'\bOA1 SJ SJ\b',
        'replacement': r'OA1 RS SJ',
        'constraints': [],
    },
    ]
}

# Replace SJ RL with SJ L
# SJ RL EE2 P EH3 N D NX0 --> SJ L EE2 P EH3 N D NX0
errorfix_sj_rl = {
    'name': 'errorfix_sj_rl',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bSJ RL\b',
        'replacement': r'SJ L',
        'constraints': [],
    },
    ]
}

# Replace R SJ with RS
# J OO2 R SJ EH3 L V --> J OO2 RS EH3 L V
dialect_r_sj_to_rs = {
    'name': 'dialect_r_sj_to_rs',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        't_spoken',
        't_written'],
    'rules': [
    {
        'pattern': r'(?<!R\w )R SJ\b(?! R\w)',
        'replacement': r'RS',
        'constraints': [
            # Skip all strings with "rrs"
            {
            "field": 'wordform',
            "pattern": r'^((?!rrs).)*$',
            "is_regex": True
            },
		],
    },
    ]
}

# Replace R RS with R S/SJ
# R RS is changed to R SJ in sw and w and RS in e, n, and t
# OA2 V AX0 R RS YY3 AH0 --> OA2 V AX0 R SJ YY3 AH0
dialect_r_sj = {
    'name': 'dialect_r_sj',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR RS R([NT])\b',
        'replacement': r'R S \1',
        'constraints': [],
    },
    {
        'pattern': r'\bR RS\b',
        'replacement': r'R SJ',
        'constraints': [],
    },
    ]
}

# Replace R RS with RS
# R RS is changed to R SJ in sw and w and RS in e, n, and t
# OA2 V AX0 R RS YY3 AH0 --> OA2 V AX0 RS YY3 AH0
dialect_r_rs = {
    'name': 'dialect_r_rs',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        't_spoken',
        't_written'],
    'rules': [
    {
        'pattern': r'\bR RS R([NT])\b',
        'replacement': r'RS R\1',
        'constraints': [],
    },
    {
        'pattern': r'\bR RS\b',
        'replacement': r'RS',
        'constraints': [],
    },
    ]
}

# Replace RNX0 with NX0 and RN with R AX0 N
# V IH1 N T AX0 RN --> V IH1 N T AX0 R AX0 N
dialect_rn_def = {
    'name': 'dialect_rn_def',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'(?<!R\w )RS RT RNX0(?:( )R?(S))?$',
        'replacement': r'R S T NX0\1\2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([DT]) RN AX0 RN(?:( )R?(S))?$',
        'replacement': r'R \1 N AX0 R AX0 N\2\3',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([DT]) RNX0(?:( )R?(S))?$',
        'replacement': r'R \1 NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bAX0 RN(?:( )R?(S))?$',
        'replacement': r'AX0 R AX0 N\1\2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RNX0(?:( )R?(S))?$',
        'replacement': r'R AX0 N\1\2',
        'constraints': [],
    },
    ]
}

# Replace all six- and fivegrams with retroflexes only to non-retroflexes
# V AEH1 RD RNX0 RS RS RT J AE3 RN AX0 --> V AEH1 R D NX0 S S T J AE3 RN AX0
dialect_retro_fivegram_sixgram = {
    'name': 'dialect_retro_fivegram_sixgram',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bRS RT RNX0 RS RNX0(( )R(S))?\b',
        'replacement': r'R S T NX0 S NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRD RNX0 RS RS RT\b',
        'replacement': r'R D NX0 S S T',
        'constraints': [],
    },
    {
        'pattern': r'\bRNX0 RT RS RNX0(( )R(S))?\b',
        'replacement': r'R NX0 T S NX0\2\3',
        'constraints': [],
    },
    ]
}

# Replace all fourgrams with retroflexes only to non-retroflexes
# V EH2 L F AX0 RD RS RS RT AA3 T --> V EH2 L F AX0 R D S S T AA3 T
dialect_retro_fourgram = {
    'name': 'dialect_retro_fourgram',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bRD RNX0 R([ST]) R([DNLST])\b',
        'replacement': r'R D NX0 \1 \2',
        'constraints': [],
    },
    {
        'pattern': r'\bRD RNX3 RT RL\b',
        'replacement': r'R D EH3 N T L',
        'constraints': [],
    },
    {
        'pattern': r'\bR([DLS]) R([ST]) RNX0(( )R([ST]))?\b',
        'replacement': r'R \1 \2 NX0\4\5',
        'constraints': [],
    },
    {
        'pattern': r'\bR([DNT]) R([ST]) R([ST]) R([ST])\b',
        'replacement': r'R \1 \2 \3 \4',
        'constraints': [],
    },
    {
        'pattern': r'\bRN RT RS RNX0(( )R(S))?\b',
        'replacement': r'R N T S NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRT RNX0 RS RD(( )R(S))?\b',
        'replacement': r'R T NX0 S D\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRT RNX0 RS RNX0(( )R(S))?\b',
        'replacement': r'R T NX0 S NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRT RNX0 RT(( )R(S))?$',
        'replacement': r'R T NX0 T\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRNX0 RS RNX0(( )R(S))?\b',
        'replacement': r'R NX0 S NX0\2\3',
        'constraints': [],
    },
    ]
}

# Replace all trigrams with retroflexes only to non-retroflexes
# S P OO1 RNX0 RS RT R EH3 K S --> S P OO1 R AX0 N S T R EH3 K S
dialect_retro_trigram = {
    'name': 'dialect_retro_trigram',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bR([DLNST]) R([NST]) R([DLNST])\b',
        'replacement': r'R \1 \2 \3',
        'constraints': [],
    },
    {
        'pattern': r'\bR([DLNST]) R([LNST]) R([LN])X0\b',
        'replacement': r'R \1 \2 \3X0',
        'constraints': [],
    },
    {
        'pattern': r'\bR([DT]) RL RNX1\b',
        'replacement': r'R \1 L EH1 N',
        'constraints': [],
    },
    {
        'pattern': r'\bR([DST]) RNX0 R([DLST])\b',
        'replacement': r'R \1 NX0 \2',
        'constraints': [],
    },
    {
        'pattern': r'\bRNX0 R([ST]) R([ST])\b',
        'replacement': r'R AX0 N \1 \2',
        'constraints': [],
    },
    ]
}

# Replace all bigrams with retroflexes only to non-retroflexes
# F OAH1 RT RS EH3 T AX0 R --> F OAH1 R T S EH3 T AX0 R
dialect_retro_bigram = {
    'name': 'dialect_retro_bigram',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'(?<!R\w )R([DLNST]) R([DLNST])\b(?! R\w)',
        'replacement': r'R \1 \2',
        'constraints': [],
    },
    # TODO: Bruk FA til å sjekke om stavelsesbærende konsonant er riktig her.
    {
        'pattern': r'(?<!R\w )R([DLNST]) R([LN])X0\b(?! R\w)',
        'replacement': r'R \1 \2X0',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([DST]) R([LN])X([1-3])\b(?! R\w)',
        'replacement': r'R \1 EH\3 \2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([LN])X0 R([DLNST])\b(?! R\w)',
        'replacement': r'R AX0 \1 \2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([LN])X0 SJ\b(?! R\w)',
        'replacement': r'R AX0 \1 S',
        'constraints': [],
    },
    ]
}

# Replace all unigrams with retroflexes only to non-retroflexes
# J AE1 RN AX0 --> J AE1 R N AX0
dialect_retro_unigram = {
    'name': 'dialect_retro_unigram',
    'areas': [
        'sw_spoken',
        'sw_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'(?<!R\w )R([DLNST])\b(?! R\w)',
        'replacement': r'R \1',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )R([LN])X0\b(?! R\w)',
        'replacement': r'R AX0 \1',
        'constraints': [],
    },
    ]
}

# Replace some retroflexes with non-retroflexes
# K AH2 RS RT RNX0 RS RNX0 RS --> K AH2 RS RT RNX0 S NX0 S
dialect_retro_e_written = {
    'name': 'dialect_retro_e_written',
    'areas': ['e_written'],
    'rules': [
    #### Six- and fivegrams ####
    {
        'pattern': r'\bRS RT RNX0 RS RNX0(( )R(S))?\b',
        'replacement': r'RS RT RNX0 S NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'\bRD RNX0 RS RS RT\b',
        'replacement': r'R D NX0 S S T',
        'constraints': [],
    },
    #### Fourgrams ####
    {
        'pattern': r'(?<!R\w )RD R(NX0|S) RS R([DNLST])\b(?! R\w)',
        'replacement': r'R D \1 S \2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(R[DS]) (R[ST]) RNX0(( )R(S))?\b(?! R\w)',
        'replacement': r'\1 \2 NX0\4\5',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RL RS RNX0(( )R(S))?\b(?! R\w)',
        'replacement': r'RL S NX0\2\3',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RN RS RT RS\b(?! R\w)',
        'replacement': r'RN RS RT S',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(R[NT]) (R[ST]) RS RT\b(?! R\w)',
        'replacement': r'\1 \2 S T',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RT RNX0 RS R(D|NX0)(( )R(S))?\b(?! R\w)',
        'replacement': r'RT RNX0 S \1\3\4',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RNX0 RS RNX0 RS\b(?! R\w)',
        'replacement': r'RNX0 RS RNX0 S',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RNX0 RT RS RNX0\b(?! R\w)',
        'replacement': r'R AX0 N T S NX0',
        'constraints': [],
    },
    #### Trigrams ####
    {
        'pattern': r'(?<!R\w )(?<!RNX0 )(R[NS]) RS R([DT])\b(?! R\w)',
        'replacement': r'\1 S \2',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(R[NST]) (R[ST]) R([NS])\b(?! R\w)',
        'replacement': r'\1 \2 \3',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RT RS RD\b(?! R\w)',
        'replacement': r'RT RS D',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(?<!AEH[1-3] )RN RS RT\b(?! R\w)',
        'replacement': r'RN RS RT',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RL RS R(NX0|T)\b(?! R\w)',
        'replacement': r'RL S \1',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(?<!RNX0 )(R[NST]) R([LNS]) RNX0\b(?! R\w)',
        'replacement': r'\1 \2 NX0',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RT RNX0 R([DLS])\b(?! R\w)',
        'replacement': r'RT RNX0 \1',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(?<!RNX0 )RS RNX0 RS\b(?! R\w)',
        'replacement': r'RS NX0 S',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RNX0 RS R(NX0|T)\b(?! R\w)',
        'replacement': r'RNX0 S \1',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )RNX0 RT RS\b(?! R\w)',
        'replacement': r'R AX0 N T S',
        'constraints': [],
    },
    #### Bigrams#####
    {
        'pattern': r'(?<!R\w )(?<!RNX0 )RS R([DS])\b(?! R\w)',
        'replacement': r'RS \1',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(?<!RNX0 )RT RS\b(?! R\w)',
        'replacement': r'RT S',
        'constraints': [
            # Skip all strings with "fortsett"
            {
            "field": 'wordform',
            "pattern": r'^((?!fortsett).)*$',
            "is_regex": True
            },
		],
    },
    {
        'pattern': r'(?<!R\w )(R[DLST]) RS$',
        'replacement': r'\1 S',
        'constraints': [],
    },
    {
        'pattern': r'(?<!R\w )(RNX0|RL) R([LS])\b(?! R\w)',
        'replacement': r'\1 \2',
        'constraints': [],
    },
    #### Tri-, bi-, and unigrams that start with /RD/ and are preceeded by ####
    #### a short vowel with stress but aren't proceeded by phonemes that ####
    #### have stress or vowels that are /OAH0/ or long ####
    {
        'pattern': r'\b(\w{1,2}H)([1-3]) RD\b(?! (?:\w{2,3}3|OAH0|(?:A[AE]|EE|II|O[AEO]|UU|YY)0))(?:( )R([LN]X0|[DLNST])(?:( )R([LN]X0|[DLNST]))?)?(?! R\w)',
        'replacement': r'\1\2 R D\3\4\5\6',
        'constraints': [],
    },
    ]
}

# Replace AX0 R AX0 comparative adjective ending with AH0 R in n_spoken
# K OAH2 RT AX0 R AX0 --> K OAH2 RT AH0 R
dialect_ar_comp_adjective = {
    'name': 'dialect_ar_comp_adjective',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R AX0$',
        'replacement': r'AH0 R',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'JJ',
            "is_regex": False
            },
            {
            "field": 'feats',
            "pattern": r'KOM|',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'(?!((?<!sjo)flere|(?<=^)mere))$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace AX0 N AX0 adjective ending with AH0 N AX0 S
# S P EH2 N NX0 AX0 --> S P EH2 N AH0 N AX0 S
dialect_anes_adjective = {
    'name': 'dialect_anes_adjective',
    'areas': [
        'n_spoken',
        'sw_spoken'],
    'rules': [
	{
        'pattern': r'\b(AX0 N|NX0) AX0( S)?$',
        'replacement': r'AH0 N AX0 S',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'JJ|VB',
            "is_regex": True
            },
            {
            "field": 'wordform',
            "pattern": r'endes?$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace AX0 N AX0 adjective ending with AH0 N D AX0
# S P EH2 N NX0 AX0 --> S P EH2 N AH0 N D AX0
dialect_ande_adjective = {
    'name': 'dialect_ande_adjective',
    'areas': ['w_spoken'],
    'rules': [
	{
        'pattern': r'\b(AX0 N|NX0) AX0( S)?$',
        'replacement': r'AH0 N D AX0\2',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'JJ|VB',
            "is_regex": True
            },
            {
            "field": 'wordform',
            "pattern": r'endes?$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Add G after NG in -ng- sequence
# R IH2 NG AX0 --> R IH2 NG G AX0
# S AH1 NG --> S AH1 NG G
# H EH2 NG AX0 --> H EH2 NG G AX0
# B AX0 T OAH1 NG --> B AX0 T OAH1 NG G
# OH2 NG AX0 --> OH2 NG G AX0
dialect_g_plosive_ng = {
    'name': 'dialect_g_plosive_ng',
    'areas': ['w_spoken'],
    'rules': [
	{
        'pattern': r'\b((I[IH])[0-3] )NG(?! [GKDTBPS])',
        'replacement': r'\1NG G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(?<!lign)(?<!sign)(?<!signer)(?<!signekjerr)(?<!signetr)ing(?!ssignal)',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'^((?<!PM).)*$',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b(AH[0-3] )NG(?! [GKDTBPS])',
        'replacement': r'\1NG G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ang(?!ement|eant)',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'^((?<!PM).)*$',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b((AX|E[EH])[0-3] )NG(?! [GKDTBPS])',
        'replacement': r'\1NG G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'eng',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'^((?<!PM).)*$',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b(((OA?|U|Y)H)[0-3] )NG(?! [GKDTBPS])',
        'replacement': r'\1NG G',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[ouy]ng',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'^((?<!PM).)*$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Add D after N in -nd- sequence
# S T R AH1 N --> S T R AH1 N D
# UH1 N AX0 R --> UH1 N D AX0 R
# B OH2 N AX0 --> B OH2 N D AX0
dialect_d_plosive_nd = {
    'name': 'dialect_d_plosive_nd',
    'areas': ['w_spoken'],
    'rules': [
    #### rules that deal with -and- sequences
	{
        'pattern': r'\b(L AH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'land(?!nåm)',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b([HR] AH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[hr]and(?!(granat|nerve[dt]))',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b([BST] AH[0-3] |B AE3 )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[bst]and(?!nes)',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b(AH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[egikp]and',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'^(AH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'^and',
            "is_regex": True
            },
        ],
    },
    #### rules that deal with -und- sequences
    {
        'pattern': r'\b(UH[0-3] )N( AX0 R)\b',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'under',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b([BHLR] UH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[bhlr]und(?!n)',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b([KMST] UH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[kmst]und',
            "is_regex": True
            },
        ],
    },
    #### rules that deal with -end- sequences
    {
        'pattern': r'\b((AX|EH)[0-3] )N (AX0(?!( S)?$)|LX0|IH[0-3] NG)\b',
        'replacement': r'\1N D \3',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'end(e|ing)',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b([LR] EH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[lr]end',
            "is_regex": True
            },
        ],
    },
    #### rules that deal with -ind- sequences
    {
        'pattern': r'\b([BRTV] IH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[brtv]ind',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b(L IH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'lind',
            "is_regex": True
            },
        ],
    },
    #### rule that deals with -ond- sequence
    {
        'pattern': r'\b(OA?H[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(?<!k)(?<!t)(?<!tf)ond(?!(on|heims_))',
            "is_regex": True
            },
        ],
    },
    #### rule that deals with -ånd- sequence
    {
        'pattern': r'\b(OAH[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\2',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ånd(?!n)',
            "is_regex": True
            },
        ],
    },
    #### rule that deals with -ynd- and -ønd- sequences
    {
        'pattern': r'\b((Y|OE)H[0-3] )N($| [^GKTDBPS])',
        'replacement': r'\1N D\3',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'[yø]nd',
            "is_regex": True
            },
        ],
    },
    ]
}

# Add D after L in -ld- sequence
# M EH2 L IH0 NG --> M EH2 L D IH0 NG
# K V EH1 L --> K V EH1 L D
# IH1 L NX0 --> IH1 L D NX0
dialect_d_plosive_ld = {
    'name': 'dialect_d_plosive_ld',
    'areas': ['w_spoken'],
    'rules': [
    {
        'pattern': r'\b(M (EH|AX)[0-3] )L($| [^GKTDBPS])',
        'replacement': r'\1L D\3',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'meld',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b(K [AU]H[0-3]|(J|K V) (EH|AX)[0-3]|(F|H|SJ) OAH[0-3]|YH[0-3]) L($| [^GKTDBPS])',
        'replacement': r'\1 L D\5',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(k[auy]|(gj|kv)e|(f|h|skj)o)ld',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\b((^|AX0|[DKMNST]) IH[0-3] )L($| [^GKTDBPS])',
        'replacement': r'\1L D\3',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(^|[dekmnst])ild',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-er" ending in stem with "-ar" for masculine singular indefinite and definite nouns
# F IH2 S K AX0 R --> F IH2 S K AH0 R
# F IH2 S K AX0 R AX0 N --> F IH2 S K AH0 R AX0 N
dialect_ar_ending_mas_sg = {
    'name': 'dialect_ar_ending_mas_sg',
    'areas': ['sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R( S)?$',
        'replacement': r'AH0 R\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ers?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^SIN\|.*\|MAS$',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\bAX0 R AX0 N( S)?$',
        'replacement': r'AH0 R AX0 N\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'erens?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(SIN\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-ere" ending with "-ara" for masculine plural indefinite nouns
# F IH2 S K AX0 R AX0 --> F IH2 S K AH0 R AH0
dialect_ara_ending_mas_pl_ind = {
    'name': 'dialect_ara_ending_mas_pl_ind',
    'areas': ['sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R AX0( S)?$',
        'replacement': r'AH0 R AH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'eres?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-ere" ending with "-era" for masculine plural indefinite nouns
# F IH2 S K AX0 R AX0 --> F IH2 S K AX0 R AH0
dialect_era_ending_mas_pl_ind = {
    'name': 'dialect_era_ending_mas_pl_ind',
    'areas': ['w_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R AX0( S)?$',
        'replacement': r'AX0 R AH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'eres?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-er" ending with "-a" for masculine plural indefinite nouns
# The rule excludes plural words that end with /AX0 R AX0 R/ since these are erroneous plural forms (*lærerer)
# H EH2 S T AX0 R --> H EH2 S T AH0
# G OH0 R IH1 L AH0 AX0 R --> G OH0 R IH1 L AH0 AH0
# TODO: Use FA to validate whether a double /AH0 AH0/ ending is correct here
dialect_a_ending_mas_pl_ind = {
    'name': 'dialect_a_ending_mas_pl_ind',
    'areas': [
        'sw_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'(?<!AX0 R )AX0 R( S)?$',
        'replacement': r'AH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ers?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^PLU\|.*\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-erne" ending with "-arane" for masculine plural definite nouns
# F IH2 S K AX0 R N AX0 --> F IH2 S K AH0 R AH0 N AX0
dialect_arane_ending_mas_pl_def = {
    'name': 'dialect_arane_ending_mas_pl_def',
    'areas': ['sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R N AX0( S)?$',
        'replacement': r'AH0 R AH0 N AX0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ernes?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-ene" ending with "-ane" for masculine plural definite nouns
# H EH2 S T AX0 N AX0 --> H EH2 S T AH0 N AX0
# F OAH2 L NX0 AX0 --> F OAH2 L AH0 N AX0
# G AH1 L AH0 AX0 N AX0 --> G AH1 L AH0 N AX0
# AH2 NG K LX0 N AX0 S --> AH2 NG K L AH0 N AX0 S
dialect_ane_ending_mas_pl_def = {
    'name': 'dialect_ane_ending_mas_pl_def',
    'areas': [
        'sw_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'\b(AH0 )?((AX|EH)([02]) N|NX([03])) AX0( S)?$',
        'replacement': r'AH\4\5 N AX0\6',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'enes?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
            {
            "field": 'wordform',
            "pattern": r'^((?!(brødrene|bøndene|foreldrene|føttene|mennene|neglene|sønnene|æsene)s?).)*$',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\bLX0 N AX0( S)?$',
        'replacement': r'L AH0 N AX0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'enes?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-e" ending with "-a" for feminine singular indefinite nouns
# J EH2 N T AX0 --> J EH2 N T AH0
dialect_a_ending_fem_sg_ind = {
    'name': 'dialect_a_ending_fem_sg_ind',
    'areas': [
        'sw_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0( S)?$',
        'replacement': r'AH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'es?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^SIN\|.*\|(MAS-)?FEM$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-a" ending with "-å" for feminine singular definite nouns
# J EH2 N T AH0 --> J EH2 N T OAH0
dialect_oa_ending_fem_sg_def = {
    'name': 'dialect_oa_ending_fem_sg_def',
    'areas': ['sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAH0( S)?$',
        'replacement': r'OAH0\1',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(SIN\|.*|\|\|)\|FEM$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-a" ending with "-i" for feminine singular definite nouns
# B YH1 G D AH0 --> B YH1 G D IH0
dialect_i_ending_fem_sg_def = {
    'name': 'dialect_i_ending_fem_sg_def',
    'areas': ['w_spoken'],
    'rules': [
    {
        'pattern': r'\bAH0( S)?$',
        'replacement': r'IH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": (r'((a(rt|vis))'
+                        r'|(b(eit|jørk|lokk|ot|ru|u|ukt|ygd))'
+                        r'|(d(rakt|rift|ør))'
+                        r'|(e(ik|lv))'
+                        r'|(f(art|erd|il|jær|lis|lukt|rakt|uru))'
+                        r'|(g(eit|ift|ran|rav|rein|ren|rend|rind'
+                            r'|rop|røft|ås))'
+                        r'|(h(and|avn|eks|elg|et|ud|ånd))'
+                        r'|ing'
+                        r'|(j(akt|ul))'
+                        r'|(k(ai|lo|løft|raft|ran|u|vern))'
+                        r'|(l(ast|ukt|ykt|yst|øgn|ønn))'
+                        r'|(m(akt|ark|ast|or|t|yr))'
+                        r'|(n(att|emnd|ål))'
+                        r'|pakt'
+                        r'|(r(ad|and|ist|m|o|ogn|ot|ud))'
+                        r'|(s(aft|ag|ak|eng|jel|ki|kje|krift'
+                            r'|kur|kyld|kål|lekt|nor|ol|org'
+                            r'|tang|trand|tri|tund|ynd))'
+                        r'|(t(akk|akt|ann|ekt|id|rakt|rapp|ro|ru|rygd))'
+                        r'|(v(akt|eit|ekt|ik|ogn))'
+                        r'|ætt'
+                        r'|(ø(ks|kt|rn|y))|å)as?$'),
             "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(SIN\|.*|\|\|)\|FEM$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Remove final "r" from feminine plural indefinite nouns
# J EH2 N T AX0 R --> J EH2 N T AX0
dialect_e_ending_fem_pl_ind = {
    'name': 'dialect_e_ending_fem_pl_ind',
    'areas': [
        'sw_spoken',
        'w_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R( S)?$',
        'replacement': r'AX0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'ers?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|(MAS-)?FEM(-MAS)?$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-a" ending with "-å" for neuter plural definite nouns
# H UU1 S AH0 --> H UU1 S OAH0
dialect_oa_ending_neu_pl_def = {
    'name': 'dialect_oa_ending_neu_pl_def',
    'areas': ['sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAH0( S)?$',
        'replacement': r'OAH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'as?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^PLU\|.*\|((MAS|FEM)-)?NEU$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace "-a" ending with "-i" for neuter plural definite nouns
# H UU1 S AH0 --> H UU1 S IH0
dialect_i_ending_neu_pl_def = {
    'name': 'dialect_i_ending_neu_pl_def',
    'areas': ['w_spoken'],
    'rules': [
    {
        'pattern': r'\bAH0( S)?$',
        'replacement': r'IH0\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'as?$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },         
            {
            "field": 'feats',
            "pattern": r'^PLU\|.*\|((MAS|FEM)-)?NEU$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace AX0 infinitive suffix with AH0
# S AEJ2 L AX0 --> S AEJ2 L AH0
dialect_a_infinitive = {
    'name': 'dialect_a_infinitive',
    'areas': [
        'sw_spoken',
        'w_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0$',
        'replacement': r'AH0',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
    ]
}

# Change stressed vowel and/or present tense suffix in four irregular verbs
# J II1 R --> J EE1 R
# S OA1 V AX0 R --> S OE1 V AX0
dialect_irreg_verbs_prs_w_sw = {
    'name': 'dialect_irreg_verbs_prs_w_sw',
    'areas': [
        'w_spoken',
        'sw_spoken'],
    'rules': [
    {
        'pattern': r'\bJ II([13]) R$',
        'replacement': r'J EE\1 R',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'gir$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bJ OE([13]) R$',
        'replacement': r'J EE\1 R AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'gjør$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bH OAH([13]) L( D)? AX0 R$',
        'replacement': r'H EH\1 L\2 AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'holder$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bS OA([13]) V AX0 R$',
        'replacement': r'S OE\1 V AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'sover$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Replace AA R with EE in the present tense irregular verb "har"
# H AA1 R --> H EE1 
dialect_irreg_verb_prs_har = {
    'name': 'dialect_irreg_verb_prs_har',
    'areas': ['sw_spoken'],
    'rules': [
	{
        'pattern': r'\bAA([13]) R$',
        'replacement': r'EE\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'^(inne)?har$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace AX0 R present tense suffix with AH0 in selected a-verbs
# B AH2 NG K AX0 R --> B AH2 NG K AH0
dialect_a_ending_a_verbs_prs_w_sw = {
    'name': 'dialect_a_ending_a_verbs_prs_w_sw',
    'areas': [
        'w_spoken',
        'sw_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R$',
        'replacement': r'AH0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern":(r'(auk'
                        r'|bank'
                        r'|dann|dans|dukk|dykk'
                        r'|elsk|(?<!b)(?<!v)end|endr'
                        r'|fang|farg|film|fisk|frist|frykt'
                        r'|hamn|handl|havn|hent|hevd|hindr'
                            r'|hopp|hugs|husk'
                        r'|jobb'
                        r'|kall|kast|kjemp|klag|klar|kost'
                        r'|lag|lign|likn'
                        r'|mangl|merk|mink|mål'
                        r'|nekt|nytt|nærm'
                        r'|oppdag|oppfatt|oppfordr|ordn'
                        r'|pass|plant'
                        r'|rull'
                        r'|sakn|saml|sats|savn|sikr|skaff'
                            r'|skildr|slutt|snakk|start|støtt'
                            r'|sving|sykl'
                        r'|takk|tegn|tekst'
                        r'|understrek|undr|utfordr|utvikl'
                        r'|varsl|vent|virk|vitn|våkn'
                        r'|(?<!fl)(?<!r)øk)er$'),
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },         
        ],
    },
    ]
}

# Remove R at the end of present tense suffix
# D OEH2 M AX0 R --> D OEH2 M AX0
dialect_e_ending_e_verbs_prs_w_sw = {
    'name': 'dialect_e_ending_e_verbs_prs_w_sw',
    'areas': [
        'w_spoken',
        'sw_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R$',
        'replacement': r'AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Replace AX0 S with AH0 S T in passive infinitive verbs
# D EH2 K AX0 S --> D EH2 K AH0 S T
dialect_ast_ending_pas_inf_verbs = {
    'name': 'dialect_ast_ending_pas_inf_verbs',
    'areas': ['w_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 S$',
        'replacement': r'AH0 S T',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'es$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'(AKT-)?PAS(-AKT)?\|(PRS-)?INF',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace -ene with -en in some plural definite feminine nouns and plural definite nouns with umlaut in n_spoken
# S AA2 K AX0 N AX0 --> S AA2 K AX0 N
# F OEH1 T NX0 AX0 --> F OEH1 T NX0
# T II2 D NX0 AX0 --> T II2 AX0 N
dialect_en_ending_pl_def = {
    'name': 'dialect_en_ending_pl_def',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 N AX0( S)?$',
        'replacement': r'AX0 N\1',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS(-FEM)?$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": (r'((b(lokk|ygd|øk|rødr)ene)'
+                        r'|(d(am|øtr)ene)'
+                        r'|(fruene)'
+                        r'|(gruvene)'
+                        r'|(helgene)'
+                        r'|(kaiene)'
+                        r'|(m(ark|ødr)ene)'
+                        r'|(s(ak|ki|etr)ene))s?$'),
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\bNX0 AX0( S)?$',
        'replacement': r'NX0\1',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS(-FEM)?$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": (r'((bøndene)'
+                        r'|(g(eit|rei?n|rend)ene)'
+                        r'|(vaktene)'
+                        r'|(føttene)'
+                        r'|(h(end|ytt)ene)'
+                        r'|((?<!bet)jentene)'
+                        r'|(mennene)'
+                        r'|((?<!klari)(?<!bajo)(?<!so)(?<!vig)(?<!bru)(?<!falko)(?<!k)(?<!kor)(?<!lorg)(?<!mario)(?<!pa)(?<!no)nettene)'
+                        r'|(platene)'
+                        r'|(røttene)'
+                        r'|((?<!an)tennene)'
+                        r'|((?<!ad)(?<!de)(?<!dri)(?<!gra)(?<!gro)(?<!k)(?<!kal)(?<!kra)(?<!sk)(?<!skro)visene))s?$'),
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\bII(2|3)( D NX0| AX0 N) AX0( S)?$',
        'replacement': r'II\1 AX0 N\3',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS-FEM$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'((?<!k)s|t)idenes?$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace -ene with -an in plural definite nouns in n_spoken and t_spoken
# D AA2 G AX0 N AX0 --> D AA2 G AH0 N
# G UH2 T NX0 AX0 --> G UH2 T AH0 N
# F IH2 S K AX0 RN AX0 --> F IH2 S K AX0 R AH0 N
dialect_an_ending_pl_def = {
    'name': 'dialect_an_ending_pl_def',
    'areas': [
        'n_spoken',
        't_spoken'],
    'rules': [
	{
        'pattern': r'\bAH0 AX0 N AX0( S)?$',
        'replacement': r'AH0 N\1',
        'constraints': [
		{
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
		],
    },
	{
        'pattern': r'\bAX0 N AX0( S)?$',
        'replacement': r'AH0 N\1',
        'constraints': [
		{
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
		],
    },
	{
        'pattern': r'\bNX0 AX0( S)?$',
        'replacement': r'AH0 N\1',
        'constraints': [
		{
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'^((?!(tidene|(?<!ok)sidene)s?).)*$',
            "is_regex": True
            },
		],
    },
		{
        'pattern': r'\bAX0 RN AX0( S)?$',
        'replacement': r'AX0 R AH0 N\1',
        'constraints': [
		{
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'ernes?$',
            "is_regex": True
            },
		],
    },
    ]
}

# Replace -er with -e in plural indefinite feminine nouns in n_spoken
# B YH2 G D AX0 R --> B YH2 G D AX0
# T II2 D AX0 R --> T II2 AX0
dialect_e_ending_pl_ind = {
    'name': 'dialect_e_ending_pl_ind',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R$',
        'replacement': r'AX0',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^PLU\|.*\|MAS(-FEM)?$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": (r'((b(lokk|ygd)er)'
+                        r'|(g(eit|rei?n|rend)er)'
+                        r'|(hytter)'
+                        r'|((?<!bet)jenter)'
+                        r'|(plater)'
+                        r'|((?<!ad)(?<!de)(?<!dri)(?<!gra)(?<!gro)(?<!k)(?<!kal)(?<!kra)(?<!sk)(?<!skro)viser)'
+                        r'|(damer)'
+                        r'|(fruer)'
+                        r'|(gruver)'
+                        r'|(helger)'
+                        r'|(kaier)'
+                        r'|(marker)'
+                        r'|(vakter)'
+                        r'|(saker))$'),
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\bII(2|3)( D)? AX0 R$',
        'replacement': r'II\1 AX0',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^PLU\|.*\|MAS(-FEM)?$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'((?<!ok)s|t)ider$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace sider with sia, sidene with sian and tidene with tian in t_spoken
# S II2 D AX0 R --> S II2 AH0
# T II2 D NX0 AX0 --> T II2 AH0 N
dialect_side_tid_pl = {
    'name': 'dialect_side_tid_pl',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\bII(2|3) D AX0 R$',
        'replacement': r'II\1 AH0',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^PLU\|.*\|MAS(-FEM)?$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'(?<!ok)sider$', 
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\bII(2|3) D NX0 AX0( S)?$',
        'replacement': r'II\1 AH0 N\2',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^(PLU\|.*|\|\|)\|MAS-FEM$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'((?<!ok)s|t)idenes?$',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace -er with -a in plural indefinite masculine and neuter nouns in n_spoken
# B II2 L AX0 R --> B II2 L AH0
# P R OH0 B L EE1 M AX0 R --> P R OH0 B L EE1 M AH0
# L AE2 R AX0 R AX0 --> L AE2 R AX0 R AH0
dialect_a_ending_pl_ind = {
    'name': 'dialect_a_ending_pl_ind',
    'areas': [
        'n_spoken',
        't_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R$',
        'replacement': r'AH0',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^PLU\|.*\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": (r'^.*$'
+                        r'(?<!alter)(?<!anker)'
+                        r'(?<!beger)(?<!bøker)(?<!bønder)'
+                        r'(?<!døtrer)'
+                        r'(?<!filter)(?<!foster)(?<!føtter)'
+                        r'(?<!gelender)(?<!gitter)'
+                        r'(?<!(?<!subtra)hender)'
+                        r'(?<!kammer)(?<!kloster)'
+                        r'(?<!lager)'
+                        r'(?<!meter)(?<!monster)(?<!mødrer)(?<!mønster)'
+                        r'(?<!(?<!klari)(?<!bajo)(?<!so)(?<!vig)(?<!bru)(?<!falko)(?<!k)(?<!kor)(?<!lorg)(?<!mario)(?<!pa)(?<!no)netter)(?<!nummer)'
+                        r'(?<!(?<!st)offer)(?<!orkester)'
+                        r'(?<!plaster)(?<!pulver)'
+                        r'(?<!register)'
+                        r'(?<!(?<!ak)(?<!do)(?<!dos)(?<!du)(?<!interes)(?<!pro)(?<!recen)(?<!rekonvale)(?<!tras)(?<!vi)senter)(?<!siffer)(?<!spekter)(?<!søstrer)'
+                        r'(?<!teater)(?<!(?<!an)tenner)(?<!tider)(?<!tømmer)'),
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\bR AX0$',
        'replacement': r'R AH0',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'NN',
            "is_regex": False
            },
			{
            "field": 'feats',
            "pattern": r'^PLU\|.*\|(NEU|(NEU-)?MAS(-FEM)?)$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": (r'^.*$'
+                        r'(?<!altre)(?<!ankre)'
+                        r'(?<!begre)(?<!brødre)'
+                        r'(?<!døtre)'
+                        r'(?<!fedre)(?<!filtre)(?<!fostre)'
+                        r'(?<!gelendre)(?<!gitre)'
+                        r'(?<!kamre)(?<!klostre)'
+                        r'(?<!lagre)'
+                        r'(?<!metre)(?<!monstre)(?<!mødre)(?<!mønstre)'
+                        r'(?<!numre)'
+                        r'(?<!ofre)(?<!orkestre)'
+                        r'(?<!plastre)'
+                        r'(?<!registre)'
+                        r'(?<!sentre)(?<!sifre)(?<!spektre)(?<!søstre)'
+                        r'(?<!teatre)(?<!tømre)'),
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace OAH0 with OEH0 in unstressed for- and -for in n_spoken
# F OAH0 R EH1 L D AX0 R --> F OEH0 R EH1 L D AX0 R
dialect_o_lowering = {
    'name': 'dialect_o_lowering',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'^F OAH0 R',
        'replacement': r'F OEH0 R',
        'constraints': [],
    },
	{
        'pattern': r'\bF OAH(0|3) R$',
        'replacement': r'F OEH\1 R',
        'constraints': [],
    },
	{
        'pattern': r'^F OAH1 R$',
        'replacement': r'F OEH1 R',
        'constraints': [
		{
            "field": 'wordform',
            "pattern": r'for',
            "is_regex": False
            },
		],
    },
    ]
}

# Replace YH with OEH in n_spoken and t_spoken
# F R YH2 K T AX0 L IH0 --> F R OEH2 K T AX0 L IH0
dialect_y_lowering = {
    'name': 'dialect_y_lowering',
    'areas': [
        'n_spoken',
        't_spoken'],
    'rules': [
	{
        'pattern': r'\bYH([1-3])',
        'replacement': r'OEH\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": (r'^(((be|ut)?nytt(e(t|r|ne?)?|a|ig(e(re)?|ste?)?))'
+                        r'|(bryst(e(r|t|ne)|a)?)'
+                        r'|(lykt(a|e(ne?|r))?)'
+                        r'|(lyst(a|e(ne?|r))?)'
+                        r'|(fryktelig(e(re)?|ste?)?)'
+                        r'|(syng(er?)?)'
+                        r'|((ut|inn)?trykk(e(r|t|ne?)?|te?|a)?)'
+                        r'|(yng(re|ste?)))$'),
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace EH/EE with AEH/AE in n_spoken
# V EH2 L D IH0 --> V AEH2 L D IH0
# B AX0 V EE1 G AX0 --> B AX0 V AE1 G AX0
dialect_e_lowering = {
    'name': 'dialect_e_lowering',
    'areas': [
        'n_spoken',
        't_spoken'],
    'rules': [
	{
        'pattern': r'\bE(E?)(H?)([1-3])',
        'replacement': r'AE\2\3',
        'constraints': [
		{
            "field": 'wordform',
            "pattern": (r'^((beveg(e(r|t|lse(ne?|r)?)?|a|de?)?)'
+                        r'|(etter(på)?)'
+                        r'|(fest(e(r|t|ne?)?|a)?)'
+                        r'|(i?gjennom)'
+                        r'|(heftig(e(re)?|ste?)?)'
+                        r'|(hjelp(e(r|ne?)?|a)?)'
+                        r'|(kjeft(e(ne?|r|t)?|a)?)'
+                        r'|(rett(e(re?|t|ne?|ste?)?|a)?)'
+                        r'|(sent(rum(et)?|er(et)?|r(e(t|ne)?|a(ene)?)))'
+                        r'|(s(pel(l(e|et|ene|er|a)?|te?)|lepp(e|er|en|et|ene|a)?))'
+                        r'|(stjel(er?)?)'
+                        r'|(tjen(e(r|ste(ne?|r)?)?|te?)?)'
+                        r'|(tre(ff(e(r|t|ne)?|a)?|n(e(r((ne)?|en?)?)?|ing(e(ne?|r)|a)?)?))'
+                        r'|(veldige?)'
+                        r'|(venn(e(ne?|r))?))$'),
             "is_regex": True
        },
        ],
    },
	{
        'pattern': r'\bEH([0-3]) (G|K|NG|S T|M)',
        'replacement': r'AEH\1 \2',
        'constraints': [],
    },
    ]
}

# Replace IH with EH in n_spoken
# F IH1 S K --> F EH1 S K
dialect_i_lowering_n_spoken = {
    'name': 'dialect_i_lowering_n_spoken',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bIH([1-3])',
        'replacement': r'EH\1',
        'constraints': [
		{
            "field": 'wordform',
            "pattern": (r'^((cirka)'
+                        r'|(drikk(e(r|ne?)?)?)'
+                        r'|(f(isk(e(r|ne?)?)?|risk(e(re|st)?|t)?|ing(er(en)?|re(r|ne)?)))'
+                        r'|(klipp(ing|e(r|ne?)?)?)'
+                        r'|(mitt)'
+                        r'|(oversikt(e(r|ne?)|a)?)'
+                        r'|(sikt(e(r|ne?)|a)?)'
+                        r'|(snitt(e(t|ne)|a)?)'
+                        r'|(strikk(e(r|t)?|a)?)'
+                        r'|(u?forsiktig(e(re)?|st)?)'
+                        r'|(u?sik(kert?|r(e(t|re|st)?|a)))'
+                        r'|(virk(elige?|er|et|a))'
+                        r'|(viss(te?)?))$'),
             "is_regex": True
            },
		],
    },
	{
        'pattern': r'\bJ IH([1-3]) T$',
        'replacement': r'J EH\1 T',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'gitt$',
            "is_regex": True
            },
			{
            "field": 'pos',
            "pattern": r'VB|JJ',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace IH with EH in t_spoken
# F IH1 S K --> F EH1 S K
dialect_i_lowering_t_spoken = {
    'name': 'dialect_i_lowering_t_spoken',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\bIH([1-3])',
        'replacement': r'EH\1',
        'constraints': [
		{
            "field": 'wordform',
            "pattern": (r'^((f(isk(e(r|ne?)?)?|risk(e(re|st)?|t)?))'
+                        r'|(strikk(e(r|t)?|a)?)'
+                        r'|(u?sik(kert?|r(e(t|re|st)?|a)))'
+                        r'|(virk(elige?|er|et|a))'
+                        r'|(viss(te?)?))$'),
             "is_regex": True
            },
		],
    },
    ]
}

# Replace IH with AEH in n_spoken and t_spoken
# S P IH2 L AX0 --> S P AEH2 L AX0
dialect_i_to_ae_lowering = {
    'name': 'dialect_i_to_ae_lowering',
    'areas': [
        'n_spoken',
        't_spoken'],
    'rules': [
	{
        'pattern': r'\bIH(1|2)',
        'replacement': r'AEH\1',
        'constraints': [
		{
            "field": 'wordform',
            "pattern": r'^s(pil(l(e|et|ene|er|a)?|te?)|lipp(e|er|en|et|ene|a)?)$',
             "is_regex": True
            },
		],
    },
    ]
}

# Replace AA with AE in "fare" (verb) in n_spoken
# F AA2 R AX0 --> F AE2 R AX0
dialect_a_lowering = {
    'name': 'dialect_a_lowering',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'^F AA(1|2) R AX0( R)?$',
        'replacement': r'F AE\1 R AX0\2',
        'constraints': [
			{
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace T with D in past participle in n_spoken
# F OAH1 T --> F OAH1 D
dialect_t_voicing = {
    'name': 'dialect_t_voicing',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bT$',
        'replacement': r'D',
        'constraints': [
            {
            "field": 'pos',
            "pattern": r'VB|JJ',
            "is_regex": True
            },
			{
            "field": 'feats',
            "pattern": r'^((?!IMP).)*$',
            "is_regex": True
            },
			{
            "field": 'wordform',
            "pattern": r'(b(edt|litt)|dratt|f(ødt|ått)|g(itt|ått)|(?<!for)hatt|nødt|(?<!saman)sett|s(l|t)ått|(?<!ers)tatt)$',
            "is_regex": True
            },
        ],
    },
    ]
}	
	
# Remove infinitive suffix in n_spoken
# H OAH2 P AX0 --> H OAH2 P
dialect_apocope_inf_n = {
    'name': 'dialect_apocope_inf_n',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\b([BDFGKLMNPSTV]|NG) R AX0$',
        'replacement': r'\1 AX0 R',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\b([BDFGKLMNPST] [LN]) AX0$',
        'replacement': r'\1X0',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r'\b(NG|V) L AX0$',
        'replacement': r'\1 LX0',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
	{
        'pattern': r' AX0$',
        'replacement': r'',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
    ]
}

# Replace AX0 R present tense suffix with AH0 in selected a-verbs
# B AH2 NG K AX0 R --> B AH2 NG K AH0
dialect_a_ending_a_verbs_prs_n = {
    'name': 'dialect_a_ending_a_verbs_prs_n',
    'areas': ['n_spoken'],
    'rules': [
    {
        'pattern': r'\bAX0 R$',
        'replacement': r'AH0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern":(r'(amm|auk'
                        r'|bad|bank'
                        r'|dann|dans|dusj|dukk|dykk'
                        r'|elsk|(?<!b)(?<!v)end'
                        r'|fang|farg|film|fisk|flytt|frist|frykt'
                        r'|havn|hent|hevd|hopp|hugs|husk'
                        r'|jobb'
                        r'|kall|kast|kjemp|klag|klar|kost'
                        r'|lag|lign|likn'
                        r'|merk|mink|mål'
                        r'|nekt|nytt|nærm|ny'
                        r'|oppdag|oppfatt|oppfordr|ordn'
                        r'|pass|plant'
                        r'|rull|ro'
                        r'|sats|savn|sikr|skaff|slutt|'
                            r'snakk|start|støtt|sving'
                        r'|takk|tegn|tekst'
                        r'|understrek|utfordr'
                        r'|varsl|vent|vi|virk'
                        r'|(?<!fl)(?<!r)øk)er$'),
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },         
        ],
    },
    {
        'pattern': r'\b([BDFGKLMNPST] [LNR]|(NG|V) [LR]) AX0 R$',
        'replacement': r'\1 AH0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },         
        ],
    },
    ]
}

# Change stressed vowel and remove present tense suffix in irregular verbs
# L EE1 S AX0 R --> L AE1 S
# S OA1 V AX0 R --> S OE1 V
dialect_irreg_verbs_prs_n = {
    'name': 'dialect_irreg_verbs_prs_n',
    'areas': ['n_spoken'],
    'rules': [
    {
        'pattern': r'\bE(E|(H))([13]) ([LST]) AX0 R$',
        'replacement': r'AE\2\3 \4',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(dett|les|selg|sett|sprett)er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bOA([13]) V AX0 R$',
        'replacement': r'OE\1 V',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'sover$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Remove present tense suffix AX0 R
# D OEH2 M AX0 R --> D OEH2 M
dialect_apocope_e_verbs_prs = {
    'name': 'dialect_apocope_e_verbs_prs',
    'areas': ['n_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R$',
        'replacement': r'',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": (r'(an|avtal'
                        r'|bak|begynn|bestemm|betal|bind|bit|blås'
                            r'|brenn|bruk|bryt|bråk|bygg|bær|bøy'
                        r'|dekk|drei|drep|drikk|drit|driv|drypp|drømm'
                        r'|ei|et'
                        r'|fall|finn|flyt|forklar|frys|funger|fyll|fød|føl|følg|før'
                        r'|gjeld|gjemm|glemm|grav|grei|grin|grip|gråt'
                        r'|hei?t|hend|heng|hils|hiv|hjelp|hold|hør|håp'
                        r'|kall|kjenn|kjøp|kjør|klar|klemm|klyp|kok|kos|krev|kryp'
                        r'|lag|legg|lei|lei?k|lei?t|lev|lever|lik|lov|lur|lyg|lys|lær|lønn|løp|løs|lån'
                        r'|mal|meld|mei?n|minn|møt|mål|nevn'
                        r'|pei?k|plei|prøv|reis|rekk|renn|ring|riv|rop'
                        r'|send|si|sitt|skap|skill|skinn|skit|skjelv|skjær|skjønn'
                            r'|skrik|skriv|skyt|slipp|slit|smak|smett|smil|snyt|spar|spill'
                            r'|spis|sprekk|spring|stek|stell|stemm|stikk|still|stjel'
                            r'|strekk|stryk|styr|svar|svik|svømm|syng|synk|søk|søl'
                        r'|tap|tell|tenk|tenn|tjen|treff|trekk|tren|treng|tømm|tål'
                        r'|var|vei|vend|vinn|vis|voks|vurder'
                        r'|yt|øver)er$'),
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Remove final AX0 in past tense e-verbs in n_spoken
# KJ OE2 P T AX0 --> KJ OE2 P T
dialect_apocope_e_verbs_prt_n = {
    'name': 'dialect_apocope_e_verbs_prt_n',
    'areas': ['n_spoken'],
    'rules': [
    {
        'pattern': r'\bRD AX0$',
        'replacement': r'R',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'gjorde$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'PRT',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'([TDLN]) AX0$',
        'replacement': r'\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(?<!bl)(?<!vill)e$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'PRT',
            "is_regex": True
            },
        ],
    },
    ]
}

# Remove infinitive suffix in t_spoken
# H OAH2 P AX0 --> H OAH2 P
dialect_apocope_inf_t = {
    'name': 'dialect_apocope_inf_t',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\b((?<![BDFGKLMNPSTV] [LNR])(?<!NG [LR])) AX0$',
        'replacement': r'\1',
        'constraints': [
            {
            "field": 'feats',
            "pattern": r'INF',
            "is_regex": True
            },
        ],
    },
    ]
}

# Remove present tense suffix and/or change stressed vowel in irregular verbs
# B AE1 R AX0 R --> B AE1 R
# G R AA2 V AX0 R --> G R AE2 V
# H OAH1 L AX0 R --> H EH1 L
# S OA1 V AX0 R --> S OE1 V
dialect_irreg_verbs_prs_t = {
    'name': 'dialect_irreg_verbs_prs_t',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\b AX0 R$',
        'replacement': r'',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(bind|bit|brenn|bryt|bær'
                        r'|drikk|drit|driv|drypp'
                        r'|(?<!gj)(?<!h)(?<!l)et'
                        r'|finn|flyt|frys'
                        r'|gjeld|grin|grip'
                        r'|hiv'
                        r'|klyp|kryp'
                        r'|(?<!s)legg|lyg'
                        r'|rekk|renn|riv|ryk'
                        r'|sitt|si|skinn|skit|skjelv|skjær|skrik|skriv'
                            r'|skryt|skyt|slipp|slit|smett|snyt|sprekk'
                            r'|spring|stikk|stjel|stryk|svik|syng|synk'
                        r'|treff|trekk|(?<!s)treng'
                        r'|vik|(?<!t)vinn'
                        r'|(?<!ø)yt)er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\b(AA|EE|OA|(E|OA)(H))([13]) ((K )?[FLPSTV]) AX0 R$',
        'replacement': r'AE\3\4 \5',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(blås|dett|drep|grav|gråt|les|selg|sett|sprett|voks)er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bO?AH([0-3]) L AX0 R$',
        'replacement': r'EH\1 L',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(fall|hold)er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    {
        'pattern': r'\bOA([13]) V AX0 R$',
        'replacement': r'OE\1 V',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'sover$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Remove R at the end of present tense suffix
# D OEH2 M AX0 R --> D OEH2 M AX0
dialect_e_ending_prs = {
    'name': 'dialect_e_ending_prs',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\bAX0 R$',
        'replacement': r'AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'er$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Remove final AX0 in past tense e-verbs in t_spoken
# KJ OE2 P T AX0 --> KJ OE2 P T
dialect_apocope_e_verbs_prt_t = {
    'name': 'dialect_apocope_e_verbs_prt_t',
    'areas': ['t_spoken'],
    'rules': [
	{
        'pattern': r'\bL T AX0$',
        'replacement': r'RT',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(hæ|ju|kjø|ma|må|pu|ta)lte$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'PRT',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\bRD AX0$',
        'replacement': r'R',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'gjorde$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'PRT',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'([TDLN]) AX0$',
        'replacement': r'\1',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(?<!bl)(?<!vill)e$',
            "is_regex": True
            },
            {
            "field": 'feats',
            "pattern": r'PRT',
            "is_regex": True
            },
        ],
    },
    ]
}

# Remove T at the end of participle
# F UH2 N AX0 T --> F UH2 N AX0
dialect_irreg_verbs_participle = {
    'name': 'dialect_irreg_verbs_participle',
    'areas': [
        't_spoken',
        'n_spoken'],
    'rules': [
	{
        'pattern': r'\b[EI]H([1-3]) (G|T) AX0 T$',
        'replacement': r'OH\1 \2 AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": r'(dett|ligg|sitt|sprett)et$',
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": True
            },
        ],
    },
    {
        'pattern': r'\bAX0 T$',
        'replacement': r'AX0',
        'constraints': [
            {
            "field": 'wordform',
            "pattern": (r'(bund|drev|drukk|funn|grep|hjulp'
                        r'|komm|krøp|løy|pep|rev'
                        r'|skrek|skrev|skjøv|slupp|sov'
                            r'|sprukk|sprung|stukk|stjål'
                            r'|strukk|strøk|svek|sung'
                        r'|truff|trukk|tvung|vunn)et$'),
            "is_regex": True
            },
            {
            "field": 'pos',
            "pattern": r'VB',
            "is_regex": False
            },
        ],
    },
    ]
}

# Replace OJ phoneme with OAJ
# J OJ1 K --> J OAJ1 K
errorfix_oj_to_oaj = {
    'name': 'errorfix_oj_to_oaj',
    'areas': [
        'e_spoken',
        'e_written',
        'n_spoken',
        'n_written',
        'sw_spoken',
        'sw_written',
        't_spoken',
        't_written',
        'w_spoken',
        'w_written'],
    'rules': [
    {
        'pattern': r'\bOJ',
        'replacement': r'OAJ',
        'constraints': [],
    },
    ]
}

