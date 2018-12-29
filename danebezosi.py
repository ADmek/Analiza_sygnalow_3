# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:03:31 2018

@author: Adam
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import aseegg as ag

dane = pd.read_csv(r"C:\Users\Adam\Desktop\dane.csv", delimiter=';', engine='python')
mojeDane = dane['Sub01']


czestProbkowania =256
przefiltrowany1 = ag.pasmowozaporowy(mojeDane, czestProbkowania, 49,51)
przefiltrowany2 =  ag.gornoprzepustowy(przefiltrowany1, czestProbkowania, 3)


ag.spektrogram(przefiltrowany2, 256,)


ag.rysujFFT(przefiltrowany2[7*256:12*256])