from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Vitrine(models.Model):

    categoria = (
        ("Informatica", "Informática"),
        ("Celulares", "Celulares"),
        ("Moda", "Moda")
    )

    estado = (
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'),
        ('PR', 'Paraná'), ('PE', 'Pernambuco'),
        ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
        ('SE', 'Sergipe'), ('TO', 'Tocantis')
    )

    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    foto = models.ImageField(blank=True, default='vitrine.png', upload_to='vitrines')
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=estado, default='')
    categoria = models.CharField(max_length=20, choices=categoria)
    descricao = models.TextField(default='', blank=True)
    acessos = models.BigIntegerField(default=0)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    vitrine = models.ForeignKey('blog.Vitrine', on_delete=models.CASCADE)
    media_nota = models.PositiveSmallIntegerField(default=0)
    somaTotal_nota = models.PositiveSmallIntegerField(default=0)
    quantidade = models.BigIntegerField(default=0)

    def __str__(self):
        return 'avaliação da vitrine: {}'.format(self.vitrine.nome)

class Produto(models.Model):

    categoria = (
        ("Informatica", "Informática"),
        ("Celulares", "Celulares"),
        ("Moda", "Moda")
    )

    proprietario = models.ForeignKey('blog.Vitrine', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    foto = models.ImageField(blank=True, default='produto.jpeg', upload_to='produtos')
    categoria = models.CharField(max_length=20, choices=categoria)
    descricao = models.TextField(default='', null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField(default=0)
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome

class Perfil(models.Model):

    estado = (
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'),
        ('PR', 'Paraná'), ('PE', 'Pernambuco'),
        ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'), ('RS', 'Rio grande do Sul'),
        ('RO', 'Rondônia'), ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
        ('SE', 'Sergipe'), ('TO', 'Tocantis')
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True, default='user.png', upload_to='perfis')
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=estado)
    bairro = models.CharField(max_length=200, default='')
    rua = models.CharField(max_length=200, default='')
    cep = models.PositiveIntegerField(default=0)
    numero = models.PositiveIntegerField(default=0)
    ponto_referencia = models.TextField(default='')

class Encomenda(models.Model):

    vendedor = models.ForeignKey('blog.Vitrine', on_delete=models.CASCADE)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey('blog.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveSmallIntegerField()
    data_pedido = models.DateField()
    data_entrega = models.DateField()
    comentario = models.TextField(default='')

    def __str__(self):
        return 'encomenda do cliente: {}, com os produtos: {}, da vitrine {}'.format(self.cliente,self.produto.nome, self.vendedor.nome)
