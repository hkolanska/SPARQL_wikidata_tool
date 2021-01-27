from enum import Enum
select_possibilities = {
        0: '?countryLabel',
        1: '?population',
        2: '?life_expectancy',
        3: '?GDB',
        4: "?capitalLabel"
}


where_possibilities = {
        1: '?country wdt:P1082 ?population .',
        2: '?country wdt:P2250 ?life_expectancy .',
        3: '?country wdt:P2131 ?GDB .',
        4: '?country wdt:P36 ?capital .',
        5: '?country wdt:P463 wd:Q1065 .',
        6: '?country wdt:P463 wd:Q458 .',
        7: '?country wdt:P463 wd:Q7184 .',
        8: '?country wdt:P30 wd:Q46 .',
        9:'?country wdt:P30 wd:Q49.'
}


friendly_names = {
        1: 'Population',
        2: 'Life Expectancy',
        3: 'GDB',
        4: 'Capital',
        5: 'UN', #member of
        6: 'EU',
        7: 'NATO',
        8: 'Europe', #continent
        9: 'North America'
}


