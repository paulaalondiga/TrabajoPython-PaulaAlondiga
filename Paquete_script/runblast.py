#!/usr/bin/python3
# encoding: utf-8

#Modulos
import os
import subprocess as sp

#Blast
def correrblast():
	#Preguntar valor de evalue
	query_user=input("Escriba el path a su carpeta con los querys a usar: ")
	archivos_query=os.listdir(query_user)

	pregunta=input("¿Quiere establecer un evalue especifico? (Si/No): ")
	if(pregunta.lower()=="si"):
		N=input("Introduce un evalue: ")
	else:
		N="0.00001"
		print("El valor del evalue será por defecto 0.00001")

	#Hacer blast
	blastgeneral=open("lista_blast","a")
	for query_file  in archivos_query:
		actividad_blast=sp.Popen(['blastp','-query', query_user+'/'+query_file,'-subject', 'mis_genbanks.fasta', '-evalue', N, '-outfmt','6 qseqid qseq sseqid sseq qcovs pident evalue'], stdout=sp.PIPE)
		listado_blast=actividad_blast.stdout.read()
		blastgeneral.write(listado_blast)

	blastgeneral.close()
