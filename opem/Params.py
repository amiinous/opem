# -*- coding: utf-8 -*-
HHV = 1.482
uF = 0.95
n = 8 * (10 ** -3)
m = 3 * (10 ** -5)
xi1 = -0.948
xi3 = 7.6 * (10 ** -5)
xi4 = -1.93 * (10 ** -4)
F=96500
R1=8.314
Amphlett_InputParams = {"T": "Cell Operation Temperature [K]", "PH2": "Partial Pressure [atm]", "PO2": "Partial Pressure [atm]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]", "A": "active area [cm^2]",
               "l": "Membrane Thickness [cm]",
               "lambda": "is an adjustable parameter with a min value of 14 and max value of 23",
               "N": "Number Of Single Cells", "R": "R-Electronic [ohm] (*Optional)",
               "B": "An empirical constant depending on the cell and its operation state (Tafel Slope) [V]",
               "JMax": "maximum current density [A/(cm^2)]"}
Amphlett_OutputParams = {"Enernst": "V", "Eta Activation": "V", "Eta Ohmic": "V", "Eta Concentration": "V", "Loss": "V",
                "Vcell": "V", "PEM Efficiency": "", "Power": "W", "VStack": "V","Power-Stack":"W"}


Larminiee_InputParams = {"E0":"Fuel Cell reversible no loss voltage [V]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]",
               "RM": "The membrane and contact resistances [ohm]",
               "B": "Constant in the mass transfer term [V]",
               "i_n": "Internal current [A]",
               "i_0":"Exchange current at which the overvoltage begins to move from zero [A]",
               "i_L":"limiting current [A]",
                "A": "The slope of the Tafel line [V]","N": "Number Of Single Cells"}
Larminiee_OutputParams = {"Vcell": "V", "PEM Efficiency": "", "Power": "W","VStack": "V","Power-Stack":"W"}

Chamberline_InputParams = {"E0": "Open circuit voltage [V]", "b": "Tafel's parameter for the oxygen reduction [V]", "R": "Resistance [ohm.cm^2]",
               "m": "Diffusion's parameters [V]", "n": "Diffusion's parameters [(A^-1)(cm^2)]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]",
               "A": "Active area [cm^2]",
               "N": "Number Of Single Cells"}
Chamberline_OutputParams = {"Vcell": "V", "PEM Efficiency": "", "Power": "W", "VStack": "V","Power-Stack":"W"}