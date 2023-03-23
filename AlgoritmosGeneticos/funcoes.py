import random

#######################
### CAIXAS BINÁRIAS ###
#######################

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

def mutacao_cb(individuo):
    """Realiza a mutação de um gene
    
    Args:
        individuo: uma lista de genes
        
    Return:
        Um individuo com um gene mutado
    """
    gene_mutavel = random.randint(0, len(individuo) - 1)
    individuo[gene_mutavel] = gene_cb()
    
    return individuo

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
        
    Return:
        A soma dos genes do indivíduo.
    """
    return sum(individuo)

def funcao_objetivo_pop_cb(populacao):
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

###########################
### CAIXAS NÃO-BINÁRIAS ###
###########################

def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias
    
    Args:
        valor_max_caixa: Valor máximo que a caixa pode assumir
        
    Return:
        Um valor entre 0 e o valor máximo.
        
    """
    
    gene = random.randint(0, valor_max_caixa)
    return gene
    
def individuo_cnb(numero_genes, valor_max_caixa):
    """Gera um indivíduo válido para o problema das caixas não-binárias
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Return:
        Uma lista que representa um indivíduo válido para o problema das caixa não-binárias
    
    """
    
    individuo = []
    for _ in range(numero_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    """Gera uma população de individuos para o problema das caixas não-binárias
    
    Args:
        tamanho_populacao: número de indivíduos da população
        numero_genes: número de genes de cada indivíduo
        valor_max_caixa: valor máximo dos genes do indivíduo
        
    Return:
        Uma lista onde cada item representa um indivíduo.
    """
    
    populacao = []
    
    for _ in range(tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    
    return populacao

def funcao_objetivo_cnb(individuo):
    """Calcula o fitness do individuo para o problema das caixa não-binárias
    
    Args:
        individuo: lista que representa um individuo dentro do problema das caixas não-binárias
    
    Return:
        fitness: o valor da função objetivo para um determinado individuo
    
    """
    fitness = sum(individuo)
    
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    """Calcula o fitness da população completa
    
    Args:
        populacao: lista com todos os individuos da população
        
    Return:
        Uma lista com o fitness de cada indivíduo
      
    """
    
    fitness_pop = []
    
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    
    return fitness_pop
    
def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação do individuo
    
    Args:
        individuo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Return:
        individuo que sofreu uma mutação
        
    """
    gene_mutavel = random.randint(0, len(individuo) - 1)
    individuo[gene_mutavel] = gene_cnb(valor_max_caixa)
    
    return individuo

###############
### SELEÇÃO ###
###############

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

##################
### CRUZAMENTO ###
##################

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Args:
        Pai: uma lista representando um individuo.
        Mae: uma lista representando um individuo.
    
    Return:
        Duas listas, cada qual representa um filho dos pais.
    """
    ponto_de_corte = random.randint(1, len(mae) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

### Fim