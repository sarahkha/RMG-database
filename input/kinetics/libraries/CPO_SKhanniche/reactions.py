#!/usr/bin/env python
# enndex = 9,
#coding: utf-8

name = "CPO_sarahkha"
shortDesc = u"Reactions for cyclopentanone(CPO) oxidation"
longDesc = u"""
In conjunction with the CPO thermo library,
this reaction library contains CBS-QB3 calculations for reactions
relevant to CPO oxidation.

Both calculations are done in CBS-QB3 level of theory.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Cantherm.
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were not used.
"""

entry(
    index = 0,
    label = 'aRO2 <=> aQOOHa_p',
    kinetics = Arrhenius(
        A = (1863.66, 's^-1'),
        n = 2.44949,
        Ea = (91.7515, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.40532, dn = +|- 0.0426847, dEa = +|- 0.353579 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R1/radA/reactionA/reaction"
)

entry(
    index = 1,
    label = 'aRO2 <=> aQOOHb_p',
    kinetics = Arrhenius(
        A = (88969.5, 's^-1'),
        n = 1.98036,
        Ea = (88.9399, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.21884, dn = +|- 0.0248255, dEa = +|- 0.205643 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radA/reactionB/reaction "
)

entry(
    index = 2,
    label = 'aRO2 <=> aQOOHb',
    kinetics = Arrhenius(
        A = (1447.85, 's^-1'),
        n = 2.67718,
        Ea = (106.05, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.48548, dn = +|- 0.0496438, dEa = +|- 0.411226 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche entered Oct 4 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radA/reactionC/reaction "
)

entry(
    index = 3,
    label = 'bRO2 <=> bQOOHa_p',
    kinetics = Arrhenius(
        A = (40994.6, 's^-1'),
        n = 2.08069,
        Ea = (85.4101, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.40463, dn = +|- 0.0426233, dEa = +|- 0.353071 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"New Conformer for TS Calculation performed by Sarah Khanniche, updated November 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionA/reaction",
)

entry(
    index = 4,
    label = 'bRO2 <=> bQOOHb_p',
     kinetics = Arrhenius(
        A = (10180.3, 's^-1'),
        n = 2.50551,
        Ea = (113.57, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.41645, dn = +|- 0.043674, dEa = +|- 0.361775 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionB/reaction",
)

entry(
    index = 5,
    label = 'bRO2 <=> bQOOHa',
     kinetics = Arrhenius(
        A = (38.384, 's^-1'),
        n = 3.14228,
        Ea = (105.481, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.74615, dn = +|- 0.0699246, dEa = +|- 0.579221 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered Oct 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R1/radB/reactionC/reaction",
)

entry(
    index = 6,
    label = 'aQOOHa_p <=> aRO2-OH',
    kinetics = Arrhenius(
        A = (4.03079e+12, 's^-1'),
        n = -0.237668,
        Ea = (52.1002, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04897, dn = +|- 0.00599797, dEa = +|- 0.0496843 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche, entered May 2018, CBS-QB3 level of theory,/home/sarahkha/Cantherm/CPO/R2/radA/reaction",
)

entry(
    index = 7,
    label = 'bQOOHa_p <=> bRO2-OH',
    kinetics = Arrhenius(
        A = (29457.8, 's^-1'),
        n = 1.88499,
        Ea = (160.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.2886, dn = +|- 0.0318073, dEa = +|- 0.263477 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2/radB/reactionalphaprim/reaction
"""
)

entry(
    index = 8,
    label = 'aRO2 <=> Olefinab + HO2',
    kinetics = Arrhenius(
        A = (4.01749e+08, 's^-1'),
        n = 1.26964,
        Ea = (94.8236, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.06938, dn = +|- 0.00841526, dEa = +|- 0.069708 kJ/mol',
    ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionA
"""
)

entry(
    index = 9,
    label = 'bRO2 <=> Olefinab + HO2',
    kinetics = Arrhenius(
        A = (6.31544e+08, 's^-1'),
        n = 1.21279,
        Ea = (99.3376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.06104, dn = +|- 0.0074331, dEa = +|- 0.0615722 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionB
"""
)

entry(
    index = 10,
    label = 'bRO2 <=> Olefinbb_p + HO2',
    kinetics = Arrhenius(
        A = (7.87995e+08, 's^-1'),
        n = 1.29231,
        Ea = (121.886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.06954, dn = +|- 0.00843305, dEa = +|- 0.0698553 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionD
"""
)

entry(
    index = 11,
    label = 'aQOOHb <=> Olefinab + HO2',
    kinetics = Arrhenius(
        A = (4.36611e+15, 's^-1'),
        n = -0.608303,
        Ea = (47.5506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04148, dn = +|- 0.00509819, dEa = +|- 0.0422309 kJ/mol',
    ),
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionQOOHA
"""
)

entry(
    index = 12,
    label = 'bQOOHa <=> Olefinab + HO2',
    kinetics = Arrhenius(
        A = (6.91542e+12, 's^-1'),
        n = 0.342751,
        Ea = (78.1113, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02611, dn = +|- 0.00323351, dEa = +|- 0.0267849 kJ/mol',
    ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionQOOHB
"""
)

entry(
    index = 13,
    label = 'bQOOHb_p <=> Olefinbb_p + HO2',
    kinetics = Arrhenius(
        A = (1.82743e+11, 's^-1'),
        n = 0.51215,
        Ea = (66.5156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.01607, dn = +|- 0.00199966, dEa = +|- 0.0165642 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/ELIMHO2/reactionQOOHC
"""
)

entry(
    index = 14,
    label = 'aQOOHa_p <=> CyclicOaa_p + OH',
    kinetics = Arrhenius(
        A = (7.23492e+16, 's^-1'),
        n = -0.883526,
        Ea = (142.924, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04281, dn = +|- 0.00525833, dEa = +|- 0.0435575 kJ/mol',
    ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radA/reaction
"""
)

entry(
    index = 15,
    label = 'aQOOHb_p <=> CyclicOab_p + OH',
    kinetics = Arrhenius(
        A = (1.22443e+18, 's^-1'),
        n = -1.34152,
        Ea = (113.95, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.08046, dn = +|- 0.00970796, dEa = +|- 0.0804161 kJ/mol',
    ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radB/reaction
"""
)

entry(
    index = 16,
    label = 'aQOOHb <=> CyclicOab + OH',
    kinetics = Arrhenius(
        A = (7.96939e+16, 's^-1'),
        n = -0.811367,
        Ea = (62.3906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02924, dn = +|- 0.00361491, dEa = +|- 0.0299442 kJ/mol',
        ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radC/reaction
"""
)

entry(
    index = 17,
    label = 'bQOOHa_p <=> CyclicOba_p + OH',
    kinetics = Arrhenius(
        A = (1.52897e+11, 's^-1'),
        n = 0.563971,
        Ea = (127.55, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02518, dn = +|- 0.00311982, dEa = +|- 0.0258431 kJ/mol',
),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered July 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Beta/radA/reaction
"""
)

entry(
    index = 18,
    label = 'bQOOHb_p <=> CyclicObb_p + OH',
    kinetics = Arrhenius(
        A = (1.33536e+11, 's^-1'),
        n = 0.502177,
        Ea = (45.0341, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.01863, dn = +|- 0.00231543, dEa = +|- 0.0191799 kJ/mol',
        ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Alpha/radC/reaction
"""
)

entry(
    index = 19,
    label = 'bQOOHa <=> CyclicOab + OH',
    kinetics = Arrhenius(
        A = (2.22078e+11, 's^-1'),
        n = 0.523586,
        Ea = (63.6122, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02759, dn = +|- 0.00341466, dEa = +|- 0.0282854 kJ/mol',
),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location:/home/sarahkha/Cantherm/CPO/R2OHEli/Beta/radC/reaction
"""
)

entry(
    index = 20,
    label = 'aQOOHa_p <=> [CH2]C(OO)C(=O)C=C',
    kinetics = Arrhenius(
        A = (9.59076e+11, 's^-1'),
        n = 0.757079,
        Ea = (165.14, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.0264, dn = +|- 0.00326931, dEa = +|- 0.0270814 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory", 
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/R3/Alpha/radAprim/reaction
"""
)

entry(
    index = 21,
    label = 'aQOOHb_p <=> C=CCC([C]=O)OO',
    kinetics = Arrhenius(
        A = (1.9222e+17, 's^-1'),
        n = -0.908278,
        Ea = (130.211, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04414, dn = +|- 0.00541818, dEa = +|- 0.0448816 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R3/Alpha/radBprim/reaction",
    longDesc =
"""
"""
)

entry(
    index = 22,
    label = 'bQOOHa_p <=> [CH2]C(CC=C=O)OO',
    kinetics = Arrhenius(
        A = (1.5413e+10, 's^-1'),
        n = 1.10727,
        Ea = (159.948, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02288, dn = +|- 0.00283829, dEa = +|- 0.0235111 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R3/Beta/radA/reaction",
    longDesc =
"""

"""
)

entry(
    index = 23,
    label = 'bQOOHb_p <=> C=CC(C[C]=O)OO',
    kinetics = Arrhenius(
        A = (3.10257e+11, 's^-1'),
        n = 0.616304,
        Ea = (120.454, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04919, dn = +|- 0.00602424, dEa = +|- 0.0499019 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory, /home/sarahkha/Cantherm/CPO/R3/Beta/radB/reaction",
    longDesc =
"""
"""
)

entry(
    index = 24,
    label = 'aQOOHb_p <=> aQOOHa_p',
    kinetics = Arrhenius(
        A = (4.15832e+09, 's^-1'),
        n = 1.06507,
        Ea = (127.406, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.06195, dn = +|- 0.00754069, dEa = +|- 0.0624635 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"",
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/InterconveR1/reaction
"""
)

entry(
    index = 25,
    label = 'bQOOHb_p <=> bQOOHa_p',
    kinetics = Arrhenius(
        A = (6.59389e+07, 's^-1'),
        n = 1.63664,
        Ea = (127.644, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.24266, dn = +|- 0.0272536, dEa = +|- 0.225755 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/InterconvR1O2beta/reaction
"""
)

entry(
    index = 26,
    label = 'OQ_paOOH <=> CPOadione + H2O',
    kinetics = Arrhenius(
        A = (2.26394e+09, 's^-1'),
        n = 1.18759,
        Ea = (182.61, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.63765, dn = +|- 0.0618777, dEa = +|- 0.512565 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/Review/WaterElimination 
"""
)

#entry(
#    index = 27,
#    label = 'OQ_paOOH <=> CPOadione + H2O',
#    kinetics = Arrhenius(
#        A = (4.81777e+13, 's^-1'),
#        n = 0.213937,
#        Ea = (228.37, 'kJ/mol'),
#        T0 = (1, 'K'),
#        Tmin = (500, 'K'),
#        Tmax = (2000, 'K'),
#        comment = 'Fitted to 151 data points; dA = *|/ 1.11372, dn = +|- 0.0135117, dEa = +|- 0.111925 kJ/mol',
#    ),
#    degeneracy = 1,
#    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
#    longDesc =
#"""
#location: /home/sarahkha/Cantherm/CPO/Review/waterElim2 
#"""
#)

entry(
    index = 27,
    label = 'OQ_paOOH <=> O=C(O)CCCC(=O)',
    kinetics = Arrhenius(
        A = (1.17568e+16, 's^-1'),
        n = -0.875905,
        Ea = (169.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04771, dn = +|- 0.00584699, dEa = +|- 0.0484336 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/Review/reaction 
"""
)

entry(
    index = 28,
    label = 'OQ_paOOH <=> CPOaoxyl + OH',
    kinetics = Arrhenius(
        A = (5.22769e+17, 's^-1'),
        n = -0.603292,
        Ea = (202.974, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04858, dn = +|- 0.00595037, dEa = +|- 0.04929 kJ/mol',
    ),
    degeneracy = 1,
    shortDesc = u"Calculation performed by Sarah Khanniche,entered May 2018, CBS-QB3 level of theory",
    longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/Review/OH_ELIMINATION 
This value is for the triplet channel only assuming fast intersystem crossing, but we expect the singlet channel rate will have a much higher rate, so this underestimates the importance of OQ’αOOH → CPOαoxyl + OH
"""
)

entry(
    index = 29,
    label = 'Hrad + Olefinab <=> O=C1cCCC1',
    kinetics = Arrhenius(
        A = (3.6842e+08, 'cm^3/(mol*s)'),
        n = 1.52522,
        Ea = (3.79501, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.0031, dn = +|- 0.00038811, dEa = +|- 0.00321492 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/SENSITIVITY/3rdReaction/reaction
"""
)

entry(
    index = 30,
    label = 'Olefinab1a_p-OH <=> Olefinab',
    kinetics = Arrhenius(
        A = (6840.44, 's^-1'),
        n = 2.5097,
        Ea = (219.454, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.6945, dn = +|- 0.0661583, dEa = +|- 0.548024 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/SENSITIVITY/Tauto/reaction
"""
)

entry(
    index = 31,
    label = 'O=C1[CH]C[C]=C1 + HO2 <=> O=C1C=C[CH]C1OO',
    kinetics = Arrhenius(
        A = (139.033, 'cm^3/(mol*s)'),
        n = 3.44867,
        Ea = (10.5943, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 11 data points; dA = *|/ 1.61314, dn = +|- 0.0617306, dEa = +|- 0.378704 kJ/mol',
   ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/HO2ADD/reactionA 
"""
)

entry(
    index = 32,
    label = 'O=C1[CH]C[C]=C1 + HO2 <=> O=C1[CH]C(OO)C=C1',
    kinetics = Arrhenius(
        A = (15.1784, 'cm^3/(mol*s)'),
        n = 3.66523,
        Ea = (21.673, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 11 data points; dA = *|/ 1.7097, dn = +|- 0.0692352, dEa = +|- 0.424743 kJ/mol',
    ),
   degeneracy = 1,
   shortDesc = u"Calculation performed by Sarah Khanniche,entered Oct 2018, CBS-QB3 level of theory",
   longDesc =
"""
location: /home/sarahkha/Cantherm/CPO/HO2ADD/reactionB
"""
)


