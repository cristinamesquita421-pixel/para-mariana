from tkinter import *
from tkinter import messagebox
import random

janela = Tk()
janela.title("Carta ❤️")
janela.geometry("700x500")
janela.config(bg="#ffd6e0")

def abrir_carta():
    titulo.pack_forget()
    botao_abrir.pack_forget()

    mensagem = """
Oi amor ❤️

Se você está lendo isso,
é porque eu quis fazer algo especial pra vc rs.

Talvez não seja perfeito KKKK
mas foi feito com carinho.

Você me faz muito feliz ❤️
E eu gosto muito de passar tempo com você.
"""

    texto.config(text="")

    def escrever(i=0):
        if i < len(mensagem):
            texto.config(text=mensagem[:i+1])
            janela.after(35, escrever, i+1)

    escrever()

titulo = Label(
    janela,
    text="✉️\n\nVocê recebeu uma carta",
    font=("Arial", 24),
    bg="#ffd6e0"
)

titulo.pack(pady=50)

botao_abrir = Button(
    janela,
    text="Abrir carta ❤️",
    font=("Arial", 16),
    command=abrir_carta
)

botao_abrir.pack()

texto = Label(
    janela,
    text="",
    font=("Arial", 16),
    bg="#ffd6e0",
    justify="center"
)

texto.pack(pady=30)

motivos = [
    "Seu jeito me conquista todo dia ❤️",
    "Sua personalidade é incrível",
    "Seu cabelo é lindo demais KKKK",
    "Sua gentileza me acalma ❤️",
    "Você consegue me fazer sorrir mesmo nos dias ruins",
    "Eu amo passar tempo com você ❤️",
    "Você é muito perfeita ❤️",
    "Você é engraçada sem nem perceber KKKK",
    "Você faz minha vida ficar mais leve ❤️",
    "Seu carinho é viciante",
    "Você é muito especial pra mim ❤️",
    "Eu amo nossas conversas",
    "Você me faz sentir importante ❤️",
    "Até seu ciúme às vezes fica fofo KKKK"
]

def mostrar_motivo():
    texto_motivo.config(
        text=random.choice(motivos)
    )

botao_motivo = Button(
    janela,
    text="💌 Motivos que eu gosto de você",
    font=("Arial", 12),
    command=mostrar_motivo
)

botao_motivo.pack(pady=10)

texto_motivo = Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#ffd6e0"
)

texto_motivo.pack()
def mensagem_triste():
    messagebox.showinfo(
        "Pra você ❤️",
        "Ei.\n\nMesmo nos dias ruins,\nvc continua sendo incrível ❤️\n\nEu sempre vou estar aqui pra você."
    )

botao_triste = Button(
    janela,
    text="🌧️ Abra quando estiver triste",
    font=("Arial", 12),
    command=mensagem_triste
)

botao_triste.pack(pady=10)
from datetime import datetime

data_inicio = datetime(2026, 1, 16)

def mostrar_tempo():
    agora = datetime.now()
    diferenca = agora - data_inicio

    dias = diferenca.days
    horas = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60

    texto_tempo.config(
        text=f"⏳ Estamos juntos há:\n{dias} dias\n{horas} horas\n{minutos} minutos ❤️"
    )

botao_tempo = Button(
    janela,
    text="⏳ Nosso tempo juntos",
    font=("Arial", 12),
    command=mostrar_tempo
)

botao_tempo.pack(pady=10)

texto_tempo = Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#ffd6e0"
)

texto_tempo.pack()
def segredo():
    messagebox.showinfo(
        "Segredo ❤️",
        "Você encontrou a mensagem secreta 😳\n\nEU TE AMO NENEM ❤️"
    )

botao_secreto = Button(
    janela,
    text=".",
    command=segredo,
    bg="#ffd6e0",
    bd=0
)

botao_secreto.place(x=680, y=480)
mostrar = True

def piscar():
    global mostrar

    if mostrar:
        texto_amor.config(text="EU AMOOOOOOO VC ❤️")
    else:
        texto_amor.config(text="")

    mostrar = not mostrar

    janela.after(700, piscar)

texto_amor = Label(
    janela,
    text="",
    font=("Arial", 22),
    bg="#ffd6e0"
)

texto_amor.pack(pady=20)

piscar()
janela.mainloop()