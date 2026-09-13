"""
Gerador de Senhas Seguras
--------------------------
Aplicativo com interface grafica (Tkinter) que gera senhas
aleatorias e seguras, com opcoes personalizaveis.

Autor: William Santos
"""

import tkinter as tk
from tkinter import messagebox
import secrets   # modulo do Python para gerar valores aleatorios seguros
import string    # fornece conjuntos prontos de letras, numeros e simbolos


# ---------------------------------------------------------------
# Funcao que gera a senha de acordo com as opcoes escolhidas
# ---------------------------------------------------------------
def gerar_senha():
    tamanho = tamanho_var.get()

    # Monta o conjunto de caracteres permitidos com base nas caixas marcadas
    caracteres = ""
    if usar_maiusculas.get():
        caracteres += string.ascii_uppercase   # A-Z
    if usar_minusculas.get():
        caracteres += string.ascii_lowercase   # a-z
    if usar_numeros.get():
        caracteres += string.digits            # 0-9
    if usar_simbolos.get():
        caracteres += "!@#$%&*?-_+="           # simbolos escolhidos

    # Se o usuario nao marcou nenhuma opcao, avisa e para
    if not caracteres:
        messagebox.showwarning(
            "Atencao",
            "Selecione pelo menos um tipo de caractere."
        )
        return

    # Gera a senha sorteando um caractere por vez, de forma segura
    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))

    # Mostra a senha no campo de resultado
    campo_senha.delete(0, tk.END)
    campo_senha.insert(0, senha)


# ---------------------------------------------------------------
# Funcao que copia a senha gerada para a area de transferencia
# ---------------------------------------------------------------
def copiar_senha():
    senha = campo_senha.get()
    if not senha:
        messagebox.showinfo("Aviso", "Gere uma senha primeiro.")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiado", "Senha copiada para a area de transferencia!")


# ---------------------------------------------------------------
# Montagem da janela (interface grafica)
# ---------------------------------------------------------------
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("420x380")
janela.configure(bg="#1d2027")
janela.resizable(False, False)

# Cores usadas na interface (grafite + ambar)
COR_FUNDO = "#1d2027"
COR_TEXTO = "#e9eaec"
COR_AMBAR = "#f5a623"

# Titulo
titulo = tk.Label(
    janela, text="Gerador de Senhas",
    font=("Segoe UI", 18, "bold"),
    bg=COR_FUNDO, fg=COR_AMBAR
)
titulo.pack(pady=(20, 15))

# --- Controle de tamanho da senha ---
frame_tamanho = tk.Frame(janela, bg=COR_FUNDO)
frame_tamanho.pack(pady=5)

tk.Label(
    frame_tamanho, text="Tamanho:",
    font=("Segoe UI", 11), bg=COR_FUNDO, fg=COR_TEXTO
).pack(side=tk.LEFT, padx=5)

tamanho_var = tk.IntVar(value=12)   # tamanho padrao: 12 caracteres

tk.Scale(
    frame_tamanho, from_=4, to=40, orient=tk.HORIZONTAL,
    variable=tamanho_var, length=220,
    bg=COR_FUNDO, fg=COR_TEXTO, highlightthickness=0,
    troughcolor="#3a3f4b"
).pack(side=tk.LEFT)

# --- Caixas de selecao (checkboxes) ---
usar_maiusculas = tk.BooleanVar(value=True)
usar_minusculas = tk.BooleanVar(value=True)
usar_numeros = tk.BooleanVar(value=True)
usar_simbolos = tk.BooleanVar(value=True)

opcoes = [
    ("Letras maiusculas (A-Z)", usar_maiusculas),
    ("Letras minusculas (a-z)", usar_minusculas),
    ("Numeros (0-9)", usar_numeros),
    ("Simbolos (!@#$...)", usar_simbolos),
]

frame_opcoes = tk.Frame(janela, bg=COR_FUNDO)
frame_opcoes.pack(pady=10)

for texto, variavel in opcoes:
    tk.Checkbutton(
        frame_opcoes, text=texto, variable=variavel,
        font=("Segoe UI", 10), bg=COR_FUNDO, fg=COR_TEXTO,
        selectcolor="#282c35", activebackground=COR_FUNDO,
        activeforeground=COR_AMBAR, anchor="w", width=25
    ).pack(anchor="w")

# --- Botao gerar ---
tk.Button(
    janela, text="Gerar senha", command=gerar_senha,
    font=("Segoe UI", 12, "bold"), bg=COR_AMBAR, fg="#16181d",
    activebackground="#d98410", relief=tk.FLAT, padx=20, pady=6
).pack(pady=(10, 12))

# --- Campo que mostra a senha gerada ---
campo_senha = tk.Entry(
    janela, font=("Consolas", 13), justify="center",
    bg="#282c35", fg=COR_TEXTO, relief=tk.FLAT
)
campo_senha.pack(fill=tk.X, padx=30, ipady=6)

# --- Botao copiar ---
tk.Button(
    janela, text="Copiar", command=copiar_senha,
    font=("Segoe UI", 10), bg="#3a3f4b", fg=COR_TEXTO,
    activebackground="#4a505e", relief=tk.FLAT, padx=15, pady=4
).pack(pady=12)

# Inicia o programa (mantem a janela aberta)
janela.mainloop()
