from django.db import models
from django.contrib.auth.models import User

# Custom User model that extends the built-in User model

class housing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='housing_expenses')
    rent = models.FloatField()
    electricity = models.FloatField()
    water = models.FloatField()
    gas = models.FloatField()
    sewage = models.FloatField()
    internet = models.FloatField()
    insurance = models.FloatField()
    taxes = models.FloatField()
    repairs = models.FloatField()
    furnishings = models.FloatField()
    security = models.FloatField()
    other = models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.rent = float(self.rent or 0.0)
        self.electricity = float(self.electricity or 0.0)
        self.water = float(self.water or 0.0)
        self.gas = float(self.gas or 0.0)
        self.sewage = float(self.sewage or 0.0)
        self.internet = float(self.internet or 0.0)
        self.insurance = float(self.insurance or 0.0)
        self.taxes = float(self.taxes or 0.0)
        self.repairs = float(self.repairs or 0.0)
        self.furnishings = float(self.furnishings or 0.0)
        self.security = float(self.security or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.rent + self.electricity + self.water + self.gas +
            self.sewage + self.internet + self.insurance + self.taxes +
            self.repairs + self.furnishings + self.security + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)
    def __str__(self):
          #return f"Housing for {self.user.username}: {self.total}"
          return f"Housing for : {self.total}"

class food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_expenses')
    fresh=models.FloatField()
    meat=models.FloatField()
    sweets=models.FloatField()
    fast=models.FloatField()
    dairy=models.FloatField()
    beverages=models.FloatField()
    restaurants=models.FloatField()
    pet=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.fresh = float(self.fresh or 0.0)
        self.meat = float(self.meat or 0.0)
        self.sweets = float(self.sweets or 0.0)
        self.fast = float(self.fast or 0.0)
        self.dairy = float(self.dairy or 0.0)
        self.beverages = float(self.beverages or 0.0)
        self.restaurants = float(self.restaurants or 0.0)
        self.pet = float(self.pet or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.fresh + self.meat + self.sweets + self.fast +
            self.dairy + self.beverages + self.restaurants + self.pet + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Food Total: {self.total}"
    
class shopping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_expenses')
    clothes=models.FloatField()
    access=models.FloatField()
    beauty=models.FloatField()
    electronics=models.FloatField()
    homeacs=models.FloatField()
    sports=models.FloatField()
    toys=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.clothes = float(self.clothes or 0.0)
        self.access = float(self.access or 0.0)
        self.beauty = float(self.beauty or 0.0)
        self.electronics = float(self.electronics or 0.0)
        self.homeacs = float(self.homeacs or 0.0)
        self.sports = float(self.sports or 0.0)
        self.toys = float(self.toys or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.clothes + self.access + self.beauty + self.electronics +
            self.homeacs + self.sports + self.toys + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"shopping Total: {self.total}"
    
class travelling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='travelling_expenses')
    transportation=models.FloatField()
    accommodation=models.FloatField()
    insurance=models.FloatField()
    visa=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.transportation = float(self.transportation or 0.0)
        self.accommodation = float(self.accommodation or 0.0)
        self.insurance = float(self.insurance or 0.0)
        self.visa = float(self.visa or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.transportation + self.accommodation + self.insurance + self.visa + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"travelling Total: {self.total}"

class socialservice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socialservice_expenses')
    program=models.FloatField()
    staff=models.FloatField()
    operational=models.FloatField()
    donation=models.FloatField()
    transportation=models.FloatField()
    legal=models.FloatField()
    subsidies=models.FloatField()
    health=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)
   
    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.program = float(self.program or 0.0)
        self.staff = float(self.staff or 0.0)
        self.operational = float(self.operational or 0.0)
        self.donation = float(self.donation or 0.0)
        self.transportation = float(self.transportation or 0.0)
        self.legal = float(self.legal or 0.0)
        self.subsidies = float(self.subsidies or 0.0)
        self.health = float(self.health or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.program + self.staff + self.operational + self.donation + self.transportation + self.legal + self.subsidies + self.health + self.subsidies
        )
        print(self.total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"socialservice Total: {self.total}"
    
class entertainment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entertainment_expenses')
    movie=models.FloatField()
    music=models.FloatField()
    sports=models.FloatField()
    gaming=models.FloatField()
    book=models.FloatField()
    hobby=models.FloatField()
    event=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.movie = float(self.movie or 0.0)
        self.music = float(self.music or 0.0)
        self.sports = float(self.sports or 0.0)
        self.gaming = float(self.gaming or 0.0)
        self.book = float(self.book or 0.0)
        self.hobby = float(self.hobby or 0.0)
        self.event = float(self.event or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.movie + self.music + self.sports + self.gaming + self.book + self.hobby + self.event + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"entertainment Total: {self.total}"

class health(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='healthcare_expenses')
    medicines=models.FloatField()
    mental=models.FloatField()
    physical=models.FloatField()
    insurance=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.medicines = float(self.medicines or 0.0)
        self.mental = float(self.mental or 0.0)
        self.physical = float(self.physical or 0.0)
        self.insurance = float(self.insurance or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.medicines + self.mental + self.physical + self.insurance + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"health Total: {self.total}"
    
class school(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schooling_expenses')
    fee=models.FloatField()
    supplies=models.FloatField()
    uniforms=models.FloatField()
    transportation=models.FloatField()
    enrichment=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.fee = float(self.fee or 0.0)
        self.supplies = float(self.supplies or 0.0)
        self.uniforms = float(self.uniforms or 0.0)
        self.transportation = float(self.transportation or 0.0)
        self.enrichment = float(self.enrichment or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.fee + self.supplies + self.uniforms + self.transportation + self.enrichment + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"school Total: {self.total}"
    
class busines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='busines_expenses')
    operational=models.FloatField()
    employ=models.FloatField()
    adv=models.FloatField()
    sales=models.FloatField()
    other=models.FloatField()
    total = models.FloatField(default=0.0)
    date_field = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure no empty strings are passed to FloatField
        self.operational = float(self.operational or 0.0)
        self.employ = float(self.employ or 0.0)
        self.adv = float(self.adv or 0.0)
        self.sales = float(self.sales or 0.0)
        self.other = float(self.other or 0.0)

        # Recalculate the total
        self.total = (
            self.operational + self.employ + self.adv + self.sales + self.other
        )
        print(self.total)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"business Total: {self.total}"
    
class budgetplanning(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income=models.IntegerField()
    housing=models.IntegerField()
    food=models.IntegerField()
    shopping=models.IntegerField()
    travelling=models.IntegerField()
    entertainment=models.IntegerField()
    health=models.IntegerField()
    school=models.IntegerField()
    busines=models.IntegerField()
    socialservice=models.IntegerField()
    other=models.IntegerField()
    def __str__(self):
         # Return a string representation
        return f"Budget for {self.user.username} - Income: {self.income}"

class bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
    account_type = models.CharField(max_length=50)  # E.g., Savings, Current
    branch_name = models.CharField(max_length=255)
    holder = models.CharField(max_length=255)  # Account holder's name
    #swift = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"Bank for {self.user.username} - : {self.bank_name}"
