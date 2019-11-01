#!/usr/bin/env python
# encoding: utf-8

name = "cyclopentanone (CPO) oxidation"
shortDesc = u"sarahkha ab initio calculations"
longDesc = u"""
Calculated at the CBS-QB3 level with 1D HR with Gaussian09 on NERSC and Pharos
/home/sarahkha/Cantherm/CPO
"""

entry(
    index = 0,
    label = "aRO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u1 p2 c0 {6,S}
8  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.601,36.798,43.438,49.333,58.546,64.588,73.127],'cal/(mol*K)'),
        H298 = (-30.663,'kcal/mol'),
        S298 = (91.965,'cal/(mol*K)'),
    ),
    shortDesc = u"""CPO peroxy radicals_alpha, alphaRO2""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 NERSC entered Feb. 8, 2018
/home/sarahkha/Cantherm/CPO/R1/radA/reactionA/species/cpoOOrad/THERMO
optical isomer =2
one HR = CCOO
""",
)

entry(
    index = 1,
    label = "bRO2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {7,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  O u1 p2 c0 {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.210,37.513,44.139,49.914,58.723,64.574,73.186],'cal/(mol*K)'),
        H298 = (-36.280,'kcal/mol'),
        S298 = (90.633,'cal/(mol*K)'),
    ),
    shortDesc = u"""CPO peroxy radicals_beta, betaRO2""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 NERSC entered Feb. 8, 2018
/home/sarahkha/Cantherm/CPO/R1/radB/reactionA/species/cpoOOrad/THERMO
optical isomer =2
one HR = CCOO
""",
)

entry(
    index = 2,
    label = "aQOOHa_p",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u1 p0 c0 {2,S} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.652,40.924,48.453,54.317,63.032,68.752,75.366],'cal/(mol*K)'),
        H298 = (-30.744,'kcal/mol'),
        S298 = (86.802,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species, alphaQOOHalphaprim""",
    longDesc = 
u"""
Lowest conformer:/home/sarahkha/Cantherm/CPO/R1/radA/reactionA/species/cpoOOHrad/THERMO 
sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018
other conf:/home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/A/fromHabs
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 3,
    label = "aQOOHb_p",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u1 p0 c0 {6,S} {8,S} {14,S}
8  C u0 p0 c0 {2,S} {7,S} {9,S} {15,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.232,41.658,49.269,55.180,63.910,69.549,75.778],'cal/(mol*K)'),
        H298 = (-22.754,'kcal/mol'),
        S298 = (88.784,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species, alphaQOOHbetaprim""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018
/home/sarahkha/Cantherm/CPO/R1/radA/reactionB/species/cpoOOHradB/THERMO
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 4,
    label = "aQOOHb",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {2,S} {5,S} {8,S} {14,S}
8  O u0 p2 c0 {7,S} {9,S}
9  O u0 p2 c0 {8,S} {15,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.785,43.341,50.761,56.218,64.106,69.204,75.034],'cal/(mol*K)'),
        H298 = (-21.601,'kcal/mol'),
        S298 = (89.093,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species, alphaQOOHbeta""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered Oct 3, 2018
/home/sarahkha/Cantherm/CPO/R1/radA/reactionC/species/QOOH/THERMO
optisomer=2
2 HR = ROTOO,ROTOH
""",
)

entry(
    index = 5,
    label = "bQOOHa_p",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
8  C u1 p0 c0 {2,S} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.514,39.535,46.306,51.720,59.764,65.492,73.357],'cal/(mol*K)'),
        H298 = (-31.101,'kcal/mol'),
        S298 = (91.308,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species, betaQOOHalphaprim""",
    longDesc = 
u"""
LOWEST conformer:/home/sarahkha/Cantherm/CPO/R1/radB/reactionA/species/cpoOHrad/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018
other conf: /home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/B/fromHabs
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 6,
    label = "bQOOHb_p",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  C u1 p0 c0 {4,S} {8,S} {14,S}
8  C u0 p0 c0 {2,S} {7,S} {9,S} {15,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.360,39.635,46.079,51.613,59.971,65.411,73.221],'cal/(mol*K)'),
        H298 = (-23.825,'kcal/mol'),
        S298 = (94.634,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species, betaQOOHbetaprim""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018
/home/sarahkha/Cantherm/CPO/R1/radB/reactionB/species/cpoHO2radB/THERMO
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 7,
    label = "bQOOHa",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {10,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {11,S}
8  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
9  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.788,39.385,45.984,51.452,59.440,65.073,73.092],'cal/(mol*K)'),
        H298 = (-29.471,'kcal/mol'),
        S298 = (92.199,'cal/(mol*K)'),
    ),
    shortDesc = u"""QOOH species,betaQOOHalpha""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R1/radB/reactionC/species/QOOH/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered Oct 3, 2018
optisomer=2
2 HR = ROTOO,ROTOH
""",
)

entry(
    index = 8,
    label = "CyclicOaa_p",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {7,D}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {13,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
7  C u0 p0 c0 {2,D} {3,S} {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.420,30.993,37.459,42.603,50.446,55.993,63.525],'cal/(mol*K)'),
        H298 = (-34.198,'kcal/mol'),
        S298 = (74.795,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclic ether, cyclicOalphaalphaprim""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radA/species/cyclicEtherA/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered July24, 2018
optisomer=1
""",
)

entry(
    index = 9,
    label = "CyclicOab_p",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  O u0 p2 c0 {3,S} {6,S}
5  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {5,S} {7,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.149,30.909,37.491,42.669,50.515,56.054,63.550],'cal/(mol*K)'),
        H298 = (-36.251,'kcal/mol'),
        S298 = (75.454,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclic ether, CylicOalphabetaprim""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radB/species/cyclicEtherB/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered July24, 2018
optisomer=2
""",
)

entry(
    index = 10,
    label = "CyclicOab",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {13,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.963,31.325,37.591,42.638,50.446,55.980,63.525],'cal/(mol*K)'),
        H298 = (-46.806,'kcal/mol'),
        S298 = (77.432,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclic ether, CyclicOalphabeta""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radC/species/CyclicEther/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered Oct 3, 2018
optisomer=2
""",
)

entry(
    index = 11,
    label = "CyclicObb_p",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {4,S} {5,S} {7,S} {11,S}
7  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.067,31.488,37.776,42.816,50.598,56.106,63.596],'cal/(mol*K)'),
        H298 = (-49.465,'kcal/mol'),
        S298 = (76.443,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclic ether, CylicObetabetaprim""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R2OHEli/Beta/radB/species/cyclicEther
optisomer=1
""",
)

entry(
    index = 12,
    label = "aRO2-OH",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {1,S} {6,D} {8,S}
8  O u0 p2 c0 {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.705,40.590,47.618,53.044,61.237,66.772,73.728],'cal/(mol*K)'),
        H298 = (-25.667,'kcal/mol'),
        S298 = (87.737,'cal/(mol*K)'),
    ),
    shortDesc = u"""enol, alphaRO2-OH""",
    longDesc = 
u"""
sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb.10, 2018
/home/sarahkha/Cantherm/CPO/R2/radA/species/Prod/THERMO
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 13,
    label = "bRO2-OH",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {1,S} {8,S}
4  C u0 p0 c0 {5,D} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {7,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {3,S} {6,S} {7,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.258,40.422,46.655,51.721,59.614,65.144,72.646],'cal/(mol*K)'),
        H298 = (-26.393,'kcal/mol'),
        S298 = (89.204,'cal/(mol*K)'),
    ),
    shortDesc = u"""enol, betaRO2-OH""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R2/radB/reactionalphaprim/species/Prod/THERMO
optisomer=2
2 HR treatments
""",
)

entry(
    index = 14,
    label = "Olefinab",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.401,27.865,33.512,38.149,45.373,50.563,57.816],'cal/(mol*K)'),
        H298 = (-23.096,'kcal/mol'),
        S298 = (73.287,'cal/(mol*K)'),
    ),
    shortDesc = u"""Olefin, Olefinalphabeta""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/ELIMHO2/species/prod/THERMO
""",
)

entry(
    index = 15,
    label = "Olefinbb_p",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.695,28.221,33.852,38.442,45.603,50.741,57.911],'cal/(mol*K)'),
        H298 = (-18.344,'kcal/mol'),
        S298 = (72.204,'cal/(mol*K)'),
    ),
    shortDesc = u"""Olefin, Olefinbetabetaprim""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/ELIMHO2/species/prodD/THERMO
""",
)

entry(
    index = 16,
    label = "[CH2]C(OO)C(=O)C=C",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
5  C u1 p0 c0 {4,S} {13,S} {14,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.339,44.399,51.359,57.167,65.456,70.197,75.706],'cal/(mol*K)'),
        H298 = (-2.275,'kcal/mol'),
        S298 = (97.256,'cal/(mol*K)'),
    ),
    shortDesc = u"""acyclic radical with CH2 terminal,sciss-HO2_alpha-rad_alpha""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R3/Alpha/radAprim/species/prod
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018
optisomer=2
5 HR treatments
""",
)

entry(
    index = 17,
    label = "C=CCC([C]=O)OO",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {14,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  C u1 p0 c0 {4,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.689,44.877,50.739,55.452,62.168,66.567,72.716],'cal/(mol*K)'),
        H298 = (-7.450,'kcal/mol'),
        S298 = (98.477,'cal/(mol*K)'),
    ),
    shortDesc = u"""acyclic radical with Crad=O,sciss-HO2_alpha-rad_alpha""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R3/Alpha/radBprim/species/prod
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018
optisomer=2
5 HR treatments
""",
)

entry(
    index = 18,
    label = "[CH2]C(CC=C=O)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {12,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {13,S}
8  C u1 p0 c0 {5,S} {14,S} {15,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.833,45.927,50.567,54.251,60.024,64.420,71.023],'cal/(mol*K)'),
        H298 = (1.161,'kcal/mol'),
        S298 = (104.270,'cal/(mol*K)'),
    ),
    shortDesc = u"""acyclic radical with CH2 terminal,sciss-HO2_beta-rad_alpha""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R3/Beta/radA/species/prod/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered June4, 2018
optisomer=2
5 HR treatments
""",
)

entry(
    index = 19,
    label = "C=CC(C[C]=O)OO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  C u0 p0 c0 {4,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {14,S} {15,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.352,44.318,49.418,53.750,60.477,65.171,71.514],'cal/(mol*K)'),
        H298 = (-8.657,'kcal/mol'),
        S298 = (103.390,'cal/(mol*K)'),
    ),
    shortDesc = u"""acyclic radicals with Crad=O,sciss-HO2_beta-rad_beta""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/R3/Beta/radB/species/prod/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered June4, 2018
optisomer=2
5 HR treatments
""",
)

entry(
    index = 20,
    label = "OQ_paOOH",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.436,40.780,48.600,55.107,65.042,71.736,79.846],'cal/(mol*K)'),
        H298 = (-67.431,'kcal/mol'),
        S298 = (86.546,'cal/(mol*K)'),
    ),
    shortDesc = u"""OQ'alphaOOH""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/Review/species/QnonrOOH
optisomer=2
2 HR
""",
)

entry(
    index = 21,
    label = "CPOaoxyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {7,S} {14,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.545,33.935,40.183,45.490,53.867,59.853,68.200],'cal/(mol*K)'),
        H298 = (-30.323,'kcal/mol'),
        S298 = (82.706,'cal/(mol*K)'),
    ),
    shortDesc = u"""CPOalphaoxyl""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/Review/OH_ELIMINATION/THERMOprod
optisomer=2
no HR
""",
)

entry(
    index = 22,
    label = "CPOadione",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.044,31.793,37.509,42.383,50.078,55.578,63.240],'cal/(mol*K)'),
        H298 = (-62.260,'kcal/mol'),
        S298 = (78.836,'cal/(mol*K)'),
    ),
    shortDesc = u"""CPOalphadione""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/Review/WaterElimination/THERMOprod
optisomer=1
""",
)

entry(
    index = 23,
    label = "O=C(O)CCCC(=O)",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {8,D} {16,S}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.254,42.846,48.519,53.519,61.750,67.791,76.416],'cal/(mol*K)'),
        H298 = (-136.869,'kcal/mol'),
        S298 = (96.426,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/Review/species/ProdLinear
optisomer=1
5HR
""",
)

entry(
    index = 24,
    label = "CPOboxyl",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
7  O u1 p2 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.681,34.229,40.595,45.930,54.303,60.238,68.406],'cal/(mol*K)'),
        H298 = (-33.417,'kcal/mol'),
        S298 = (82.725,'cal/(mol*K)'),
    ),
    shortDesc = u"""CPObetaoxyl""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/SENSITIVITY/OHsciss/species/ProdO/THERMO
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered Oct 3, 2018
optisomer=2
""",
)

entry(
    index = 25,
    label = "Olefinab1a_p-OH",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.614,30.022,35.393,39.678,46.217,50.776,56.992],'cal/(mol*K)'),
        H298 = (-8.705,'kcal/mol'),
        S298 = (73.017,'cal/(mol*K)'),
    ),
    shortDesc = u"""Olefinab-1a_p-OH""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/SENSITIVITY/Tauto/species/react/THERMO
optisomer=1
1 HR = ROTOH
sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered Oct 3, 2018
""",
)

entry(
    index = 26,
    label = "OQ_pbOOH",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.247,40.311,47.502,53.614,62.625,68.777,77.731],'cal/(mol*K)'),
        H298 = (-71.207,'kcal/mol'),
        S298 = (90.744,'cal/(mol*K)'),
    ),
    shortDesc = u"""OQ'betaOOH""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/SENSITIVITY/OHsciss/species/QOOH/THERMO
""",
)

