import datetime

from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_all_styles, monokai

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)


def save(self, *args, **kwargs):
    lexer = get_lexer_by_name(monokai, stripall=True)
    options = {}
    if self.linenos:
        options['linenos'] = LINENOS_TABLE = 'table'
    if self.title:
        options['title'] = self.title
    formatter = HtmlFormatter(style=monokai, full=True, **options)


class List(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass


PRIORITY_CHOICES = (
    (1, 'Low'),
    (2, 'Normal'),
    (3, 'High'),
)


class Item(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(List, on_delete=models)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']

    class Admin:
        pass
