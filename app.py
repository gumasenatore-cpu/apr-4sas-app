import streamlit as st
import pandas as pd
import json
import os
import datetime
import copy
from gerador_pdf import criar_pdf_apr 

st.set_page_config(page_title="APR 4SAS - Gestão de Riscos", layout="wide")

if 'riscos_customizados' not in st.session_state:
    st.session_state.riscos_customizados = []

@st.cache_data
def load_data():
    try:
        with open('riscos_db_clean.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

riscos_db = load_data()

# --- BARRA LATERAL ---
col_espaco1, col_logo, col_espaco2 = st.sidebar.columns([1, 2, 1])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.markdown("### 4SAS")

st.sidebar.divider()

st.sidebar.header("1. Detalhes da Campanha")
colaborador = st.sidebar.text_input("Nome do Colaborador (Autor)", placeholder="Ex: Gustavo Senatore")
data_apr = st.sidebar.date_input("Data da APR", datetime.date.today())
os_num = st.sidebar.text_input("Número da OS", placeholder="Ex: 1045")
local = st.sidebar.text_input("Local da Operação", placeholder="Ex: Porto do Açu")

st.sidebar.header("2. Seleção de Equipamentos")
sensores = ["MBES", "SBES", "SVP", "SSS", "MAG", "SBP", "Sísmica Monocanal", "Sísmica Multicanal", "Vibro Core", "Jet Probe"]
selecao_sensores = st.sidebar.multiselect("Marque os sensores da OS:", sensores)

st.sidebar.header("3. Controle de Revisão")
historico_padrao = pd.DataFrame([
    {"Rev": 0, "Data": data_apr.strftime('%d/%m/%Y'), "Autor": colaborador if colaborador else "Autor", "Descrição": "Emissão Inicial"}
])
historico_df = st.sidebar.data_editor(historico_padrao, num_rows="dynamic", use_container_width=True)

# --- LÓGICA DE SEPARAÇÃO POR EQUIPAMENTO ---
riscos_gerais = []
riscos_especificos = {}

for r in riscos_db:
    tags = r.get("sensores_aplicaveis", ["Geral"])
    if "Geral" in tags:
        riscos_gerais.append(r)
    else:
        # Se for específico, cria uma cópia dedicada para cada sensor selecionado
        for s in selecao_sensores:
            if s in tags:
                r_copy = copy.deepcopy(r)
                r_copy['tarefa'] = f"[{s}] {r['tarefa']}"
                r_copy['id_unique'] = f"{r['id']}-{s}"
                
                if s not in riscos_especificos:
                    riscos_especificos[s] = []
                riscos_especificos[s].append(r_copy)

# --- ÁREA PRINCIPAL ---
st.title("Análise Preliminar de Risco (APR)")

if os_num and local and colaborador and selecao_sensores:
    st.success(f"**Gestão Ativa:** {colaborador} | **OS:** {os_num} | **Local:** {local}")
    
    st.markdown("### Seleção e Exclusão de Riscos Mapeados")
    st.write("Desmarque a caixa dos riscos que **não se aplicam**. Os desmarcados não entrarão no PDF final.")
    
    riscos_selecionados_para_pdf = []
    
    # 1. Riscos Gerais da Operação
    st.subheader("🌐 Riscos Gerais (Aplicáveis a toda a operação)")
    fases_gerais = sorted(list(set([r['categoria_fase'] for r in riscos_gerais])))
    for fase in fases_gerais:
        with st.expander(f"Fase: {fase}", expanded=True):
            for risco in [r for r in riscos_gerais if r['categoria_fase'] == fase]:
                incluir = st.checkbox(f"**{risco['id']} - {risco['tarefa']}** (Nível Inicial {risco['risco_inicial']['nivel']})", value=True, key=f"chk_geral_{risco['id']}")
                if incluir:
                    riscos_selecionados_para_pdf.append(risco)
                    st.caption(f"**Perigo:** {risco['perigo']} | **Mitigação:** {risco['mitigacao']['medidas_padrao']}")

    # 2. Riscos Específicos Separados por Sensor
    if riscos_especificos:
        st.subheader("⚙️ Riscos Específicos por Equipamento")
        for sensor in selecao_sensores:
            if sensor in riscos_especificos:
                with st.expander(f"Equipamento: {sensor}", expanded=True):
                    for risco in riscos_especificos[sensor]:
                        incluir = st.checkbox(f"**{risco['id']} - {risco['tarefa']}** (Nível Inicial {risco['risco_inicial']['nivel']})", value=True, key=f"chk_esp_{risco['id_unique']}")
                        if incluir:
                            riscos_selecionados_para_pdf.append(risco)
                            st.caption(f"**Perigo:** {risco['perigo']} | **Mitigação:** {risco['mitigacao']['medidas_padrao']}")

    st.divider()

    # --- ADICIONAR RISCO CUSTOMIZADO ---
    st.subheader("Adicionar Risco Específico do Local")
    with st.expander("➕ Clique aqui para adicionar um risco que não está no banco"):
        with st.form("form_novo_risco", clear_on_submit=True):
            fase_custom = st.selectbox("Fase", ["1 - Preparação e Onshore", "2 - Mobilização", "3 - Operação", "4 - Desmobilização"])
            tarefa_c = st.text_input("Tarefa / Processo (Ex: [USV] Navegação Costeira)")
            perigo_c = st.text_area("Perigo Identificado")
            cons_c = st.text_input("Possíveis Consequências")
            mit_c = st.text_area("Medidas de Mitigação")
            
            col_c1, col_c2 = st.columns(2)
            niv_ini_c = col_c1.number_input("Nível Inicial (1 a 25)", min_value=1, max_value=25, value=15)
            niv_res_c = col_c2.number_input("Nível Residual (1 a 25)", min_value=1, max_value=25, value=4)
            
            if st.form_submit_button("Salvar Novo Risco"):
                if tarefa_c and perigo_c and mit_c:
                    novo_risco = {
                        "id": f"EXT-{len(st.session_state.riscos_customizados)+1}",
                        "categoria_fase": fase_custom,
                        "tarefa": tarefa_c,
                        "perigo": perigo_c,
                        "consequencias": cons_c,
                        "risco_inicial": {"severidade": 0, "probabilidade": 0, "nivel": niv_ini_c},
                        "mitigacao": {"medidas_padrao": mit_c, "responsavel": "Equipa"},
                        "risco_residual": {"severidade": 0, "probabilidade": 0, "nivel": niv_res_c},
                        "sensores_aplicaveis": ["Geral"]
                    }
                    st.session_state.riscos_customizados.append(novo_risco)
                    st.success("Risco adicionado com sucesso à APR!")
                else:
                    st.error("Preencha Tarefa, Perigo e Mitigação para salvar.")
                    
    if st.session_state.riscos_customizados:
        st.write("**Riscos Específicos Adicionados Manualmente:**")
        for rc in st.session_state.riscos_customizados:
            st.warning(f"{rc['id']} - {rc['tarefa']} (Nível: {rc['risco_inicial']['nivel']})")
            riscos_selecionados_para_pdf.append(rc)
            
    st.divider()
    
    # --- GERADOR DE PDF ---
    st.subheader("Finalizar Documentação")
    if st.button("📄 Gerar Relatório PDF da APR", use_container_width=True):
        with st.spinner("Compilando a matriz Ouro..."):
            historico_dict = historico_df.to_dict('records')
            try:
                arquivo_gerado = criar_pdf_apr(os_num, local, selecao_sensores, riscos_selecionados_para_pdf, colaborador, data_apr.strftime('%d/%m/%Y'), historico_dict)
                with open(arquivo_gerado, "rb") as pdf_file:
                    st.download_button("📥 Baixar PDF Finalizado", data=pdf_file.read(), file_name=arquivo_gerado, mime='application/octet-stream', type="primary")
            except Exception as e:
                st.error(f"Erro ao gerar o PDF. Detalhe técnico: {e}")
else:
    st.info("👈 Preencha todos os dados básicos e selecione pelo menos um sensor na barra lateral para carregar a matriz.")
