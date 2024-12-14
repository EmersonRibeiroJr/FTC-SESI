import streamlit as st
import pandas as pd

# Dados das equipes
if 'teams' not in st.session_state:
    st.session_state.teams = []

# Adicionar equipe
st.title("Gerenciador de Equipes")
with st.form("add_team_form"):
    team_name = st.text_input("Nome da Equipe:")
    submitted = st.form_submit_button("Adicionar Equipe")
    if submitted:
        if team_name and team_name not in [team['name'] for team in st.session_state.teams]:
            st.session_state.teams.append({'name': team_name, 'points': 0})
            st.success(f"Equipe '{team_name}' adicionada!")
        elif team_name:
            st.warning("Essa equipe já foi cadastrada.")
        else:
            st.error("Por favor, insira um nome válido.")

# Mostrador de equipes
st.subheader("Equipes e Pontuações")
if st.session_state.teams:
    for team in st.session_state.teams:
        team['points'] += st.number_input(f"Adicionar pontos para {team['name']}:", 0, step=1, key=team['name'])
else:
    st.write("Nenhuma equipe cadastrada.")

# Salvar em Excel
if st.button("Salvar em Excel"):
    if st.session_state.teams:
        df = pd.DataFrame(st.session_state.teams)
        df.to_excel("teams_data.xlsx", index=False)
        st.success("Os dados foram salvos no arquivo 'teams_data.xlsx'.")
    else:
        st.warning("Não há dados para salvar.")
