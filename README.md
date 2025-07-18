🛒 Gerenciador de Compras Online (CLI)

Um sistema simples de linha de comando (CLI) desenvolvido em Python para ajudar a rastrear e gerenciar suas compras online. Adicione, liste, atualize o status e veja o total gasto, tudo de forma organizada e persistente.

📜 Descrição

Este projeto é uma ferramenta de console que permite ao utilizador manter um registo de todas as suas compras online. As informações são salvas localmente num ficheiro compras.json, garantindo que os dados não são perdidos ao fechar o programa. 

É uma solução prática para quem quer organizar as suas compras sem a necessidade de aplicações complexas.✨ FuncionalidadesAdicionar Compra: Registe um novo item comprado, incluindo nome, preço e loja.

Listar Compras: Veja uma lista de todas as suas compras, ordenadas da mais recente para a mais antiga.Atualizar Status: Modifique o status de uma compra (ex: de "Processando" para "Enviado") e adicione um código de rastreio.Calcular

Gasto Total: Obtenha um resumo do valor total gasto em todas as compras registadas.Persistência de Dados: Todas as informações são salvas automaticamente num ficheiro compras.json.

🚀 Como Executar

Para executar este projeto, precisa de ter o Python 3 instalado no seu sistema.Clone o Repositório (ou Descarregue os Ficheiros)git clone https://github.com/pedrojtzonta/gerenciador-compras.git
cd gerenciador-compras

Se não usar o Git, basta descarregar o ficheiro gerenciador_compras.py.Navegue até à Pasta do ProjetoUse o seu terminal ou prompt de comando para aceder à pasta onde o ficheiro foi salvo.Execute o Scriptpython gerenciador_compras.py

Interaja com o MenuO programa irá apresentar um menu de opções no terminal. Digite o número da opção desejada e pressione Enter.🛠️ Tecnologias UtilizadasPython 3: Linguagem principal do projeto.Módulos Nativos do Python:json: Para serializar e desserializar os dados das compras.os: Para verificar a existência do ficheiro de dados.datetime: Para registar a data e hora de cada compra.

📂 Estrutura de Ficheiros.
├── gerenciador_compras.py   # O código principal da aplicação
└── compras.json             # Ficheiro de dados (criado automaticamente)
g
erenciador_compras.py: Contém toda a lógica do programa, incluindo as classes Compra e GerenciadorCompras, e a interface de menu.compras.json: Ficheiro onde as suas compras são armazenadas. Não o apague se não quiser perder os seus dados.
