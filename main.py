# -*- coding: utf-8 -*-

# Using an ELGA Techneco Hybrid Heatpump


def gas_energy() -> float:
    # Total energy in kW/h in a m3 gas
    gas_energy = 9.8
    CV_efficiency = 0.944
    return gas_energy * CV_efficiency

def electricity_price() :
    # Total price for one kW/h
    price_elec_levering = 0.07156
    price_elec_ODE = 0.030371
    price_elec_EB = 0.121726

    return price_elec_EB + price_elec_ODE + price_elec_levering

def gas_price():
    # Total price for one m3
    price_gas_levering = 0.27350
    price_gas_EB = 0.3617779
    price_gas_ODE = 0.084337

    return price_gas_levering + price_gas_EB + price_gas_ODE

def calculate():
    T_min = -7
    T_plus = 7
    Delta_T = abs(T_min - T_plus)
    COP_min = 2.7
    COP_plus = 4.6
    COP_diff_K = (COP_plus - COP_min) / Delta_T
    OP_COP = optimal_COP()

    for x in range(T_plus, -20,  -1):
        y = abs(T_plus - x)
        print ("Temp to check " + str(x) + "  "+ str(COP_plus - (y*COP_diff_K)) + "    "+ str(OP_COP))
        if (COP_plus - (y*COP_diff_K)) <= OP_COP:
            print("optimal COP is at " + str(x+1))
            break

def optimal_COP() -> float:
    opt = electricity_price() / gas_price() * gas_energy()
    # print("Optimal COP is " + str(opt))
    return opt

calculate()
# print(electricity_price(), gas_price())
