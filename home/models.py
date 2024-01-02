from django.db import models
from django.template.defaultfilters import slugify  # new
from django.urls import reverse
from accounts.models import User


class FirstLevelCategory(models.Model):
    MEDICAL = 'MD'
    HOSPITAL = 'HOS'
    DENTAL = 'DEN'
    LABORATORY = 'LAB'
    FIRST_LEVEL_CHOICES = [
        (MEDICAL, 'Medical'),
        (HOSPITAL, 'Hospital'),
        (DENTAL, 'Dental'),
        (LABORATORY, 'Laboratory'),
    ]

    first_level = models.CharField(choices=FIRST_LEVEL_CHOICES, max_length=10, default=MEDICAL)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        ordering = ('first_level',)
        verbose_name = 'first level category'
        verbose_name_plural = 'first level categories'

    def __str__(self):
        return self.first_level

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug])


class SecondLevelCategory(models.Model):
    second_level_name = models.CharField(blank=True, max_length=300)
    second_sub_category = models.ForeignKey(FirstLevelCategory, on_delete=models.CASCADE,
                                            related_name='sscategory',
                                            null=True,
                                            blank=True, )

    class Meta:
        ordering = ('second_level_name','second_sub_category')
        verbose_name = 'second level category'
        verbose_name_plural = 'second level categories'

    def __str__(self):
        return f'{self.second_sub_category} / {self.second_level_name}'


class Device(models.Model):
    status = [
        ('p', 'published'),
        ('d', 'draft'),
        ('w', 'Withdrawn'),


    ]

    first_level_category = models.ForeignKey(FirstLevelCategory, on_delete=models.CASCADE, related_name='dfcategory',
                                             blank=False,
                                             null=True)
    second_level_category = models.ForeignKey(SecondLevelCategory, on_delete=models.CASCADE, related_name='dscategory',
                                              blank=False,
                                              null=True)
    name = models.CharField(max_length=100)
    display_status = models.CharField(choices=status, max_length=1, default='d')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DUser', null=True, blank=True)
    UMDNS = models.PositiveIntegerField(blank=True, null=True)
    risk_class = models.CharField(max_length=10, blank=True)
    modality = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    history = models.TextField(blank=True)
    slug = models.SlugField(max_length=15, unique=True)

    class Meta:
        ordering = ('first_level_category', 'second_level_category', 'name')
        get_latest_by = 'created'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:device_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Device, self).save(*args, **kwargs)
