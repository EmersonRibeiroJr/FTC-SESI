import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Lista para armazenar equipes e pontuações
teams = []

# Função para adicionar uma equipe
def add_team():
    team_name = entry_team.get().strip()
    if team_name:
        if team_name not in [team['name'] for team in teams]:
            teams.append({'name': team_name, 'points': 0})
            update_team_list()
            entry_team.delete(0, tk.END)
        else:
            messagebox.showwarning("Equipe já existe", "Essa equipe já foi cadastrada.")
    else:
        messagebox.showwarning("Nome inválido", "Digite um nome válido para a equipe.")

# Função para atualizar a lista de equipes no mostrador
def update_team_list():
    for row in tree.get_children():
        tree.delete(row)
    for i, team in enumerate(teams):
        tree.insert('', 'end', iid=i, values=(team['name'], team['points']))

# Função para adicionar pontos com base nas regras
def add_points():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Nenhuma equipe selecionada", "Selecione uma equipe para adicionar pontos.")
        return

    team_index = int(selected_item[0])
    total_points = 0

    # Regras de pontuação
    if inspection_var.get():
        total_points += 20
    if coral_tree_var.get():
        total_points += 20
    if coral_base_var.get():
        total_points += 10
    if coral_branches_var.get():
        total_points += 20
    if shark_cave_var.get():
        total_points += 20
    if shark_habitat_var.get():
        total_points += 10
    if coral_reef_var.get():
        total_points += 20
    if reef_segments_var.get():
        total_points += 5 * min(reef_segments_spinbox.get(), 3)

    # Adicionar pontos à equipe
    teams[team_index]['points'] += total_points
    update_team_list()

# Função para salvar os dados em um arquivo Excel
def save_to_excel():
    if teams:
        df = pd.DataFrame(teams)
        df.to_excel('teams_data.xlsx', index=False)
        messagebox.showinfo("Salvo com sucesso", "Os dados foram salvos em 'teams_data.xlsx'.")
    else:
        messagebox.showwarning("Sem dados", "Não há equipes para salvar.")

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Equipes - Regras de Pontuação")

# Frame para cadastro de equipes
frame_add_team = ttk.LabelFrame(root, text="Adicionar Equipe")
frame_add_team.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

ttk.Label(frame_add_team, text="Nome da equipe:").grid(row=0, column=0, padx=5, pady=5)
entry_team = ttk.Entry(frame_add_team, width=30)
entry_team.grid(row=0, column=1, padx=5, pady=5)

btn_add_team = ttk.Button(frame_add_team, text="Adicionar", command=add_team)
btn_add_team.grid(row=0, column=2, padx=5, pady=5)

# Frame para o mostrador de equipes
frame_team_list = ttk.LabelFrame(root, text="Lista de Equipes")
frame_team_list.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tree = ttk.Treeview(frame_team_list, columns=("Equipe", "Pontos"), show='headings', height=10)
tree.heading("Equipe", text="Equipe")
tree.heading("Pontos", text="Pontos")
tree.column("Equipe", width=150)
tree.column("Pontos", width=50)
tree.pack(padx=5, pady=5)

# Frame para adicionar pontos
frame_add_points = ttk.LabelFrame(root, text="Adicionar Pontos")
frame_add_points.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Regras de pontuação
inspection_var = tk.BooleanVar()
coral_tree_var = tk.BooleanVar()
coral_base_var = tk.BooleanVar()
coral_branches_var = tk.BooleanVar()
shark_cave_var = tk.BooleanVar()
shark_habitat_var = tk.BooleanVar()
coral_reef_var = tk.BooleanVar()
reef_segments_var = tk.BooleanVar()
reef_segments_spinbox = tk.IntVar(value=0)

ttk.Checkbutton(frame_add_points, text="Inspeção de equipamentos (20 pontos)", variable=inspection_var).grid(row=0, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Árvore de corais pendurada (20 pontos)", variable=coral_tree_var).grid(row=1, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Base da árvore no encaixe (10 pontos)", variable=coral_base_var).grid(row=2, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Ramos de coral virados para cima (20 pontos)", variable=coral_branches_var).grid(row=3, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Tubarão fora da caverna (20 pontos)", variable=shark_cave_var).grid(row=4, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Tubarão no habitat (10 pontos)", variable=shark_habitat_var).grid(row=5, column=0, sticky="w")
ttk.Checkbutton(frame_add_points, text="Recife de coral virado para cima (20 pontos)", variable=coral_reef_var).grid(row=6, column=0, sticky="w")

ttk.Checkbutton(frame_add_points, text="Segmento recifal (5 pontos/até 3x)", variable=reef_segments_var).grid(row=7, column=0, sticky="w")
ttk.Label(frame_add_points, text="Nº de segmentos:").grid(row=7, column=1)
ttk.Spinbox(frame_add_points, from_=0, to=3, textvariable=reef_segments_spinbox, width=5).grid(row=7, column=2)

# Botões
btn_add_points = ttk.Button(frame_add_points, text="Adicionar Pontos", command=add_points)
btn_add_points.grid(row=8, column=0, padx=5, pady=5)

btn_save = ttk.Button(root, text="Salvar em Excel", command=save_to_excel)
btn_save.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()
