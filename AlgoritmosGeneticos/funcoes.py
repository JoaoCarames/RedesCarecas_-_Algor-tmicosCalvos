import random

def gene_cb():
    """Fornece um gene válido ao problema das caixas binárias
    
    Return:
        Um valor zero ou um.
    """
    lista = [0,1]
    gene = random.choice(lista)
    
    return gene

def individuo_cb(n):
    """Gera um individuo ao problema das caixas binárias.
    
    Args:
        n: número de genes do indivíduo.
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    
    return individuo

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
        
    Return:
        A soma dos genes do indivíduo.
    """
    return sum(individuo)