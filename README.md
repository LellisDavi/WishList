📋 WishList

Sistema de organização financeira pessoal desenvolvido em Python, com foco em Programação Orientada a Objetos. O projeto classifica automaticamente os itens que você deseja comprar entre Desejo e Necessidade, ajudando a visualizar melhor onde seu dinheiro está indo — e a priorizar o que realmente importa.

🏍️ A motivação: tirei minha habilitação de moto e comecei a me organizar financeiramente pra comprar uma. O WishList nasceu como uma forma de unir esse objetivo pessoal com a prática de programação.

💡 Como funciona

A ideia central é simples:

Você cadastra categorias (ex: Saúde, Higiene, Entretenimento), definindo se cada uma representa uma Necessidade ou um Desejo
Você cadastra itens que quer comprar, vinculando cada um a uma categoria
O sistema classifica automaticamente o item com base na categoria escolhida
Quando um item é comprado, ele não é apagado — só muda de status para "adquirido", ficando disponível numa lista separada

Critério de classificação:

Se o item resolve um problema real da vida → Necessidade
Se é motivado por sentimento ou vontade → Desejo
🖥️ Funcionalidades

O sistema roda via terminal, com um menu interativo:

--- MENU WISHLIST ---
[1] ADICIONAR CATEGORIA
[2] LISTAR CATEGORIA
[3] ADICIONAR ITEM
[4] LISTAR ITENS
[5] MARCAR ITEM COMO ADQUIRIDO
[6] LISTAR ADQUIRIDOS
[7] SAIR
✅ Cadastro de categorias (com verificação de duplicidade, sem diferenciar maiúsculas/minúsculas)
✅ Cadastro de itens, vinculados a uma categoria já existente
✅ Listagem de itens separada visualmente entre Necessidade x Desejo
✅ Marcação de itens como adquiridos, mantendo o histórico
✅ Listagem exclusiva dos itens já adquiridos
🏗️ Arquitetura

O projeto segue uma separação de responsabilidades em camadas, um princípio de design que evita misturar lógica de negócio, acesso a dados e interface:

WishList/
├── main.py                  # Ponto de entrada — menu do terminal
├── models/                  # Classes de domínio (não sabem de banco nem de menu)
│   ├── categoria.py
│   └── item.py
├── repositorio/              # Camada de acesso a dados (só fala com o SQLite)
│   └── repositorio.py
├── services/                 # Regras de negócio — orquestra tudo
│   └── wishlist.py
└── database/
    └── wishlist.db           # Banco SQLite (gerado em tempo de execução)
Classes principais
Classe	Responsabilidade
Categoria	Representa uma categoria (nome, tipo, id)
Item	Representa um item desejado (nome, preço, categoria, status), com o método obter_tipo() que consulta o tipo através da categoria vinculada
Repositorio	Único ponto de contato com o banco SQLite — insere, busca e atualiza dados
Wishlist	Orquestra as regras de negócio (ex: evitar categorias duplicadas) e conecta o menu ao repositório
Modelo de dados (SQLite)
categoria                    item
├── id (PK)                  ├── id (PK)
├── nome                     ├── nome
└── tipo                     ├── preco
                              ├── categoria_id (FK → categoria.id)
                              └── status
🛠️ Tecnologias e conceitos aplicados
Python 3 — orientação a objetos (encapsulamento, composição entre classes)
SQLite — persistência de dados, com relacionamento via chave estrangeira
Padrão Repository — separação entre lógica de negócio e acesso ao banco
Prepared statements (?) — prevenção contra SQL Injection
Git/GitHub — versionamento do projeto
🚀 Como rodar o projeto
bash
# Clone o repositório
git clone https://github.com/LellisDavi/WishList.git
cd WishList

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate.ps1      # Windows (PowerShell)

# Rode o programa
python main.py

O banco de dados SQLite é criado automaticamente na primeira execução — não é necessário nenhuma configuração adicional.
