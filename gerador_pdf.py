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
    
    doc = BaseDocTemplate(nome_arquivo, pagesize=landscape(A4), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=40)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    def rodape(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.dimgrey)
        canvas.drawString(30, 20, nome_arquivo.replace(".pdf", ""))
        canvas.drawCentredString(doc.pagesize[0] / 2.0, 20, f"Página {doc.page}")
        # Blindagem: se colaborador não for string limpa
        canvas.drawRightString(doc.pagesize[0] - 30, 20, f"Autor: {str(colaborador)}")
        canvas.restoreState()
        
    template = PageTemplate(id='apr_template', frames=frame, onPage=rodape)
    doc.addPageTemplates([template])
    
    elementos = []
    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle('Titulo', parent=estilos['Title'], textColor=colors.HexColor("#000080"), fontSize=18)
    estilo_normal = estilos['Normal']
    estilo_normal.alignment = 4
    estilo_bold = ParagraphStyle('Bold', parent=estilos['Normal'], fontName='Helvetica-Bold')

    # Capa
    elementos.append(Paragraph("<b>ANÁLISE PRELIMINAR DE RISCO (APR)</b>", estilo_titulo))
    elementos.append(Spacer(1, 15))
    info_texto = f"<b>Data:</b> {data_apr} &nbsp;&nbsp;&nbsp; <b>OS:</b> {os_num} &nbsp;&nbsp;&nbsp; <b>Local:</b> {local}<br/><b>Sensores/Operações:</b> {', '.join(sensores)}"
    elementos.append(Paragraph(info_texto, estilo_bold))
    elementos.append(Spacer(1, 15))
    
    desc_texto = """A Análise Preliminar de Risco (APR) é um documento diretor de planeamento e segurança, elaborado com antecedência, 
    que visa identificar, avaliar e estabelecer medidas de mitigação para os perigos operacionais, logísticos e ambientais da campanha. 
    Este documento é mandatório e norteia todas as intervenções a bordo da embarcação, operações de cais e manuseamento de sensores."""
    elementos.append(Paragraph(desc_texto, estilo_normal))
    elementos.append(Spacer(1, 15))
    
    elementos.append(Paragraph("<b>Matriz de Classificação de Riscos (Severidade x Probabilidade):</b>", estilo_bold))
    elementos.append(Spacer(1, 5))
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
    elementos.append(Spacer(1, 20))
    
    elementos.append(Paragraph("<b>Histórico de Revisões:</b>", estilo_bold))
    elementos.append(Spacer(1, 5))
    dados_rev = [["Rev.", "Data", "Autor", "Descrição da Alteração"]]
    for rev in historico_rev:
        # Blindagem contra campos nulos
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

    # Tabela de Riscos
    dados_tabela_riscos = [["ID", "Fase", "Tarefa / Perigo", "Medidas de Mitigação Obrigatórias", "Risco\nInicial", "Risco\nResidual"]]
    for r in riscos:
        # Blindagem: Limpeza de textos para evitar erros no ReportLab
        tarefa_limpa = str(r.get('tarefa', '')).replace('<','').replace('>','')
        perigo_limpo = str(r.get('perigo', '')).replace('<','').replace('>','')
        cons_limpo = str(r.get('consequencias', '')).replace('<','').replace('>','')
        mitig_limpo = str(r.get('mitigacao', {}).get('medidas_padrao', '')).replace('<','').replace('>','')
        
        perigo_txt = Paragraph(f"<b>{tarefa_limpa}</b><br/><u>Perigo:</u> {perigo_limpo}<br/><u>Consequências:</u> {cons_limpo}", estilo_normal)
        mitigacao_txt = Paragraph(mitig_limpo, estilo_normal)
        nome_fase = str(r.get('categoria_fase', 'Geral')).split(' - ')[-1][:15] + "." 
        
        linha = [
            str(r.get('id', '-')),
            nome_fase,
            perigo_txt,
            mitigacao_txt,
            str(r.get('risco_inicial', {}).get('nivel', '0')),
            str(r.get('risco_residual', {}).get('nivel', '0'))
        ]
        dados_tabela_riscos.append(linha)

    tabela_riscos = Table(dados_tabela_riscos, colWidths=[35, 70, 250, 315, 50, 50])
    estilo_tabela_riscos = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#000080")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    
    for i in range(1, len(dados_tabela_riscos)):
        estilo_tabela_riscos.add('BACKGROUND', (4, i), (4, i), get_cor_risco(dados_tabela_riscos[i][4]))
        estilo_tabela_riscos.add('BACKGROUND', (5, i), (5, i), get_cor_risco(dados_tabela_riscos[i][5]))

    tabela_riscos.setStyle(estilo_tabela_riscos)
    elementos.append(tabela_riscos)

    doc.build(elementos)
    return nome_arquivo
