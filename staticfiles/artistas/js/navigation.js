$(document).ready(function(){
    // Inicializa o ponto indicador na posição do item ativo
    var activeOffset = $('nav ul .active').position().left;
    var activeItemWidth = $('nav ul .active').width();
    
    $('.dot').css('left', activeOffset + activeItemWidth / 2);
    var bgColor = $('.active a').css("background-color");
    $('.dot').css('background-color', bgColor);
});

// Quando o mouse sai do menu, retorna o ponto para o item ativo
$('nav').mouseout(function(){
    var activeOffset = $('nav ul .active').position().left;
    var activeItemWidth = $('nav ul .active').width();
    $('.dot').css('left', activeOffset + activeItemWidth / 2);
    var bgColor = $('.active a').css("background-color");
    $('.dot').css('background-color', bgColor);
});

// Quando o mouse passa sobre um item do menu
$('nav ul li').hover(function(){
    var navOffset = $(this).position().left;
    var navItemWidth = $(this).width();
    
    $('.dot').css('left', navOffset + navItemWidth / 2);
    
    var bgColor = $('a', this).css("background-color");
    
    $('.dot').css('background-color', bgColor);
}); 