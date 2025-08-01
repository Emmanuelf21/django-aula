from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cooking_time = models.IntegerField(help_text="Em minutos")
    ingredients = models.TextField()
    instructions = models.TextField()
    #faz o upload da imagem na MEDIA_ROOT/recipes
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        # Define o nome da tabela no plural para o painel de administração
        verbose_name_plural="Recipes"