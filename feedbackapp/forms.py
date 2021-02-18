from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control'

            }
        )

    )
    rating=forms.IntegerField(
        label='Enter your rating',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your rating',
                'class':'form-control'
            }
        )
    )
    feedback=forms.CharField(
        label='Enter Your feedback',
        widget=forms.TextInput(
            attrs={
                'plaholder':'Enter Your Feedback',
                'class':'form-control'

            }
        )
    )

