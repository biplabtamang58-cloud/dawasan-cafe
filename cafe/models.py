from django.db import models


class CafeInfo(models.Model):
    """Add just ONE of these in admin. It feeds the footer and contact page."""
    name = models.CharField(max_length=100, default="Dawasan Cafe")
    tagline = models.CharField(max_length=200, blank=True, default="Where every cup is an occasion.")
    about_text = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    opening_hours = models.CharField(max_length=100, blank=True, default="Open daily · 8:00 – 22:00")
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        verbose_name = "Cafe info"
        verbose_name_plural = "Cafe info"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first")

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    vegetarian = models.BooleanField(default=False)
    featured = models.BooleanField(default=False, help_text="Show on the home page")
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['category__order', 'name']

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Image {self.pk}"


class Reservation(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveSmallIntegerField(default=2)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.name} · {self.date} {self.time:%H:%M} · {self.guests} guests"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.name}: {self.subject or self.message[:30]}"