import pyautogui
import tkinter as tk

def mostrar_posicao():
    # Obter a posição atual do mouse
    x, y = pyautogui.position()
    # Atualizar a etiqueta com as coordenadas do mouse
    etiqueta.config(text=f'X={x}, Y={y}')
    # Mover a janela para exibir as coordenadas na tela
    janela.geometry(f'+{x}+{y}')
    # Chamar esta função novamente após 100 milissegundos
    janela.after(100, mostrar_posicao)

# Criar uma janela
janela = tk.Tk()
janela.title('Mapeador de Posições')

# Criar uma etiqueta para exibir as coordenadas do mouse
etiqueta = tk.Label(janela, font=('Arial', 12))
etiqueta.pack(padx=10, pady=10)

# Desativar o redimensionamento da janela
janela.resizable(False, False)

# Chamar a função para mostrar a posição inicialmente
mostrar_posicao()

# Iniciar a janela
janela.mainloop()
