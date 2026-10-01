#!/usr/bin/env python3
"""Gera os cursos em páginas únicas que abrem no navegador com dois cliques, sem internet.

  CURSO.html              Edição com IA (também em site/index.html)
  CURSO-MESA-AGENTES.html Mesa Operada por Agentes

Rode de novo sempre que editar os arquivos .md:
  pip install markdown
  python3 ferramentas/gerar_site.py
"""
import html
import json
import re
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent

CURSOS = [
    {
        "titulo": "Edição com IA — Curso HN",
        "manual": "curso/MANUAL-EDICAO-COM-IA-HN.md",
        "saidas": ["CURSO.html", "site/index.html"],
        "chave": "curso-hn-concluidas",
        "materiais": [
            ("comandos", "Guia de comandos", "modelos/guia-de-comandos.md"),
            ("briefing", "Modelo de briefing", "modelos/briefing.md"),
            ("pastas", "Pasta modelo", "modelos/estrutura-de-pastas.md"),
            ("revisao", "Ficha de revisão", "modelos/ficha-de-revisao.md"),
        ],
        "grupo_skills": "Skills de edição",
        "skills": [
            ("skill-estilo", "Estilo", ".claude/skills/edicao-estilo/SKILL.md"),
            ("skill-ritmo", "Ritmo", ".claude/skills/edicao-ritmo/SKILL.md"),
            ("skill-legendas", "Legendas", ".claude/skills/edicao-legendas/SKILL.md"),
            ("skill-movimento", "Movimento", ".claude/skills/edicao-movimento/SKILL.md"),
            ("skill-composicao", "Composição", ".claude/skills/edicao-composicao/SKILL.md"),
        ],
        "ferramentas": "ferramentas/LEIA-ME.md",
        "codigo": ["ferramentas/cortar_silencios.py", "ferramentas/legendar.py", "ferramentas/gerar_site.py"],
        "links": {
            "modelos/briefing.md": "#briefing",
            "modelos/estrutura-de-pastas.md": "#pastas",
            "modelos/ficha-de-revisao.md": "#revisao",
            "modelos/guia-de-comandos.md": "#comandos",
            ".claude/skills/": "#skill-estilo",
            "ferramentas/cortar_silencios.py": "#ferramentas",
            "ferramentas/legendar.py": "#ferramentas",
            "ferramentas/": "#ferramentas",
        },
    },
    {
        "titulo": "Mesa Operada por Agentes — Curso HN",
        "manual": "algomaker/curso/MANUAL-MESA-OPERADA-POR-AGENTES-HN.md",
        "saidas": ["CURSO-MESA-AGENTES.html"],
        "chave": "curso-mesa-hn-concluidas",
        "materiais": [
            ("mandato", "Mandato comercial", "algomaker/modelos/mandato-comercial.md"),
            ("aderencia", "Painel de aderência", "algomaker/modelos/painel-aderencia.md"),
        ],
        "grupo_skills": "Doutrina do agente",
        "skills": [
            ("skill-mesa", "Mesa comercial HN", ".claude/skills/mesa-comercial-hn/SKILL.md"),
        ],
        "ferramentas": "algomaker/ferramentas/LEIA-ME.md",
        "codigo": ["algomaker/ferramentas/funil_campanhas.py", "algomaker/ferramentas/mcp_mesa_hn.py",
                   "algomaker/modelos/mandato.json", "algomaker/modelos/exemplo-campanhas.csv"],
        "links": {},
    },
]


def subir_titulos(texto):
    """Promove ## -> #, ### -> ## fora dos blocos de código."""
    saida, em_codigo = [], False
    for linha in texto.splitlines():
        if linha.startswith("```"):
            em_codigo = not em_codigo
        elif not em_codigo and re.match(r"^#{2,6} ", linha):
            linha = linha[1:]
        saida.append(linha)
    return "\n".join(saida)


def limpar_separadores(texto):
    return re.sub(r"(^\s*---\s*$\n?)+\s*\Z", "", texto.strip(), flags=re.M).strip()


def render(texto, links):
    corpo = markdown.markdown(texto, extensions=["tables", "fenced_code", "sane_lists"])

    def trocar(m):
        alvo = m.group(1)
        for fim, ancora in links.items():
            if alvo.endswith(fim):
                return f'href="{ancora}"'
        return m.group(0)

    return re.sub(r'href="([^"#][^"]*)"', trocar, corpo)


def secoes_do_manual(curso):
    texto = (RAIZ / curso["manual"]).read_text(encoding="utf-8")
    partes = re.split(r"(?m)^(?=## )", texto)
    cabecalho, secoes = partes[0], partes[1:]
    intro = [cabecalho.split("\n", 1)[1] if cabecalho.startswith("# ") else cabecalho]
    aulas, final = [], []
    for s in secoes:
        titulo = s.splitlines()[0][3:].strip()
        m = re.match(r"(Aula|Bônus) (\d+) — (.+)", titulo)
        if m:
            tipo, num, nome = m.groups()
            pid = f"{'aula' if tipo == 'Aula' else 'bonus'}-{num}"
            rotulo = f"{num} · {nome}" if tipo == "Aula" else f"B{int(num)} · {nome}"
            aulas.append((pid, rotulo, tipo, subir_titulos(limpar_separadores(s))))
        elif aulas:
            final.append(limpar_separadores(s))
        else:
            intro.append(limpar_separadores(s))
    inicio = f"# {curso['titulo']}\n\n" + subir_titulos("\n\n".join(limpar_separadores(x) for x in intro))
    materiais = subir_titulos("\n\n".join(final))
    return inicio, aulas, materiais


def pagina_md(caminho, links, nota=None):
    texto = (RAIZ / caminho).read_text(encoding="utf-8")
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)
    corpo = render(texto, links)
    if nota:
        corpo = corpo.replace("</h1>", f'</h1><p class="arquivo">{nota}</p>', 1)
    return corpo


def pagina_ferramentas(curso):
    blocos = ["<h2>Código-fonte</h2>"]
    for caminho in curso["codigo"]:
        codigo = (RAIZ / caminho).read_text(encoding="utf-8")
        blocos.append(
            f"<details><summary><code>{html.escape(caminho)}</code></summary>"
            f"<pre><code>{html.escape(codigo)}</code></pre></details>"
        )
    return pagina_md(curso["ferramentas"], curso["links"]) + "\n".join(blocos)


def montar(curso):
    links = curso["links"]
    inicio, aulas, materiais = secoes_do_manual(curso)
    paginas = [("inicio", "Visão geral", "Começo", render(inicio, links))]
    for pid, rotulo, tipo, texto in aulas:
        paginas.append((pid, rotulo, "Aulas" if tipo == "Aula" else "Bônus", render(texto, links)))
    for pid, rotulo, caminho in curso["materiais"]:
        paginas.append((pid, rotulo, "Materiais", pagina_md(caminho, links)))
    paginas.append(("materiais", "Materiais e glossário", "Materiais", render(materiais, links)))
    for pid, rotulo, caminho in curso["skills"]:
        paginas.append((pid, rotulo, curso["grupo_skills"],
                        pagina_md(caminho, links, f"Arquivo: <code>{html.escape(caminho)}</code>")))
    paginas.append(("ferramentas", "Ferramentas", "Ferramentas", pagina_ferramentas(curso)))

    nav, grupo_atual = [], None
    for pid, rotulo, grupo, _ in paginas:
        if grupo != grupo_atual:
            if grupo_atual:
                nav.append("</ul>")
            nav.append(f'<p class="grupo">{html.escape(grupo)}</p><ul>')
            grupo_atual = grupo
        marca = '<span class="ok" aria-hidden="true"></span>' if pid.startswith(("aula-", "bonus-")) else ""
        nav.append(f'<li><a href="#{pid}" data-id="{pid}">{marca}{html.escape(rotulo)}</a></li>')
    nav.append("</ul>")

    secoes = "\n".join(
        f'<section class="pagina" id="pg-{pid}" data-id="{pid}" hidden>{corpo}</section>'
        for pid, _, _, corpo in paginas
    )
    ordem = [{"id": p[0], "rotulo": p[1], "aula": p[0].startswith(("aula-", "bonus-"))} for p in paginas]
    saida = MODELO.replace("{{TITULO}}", html.escape(curso["titulo"])).replace("{{CHAVE}}", curso["chave"])
    saida = saida.replace("{{NAV}}", "\n".join(nav)).replace("{{SECOES}}", secoes)
    saida = saida.replace("{{ORDEM}}", json.dumps(ordem, ensure_ascii=False))
    for destino in curso["saidas"]:
        arq = RAIZ / destino
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_text(saida, encoding="utf-8")
    print(f"{curso['titulo']}: {len(paginas)} páginas -> {', '.join(curso['saidas'])}")


MODELO = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITULO}}</title>
<style>
:root{--bg:#f7f6fb;--painel:#fff;--texto:#1c1530;--suave:#5d5675;--linha:#e4e0ef;--marca:#7c3aed;--marca-suave:#efe7fd;--codigo-bg:#16101f;--codigo-tx:#ece6f8;--ok:#16a34a}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d0915;--painel:#151020;--texto:#ece8f5;--suave:#a39bb8;--linha:#2a2238;--marca:#a78bfa;--marca-suave:#231a36;--codigo-bg:#0a0710;--codigo-tx:#ece6f8;--ok:#4ade80}}
:root[data-theme="dark"]{--bg:#0d0915;--painel:#151020;--texto:#ece8f5;--suave:#a39bb8;--linha:#2a2238;--marca:#a78bfa;--marca-suave:#231a36;--codigo-bg:#0a0710;--codigo-tx:#ece6f8;--ok:#4ade80}
*{box-sizing:border-box}
html{scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--texto);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,sans-serif}
.topo{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--painel);border-bottom:1px solid var(--linha)}
.topo strong{font-size:15px;letter-spacing:.01em}
.topo .marca{width:28px;height:28px;border-radius:8px;background:var(--marca);color:#fff;display:grid;place-items:center;font-weight:800;font-size:13px}
.topo .espaco{flex:1}
.progresso{font-size:13px;color:var(--suave);white-space:nowrap}
.barra{height:4px;width:120px;background:var(--linha);border-radius:4px;overflow:hidden}
.barra i{display:block;height:100%;width:0;background:var(--marca);transition:width .3s}
button{font:inherit;cursor:pointer}
.botao-menu{display:none;background:none;border:1px solid var(--linha);color:var(--texto);border-radius:8px;padding:4px 10px}
.layout{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1240px;margin:0 auto}
nav{position:sticky;top:53px;height:calc(100vh - 53px);overflow:auto;padding:16px 12px 40px;border-right:1px solid var(--linha)}
nav .grupo{margin:18px 10px 6px;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--suave)}
nav ul{list-style:none;margin:0;padding:0}
nav a{display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:8px;color:var(--texto);text-decoration:none;font-size:14.5px}
nav a:hover{background:var(--marca-suave)}
nav a.ativo{background:var(--marca-suave);color:var(--marca);font-weight:600}
nav .ok{width:14px;height:14px;flex:none;border-radius:50%;border:2px solid var(--linha)}
nav a.feito .ok{background:var(--ok);border-color:var(--ok)}
main{padding:32px 40px 80px;min-width:0}
.pagina{max-width:760px}
h1{font-size:32px;line-height:1.2;margin:0 0 20px;letter-spacing:-.01em}
h2{font-size:22px;margin:36px 0 12px;padding-top:8px}
h3{font-size:18px;margin:26px 0 8px}
a{color:var(--marca)}
blockquote{margin:18px 0;padding:12px 16px;background:var(--marca-suave);border-left:4px solid var(--marca);border-radius:0 10px 10px 0}
blockquote p{margin:.3em 0}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:15px;display:block;overflow-x:auto}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--linha);vertical-align:top}
th{background:var(--marca-suave)}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.9em;background:var(--marca-suave);padding:.1em .35em;border-radius:5px}
pre{position:relative;background:var(--codigo-bg);color:var(--codigo-tx);padding:40px 16px 16px;border-radius:12px;overflow-x:auto;font-size:14px;line-height:1.55}
pre code{background:none;padding:0;color:inherit;white-space:pre}
.copiar{position:absolute;top:8px;right:8px;background:#ffffff1a;color:#fff;border:1px solid #ffffff33;border-radius:6px;padding:2px 10px;font-size:12px}
.copiar:hover{background:#ffffff33}
details{margin:12px 0;border:1px solid var(--linha);border-radius:10px;padding:8px 14px;background:var(--painel)}
summary{cursor:pointer;font-weight:600}
.arquivo{color:var(--suave);font-size:14px;margin-top:-10px}
.rodape{max-width:760px;display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center;margin-top:40px;padding-top:20px;border-top:1px solid var(--linha)}
.rodape a{text-decoration:none;padding:8px 14px;border:1px solid var(--linha);border-radius:10px;background:var(--painel);color:var(--texto);font-size:14px}
.rodape a:hover{border-color:var(--marca)}
.concluir{display:flex;align-items:center;gap:8px;font-weight:600;padding:8px 14px;border-radius:10px;border:1px solid var(--marca);background:var(--painel);color:var(--marca)}
.concluir.feito{background:var(--ok);border-color:var(--ok);color:#fff}
@media (max-width:860px){
.layout{grid-template-columns:1fr}
.botao-menu{display:block}
nav{position:fixed;top:53px;left:0;width:min(300px,85vw);background:var(--painel);z-index:15;transform:translateX(-105%);transition:transform .2s;box-shadow:0 10px 30px #0004}
body.menu-aberto nav{transform:none}
main{padding:24px 16px 64px}
h1{font-size:26px}
.barra{display:none}
}
</style>
</head>
<body>
<header class="topo">
<button class="botao-menu" aria-label="Abrir menu" onclick="document.body.classList.toggle('menu-aberto')">☰</button>
<span class="marca">HN</span><strong>{{TITULO}}</strong>
<span class="espaco"></span>
<span class="progresso" id="progresso"></span><span class="barra"><i id="barra"></i></span>
</header>
<div class="layout">
<nav aria-label="Conteúdo do curso">{{NAV}}</nav>
<main>
{{SECOES}}
<div class="rodape" id="rodape"></div>
</main>
</div>
<script>
const ORDEM={{ORDEM}};
const CHAVE="{{CHAVE}}";
function ler(){try{return new Set(JSON.parse(localStorage.getItem(CHAVE)||"[]"))}catch(e){return new Set()}}
function gravar(s){try{localStorage.setItem(CHAVE,JSON.stringify([...s]))}catch(e){}}
let feitas=ler();
function atualizarProgresso(){
  const aulas=ORDEM.filter(p=>p.aula);
  const n=aulas.filter(p=>feitas.has(p.id)).length;
  document.getElementById("progresso").textContent=n+"/"+aulas.length+" aulas";
  document.getElementById("barra").style.width=(100*n/aulas.length)+"%";
  document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("feito",feitas.has(a.dataset.id)));
}
function mostrar(){
  let id=location.hash.slice(1);
  if(!ORDEM.some(p=>p.id===id))id="inicio";
  document.querySelectorAll(".pagina").forEach(s=>s.hidden=s.dataset.id!==id);
  document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("ativo",a.dataset.id===id));
  const i=ORDEM.findIndex(p=>p.id===id),p=ORDEM[i],ant=ORDEM[i-1],prox=ORDEM[i+1];
  const r=document.getElementById("rodape");r.innerHTML="";
  r.append(ant?link(ant,"← "+ant.rotulo):document.createElement("span"));
  if(p.aula){
    const b=document.createElement("button");b.className="concluir";
    const pintar=()=>{const f=feitas.has(id);b.classList.toggle("feito",f);b.textContent=f?"✓ Aula concluída":"Marcar como concluída"};
    b.onclick=()=>{feitas.has(id)?feitas.delete(id):feitas.add(id);gravar(feitas);pintar();atualizarProgresso()};
    pintar();r.append(b);
  }
  if(prox)r.append(link(prox,prox.rotulo+" →"));
  document.body.classList.remove("menu-aberto");
  window.scrollTo(0,0);
  document.title=p.rotulo+" · {{TITULO}}";
}
function link(p,t){const a=document.createElement("a");a.href="#"+p.id;a.textContent=t;return a}
document.querySelectorAll("pre").forEach(pre=>{
  const b=document.createElement("button");b.className="copiar";b.textContent="Copiar";
  b.onclick=async()=>{
    const t=pre.querySelector("code").innerText;
    try{await navigator.clipboard.writeText(t)}catch(e){const a=document.createElement("textarea");a.value=t;document.body.append(a);a.select();document.execCommand("copy");a.remove()}
    b.textContent="Copiado";setTimeout(()=>b.textContent="Copiar",1500);
  };
  pre.append(b);
});
window.addEventListener("hashchange",mostrar);
atualizarProgresso();mostrar();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    for c in CURSOS:
        montar(c)
