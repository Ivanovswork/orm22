from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'Создать раздел'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # tags = models.ManyToManyField(Tag, related_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag")
    article = models.ForeignKey(Article, on_delete=models.CASCADE,  related_name="scopes")
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'связь'
        verbose_name_plural = 'Редактирование статьи'

    def __str__(self):
        return f'{self.tag} -> {self.article}'