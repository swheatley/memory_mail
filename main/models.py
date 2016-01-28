from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from registration.signals import user_activated, user_registered
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if username != None:
            email = username

        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s %s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class profile(models.Model):
    name = models.CharField(max_length=1200)
    description = models.TextField(default='description default')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        return self.name


class userStripe(AbstractBaseUser):
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username


def stripeCallback(sender, request, user, **kwargs):
    user_stripe_account, created = userStripe.objects.get_or_create(user=user)
    if created:
        print 'created for %s' % (user.username)

    if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=user.email)
        user_stripe_account.stripe.id = new_stripe_id['id']
        user_stripe_account.save()


def profileCallback(sender, request, user, **kwargs):
    userProfile, is_created = profile.objects.get_or_create(user=user)
    if is_created:
        userProfile.name = user.username
        userProfile.save()


user_activated.connect(stripeCallback)
user_registered.connect(profileCallback)


