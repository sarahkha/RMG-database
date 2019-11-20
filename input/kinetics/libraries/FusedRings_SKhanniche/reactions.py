#!/usr/bin/env python
# encoding: utf-8

name = "EndoCycloAddHB"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = 'HBrad2 <=> Fusedsynrad2',
    kinetics = Arrhenius(
        A = (496252, 's^-1'),
        n = 1.57961,
        Ea = (114.573, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.06922, dn = +|- 0.00839539, dEa = +|- 0.0695434 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Feb. 5, 2018  TST for T=500-200K
""",
)

entry(
    index = 2,
    label = 'HBrad3 <=> Fusedsynrad3',
    kinetics = Arrhenius(
        A = (8572.66, 's^-1'),
        n = 2.43882,
        Ea = (51.423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.04634, dn = +|- 0.00568292, dEa = +|- 0.0470746 kJ/mol',
    ),   
	shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Feb. 5, 2018  TST for T=500-200K
""",
)

entry(
    index = 3,
    label = 'HBrad4 <=> Fusedantirad4',
    kinetics = Arrhenius(
        A = (7438.71, 's^-1'),
        n = 1.56256,
        Ea = (24.9924, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.05454, dn = +|- 0.00666172, dEa = +|- 0.0551825 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
   longDesc =
u"""
sarahkha Feb. 5, 2018 + Jan. 23, 2018  TST for T=500-200K
""",
)

entry(
    index = 7,
    label = 'HBrad5 <=> Fusedsynrad5',
    kinetics = Arrhenius(
        A = (558.663, 's^-1'),
        n = 1.64406,
        Ea = (35.2182, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.09481, dn = +|- 0.0113632, dEa = +|- 0.0941276 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Feb. 5, 2018  TST for T=500-200K
""",
)

