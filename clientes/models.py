from django.db import models


class Cliente(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=80
    )

    email = models.EmailField(
        'E-mail',
        unique=True
    )

    data_cadastro = models.DateTimeField(
        'Data de Cadastro',
        auto_now_add=True
    )

    pontos = models.PositiveIntegerField(
        'Pontos',
        default=0
    )

    avatar = models.URLField(
        'Avatar (URL)',
        blank=True,
        null=True
    )

    personagem_favorito = models.CharField(
        'Personagem Favorito',
        max_length=50,
        blank=True,
        null=True
    )  # NOVO

    def __str__(self):
        return self.nome