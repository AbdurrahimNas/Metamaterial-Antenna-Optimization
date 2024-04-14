from django.db import models

# Create your models here.


class Metamaterial(models.Model):
    Wm = models.DecimalField("Wm",
                             max_digits=9, decimal_places=3,
                             blank=False, null=False,
                             help_text="Width and height of SRR cell")
    
    W0m = models.DecimalField("W0m",
                             max_digits=7, decimal_places=3,
                             blank=False, null=False,
                             help_text="Gap between rings")
    
    dm = models.DecimalField("dm",
                            max_digits=7, decimal_places=3,
                            blank=False, null=False,
                            help_text="Distance between rings")
    
    tm = models.DecimalField("tm",
                            max_digits=9, decimal_places=3,
                            blank=False, null=False,
                            help_text="Width of the rings")
    
    rows = models.DecimalField("rows",
                            max_digits=3, decimal_places=1,
                            blank=False, null=False,
                            help_text="Number of SRR cells in a array")
    
    Xa = models.DecimalField("Xa",
                            max_digits=9, decimal_places=3,
                            blank=False, null=False,
                            help_text="Distance between antenna patch and array")
    
    Ya = models.DecimalField("Ya",
                            max_digits=9, decimal_places=3,
                            blank=False, null=False,
                            help_text="Distance between SRR cells in the array")
    
    gain = models.DecimalField("gain",
                            max_digits=9, decimal_places=7,
                            blank=False, null=False,
                            help_text="Antenna gain")
    
    vswr = models.DecimalField("vswr",
                            max_digits=9, decimal_places=7,
                            blank=False, null=False,
                            help_text="Voltage Standing Wave Ratio of the antenna")
    

    bandwidth = models.DecimalField("bandwidth",
                            max_digits=10, decimal_places=7,
                            blank=False, null=False,
                            help_text="Bandwidth of the antenna")
    
    s = models.DecimalField("s", default=0,
                            max_digits=10, decimal_places=7,
                            blank=False, null=False,
                            help_text="Return Loss (S11) of the antenna")
    
    pr = models.DecimalField("pr", default=0,
                            max_digits=9, decimal_places=7,
                            blank=False, null=False,
                            help_text="Power radiated by antenna")
    

    p0 = models.DecimalField("p0", default=0,
                            max_digits=9, decimal_places=7,
                            blank=False, null=False,
                            help_text="Power accepted by antenna")
    

    def __str__(self):
        return self.id
    
    
        