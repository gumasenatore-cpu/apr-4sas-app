import json

# Lendo o arquivo JSON existente e injetando o novo campo
with open('riscos_db_clean.json', 'r', encoding='utf-8') as f:
    riscos_definitivos = json.load(f)

for risco in riscos_definitivos:
    if "controle_adicional" not in risco["mitigacao"]:
        risco["mitigacao"]["controle_adicional"] = "N/A"

with open('riscos_db_clean.json', 'w', encoding='utf-8') as f:
    json.dump(riscos_definitivos, f, ensure_ascii=False, indent=4)
    
print("Banco atualizado com o campo de Controle Adicional!")
