import json

riscos_definitivos = [
    # ==========================================
    # FASE 1: PREPARAÇÃO E ONSHORE
    # ==========================================
    {
        "id": "1.1", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Testes de Bancada, Documentação e Integração",
        "perigo": "Risco de Acidente / Elétrico (NR-10): Manuseamento de equipamentos ligados à corrente, documentação da equipe incompleta ou sem treino.",
        "consequencias": "Choque elétrico, queima de placas de sensores de alto valor, impedimento de embarque por falta de NRs/ASO.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Auditoria de documentação (ASO, NRs, CBSP). Uso de bancadas aterradas. Revisão visual de cabos e conectores submarinos.", "controle_adicional": "N/A", "responsavel": "Diretor Técnico / RH"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "1.2", "categoria_fase": "1 - Preparação e Onshore",
        "tarefa": "Logística Base e Movimentação Manual",
        "perigo": "Risco Ergonômico (NR-17): Movimentação manual e elevação de cases pesados, baterias e falha no transporte rodoviário.",
        "consequencias": "Lesões musculoesqueléticas, lombalgia, acidentes de trânsito durante deslocamento para o porto.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso de carrinhos de carga. Limite prático de elevação de 25kg por pessoa. Veículos homologados e motoristas com descanso garantido.", "controle_adicional": "N/A", "responsavel": "Logística"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 2: MOBILIZAÇÃO
    # ==========================================
    {
        "id": "2.1", "categoria_fase": "2 - Mobilização",
        "tarefa": "Içamento de Cargas no Cais/Convés",
        "perigo": "Risco de Acidente (NR-11): Movimentação de cargas suspensas por guindastes. Queda de objetos (Dropped Objects).",
        "consequencias": "Esmagamento fatal, perda total do equipamento, danos estruturais à embarcação.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Permissão de Trabalho (PTW) para içamento. Inspeção de lingas e manilhas. Isolamento da área (ninguém sob a carga). Uso de cabos-guia (Tag Lines).", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / Contramestre"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Geral", "Vibro Core", "Jet Probe", "Sísmica Multicanal"]
    },
    {
        "id": "2.2", "categoria_fase": "2 - Mobilização",
        "tarefa": "Fixação de Equipamentos - Sea Fastening",
        "perigo": "Risco Operacional: Má fixação de guinchos, racks de computadores e cilindros no convés ou cabine.",
        "consequencias": "Equipamentos a rolar/soltar-se com o balanço do mar, impacto contra a tripulação.",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Inspeção de soldas ou cintas catraca amarradas aos olhais do convés. Verificação final de amarração antes de largar as amarras.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / Comandante"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 3: OPERAÇÃO (RISCOS GERAIS DE SST)
    # ==========================================
    {
        "id": "3.1", "categoria_fase": "3 - Operação",
        "tarefa": "Exposição no Convés e Praça de Máquinas",
        "perigo": "Risco Físico (NR-15): Níveis de ruído acima de 85 dB(A). Exposição contínua a radiação solar (UV) e vibração mecânica.",
        "consequencias": "Perda auditiva induzida por ruído (PAIR), insolação, queimaduras de pele, fadiga.",
        "risco_inicial": {"severidade": 3, "probabilidade": 5, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Uso obrigatório de protetor auricular tipo concha. Fornecimento de protetor solar, roupas com proteção UV e pausas em áreas climatizadas.", "controle_adicional": "N/A", "responsavel": "HSE / Gerente de Operações"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "3.2", "categoria_fase": "3 - Operação",
        "tarefa": "Manuseio de Óleos e Combustíveis",
        "perigo": "Risco Químico (NR-20): Lubrificação de guinchos, reabastecimento de compressores, contato com fluidos hidráulicos.",
        "consequencias": "Dermatite de contato, inalação de vapores, derramamento no mar (dano ambiental).",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Uso de luvas nitrílicas e óculos. Bandejas de contenção (drip trays). Kit de mitigação de vazamento (SOPEP) disponível.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / Manutenção"},
        "risco_residual": {"severidade": 2, "probabilidade": 1, "nivel": 2},
        "sensores_aplicaveis": ["Geral", "Vibro Core", "Jet Probe", "Sísmica Multicanal"]
    },
    {
        "id": "3.3", "categoria_fase": "3 - Operação",
        "tarefa": "Habitabilidade e Suporte à Vida",
        "perigo": "Risco Biológico: Consumo de água de tanques mal higienizados, contato com vetores (mosquitos) em estuários.",
        "consequencias": "Surtos de gastroenterite, desidratação, transmissão de doenças (Dengue, Malária).",
        "risco_inicial": {"severidade": 4, "probabilidade": 3, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Limpeza certificada dos tanques. Água mineral engarrafada. Aplicação de repelentes e controle sanitário dos alimentos.", "controle_adicional": "N/A", "responsavel": "Logística / Comandante"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "3.4", "categoria_fase": "3 - Operação",
        "tarefa": "Rotina de Aquisição de Dados",
        "perigo": "Risco Ergonômico (NR-17): Postura estática na frente de múltiplos monitores, movimentos do navio, trabalho noturno.",
        "consequencias": "Distúrbios musculoesqueléticos, fadiga visual aguda, estresse psicológico crônico.",
        "risco_inicial": {"severidade": 3, "probabilidade": 5, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Postos de trabalho com cadeiras ajustáveis. Pausas visuais a cada 90 minutos. Cumprimento rigoroso das 12h de trabalho máximo/dia.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / RH"},
        "risco_residual": {"severidade": 2, "probabilidade": 2, "nivel": 4},
        "sensores_aplicaveis": ["Geral"]
    },

    # ==========================================
    # FASE 3: OPERAÇÃO (RISCOS ESPECÍFICOS)
    # ==========================================
    {
        "id": "3.5", "categoria_fase": "3 - Operação",
        "tarefa": "Manuseio de Sensores de Casco",
        "perigo": "Risco de Acidente (NR-35): Trabalho sobre a borda d'água para calibração, descida e fixação de hastes (poles).",
        "consequencias": "Queda de homem ao mar (MOB), esmagamento de dedos nos flanges, perda do sensor.",
        "risco_inicial": {"severidade": 5, "probabilidade": 3, "nivel": 15},
        "mitigacao": {"medidas_padrao": "Uso obrigatório de colete salva-vidas automático e cinto de segurança ancorado. Motores em neutro. Cabos de retenção instalados.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["MBES", "SBES", "SVP"]
    },
    {
        "id": "3.6", "categoria_fase": "3 - Operação",
        "tarefa": "Operação de Sensores Rebocados",
        "perigo": "Risco Operacional (NR-12): Equipamento enroscado no fundo ou em petrechos de pesca. Tensão extrema no cabo criando 'Snap-back zones'.",
        "consequencias": "Ruptura violenta do cabo chicoteando pelo convés (potencial fatal). Perda do torpedo.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Demarcação das Zonas de Snap-back. Vigia de convés em comunicação contínua via rádio. Uso de Weak Link. Alicate corta-cabo posicionado.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["SSS", "MAG", "SBP"]
    },
    {
        "id": "3.7", "categoria_fase": "3 - Operação",
        "tarefa": "Operações Sísmicas - Sparker/Boomer",
        "perigo": "Risco Elétrico (NR-10/NR-12): Geração de alta voltagem em conveses úmidos. Operação de guinchos rotativos pesados.",
        "consequencias": "Eletrocussão fatal. Incêndio elétrico no banco de capacitores. Esmagamento nos tambores rotativos.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Isolamento elétrico com tapetes. Procedimento LOTO. Aviso 'All Clear' via rádio antes do disparo. Proibido uso de roupas soltas.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / Diretor Técnico"},
        "risco_residual": {"severidade": 5, "probabilidade": 1, "nivel": 5},
        "sensores_aplicaveis": ["Sísmica Monocanal", "Sísmica Multicanal"]
    },
    {
        "id": "3.8", "categoria_fase": "3 - Operação",
        "tarefa": "Amostragem Geotécnica e Mergulho Raso (Jet Probe)",
        "perigo": "Risco Operacional e de Mergulho em Águas Rasas: Içamento de torre de aço. Operação submarina próxima à costa com bombas de água a altíssima pressão. Forte influência de correntes, ondulação (swell) e baixa visibilidade.",
        "consequencias": "Choque do mergulhador contra o fundo ou embarcação. Injeção de água sob alta pressão na pele/traje, afogamento e emaranhamento em umbilicais ou cabos devido a correntes.",
        "risco_inicial": {"severidade": 5, "probabilidade": 4, "nivel": 20},
        "mitigacao": {"medidas_padrao": "Plano de Mergulho Raso aprovado (PTW). Monitoramento constante de maré e correntes. Mergulhador de resgate (Standby Diver) pronto. Instalação de Whip Checks. Manter umbilicais tensionados para evitar emaranhamento.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / Equipe de Mergulho"},
        "risco_residual": {"severidade": 4, "probabilidade": 1, "nivel": 4},
        "sensores_aplicaveis": ["Vibro Core", "Jet Probe"]
    },

    # ==========================================
    # FASE 4: DESMOBILIZAÇÃO
    # ==========================================
    {
        "id": "4.1", "categoria_fase": "4 - Desmobilização",
        "tarefa": "Encerramento e Logística Reversa",
        "perigo": "Risco Humano/Fadiga: Desmobilizar apressadamente equipamentos pesados. Perda de concentração devido à pressa no retorno.",
        "consequencias": "Acidentes de trabalho no último dia (cortes, prensamentos), acidentes de trânsito no retorno terrestre.",
        "risco_inicial": {"severidade": 4, "probabilidade": 4, "nivel": 16},
        "mitigacao": {"medidas_padrao": "Toolbox Talk focada no não relaxamento. Manutenção dos PTWs de içamento. Descanso obrigatório (12h) antes de dirigir veículos de retorno.", "controle_adicional": "N/A", "responsavel": "Gerente de Operações / RH"},
        "risco_residual": {"severidade": 3, "probabilidade": 1, "nivel": 3},
        "sensores_aplicaveis": ["Geral"]
    },
    {
        "id": "4.2", "categoria_fase": "4 - Desmobilização",
        "tarefa": "Desinstalação e Transporte",
        "perigo": "Risco Operacional: Acondicionamento incorreto de sensores ainda molhados ou com sal. Desconexão brusca de cabos.",
        "consequencias": "Corrosão acelerada, pinos partidos, fibra ótica rompida, inutilizando o ativo.",
        "risco_inicial": {"severidade": 3, "probabilidade": 4, "nivel": 12},
        "mitigacao": {"medidas_padrao": "Lavagem com água doce. Secagem e aplicação de protetivo (WD-40) nos conectores. Uso de tampas de proteção mecânica.", "controle_adicional": "N/A", "responsavel": "Logística / Gerente de Operações"},
        "risco_residual": {"severidade": 2, "probabilidade": 1, "nivel": 2},
        "sensores_aplicaveis": ["Geral"]
    }
]

with open('riscos_db_clean.json', 'w', encoding='utf-8') as f:
    json.dump(riscos_definitivos, f, ensure_ascii=False, indent=4)
    
print("Banco de Dados Atualizado: Português BR aplicado e Controle Adicional dinâmico integrado!")
