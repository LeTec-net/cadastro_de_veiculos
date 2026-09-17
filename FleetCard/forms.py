from django import forms

from .models import Veiculo


class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo

        fields = [
            'tipo',
            'marca',
            'modelo',
            'placa',
            'ano',
            'cor',
            'combustivel',
            'quilometragem',
            'observacoes',
            'imagem',
        ]