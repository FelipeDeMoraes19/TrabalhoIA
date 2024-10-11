# 8 Puzzle Solver

**Este projeto implementa uma solução para o problema do 8-puzzle usando a **Busca em Profundidade de Aprofundamento Iterativo** (IDDFS). O projeto contém duas versões da busca: uma que utiliza cópia de estado e outra que modifica diretamente o estado atual, desfazendo as alterações conforme necessário.**

# Descrição dos Arquivos

`main.py`: Este é o ponto de entrada do projeto. Ele cria o estado inicial do 8-puzzle e executa as duas versões da busca (cópia de estado e modificação direta). O script também mede o tempo de execução de cada abordagem e exibe os resultados no console.

`src/iddfs_copy.py`: Neste arquivo está implementada a versão da busca IDDFS que utiliza cópia de estado. Para cada nó visitado, uma nova cópia completa do estado do tabuleiro é criada antes de realizar qualquer movimento. Isso garante que o estado original permaneça inalterado enquanto a busca avança, facilitando o retorno aos estados anteriores.

`src/performance.py`: Este arquivo contém a função compare_performance para comparar o desempenho das duas abordagens (cópia de estado e modificação direta). A função mede o tempo de execução de ambas as versões para um estado inicial do 8-puzzle e exibe os resultados em termos de tempo.

# Testes

`tests/test_puzzle.py`: Contém testes unitários para a classe PuzzleState, verificando se as funções de movimentos e verificação do estado objetivo estão funcionando corretamente.

`tests/test_iddfs_copy.py`: Testa a versão da busca com cópia de estado, verificando se a busca encontra corretamente o estado objetivo ou retorna None para estados sem solução.

`tests/test_iddfs_modify.py`: Testa a versão da busca com modificação direta de estado, garantindo que os resultados sejam consistentes com a versão que copia o estado.

# Como rodar o projeto

- *Certifique-se de ter o Python instalado e de ter instalado as dependências do projeto com:*

```
pip install -r requirements.txt
```

- *Para rodar o programa principal, execute o seguinte comando na raiz do projeto:*

```
python main.py
```

- *Isso irá executar a comparação de desempenho entre as duas abordagens e mostrar os tempos de execução no console.*
