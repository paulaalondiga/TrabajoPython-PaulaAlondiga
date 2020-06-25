#!/usr/bin/python3
# encoding: utf-8

#Modulos
from Bio.Applications import MuscleCommandline
import subprocess as sp

#Muscle alineamiento
def alinermuscle(input, output):
        muscle_cline=MuscleCommandline(input=input, out=output)
        stdout, stderr=muscle_cline()
	return

#Muscle árbol
def arbolfilogenetico(input,output):
	sp.call(['muscle','-maketree', '-in', input, '-out', output, '-cluster', 'neighborjoining'])
	return
