#!/usr/bin/env python
# encoding: utf-8

name = "HBPhenylMigration"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "HBrad2 <=> Spirorad2 ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46139e+07,'s^-1'), n=1.30419, Ea=(54.6853, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from sarahkha quantum calculations at CBSQB3 level of theory with Hindered rotors treatment and Eckart Tunelling""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/PhenylMig/wHBrad2/reaction1
""",
)

entry(
    index = 2,
    label = "Spirorad2 <=> 2HBrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.1705e+13,'s^-1'), n=0.383545, Ea=(19.8222, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/PhenylMig/wHBrad2/reaction2
""",
)

entry(
    index = 3,
    label = "HBrad3 <=> Spirorad3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(966131,'s^-1'), n=1.86605, Ea=(70.0712, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/PhenylMig/wHBrad3/reaction1 
""",
)

entry(
    index = 4,
    label = "Spirorad3 <=> 3HBrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.0336e+12,'s^-1'), n=0.135082, Ea=(42.4868, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/PhenylMig/wHBrad3/reaction2
""",
)

entry(
    index = 5,
    label = "HBrad4 <=> Spirorad4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(905.719,'s^-1'), n=2.15234, Ea=(31.5819, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: /home/sarahkha/Cantherm/HB/PhenylMig/wHBrad4/reaction1
""",
)

entry(
    index = 6,
    label = "Spirorad4 <=> 4HBrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.3477e+12,'s^-1'), n=0.514347, Ea=(72.4192, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
   longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
location: 
""",
)

entry(
    index = 7,
    label = "HBrad5 <=> Spirorad5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(284.136,'s^-1'), n=1.70342, Ea=(26.0501, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
""",
)

entry(
    index = 8,
    label = "Spirorad5 <=> 5HBrad",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.86326e+12,'s^-1'), n=0.527375, Ea=(90.7394, 'kJ/mol'), T0=(1, 'K')),
     shortDesc = u"""Training reaction from quantum calculations at CBSQB3 level of theory with Hindered rotors treatment""",
    longDesc =
u"""
sarahkha Dec 11, 2017 + Jan. 23, 2018  TST for T=500-200K
""",
)

