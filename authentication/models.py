from django.db import models
from services.models import Usuario

class Token(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
	
    def save(self, *args, **kwargs):
	    if not self.token:
	        self.token = self.generate_token()
	        return super(Token, self).save(*args, **kwargs)

    def generate_token(self):
	    return binascii.hexlify(os.urandom(20)).decode()

    def __unicode__(self):
	    return self.token
