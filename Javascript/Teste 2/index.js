function modoEscuro()
{
    var body = document.body;
    if(body.getAttribute('class') === 'body-white-mode')
    {
        body.setAttribute('class', 'body-dark-mode');

        var inputButtons = document.getElementsByClassName('input-button-white-mode');
        for(let i = 0; i < inputButtons.length; i++)
        {
            inputButtons[i].setAttribute('class', 'input-button-dark-mode');
        }

        var inputText = document.getElementsByClassName('input-text-white-mode');
        for(let i = 0; i < inputText.length; i++)
        {
            inputText[i].setAttribute('class', 'input-text-dark-mode');
        }
    }
    else
    {
        body.setAttribute('class', 'body-white-mode');

        var inputButtons = document.getElementsByClassName('input-button-dark-mode');
        for(let i = 0; i < inputButtons.length; i++)
        {
            inputButtons[i].setAttribute('class', 'input-button-white-mode');
        }

        var inputText = document.getElementsByClassName('input-text-dark-mode');
        for(let i = 0; i < inputText.length; i++)
        {
            inputText[i].setAttribute('class', 'input-text-white-mode');
        }
    }
}