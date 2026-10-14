import json

riscos_ouro = [
    # ==========================================
    # FASE 1: PREPARAÇÃO E MOBILIZAÇÃO (GERAL)
    # ==========================================
    {
        "id": "1.1", "categoria_fase": "1 - Mobilização",
        "tarefa": "Içamento e Movimentação de Cargas Suspensas (Grua / Guindaste / Pórtico)",
        "perigo": "Falha no equipamento de içamento, rompimento de lingas, balanço incontrolável da carga (contêineres, guinchos, sensores pesados) devido ao vento ou mar.",
        "consequencias": "Esmagamento, fatalidade, danos estruturais severos à embarcação ou perda total do equipamento.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "1. Emissão de Permissão de Trabalho (PTW) e Plano de Rigging. 2. Inspeção visual de todas as cintas, manilhas e cabos (certificados de carga válidos). 3. Isolamento físico da área (barreiras). 4. Uso obrigatório de cabos guia (tag lines) para evitar uso das mãos na carga. 5. Ninguém sob carga suspensa (Line of Fire).", "responsavel": "Contramestre / Rigger"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "SSS", "MAG", "SBP", "Sísmica Monocanal", "Sísmica Multicanal", "Vibro Core", "Jet Probe"]
    },
    {
        "id": "1.2", "categoria_fase": "1 - Mobilização",
        "tarefa": "Trabalhos em Altura (Instalação de Antenas GNSS / Mastros)",
        "perigo": "Queda de nível durante a fixação de antenas, cabos ou sensores meteorológicos. Queda de ferramentas (Dropped Objects) no convés.",
        "consequencias": "Fraturas múltiplas, fatalidade, traumatismo craniano na equipa de convés.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "1. PTW para trabalho em altura. 2. Uso obrigatório de arnês de segurança com talabarte duplo ancorado em ponto fixo certificado. 3. Ferramentas amarradas ao corpo ou cinto (lanyards). 4. Isolamento da área abaixo da intervenção.", "responsavel": "Técnico / Oficial"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "Sísmica Multicanal"]
    },
    
    # ==========================================
    # FASE 2: OPERAÇÃO - RISCOS GERAIS DE CONVÉS
    # ==========================================
    {
        "id": "2.1", "categoria_fase": "2 - Operação",
        "tarefa": "Trabalhos gerais no convés (Housekeeping e Deslocamento)",
        "perigo": "Superfícies molhadas ou oleosas, cabos soltos no convés, balanço da embarcação devido à ondulação.",
        "consequencias": "Quedas ao mesmo nível, entorses, fraturas, contusões (Slip, Trip and Fall).",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "1. Manutenção da arrumação e limpeza (Housekeeping). 2. Cabos de sensores e energia devem ser roteados, fixados ou suspensos. 3. Uso estrito de botas antiderrapantes e capacete com francalete. 4. Regra dos 3 pontos de contato ao circular na embarcação.", "responsavel": "Toda a Equipe"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "2.2", "categoria_fase": "2 - Operação",
        "tarefa": "Condições Meteorológicas e Oceanográficas Adversas",
        "perigo": "Operação em condições de mar agitado, ventos fortes ou tempestades elétricas.",
        "consequencias": "Perda de estabilidade, homem ao mar (MOB), danos catastróficos aos sensores e embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "1. Monitoramento constante dos boletins meteorológicos. 2. Cumprimento restrito das janelas operacionais definidas no manual da embarcação/equipamento. 3. Interrupção imediata (Stop Work Authority) em caso de degradação do tempo. 4. Proibição de trabalhos no convés aberto em tempestades elétricas.", "responsavel": "Comandante / Party Chief"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 3: OPERAÇÃO - ESPECÍFICOS POR SENSOR
    # ==========================================
    # --- MBES / SBES ---
    {
        "id": "3.1", "categoria_fase": "2 - Operação",
        "tarefa": "Instalação / Operação de Sensores Acústicos em Haste (Over-the-side pole)",
        "perigo": "Montagem ou ajuste do transdutor (MBES/SBES) no pole lateral com exposição ao mar.",
        "consequencias": "Queda de homem ao mar (MOB), esmagamento de dedos nos flanges de fixação, perda do sensor.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "1. Procedimento feito exclusivamente com a embarcação fundeada ou a 0 nós. 2. Uso obrigatório de colete salva-vidas (Lifejacket) e arnês de restrição para trabalhos próximos à borda. 3. Fixação redundante (cabos de segurança independentes) no sensor.", "responsavel": "Hidrógrafo / Marinheiro"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["MBES", "SBES"]
    },
    # --- SIDE SCAN SONAR (SSS) E MAGNETÔMETRO ---
    {
        "id": "3.2", "categoria_fase": "2 - Operação",
        "tarefa": "Lançamento, Reboque e Recolhimento de Sensores (SSS / MAG / SBP)",
        "perigo": "Tensão extrema no cabo de reboque. Formação de áreas de chicoteamento (Snap-back zones). Risco do equipamento enroscar no fundo, em cabos submarinos ou petrechos de pesca.",
        "consequencias": "Rompimento do cabo resultando em amputações ou fatalidade no convés. Perda do equipamento. Danos severos ao propulsor (hélice) da embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "1. Identificação visual e proibição de permanência nas áreas de Snap-back (pintadas no convés). 2. Comunicação via rádio dedicada entre operador do guincho e Passadiço. 3. Monitoramento da profundidade e tensão do cabo em tempo real. 4. Faca de emergência ou guilhotina pronta para corte do cabo em caso de emergência (enrosco severo).", "responsavel": "Operador de Guincho / Ponte"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["SSS", "MAG", "SBP"]
    },
    # --- SÍSMICA (ALTA VOLTAGEM) ---
    {
        "id": "3.3", "categoria_fase": "2 - Operação",
        "tarefa": "Operação de Fontes Acústicas de Alta Voltagem (Sparker / Boomer)",
        "perigo": "Manuseio de bancos de capacitores e cabos de alta tensão operando em ambiente marítimo (molhado).",
        "consequencias": "Eletrocussão grave, fatalidade, incêndio elétrico a bordo.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "1. Isolamento da fonte de energia (Lock-out/Tag-out - LOTO) antes de qualquer manuseio nos cabos. 2. A fonte só é armada mediante aviso sonoro e confirmação clara ('All Clear') com a fonte já submersa. 3. Cabos HV inspecionados visualmente antes de cada turno. 4. Uso de tapetes isolantes na bancada de aquisição.", "responsavel": "Geofísico / Eletrotécnico"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Sísmica Monocanal", "Sísmica Multicanal", "SBP"]
    },
    # --- SÍSMICA MULTICANAL (STREAMER) ---
    {
        "id": "3.4", "categoria_fase": "2 - Operação",
        "tarefa": "Manuseio e Lançamento de Streamer Sísmico",
        "perigo": "Trabalho contínuo em guinchos rotativos de grande porte. Manipulação de fluidos de preenchimento do streamer (ex: Isopar).",
        "consequencias": "Pontos de esmagamento (Pinch points) entalando mãos ou membros no guincho. Poluição ambiental no mar.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "1. Controle rigoroso de roupas (proibido roupas largas ou anéis perto do guincho rotativo). 2. Kit de contingência para vazamento de óleo (SOPEP) preparado no convés. 3. Operação guiada por sinaleiro qualificado. 4. Ninguém deve cruzar o cabo sob tensão.", "responsavel": "Operador de Streamer / HSE"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Sísmica Multicanal"]
    },
    # --- VIBRO CORE ---
    {
        "id": "3.5", "categoria_fase": "2 - Operação",
        "tarefa": "Lançamento e Penetração de Vibro Core",
        "perigo": "Operação de pórtico (A-Frame) no limite de carga. Torre metálica pesada balançando no convés. Pressurização do sistema hidráulico/elétrico de vibração.",
        "consequencias": "Colapso do pórtico, esmagamento de operadores no convés, ruptura de mangueiras hidráulicas de alta pressão (injeção de óleo na pele).",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "1. Operação estritamente proibida fora da janela climática de segurança. 2. Uso obrigatório de Tugger Winches (guinchos pneumáticos auxiliares) para travar a oscilação da torre durante o içamento. 3. Tripulação evacua a "zona quente" até que o equipamento transpasse a borda falsa. 4. Inspeção das conexões hidráulicas antes da pressurização.", "responsavel": "Geólogo / Rigger / Ponte"},
        "risco_residual": {"severidade": 5, "probabilidade": 2, "nivel": 10},
        "sensores_aplicaveis": ["Vibro Core"]
    },
    # --- JET PROBE ---
    {
        "id": "3.6", "categoria_fase": "2 - Operação",
        "tarefa": "Operação com Sistema de Bombeamento (Jet Probe)",
        "perigo": "Trabalho direto com bombas de água em alta pressão. Mangueiras pressurizadas cruzando o convés.",
        "consequencias": "Ruptura da mangueira gerando efeito chicote violento (Whip effect). Lesões oculares ou cortes na pele devido à injeção de água em alta pressão.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "1. Uso obrigatório de cabos de segurança de contenção (Whip Checks) em todas as juntas e acoplamentos da mangueira. 2. Válvulas de alívio de pressão calibradas e testadas. 3. Isolamento físico da bomba de pressão. 4. Operadores diretos equipados com proteção ocular total (viseira face shield) e capas impermeáveis.", "responsavel": "Operador Jet Probe"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Jet Probe"]
    },

    # ==========================================
    # FASE 4: DESMOBILIZAÇÃO
    # ==========================================
    {
        "id": "4.1", "categoria_fase": "3 - Desmobilização",
        "tarefa": "Desmobilização e Conclusão do Projeto",
        "perigo": "Acúmulo de fadiga física e mental após semanas de turno contínuo. Pressa para finalizar e retornar a terra.",
        "consequencias": "Baixa percepção de risco gerando acidentes bobos no manuseio de caixas, lesões lombares, acidentes de trânsito ao retornar para casa.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "1. Controle e respeito à carga horária de descanso (Gerenciamento de Fadiga). 2. Toolbox Talk focada em não baixar a guarda durante a desmobilização. 3. Técnicas corretas de levantamento de peso manual (ergonomia) ou uso obrigatório de empilhadeiras/carrinhos. 4. Garantir descanso adequado antes de dirigir veículos particulares.", "responsavel": "Party Chief / HSE"},
        "risco_residual": {"severidade": 3, "probabilidade": 2, "nivel": 6},
        "sensores_aplicaveis": ["Geral", "SBES", "MBES", "SSS", "MAG", "SBP", "Sísmica Monocanal", "Sísmica Multicanal", "Vibro Core", "Jet Probe"]
    }
]

with open('riscos_db_clean.json', 'w', encoding='utf-8') as f:
    json.dump(riscos_ouro, f, ensure_ascii=False, indent=4)
print("Banco de dados padrao OURO gerado com sucesso!")