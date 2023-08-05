from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enroll.models import Job, JobSuitability 
from django.core import serializers
from django.http import JsonResponse

# @login_required
# def main_view(request):
#     job_suitabilitys = JobSuitability.objects.all()
#     jobs = Job.objects.all()
#     for job in jobs:
#         job.suitability_score = job.calculate_suitability_score()
#         job.save()
#     jobs = sorted(jobs, key=lambda job: job.suitability_score, reverse=True)
#     jobs_json = serializers.serialize('json', jobs)
#     return render(
#         request, 
#         'main/base_full_width.html',
#         {'job_suitabilitys': job_suitabilitys, 'jobs': jobs_json}
#     )

@login_required
def main_view(request):
    job_suitabilitys = JobSuitability.objects.all()
    jobs = Job.objects.all()
    suitable_jobs = []

    for job in jobs:
        job.suitability_score = job.calculate_suitability_score()
        job.save()
        try:
            job_suitability = JobSuitability.objects.get(job_name=job.job_name)
            if job.suitability_score >= job_suitability.suitability:  
                suitable_jobs.append(job)
        except JobSuitability.DoesNotExist:
            pass  # or handle this situation as you prefer

    suitable_jobs = sorted(suitable_jobs, key=lambda job: job.suitability_score, reverse=True)
    # Fetch the updated Job objects from the database
    suitable_jobs = [Job.objects.get(id=job.id) for job in suitable_jobs]
    jobs_json = serializers.serialize('json', suitable_jobs)

    return render(
        request, 
        'main/base_full_width.html',
        {'job_suitabilitys': job_suitabilitys, 'jobs': jobs_json}
    )

def get_jobs_by_job_name(request):
    job_name = request.GET.get('job_name', None)
    if job_name is None:
        return JsonResponse({'error': 'No job_name provided.'}, status=400)

    jobs = Job.objects.filter(job_name=job_name)
    jobs = [Job.objects.get(id=job.id) for job in jobs]
    jobs_json = serializers.serialize('json', jobs)
    return JsonResponse({'jobs': jobs_json}, safe=False)


def get_jobs(request):
    job_name = request.GET.get('job_name', None)
    jobs = Job.objects.filter(job_name=job_name)
    count = jobs.count()

    try:
        suitability = JobSuitability.objects.get(job_name=job_name).suitability
    except JobSuitability.DoesNotExist:
        return JsonResponse({'error': 'JobSuitability for this job_name does not exist.'}, status=404)

    suitable_count = 0
    for job in jobs:
        if job.calculate_suitability_score() >= suitability:
            suitable_count += 1

    response_data = {
        'count': count,
        'suitability': suitability,
        'suitable_count': suitable_count
    }
    return JsonResponse(response_data, safe=False)


def job_list(request):
    selected_job_name = request.GET.get('selected_job', None)  # 셀렉트 박스에서 선택된 직무 이름 가져오기
    if selected_job_name:
        try:
            suitability_threshold = JobSuitability.objects.get(job_name=selected_job_name).suitability
        except JobSuitability.DoesNotExist:
            return JsonResponse({'error': 'JobSuitability for this job_name does not exist.'}, status=404)

        jobs = Job.objects.filter(name=selected_job_name, Suitability__gte=suitability_threshold).order_by('-Suitability')
    else:
        jobs = Job.objects.all().order_by('-Suitability')  # 기본적으로 모든 작업을 정확도에 따라 내림차순으로 정렬
    return render(request, 'main/base_full_width.html', {'jobs': jobs})
