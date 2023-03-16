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

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho: número de indivíduos da população.
        n: número de genes de cada indivíduo.
    Return:
        Uma lista onde cada item é um individuo. Um individuo é uma lista de genes.
    """
    populacao = []
    
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.
    
    Nota: Funcional apenas para problemas de maximização.
    
    Args:
        populacao: lista de individuos.
        fitness: lista com o valor da função objetivo dos individuos
    
    Return:
        População de individuos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
        
    Return:
        A soma dos genes do indivíduo.
    """
    return sum(individuo)

def funcao_objetivos_pop_cb(populacao):
    """Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        população: lista com todos os individuos da população.
    
    Return:
        Lista de valores representando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    
    return fitness

