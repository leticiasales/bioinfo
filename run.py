# coding=utf-8

min_val = 0

def frag(seq):
	#faz uma quebra aleatória do DNA
	#resultando em várias cópias quebradas 
	#em posições aleatórias de suas sequências
	return ['abc', 'cdef', 'fg', 'fghi', 'da']

def sym_val_2(a, b):
	#procurar pela existência de casamento 
	#entre o sufixo de a e o prefixo de b
	sym = []
	for i in range(len(b)):
		aux = a.find(b[i:])
		if aux != -1:
			size = len(b[i:])
			sym.append(-1 * size)
		aux = a.find(b[:i])
		if aux != -1:
			size = len(b[:i])
			sym.append(size)
	return(max(sym, key=abs) if len(sym) else 0)

def sym_val_full(a, b):
	#escolhe máximo entra sym_val_2 para
	#a e b e sym_val_2 para b e a
  return sym_val_2(a, b)

def find_relevant(frags):
	#para todo par (a, b) chama sym_val_full(a, b)
	#se o retorno for maior que min_val
	#e diferente de 100%
	#adiciona a e b no valor de retorno
	sym=[];orig=[];dest=[];
	for x in range(len(frags) - 1):
		for y in range(len(frags) - 1):
			if x != (y + 1): 
				aux = sym_val_full(frags[x], frags[y + 1])
				# exit()
				print(frags[x], frags[y + 1])
				print(aux)
				if abs(aux) > min_val:
					sym.append(aux)
					orig.append(frags[x])
					dest.append(frags[y + 1])
	return(sym, orig, dest)


def main():
	#lê sequencia
	seq = 'abcdefghi'

	#fragmenta sequencia
	frags = frag(seq)
	
	#encontra relevantes
	sym, orig, dest = find_relevant(frags)

	print(sym)
	print(orig)
	print(dest)

	#para todos os contigs
		#add contigs no grafo G como vértice 
		#orientação das arestas é dada pela ordem do casamento
		#peso da aresta é dado pelo sym_val

	pass

main()