export function modoEscuro()
{
    var body = document.body;
    if(body.getAttribute('class') === 'body-white-mode')
    {
        body.setAttribute('class', 'body-dark-mode');

        var inputButtons = [...document.querySelectorAll(".input-button-white-mode")]
        for(let i = 0; i < inputButtons.length; i++){
            inputButtons[i].setAttribute("class", "input-button-dark-mode")
        }

        var inputTexts = [...document.querySelectorAll(".input-text-white-mode")]
        for(let i = 0; i < inputTexts.length; i++){
            inputTexts[i].setAttribute("class", "input-text-dark-mode")
        }

        var inputDates = [...document.querySelectorAll(".input-date-white-mode")]
        for(let i = 0; i < inputDates.length; i++){
            inputDates[i].setAttribute("class", "input-date-dark-mode")
        }
    }
    else
    {
        body.setAttribute('class', 'body-white-mode');

        var inputButtons = [...document.querySelectorAll(".input-button-dark-mode")]
        for(let i = 0; i < inputButtons.length; i++){
            inputButtons[i].setAttribute("class", "input-button-white-mode")
        }

        var inputTexts = [...document.querySelectorAll(".input-text-dark-mode")]
        for(let i = 0; i < inputTexts.length; i++){
            inputTexts[i].setAttribute("class", "input-text-white-mode")
        }

        var inputDates = [...document.querySelectorAll(".input-date-dark-mode")]
        for(let i = 0; i < inputDates.length; i++){
            inputDates[i].setAttribute("class", "input-date-white-mode")
        }
    }
}