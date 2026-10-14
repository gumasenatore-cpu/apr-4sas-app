import json

riscos_offshore = [
    # --- FASE 1: PREPARAÇÃO ---
    {
        "id": "1.1", "categoria_fase": "1 - Preparação e Planeamento",
        "tarefa": "Reunião de Segurança (Toolbox Talk) e PTW",
        "perigo": "Falta de comunicação dos riscos diários e ausência de Permissão de Trabalho (PTW).",
        "consequencias": "Trabalho não coordenado, acidentes por desconhecimento dos perigos simultâneos.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Realização de Toolbox Talk antes de qualquer atividade. Emissão de Permissão de Trabalho (PTW) para trabalhos em altura, energia perigosa ou içamento.", "responsavel": "Coordenador / Oficial"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "SSS", "MAG", "SBP", "Vibro Core", "Jet Probe", "Sísmica Monocanal", "Sísmica Multicanal"]
    },
    # --- FASE 2: MOBILIZAÇÃO ---
    {
        "id": "2.1", "categoria_fase": "2 - Mobilização",
        "tarefa": "Movimentação de Cargas Suspensas (Grua/Guindaste)",
        "perigo": "Içamento de equipamentos pesados no convés (contêineres, guinchos, pórticos). Falha estrutural ou balanço da carga.",
        "consequencias": "Esmagamento, fatalidade, danos estruturais à embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Isolamento da área com barreiras físicas. Uso obrigatório de tag lines (cabo guia). Inspeção visual de lingas e manilhas (certificados válidos). Contato visual contínuo com o manobrador.", "responsavel": "Rigger / Contramestre"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "Vibro Core", "Jet Probe", "Sísmica Multicanal", "SSS"]
    },
    {
        "id": "2.2", "categoria_fase": "2 - Mobilização",
        "tarefa": "Trabalhos em Altura (Mastros e Antenas)",
        "perigo": "Instalação de antenas GNSS/UHF ou sensores meteorológicos em locais elevados.",
        "consequencias": "Queda de nível, lesões graves ou fatalidade. Queda de ferramentas sobre a equipa.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Uso de arnês de segurança com talabarte duplo ancorado em ponto fixo certificado. Ferramentas amarradas (lanyards). Emissão de PTW para trabalho em altura.", "responsavel": "Técnico GNSS"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "MBES", "SBES"]
    },
    # --- FASE 3: OPERAÇÃO (GERAL E ESPECÍFICOS) ---
    {
        "id": "3.1", "categoria_fase": "3 - Operação",
        "tarefa": "Trabalho no Convés (Slip and Trip)",
        "perigo": "Superfícies escorregadias, cabos soltos no convés, balanço da embarcação.",
        "consequencias": "Quedas ao mesmo nível, entorses, fraturas.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Manter o convés limpo e organizado (housekeeping). Rotear cabos ordenadamente. Uso de botas de segurança anti-derrapantes. Caminhar mantendo 3 pontos de contacto.", "responsavel": "Equipa de Convés"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "SSS", "MAG", "SBP", "Vibro Core", "Jet Probe", "Sísmica Monocanal", "Sísmica Multicanal"]
    },
    {
        "id": "3.2", "categoria_fase": "3 - Operação",
        "tarefa": "Instalação e Operação de Sensores no Casco/Haste (Pole)",
        "perigo": "Montagem do transdutor no pole lateral com a embarcação em movimento ou sujeita a ondas.",
        "consequencias": "Queda de homem ao mar (MOB), perda do sensor, esmagamento de mãos nos flanges.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Fixação realizada com a embarcação parada ou fundeada. Uso de colete salva-vidas obrigatório no bordo. Fixação redundante (cabos de segurança no sensor).", "responsavel": "Hidrógrafo / Marinheiro"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["MBES", "SBES"]
    },
    {
        "id": "3.3", "categoria_fase": "3 - Operação",
        "tarefa": "Reboque de Equipamentos (Towfish / Magnetómetro)",
        "perigo": "Tensão excessiva no cabo de reboque, risco de enrosco no fundo do mar ou nos hélices da embarcação principal.",
        "consequencias": "Corte de cabo (chicoteamento), perda do equipamento, danos severos à propulsão do navio.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "Comunicação permanente entre os operadores do guincho e o passadiço (Ponte). Uso de defletores de hélice. Evitar curvas apertadas. Monitorização constante da profundidade do Towfish em relação ao fundo.", "responsavel": "Operador de SSS/MAG / Passadiço"},
        "risco_residual": {"severidade": 3, "probabilidade": 2, "nivel": 6},
        "sensores_aplicaveis": ["SSS", "MAG"]
    },
    {
        "id": "3.4", "categoria_fase": "3 - Operação",
        "tarefa": "Operação com Fontes Acústicas de Alta Voltagem (Boomer/Sparker/Sísmica)",
        "perigo": "Cabos de alta tensão danificados, manuseamento de conectores em ambiente húmido no convés.",
        "consequencias": "Eletrocussão grave ou fatal, incêndio elétrico.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Procedimentos estritos de Bloqueio e Etiquetagem (LOTO) antes da intervenção. Inspecionar cabos HV diariamente. O sistema só é ativado após ordem clara ('All Clear') e com equipamento na água. Barreiras no convés afastando pessoal não essencial.", "responsavel": "Geofísico / Eletrotécnico"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["SBP", "Sísmica Monocanal", "Sísmica Multicanal"]
    },
    {
        "id": "3.5", "categoria_fase": "3 - Operação",
        "tarefa": "Lançamento e Manuseamento de Streamers (Cabos Sísmicos)",
        "perigo": "Manuseamento de cabos longos com fluído (óleo/isopar), risco de vazamento ou esmagamento nos tambores do guincho.",
        "consequencias": "Poluição marinha, entalamento de membros nos guinchos rotativos.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Operação do guincho por profissional qualificado. Kit antipoluição (SOPEP) pronto a usar. Não usar roupas largas ou adornos perto do guincho. Comunicação via rádio dedicada.", "responsavel": "Equipa Sísmica"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Sísmica Multicanal"]
    },
    {
        "id": "3.6", "categoria_fase": "3 - Operação",
        "tarefa": "Amostragem Geotécnica Pesada (Vibro Core)",
        "perigo": "Içamento da torre de vibro core em mar aberto, balanço acentuado do pórtico (A-Frame).",
        "consequencias": "Esmagamento contra a amurada, impacto severo contra a tripulação no convés.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Janela meteorológica restrita (suspender operação com mar agitado superior aos limites do navio). Uso de tugger winches para estabilizar a torre antes de pousar. Tripulação completamente afastada até a torre estar apoiada.", "responsavel": "Rigger / Geólogo"},
        "risco_residual": {"severidade": 5, "probabilidade": 2, "nivel": 10},
        "sensores_aplicaveis": ["Vibro Core"]
    },
    {
        "id": "3.7", "categoria_fase": "3 - Operação",
        "tarefa": "Sistema de Alta Pressão de Água (Jet Probe)",
        "perigo": "Ruptura de mangueiras de alta pressão no convés, falha nas válvulas da bomba de água.",
        "consequencias": "Projeção de água a alta pressão cortando pele ou olhos, chicoteamento violento da mangueira.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Cabos de segurança (whip checks) instalados em todas as conexões de alta pressão. Válvula de alívio de pressão calibrada e testada. Isolamento da área da bomba. EPI obrigatório com proteção ocular completa (viseira).", "responsavel": "Operador Jet Probe"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Jet Probe"]
    },
    # --- FASE 4: DESMOBILIZAÇÃO ---
    {
        "id": "4.1", "categoria_fase": "4 - Desmobilização",
        "tarefa": "Remoção de Sensores e Fadiga",
        "perigo": "Trabalho manual extenuante no final da campanha com acumulação de fadiga.",
        "consequencias": "Erros humanos, lesões músculo-esqueléticas, acidentes de viação no regresso.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Respeito rigoroso pelos períodos de descanso (horas de sono). Realização correta de levantamento de pesos (técnica ergonómica). Auxílio mecânico para equipamentos pesados.", "responsavel": "Colaboradores / HSE"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "SSS", "MAG", "SBP", "Vibro Core", "Jet Probe", "Sísmica Monocanal", "Sísmica Multicanal"]
    }
]

with open('riscos_db_clean.json', 'w', encoding='utf-8') as f:
    json.dump(riscos_offshore, f, ensure_ascii=False, indent=4)
print("Novo banco de dados robusto 'riscos_db_clean.json' criado com sucesso!")