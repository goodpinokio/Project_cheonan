from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from enroll.models import Job, JobSuitability

def table_view(request):
    job_suitabilitys = JobSuitability.objects.all()
    jobs = Job.objects.all()
    jobs_json = serializers.serialize('json', jobs)
    return render(
        request,
        'table/table.html',
        {'job_suitabilitys': job_suitabilitys, 'jobs': jobs_json}
    )

def get_jobs(request):
    job_name = request.GET.get('job_name', None)
    jobs = Job.objects.filter(job_name=job_name)
    print(f"Jobs for {job_name}: {jobs}")
    jobs_json = serializers.serialize('json', jobs)
    return JsonResponse(jobs_json, safe=False)
