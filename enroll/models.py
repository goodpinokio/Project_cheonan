from django.db import models

factor_mapping = {
    '걱정': 'concern',
    '분노': 'anger',
    '위축': 'atrophy',
    '열등': 'inferiority',
    '충동': 'impulse',
    '심약': 'faint',
    '온정': 'warmth',
    '사교': 'sociability',
    '주장': 'assertiveness',
    '활력': 'activity',
    '열정': 'excitement',
    '낙천': 'optimism',
    '상상': 'imagination',
    '심미': 'aesthetic',
    '감정': 'feelings',
    '시도': 'adventurous',
    '독창': 'originality',
    '가치': 'values',
    '신뢰': 'trust',
    '솔직': 'honesty',
    '이타': 'altruism',
    '순응': 'compliance',
    '겸양': 'modesty',
    '온유': 'gentleness',
    '자신': 'confidence',
    '질서': 'order',
    '소명': 'calling',
    '성취': 'achievement',
    '자율': 'autonomy',
    '숙고': 'deliberation',
}


def calculate_score(score, factor_weight, positive=True):
    if positive:
        if score <= 45:
            return factor_weight * 1
        elif 45 < score <= 50:
            return factor_weight * 2
        elif 50 < score <= 60:
            return factor_weight * 3
        elif 60 < score <= 65:
            return factor_weight * 2
        else:
            return factor_weight * 1
    else:
        if score <= 35:
            return factor_weight * 1
        elif 35 < score <= 40:
            return factor_weight * 2
        elif 40 < score <= 50:
            return factor_weight * 3
        elif 50 < score <= 55:
            return factor_weight * 2
        else:
            return factor_weight * 1



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
    suitability_score = models.FloatField(default=0.0)
    job_name = models.CharField(max_length=255, null=True)

   # 수정된 calculate_suitability_score 메서드
    def calculate_suitability_score(self):
        job_suitability = JobSuitability.objects.get(job_name=self.job_name)
        
        positive_fields = [job_suitability.score1_p, job_suitability.score2_p, job_suitability.score3_p]
        negative_fields = [job_suitability.score1_m, job_suitability.score2_m, job_suitability.score3_m]
        positive_weights = [1, 2, 3]  # score1_p, score2_p, score3_p에 대한 가중치
        negative_weights = [1, 2, 3]  # score1_m, score2_m, score3_m에 대한 가중치
        
        def calculate_scores(score_fields, factor_weights, positive=True):
            total = 0
            for field, weight in zip(score_fields, factor_weights):
                if field:
                    keywords = field.split(',')
                    for keyword in keywords:
                        total += calculate_score(getattr(self, factor_mapping[keyword.strip()]), weight, positive)
            return total

        positive_scores = calculate_scores(positive_fields, positive_weights, True)
        negative_scores = calculate_scores(negative_fields, negative_weights, False)

        total_score = positive_scores + negative_scores
        score = (total_score / 33) * 100
        return score
 
    def __str__(self):
        return f'{self.job_name}_{self.name}_{self.No}'

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


