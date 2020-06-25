#!/usr/bin/python3
# encoding: utf-8

#Modulos usados
from Bio import Seq, SeqIO
import os

#Creacion del multifasta para las secuencias subject del blast
def parsear():
	gbk=open("mis_genbanks.fasta","a")
	carpeta=input("Escriba el path a su carpeta con los genbanks: ")

	archivos=os.listdir(carpeta)
	for carpeta+'/'+file in archivos:
		with open(file, "r") as input_handle:
			for record in SeqIO.parse(input_handle, "genbank"):
				for feature in record.features:
					if feature.type == 'CDS':
						try:
							seq=feature.qualifiers['translation'][0]
						except:
							seq="nada"

						if(seq != "nada"):
							gbk.write(">" + feature.qualifiers['locus_tag'][0] + "\n" + seq + "\n")
							gbk.close()

