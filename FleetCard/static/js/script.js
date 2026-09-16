    const campoImagem = document.getElementById('{{ form.imagem.id_for_label }}');
    const preview = document.getElementById('imagem-preview');

    campoImagem.addEventListener('change', function () {

        const arquivo = this.files[0];

        if (arquivo) {

            preview.src = URL.createObjectURL(arquivo);
            preview.style.display = 'block';

        } else {

            preview.src = '';
            preview.style.display = 'none';

        }

    });


  document.addEventListener('DOMContentLoaded', function () {
        const input = document.getElementById('vehicleSearch');
        const precoMinimo = document.getElementById('precoMinimo');
        const precoMaximo = document.getElementById('precoMaximo');
        const anoMinimo = document.getElementById('anoMinimo');
        const anoMaximo = document.getElementById('anoMaximo');
        const limparFiltros = document.getElementById('limparFiltros');

        const result = document.getElementById('searchResult');
        const noResults = document.getElementById('noSearchResults');
        const sections = document.querySelectorAll('[data-vehicle-section]');
        const items = document.querySelectorAll('[data-vehicle-item]');

        function normalize(text) {
            return text
                .toLocaleLowerCase('pt-BR')
                .normalize('NFD')
                .replace(/[\u0300-\u036f]/g, '');
        }

        function numberValue(value) {
            if (value === '' || value === null || value === undefined) {
                return null;
            }

            const number = Number(value);
            return Number.isNaN(number) ? null : number;
        }

        function filterVehicles() {
            const query = normalize(input.value.trim());

            const precoMin = numberValue(precoMinimo.value);
            const precoMax = numberValue(precoMaximo.value);
            const anoMin = numberValue(anoMinimo.value);
            const anoMax = numberValue(anoMaximo.value);

            let visibleCount = 0;

            items.forEach(function (item) {
                const card = item.querySelector('[data-search-text]');

                const searchText = normalize(
                    card.dataset.searchText || ''
                );

                const preco = numberValue(card.dataset.price);
                const ano = numberValue(card.dataset.year);

                const matchesText =
                    !query || searchText.includes(query);

                const matchesPrecoMin =
                    precoMin === null ||
                    (preco !== null && preco >= precoMin);

                const matchesPrecoMax =
                    precoMax === null ||
                    (preco !== null && preco <= precoMax);

                const matchesAnoMin =
                    anoMin === null ||
                    (ano !== null && ano >= anoMin);

                const matchesAnoMax =
                    anoMax === null ||
                    (ano !== null && ano <= anoMax);

                const matches =
                    matchesText &&
                    matchesPrecoMin &&
                    matchesPrecoMax &&
                    matchesAnoMin &&
                    matchesAnoMax;

                item.classList.toggle('d-none', !matches);

                if (matches) {
                    visibleCount++;
                }
            });

            sections.forEach(function (section) {
                const hasVisibleVehicle = section.querySelector(
                    '[data-vehicle-item]:not(.d-none)'
                );

                section.classList.toggle(
                    'd-none',
                    !hasVisibleVehicle
                );
            });

            const hasAnyFilter =
                query ||
                precoMin !== null ||
                precoMax !== null ||
                anoMin !== null ||
                anoMax !== null;

            noResults.classList.toggle(
                'd-none',
                !hasAnyFilter || visibleCount > 0
            );

            result.textContent = hasAnyFilter
                ? `${visibleCount} veículo(s) encontrado(s)`
                : '';
        }

        [
            input,
            precoMinimo,
            precoMaximo,
            anoMinimo,
            anoMaximo
        ].forEach(function (element) {
            element.addEventListener('input', filterVehicles);
        });

        limparFiltros.addEventListener('click', function () {
            input.value = '';
            precoMinimo.value = '';
            precoMaximo.value = '';
            anoMinimo.value = '';
            anoMaximo.value = '';

            filterVehicles();
        });
    });