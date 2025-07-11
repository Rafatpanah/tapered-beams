import math
import argparse

def f1(r, L1, d, E, G, P, h, s_allowable):

    term1 = -(d * E * G * (3 * h + 4 * L1 * r)**3 * (3 * h + 2 * L1 + 4 * L1 * r)**3) / (2 * P)

    term2 = (9 * (3/2)**(2/3) * G * h**3 * (3 * h + 2 * L1 + 4 * L1 * r)**3) / (
        2 * (3 * h + 4 * L1 * r) * (P / ((h + 2 * L1 * r)**2 * s_allowable))**(4/3)
    )

    term3 = 3 * (3/2)**(1/3) * E * h * (3 * h + 4 * L1 * r) * (3 * h + 2 * L1 + 4 * L1 * r)**3 * (
        ((h + 2 * L1 * r)**2 * s_allowable) / P
    )**(2/3)

    inside_term = (
        G * h * (h + 2 * L1) * (3 * h + 4 * L1 * r) * (3 * h + 2 * L1 + 4 * L1 * r) +
        G * h**2 * (3 * h + 2 * L1 + 4 * L1 * r)**2 +
        (3 * h + 4 * L1 * r)**2 * (
            G * (h + 2 * L1)**2 +
            (2/3) * (2/3)**(1/3) * E * (3 * h + 2 * L1 + 4 * L1 * r)**2 * (
                P / ((h + 2 * L1 * r)**2 * s_allowable)
            )**(2/3)
        )
    )

    term4 = 9 * (3/2)**(2/3) * L1 * inside_term * (
        ((h + 2 * L1 * r)**2 * s_allowable) / P
    )**(4/3)

    return term1 + term2 + term3 + term4


def f2(r, L1, d, E, G, P, h, s_allowable):

    term1 = 2 * 2**(1/3) * E * P**(5/3) * (3 * h + 4 * L1 * r)**2 * (3 * h + 2 * L1 + 4 * L1 * r)**2

    inner1 = (
        9 * h**3 * r +
        8 * L1**3 * r**2 * (-1 + 4 * r) +
        3 * h**2 * L1 * (3 + 2 * r) * (-1 + 4 * r) +
        2 * h * L1**2 * r * (-7 + 8 * r * (4 + r))
    )

    term1_total = term1 * inner1 * s_allowable**(1/3)

    term2 = 6 * 3**(1/3) * G * P * (h + 2 * L1 * r)**(4/3)

    inner2 = (
        81 * h**7 * r +
        256 * L1**7 * r**4 * (-5 + 8 * r) +
        64 * h * L1**6 * r**3 * (-65 + 16 * r * (5 + 3 * r)) +
        27 * h**6 * L1 * (-9 + 2 * r * (13 + 8 * r)) +
        54 * h**5 * L1**2 * (-14 + r * (7 + 16 * r * (4 + r))) +
        128 * h**2 * L1**5 * r**2 * (-40 + r * (25 + 3 * r * (25 + 4 * r))) +
        8 * h**3 * L1**4 * r * (-355 + 4 * r * (-50 + r * (345 + 8 * r * (20 + r)))) +
        12 * h**4 * L1**3 * (-51 + 2 * r * (-104 + r * (213 + 8 * r * (33 + 4 * r))))
    )
    
    term2_total = term2 * inner2 * s_allowable
    
    return term1_total + term2_total
    
if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Calculate f1 and f2.")

    # Add arguments for each input value
    parser.add_argument("r", type=float, help="Value for r")
    parser.add_argument("L1", type=float, help="Value for L1")
    parser.add_argument("d", type=float, help="Value for d")
    parser.add_argument("E", type=float, help="Value for E")
    parser.add_argument("G", type=float, help="Value for G")
    parser.add_argument("P", type=float, help="Value for P")
    parser.add_argument("h", type=float, help="Value for h")
    parser.add_argument("s_allowable", type=float, help="Value for s_allowable")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Calculate f1 and f2 using the provided arguments
    f1_result = f1(args.r, args.L1, args.d, args.E, args.G, args.P, args.h, args.s_allowable)
    f2_result = f2(args.r, args.L1, args.d, args.E, args.G, args.P, args.h, args.s_allowable)

    # Output for APDL (You can modify this format as needed)
    print(f"f1_result = {f1_result}")
    print(f"f2_result = {f2_result}")
    
with open("f_results.txt", "w") as f:
    f.write(f"F1_OUT = {f1_result}\n")
    f.write(f"F2_OUT = {f2_result}\n")