from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job, JobSuitability
import pandas as pd
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



def enroll_view(request):
    form = JobForm()

    # When the form is submitted
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():

            messages.success(request, '성공적으로 업로드하였습니다.')
            
            score1_p = request.POST.get('score1_p')
            score1_m = request.POST.get('score1_m')
            score2_p = request.POST.get('score2_p')
            score2_m = request.POST.get('score2_m')
            score3_p = request.POST.get('score3_p')
            score3_m = request.POST.get('score3_m')

            job_name = form.cleaned_data.get('job_name')
            suitability = form.cleaned_data.get('suitability')
            excel_file = request.FILES['excel_file']
    

            try:
                data = pd.read_excel(excel_file)

                # Store job suitability
                job_suit = JobSuitability(job_name=job_name, suitability=suitability, 
                                          score1_p=score1_p, score1_m=score1_m, 
                                          score2_p=score2_p, score2_m=score2_m, 
                                          score3_p=score3_p, score3_m=score3_m)
                job_suit.save()

                for index, row in data.iterrows():
                    job = Job()
                    job.No = row['No']
                    job.name = row['성명']
                    job.email = row['이메일']
                    job.Age = row['나이']
                    job.I = row['I']
                    job.S = row['S']
                    job.N = row['N']
                    job.concern = row['걱정']
                    job.anger = row['분노']
                    job.atrophy = row['위축']
                    job.inferiority = row['열등']
                    job.impulse = row['충동']
                    job.faint = row['심약']
                    job.E = row['E']
                    job.warmth = row['온정']
                    job.sociability = row['사교']
                    job.assertiveness = row['주장']
                    job.activity = row['활력']
                    job.excitement = row['열정']
                    job.optimism = row['낙천']
                    job.O = row['O']
                    job.imagination = row['상상']
                    job.aesthetic = row['심미']
                    job.feelings = row['감정']
                    job.adventurous = row['시도']
                    job.originality = row['독창']
                    job.values = row['가치']
                    job.A = row['A']
                    job.trust = row['신뢰']
                    job.honesty = row['솔직']
                    job.altruism = row['이타']
                    job.compliance = row['순응']
                    job.modesty = row['겸양']
                    job.gentleness = row['온유']
                    job.C = row['C']
                    job.confidence = row['자신']
                    job.order = row['질서']
                    job.calling = row['소명']
                    job.achievement = row['성취']
                    job.autonomy = row['자율']
                    job.deliberation = row['숙고']
                    job.job_name = job_name  # Add job name
                    job.save()

                    # Store job suitability
                # job_suit = JobSuitability(job_name=job_name, suitability=suitability, factor='your_factor', score=0)
                # job_suit.save()

            except Exception as e:
                messages.error(request, 'There was a problem processing your file: {}'.format(e))
                print(e)
                
            return redirect('enroll_view') # or wherever you want to go after the form is successfully submitted

    # if it's a GET request, just render the form
    context = {'form': form}
    return render(
        request,
        'enroll/enroll.html',
          context)
