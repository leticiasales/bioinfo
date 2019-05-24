# coding=utf-8

min_val = 0

def frag(seq):
	#faz uma quebra aleatória do DNA
	#resultando em várias cópias quebradas 
	#em posições aleatórias de suas sequências
	return []

def sym_val_2(a, b):
	#procurar pela existência de casamento 
	#entre o sufixo de a e o prefixo de b
	pass

def sym_val_full():
	#escolhe máximo entra sym_val_2 para
	#a e b e sym_val_2 para b e a
	pass

def find_relevant(frags):
	#para todo par (a, b) chama sym_val_full(a, b)
	#se o retorno for maior que min_val
	#e diferente de 100%
	#adiciona a e b no valor de retorno
	pass

def main():
	#lê sequencia
	seq = ''

	#fragmenta sequencia
	frags = frag(seq)
	
	#encontra relevantes
	contigs, sym_val = find_relevant(frags)

	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val

	pass

main()