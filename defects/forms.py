from django import forms
from defects.models import defectData

class DefectEditForm(forms.ModelForm):
    defect_id = forms.CharField(max_length=100,disabled=True)
    defect_name = forms.CharField(max_length=100,disabled=True)
    # assigned_by = forms.CharField(max_length=100,disabled=True)
    class Meta:
        model = defectData
        fields = ['defect_id','defect_name','assigned_by','assigned_to','priority','description','defect_status']

class DefectAddForm(forms.ModelForm):
    class Meta:
        model = defectData
        fields = "__all__"
class FilterDefectForm(forms.ModelForm):
    class Meta:
        model =defectData
        fields = ['assigned_to']