import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import * 

#variaveis globais
player = True
count=0

def destroy():
    for widget in root.winfo_children():
        widget.destroy()

#funcionalidade botão
def clicked_button(b):
    global player
    global count 
    global board
    if b['text']== " " and player==True:
        b['text'] = "X"
        b.config(style='danger.TButton')
        player= False
        count= count + 1
        b_row = b.grid_info()['row']
        b_column = b.grid_info()['column']
        board[b_row][b_column] = "X"
        game()
    elif b['text']== " " and player==False:
        b['text'] = "O"
        b.config(style= 'info.TButton' )
        player=True
        count= count+1
        b_row = b.grid_info()['row']
        b_column = b.grid_info()['column']
        board[b_row][b_column] = "O"
        game()
        
    else:
        Messagebox.show_error("Este campo já está preenchido!", "Movimento inválido")
        


#o jogo em si:
def game():
    w= winner()
    if w== True:
        desativar()
    else:
        cheker()

def winner():
        for row in range (3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
                Messagebox.show_info("Você ganhou! ", 'Jogo da velha')
                return True
        for column in range (3):
            if board[0][column] == board[1][column] == board[2][column] and board[0][column] != " ":
                Messagebox.show_info("Você ganhou! ", 'Jogo da velha')
                return True
        if board[0][0] == board[1][1]== board[2][2] and board [0][0] != " ":
            Messagebox.show_info("Você ganhou! ", 'Jogo da velha')
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            Messagebox.show_info("Você ganhou! ", 'Jogo da velha')
            return True

#função para checkar o vencedor ou empate
def cheker():
    if count==9:
        Messagebox.show_info("Deu velha! ", 'Jogo da velha')
        desativar()

#função desativar os botões
def desativar():
    destroy()
    global player 
    global board
    global count
    player=True
    board = [[" " for _ in range(3)] for _ in range(3)]
    count=0
    label= ttk.Label(text= 'Obrigado por jogar', font= ("Helvetica", 20))
    label.pack(pady= 10)
    bu= ttk.Button(text='Reiniciar', style='info.TButton', command=main_menu)
    bu.pack (pady=20)

def main_menu():
    destroy()
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    # Criação dos botões
    b1 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b1))
    b2 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b2))
    b3 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b3))
 
    b4 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b4))
    b5 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b5))
    b6 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b6))

    b7 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b7))
    b8 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b8))
    b9 = ttk.Button(text=" ", style="default.TButton", command= lambda: clicked_button(b9))


    # Posicionamento dos botões
    b1.grid(row=0, column=0, padx=3, pady=3)
    b2.grid(row=0, column=1, padx=3, pady=3)
    b3.grid(row=0, column=2, padx=3, pady=3)

    b4.grid(row=1, column=0, padx=3, pady=3)
    b5.grid(row=1, column=1, padx=3, pady=3)
    b6.grid(row=1, column=2, padx=3, pady=3)

    b7.grid(row=2, column=0, padx=3, pady=3)
    b8.grid(row=2, column=1, padx=3, pady=3)
    b9.grid(row=2, column=2, padx=3, pady=3)


# Criação da janela
root = ttk.Window(themename='darkly')
root.title("Jogo da Velha")
root.geometry("390x385")

# Criação de estilo
my_style = ttk.Style()
my_style.configure('default.TButton', font=('Helvetica', 20), height= 3, width=6, padding=(6, 40))

x_style = ttk.Style()
x_style.configure('danger.TButton', font=('Helvetica', 20), height= 3, width=6, padding=(6, 40))

o_style = ttk.Style()
o_style.configure('info.TButton', font=('Helvetica', 20), height= 3, width=6, padding=(6, 40))

main_menu()
# Inicialização da interface
root.mainloop()
