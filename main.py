#!/usr/bin/python3
# encoding: utf-8

#Importamos modulos del paquete a usar
import sys
import Paquete_script.genbankparse as gbp
import Paquete_script.runblast as rb
import Paquete_script.filtradoblast as fb
import Paquete_script.runmuscle as rm
import os


#Mensaje de ayuda
if(sys.argv[1]=="-h"):
	print("Este programa sirve para encontrar PBP en genomas ensamblados de la antártida:")
	print("Se realizará un blast para localizar los hits en dichos genomas")
	print("Con muscle se realizará un alineamiento y se generarán árboles filogenéticos correspondientes a cada query")
	print("Finalmente se mostraran dominios proteicos encontrados usando la BBDD Prosite")


#Parseo de los genbanks
gbp.parsear()


#Blastp
rb.correrblast()


#Filtrado de blast
fb.filtrarblast()


#Crear fasta del blast filtrado
fb.fastablast()


#Muscle:Alineamiento y Arbol filogénetico
rm.alinearmuscle("blast_fasta","Alineamiento.fa")
rm.arbolfilogenetico("blast_fasta","Arbol_filogenetico.fa")


#Guardar resultados en carpetas
num_veces=""
while True:
	try:
		resultados_dir=os.getcwd()+"/Resultadosejercicio"+num_veces
		os.mkdir(resultados_dir)
		break
	except:
		if num_veces:
			num_veces='('+str(int(num_veces[1:-1])+1)+')'
		else:
			num_veces='(1)'
			pass

os.rename('lista_blast',resultados_dir+'/lista_blast')
os.rename('lista_blast_filtrado',resultados_dir+'/lista_blast_filtrado')
os.rename('blast_fasta',resultados_dir+'/blast_fasta')
os.rename('Alineamiento.fa',resultados_dir+'/Alineamiento.fa')
os.rename('Arbol_filogenetico',resultados_dir+'/Arbol_filogenetico')
