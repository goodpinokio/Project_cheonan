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
    # `JobSuitability` 모델에서 직무 이름으로 데이터를 조회합니다.
    data = {}
    try:
        job_suit = JobSuitability.objects.get(job_name=job_name)
        data = {
            'job_name': job_suit.job_name,
            'suitability': job_suit.suitability,
            # 필요한 다른 필드들도 여기에 추가하세요.
        }
    except JobSuitability.DoesNotExist:
        pass  # 선택된 직무와 일치하는 항목이 없으면 아무것도 하지 않습니다.

    return JsonResponse(data)

def edit_job_suitability(request):
    context = {} 
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        
        if form.is_valid():
            # 선택한 직무 이름으로 기존 데이터 삭제
            selected_job_name = form.cleaned_data.get('job_name')
            
            Job.objects.filter(job_name=selected_job_name).delete()
            JobSuitability.objects.filter(job_name=selected_job_name).delete()

            # 새롭게 제출된 데이터를 기반으로 `JobSuitability` 객체 생성 및 저장
            job_suitability = JobSuitability()
            job_suitability.job_name = form.cleaned_data.get('job_name')
    
            # 이미 존재하는 job_suitability 객체의 정보 업데이트
            suitability_value = float(request.POST.get('suitability', 0.0))  # POST에서 suitability 값을 가져오며, 없으면 0.0으로 기본 설정
            job_suitability.suitability = suitability_value

            job_suitability.score1_p = request.POST.get('score1_p')
            job_suitability.score1_m = request.POST.get('score1_m')
            job_suitability.score2_p = request.POST.get('score2_p')
            job_suitability.score2_m = request.POST.get('score2_m')
            job_suitability.score3_p = request.POST.get('score3_p')
            job_suitability.score3_m = request.POST.get('score3_m')
            job_name = form.cleaned_data.get('job_name')
            job_suitability.save()

            # 엑셀 파일에서 데이터를 읽어와서 Job 모델에 저장하는 로직
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

    jobs = JobSuitability.objects.all()
    context = {'form': form, 'jobs': jobs}

    return render(request, 'edit/edit.html', context)