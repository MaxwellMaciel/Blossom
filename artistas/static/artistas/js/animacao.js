// Pré-carregar a página de álbuns para transição mais suave
if (window.location.pathname === '/' || window.location.pathname === '/index/' ) {
    // Pré-carrega a página de visão
    fetch('/visao/');

    const uriasImg = document.querySelector('.artista img');
    const overlay = document.getElementById('overlay-animacao');
    if (uriasImg) {
        uriasImg.addEventListener('click', function(e) {
            e.preventDefault();
            // Animação simultânea: imagem desce e overlay escurece
            gsap.to(uriasImg, {
                y: 300,
                duration: 0.8,
                ease: 'power2.in',
                onStart: function() {
                    if (overlay) {
                        gsap.to(overlay, { 
                            opacity: 0.7, 
                            duration: 0.8, 
                            ease: 'power2.in' 
                        });
                    }
                },
                onComplete: function() {
                    window.location.href = uriasImg.parentElement.getAttribute('href');
                }
            });
        });
    }
}

// Animação na página de álbuns
if (window.location.pathname.includes('albuns')) {
    window.addEventListener('DOMContentLoaded', function() {
        const albuns = document.querySelectorAll('.album');
        const overlay = document.getElementById('overlay-animacao');
        
        // Inicia com overlay escuro e álbuns invisíveis
        gsap.set(overlay, { opacity: 0.7 });
        gsap.set(albuns, { y: 100, opacity: 0 });
        
        // Anima os álbuns subindo e o overlay clareando
        gsap.to(albuns, {
            y: 0,
            opacity: 1,
            duration: 0.8,
            stagger: 0.15,
            ease: 'power2.out'
        });
        
        gsap.to(overlay, {
            opacity: 0,
            duration: 1.2,
            ease: 'power2.out',
            delay: 0.2
        });

        // Animação reversa ao clicar em voltar
        const backBtn = document.querySelector('.back-button');
        if (backBtn) {
            backBtn.addEventListener('click', function(e) {
                e.preventDefault();
                // Primeiro escurece o overlay
                gsap.to(overlay, {
                    opacity: 0.7,
                    duration: 0.4,
                    ease: 'power2.in'
                });
                
                // Depois anima os álbuns saindo
                gsap.to(albuns, {
                    y: 100,
                    opacity: 0,
                    duration: 0.6,
                    stagger: 0.1,
                    ease: 'power2.in',
                    onComplete: function() {
                        window.location.href = backBtn.getAttribute('href');
                    }
                });
            });
        }
    });
}

function animarUriasESair(callback) {
    const uriasImg = document.querySelector('.artista img');
    const overlay = document.getElementById('overlay-animacao');
    
    // Primeiro escurece o overlay
    gsap.to(overlay, {
        opacity: 0.7,
        duration: 0.8,
        ease: 'power2.in'
    });
    
    // Depois anima a URIAS descendo
    gsap.to(uriasImg, {
        y: 300,
        duration: 0.8,
        ease: 'power2.in',
        onComplete: callback
    });
}

function animarAlbunsEntrada() {
    const albuns = document.querySelectorAll('.album');
    const overlay = document.getElementById('overlay-animacao');
    
    // Inicia com overlay escuro e álbuns invisíveis
    gsap.set(overlay, { opacity: 0.7 });
    gsap.set(albuns, { y: 100, opacity: 0 });
    
    // Anima os álbuns subindo e o overlay clareando
    gsap.to(albuns, {
        y: 0,
        opacity: 1,
        duration: 0.8,
        stagger: 0.15,
        ease: 'power2.out'
    });
    
    gsap.to(overlay, {
        opacity: 0,
        duration: 1.2,
        ease: 'power2.out',
        delay: 0.2
    });
}

function animarAlbunsESair(callback) {
    const albuns = document.querySelectorAll('.album');
    const overlay = document.getElementById('overlay-animacao');
    
    // Primeiro escurece o overlay
    gsap.to(overlay, {
        opacity: 0.7,
        duration: 0.4,
        ease: 'power2.in'
    });
    
    // Depois anima os álbuns saindo
    gsap.to(albuns, {
        y: 100,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.in',
        onComplete: callback
    });
}

function carregarPaginaSPA(url, animacaoSaida, animacaoEntrada) {
    fetch(url, {headers: {'X-Requested-With': 'XMLHttpRequest'}})
        .then(resp => resp.text())
        .then(html => {
            const temp = document.createElement('div');
            temp.innerHTML = html;
            const novoConteudo = temp.querySelector('#spa-content');
            
            if (novoConteudo) {
                animacaoSaida(function() {
                    document.querySelector('#spa-content').innerHTML = novoConteudo.innerHTML;
                    window.history.pushState({}, '', url);
                    inicializarSPA();
                    animacaoEntrada();
                });
            }
        });
}

function inicializarSPA() {
    // Clique na URIAS
    const uriasLink = document.querySelector('.artista');
    if (uriasLink) {
        uriasLink.addEventListener('click', function(e) {
            e.preventDefault();
            carregarPaginaSPA('/visao/', animarUriasESair, animarAlbunsEntrada);
        });
    }
    
    // Clique no voltar
    const backBtn = document.querySelector('.back-button');
    if (backBtn) {
        backBtn.addEventListener('click', function(e) {
            e.preventDefault();
            carregarPaginaSPA('/', function(cb){
                animarAlbunsESair(cb);
            }, function(){
                // Resetar overlay e animação da URIAS
                const overlay = document.getElementById('overlay-animacao');
                if (overlay) gsap.to(overlay, { opacity: 0, duration: 0.5 });
                const uriasImg = document.querySelector('.artista img');
                if (uriasImg) gsap.set(uriasImg, {y: 0});
            });
        });
    }
}

// Suporte ao botão voltar/avançar do navegador
window.addEventListener('popstate', function() {
    const url = window.location.pathname;
    fetch(url, {headers: {'X-Requested-With': 'XMLHttpRequest'}})
        .then(resp => resp.text())
        .then(html => {
            const temp = document.createElement('div');
            temp.innerHTML = html;
            const novoConteudo = temp.querySelector('#spa-content');
            
            if (novoConteudo) {
                // Resetar todas as animações
                gsap.killTweensOf("*");
                
                // Atualizar conteúdo
                document.querySelector('#spa-content').innerHTML = novoConteudo.innerHTML;
                
                // Inicializar nova página
                inicializarSPA();
                
                // Animar entrada baseado na página
                if (url.includes('albuns')) {
                    animarAlbunsEntrada();
                }
            }
        });
});

document.addEventListener('DOMContentLoaded', function() {
    inicializarSPA();
    // Animação inicial dos álbuns se já estiver na página
    if (window.location.pathname.includes('albuns')) {
        animarAlbunsEntrada();
    }
}); 