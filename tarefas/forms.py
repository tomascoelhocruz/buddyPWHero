from django import forms
from django.forms import ModelForm

from .models import Contact, Comment, Quizz, Networking, QuizzAval, Comentarios


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. John'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. johndoe@mail.com'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 910000000'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Contact Card Approval'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. John'}),
            'rating': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '5'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us what you’re thinking'}),
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Joyful'}),
            'satisfaction': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Portugal'}),
            'visitDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'groupSize': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 2'}),
            'useAgain': forms.NullBooleanSelect(),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'description': 'Describe your experience',
            'satisfaction': 'Overall satisfaction',
            'visitDate': 'When?',
            'groupSize': 'How many people did you travel with?',
            'useAgain': 'Would you use buddy abroad again?',
            'image': 'Send us a picture!',

        }

        help_texts = {
            'satisfaction': 'Scale from 0 to 10',
        }


class NetworkingForm(ModelForm):
    class Meta:
        model = Networking
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. John'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. johndoe@mail.com'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 910000000'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'typeOfUser': forms.NullBooleanSelect(),

        }


class QuizzAvalForm(ModelForm):
    class Meta:
        model = QuizzAval
        fields = '__all__'

        widgets = {
            'layout': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Block'}),
            'numberOfApps': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 7'}),
            'availablePlataforms': forms.NullBooleanSelect(),
            'percentageOfPay': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 15%'}),
            'beAguide': forms.NullBooleanSelect(),
            'howManyDevs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 5'}),
            'animations': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 30'}),
            'audioQuestion': forms.NullBooleanSelect(),
            'disciplina': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Redes de computadores'}),
            'diff': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '24'}),
        }

        labels = {
            'layout': 'Qual é o layout utilizado neste website?(1pt)',
            'numberOfApps': 'Quantas aplicações compõem o Buddy Abroad?(1pt)',
            'availablePlataforms': 'O Buddy Abroad está disponível em iOS e Android?(1pt)',
            'percentageOfPay': 'O Buddy Abroad cobra quanto % de taxa?(1pt)',
            'beAguide': 'Posso ser um guia Buddy Abroad se conhecer bem a minha cidade?(1pt)',
            'howManyDevs': 'Quantos alunos trabalharam no Buddy Abroad?(1pt)',
            'animations': 'Quantas animações existem neste projecto?(1pt)',
            'audioQuestion': 'Existe algum output de audio neste website?(1pt)',
            'disciplina': 'Em que disciplina começou o projecto Buddy Abroad?(1pt)',
            'diff': 'Acha que foi difícil desenvolver este projecto? (estimativa)(1pt)',
        }


class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'

        widgets = {
            'clareza': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'rigor': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'precisao': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'profundidade': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'amplitude': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'logica': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'significancia': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'originalidade': forms.TextInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '10'}),
            'sugestao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dê uma sugestão'}),
        }

        labels = {
            'clareza': 'Clareza (compreensível, em que o significado pode ser identificado sem que haja confusão ou '
                       'ambiguidade.):',
            'rigor': 'Rigor (livre de erros):',
            'precisao': 'Precisão (exato, segundo o nível necessário do pormenor):',
            'profundidade': 'Profundidade (contém complexidades e múltiplas inter-relações):',
            'amplitude': 'Amplitude (que abrange diferentes aspectos, pontos de vista, pespectivas):',
            'logica': 'Lógica (em que as partes fazem sentido num todo, sem contradições: faz sentido no conjunto, '
                      'provém de evidências):',
            'significancia': 'Significância (focado no importante, não trivial):',
            'originalidade': 'Originalidade (criativo e original):',
            'sugestao': 'Sugestões de melhoria:',
        }
