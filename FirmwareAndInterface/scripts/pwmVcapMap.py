# Table of PWM frequencies and duty cycles (in SMCLK cycles)
# and resulting Vcap value for the WISP debugger.
# Structure: { PWM frequency (cycles) :
#               { PWM duty cycle (cycles) : Vcap (V) }}
pwmVcapMap = {
    8 : {
        1 : 0.299,
        2 : 0.704,
        3 : 1.12,
        4 : 1.53,
        5 : 1.96,
        6 : 2.27,
        7 : 2.68,
        8 : 3.10
    },
    9 : {
        1 : 0.259,
        2 : 0.613,
        3 : 0.985,
        4 : 1.35,
        5 : 1.73,
        6 : 2.11,
        7 : 2.37,
        8 : 2.72,
        9 : 3.10
    },
    10 : {
        1 : 0.223,
        2 : 0.543,
        3 : 0.874,
        4 : 1.21,
        5 : 1.54,
        6 : 1.88,
        7 : 2.22,
        8 : 2.44,
        9 : 2.76,
        10 : 3.10
    },
    11 : {
        1 : 0.194,
        2 : 0.482,
        3 : 0.780,
        4 : 1.09,
        5 : 1.39,
        6 : 1.70,
        7 : 2.00,
        8 : 2.31,
        9 : 2.49,
        10 : 2.79,
        11 : 3.09
    },
    12 : {
        1 : 0.174,
        2 : 0.436,
        3 : 0.705,
        4 : 0.986,
        5 : 1.26,
        6 : 1.54,
        7 : 1.83,
        8 : 2.11,
        9 : 2.27,
        10 : 2.55,
        11 : 2.82,
        12 : 3.10
    },
    13 : {
        1 : 0.158,
        2 : 0.403,
        3 : 0.647,
        4 : 0.904,
        5 : 1.17,
        6 : 1.41,
        7 : 1.68,
        8 : 1.94,
        9 : 2.20,
        10 : 2.34,
        11 : 2.59,
        12 : 2.84,
        13 : 3.10
    },
    14 : {
        1 : 0.145,
        2 : 0.368,
        3 : 0.596,
        4 : 0.830,
        5 : 1.07,
        6 : 1.30,
        7 : 1.54,
        8 : 1.79,
        9 : 2.03,
        10 : 2.27,
        11 : 2.39,
        12 : 2.62,
        13 : 2.86,
        14 : 3.10
    },
    15 : {
        1 : 0.123,
        2 : 0.332,
        3 : 0.545,
        4 : 0.762,
        5 : 0.992,
        6 : 1.21,
        7 : 1.43,
        8 : 1.66,
        9 : 1.89,
        10 : 2.11,
        11 : 2.34,
        12 : 2.44,
        13 : 2.65,
        14 : 2.87,
        15 : 3.10
    },
    16 : {
        1 : 0.115,
        2 : 0.306,
        3 : 0.512,
        4 : 0.711,
        5 : 0.924,
        6 : 1.13,
        7 : 1.33,
        8 : 1.54,
        9 : 1.75,
        10 : 1.96,
        11 : 2.18,
        12 : 2.27,
        13 : 2.48,
        14 : 2.67,
        15 : 2.88,
        16 : 3.10
    },
    512 : {
        10 : 0.007,
        20 : 0.057,
        50 : 0.286,
        55 : 0.309,
        60 : 0.346,
        65 : 0.378,
        70 : 0.421,
        75 : 0.453,
        80 : 0.491,
        85 : 0.521,
        90 : 0.563,
        95 : 0.592,
        100 : 0.638,
        105 : 0.663,
        110 : 0.699,
        115 : 0.732,
        120 : 0.771,
        125 : 0.805,
        130 : 0.844,
        135 : 0.878,
        140 : 0.916,
        145 : 0.948,
        150 : 0.993,
        200 : 1.33,
        250 : 1.66,
        256 : 1.70,
        300 : 1.98,
        350 : 2.29,
        400 : 2.42,
        450 : 2.71,
        500 : 3.03,
        512 : 3.11
    }
}