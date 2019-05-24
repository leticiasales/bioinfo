# coding=utf-8

min_val = 0

def frag(seq):
	#faz uma quebra aleatória do DNA
	#resultando em várias cópias quebradas 
	#em posições aleatórias de suas sequências
	return ['abc', 'cdef', 'fg', 'fghi']

def sym_val_2(a, b):
	#procurar pela existência de casamento 
	#entre o sufixo de a e o prefixo de b
	sym = []
	print('sym_val_2(' + a + ', ' + b + ')')
	for i in range(len(b)):
		aux = a.find(b[i:])
		if aux != -1:
			sym.append(aux)
		aux = a.find(b[:i])
		if aux != -1:
			sym.append(aux)
	# print(sym)
	return(max(sym, key=abs) if len(sym) else 0)

def sym_val_full(a, b):
	#escolhe máximo entra sym_val_2 para
	#a e b e sym_val_2 para b e a
  # print(a, b)
  c = sym_val_2(a, b)
  d = sym_val_2(b, a)
  if c == -1: return d
  if d == -1: return c
  # print (c, d)
  return c if (abs(c) > abs(d)) else d

def find_relevant(frags):
	#para todo par (a, b) chama sym_val_full(a, b)
	#se o retorno for maior que min_val
	#e diferente de 100%
	#adiciona a e b no valor de retorno
	for x in range(len(frags) - 1):
		for y in range(len(frags) - 1):
			print(sym_val_full(frags[x], frags[y + 1]))
	return(frags, frags)


def main():
	#lê sequencia
	seq = 'abcdefghi'

	#fragmenta sequencia
	frags = frag(seq)
	
	#encontra relevantes
	contigs, sym_val = find_relevant(frags)

	print(contigs)

	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val

	pass

main()