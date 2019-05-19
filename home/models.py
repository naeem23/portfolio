from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class TitleSubtitle(models.Model):
    about_title = models.CharField(max_length=25, default='about me', blank=True, null=True)
    about_sub_title = models.CharField(max_length=255, default='', blank=True, null=True)
    service_title = models.CharField(max_length=25, default='services', blank=True, null=True)
    service_sub_title = models.CharField(max_length=255, default='', blank=True, null=True)
    portfolio_title = models.CharField(max_length=25, default='portfolio', blank=True, null=True)
    portfolio_sub_title = models.CharField(max_length=255, default='', blank=True, null=True)
    feedback_title = models.CharField(max_length=25, default='feedback', blank=True, null=True)
    feedback_sub_title = models.CharField(max_length=255, default='', blank=True, null=True)
    contact_title = models.CharField(max_length=25, default='contact me', blank=True, null=True)
    contact_sub_title = models.CharField(max_length=255, default='', blank=True, null=True)

class Home(models.Model):
    brand_name = models.CharField(max_length=25, default='', blank=True, null=True)
    up_heading = models.CharField(max_length= 255, default='', blank=True, null=True)
    down_heading = models.CharField(max_length= 255, default='', blank=True, null=True)
    button_text = models.CharField(max_length=255, default='Know More', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'home'

    def __str__(self):
        return self.brand_name

class About(models.Model):
    about = models.TextField(default='', blank=True, null=True)
    cv = models.FileField(upload_to='About/', default='About/NID-card.pdf', blank=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str(self):
        return self.cv

class Skill(models.Model):
    skills = models.CharField(max_length=25, default='', blank=True, null=True)

    def __str__(self):
        return self.skills

class Service(models.Model):
    s_icon = models.ImageField(upload_to = 'ServiceIcon/', default='ServiceIcon/settings.png', blank=True)
    s_title = models.CharField(max_length=255, default='', blank=True, null=True)
    s_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.s_title

class Project(models.Model):
    project_name = models.CharField(max_length=50, default='Threads', blank=True, null=True)
    category = models.CharField(max_length=50, default='Illustration', blank=True, null=True)
    thumb_1 = models.ImageField(upload_to = 'Portfolio/%Y/%m/%d', blank=True)
    thumb_2 = models.ImageField(upload_to = 'Portfolio/%Y/%m/%d', blank=True)
    project_info = models.TextField(blank=True, null=True)
    clients = models.CharField(max_length=50, default='Brand & Co.', blank=True, null='True')
    tools = models.CharField(max_length=255, blank=True, null=True)
    live_url = models.URLField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=50, default='', blank=True, null=True)

    def __str__(self):
        return self.project_name

    def _get_unique_slug(self):
        slug = slugify(self.project_name)
        unique_slug = slug
        num = 1
        while Project.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class Feedback(models.Model):
    photo = models.ImageField(upload_to="Feedback/%Y/%m/%d", blank=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=255)


class FollowMe(models.Model):
    facebook_id = models.CharField(max_length=50, default='', blank=True, null=True)
    facebook_url = models.URLField(max_length=255, default='https://www.facebook.com/', blank=True, null=True)
    twitter_id = models.CharField(max_length=50, default='', blank=True, null=True)
    twitter_url = models.URLField(max_length=255, default='https://www.twitter.com/', blank=True, null=True)
    linkedin_id = models.CharField(max_length=50, default='', blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, default='https://www.linkedin.com/', blank=True, null=True)
    google_plus_id = models.CharField(max_length=50, default='', blank=True, null=True)
    google_plus_url = models.URLField(max_length=255, default='https://plus.google.com/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Follow Me'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.subject
