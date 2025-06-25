# Do e Donot

## Desenvolvimento

### Imagens

```html
<!-- DO -->
<img src="grafico.png" alt="Gráfico de crescimento anual">
<!-- DON'T -->
<img src="grafico.png">

<!-- DO -->
<img src="decorativo.png" alt="">
<!-- DON'T -->
<img src="decorativo.png" alt="imagem legal">

<!-- DO -->
<img src="texto-promocao.png" alt="Compre 1 e leve 2 - Promoção válida até domingo">
<!-- DON'T -->
<img src="texto-promocao.png">
```

### Vídeos e Áudios

```html
<!-- DO -->
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="subtitles" src="legenda.vtt" srclang="pt" label="Português">
</video>
<!-- DON'T -->
<video controls>
  <source src="video.mp4" type="video/mp4">
</video>
```

### Controles

```html
<!-- DO -->
<a href="/home">Início</a>
<!-- DON'T -->
<a>Início</a>

<!-- DO -->
<a href="/contato" style="text-decoration: underline">Contato</a>
<!-- DON'T -->
<a href="/contato" style="text-decoration: none">Contato</a>

<!-- DO -->
<input onfocus="this.style.border='2px solid #00f'">
<!-- DON'T -->
<input>

<!-- DO -->
<button type="button">Cancelar</button>
<!-- DON'T -->
<button>Cancelar</button>

<!-- DO -->
<a href="#main-content" class="skip-link">Pular para conteúdo principal</a>
<!-- DON'T -->
<!-- nenhum skip link -->

<!-- DO -->
<a href="https://externo.com" target="_blank" rel="noopener">Abrir em nova aba</a>
<!-- DON'T -->
<a href="https://externo.com" target="_blank">Abrir em nova aba</a>

<!-- DO -->
<select>
  <option>Selecione</option>
</select>
<!-- DON'T -->
<select onchange="window.location.href=this.value">
  <option value="/auto">Auto Redireciona</option>
</select>

<!-- DO -->
<div ontouchstart="handler()" tabindex="0">Interação por movimento com alternativa</div>
<!-- DON'T -->
<div ontouchstart="handler()">Somente gesto</div>

```

### Formulário

```html
<!-- DO -->
<label for="email">E-mail</label>
<input type="email" id="email">
<!-- DON'T -->
<input type="email">

<!-- DO -->
<fieldset>
  <legend>Escolha uma opção</legend>
  <label><input type="radio" name="opcao"> Sim</label>
  <label><input type="radio" name="opcao"> Não</label>
</fieldset>
<!-- DON'T -->
<label><input type="radio" name="opcao"> Sim</label>
<label><input type="radio" name="opcao"> Não</label>

<!-- DO -->
<input type="text" name="nome" autocomplete="name">
<!-- DON'T -->
<input type="text" name="nome">

<!-- DO -->
<div class="erro" role="alert">Erro: nome é obrigatório</div>
<form>...</form>
<!-- DON'T -->
<form><div class="erro">Erro: nome é obrigatório</div>...</form>

<!-- DO -->
<input id="senha" aria-describedby="requisitos">
<div id="requisitos">A senha deve ter ao menos 8 caracteres</div>
<!-- DON'T -->
<input id="senha">

<!-- DO -->
<div role="alert">Cadastro realizado com sucesso</div>
<!-- DON'T -->
<div class="sucesso">Cadastro realizado com sucesso</div>
```

### Mídia

```html
<!-- DO -->
<video controls>
  <source src="demo.mp4" type="video/mp4">
</video>
<!-- DON'T -->
<video autoplay>
  <source src="demo.mp4" type="video/mp4">
</video>

<!-- DO -->
<button type="submit">Enviar</button>
<!-- DON'T -->
<button>Enviar</button>

<!-- DO -->
<video controls>
  <source src="midia.mp4">
  <button onclick="pauseVideo()">Pausar vídeo</button>
</video>
<!-- DON'T -->
<video autoplay loop>
  <source src="midia.mp4">
</video>

<!-- DO -->
<p>Transcrição: Este áudio descreve os recursos de acessibilidade disponíveis.</p>
<!-- DON'T -->
<!-- nenhum conteúdo de transcrição -->
```

### Semântica

```html
<!-- DO -->
<main><section><h1>Título</h1></section></main>
<!-- DON'T -->
<div><div><span style="font-size: 24px">Título</span></div></div>
```

### Texto

```html
<!-- DO -->
<p>Promoção imperdível: leve 3 e pague 2</p>
<!-- DON'T -->
<img src="promo-texto.png" alt="promoção imperdível">
```

### Teclado

```html
<!-- DO -->
<button accesskey="s">Salvar</button>
<!-- DON'T -->
<div onclick="salvar()">Salvar</div>

<!-- DO -->
<div tabindex="0" onmouseover="...">Dica</div>
<!-- DON'T -->
<div onmouseover="...">Dica</div>

<!-- DO -->
<style>
  button:focus {
    outline: 2px solid green;
  }
</style>
<!-- DON'T -->
<style>
  button:focus {
    outline: none;
  }
</style>

<!-- DO -->
<style>
  .botao:hover, .botao:focus {
    background: #333;
  }
</style>
<!-- DON'T -->
<style>
  .botao:hover {
    background: #333;
  }
</style>

<!-- DO -->
<button tabindex="0">Enviar</button>
<!-- DON'T -->
<div onclick="enviar()">Enviar</div>

<!-- DO -->
<a href="#conteudo" class="skip-link">Pular conteúdo</a>
<!-- DON'T -->
<!-- nenhum skip link -->
```

### Títulos

```html
<!-- DO -->
<h1>Sobre nós</h1><h2>Missão</h2><h3>Visão</h3>
<!-- DON'T -->
<h1>Sobre nós</h1><h3>Missão</h3>

<!-- DO -->
<h1>Página de Contato</h1>
<!-- DON'T -->
<div style="font-size: 24px">Página de Contato</div>
```

### Tabelas

```html
<!-- DO -->
<table>
  <caption>Estatísticas de uso</caption>
  <thead>
    <tr><th scope="col">Usuário</th><th scope="col">Acessos</th></tr>
  </thead>
  <tbody>
    <tr><td>Maria</td><td>20</td></tr>
  </tbody>
</table>
<!-- DON'T -->
<table>
  <tr><td>Usuário</td><td>Acessos</td></tr>
  <tr><td>Maria</td><td>20</td></tr>
</table>

<!-- DO -->
<p>Esta tabela mostra as vendas do mês por região.</p>
<!-- DON'T -->
<!-- nenhuma explicação textual -->
```

### Modais

```html
<!-- DO -->
<div role="dialog" aria-modal="true">
  <button onclick="closeModal()">Fechar</button>
</div>
<!-- DON'T -->
<div class="modal">Modal sem botão de fechar</div>

<!-- DO -->
<div role="dialog" aria-modal="true">
  <button onkeydown="if(event.key==='Escape'){closeModal()}">Fechar</button>
</div>
<!-- DON'T -->
<div role="dialog">Sem ESC</div>
```

### Mobile

```html
<!-- DO -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- DON'T -->
<!-- ausência de meta viewport -->

<!-- DO -->
<style>
  body {
    overflow-x: hidden;
  }
</style>
<!-- DON'T -->
<style>
  body {
    overflow-x: auto;
  }
</style>

<!-- DO -->
<button style="padding: 12px 20px;">Toque aqui</button>
<!-- DON'T -->
<button style="padding: 5px 5px;">Toque aqui</button>

<!-- DO -->
<style>
  .botao + .botao {
    margin-left: 1rem;
  }
</style>
<!-- DON'T -->
<!-- botões colados -->
```

### Extras

```html
<!-- DO -->
<marquee behavior="scroll" direction="left" aria-hidden="true"></marquee>
<button onclick="pararConteudo()">Parar</button>
<!-- DON'T -->
<marquee behavior="scroll" direction="left"></marquee>

<!-- DO -->
<nav aria-label="Você está aqui">
  <ol><li><a href="/">Início</a></li><li>Página atual</li></ol>
</nav>
<!-- DON'T -->
<!-- nenhum breadcrumb -->

<!-- DO -->
<a href="/acessibilidade">Dicas de acessibilidade</a>
<!-- DON'T -->
<!-- nenhuma seção de dicas -->

<!-- DO -->
<button style="width: 44px; height: 44px;">OK</button>
<!-- DON'T -->
<button style="width: 20px; height: 20px;">OK</button>

<!-- DO -->
<label for="captcha">Resolva: 2+2 = ?</label>
<input id="captcha" type="text">
<!-- DON'T -->
<img src="captcha.png">

<!-- DO -->
<input type="search" placeholder="Buscar no site">
<!-- DON'T -->
<!-- nenhum campo de busca -->
```


## Design

### Aparencia

```html
<!-- DO -->
<p>Pressione o botão com o ícone de engrenagem <strong>localizado acima</strong> para abrir as configurações.</p>
<!-- DON'T -->
<p>Pressione o botão vermelho à direita.</p>

<!-- DO -->
<p>Os campos obrigatórios estão marcados com um asterisco *</p>
<!-- DON'T -->
<p>Campos obrigatórios estão marcados em vermelho.</p>

<!-- DO -->
<div style="font-size: 1.2em;">Texto que se adapta ao zoom</div>
<!-- DON'T -->
<div style="font-size: 12px;">Texto fixo</div>

<!-- DO -->
<p style="max-width: 600px;">Este parágrafo possui no máximo 80 caracteres por linha e facilita a leitura.</p>
<!-- DON'T -->
<p style="max-width: 1000px; text-align: justify;">Texto com linhas muito longas e alinhamento justificado prejudica a leitura.</p>

<!-- DO -->
<button>
  <i class="icon-download"></i> Baixar
</button>
<!-- DON'T -->
<button><i class="icon-download"></i></button>

<!-- DO -->
<button style="min-height: 24px; min-width: 24px;">Enviar</button>
<!-- DON'T -->
<button style="width: 16px; height: 16px;"></button>

<!-- DO -->
<style>
  .escondido {
    position: absolute;
    left: -9999px;
  }
</style>
<!-- DON'T -->
<style>
  .escondido {
    display: none;
  }
</style>
```

### Animação

```html
<!-- DO -->
<style>
  @media (prefers-reduced-motion: reduce) {
    .animar {
      animation: none;
    }
  }
</style>
<!-- DON'T -->
<style>
  .animar {
    animation: bounce 2s infinite;
  }
</style>

<!-- DO -->
<div class="marquee" aria-hidden="true"></div>
<button onclick="pausarAnimacao()">Pausar animação</button>
<!-- DON'T -->
<div class="marquee"></div>
```

### Contraste de cores

```html
<!-- DO -->
<p style="color: #000; background: #fff;">Texto com contraste adequado</p>
<!-- DON'T -->
<p style="color: #aaa; background: #fff;">Texto com pouco contraste</p>

<!-- DO -->
<h1 style="color: #111; font-size: 2em;">Título destacado</h1>
<!-- DON'T -->
<h1 style="color: #bbb; font-size: 2em;">Título apagado</h1>

<!-- DO -->
<i class="icone" style="color: #222;"></i>
<!-- DON'T -->
<i class="icone" style="color: #ccc;"></i>

<!-- DO -->
<input style="border: 2px solid #333">
<!-- DON'T -->
<input style="border: 1px solid #ddd">

<!-- DO -->
<div style="background: url('imagem.jpg'); color: #fff; text-shadow: 1px 1px #000;">
  Texto sobre imagem
</div>
<!-- DON'T -->
<div style="background: url('imagem.jpg'); color: #fff;">
  Texto sobre imagem
</div>

<!-- DO -->
<style>
  ::selection {
    background: #000;
    color: #fff;
  }
</style>
<!-- DON'T -->
<style>
  ::selection {
    background: #eee;
    color: #ccc;
  }
</style>
```

## Geração de Conteúdo

### Termos e textos

```html
<!-- DO -->
<p>O site oferece recursos para <strong>pessoas com deficiência visual</strong>.</p>
<!-- DON'T -->
<p>O site oferece recursos para deficientes.</p>

<!-- DO -->
<p>Clique no botão para continuar.</p>
<!-- DON'T -->
<p>Não perca tempo! Clique agora mesmo!</p>

<!-- DO -->
<p>Use palavras simples e frases curtas.</p>
<!-- DON'T -->
<p>Em virtude das circunstâncias previamente mencionadas, recomendamos enfaticamente...</p>
```

### Ícones

```html
<!-- DO -->
<button aria-label="Salvar">
  💾 <span>Salvar</span>
</button>
<!-- DON'T -->
<button>💾</button>

<!-- DO -->
<i class="icon-seta" aria-label="Ir para a próxima página"></i>
<!-- DON'T -->
<i class="icon-seta"></i>
```

<!-- ===================== -->
<!-- HIPERLINKS -->
<!-- ===================== -->

### Hiperlinks

```html
<!-- DO -->
<a href="/relatorio">Baixar relatório em PDF</a>
<!-- DON'T -->
<a href="/relatorio">Clique aqui</a>
```

## Gestão de Projetos

###  Primeiros Passos

```html
<!-- DO -->
<p>Incluímos uma persona representando <strong>uma pessoa com deficiência visual</strong> no planejamento do projeto.</p>
<!-- DON'T -->
<p>Definimos um usuário genérico sem considerar deficiência alguma.</p>

<!-- DO -->
<p>Modelamos também <strong>personas com deficiência física, neurodiversidade e analfabetismo funcional</strong>.</p>
<!-- DON'T -->
<p>Consideramos apenas usuários que usam o sistema com mouse e teclado.</p>
```

### Conscientização

```html
<!-- DO -->
<p>Apresentamos dados do IBGE à equipe, como: "Cerca de 18,6% da população brasileira possui algum tipo de deficiência".</p>
<!-- DON'T -->
<p>A equipe não foi orientada sobre o público com deficiência.</p>

<!-- DO -->
<p>Discutimos a legislação vigente, como a <strong>Convenção sobre os Direitos das Pessoas com Deficiência</strong>.</p>
<!-- DON'T -->
<p>Ignoramos normas legais e diretrizes internacionais.</p>

<!-- DO -->
<p>Estimamos o esforço adicional de forma realista e mostramos exemplos de como acessibilidade gera mais alcance.</p>
<!-- DON'T -->
<p>Afirmamos que acessibilidade só dá trabalho e não vale a pena.</p>
```

### Planejamento

```html
<!-- DO -->
<p>Definimos atividades com metas baseadas nas diretrizes <strong>WCAG nível A e AA</strong>.</p>
<!-- DON'T -->
<p>Não incluímos nenhuma atividade específica relacionada à acessibilidade.</p>

<!-- DO -->
<p>Alocamos recursos como treinamentos, revisores e ferramentas de validação de acessibilidade.</p>
<!-- DON'T -->
<p>Acreditamos que os desenvolvedores resolverão tudo sozinhos no final do projeto.</p>
```