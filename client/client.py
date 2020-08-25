#!/usr/bin/env python3
 
import urllib.request
from gen1 import gen1_main
from gen2 import gen2_main
print("X = 2 radians")
sine = gen1_main()
cosine = gen2_main()
print("Sine Value obtained from Mainframe :", sine)
print("Cosine Value obtained from Database :", cosine)
print(" sin^2(x) + cos^2(x)")
print("=", sine**2,"+", cosine**2);
print("=", sine**2 + cosine**2 );
