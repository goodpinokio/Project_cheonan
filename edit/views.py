from django.shortcuts import render, redirect
from enroll.models import Job, JobSuitability
from .forms import JobForm
from django.contrib import messages
from django.http import JsonResponse
import pandas as pd
from django.db import transaction

def get_job_edit(request):
    job_name = request.GET.get('job_name')
    print(f"Requested job_name: {job_name}")
    data = {}
    try:
        job_suit = JobSuitability.objects.get(job_name=job_name)
        data = {
            'job_name': job_suit.job_name,
            'suitability': job_suit.suitability,
            'score1_p': job_suit.score1_p,
            'score1_m': job_suit.score1_m,
            'score2_p': job_suit.score2_p,
            'score2_m': job_suit.score2_m,
            'score3_p': job_suit.score3_p,
            'score3_m': job_suit.score3_m,
        }
    except JobSuitability.DoesNotExist:
        pass 

    return JsonResponse(data)

def edit_job_suitability(request):
    context = {} 
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        
        if form.is_valid():
            selected_job_name = form.cleaned_data.get('job_name')
            Job.objects.filter(job_name=selected_job_name).delete()
            JobSuitability.objects.filter(job_name=selected_job_name).delete()
            job_suitability = JobSuitability()
            job_suitability.job_name = form.cleaned_data.get('job_name')
            suitability_value = float(request.POST.get('suitability', 0.0))
            job_suitability.suitability = suitability_value

            job_suitability.score1_p = request.POST.get('score1_p')
            job_suitability.score1_m = request.POST.get('score1_m')
            job_suitability.score2_p = request.POST.get('score2_p')
            job_suitability.score2_m = request.POST.get('score2_m')
            job_suitability.score3_p = request.POST.get('score3_p')
            job_suitability.score3_m = request.POST.get('score3_m')
            job_name = form.cleaned_data.get('job_name')
            job_suitability.save()

            # 엑셀 파일불러오기
            excel_file = request.FILES['excel_file']
            try:
                data = pd.read_excel(excel_file)
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

            except Exception as e:
                messages.error(request, 'There was a problem processing your file: {}'.format(e))

            messages.success(request, "성공적으로 업데이트되었습니다.")
            return redirect('edit_job_suitability')
        else:
            messages.error(request, "폼을 올바르게 작성해주세요.")
    else:
        form = JobForm()
    
    if request.method == 'GET':
        jobs = JobSuitability.objects.all()
        context = {'form': form, 'jobs': jobs}
        selected_job_id = request.GET.get('job_id')
        
        if selected_job_id:
            selected_job = JobSuitability.objects.filter(id=selected_job_id).first()
            if selected_job:
                context['selected_job'] = selected_job
        
        return render(request, 'edit/edit.html', context)

    jobs = JobSuitability.objects.all()
    context = {'form': form, 'jobs': jobs}

    return render(request, 'edit/edit.html', context)