# 🔐 Gerador de Senhas Seguras

   ![Gerador de Senhas funcionando](screenshot.png)

Aplicativo de desktop com interface gráfica que gera senhas aleatórias e seguras, com opções personalizáveis. Feito em Python com Tkinter.

## ✨ Funcionalidades

- Escolha do **tamanho** da senha (de 4 a 40 caracteres)
- Seleção dos tipos de caractere:
  - Letras maiúsculas (A-Z)
  - Letras minúsculas (a-z)
  - Números (0-9)
  - Símbolos (!@#$%&...)
- Botão para **copiar** a senha com um clique
- Geração segura usando o módulo `secrets` do Python

## 🛠️ Tecnologias

- **Python 3**
- **Tkinter** — interface gráfica (já incluída no Python)
- **secrets** — geração de valores aleatórios criptograficamente seguros
- **string** — conjuntos de caracteres

## 💻 Como executar

Você precisa ter o **Python 3** instalado.

1. Baixe ou clone este repositório
2. Abra o terminal na pasta do projeto
3. Execute:

```bash
python gerador_senhas.py
```

No Windows, também é possível dar dois cliques no arquivo `gerador_senhas.py`.

## 📁 Estrutura

```
gerador-senhas/
├── gerador_senhas.py   # código do aplicativo
├── README.md           # este arquivo
└── .gitignore          # arquivos ignorados pelo Git
```

## 🔒 Por que é seguro?

O programa usa o módulo `secrets`, recomendado pela documentação oficial do Python para gerar senhas e tokens. Diferente do `random` comum, ele é apropriado para fins de segurança.

## 👤 Autor



**William Santos** — automação e desenvolvimento

---

Projeto desenvolvido como parte do meu portfólio de Python.
