from django.forms import ModelForm
from app.models import Produto

# Create the form class.
class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['codigoProduto', 'produto', 'valor', 'validade', 'quantidade']
