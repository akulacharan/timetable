from django.db import models

# Create your models here.

class TimeTable(models.Model):
    username = models.CharField(max_length=100)
    email    = models.CharField(max_length=100)
    #Timings
    tm1      = models.CharField(max_length=100,blank=True,null=True)
    tm2      = models.CharField(max_length=100,blank=True,null=True)
    tm3      = models.CharField(max_length=100,blank=True,null=True)
    tm4      = models.CharField(max_length=100,blank=True,null=True)
    tm5      = models.CharField(max_length=100,blank=True,null=True)
    tm6      = models.CharField(max_length=100,blank=True,null=True)
    tm7      = models.CharField(max_length=100,blank=True,null=True)
    tm8      = models.CharField(max_length=100,blank=True,null=True)
    # ON MONDAY
    m1       = models.CharField(max_length=100,blank=True,null=True)
    m2       = models.CharField(max_length=100,blank=True,null=True)
    m3       = models.CharField(max_length=100,blank=True,null=True)
    m4       = models.CharField(max_length=100,blank=True,null=True)
    m5       = models.CharField(max_length=100,blank=True,null=True)
    m6       = models.CharField(max_length=100,blank=True,null=True)
    m7       = models.CharField(max_length=100,blank=True,null=True)
    m8       = models.CharField(max_length=100,blank=True,null=True)

    #ON TUESDAY
    tu1     = models.CharField(max_length=100,blank=True,null=True)
    tu2     = models.CharField(max_length=100,blank=True,null=True)
    tu3     = models.CharField(max_length=100,blank=True,null=True)
    tu4     = models.CharField(max_length=100,blank=True,null=True)
    tu5     = models.CharField(max_length=100,blank=True,null=True)
    tu6     = models.CharField(max_length=100,blank=True,null=True)
    tu7     = models.CharField(max_length=100,blank=True,null=True)

    # ON WEDNESDAY

    w1      = models.CharField(max_length=100,blank=True,null=True)
    w2      = models.CharField(max_length=100,blank=True,null=True)
    w3      = models.CharField(max_length=100,blank=True,null=True)
    w4      = models.CharField(max_length=100,blank=True,null=True)
    w5      = models.CharField(max_length=100,blank=True,null=True)

    # ON THURSDAY

    th1     = models.CharField(max_length=100,blank=True,null=True)
    th2     = models.CharField(max_length=100,blank=True,null=True)
    th3     = models.CharField(max_length=100,blank=True,null=True)
    th4     = models.CharField(max_length=100,blank=True,null=True)
    th5     = models.CharField(max_length=100,blank=True,null=True)
    th6     = models.CharField(max_length=100,blank=True,null=True)
    th7     = models.CharField(max_length=100,blank=True,null=True)

    # ON FRIDAY

    f1      = models.CharField(max_length=100,blank=True,null=True)
    f2      = models.CharField(max_length=100,blank=True,null=True)
    f3      = models.CharField(max_length=100,blank=True,null=True)
    f4      = models.CharField(max_length=100,blank=True,null=True)
    f5      = models.CharField(max_length=100,blank=True,null=True)
    f6      = models.CharField(max_length=100,blank=True,null=True)
    f7      = models.CharField(max_length=100,blank=True,null=True)

    # ON SATURDAY

    s1      = models.CharField(max_length=100,blank=True,null=True)
    s2      = models.CharField(max_length=100,blank=True,null=True)
    s3      = models.CharField(max_length=100,blank=True,null=True)
    s4      = models.CharField(max_length=100,blank=True,null=True)
    s5      = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.username



