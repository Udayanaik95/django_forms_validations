from django import forms

g=[('Male','male'),('Female','female')]
c=[['Python','python'],('Java','java'),{'Sql','sql'}]

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':20, 'rows':5}))
    gender=forms.ChoiceField(choices=g) # Dropdown List 
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect) # Radio Buttons
    course=forms.MultipleChoiceField(choices=c) # Single Choice
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple) # Multiple Choice
