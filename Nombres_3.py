# coding: utf-8

import typing
import collections
import bs4




# structure de données double, un dictionnaire central et une hiérarchie de contraintes
lexique_1 = {
    "word_zero": {
        "graphie": {
            "_C": {
                "M": "zéro",
                "F": "zéro"
            },
            "_V": {
                "M": "zéro",
                "F": "zéro"
            },
            "_#": {
                "M": "zéro",
                "F": "zéro"
            },
            "_add": {
                "M": "Ø",
                "F": "Ø"
            },
            "_mul": {
                "M": "Ø",
                "F": "Ø"
            },
            "_latin": {
                "M": "Ø",
                "F": "Ø"
            }
        },
        "phonologie": {
            "_C": {
                "M": "zeRo",
                "F": "zeRo"
            },
            "_V": {
                "M": "zeRo",
                "F": "zeRo"
            },
            "_#": {
                "M": "zeRo",
                "F": "zeRo"
            },
            "_add": {
                "M": "Ø",
                "F": "Ø"
            },
            "_mul": {
                "M": "Ø",
                "F": "Ø"
            },
            "_latin": {
                "M": "Ø",
                "F": "Ø"
            }
        }
    },
    "word_un": {
        "graphie": {
            "_C": {
                "M": "un",
                "F": "une"
            },
            "_V": {
                "M": "un",
                "F": "une"
            },
            "_#": {
                "M": "un",
                "F": "une"
            },
            "_add": {
                "M": "on",
                "F": "on"
            },
            "_mul": {
                "M": "Ø",
                "F": "Ø"
            },
            "_latin": {
                "M": "Ø",
                "F": "Ø"
            }
        },
        "phonologie": {
            "_C": {
                "M": "E_~",
                "F": "yn"
            },
            "_V": {
                "M": "E_~n",
                "F": "yn"
            },
            "_#": {
                "M": "E_~",
                "F": "yn"
            },
            "_add": {
                "M": "O_~",
                "F": "O_~"
            },
            "_mul": {
                "M": "",
                "F": ""
            },
            "_latin": {
                "M": "",
                "F": ""
            }
        }
    },
    "word_deux": {
        "graphie": {
            "_C": {
                "M": "deux",
                "F": "deux"
            },
            "_V": {
                "M": "deux",
                "F": "deux"
            },
            "_#": {
                "M": "deux",
                "F": "deux"
            },
            "_add": {
                "M": "dou",
                "F": "dou"
            },
            "_mul": {
                "M": "vI/",
                "F": "vI/"
            },
            "_latin": {
                "M": "bi",
                "F": "bi"
            }
        },
        "phonologie": {
            "_C": {
                "M": "d2",
                "F": "d2"
            },
            "_V": {
                "M": "d2",
                "F": "d2"
            },
            "_#": {
                "M": "d2z",
                "F": "d2z"
            },
            "_add": {
                "M": "du",
                "F": "du"
            },
            "_mul": {
                "M": "vI/",
                "F": "vI/"
            },
            "_latin": {
                "M": "bi",
                "F": "bi"
            }
        }
    },
    "word_trois": {
        "graphie": {
            "_C": {
                "M": "trois",
                "F": "trois"
            },
            "_V": {
                "M": "trois",
                "F": "trois"
            },
            "_#": {
                "M": "trois",
                "F": "trois"
            },
            "_add": {
                "M": "trei",
                "F": "trei"
            },
            "_mul": {
                "M": "tre",
                "F": "tre"
            },
            "_latin": {
                "M": "tri",
                "F": "tri"
            }
        },
        "phonologie": {
            "_C": {
                "M": "tRwa",
                "F": "tRwa"
            },
            "_V": {
                "M": "tRwaz",
                "F": "tRwaz"
            },
            "_#": {
                "M": "tRwa",
                "F": "tRwa"
            },
            "_add": {
                "M": "tRE",
                "F": "tRE"
            },
            "_mul": {
                "M": "tR",
                "F": "tR"
            },
            "_latin": {
                "M": "tRi",
                "F": "tRi"
            }
        }
    },
    "word_quatre": {
        "graphie": {
            "_C": {
                "M": "quatre",
                "F": "quatre"
            },
            "_V": {
                "M": "quatre",
                "F": "quatre"
            },
            "_#": {
                "M": "quatre",
                "F": "quatre"
            },
            "_add": {
                "M": "quator",
                "F": "quator"
            },
            "_mul": {
                "M": "quar",
                "F": "quar"
            },
            "_latin": {
                "M": "quadri",
                "F": "quadri"
            }
        },
        "phonologie": {
            "_C": {
                "M": "kat(R)",
                "F": "kat(R)"
            },
            "_V": {
                "M": "kat(R)(z)",
                "F": "kat(R)(z)"
            },
            "_#": {
                "M": "kat(R)",
                "F": "kat(R)"
            },
            "_add": {
                "M": "katOR",
                "F": "katOR"
            },
            "_mul": {
                "M": "kaR",
                "F": "kaR"
            },
            "_latin": {
                "M": "k(w)adRi",
                "F": "k(w)adRi"
            }
        }
    },
    "word_cinq": {
        "graphie": {
            "_C": {
                "M": "cinq",
                "F": "cinq"
            },
            "_V": {
                "M": "cinq",
                "F": "cinq"
            },
            "_#": {
                "M": "cinq",
                "F": "cinq"
            },
            "_add": {
                "M": "quin",
                "F": "quin"
            },
            "_mul": {
                "M": "cinqu",
                "F": "cinqu"
            },
            "_latin": {
                "M": "quinti",
                "F": "quinti"
            }
        },
        "phonologie": {
            "_C": {
                "M": "sE_~(k)",
                "F": "sE_~(k)"
            },
            "_V": {
                "M": "sE_~k",
                "F": "sE_~k"
            },
            "_#": {
                "M": "sE_~k",
                "F": "sE_~k"
            },
            "_add": {
                "M": "kE_~",
                "F": "kE_~"
            },
            "_mul": {
                "M": "sE_~k",
                "F": "sE_~k"
            },
            "_latin": {
                "M": "kE_~ti",
                "F": "kE_~ti"
            }
        }
    },
    "word_six": {
        "graphie": {
            "_C": {
                "M": "six",
                "F": "six"
            },
            "_V": {
                "M": "six",
                "F": "six"
            },
            "_#": {
                "M": "six",
                "F": "six"
            },
            "_add": {
                "M": "sei",
                "F": "sei"
            },
            "_mul": {
                "M": "soix",
                "F": "soix"
            },
            "_latin": {
                "M": "sexti",
                "F": "sexti"
            }
        },
        "phonologie": {
            "_C": {
                "M": "si",
                "F": "si"
            },
            "_V": {
                "M": "siz",
                "F": "siz"
            },
            "_#": {
                "M": "sis",
                "F": "sis"
            },
            "_add": {
                "M": "sE",
                "F": "sE"
            },
            "_mul": {
                "M": "swas",
                "F": "swas"
            },
            "_latin": {
                "M": "sEksti",
                "F": "sEksti"
            }
        }
    },
    "word_sept": {
        "graphie": {
            "_C": {
                "M": "sept",
                "F": "sept"
            },
            "_V": {
                "M": "sept",
                "F": "sept"
            },
            "_#": {
                "M": "sept",
                "F": "sept"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "sept",
                "F": "sept"
            },
            "_latin": {
                "M": "septi",
                "F": "septi"
            }
        },
        "phonologie": {
            "_C": {
                "M": "sEt",
                "F": "sEt"
            },
            "_V": {
                "M": "sEt",
                "F": "sEt"
            },
            "_#": {
                "M": "sEt",
                "F": "sEt"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "sEpt",
                "F": "sEpt"
            },
            "_latin": {
                "M": "sEpti",
                "F": "sEpti"
            }
        }
    },
    "word_huit": {
        "graphie": {
            "_C": {
                "M": "huit",
                "F": "huit"
            },
            "_V": {
                "M": "huit",
                "F": "huit"
            },
            "_#": {
                "M": "huit",
                "F": "huit"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "huit",
                "F": "huit"
            },
            "_latin": {
                "M": "octi",
                "F": "octi"
            }
        },
        "phonologie": {
            "_C": {
                "M": "Hi(t)",
                "F": "Hi(t)"
            },
            "_V": {
                "M": "Hit",
                "F": "Hit"
            },
            "_#": {
                "M": "Hit",
                "F": "Hit"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "Hit",
                "F": "Hit"
            },
            "_latin": {
                "M": "Okti",
                "F": "Okti"
            }
        }
    },
    "word_neuf": {
        "graphie": {
            "_C": {
                "M": "neuf",
                "F": "neuf"
            },
            "_V": {
                "M": "neuf",
                "F": "neuf"
            },
            "_#": {
                "M": "neuf",
                "F": "neuf"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "non",
                "F": "non"
            },
            "_latin": {
                "M": "noni",
                "F": "noni"
            }
        },
        "phonologie": {
            "_C": {
                "M": "n9f",
                "F": "n9f"
            },
            "_V": {
                "M": "n9v",
                "F": "n9v"
            },
            "_#": {
                "M": "n9f",
                "F": "n9f"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "non",
                "F": "non"
            },
            "_latin": {
                "M": "noni",
                "F": "noni"
            }
        }
    },
    "word_dix": {
        "graphie": {
            "_C": {
                "M": "dix",
                "F": "dix"
            },
            "_V": {
                "M": "dix",
                "F": "dix"
            },
            "_#": {
                "M": "dix",
                "F": "dix"
            },
            "_add": {
                "M": "ze",
                "F": "ze"
            },
            "_mul": {
                "M": "ante",
                "F": "ante"
            },
            "_latin": {
                "M": "déci",
                "F": "déci"
            }
        },
        "phonologie": {
            "_C": {
                "M": "di",
                "F": "di"
            },
            "_V": {
                "M": "diz",
                "F": "diz"
            },
            "_#": {
                "M": "dis",
                "F": "dis"
            },
            "_add": {
                "M": "z",
                "F": "z"
            },
            "_mul": {
                "M": "A_~t",
                "F": "A_~t"
            },
            "_latin": {
                "M": "desi",
                "F": "desi"
            }
        }
    },
    "word_cent": {
        "graphie": {
            "_C": {
                "M": "cent",
                "F": "cent"
            },
            "_V": {
                "M": "cent",
                "F": "cent"
            },
            "_#": {
                "M": "cent",
                "F": "cent"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "",
                "F": ""
            },
            "_latin": {
                "M": "centi",
                "F": "centi"
            }
        },
        "phonologie": {
            "_C": {
                "M": "sA_~",
                "F": "sA_~"
            },
            "_V": {
                "M": "sA_~t",
                "F": "sA_~t"
            },
            "_#": {
                "M": "sA_~",
                "F": "sA_~"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "",
                "F": ""
            },
            "_latin": {
                "M": "sA_~t",
                "F": "sA_~t"
            }
        }
    },
    "word_mille": {
        "graphie": {
            "_C": {
                "M": "mille",
                "F": "mille"
            },
            "_V": {
                "M": "mille",
                "F": "mille"
            },
            "_#": {
                "M": "mille",
                "F": "mille"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "",
                "F": ""
            },
            "_latin": {
                "M": "mi",
                "F": "mi"
            }
        },
        "phonologie": {
            "_C": {
                "M": "mil",
                "F": "mil"
            },
            "_V": {
                "M": "mil",
                "F": "mil"
            },
            "_#": {
                "M": "mil",
                "F": "mil"
            },
            "_add": {
                "M": "",
                "F": ""
            },
            "_mul": {
                "M": "",
                "F": ""
            },
            "_latin": {
                "M": "mi",
                "F": "mi"
            }
        }
    }
}

lexique_2 = {
    0: ("zéro", "zeRo"),
    1: ("un", "E_~"),
    2: ("deux", "d2"),
    3: ("trois", "tRwa"),
    4: ("quatre", "katR"),
    5: ("cinq", "sE_~k"),
    6: ("six", "sis"),
    7: ("sept", "sEt"),
    8: ("huit", "Hi"),
    9: ("neuf", "n9f"),
    10: ("dix", "dis"),
    11: ("onze", "O_~z"),
    12: ("douze", "duz"),
    13: ("treize", "tREz"),
    14: ("quatorze", "katORz"),
    15: ("quinze", "kE_~z"),
    16: ("seize", "sEz"),
    20: ("vingt", "vE_~t"),
    30: ("trente", "tRA_~t"),
    40: ("quarante", "kaRA_~t"),
    50: ("cinquante", "sE_~kA_~t"),
    60: ("soixante", "swasA_~t"),
    70: ("soixante dix", "swasA_~tdis"),
    80: ("quatre vingt", "katR@vE_~"),
    90: ("quatre vingt dix", "katR@vE_~dis"),
    100: ("cent", "sA_~"),
    1000: ("mille", "mil"),
    1000000: ("million", "miljO_~"),
    1000000000: ("milliaird", "miljaR"),
    '+': ("et", "e")
}


def add_dix_unit(disaine, unit, graph: bool=False):
    s = "graphie" if graph else "phonologie"
    m = disaine[s][""]['M']
    f = disaine[s][""]['F']


# construction avec 10 pour unit+10
# la régle générale d'une addition entre cardinaux est dizaine+unité
# ainsi cette fonction ci-dessous va override 11, 12, 13, 14, 15 et 16
# 10+unit if not unit[s]['_add'] else unit[s]['_add']
def unit_dix(unit, dix, graphie: bool=False, gender: str='f'):
    gender = 'F' if 'f' else 'M'
    s = "graphie" if graphie else "phonologie"
    return unit[s]["_add"][gender] + dix[s]["_add"][gender]


# construction avec 10 pour unit*10
# construction avec 10 pour unit*10+1
# selection entre la graphie et la phonologie
# construction pour les grands nombres

# base = {
#     0: lexique["word_zero"],
#     1: lexique["word_un"],
#     2: lexique["word_deux"],
#     3: lexique["word_trois"],
#     4: lexique["word_quatre"],
#     5: lexique["word_cinq"],
#     6: lexique["word_six"],
#     7: lexique['word_sept'],
#     8: lexique['word_huit'],
#     9: lexique['word_neuf'],
#     10: lexique["word_dix"],
#     pow(10, 2): lexique["word_cent"],
#     pow(10, 3): lexique["word_mille"]
# }


def int2string(i: int, contraintes: collections.deque, base: dict):
    """
        Fonction qui appelle la fonction récurive "recursion_modulaire", modulaire pour le fait qu'on va prendre un
        nombre et récursivement appliquer la division euclidienne modulaire.
    :param i: entier
    :param contraintes: liste de couples (diviseur (int), constraintes (None par défaut))
    :param base: base de connaissances (dictionnaire ici)
    :return: return une liste de couple (graphie (str), phonie (str))
    """
    sortie = list()
    recursion_modulaire(i, contraintes, base, sortie)
    print(sortie)
    return list(map(lambda x: base.get(x), sortie))


def suivant(i, contraintes):
    """
        Suivant(i, contraintes) permet d'avancer itérativement dans les contraintes pour prendre le diviseur "suivant"
        donnant un quotient non nul tout en respectant les contraintes données en paramètres.

        Les contraintes seront à structurer car pour l'instant, ces contraintes ne gèrent explusivement que
        des détails liées qu'au quotient. à terme des contraintes pourraient gérer d'autre éléments suivant la langue
        à traiter.
    :param i: entier
    :param contraintes: liste de couples (diviseur (int), constraintes (None par défaut))
    :return: quadruplet (quotient, reste, diviseur, contraintes)
    """
    j = 0
    (n, spec) = contraintes[j]
    if spec is not None:
        if str(i)[0] not in spec:
            j += 1
            (n, spec) = contraintes[j]
    (q, r) = divmod(i, n)
    while not q and j < len(contraintes):
        j += 1
        (n, spec) = contraintes[j]
        if spec is not None:
            if str(i)[0] not in spec:
                j += 1
                (n, spec) = contraintes[j]
        (q, r) = divmod(i, n)

    return q, r, n, spec


def recursion_modulaire(i: int, contraintes: collections.deque, base: dict, struc: typing.List):
    """
        Fonction suivant la logique de la division euclidienne modulaire.
        On applique les contraintes données en paramètres.
    :param i: entier représentant un cardinal
    :param contraintes: liste de Contraintes
    :param base: base de connaissances (lexique)
    :param struc: structure de donnée de type List
    :return: None
    """
    if i in base:
        if struc and struc[-1] in (20, 30, 40, 50, 60, 70) and i == 1:
            struc.append('+')
        elif i >= pow(10, 6):
            struc.append(1)
        struc.append(i)
    else:
        (q, r, n, spec) = suivant(i, contraintes)
        tmp = q * n
        if n >= pow(10, 6) and q == 1:

            struc.append(q)
            struc.append(n)
        elif tmp in base:
            struc.append(tmp)
        else:
            recursion_modulaire(q, contraintes, base, struc)
            struc.append(n)
        if r:
            recursion_modulaire(r, contraintes, base, struc)


def main():
    # i = 123456789223
    contraintes = collections.deque(
        [(1000000000, None), (1000000, None), (1000, None), (100, None), (20, ['6', '7', '8', '9']), (10, None)])
    # print(" ".join(list(map(lambda x: x[0], int2string(21, contraintes, lexique_2)))))
    # for i in 98000000000:
    print(" ".join(list(map(lambda x: x[1], int2string(91, contraintes, lexique_2)))))
    # print(" ".join(list(map(lambda x: x[1], int2string(i, contraintes, lexique_2)))), sep='\n')


if __name__ == '__main__':
    main()
