import json

riscos_definitivos = [
    # --- FASE 1: PREPARAÇÃO, ONSHORE E MOBILIZAÇÃO ---
    {
        "id": "1.1", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Deslocamento Terrestre (Base para o Porto)",
        "perigo": "Condução de viaturas carregadas em autoestradas ou acessos portuários. Condições de trânsito severo ou estradas más.",
        "consequencias": "Acidente de viação, capotamento, atraso crítico, lesões ou fatalidade.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Viaturas com manutenção em dia. Respeitar limites de velocidade. Proibido conduzir após o turno noturno (fadiga). Uso obrigatório de cinto de segurança.", "responsavel": "Motoristas / Equipa"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "1.2", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Movimentação Manual de Cargas (Ergonomia)",
        "perigo": "Levantamento manual de sensores pesados, caixas Peli, cabos e consumíveis durante a carga/descarga das carrinhas para o cais.",
        "consequencias": "Lombalgias agudas, distensões musculares, esmagamento de dedos ou pés.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Limitar o peso manual a 25kg por pessoa. Levantar peso usando as pernas e não as costas. Uso de empilhadores ou carrinhos sempre que possível. Uso de botas com biqueira de aço.", "responsavel": "Toda a Equipe"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "1.3", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Operação de Içamento com Guindaste (Porto/Embarcação)",
        "perigo": "Falta de requisitos para içamento. Uso de cintas danificadas. Carga a balançar sobre a equipa.",
        "consequencias": "Queda de carga suspensa (Dropped Object), esmagamento, danos à embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Plano de Rigging (PTW). Inspeção visual de lingas e manilhas. Isolamento da área física (Ninguém sob a carga). Uso de cabos guia (tag lines).", "responsavel": "Contramestre / Rigger"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral"]
    },

    # --- FASE 2: OPERAÇÃO GERAL E ERGONOMIA A BORDO ---
    {
        "id": "2.1", "categoria_fase": "2 - Operação",
        "tarefa": "Condições Metaoceanográficas e Integridade",
        "perigo": "Mar agitado, tempestades, falha de motores da embarcação em mar aberto.",
        "consequencias": "Embarcação à deriva, naufrágio, homem ao mar, interrupção total.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Autoridade de paragem de trabalho (Stop Work Authority) respeitada. Acompanhamento diário da previsão do tempo. Manutenção da embarcação verificada (Diário de Bordo).", "responsavel": "Comandante / Party Chief"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "2.2", "categoria_fase": "2 - Operação",
        "tarefa": "Trabalho Contínuo na Cabine de Survey (Ergonomia e Fadiga)",
        "perigo": "Má postura em estações de processamento, vibração constante do navio, brilho dos monitores em turnos de 12 horas.",
        "consequencias": "Fadiga extrema, tendinite, perda de acuidade visual, erros de julgamento críticos.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Pausas curtas a cada 2 horas. Cadeiras com ajuste lombar e monitores na altura dos olhos. Respeito absoluto às 12h máximas de trabalho diário. Filtro de luz azul nos ecrãs.", "responsavel": "Processador / Party Chief"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "2.3", "categoria_fase": "2 - Operação",
        "tarefa": "Riscos Biológicos e Alimentares Costeiros/Offshore",
        "perigo": "Água ou alimentos contaminados a bordo, exposição a mosquitos em zonas costeiras ou mangais.",
        "consequencias": "Intoxicação alimentar severa, surto de viroses na embarcação paralisando a equipa.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Certificação sanitária do cozinheiro/embarcação. Uso exclusivo de água engarrafada para beber. Uso de repelente e mangas compridas em áreas endémicas (costeiras).", "responsavel": "Comandante / HSE"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # --- FASE 2: OPERAÇÃO ESPECÍFICA DE SENSORES ---
    {
        "id": "3.1", "categoria_fase": "2 - Operação",
        "tarefa": "Manuseamento de Sensores Acústicos (MBES/SBES)",
        "perigo": "Instalação do mastro (pole) sobre a borda com a embarcação no mar.",
        "consequencias": "Queda ao mar (MOB), esmagamento de mãos nos flanges.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso obrigatório de colete salva-vidas. Fixar mastro com embarcação parada (0 nós). Cabos de segurança redundantes aplicados no sensor.", "responsavel": "Surveyor"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["MBES", "SBES"]
    },
    {
        "id": "3.2", "categoria_fase": "2 - Operação",
        "tarefa": "Sensores Rebocados (SSS / MAG / SBP)",
        "perigo": "Tensão extrema no cabo. Áreas de chicoteamento do cabo (Snap-back zones).",
        "consequencias": "Corte de cabo causando fatalidade no convés. Perda de equipamento.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Proibição de acesso às áreas de Snap-back. Comunicação de rádio ativa. Faca/Guilhotina pronta para corte emergencial do cabo.", "responsavel": "Operador Guincho"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["SSS", "MAG", "SBP"]
    },
    {
        "id": "3.3", "categoria_fase": "2 - Operação",
        "tarefa": "Fontes Acústicas de Alta Voltagem e Streamers (Sísmica)",
        "perigo": "Trabalho em convés molhado com fontes de alta voltagem (Sparker) e guinchos rotativos pesados.",
        "consequencias": "Eletrocussão grave, esmagamento em partes móveis do guincho.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Protocolo Lock-out/Tag-out (LOTO). Aviso sonoro ('All Clear') antes do disparo. Não utilizar roupas largas ou adornos. Tapetes isolantes no convés.", "responsavel": "Geofísico / Eletrotécnico"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Sísmica Monocanal", "Sísmica Multicanal"]
    },
    {
        "id": "3.4", "categoria_fase": "2 - Operação",
        "tarefa": "Equipamentos de Penetração e Alta Pressão (Vibro Core / Jet Probe)",
        "perigo": "Içamento de torre pesada. Ruptura de mangueiras de água a altíssima pressão cruzando o convés.",
        "consequencias": "Colapso do pórtico. Corte na pele ou lesão ocular grave por injeção de água. Chicoteamento de mangueira.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Uso de Tugger Winches para estabilizar a torre. Cabos de contenção (Whip Checks) em todas as juntas de pressão. EPI completo com viseira (face shield).", "responsavel": "Geólogo / Técnico Jet Probe"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Vibro Core", "Jet Probe"]
    },

    # --- FASE 3: DESMOBILIZAÇÃO ---
    {
        "id": "4.1", "categoria_fase": "3 - Desmobilização",
        "tarefa": "Conclusão e Logística Reversa",
        "perigo": "Excesso de confiança e fadiga ao final do projeto. Desmontagem apressada de equipamentos pesados.",
        "consequencias": "Acidentes no cais por desatenção, entorses, acidentes na viagem de volta para casa.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "Manutenção dos procedimentos rigorosos de PTW até ao último minuto. Proibição de conduzir viaturas se o colaborador estiver fadigado. Garantir 12h de descanso antes da viagem.", "responsavel": "Party Chief"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Geral"]
    }
]

with open('riscos_db_clean.json', 'w', encoding='utf-8') as f:
    json.dump(riscos_definitivos, f, ensure_ascii=False, indent=4)
print("Banco de Dados Robusto Ouro Gerado com Sucesso!")
