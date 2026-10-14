from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def criar_pdf_apr(os_num, local, sensores, riscos, colaborador, data_apr):
    nome_arquivo = f"APR_4SAS_OS_{os_num}.pdf"
    
    doc = SimpleDocTemplate(nome_arquivo, pagesize=landscape(A4), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    elementos = []
    estilos = getSampleStyleSheet()

    # Título do Documento
    titulo = Paragraph("<b>APR - Análise Preliminar de Risco | 4SAS Offshore</b>", estilos['Title'])
    
    # Subtítulo com Nome e Data
    info_texto = f"<b>Data:</b> {data_apr} &nbsp;&nbsp;&nbsp; <b>Colaborador:</b> {colaborador} &nbsp;&nbsp;&nbsp; <b>OS:</b> {os_num} &nbsp;&nbsp;&nbsp; <b>Local:</b> {local}<br/><b>Sensores:</b> {', '.join(sensores)}"
    subtitulo = Paragraph(info_texto, estilos['Normal'])
    
    elementos.append(titulo)
    elementos.append(Spacer(1, 12))
    elementos.append(subtitulo)
    elementos.append(Spacer(1, 20))

    # Tabela
    dados_tabela = [["ID", "Fase", "Tarefa / Perigo", "Mitigação 4SAS", "Risco\nInicial", "Risco\nResidual"]]

    for r in riscos:
        perigo_txt = Paragraph(f"<b>{r['tarefa']}</b><br/>{r['perigo']}", estilos['Normal'])
        mitigacao_txt = Paragraph(r['mitigacao']['medidas_padrao'], estilos['Normal'])
        nome_fase = r['categoria_fase'].split(' - ')[1][:12] + "." 
        
        linha = [
            r['id'],
            nome_fase,
            perigo_txt,
            mitigacao_txt,
            str(r['risco_inicial']['nivel']),
            str(r['risco_residual']['nivel'])
        ]
        dados_tabela.append(linha)

    tabela = Table(dados_tabela, colWidths=[30, 70, 250, 310, 40, 40])
    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#000080")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    tabela.setStyle(estilo)
    elementos.append(tabela)

    doc.build(elementos)
    return nome_arquivo