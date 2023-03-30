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

#############
### SENHA ###
#############

def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

##################
### PALINDROMO ###
##################

def gene_palindromo(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

def individuo_palindromo(tamanho_palindromo, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_palindromo):
        candidato.append(gene_palindromo(letras))

    return candidato

def populacao_inicial_palindromo(tamanho, tamanho_palindromo, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_palindromo(tamanho_palindromo, letras))
    return populacao

def mutacao_palindromo(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_palindromo(letras)
    return individuo

def funcao_objetivo_palindromo(individuo):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0
    palindromo = individuo[::-1]
    for letra_candidato, letra_oposta in zip(individuo, palindromo):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oposta))

    return diferenca

def funcao_objetivo_pop_palindromo(populacao):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_palindromo(individuo))

    return resultado

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

def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados

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