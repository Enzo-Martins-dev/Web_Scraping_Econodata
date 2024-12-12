# Econodata Scraper
Este projeto visou o aprendizado de web scraping, utilizando a biblioteca Playwright em Python para realizar a automação de coleta de dados de empresas no site Econodata.  

Buscou-se acessar as páginas das empresas e extrair as informações que foram consideradas relevantes.


# Tecnologias Utilizadas
- Python (3.12.6): Linguagem de Programação base
- Playwright: Automação de navegador para extração de dados.
- Pandas: Manipulação de dados.
- OpenPyXL: Exportação dos dados para planilhas Excel.
- JSON: Armazenamento estruturado dos dados.
- CSV: Exportação inicial dos dados em forma de tabela.

# Funcionalidades
## Extração automatizada de informações:  
- Atividade econômica.
- Razão social.
- CNPJ.
- Situação.
- Endereço (logradouro, número, bairro, município, estado e CEP).
##  Armazenamento dos dados:
- Arquivos exportados em formato JSON, CSV e Excel.
- Organização dos campos do endereço em colunas específicas.

# Como Configurar o Ambiente
1. Clonar o Repositório

2. Instalar Dependências: 
- pip install -r requirements.txt

# Nota
Este projeto atualmente contém um problema ao tentar acessar os dados de uma empresa (S E I) da lista especificada.




