from django.db import models

class Job(models.Model):
    No = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    Age = models.IntegerField()
    I = models.IntegerField()
    S = models.IntegerField()
    N = models.IntegerField()
    concern = models.IntegerField()
    anger = models.IntegerField()
    atrophy = models.IntegerField()
    inferiority = models.IntegerField()
    impulse = models.IntegerField()
    faint = models.IntegerField()
    E = models.IntegerField()
    warmth = models.IntegerField()
    sociability = models.IntegerField()
    assertiveness = models.IntegerField()
    activity = models.IntegerField()
    excitement = models.IntegerField()
    optimism = models.IntegerField()
    O = models.IntegerField()
    imagination = models.IntegerField()
    aesthetic = models.IntegerField()
    feelings = models.IntegerField()
    adventurous = models.IntegerField()
    originality = models.IntegerField()
    values = models.IntegerField()
    A = models.IntegerField()
    trust = models.IntegerField()
    honesty = models.IntegerField()
    altruism = models.IntegerField()
    compliance = models.IntegerField()
    modesty = models.IntegerField()
    gentleness = models.IntegerField()
    C = models.IntegerField()
    confidence = models.IntegerField()
    order = models.IntegerField()
    calling = models.IntegerField()
    achievement = models.IntegerField()
    autonomy = models.IntegerField()
    deliberation = models.IntegerField()
    job_name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f'{self.job_name}_{self.name}_{self.No}'

# class JobSuitability(models.Model):
#     job_name = models.CharField(max_length=255, null=True)
#     suitability = models.FloatField()
#     factor = models.CharField(max_length=255)
#     score = models.IntegerField()

#     def __str__(self):
#         return self.job_name   

class JobSuitability(models.Model):
    job_name = models.CharField(max_length=255, null=True)
    suitability = models.FloatField()
    score1_p = models.TextField(blank=True, null=True)  
    score1_m = models.TextField(blank=True, null=True)  
    score2_p = models.TextField(blank=True, null=True) 
    score2_m = models.TextField(blank=True, null=True)
    score3_p = models.TextField(blank=True, null=True)
    score3_m = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_name


