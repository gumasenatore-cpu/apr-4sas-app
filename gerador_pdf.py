from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_cor_risco(nivel):
    try:
        val = int(float(nivel))
        if val <= 4: return colors.HexColor("#92D050")
        elif val <= 12: return colors.HexColor("#FFC000")
        else: return colors.HexColor("#FF0000")
    except:
        return colors.whitesmoke

def criar_pdf_apr(os_num, local, sensores, riscos, colaborador, data_apr, historico_rev):
    try: rev_atual = str(historico_rev[-1]['Rev'])
    except: rev_atual = "0"

    nome_arquivo = f"OS-{os_num}-APR-Rev{rev_atual}.pdf"
    
    doc = BaseDocTemplate(nome_arquivo, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=25, bottomMargin=35)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    def rodape(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.dimgrey)
        canvas.drawString(20, 15, nome_arquivo.replace(".pdf", ""))
        canvas.drawCentredString(doc.pagesize[0] / 2.0, 15, f"Página {doc.page}")
        canvas.drawRightString(doc.pagesize[0] - 20, 15, f"Autor: {str(colaborador)}")
        canvas.restoreState()
        
    template = PageTemplate(id='apr_template', frames=frame, onPage=rodape)
    doc.addPageTemplates([template])
    
    elementos = []
    estilos = getSampleStyleSheet()
    # Título alterado para cor preta
    estilo_titulo = ParagraphStyle('Titulo', parent=estilos['Title'], textColor=colors.black, fontSize=16)
    
    estilo_tabela_txt = ParagraphStyle('TabTxt', parent=estilos['Normal'], fontSize=7, leading=8, alignment=4)
    estilo_bold = ParagraphStyle('Bold', parent=estilos['Normal'], fontName='Helvetica-Bold')

    # --- CAPA ---
    elementos.append(Paragraph("<b>ANÁLISE PRELIMINAR DE RISCO (APR)</b>", estilo_titulo))
    elementos.append(Spacer(1, 10))
    info_texto = f"<b>Data:</b> {data_apr} &nbsp;&nbsp;&nbsp; <b>OS:</b> {os_num} &nbsp;&nbsp;&nbsp; <b>Local:</b> {local}<br/><b>Sensores/Operações:</b> {', '.join(sensores)}"
    elementos.append(Paragraph(info_texto, estilo_bold))
    elementos.append(Spacer(1, 10))
    
    matriz_dados = [
        ["Sev \\ Prob", "1. Rara", "2. Baixa", "3. Possível", "4. Alta", "5. Frequente"],
        ["5. Crítica", "5", "10", "15", "20", "25"],
        ["4. Severa", "4", "8", "12", "16", "20"],
        ["3. Moderada", "3", "6", "9", "12", "15"],
        ["2. Leve", "2", "4", "6", "8", "10"],
        ["1. Insignif.", "1", "2", "3", "4", "5"]
    ]
    tabela_matriz = Table(matriz_dados, colWidths=[70, 50, 50, 50, 50, 60])
    estilo_matriz = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#000080")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (0,-1), colors.HexColor("#000080")),
        ('TEXTCOLOR', (0,1), (0,-1), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 1, colors.white),
    ])
    for row_idx in range(1, 6):
        for col_idx in range(1, 6):
            estilo_matriz.add('BACKGROUND', (col_idx, row_idx), (col_idx, row_idx), get_cor_risco(matriz_dados[row_idx][col_idx]))
    tabela_matriz.setStyle(estilo_matriz)
    elementos.append(tabela_matriz)
    elementos.append(Spacer(1, 15))
    
    dados_rev = [["Rev.", "Data", "Autor", "Descrição da Alteração"]]
    for rev in historico_rev:
        dados_rev.append([str(rev.get('Rev','')), str(rev.get('Data','')), str(rev.get('Autor','')), str(rev.get('Descrição',''))])
    
    tabela_rev = Table(dados_rev, colWidths=[40, 80, 150, 400])
    tabela_rev.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#4F4F4F")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (3,1), (3,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elementos.append(tabela_rev)
    elementos.append(PageBreak())

    # --- TABELA DE 14 COLUNAS ---
    cabecalho_linha1 = [
        "Nº", "Disciplina", 
        "Identificação dos Riscos", "", "", 
        "Nível Inicial", "", "", 
        "Mitigação dos Riscos", "", "", 
        "Nível Residual", "", ""
    ]
    cabecalho_linha2 = [
        "", "", 
        "Processo / Tarefa", "Perigo / Situações", "Consequências", 
        "Sev", "Prob", "Nív", 
        "Medidas de Controle", "Controle Adicional", "Responsável", 
        "Sev", "Prob", "Nív"
    ]
    
    dados_tabela_riscos = [cabecalho_linha1, cabecalho_linha2]

    for r in riscos:
        tarefa_limpa = str(r.get('tarefa', '')).replace('<','').replace('>','')
        perigo_limpo = str(r.get('perigo', '')).replace('<','').replace('>','')
        cons_limpo = str(r.get('consequencias', '')).replace('<','').replace('>','')
        mitig_limpo = str(r.get('mitigacao', {}).get('medidas_padrao', '')).replace('<','').replace('>','')
        adic_limpo = str(r.get('mitigacao', {}).get('controle_adicional', 'N/A')).replace('<','').replace('>','')
        resp_limpo = str(r.get('mitigacao', {}).get('responsavel', 'Equipe')).replace('<','').replace('>','')
        nome_fase = str(r.get('categoria_fase', 'Geral')).split(' - ')[-1][:12] + "." 
        
        linha = [
            Paragraph(str(r.get('id', '-')), estilo_tabela_txt),
            Paragraph(nome_fase, estilo_tabela_txt),
            Paragraph(tarefa_limpa, estilo_tabela_txt),
            Paragraph(perigo_limpo, estilo_tabela_txt),
            Paragraph(cons_limpo, estilo_tabela_txt),
            str(r.get('risco_inicial', {}).get('severidade', '0')),
            str(r.get('risco_inicial', {}).get('probabilidade', '0')),
            str(r.get('risco_inicial', {}).get('nivel', '0')),
            Paragraph(mitig_limpo, estilo_tabela_txt),
            Paragraph(adic_limpo, estilo_tabela_txt),
            Paragraph(resp_limpo, estilo_tabela_txt),
            str(r.get('risco_residual', {}).get('severidade', '0')),
            str(r.get('risco_residual', {}).get('probabilidade', '0')),
            str(r.get('risco_residual', {}).get('nivel', '0'))
        ]
        dados_tabela_riscos.append(linha)

    larguras = [20, 35, 75, 100, 85, 20, 25, 25, 160, 60, 60, 20, 25, 25]
    tabela_riscos = Table(dados_tabela_riscos, colWidths=larguras, repeatRows=2)
    
    estilo_tabela_riscos = TableStyle([
        ('SPAN', (0,0), (0,1)), ('SPAN', (1,0), (1,1)), ('SPAN', (2,0), (4,0)), 
        ('SPAN', (5,0), (7,0)), ('SPAN', (8,0), (10,0)), ('SPAN', (11,0), (13,0)), 
        ('BACKGROUND', (0, 0), (-1, 1), colors.HexColor("#000080")), 
        ('TEXTCOLOR', (0, 0), (-1, 1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, 1), 7),
        ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ])
    
    for i in range(2, len(dados_tabela_riscos)):
        estilo_tabela_riscos.add('BACKGROUND', (7, i), (7, i), get_cor_risco(dados_tabela_riscos[i][7]))
        estilo_tabela_riscos.add('BACKGROUND', (13, i), (13, i), get_cor_risco(dados_tabela_riscos[i][13]))

    tabela_riscos.setStyle(estilo_tabela_riscos)
    elementos.append(tabela_riscos)

    doc.build(elementos)
    return nome_arquivo
