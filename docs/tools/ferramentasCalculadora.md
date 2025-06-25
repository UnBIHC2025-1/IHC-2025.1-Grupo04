<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Ferramentas de Acessibilidade</title>
  <style>
    :root {
      --cor-primaria: #4cae4f;
      /* --cor-fundo: #f0f4f8; */
      /* --cor-card: #ffffff; */
      --cor-texto:rgb(255, 255, 255);
      --sombra: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    options {
      margin: 0.5rem 1.5rem;
    }

    input[type="radio"]:checked {
      accent-color: green;
    }

    button {
      display: block;
      margin: 2rem auto 0;
      padding: 0.75rem 2rem;
      font-size: 1rem;
      background-color: var(--cor-primaria);
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    button:hover {
      background-color:rgb(50, 114, 52);
    }

    #resultado {
      margin-top: 2rem;
    }
  </style>
  
</head>
<body>
  <div class="container">
    <h1>Calculadora de Ferramentas de Acessibilidade</h1>
    <h2>Receba recomendações com base no seu caso</h2>
    <form id="form">
      <label>1. Você está desenvolvendo para qual plataforma?</label>
      <div class="options">
        <input type="radio" name="plataforma" value="web"> Web
        <input type="radio" name="plataforma" value="android"> Android
      </div>

      <label>2. Quer realizar auditoria automatizada?</label>
      <div class="options">
        <input type="radio" name="auditoria" value="sim"> Sim
        <input type="radio" name="auditoria" value="nao"> Não
      </div>

      <label>3. Precisa validar contraste de cores?</label>
      <div class="options">
        <input type="radio" name="contraste" value="sim"> Sim
        <input type="radio" name="contraste" value="nao"> Não
      </div>

      <label>4. Precisa de um leitor de tela?</label>
      <div class="options">
        <input type="radio" name="leitor" value="sim"> Sim
        <input type="radio" name="leitor" value="nao"> Não
      </div>

      <label>5. Quer gerar mapa de site visual?</label>
      <div class="options">
        <input type="radio" name="sitemap" value="sim"> Sim
        <input type="radio" name="sitemap" value="nao"> Não
      </div>

      <label>6. Precisa testar com regras WCAG?</label>
      <div class="options">
        <input type="radio" name="wcag" value="sim"> Sim
        <input type="radio" name="wcag" value="nao"> Não
      </div>

      <label>7. Deseja testes diretamente no Chrome?</label>
      <div class="options">
        <input type="radio" name="chrome" value="sim"> Sim
        <input type="radio" name="chrome" value="nao"> Não
      </div>

      <label>8. Deseja integração com testes automatizados?</label>
      <div class="options">
        <input type="radio" name="automacao" value="sim"> Sim
        <input type="radio" name="automacao" value="nao"> Não
      </div>

      <label>9. Procura por uma caixa de ferramentas completa?</label>
      <div class="options">
        <input type="radio" name="caixa" value="sim"> Sim
        <input type="radio" name="caixa" value="nao"> Não
      </div>

      <label>10. Precisa de acessibilidade para usuários com baixa visão?</label>
      <div class="options">
        <input type="radio" name="visao" value="sim"> Sim
        <input type="radio" name="visao" value="nao"> Não
      </div>
      <label>11. Você quer suporte a código open-source?</label>
      <div class="options">
        <input type="radio" name="opensource" value="sim"> Sim
        <input type="radio" name="opensource" value="nao"> Não
      </div>

      <label>12. Você trabalha com equipes que usam Windows ou Apple?</label>
      <div class="options">
        <input type="radio" name="ecossistema" value="windows"> Windows
        <input type="radio" name="ecossistema" value="apple"> Apple
      </div>
      <button type="submit">Ver recomendações</button>
    </form>

    <div id="resultado"></div>
  </div>

  <script>
    document.getElementById("form").addEventListener("submit", function(e) {
      e.preventDefault();

      const respostas = {};
      document.querySelectorAll("input[type=radio]:checked").forEach(input => {
        respostas[input.name] = input.value;
      });

      const ferramentas = {
        wave: { nome: "WAVE", url: "https://wave.webaim.org/", pontos: 0 },
        axe: { nome: "AXE Core", url: "https://github.com/dequelabs/axe-core", pontos: 0 },
        lighthouse: { nome: "Lighthouse", url: "https://developer.chrome.com/docs/lighthouse", pontos: 0 },
        contrast: { nome: "WebAIM Contrast Checker", url: "https://webaim.org/resources/contrastchecker/", pontos: 0 },
        jaws: { nome: "JAWS", url: "https://www.tecassistiva.com.br/catalogo/jaws/", pontos: 0 },
        dyno: { nome: "DynoVisual Sitemap Generator", url: "https://dynomapper.com/", pontos: 0 },
        checks: { nome: "ACHECKS", url: "https://www.achecks.org/", pontos: 0 },
        android: { nome: "Accessibility Test Framework", url: "https://github.com/google/Accessibility-Test-Framework-for-Android", pontos: 0 },
        insights: { nome: "Accessibility Insights", url: "https://accessibilityinsights.io/", pontos: 0 },
        pa11y: { nome: "Pa11y", url: "https://pa11y.org/", pontos: 0 },
        nvda: { nome: "NVDA", url: "https://www.nvaccess.org/", pontos: 0 },
        voiceover: { nome: "VoiceOver", url: "https://www.apple.com/accessibility/voiceover/", pontos: 0 },
        siteimprove: { nome: "Siteimprove", url: "https://siteimprove.com/en-us/accessibility/accessibility-checker/", pontos: 0 },
        tota11y: { nome: "Tota11y", url: "https://khan.github.io/tota11y/", pontos: 0 }
      };

      // Pontuação baseada nas respostas
      if (respostas.plataforma === "web") {
        ferramentas.wave.pontos += 2;
        ferramentas.axe.pontos += 2;
        ferramentas.lighthouse.pontos += 2;
        ferramentas.insights.pontos += 2;
        ferramentas.pa11y.pontos += 1;
        ferramentas.siteimprove.pontos += 1;
        ferramentas.tota11y.pontos += 1;
      } else if (respostas.plataforma === "android") {
        ferramentas.android.pontos += 3;
      }

      if (respostas.auditoria === "sim") {
        ferramentas.axe.pontos += 1;
        ferramentas.lighthouse.pontos += 1;
        ferramentas.insights.pontos += 1;
      }

      if (respostas.contraste === "sim" || respostas.visao === "sim") {
        ferramentas.contrast.pontos += 3;
      }

      if (respostas.leitor === "sim") {
        ferramentas.jaws.pontos += 2;
        ferramentas.nvda.pontos += 2;
        ferramentas.voiceover.pontos += 2;
      }

      if (respostas.sitemap === "sim") ferramentas.dyno.pontos += 2;
      if (respostas.caixa === "sim") ferramentas.checks.pontos += 2;
      if (respostas.automacao === "sim") {
        ferramentas.axe.pontos += 2;
        ferramentas.pa11y.pontos += 2;
      }

      if (respostas.wcag === "sim") {
        ferramentas.axe.pontos += 1;
        ferramentas.checks.pontos += 1;
        ferramentas.pa11y.pontos += 1;
      }

      if (respostas.chrome === "sim") {
        ferramentas.lighthouse.pontos += 2;
        ferramentas.insights.pontos += 2;
        ferramentas.siteimprove.pontos += 2;
        ferramentas.tota11y.pontos += 1;
      }

      if (respostas.opensource === "sim") {
        ferramentas.nvda.pontos += 2;
        ferramentas.pa11y.pontos += 2;
        ferramentas.axe.pontos += 1;
        ferramentas.tota11y.pontos += 1;
      }

      if (respostas.ecossistema === "windows") {
        ferramentas.jaws.pontos += 2;
        ferramentas.nvda.pontos += 2;
      } else if (respostas.ecossistema === "apple") {
        ferramentas.voiceover.pontos += 3;
      }

      const ordenadas = Object.values(ferramentas).sort((a, b) => b.pontos - a.pontos);
      const maxPontos = Math.max(...Object.values(ferramentas).map(f => f.pontos));

      const icones = {
        "WAVE": "🌊",
        "AXE Core": "🪓",
        "Lighthouse": "🔦",
        "WebAIM Contrast Checker": "🎨",
        "JAWS": "🗣️",
        "NVDA": "🆓",
        "VoiceOver": "🍎",
        "Accessibility Insights": "🔍",
        "DynoVisual Sitemap Generator": "🗺️",
        "ACHECKS": "🧰",
        "Accessibility Test Framework": "🤖",
        "Pa11y": "⚙️",
        "Siteimprove": "📊",
        "Tota11y": "👁️"
      };

      let html = `<p font-weight:bold;">Ranking de Ferramentas Recomendadas:</p>`;
      html += `<div>`;

      ordenadas.forEach((f, index) => {
        const pontosNormalizados = maxPontos > 0 ? (f.pontos / maxPontos) * 5 : 0;
        const largura = (pontosNormalizados / 5) * 100;
        const pontosFormatado = pontosNormalizados.toFixed(1);

        const medalha = index === 0 ? "🥇" : index === 1 ? "🥈" : index === 2 ? "🥉" : "";
        const icone = icones[f.nome] || "";

        html += `
          <div class="barra" style="background-color:rgb(105, 105, 105); border-radius: 8px; overflow: hidden; margin-bottom: 8px;">
            <a href="${f.url}" target="_blank" style="text-decoration:none;">
              <span class="barra-preenchida" style="
                display: block;
                width: 0;
                background-color: #004080;
                color: #fff;
                font-weight: bold;
                padding: 0.5px 8px;
                font-size: 0.9rem;
                white-space: nowrap;
                border-radius: 8px 0 0 8px;">
                ${medalha} ${icone} ${f.nome} (${pontosFormatado} pts)
              </span>
            </a>
          </div>`;
      });

      html += `</div>`;
      document.getElementById("resultado").innerHTML = html;

      const barras = document.querySelectorAll(".barra-preenchida");
      barras.forEach((barra, i) => {
        const pontosNormalizados = maxPontos > 0 ? (ordenadas[i].pontos / maxPontos) * 5 : 0;
        const largura = (pontosNormalizados / 5) * 100;
        setTimeout(() => {
          barra.style.transition = "width 1s ease-in-out";
          barra.style.width = largura + "%";
        }, 100);
      });
    });
  </script>
</body>
</html>