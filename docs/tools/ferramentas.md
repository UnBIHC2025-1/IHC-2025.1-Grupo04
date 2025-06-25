# 🧰 Ferramentas de Acessibilidade — Guia por Categorias

Uma seleção de ferramentas úteis para testes, auditoria e suporte à acessibilidade digital, organizadas por categorias.

---

## 🧪 Testes Automáticos de Acessibilidade

- **[AXE - Accessibility Engine](https://github.com/dequelabs/axe-core)**  
  Motor de acessibilidade para testes automatizados em interfaces web.  
  🔗 Instalação via NPM: `npm install axe-core`

- **[Lighthouse (Google)](https://developer.chrome.com/docs/lighthouse)**  
  Ferramenta de auditoria integrada ao Chrome DevTools.  
  🔗 Já vem com o Chrome ou use a [Extensão do Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)

- **[Accessibility Insights (Microsoft)](https://accessibilityinsights.io/)**  
  Ferramenta para testes rápidos e detalhados.  
  🔗 [Extensão para Chrome](https://chrome.google.com/webstore/detail/accessibility-insights-for/...)

- **[ACHECKS](https://www.achecks.org/)**  
  Caixa de ferramentas para validar acessibilidade conforme WCAG.  
  🔗 Acesso via navegador (não requer instalação).

- **[Pa11y](https://pa11y.org/)**  
  Ferramenta CLI para testar páginas e gerar relatórios.  
  🔗 Instalação via NPM: `npm install -g pa11y`

---

## 🌐 Avaliação Visual e Análise Manual

- **[Wave - Web Accessibility Evaluation Tool](https://wave.webaim.org/)**  
  Visualiza erros de acessibilidade diretamente na página.  
  🔗 [Extensão para Chrome](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh)

- **[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)**  
  Calcula o contraste de cores entre texto e fundo.  
  🔗 Acesso direto via navegador.

- **[Tota11y (Khan Academy)](https://khan.github.io/tota11y/)**  
  Ferramenta visual para depurar problemas de acessibilidade.  
  🔗 Acesso via navegador ou instale como script:  
  `npm install tota11y`

---

## 🧭 Mapeamento e Organização de Conteúdo

- **[DynoMapper - Sitemap e A11Y Testing](https://dynomapper.com/)**  
  Gera sitemaps visuais e testes de acessibilidade de URLs.  
  🔗 Acesso via navegador (plano gratuito disponível).

- **[Siteimprove Accessibility Checker](https://siteimprove.com/en-us/accessibility/accessibility-checker/)**  
  Scanner de acessibilidade com sugestões detalhadas.  
  🔗 [Extensão para Chrome](https://chrome.google.com/webstore/detail/siteimprove-accessibility/djcglbcoieedgggkebcijbaaaejpnbpb)

---

## 📱 Frameworks e Ferramentas para Aplicativos Mobile

- **[Accessibility Test Framework for Android](https://github.com/google/Accessibility-Test-Framework-for-Android)**  
  Framework do Google para automatizar testes de acessibilidade em apps Android.  
  🔗 Adição ao projeto Android:  
  ```gradle
  androidTestImplementation 'androidx.test.uiautomator:uiautomator:2.2.0'

<div style="margin-top: 2rem;">
    <a href="ferramentasCalculadora.html" aria-label="Acessar calculadora de recomendação de ferramentas">
      <button style="
        background-color: #4cae4f;
        color: white;
        padding: 12px 24px;
        font-size: 1rem;
        border: none;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease;">
        ➕ Usar Calculadora de Acessibilidade
      </button>
    </a>
</div>

