Sistema de Entrega de Pedidos
Este projeto fornece uma ferramenta para auxiliar os gestores na operação de uma empresa de entregas utilizando Python, Pandas e NumPy. A ferramenta processa dados de municípios, distâncias, centrais de distribuição (HUBs) e pedidos para calcular métricas específicas relacionadas às entregas.

Requisitos
Python 3.6+
Pandas
NumPy
Instalação
Certifique-se de ter o Python instalado em sua máquina. Você pode verificar a instalação executando python --version ou python3 --version no terminal ou prompt de comando.

Instale as bibliotecas necessárias (Pandas e NumPy) usando o pip, o gerenciador de pacotes do Python:

Copy code
pip install pandas numpy
Ou, se estiver usando Python 3 no Linux ou macOS:

Copy code
pip3 install pandas numpy
Uso
Copie o código fornecido para um arquivo chamado entrega.py.

Crie uma pasta chamada "dados" no mesmo diretório onde o arquivo entrega.py está localizado. Copie os arquivos de dados CSV e ZIP (mencionados no enunciado) para a pasta "dados".

Execute o arquivo entrega.py no terminal ou prompt de comando:

Copy code
python entrega.py
Ou, se estiver usando Python 3 no Linux ou macOS:

Copy code
python3 entrega.py
O script processará os dados e gerará um arquivo chamado "output.csv" no mesmo diretório. Este arquivo contém o resultado no formato solicitado.
Funcionalidades
A ferramenta realiza as seguintes tarefas:

Ler e tratar os dados.
Processar cada arquivo de pedido individualmente.
Determinar as seguintes métricas para cada HUB:
Total de Pedidos Alocados
Total de Pedidos Redirecionados Recebidos
Total de Pedidos Redirecionados Enviados
Total de Pedidos Não Entregues
Total de dias de entrega
Distância total da frota
Gerar um arquivo CSV de saída com as métricas calculadas.
Contribuição
Sinta-se à vontade para contribuir com este projeto, corrigindo bugs, melhorando a documentação ou adicionando novas funcionalidades.



