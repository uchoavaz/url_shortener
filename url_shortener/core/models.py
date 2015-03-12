from django.db import models

class Url(models.Model):

	original_url = models.TextField('Url')
	short_url = models.TextField('Url encurtado')
	is_protected = models.BooleanField('Protegido ?', default = False)
	url_password = models.CharField('Senha', blank =True, max_length=20)
	email = models.EmailField('E-mail')
	slug = models.SlugField('Atalho')


	def __str__(self):
		return self.original_url


	@models.permalink
	def get_absolute_url(self):
		return ('core:details',(), {'slug':self.slug})

	class Meta:
		verbose_name = 'Url'
		verbose_name_plural = 'Urls'
		ordering = ['original_url']

