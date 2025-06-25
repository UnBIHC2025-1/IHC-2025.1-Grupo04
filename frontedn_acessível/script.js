let tamanhoFonte = 1;

function ajustarFonte(acao) {
  if (acao === 'aumentar' && tamanhoFonte < 4) {
    tamanhoFonte += 0.1;
  } else if (acao === 'diminuir' && tamanhoFonte > 0.8) {
    tamanhoFonte -= 0.1;
  } else if (acao === 'padrao') {
    tamanhoFonte = 1;
  }
  document.body.style.fontSize = `${tamanhoFonte}rem`;
}
