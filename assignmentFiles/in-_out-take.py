#!/usr/bin/python


def GlyKrebs(a):
    if a == 'K' or a == 'k':
        return "\n\n\nKrebs Cycle\n\nIntake: Acetyl CoA, ADP, NAD+, FAD\nOuttake: CO2, ATP, FADH2, NADH, H2O\nThe Oxaloacetic Acid created as a part of the Krebs Cycle is reused, making it both intake and outtake of the Krebs Cycle (according to me)."
    elif a == 'G' or a == 'g':
        return "\n\n\nGlycolysis\n\nIntake: ADP, NAD+, 2Pi\nOuttake: NADH, ATP, Pyruvate, H2O, H+"
    else: return "\n\nInput not valid. Please try again."

if __name__ == '__main__':
    print("Welcome to the program.\n")
    x = raw_input("What cycle would you like to study?\n'K' for Krebs Cycle; 'G' for Glycolysis.\n")
    print(GlyKrebs(x))
