#!/usr/bin/python3
# encoding: utf-8

#Filtrar el blast obtenido
def filtrarblast():
	blastgeneral=open("lista_blast","r")
	blastfiltrado=open("lista_blast_filtrado","a")

	for line in blastgeneral.readlines():
		campos1=blastgeneral.split("\t")
		if(campos1[5]>=50 and campos1[4]>=30):
			blastfiltrado.write(campos1[0], "\t", campos1[1], "\t", campos1[2], "\t", campos1[3], "\t", campos1[4], "\t", campos1[5], "\t", campos1[6], "\n") 

	blastgeneral.close()
	blastfiltrado.close()

#Crear fasta del blast filtrado
def fastablast():
	blastfiltrado=open("lista_blast_filtrado","r")
	blastfasta=open("blast_fasta","a")

	for line in blastfiltrado.readlines():
		campos2=blastfiltrado.split("\t")
		blastfasta.write(">", campos2[2], "\n", campos2[3], "\n")

	blastfiltrado.close()
	blastfasta.close()
