function modoEscuro()
{
    link = document.head.getElementsByTagName('link')[0];
    console.log(link)
    if(link.href === "style.css")
    {
        link.setAttribute('href', 'styleDark.css');
    }
    else
    {
        link.setAttribute('href', 'style.css');
    }
}