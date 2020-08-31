#!/usr/bin/python

def GlyKrebs(a):
    if a == 'K' or a == 'k':
        return "\n\n\nKrebs Cycle\n\nIntake: Acetyl CoA, NAD+, ADP, H20\nOuttake: CO2, ATP, NADH, H+, FADH2, CoA-SH"
    elif a == 'G' or a == 'g':
        return "\n\n\nGlycolysis\n\nIntake: Glucose, ATP, NAD+, ADP\nOuttake: ADP, NADH, ATP, Pyruvate"
    else: return "\n\nInput not valid. Please try again."

if __name__ == '__main__':
    assert("Krebs Cycle" in GlyKrebs('K'))
    assert("Krebs Cycle" in GlyKrebs('k'))
    assert("Glycolysis" in GlyKrebs('G'))
    assert("Glycolysis" in GlyKrebs('g'))
    assert("Input not valid" in GlyKrebs('X'))
