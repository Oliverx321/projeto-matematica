import streamlit as st
import numpy as np
import scipy.stats as stats

# Configuração da página
st.set_page_config(page_title="Projeto de Matemática", layout="centered")
st.title("📊 Aplicativo de Probabilidade e Vetores")

# Menu de navegação lateral
opcao = st.sidebar.selectbox("Escolha o Módulo", ["Início", "Probabilidade", "Cálculo de Vetores"])

if opcao == "Início":
    st.write("### Bem-vindo ao projeto!")
    st.write("Use o menu lateral para navegar entre os módulos de Probabilidade e Vetores.")
    st.info("Desenvolvido para a entrega do dia 14/08.")

# MÓDULO 1: PROBABILIDADE
elif opcao == "Probabilidade":
    st.header("🎲 Distribuição de Probabilidade (Binomial)")
    st.write("A distribuição binomial calcula a probabilidade de um número de sucessos em experimentos independentes.")
    
    # Entradas do usuário
    n = st.number_input("Número total de tentativas (n)", min_value=1, value=10)
    p = st.slider("Probabilidade de sucesso em cada tentativa (p)", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    k = st.number_input("Número de sucessos desejados (k)", min_value=0, max_value=n, value=5)
    
    if st.button("Calcular Probabilidade"):
        # Cálculo usando scipy
        prob = stats.binom.pmf(k, n, p)
        st.success(f"A probabilidade exata de obter {k} sucessos é: **{prob:.4f} ({prob*100:.2f}%)**")

# MÓDULO 2: VETORES (Com situação prática)
elif opcao == "Cálculo de Vetores":
    st.header("📐 Cálculo de Vetores")
    
    st.subheader("Situação Problema: Navegação de Drone")
    st.write("""
    **Cenário:** Um drone de entrega realiza dois deslocamentos consecutivos no espaço (2D). 
    Insira os componentes dos vetores de movimento para calcular o deslocamento resultante final.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Vetor A (Primeiro movimento)**")
        ax = st.number_input("Componente X (A)", value=3.0)
        ay = st.number_input("Componente Y (A)", value=4.0)
    with col2:
        st.write("**Vetor B (Segundo movimento)**")
        bx = st.number_input("Componente X (B)", value=1.0)
        by = st.number_input("Componente Y (B)", value=2.0)
        
    if st.button("Calcular Resultante"):
        # Operações com vetores
        rx = ax + bx
        ry = ay + by
        magnitude = np.sqrt(rx**2 + ry**2)
        
        st.success(f"**Vetor Resultante R:** ({rx}, {ry})")
        st.success(f"**Distância em linha reta até o destino (Magnitude):** {magnitude:.2f} unidades")