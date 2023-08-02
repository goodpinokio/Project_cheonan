from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from enroll.models import Job, JobSuitability  # Here, replace `table` with `enroll`


def table_view(request):
    job_suitabilitys = JobSuitability.objects.all()
    jobs = Job.objects.all()
    jobs_json = serializers.serialize('json', jobs)
    return render(
        request,
        'table/table.html',
        {'job_suitabilitys': job_suitabilitys, 'jobs': jobs_json}
    )

# def get_job_data(request):
#     job_name = request.GET.get('job_name', None)

#     data = {'job_data': []}

#     if job_name:
#         jobs = Job.objects.filter(job_name=job_name)

#         for job in jobs:
#             data['job_data'].append({
#                 'No': job.No,
#                 'Name': job.name,
#                 'Email': job.email,
#                 'Age': job.Age,
#                 # add other fields if required
#             })

#     return JsonResponse(data)

def get_jobs(request):
    job_name = request.GET.get('job_name', None)
    jobs = Job.objects.filter(job_name=job_name)
    print(f"Jobs for {job_name}: {jobs}")
    jobs_json = serializers.serialize('json', jobs)
    return JsonResponse(jobs_json, safe=False)
