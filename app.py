import streamlit as st
import pandas as pd
import json
import os
import datetime
from gerador_pdf import criar_pdf_apr 

st.set_page_config(page_title="APR 4SAS - Gestão de Riscos", layout="wide")

@st.cache_data
def load_data():
    with open('riscos_db_clean.json', 'r', encoding='utf-8') as f:
        return json.load(f)

riscos_db = load_data()

# --- BARRA LATERAL ---
# Tenta carregar o logótipo da 4SAS. Se não achar, escreve o texto.
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)
else:
    st.sidebar.title("4SAS Offshore")
    st.sidebar.markdown("*Precisão além da superfície*")

st.sidebar.divider()

st.sidebar.header("1. Detalhes da Campanha")
colaborador = st.sidebar.text_input("Nome do Colaborador (Autor)")
data_apr = st.sidebar.date_input("Data da APR", datetime.date.today())
os_num = st.sidebar.text_input("Número da OS")
local = st.sidebar.text_input("Local da Operação")

st.sidebar.header("2. Seleção de Equipamentos")
sensores = ["SBES", "MBES", "SSS", "MAG", "SBP", "Sísmica Monocanal", "Sísmica Multicanal", "Vibro Core", "Jet Probe"]
selecao_sensores = st.sidebar.multiselect("Marque os sensores da OS:", sensores)

st.sidebar.header("3. Controle de Revisão")
st.sidebar.write("Edite a tabela abaixo para atualizar o histórico. A última linha define a revisão atual do documento.")
# Cria uma tabela interativa no Streamlit para gerenciar as revisões
historico_padrao = pd.DataFrame([
    {"Rev": 0, "Data": data_apr.strftime('%d/%m/%Y'), "Autor": colaborador if colaborador else "Autor", "Descrição": "Emissão Inicial"}
])
historico_df = st.sidebar.data_editor(historico_padrao, num_rows="dynamic", use_container_width=True)

# Lógica de filtragem
riscos_filtrados = []
for r in riscos_db:
    tags = r.get("sensores_aplicaveis", ["Geral"])
    if "Geral" in tags:
        riscos_filtrados.append(r)
    elif any(sensor in tags for sensor in selecao_sensores):
        riscos_filtrados.append(r)

# --- ÁREA PRINCIPAL ---
st.title("Análise Preliminar de Risco (APR)")

if os_num and local and colaborador and selecao_sensores:
    st.success(f"**Colaborador:** {colaborador} | **OS:** {os_num} | **Local:** {local}")
    
    fases = sorted(list(set([r['categoria_fase'] for r in riscos_filtrados])))
    aba_selecionada = st.selectbox("Selecione a Fase para Revisão de Riscos:", fases)
    
    st.markdown(f"### Riscos Mapeados: {aba_selecionada} ({len([r for r in riscos_filtrados if r['categoria_fase'] == aba_selecionada])} aplicáveis)")
    riscos_fase = [r for r in riscos_filtrados if r['categoria_fase'] == aba_selecionada]
    
    for risco in riscos_fase:
        with st.expander(f"{risco['id']} - {risco['tarefa']} | Nível Inicial: {risco['risco_inicial']['nivel']}"):
            st.write(f"**Perigo:** {risco['perigo']}")
            st.write(f"**Consequências:** {risco['consequencias']}")
            st.info(f"**Mitigação 4SAS:** {risco['mitigacao']['medidas_padrao']}")
    
    st.divider()
    st.subheader("Finalizar Documentação")
    if st.button("📄 Gerar Relatório PDF da APR", use_container_width=True):
        with st.spinner("A desenhar matriz de risco em PDF..."):
            # Converte a tabela do Streamlit para um dicionário para enviar ao PDF
            historico_dict = historico_df.to_dict('records')
            
            arquivo_gerado = criar_pdf_apr(os_num, local, selecao_sensores, riscos_filtrados, colaborador, data_apr.strftime('%d/%m/%Y'), historico_dict)
            
            with open(arquivo_gerado, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="📥 Baixar PDF Finalizado", data=PDFbyte, file_name=arquivo_gerado, mime='application/octet-stream', type="primary")
else:
    st.info("👈 Preencha todos os dados na barra lateral (Colaborador, OS, Local e Sensores) para visualizar a matriz.")
