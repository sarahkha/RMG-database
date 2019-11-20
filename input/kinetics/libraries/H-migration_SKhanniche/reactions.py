#!/usr/bin/env python
# encoding: utf-8

name = "H-migration for hexylbenzene radicals (HBradx(x=2-6) --> HBrad1)"
shortDesc = u"Arrhenius parameters obtained from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "HBrad2 <=> HBrad1 ",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18247e+06, 's^-1'),
        n = 1.76914,
        Ea = (130.325, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.26931, dn = +|- 0.029915, dEa = +|- 0.247801 kJ/mol',
    ),
    longDesc =
u"""
sarahkha Nov 4, 2019 TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/Hmig/wHBrad2/reaction  
file: output.py-500-2000
""",
)

entry(
    index = 2,
    label = "HBrad3 <=> HBrad1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3629.83, 's^-1'),
        n = 2.45879,
        Ea = (127.332, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.3942, dn = +|- 0.0416885, dEa = +|- 0.345327 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Nov 4, 2019  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/Hmig/wHBrad3/reaction
""",
)

entry(
    index = 3,
    label = "HBrad4 <=> HBrad1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5594.68, 's^-1'),
        n = 2.04225,
        Ea = (63.0217, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.11742, dn = +|- 0.0139267, dEa = +|- 0.115362 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Nov 4, 2019  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/Hmig/wHBrad4/reaction
""",
)

entry(
    index = 4,
    label = "HBrad5 <=> HBrad1",
    degeneracy = 1,
        kinetics = Arrhenius(
        A = (681.379, 's^-1'),
        n = 2.0485,
        Ea = (36.9409, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.02244, dn = +|- 0.00278419, dEa = +|- 0.0230629 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Nov 4, 2019  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/Hmig/wHBrad5/reaction
""",
)

entry(
    index = 5,
    label = "HBrad6 <=> HBrad1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (349.91, 's^-1'),
        n = 2.1857,
        Ea = (31.5607, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
        comment = 'Fitted to 151 data points; dA = *|/ 1.0375, dn = +|- 0.00461757, dEa = +|- 0.0382497 kJ/mol',
    ),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Nov 4, 2019  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/Hmig/wHBrad6/reaction
""",
)


