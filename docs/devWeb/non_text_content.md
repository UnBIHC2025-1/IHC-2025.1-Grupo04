# Desenvolvimento

"Nessa fase, é importante garantir que a equipe de desenvolvimento saiba como implementar acessibilidade, verificá-la e usar as ferramentas disponíveis no mercado para
testes e padronizações. Também é importante que a equipe saiba como as pessoas com deficiência usam os sítios web e aplicativos". Nesse caso, foram incluídas técnicas relacionadas ao desenvolvimento e também formas de verificar.

## Imagens

- [ ] <b> Adicionar ``` alt ``` </b> para imagens, botões-imagem, gráficos e imagens de mapas com pontos de acesso. <a id="TEC1" href="#RP1">[1]</a>
- [ ] <b> Adicionar ``` alt="" ``` </b> para imagens decorativas que não tem significado. <a id="TEC1" href="#RP1">[1]</a>
- [ ] <b> Incluir a descrição no ``` alt ```</b> para imagens que contém texto. <a id="TEC1" href="#RP1">[1]</a>

## Vídeos e Áudios
- [ ] <b> Adicionar legendas</b> para áudio em vídeos existentes. <a id="TEC2" href="#RP2">[2]</a>
- [ ] <b> Evitar conteúdo com <i>flashes</i> (gatilhos para convulsões)</b> ou manter abaixo dos limites. <a id="TEC3" href="#RP3">[3]</a>

## Controles
- [ ] <b> Adicionar ``` href ```</b> para links. <a id="TEC4" href="#RP4">[4]</a>
- [ ] <b> Adicionar underline</b> nos links. <a id="TEC5" href="#RP5">[5]</a>
- [ ] <b> Adicionar estados de foco</b> em campos de entrada, botões, e elementos interativos. <a id="TEC6" href="#RP6">[6]</a>
- [ ] <b> Adicionar ```type="button"```</b> nos botões. <a id="TEC4" href="#RP4">[4]</a>
- [ ] <b> Adicionar skip-link </b> (link para pular) para o conteúdo principal. <a id="TEC7" href="#RP7">[7]</a>
- [ ] <b> Identifique e comunique </b> links que abrem em uma nova guia ou janela. <a id="TEC8" href="#RP8">[8]</a>
- [ ] <b> Toda mudança de contexto tem que ser previsível</b>, é iniciada apenas pelo usuário, ou há mecanismos para desativar essas mudanças de contexto.<b>  NBR 5.8.8 </b>
- [ ] <b> Toda operação por movimento deve</b>, conter formas para operar de outra forma, ou pode ser desativada pelo usuário.<b>  NBR 5.8.13 </b>


## Formulário
- [ ] <b> Adicionar ``` label ```</b> para os campos de entradas associadas ao elemento correspondente. <a id="TEC9" href="#RP9">[9]</a>
- [ ] <b> Adicionar ``` <fildset> ``` e ``` <legend> ```</b> para seção no formulário. <a id="TEC4" href="#RP4">[4]</a>
- [ ] <b> Adicionar ``` autocomplete ```</b> para campos de entrada. <a id="TEC10" href="#RP10">[10]</a>
- [ ] <b> Exibir ``` errors ``` </b> (erros) de entrada acima do formulário, após envio. <a id="TEC11" href="#RP11">[11]</a>
- [ ] <b> Adicionar ``` aria-describedby ```</b> para os campos de entrada. <a id="TEC11" href="#RP11">[11]</a>
- [ ] <b> Exibir mensagens de erro e sucesso</b> não só visualmente. <a id="TEC5" href="#RP5">[5]</a>

## Mídia
- [ ] <b> Impedir ``` autoplay ```</b> para vídeos e audios maiores que 3 segundos. <a id="TEC12" href="#RP12">[12]</a>
- [ ] <b> Adicionar ``` type ```</b> para botões e entradas. <a id="TEC4" href="#RP4">[4]</a>
- [ ] <b> Adicionar pausa </b> para todas as mídias. <a id="TEC13" href="#RP13">[13]</a>
- [ ] <b> Adicionar transcrição </b> para audios. <a id="TEC1" href="#RP1">[1]</a>

## Semântica
- [ ] Uso de elementos <b>nativos HTML</b>. 
- [ ] Fluxo continuo e <b>Lógico</b>. 
- [ ] Tem <b>descrições</b> que podem ser <b>facilmente compreendidas</b>. 
- [ ] Tem a <b>semântica correta</b>. 
- [ ] É <b>objetivo</b> nos <b>rótulos</b>. 

## Texto
- [ ] <b>Evitar</b> o uso de <b>textos dentro de imagens</b>. 
- [ ] <b>Redimensiona os textos na página</b>, aumentando o zoom em até 200%. 
- [ ] <b>Alturas </b> das fontes <b> não é fixa </b>. 

## Teclado
- [ ] <b> Funcionalidades </b> da página web estão <b> disponíveis por teclado </b>. 
- [ ] Quando se tem o <b>mouseover é permitido o uso de teclado </b>. 
- [ ] <b>Foco visível</b> remova elementos focalizáveis invisíveis. 
- [ ] Adicione o <b> ``` .hover, .focus { } ```</b>  para tornar o foco visível. 
- [ ] Permite/visa o uso de <b> Atalhos de teclado </b> como o ```TAB```. 
- [ ] <b> Primeiro </b> item interativo da página é um link para o <b> conteúdo principal </b>. 

## Título
- [ ] A <b>hierarquia</b> de conteúdo da página é definida por sua <b>lógica</b> não pelo tamanaho do texto. <a id="TEC17" href="#RP17">[17]</a>
- [ ] Use <b>elementos de título  ``` h1 h2 h3 ```</b> para apresentar o conteúdo.<a id="TEC17" href="#RP17">[17]</a>
- [ ] <b>Não pular níveis lógicos</b>.
- [ ] <b>Toda página contem um título  ``` h1 ```</b> descrevendo a página. <a id="TEC17" href="#RP17">[17]</a></b><a id="TEC19" href="#RP19">[19]</a>

## Tabela
- [ ] <b> Use o ``` table ``` </b> para elementos em formato de tabela.  <a id="TEC4" href="#RP4">[4]</a>
- [ ] Insira cabeçalhos para explicar os dados, <b>use ``` th ``` com  ``` scope ``` correto</b>.<a id="TEC15" href="#RP15">[15]</a>
- [ ] <b> Use o ```caption``` </b> elemento para fornecer um título para a tabela.<a id="TEC17" href="#RP17">[17]</a>
- [ ] <b> Toda tabela complexa,</b> possui uma descrição em texto.<b>  NBR 5.6.6 </b>

## Modais
- [ ] Deve ser <b> fácil fechar </b>.<a id="TEC19" href="#RP19">[19]</a>
- [ ] Permite o <b> uso da tecla escape ``` ESC ```</b>.</b><a id="TEC19" href="#RP19">[19]</a>
- [ ] A interação é  uma <b> tarefa simples</b>.</b><a id="TEC19" href="#RP19">[19]</a>
- [ ] <b> Evita </b> modais em <b> tela cheia </b>.</b><a id="TEC19" href="#RP19">[19]</a>
- [ ] <b> Não abrir um modal a partir de outro modal </b>.</b><a id="TEC19" href="#RP19">[19]</a>

## Dispositivo Móvel e tocável
- [ ] O site pode ser <b> rotacionado </b> para qualquer orientação.  <a id="TEC15" href="#RP15">[15]</a>
- [ ] <b> Impedir </b> rolgem horizontal. <a id="TEC16" href="#RP15">[16]</a>
- [ ] <b> Garantir </b> que botões e links possam ser ativados facilmente. <a id="TEC18" href="#RP18">[18]</a>
- [ ] <b> Garantir </b> espaço suficiente entre elementos interativos. <a id="TEC7" href="#RP7">[7]</a>

## Ferramentas e extras
- [ ] Permite <b> pausar, parar ou ocultar conteúdo em movimento </b>.
- [ ] Usar <b> Breadcrumbs </b> informando a localização atual nas páginas.
- [ ] Colocar página ou <b> área de esclarecimento de dúvidas e dicas de acessibilidade </b>.
- [ ] Áreas clicáveis com no mínimo <b> 44px (pixels) de altura e 44px de largura </b>.
- [ ] No caso de <b>captcha</b> garanta que seja simples de entender e tenha alternativas para pessoas com deficiência.
- [ ] Incluir um <b> campo de busca </b>.

<canvas id="graficoChecklist" style="max-width: 300px; margin: auto;"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  function contarCheckboxes() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const feitos = [...checkboxes].filter(cb => cb.checked).length;
    const pendentes = (checkboxes.length - 3) - feitos; // checkboxes.length esta retornando 3 num acima. fix pra depois!
    return [feitos, pendentes];
  }

  document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('graficoChecklist').getContext('2d');

    const [feitos, pendentes] = contarCheckboxes();

    const chart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Selecionados', 'Não Selecionados'],
        datasets: [{
          data: [feitos, pendentes],
          backgroundColor: ['#4cae4f', '#992a23']
        }]
      },
      options: {
        responsive: true,
        width: 300,
        height: 300,  
        plugins: {
          legend: {
            position: 'bottom'
          },
          title: {
            display: true,
            text: 'Contagem de Marcações'
          }
        }
      }
    });

    document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', () => {
        const [atualFeitos, atualPendentes] = contarCheckboxes();
        chart.data.datasets[0].data = [atualFeitos, atualPendentes];
        chart.update();
      });
    });
  });
</script>

## Referência Bibliográfica

> <a id="RP1" href="#TEC1">1.</a> WCAG 2.2 Understanding Docs. SC 1.1.1 Non-text Content (Level A) . Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html). Acesso em: 9 Mai. 2024.

> <a id="RP2" href="#TEC2">2.</a> WCAG 2.2 Understanding Docs. SC 1.2.2 Captions (Prerecorded) (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html). Acesso em: 9 Mai. 2024.

> <a id="RP3" href="#TEC3">3.</a> WCAG 2.2 Understanding Docs. SC 2.3.1 Three Flashes or Below Threshold (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html). Acesso em: 9 Mai. 2024.

> <a id="RP4" href="#TEC4">4.</a> WCAG 2.2 Understanding Docs. SC 1.3.1 Info and Relationships (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html). Acesso em: 9 Mai. 2024.

> <a id="RP5" href="#TEC5">5.</a> WCAG 2.2 Understanding Docs. SC 1.4.1 Use of Color (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). Acesso em: 9 Mai. 2024.

> <a id="RP6" href="#TEC6">6.</a> WCAG 2.2 Understanding Docs. SC 2.4.7 Focus Visible (Level AA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html). Acesso em: 9 Mai. 2024.

> <a id="RP7" href="#TEC7">7.</a> WCAG 2.2 Understanding Docs. SC 2.4.1 Bypass Blocks (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html). Acesso em: 9 Mai. 2024.

> <a id="RP8" href="#TEC8">8.</a> WCAG 2.2 Understanding Docs. G201 Giving users advanced warning when opening a new window. Disponível em: [https://www.w3.org/WAI/WCAG22/Techniques/general/G201](https://www.w3.org/WAI/WCAG22/Techniques/general/G201). Acesso em: 9 Mai. 2024.

> <a id="RP9" href="#TEC9">9.</a> WCAG 2.2 Understanding Docs. SC 3.2.2 On Input (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/on-input.html](https://www.w3.org/WAI/WCAG22/Understanding/on-input.html). Acesso em: 9 Mai. 2024.

> <a id="RP10" href="#TEC10">10.</a> WCAG 2.2 Understanding Docs. SC 1.3.5 Identify Input Purpose (Level AA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html). Acesso em: 9 Mai. 2024.

> <a id="RP11" href="#TEC11">11.</a> WCAG 2.2 Understanding Docs. SC 3.3.1 Error Identification (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html). Acesso em: 9 Mai. 2024.

> <a id="RP12" href="#TEC12">12.</a> WCAG 2.2 Understanding Docs. SC 1.4.2 Audio Control (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html](https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html). Acesso em: 9 Mai. 2024.

> <a id="RP13" href="#TEC13">13.</a> WCAG 2.2 Understanding Docs. SC 2.1.1 Keyboard (Level A). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html). Acesso em: 9 Mai. 2024.

> <a id="RP14" href="#TEC14">14.</a> WCAG 2.2 Understanding Docs. SC 1.3.4 Orientation (Level AA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/orientation.html](https://www.w3.org/WAI/WCAG22/Understanding/orientation.html). Acesso em: 9 Mai. 2024.

> <a id="RP15" href="#TEC15">15.</a> WCAG 2.2 Understanding Docs. SC 4.1.1 Orientation (Level). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/parsing.html](https://www.w3.org/WAI/WCAG22/Understanding/parsing.html). Acesso em: 9 Mai. 2024.

> <a id="RP16" href="#TEC16">16.</a> WCAG 2.2 Understanding Docs. SC 1.4.10 Reflow (Level AA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/reflow.html](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). Acesso em: 9 Mai. 2024.

> <a id="RP17" href="#TEC17">17.</a> WCAG 2.2 Understanding SC 2.4.6 Headings and Labels (Level AA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html). Acesso em: 9 Mai. 2024.

> <a id="RP18" href="#TEC18">18.</a> WCAG 2.2 Understanding Docs. SC 2.5.5 Target Size (Enhanced) (Level AAA). Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html). Acesso em: 9 Mai. 2024.

> <a id="RP19" href="#TEC19">19.</a> GUIA DE BOAS PRÁTICAS PARA ACESSIBILIDADE DIGITAL. Disponível em: [https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html](https://www.w3.org/WAI/WCAG22/Understandin/target-size-enhanced.html). Acesso em: 9 Mai. 2024.

## Bibliografia

> </a> DINIZ, V.; FERRAZ, R.; NASCIMENTO, C. M.; CREDIDIO, R. Guia de Boas Práticas para Acessibilidade Digital. Programa de Cooperação entre Reino Unido e Brasil em Acesso Digital, 2023. Disponível em: [https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/guiaboaspraaticasparaacessibilidadedigital.pdf](https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/guiaboaspraaticasparaacessibilidadedigital.pdf). Acesso em: 9 Mai. 2024.

> </a> ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS.** *ABNT NBR ISO/IEC 17225:2025 – Tecnologia da informação – Acessibilidade – Diretrizes para avaliação da acessibilidade de produtos e serviços de tecnologia da informação e comunicação (TIC).* Rio de Janeiro: ABNT, 2025. Acesso em: 24 Jun. 2025.