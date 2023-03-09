def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
        indivíduo: lista contendo os genes das caixas binárias.
        
    Return:
        A soma dos genes do indivíduo.
    """
    return sum(individuo) 
