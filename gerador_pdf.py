from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

def get_cor_risco(nivel):
    """Devolve a cor baseada no nível de risco (1 a 25)"""
    try:
        val = int(float(nivel))
        if val <= 4:
            return colors.HexColor("#92D050") # Verde (Baixo)
        elif val <= 12:
            return colors.HexColor("#FFC000") # Amarelo (Moderado)
        else:
            return colors.HexColor("#FF0000") # Vermelho (Alto/Crítico)
    except:
        return colors.whitesmoke

def criar_pdf_apr(os_num, local, sensores, riscos, colaborador, data_apr, historico_rev):
    # Determinar a revisão atual com base na última linha do histórico
    try:
        rev_atual = str(historico_rev[-1]['Rev'])
    except:
        rev_atual = "0"

    nome_arquivo = f"OS-{os_num}-APR-Rev{rev_atual}.pdf"
    
    # Configuração do Documento com Rodapé Dinâmico
    doc = BaseDocTemplate(nome_arquivo, pagesize=landscape(A4), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=40)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    
    def rodape(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.dimgrey)
        # Esquerda (Nome do Arquivo e Rev)
        canvas.drawString(30, 20, nome_arquivo.replace(".pdf", ""))
        # Centro (Página)
        canvas.drawCentredString(doc.pagesize[0] / 2.0, 20, f"Página {doc.page}")
        # Direita (Autor)
        canvas.drawRightString(doc.pagesize[0] - 30, 20, f"Autor: {colaborador}")
        canvas.restoreState()
        
    template = PageTemplate(id='apr_template', frames=frame, onPage=rodape)
    doc.addPageTemplates([template])
    
    elementos = []
    estilos = getSampleStyleSheet()
    
    # Estilos de parágrafo personalizados
    estilo_titulo = ParagraphStyle('Titulo', parent=estilos['Title'], textColor=colors.HexColor("#000080"), fontSize=18)
    estilo_normal = estilos['Normal']
    estilo_normal.alignment = 4 # Justificado
    estilo_bold = ParagraphStyle('Bold', parent=estilos['Normal'], fontName='Helvetica-Bold')

    # ==========================================
    # CAPA DO RELATÓRIO
    # ==========================================
    elementos.append(Paragraph("<b>ANÁLISE PRELIMINAR DE RISCO (APR)</b>", estilo_titulo))
    elementos.append(Spacer(1, 15))
    
    # Dados da Missão
    info_texto = f"<b>Data:</b> {data_apr} &nbsp;&nbsp;&nbsp; <b>OS:</b> {os_num} &nbsp;&nbsp;&nbsp; <b>Local:</b> {local}<br/><b>Sensores/Operações:</b> {', '.join(sensores)}"
    elementos.append(Paragraph(info_texto, estilo_bold))
    elementos.append(Spacer(1, 15))
    
    # Descrição da APR
    desc_texto = """A Análise Preliminar de Risco (APR) é um documento diretor de planeamento e segurança, elaborado com antecedência, 
    que visa identificar, avaliar e estabelecer medidas de mitigação para os perigos operacionais, logísticos e ambientais da campanha. 
    Este documento é mandatório e norteia todas as intervenções a bordo da embarcação, operações de cais e manuseamento de sensores."""
    elementos.append(Paragraph(desc_texto, estilo_normal))
    elementos.append(Spacer(1, 15))
    
    # Matriz de Risco (Exemplo Visual)
    elementos.append(Paragraph("<b>Matriz de Classificação de Riscos (Severidade x Probabilidade):</b>", estilo_bold))
    elementos.append(Spacer(1, 5))
    
    # Desenhando a Matriz 5x5
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
    
    # Colorindo as células da Matriz Visual
    for row_idx in range(1, 6):
        for col_idx in range(1, 6):
            valor = int(matriz_dados[row_idx][col_idx])
            cor = get_cor_risco(valor)
            estilo_matriz.add('BACKGROUND', (col_idx, row_idx), (col_idx, row_idx), cor)
            
    tabela_matriz.setStyle(estilo_matriz)
    elementos.append(tabela_matriz)
    elementos.append(Spacer(1, 20))
    
    # Tabela de Histórico de Revisão
    elementos.append(Paragraph("<b>Histórico de Revisões:</b>", estilo_bold))
    elementos.append(Spacer(1, 5))
    
    dados_rev = [["Rev.", "Data", "Autor", "Descrição da Alteração"]]
    for rev in historico_rev:
        dados_rev.append([str(rev['Rev']), rev['Data'], rev['Autor'], rev['Descrição']])
        
    tabela_rev = Table(dados_rev, colWidths=[40, 80, 150, 400])
    tabela_rev.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#4F4F4F")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (3,1), (3,-1), 'LEFT'), # Descrição alinhada a esquerda
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ]))
    elementos.append(tabela_rev)
    
    # Quebra de página para começar a tabela de riscos
    elementos.append(PageBreak())

    # ==========================================
    # TABELA DE RISCOS (PÁGINA 2 em diante)
    # ==========================================
    dados_tabela_riscos = [["ID", "Fase", "Tarefa / Perigo", "Medidas de Mitigação Obrigatórias", "Risco\nInicial", "Risco\nResidual"]]

    for r in riscos:
        perigo_txt = Paragraph(f"<b>{r['tarefa']}</b><br/><u>Perigo:</u> {r['perigo']}<br/><u>Consequências:</u> {r['consequencias']}", estilo_normal)
        mitigacao_txt = Paragraph(r['mitigacao']['medidas_padrao'], estilo_normal)
        nome_fase = r['categoria_fase'].split(' - ')[1][:12] + "." 
        
        linha = [
            r['id'],
            nome_fase,
            perigo_txt,
            mitigacao_txt,
            str(r['risco_inicial']['nivel']),
            str(r['risco_residual']['nivel'])
        ]
        dados_tabela_riscos.append(linha)

    tabela_riscos = Table(dados_tabela_riscos, colWidths=[25, 60, 250, 345, 45, 45])
    
    estilo_tabela_riscos = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#000080")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    
    # Colorindo dinamicamente as colunas de Risco Inicial e Residual
    for i in range(1, len(dados_tabela_riscos)):
        nivel_ini = dados_tabela_riscos[i][4]
        nivel_res = dados_tabela_riscos[i][5]
        
        estilo_tabela_riscos.add('BACKGROUND', (4, i), (4, i), get_cor_risco(nivel_ini))
        estilo_tabela_riscos.add('BACKGROUND', (5, i), (5, i), get_cor_risco(nivel_res))

    tabela_riscos.setStyle(estilo_tabela_riscos)
    elementos.append(tabela_riscos)

    # Constrói o PDF
    doc.build(elementos)
    return nome_arquivo
