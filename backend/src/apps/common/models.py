from django.db import models

# Base model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = "region"
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class SMSToken(BaseModel):
    name = models.CharField(max_length=50)
    token = models.TextField()
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SMS Token"
        verbose_name_plural = "SMS Tokens"
        ordering = ["-id"]


class SMSLog(BaseModel):
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "SMS Log"
        verbose_name_plural = "SMS Logs"
        ordering = ["-id"]
