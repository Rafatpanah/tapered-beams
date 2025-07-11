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

def f1_circ(r, L1, d, E, G, P, h, s_allowable):
    term1_a=5-8*r
    term1_b=term1_a**(5/2)
    term1_c=P/s_allowable
    term1_d=term1_c**(5/3)
    term1=-32*(math.pi)**(4/3)*d*E**2*term1_b*term1_d

    term2_a=2**(1/6)
    term2_b=3**(1/2)
    term2_c=4*r-1
    term2_d=term2_c**(1/2)
    term2_e=E/G
    term2_f=term2_e**(5/2)
    term2_g=term2_a*term2_b*P**3*term2_d*term2_f

    inner_a=8*r**2+2*r-1
    inner_b=inner_a**2
    inner_c=2*math.pi
    inner_d=inner_c**(2/3)
    inner_e=5-8*r
    inner_f=inner_e**2
    inner_g=r**(2/3)
    inner_h=r*s_allowable/P
    inner_i=inner_h**(2/3)
    inner_term=E*inner_b+6*inner_d*G*inner_f*inner_g*inner_i

    term2_den_a=r**(5/3)
    term2_den=term2_den_a*s_allowable**2

    term2=term2_g*inner_term/term2_den

    return term1+term2
    
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
    f1_result = f1_circ(args.r, args.L1, args.d, args.E, args.G, args.P, args.h, args.s_allowable)

    # Output for APDL (You can modify this format as needed)
    print(f"f1_result = {f1_result}")
    
with open("f_results.txt", "w") as f:
    f.write(f"F1_OUT = {f1_result}\n")