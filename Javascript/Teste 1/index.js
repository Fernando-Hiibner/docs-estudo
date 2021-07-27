
function criarMensagem()
{
    if(document.getElementById('askBox')) return;
    if(document.getElementById('msgBox')){
        let msgBox = document.getElementById('msgBox');
        msgBox.parentNode.removeChild(msgBox);
    }

    let html = document.querySelector('body');
    let panel = document.createElement('div');

    panel.setAttribute('class', 'askBox');
    panel.setAttribute('id', 'askBox');
    html.appendChild(panel);

    let msg = document.createElement('textarea');
    panel.appendChild(msg);

    let createMessage = document.createElement('button');
    createMessage.textContent = "Criar mensagem";

    createMessage.onclick = function() {
        let mensagem = msg.value;
        panel.parentNode.removeChild(panel);
        mostrarMensagem(mensagem, 'message');
    }
    panel.appendChild(createMessage);

    let createWarning = document.createElement('button');
    createWarning.textContent = "Criar aviso";

    createWarning.onclick = function() {
        let mensagem = msg.value;
        panel.parentNode.removeChild(panel);
        mostrarMensagem(mensagem, 'warning');
    }
    panel.appendChild(createWarning);
}
function mostrarMensagem(msgText, msgType)
{
    if(document.getElementById('msgBox')) return;

    let html = document.querySelector('body');
    let panel = document.createElement('div');

    panel.setAttribute('class', 'msgBox');
    panel.setAttribute('id', 'msgBox');
    html.appendChild(panel);

    let msg = document.createElement('p');
    msg.textContent = msgText;
    panel.appendChild(msg);

    if(msgType === 'warning'){
        msg.style.color = 'red';
    }

    let closeButton = document.createElement('button');
    closeButton.textContent = "Não!";

    closeButton.onclick = function () {
        panel.parentNode.removeChild(panel);
    }
    panel.appendChild(closeButton);
}