import kagglehub
import pandas as pd
import os


def dataset_load(dataset_id):
   
    # Baixar o conjunto de dados
    path = kagglehub.dataset_download(dataset_id)

    # Listar os arquivos no diretório
    files = os.listdir(path)
    
    # Procurar o arquivo com a extensão desejada
    file = None
    for f in files:
        
            file = os.path.join(path, f)
            break
    
    if file:
        # Ler o arquivo com a extensão desejada
            return pd.read_csv(file)
        
    else:
        raise FileNotFoundError(f"Arquivo com extensão não encontrado no diretório.")
