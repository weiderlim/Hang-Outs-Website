from django import forms

from .models import Hangouts_Model

# linking the form to the model. the model is the model name, the fields are the name of the attribute fields that is in the model.
class Hangouts_Form (forms.ModelForm):
    class Meta:
        model = Hangouts_Model
        fields = [
            'category',
            'add_1',
            'add_2',
            'add_3',
            'add_4',
            'add_5',
            'add_6',
            'add_7',
            'add_8',
            'add_9',
            'add_10'
        ]
    
    # adjusting the attributes of fields with widgets. Attrs changes the attributes (similar to changing in CSS) but widgets themselves can do more than just changing attributes.
    def __init__(self, *args, **kwargs):
        super(Hangouts_Form, self).__init__(*args, **kwargs)
        self.fields['add_1'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_2'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_3'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_4'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_5'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_6'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_7'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_8'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_9'].widget.attrs['style'] = 'width:400px; height:30px'
        self.fields['add_10'].widget.attrs['style'] = 'width:400px; height:30px'
        