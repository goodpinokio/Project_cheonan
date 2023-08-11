from django import forms

class JobForm(forms.Form):
    job_name = forms.CharField(label='직무 이름', max_length=100)
    suitability = forms.IntegerField(label='적합성 %')
    excel_file = forms.FileField(label='엑셀 파일 업로드')
    