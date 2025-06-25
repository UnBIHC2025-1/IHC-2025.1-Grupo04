import re
from pathlib import Path

def define_env(env):
    @env.macro
    def contar_checklist(caminho_md):
        conteudo = Path(caminho_md).read_text(encoding='utf-8')

        feitos = len(re.findall(r'- \[x\]', conteudo, flags=re.IGNORECASE))
        pendentes = len(re.findall(r'- \[ \]', conteudo))

        return {"feitos": feitos, "pendentes": pendentes}
