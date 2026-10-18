# Importa o módulo de templates do Django
from django import template

# Cria uma instância de biblioteca de filtros para registrar novos filtros
register = template.Library()


# Define um novo filtro chamado 'get_item' que será usado nos templates
@register.filter
def get_item(obj, key):
    # Se o objeto for um dicionário, tenta retornar o valor associado à chave
    if isinstance(obj, dict):
        return obj.get(key)

    # Caso contrário, tenta acessar como um atributo do objeto
    # (por exemplo: obj.strIngredient1)
    try:
        return getattr(obj, key)

    # Se ocorrer qualquer erro (atributo não encontrado, por exemplo),
    # retorna None
    except Exception:
        return None