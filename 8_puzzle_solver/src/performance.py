import time
from src.iddfs_copy import iddfs_copy 
from src.iddfs_modify import iddfs_modify  

def compare_performance(root, max_depth):
    # Medir desempenho da versão com cópia de estado
    start_time = time.time()
    result_copy = iddfs_copy(root, max_depth)
    copy_time = time.time() - start_time
    
    # Medir desempenho da versão com modificação direta
    start_time = time.time()
    result_modify = iddfs_modify(root, max_depth)
    modify_time = time.time() - start_time
    
    # Exibir os resultados de tempo
    print(f"Tempo (Cópia de estado): {copy_time:.4f} segundos")
    print(f"Tempo (Modificação direta): {modify_time:.4f} segundos")
