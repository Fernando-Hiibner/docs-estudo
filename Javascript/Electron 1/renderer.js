const NOTIFICATION_TITLE = "BAOZI!";
const NOTIFICATION_BODY = "Baozi grande e obeso, clique para logar isso no console.";
const CLICK_MESSAGE = "Baozi LOGADO!";

var ColorClass = Quill.import('attributors/class/color');
var SizeStyle = Quill.import('attributors/style/size');
Quill.register(ColorClass, true);
Quill.register(SizeStyle, true);

var toolbarOptions = [
    ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
    ['blockquote', 'code-block'],
  
    [{ 'header': 1 }, { 'header': 2 }],               // custom button values
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
    [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
    [{ 'direction': 'rtl' }],                         // text direction
  
    [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
    [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
  
    [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
    [{ 'font': [] }],
    [{ 'align': [] }],
  
    ['clean']                                         // remove formatting button
  ];

var quill = new Quill('#editor', {
    theme: 'snow',
    modules : {
        toolbar : toolbarOptions
    }
  });


new Notification(NOTIFICATION_TITLE, {body : NOTIFICATION_BODY}).onclick = () => console.log(CLICK_MESSAGE);

function write(event) {
    if(event.key.length === 1){
        document.getElementById("Editor").innerText += event.key;
        console.log(`You pressed ${event.key}`)
    }
    if(event.key === 'Backspace'){
        document.getElementById("Editor").innerText = document.getElementById("Editor").innerText.replace(/(\s+)?.$/, '');
    }
    if(event.key === 'Shift'){
        quill.format('color', 'red');
    }
    else{
        console.log(`You pressed ${event.key}`);
    }
}

window.addEventListener('keydown', write, true)

// Na moral melhorar isso, por hora essa foi a unica forma que eu achei de fazer
document.getElementById("dark-mode").onclick = () =>
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