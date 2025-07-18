# Geração de conteúdo

"Para produzir conteúdo digital acessível, a primeira etapa é compreender que tudo o que comunicamos impacta as pessoas; por isso, é fundamental começar pela forma como abordamos nosso público e criar a cultura e o hábito de acessibilidade digital em nossas equipes". Nesse sentido, nesta seção se apresentam boas práticas em formato de checklist para garantir acessibilidade na geração de conteúdo.

## Termos
- [ ] Sempre utilize o termo "pessoas com deficiência" (PCD) e depois complemente: visual, física, intelectual, múltipla, pessoa  surda, pessoa cega, usuária de cadeira de rodas (cadeirante), tetraplégica, paraplégica, pessoa com nanismo, com baixa visão, pessoa autista, disléxica, neurodiversa ou neurodivergente.  

## Textos
- [ ] Usar textos descomplicados e objetivos. 
- [ ] Usar de palavras conhecidas. 
- [ ] Evitar figuras de linguagem. e frases com "senso de ugência" 
- [ ] Usar pontuação adequada. 
- [ ] Evitar frases extensas (ideal é ter de 15 a 20 palavras). 
- [ ] Usar preferencialmente a ordem direta nas orações. 

## Descrição de imagens
- [ ] Identificar o tipo de imagem e personagem (foto, ilustração, mapa, gráfico... e " o que / quem"). 
- [ ] Localizar (onde). 
- [ ] Descrever a ação (o que faz, como faz). 
- [ ] Referenciar. 

## Descrição de imagens complexas
- [ ] Posicionar gráfico, quadrinhos, quadros e outras imagens compexas em um local separado. 
- [ ] Descrição sucinta no texto alternativo. 

## Ícones
- [ ] Adicionar iconografia. 
- [ ] Adicionar ícone e texto. 
- [ ] Adicionar texto alternativo para ícones clicáveis. 
- [ ] Descrever no texto alternativo, quando necessário usá-lo, a ação da pessoa usuária e para onde será direcionada. 

## Mídias de vídeo
- [ ] Adicionar descritivo curto para vídeos. 
- [ ] Optar pro legendas: Open Caption e Closed Caption para vídeos. 

## Autodescrição
- [ ] Adionar autodescrição no roteiro dos vídeos 

# Podcasts
- [ ] Transcrever o conteúdo do episódio. 
- [ ] Incluir além da partes faladas, como sons de fundos, efeitos sonoros, quem está falando etc. 
- [ ] Inserir um avatar na página falada para a interpretção do texto transcrito para Libras. 
- [ ] Considerar também formato de vídeo.

## Hashtags e Emojis
- [ ] Em hashtags, utilize a primeira letra de cada palavra em maiúsculas para que leitores possam identificar palavras corretamente. 
- [ ] Não abusar de emojis, pois nem sempre sua descrição é suficiente para um bom entendimento. 

## Hiperlinks
- [ ] Descrição de links e botões devem ser compreensíveis de maneira maneira isolada. 

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

## Bibliografia

> <a id="RP1" href="#TEC1"></a> DINIZ, V.; FERRAZ, R.; NASCIMENTO, C. M.; CREDIDIO, R. Guia de Boas Práticas para Acessibilidade Digital. Programa de Cooperação entre Reino Unido e Brasil em Acesso Digital, 2023. Disponível em: [https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/guiaboaspraaticasparaacessibilidadedigital.pdf](https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/guiaboaspraaticasparaacessibilidadedigital.pdf). Acesso em: 9 Mai. 2024.

> </a> ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS.** *ABNT NBR ISO/IEC 17225:2025 – Tecnologia da informação – Acessibilidade – Diretrizes para avaliação da acessibilidade de produtos e serviços de tecnologia da informação e comunicação (TIC).* Rio de Janeiro: ABNT, 2025. Acesso em: 24 Jun. 2025.