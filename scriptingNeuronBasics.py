# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 12:14:11 2021

@author: hyewon
"""

from neuron import h, rxd
from neuron.units import ms, mV
import textwrap
import matplotlib.pyplot as plt
import csv

soma = h.Section(name='soma')
soma.L = 20
soma.diam = 20

#print(textwrap.fill(', '.join(dir(h))))

soma.insert('hh')

iclamp = h.IClamp(soma(0.5))
iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9

v = h.Vector().record(soma(0.5)._ref_v)           # Membrane potential vector
t = h.Vector().record(h._ref_t)                   # Time stamp vector

h.load_file('stdrun.hoc')
h.finitialize(-65 * mV)
h.continuerun(40 * ms)

f1 = plt.figure()
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.plot(t, v, linewidth=2)
plt.show(f1)


with open('data.csv', 'w') as f:
    csv.writer(f).writerows(zip(t, v))