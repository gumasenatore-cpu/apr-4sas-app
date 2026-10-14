import json

riscos_definitivos = [
    # ==========================================
    # FASE 1: PREPARAÇÃO E ONSHORE
    # ==========================================
    {
        "id": "1.1", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Testes de Bancada e Integração (Pessoas e Equipamentos)",
        "perigo": "Risco de Acidente / Elétrico (NR-10): Manuseamento de equipamentos ligados à corrente, ligações provisórias, cabos descarnados.",
        "consequencias": "Choque elétrico, curto-circuito, queima de placas de sensores de alto valor.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso de bancadas aterradas. Revisão visual de todos os cabos (deck cables) e conectores submarinos. Isolamento de fontes de energia durante a montagem.", "controle_adicional": "N/A", "responsavel": "Técnico de Eletrónica"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "1.2", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Logística e Movimentação Manual (Pessoas - Ergonômico)",
        "perigo": "Risco Ergonômico (NR-17): Movimentação manual e elevação de cases tipo Pelican pesados, baterias e cabos no armazém.",
        "consequencias": "Lesões musculoesqueléticas, lombalgia, esmagamento de extremidades.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso de carrinhos de carga. Limite prático de elevação de 25kg por pessoa. Técnica de elevação com as pernas. Uso obrigatório de calçado de segurança.", "controle_adicional": "N/A", "responsavel": "Toda a Equipa"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 2: MOBILIZAÇÃO
    # ==========================================
    {
        "id": "2.1", "categoria_fase": "2 - Mobilização",
        "tarefa": "Içamento de Cargas no Cais/Convés (Pessoas e Equipamentos)",
        "perigo": "Risco de Acidente (NR-11): Movimentação de cargas suspensas por guindastes do porto ou pórticos do navio. Queda de objetos (Dropped Objects).",
        "consequencias": "Esmagamento fatal, perda total do equipamento (sensores ou guinchos caindo no mar ou convés), danos estruturais à embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Permissão de Trabalho (PTW) para içamento. Inspeção de lingas e manilhas (certificados válidos). Isolamento da área (ninguém sob a carga). Uso de cabos-guia (Tag Lines) e capacete com jugular.", "controle_adicional": "N/A", "responsavel": "Rigger / Contramestre"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "Vibro Core", "Jet Probe", "Sísmica Multicanal"]
    },
    {
        "id": "2.2", "categoria_fase": "2 - Mobilização",
        "tarefa": "Fixação de Equipamentos - Sea Fastening (Equipamentos)",
        "perigo": "Risco Operacional: Má fixação de guinchos, racks de computadores e cilindros no convés ou cabine.",
        "consequencias": "Equipamentos a rolar/soltar-se com o balanço do mar, quebra de cabos de dados, impacto contra a tripulação.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Inspeção de soldas (hot work) ou cintas catraca amarradas aos olhais do convés. Verificação final de amarração pelo Comandante antes de largar as amarras.", "controle_adicional": "N/A", "responsavel": "Party Chief / Comandante"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 3: OPERAÇÃO (RISCOS GERAIS DE SST)
    # ==========================================
    {
        "id": "3.1", "categoria_fase": "3 - Operação",
        "tarefa": "Exposição no Convés e Praça de Máquinas (Pessoas - Físico)",
        "perigo": "Risco Físico (NR-15): Níveis de ruído acima de 85 dB(A) perto de guinchos e motores. Exposição contínua a radiação solar (UV) e vibração mecânica.",
        "consequencias": "Perda auditiva induzida por ruído (PAIR), insolação, queimaduras de pele, fadiga por vibração.",
        "risco_inicial": {"severidade": 3, "probabilidade": 5, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Uso obrigatório de protetor auricular tipo concha em áreas ruidosas. Fornecimento e uso de protetor solar, roupas de manga comprida com proteção UV, e pausas em áreas climatizadas.", "controle_adicional": "N/A", "responsavel": "HSE / Equipa"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "3.2", "categoria_fase": "3 - Operação",
        "tarefa": "Manuseio de Óleos e Combustíveis (Pessoas e Ambiente - Químico)",
        "perigo": "Risco Químico (NR-20): Lubrificação de guinchos, reabastecimento de compressores, contato com fluidos hidráulicos e graxas.",
        "consequencias": "Dermatite de contato, inalação de vapores, derramamento no mar (dano ambiental e multa).",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso de luvas nitrílicas e óculos de segurança. Bandejas de contenção (drip trays) sob equipamentos a motor/hidráulicos. Kit de mitigação de vazamento (SOPEP) disponível.", "controle_adicional": "N/A", "responsavel": "Mecânico / Operadores"},
        "risco_residual": {"severidade": 2, "probabilidade": 1, "nivel": 2},
        "sensores_aplicaveis": ["Geral", "Vibro Core", "Jet Probe", "Sísmica Multicanal"]
    },
    {
        "id": "3.3", "categoria_fase": "3 - Operação",
        "tarefa": "Habitabilidade e Suporte à Vida (Pessoas - Biológico)",
        "perigo": "Risco Biológico: Consumo de água de tanques mal higienizados, conservação inadequada de alimentos, contato com vetores (mosquitos/roedores) em estuários.",
        "consequencias": "Surtos de gastroenterite severa, desidratação, transmissão de doenças (Dengue, Malária), comprometendo toda a guarnição.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Limpeza certificada dos tanques de água potável. Controle rigoroso de temperatura da câmara frigorífica. Uso exclusivo de água mineral engarrafada. Aplicação de repelentes.", "controle_adicional": "N/A", "responsavel": "Comandante / Cozinheiro"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "3.4", "categoria_fase": "3 - Operação",
        "tarefa": "Rotina de Aquisição de Dados (Pessoas - Ergonômico)",
        "perigo": "Risco Ergonômico (NR-17): Postura estática na frente de múltiplos monitores por turnos de 12 horas, movimentos do navio (Pitch/Roll/Heave), trabalho noturno.",
        "consequencias": "Distúrbios musculoesqueléticos, fadiga visual aguda, privação de sono, estresse psicológico crônico.",
        "risco_inicial": {"severidade": 3, "probabilidade": 5, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Postos de trabalho com cadeiras ajustáveis e apoio para os pés. Pausas visuais a cada 90 minutos. Cumprimento rigoroso do período de repouso (12h de trabalho máximo por dia).", "controle_adicional": "N/A", "responsavel": "Party Chief / Processadores"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 3: OPERAÇÃO (RISCOS ESPECÍFICOS)
    # ==========================================
    {
        "id": "3.5", "categoria_fase": "3 - Operação",
        "tarefa": "Manuseio de Sensores de Casco (Pessoas e Equipamentos)",
        "perigo": "Risco de Acidente (NR-35): Trabalho sobre a borda d'água para calibração, descida e fixação de hastes (poles) do ecobatímetro e perfilador (SVP).",
        "consequencias": "Queda de homem ao mar (MOB), esmagamento de dedos nos flanges de fixação, perda do sensor no fundo.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Uso obrigatório de colete salva-vidas de inflação automática e cinto de segurança ancorado à linha de vida. Motores em neutro. Cabos de retenção instalados.", "controle_adicional": "N/A", "responsavel": "Surveyor"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["MBES", "SBES", "SVP"]
    },
    {
        "id": "3.6", "categoria_fase": "3 - Operação",
        "tarefa": "Operação de Sensores Rebocados (Pessoas e Equipamentos)",
        "perigo": "Risco Operacional e Acidente (NR-12): Equipamento enroscado no fundo ou em petrechos de pesca. Tensão extrema no cabo criando 'Snap-back zones'.",
        "consequencias": "Ruptura violenta do cabo chicoteando pelo convés (potencial fatal). Perda do torpedo e danos estruturais no guincho.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Demarcação das Zonas de Snap-back. Vigia de convés em comunicação contínua via rádio. Uso de cabo fusível mecânico (Weak Link). Alicate corta-cabo posicionado.", "controle_adicional": "N/A", "responsavel": "Operador de Guincho"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["SSS", "MAG", "SBP"]
    },
    {
        "id": "3.7", "categoria_fase": "3 - Operação",
        "tarefa": "Operações Sísmicas - Sparker/Boomer (Pessoas e Equipamentos)",
        "perigo": "Risco Elétrico e Acidente (NR-10/NR-12): Geração de alta voltagem em conveses úmidos. Operação de guinchos rotativos pesados.",
        "consequencias": "Eletrocussão fatal. Incêndio elétrico no banco de capacitores. Esmagamento nos tambores rotativos dos guinchos.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Isolamento elétrico com tapetes. Procedimento LOTO. Aviso 'All Clear' via rádio antes do disparo. Proibido uso de roupas soltas perto dos guinchos.", "controle_adicional": "N/A", "responsavel": "Geofísico / Eletrotécnico"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Sísmica Monocanal", "Sísmica Multicanal"]
    },
    {
        "id": "3.8", "categoria_fase": "3 - Operação",
        "tarefa": "Amostragem Geotécnica Pesada (Pessoas e Equipamentos)",
        "perigo": "Risco Operacional Grave: Içamento de torre de aço em balanço. Bombas operando a altíssima pressão cruzando mangueiras pelo convés.",
        "consequencias": "Tombamento do equipamento, perfuração da pele por injeção de água, chicoteamento de mangueiras estouradas.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Uso de Tugger Winches para estabilização. Instalação de Whip Checks em TODAS as uniões de mangueiras. EPI obrigatório com Viseira Facial.", "controle_adicional": "N/A", "responsavel": "Geólogo / Técnico"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Vibro Core", "Jet Probe"]
    },

    # ==========================================
    # FASE 4: DESMOBILIZAÇÃO
    # ==========================================
    {
        "id": "4.1", "categoria_fase": "4 - Desmobilização",
        "tarefa": "Encerramento e Logística Reversa (Pessoas)",
        "perigo": "Risco Humano/Fadiga: Desmobilizar apressadamente equipamentos pesados. Perda de concentração devido à 'febre de ir para casa'.",
        "consequencias": "Acidentes de trabalho no último dia (cortes, prensamentos), acidentes de viação durante o regresso terrestre.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "Toolbox Talk focada nos perigos do relaxamento. Manutenção dos PTWs de içamento. Descanso obrigatório (12h) antes de conduzir.", "controle_adicional": "N/A", "responsavel": "Party Chief / HSE"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "4.2", "categoria_
