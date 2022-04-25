from django.db import models


class Branch(models.Model):
    """A branch location for a company"""
    location_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__(self):
        """Return a string representation of the model."""
        return self.location_name


class Agent(models.Model):
    """A sales agent at a branch"""
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    special_license = models.BooleanField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Brokers'

    def __str__(self):
        """Returns agent name i.e. string rep"""
        return self.name


class Transaction(models.Model):
    """A sales agent at a branch"""
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    volume = models.IntegerField()
    gross_sale_amount = models.FloatField()
    order_number = models.CharField(max_length=9)
    buyer_name = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns order # and buyer i.e. string rep"""
        return f"{self.buyer_name} - {self.order_number}"
