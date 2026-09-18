javascript
/**
 * FLEETCARD
 * JavaScript otimizado
 *
 * Objetivos:
 * - reduzir processamento desnecessário
 * - evitar múltiplos listeners
 * - pesquisa mais rápida
 * - carregamento inteligente de imagens
 * - melhorar responsividade
 * - funcionar com Bootstrap 5
 */

"use strict";

/* =========================================================
   1. INICIALIZAÇÃO
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    iniciarPesquisa();
    iniciarFiltros();
    iniciarMenu();
    iniciarImagensLazy();
    iniciarFormularios();
    iniciarBotoes();
    iniciarCarousel();

});


/* =========================================================
   2. PESQUISA DE VEÍCULOS
   ========================================================= */

function iniciarPesquisa() {

    const campoPesquisa = document.querySelector(
        "[data-pesquisa], #pesquisa, #search, #buscar"
    );

    if (!campoPesquisa) return;

    let timeout;

    campoPesquisa.addEventListener("input", () => {

        clearTimeout(timeout);

        timeout = setTimeout(() => {

            const termo = normalizarTexto(campoPesquisa.value);

            filtrarVeiculos(termo);

        }, 150);

    });

}


/* =========================================================
   3. FILTRO DE VEÍCULOS
   ========================================================= */

function iniciarFiltros() {

    const filtros = document.querySelectorAll(
        "[data-filtro], .filtro-veiculo"
    );

    if (!filtros.length) return;

    filtros.forEach(filtro => {

        filtro.addEventListener("change", aplicarFiltros);

    });

}


function aplicarFiltros() {

    const pesquisa = document.querySelector(
        "[data-pesquisa], #pesquisa, #search, #buscar"
    );

    const termo = pesquisa
        ? normalizarTexto(pesquisa.value)
        : "";

    filtrarVeiculos(termo);

}


function filtrarVeiculos(termo) {

    const veiculos = document.querySelectorAll(
        "[data-veiculo], .card-veiculo, .vehicle-card"
    );

    if (!veiculos.length) return;

    let encontrados = 0;

    veiculos.forEach(veiculo => {

        const texto = normalizarTexto(
            veiculo.textContent
        );

        const encontrado =
            termo === "" ||
            texto.includes(termo);

        veiculo.hidden = !encontrado;

        if (encontrado) {
            encontrados++;
        }

    });

    atualizarContador(encontrados);

}


/* =========================================================
   4. CONTADOR DE RESULTADOS
   ========================================================= */

function atualizarContador(total) {

    const contador = document.querySelector(
        "[data-contador-resultados]"
    );

    if (!contador) return;

    contador.textContent =
        `${total} veículo${total === 1 ? "" : "s"} encontrado${total === 1 ? "" : "s"}`;

}


/* =========================================================
   5. NORMALIZAÇÃO DE TEXTO
   ========================================================= */

function normalizarTexto(texto) {

    return texto
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .trim();

}


/* =========================================================
   6. MENU LATERAL
   ========================================================= */

function iniciarMenu() {

    const menu = document.querySelector(
        "#sidebar, .sidebar, [data-sidebar]"
    );

    const botao = document.querySelector(
        "#menu-toggle, [data-menu-toggle]"
    );

    if (!menu || !botao) return;

    botao.addEventListener("click", () => {

        menu.classList.toggle("active");

    });

}


/* =========================================================
   7. LAZY LOADING DE IMAGENS
   ========================================================= */

function iniciarImagensLazy() {

    const imagens = document.querySelectorAll(
        "img[data-src]"
    );

    if (!imagens.length) return;


    /*
     * Navegadores modernos suportam IntersectionObserver.
     */

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            (entradas, obs) => {

                entradas.forEach(entrada => {

                    if (!entrada.isIntersecting) return;

                    const imagem = entrada.target;

                    imagem.src = imagem.dataset.src;

                    imagem.removeAttribute("data-src");

                    obs.unobserve(imagem);

                });

            },
            {
                rootMargin: "200px"
            }
        );


        imagens.forEach(imagem => {

            observer.observe(imagem);

        });

        return;
    }


    /*
     * Fallback para navegadores antigos.
     */

    imagens.forEach(imagem => {

        imagem.src = imagem.dataset.src;

        imagem.removeAttribute("data-src");

    });

}


/* =========================================================
   8. FORMULÁRIOS
   ========================================================= */

function iniciarFormularios() {

    const formularios = document.querySelectorAll(
        "form"
    );

    if (!formularios.length) return;

    formularios.forEach(formulario => {

        formulario.addEventListener("submit", () => {

            const botao = formulario.querySelector(
                'button[type="submit"], input[type="submit"]'
            );

            if (!botao) return;

            /*
             * Evita múltiplos envios acidentais.
             */

            botao.disabled = true;

            const textoOriginal =
                botao.innerHTML;

            botao.dataset.textoOriginal =
                textoOriginal;

            botao.innerHTML =
                "Processando...";


            /*
             * Caso o navegador impeça o envio,
             * o botão volta ao estado original.
             */

            setTimeout(() => {

                if (document.visibilityState === "visible") {

                    botao.disabled = false;

                    botao.innerHTML =
                        botao.dataset.textoOriginal;

                }

            }, 5000);

        });

    });

}


/* =========================================================
   9. BOTÕES DE CONFIRMAÇÃO
   ========================================================= */

function iniciarBotoes() {

    const botoesExcluir = document.querySelectorAll(
        "[data-confirmar-exclusao]"
    );

    botoesExcluir.forEach(botao => {

        botao.addEventListener("click", evento => {

            const confirmar = window.confirm(
                "Tem certeza que deseja excluir este veículo?"
            );

            if (!confirmar) {

                evento.preventDefault();

            }

        });

    });

}


/* =========================================================
   10. CAROUSEL
   ========================================================= */

function iniciarCarousel() {

    /*
     * O Bootstrap já controla o carousel.
     *
     * Portanto NÃO criamos outro sistema
     * de carousel em JavaScript.
     */

    const carousels = document.querySelectorAll(
        ".carousel"
    );

    if (!carousels.length) return;


    /*
     * Apenas adiciona carregamento preguiçoso
     * nas imagens do carousel.
     */

    carousels.forEach(carousel => {

        const imagens = carousel.querySelectorAll(
            "img[data-src]"
        );

        imagens.forEach(imagem => {

            imagem.loading = "lazy";

        });

    });

}


/* =========================================================
   11. FECHAR MENU AO CLICAR EM LINK
   ========================================================= */

document.addEventListener("click", evento => {

    const link = evento.target.closest(
        ".sidebar a"
    );

    if (!link) return;

    const menu = document.querySelector(
        "#sidebar, .sidebar, [data-sidebar]"
    );

    if (!menu) return;

    menu.classList.remove("active");

});


/* =========================================================
   12. ESC PARA FECHAR MENU
   ========================================================= */

document.addEventListener("keydown", evento => {

    if (evento.key !== "Escape") return;

    const menu = document.querySelector(
        "#sidebar, .sidebar, [data-sidebar]"
    );

    if (!menu) return;

    menu.classList.remove("active");

});


document.addEventListener("DOMContentLoaded", function () {

    const imagemInput = document.querySelector('input[type="file"]');
    const previewContainer = document.getElementById("preview-container");
    const imagemPreview = document.getElementById("imagem-preview");

    if (!imagemInput || !previewContainer || !imagemPreview) {
        return;
    }

    imagemInput.addEventListener("change", function () {

        const arquivo = imagemInput.files[0];

        if (arquivo) {

            const leitor = new FileReader();

            leitor.onload = function (evento) {

                imagemPreview.src = evento.target.result;

                previewContainer.classList.remove("d-none");

            };

            leitor.readAsDataURL(arquivo);

        } else {

            imagemPreview.src = "";

            previewContainer.classList.add("d-none");

        }

    });

});
