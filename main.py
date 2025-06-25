# main.py

import re
from pathlib import Path

def define_env(env):
    @env.macro
    def contar_checklist(caminho_md):
        # Lê o conteúdo do markdown
        conteudo = Path(caminho_md).read_text(encoding='utf-8')

        # Conta checkboxes marcadas e desmarcadas
        feitos = len(re.findall(r'- \[x\]', conteudo, flags=re.IGNORECASE))
        pendentes = len(re.findall(r'- \[ \]', conteudo))

        return {"feitos": feitos, "pendentes": pendentes}
