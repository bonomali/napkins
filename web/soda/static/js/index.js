function setup()
{
    if(window.innerWidth < 768)
    {
        document.getElementsByTagName("header")[0].style.background = "#51cdf0";
        document.getElementsByTagName("header")[0].style.paddingTop = "0px";
        document.getElementsByTagName("header")[0].style.boxShadow = "1px 3px 10px #aaa";
    }
    else if(window.scrollY <= 2 * document.getElementsByClassName("navbar")[0].clientHeight)
    {
        document.getElementsByTagName("header")[0].style.background = "none";
        document.getElementsByTagName("header")[0].style.paddingTop = "10px";
        document.getElementsByTagName("header")[0].style.boxShadow = "none";
    }
    else
    {
        document.getElementsByTagName("header")[0].style.background = "#51cdf0";
        document.getElementsByTagName("header")[0].style.paddingTop = "0px";
        document.getElementsByTagName("header")[0].style.boxShadow = "1px 3px 10px #aaa";
    }
    document.getElementsByTagName("main")[0].style.top = Math.max((((document.body.clientHeight - 3 * document.getElementsByClassName("navbar")[0].clientHeight - document.getElementsByClassName("index-container")[0].clientHeight)) / 2), 40) + "px";
    document.body.style.minHeight = 3 * document.getElementsByClassName("navbar")[0].clientHeight + document.getElementsByClassName("index-container")[0].clientHeight + 35 + "px";
    try
    {
        document.getElementById("secondary").style.top = document.body.clientHeight + "px";
    }
    catch(e)
    {
    }
}

setup();
window.onresize = setup;
window.onscroll = setup;