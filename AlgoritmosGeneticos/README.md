# Experimentos de otimização e algoritmos genéticos

Os experimentos realizados nessa seção correspondem à disciplina de Algoritmos Genéticos, feitos em sala de aula, com a ajuda e/ou orientação do professor Daniel Cassar e de colegas de classe.

## Funções

O arquivo funcoes.py permite a criação a de uma biblioteca própria com funções feitas em python puro, as quais foram feitas e utilizadas ao longo dos experimentos descritos a seguir.

## Experimento A.01

O experimento A.01 propõe a resolução do Problema das Caixas Binárias (individuo de maior soma, cada um possui 4 caixas e elas podem valer 0 ou 1) com o uso da Busca Aleatória, na qual, foram utilizadas três funções que quando utilizadas em conjunto, fornecem um número n de candidatos aleatórios e sua respectiva soma.

## Experimento A.02

O experimento A.02 mostra uma outra estratégia para a resolução do problema citado no A.01, onde usamos a Busca em Grade, na qual o produto cartesiano de duas maneiras diferentes para tentar resolver o problema usando todas as combinações possíveis.

## Experimento A.03

O experimento A.03 coloca como solução para o Problema das Caixas Binárias um primeiro Algoritmo Genérico, o qual usa dos conceitos descritos no notebook para selecionar os melhores individuos de uma população ao longo das gerações. Dessa forma, os individuos da população inicial com maior valor de função objetivo são selecionados e aparecem na população final. Isso não garante a obtenção do melhor individuo, então foram usados os mecanismos de cruzamento e mutação para aumentar a variabilidade genética ao longo das gerações, o que permite a seleção selecionar o melhor individuo, mas sem a garantia por causa do acaso.

## Experimento A.04

O experimento A.04 nos põe em frente a um problema semelhante dos experimentos anteriores, mas, dessa vez, temos Caixas Não-Binárias. Essas caixas podem, então, assumir valores diferentes de 0 ou 1, podem assumir os valores que quisermos. Assim, o algoritmo tenta encontrar, nesse caso, a maior soma com os genes podendo chegar em 100. Novamente, o algoritmo genético não garante que nós encontraremos o melhor indivíduo, porém podemos encontrar um que seja melhor que todos os indivíduos da população inicial.

## Experimento A.05

O experimento A.05 propõe o desafio de encontrar uma senha, sabendo a senha. Explicando melhor, o algoritmo genético irá selecionar, cruzar e mutar os indivíduos de uma população inicial usando o critério de distância. Para isso, os caracteres da senha são transformados em números e a distância para senha real é medida gene à gene e o fitness do indivíduo é a soma das distâncias de cada gene para o gene correto da senha. Logo, o algoritmo se mostra útil para encontrar/criar uma sequência ideal a partir de uma população inicial e critérios determinados.

## Experimento A.06

O experimento A.06 nos mostra um novo problema, o do caixeiro viajante. Nesse problema, um personagem fictício (o caixeiro) viaja um número finito de cidades conhecidas, sem passar pela mesma cidade mais de uma vez e com a intenção de percorrer a menor distância possível. Assim, nossos genes serão as cidades, nosso indivíduo possuirá uma ordem de genes que significa o caminho, a mutação será do tipo de troca de genes e o cruzamento possui dois cortes. Dessa forma, o problema se mostra diferente dos demais visitados anteriormente e é do tipo NP, o que é importante para ressaltar a importância de uma boa resposta fornecida pelo algoritmo genético.

##  Experimento A.07

O experimento A.07 visa encontrar uma boa resolução para o problema da mochila, o qual consiste na tentativa de acumular o maior valor monetário possível por meio de itens em uma mochila, a qual possui uma capacidade máxima de armazenamento quanto ao peso total desses itens. Então, o algoritmo genético possui o objetivo de encontrar qual indivíduo tem a melhor combinação de genes para esse problema. Vale notar que esse é mais um problema NP difícil e para garantir que a resposta dada pelo problema é a melhor, seria necessário verificar todas as possibilidades em uma busca exaustiva.