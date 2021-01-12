from enum import Enum
select_possibilities = {
        1: '?population',
        2: '?life_expectancy',
        3: '?GDB',
        4: "?capital"
}


where_possibilities = {
        1: '?country wdt:P1082 ?population .',
        2: '?country wdt:P2250 ?life_expectancy .',
        3: '?country wdt:P2131 ?GDB .',
        4: '?country wdt:P36 ?capital .'
}


friendly_names = {
        1: 'Population',
        2: 'Life Expectancy',
        3: 'GDB',
        4: 'Capital'
}


