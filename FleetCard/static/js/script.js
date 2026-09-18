document.addEventListener("DOMContentLoaded", function () {

    const imagemInput = document.querySelector('input[type="file"]');
    const previewContainer = document.getElementById("preview-container");
    const imagemPreview = document.getElementById("imagem-preview");

    // Se a página não tiver campo de imagem, não faz nada
    if (!imagemInput || !previewContainer || !imagemPreview) {
        return;
    }

    imagemInput.addEventListener("change", function () {

        const arquivo = this.files[0];

        if (!arquivo) {
            previewContainer.classList.add("d-none");
            imagemPreview.src = "";
            return;
        }

        const leitor = new FileReader();

        leitor.onload = function (evento) {

            imagemPreview.src = evento.target.result;

            previewContainer.classList.remove("d-none");

        };

        leitor.readAsDataURL(arquivo);

    });

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