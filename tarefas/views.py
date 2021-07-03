from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm, CommentForm, QuizzForm, NetworkingForm, QuizzAvalForm, ComentariosForm
from .models import Comment, Networking, QuizzAval, Comentarios

import matplotlib.pyplot as plt
from io import StringIO
import numpy as np


# Buddy Abroad Web
def contacts_page_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Message Sent!')
        return HttpResponseRedirect(reverse('tarefas:contacts'))

    context = {'form': form}

    return render(request, 'tarefas/contacts.html', context)


def aval_page_view(request):
    return render(request, 'tarefas/aval.html')


def reviews_page_view(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:reviews'))

    average = list(Comment.objects.aggregate(Avg('rating')).values())[0] or 0

    starRatings0 = Comment.objects.filter(rating=1).count()
    starRatings1 = Comment.objects.filter(rating=2).count()
    starRatings2 = Comment.objects.filter(rating=3).count()
    starRatings3 = Comment.objects.filter(rating=4).count()
    starRatings4 = Comment.objects.filter(rating=5).count()

    context = {'form': form, 'comments': Comment.objects.all(), 'averageStars': round(average, 1),
               'starRatings0': starRatings0,
               'starRatings1': starRatings1,
               'starRatings2': starRatings2,
               'starRatings3': starRatings3,
               'starRatings4': starRatings4,
               'reviewCount': Comment.objects.count(),
               }

    return render(request, 'tarefas/reviews.html', context)


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Quizz Completed!')
        return HttpResponseRedirect(reverse('tarefas:quizz'))

    context = {'form': form, }

    return render(request, 'tarefas/quizz.html', context)


def networking_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networking.html', context)


def networkingAddUser_page_view(request):
    form = NetworkingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:index'))

    context = {'form': form}

    return render(request, 'tarefas/networkingAddUser.html', context)


def quizzAval_page_view(request):
    form = QuizzAvalForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        messages.success(request, 'Quizz Completo!')
        return HttpResponseRedirect(reverse('tarefas:quizzAvalResults', args=(task.id,)))

    context = {'form': form, }

    return render(request, 'tarefas/quizzAval.html', context)


def quizzAvalResults_page_view(request, quizzAval_id):
    quizzAnswer = QuizzAval.objects.get(id=quizzAval_id)
    questionsAndAnswer = {
        "Qual é o layout utilizado neste website?(1pt)": "column",
        "Quantas aplicações compõem o Buddy Abroad?(1pt)": "tantoFaz",
        "O Buddy Abroad está disponível em iOS e Android?(1pt": 2,
        "O Buddy Abroad cobra quanto % de taxa?(1pt)": 30,
        "Posso ser um guia Buddy Abroad se conhecer bem a minha cidade?(1pt)": "True",
        "Quantos alunos trabalharam no Buddy Abroad?(1pt)": 2,
        "Quantas animações existem neste projecto?(1pt)": 2,
        "Existe algum output de audio neste website?(1pt)": "True",
        "Em que disciplina começou o projecto Buddy Abroad?(1pt)": "trabalho final de curso",
        "Acha que foi difícil desenvolver este projecto? (estimativa)(1pt)": "menor que 12",
    }

    correctThick = [
        [str(quizzAnswer.layout), True if quizzAnswer.layout == 'column' else False],
        [str(quizzAnswer.beAguide), True],
        [str(quizzAnswer.numberOfApps), True if quizzAnswer.numberOfApps == 2 else False],
        [str(quizzAnswer.percentageOfPay), True if quizzAnswer.percentageOfPay == 30 else False],
        [str(quizzAnswer.availablePlataforms), True if quizzAnswer.availablePlataforms == True else False],
        [str(quizzAnswer.howManyDevs), True if quizzAnswer.howManyDevs == 2 else False],
        [str(quizzAnswer.animations), True if quizzAnswer.animations == 2 else False],
        [str(quizzAnswer.audioQuestion), True if quizzAnswer.audioQuestion == True else False],
        [str(quizzAnswer.disciplina), True if quizzAnswer.disciplina == 'trabalho final de curso' else False],
        [str(quizzAnswer.diff), True if quizzAnswer.diff <= 12 else False],
    ]

    CorrectNumber = sum(x.count(True) for x in correctThick)

    context = {'correctNumber': CorrectNumber,
               'questionsAndAnswer': questionsAndAnswer, 'correctThick': correctThick}

    return render(request, 'tarefas/quizzAvalResults.html', context)


def comentarios_page_view(request):
    form = ComentariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Formulário Completo!')
        return HttpResponseRedirect(reverse('tarefas:comentarios'))

    context = {'form': form, }

    return render(request, 'tarefas/comentarios.html', context)


def networkingEditUser_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networkingEditUser.html', context)


def networkingRemoveUser_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networkingRemoveUser.html', context)


def deleteConfirmation_page_view(request, card_id):
    context = {'cardId': card_id}

    return render(request, 'tarefas/deleteConfirmation.html', context)


def apaga_card_view(request, card_id):
    Networking.objects.get(id=card_id).delete()
    return HttpResponseRedirect(reverse('tarefas:networkingRemoveUser'))


def editUserCard_view(request, card_id):
    card = Networking.objects.get(id=card_id)
    form = NetworkingForm(request.POST or None, instance=card)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:networkingEditUser'))

    context = {'form': form, 'card_id': card_id}
    return render(request, 'tarefas/editUserCard.html', context)


def index_page_view(request):
    # Review Section get average and 3 reviews
    average = list(Comment.objects.aggregate(Avg('rating')).values())[0] or 0

    context = {'comments': Comment.objects.all()[:3], 'averageStars': round(average, 1),
               'reviewCount': Comment.objects.count(),
               }

    return render(request, 'tarefas/index.html', context)


def avalPt2_page_view(request):
    return render(request, 'tarefas/avalPt2.html')


def graphs_page_view(request):
    def quizz_graph():

        quizzAnswerLayout = QuizzAval.objects.all().values_list('layout', flat=True)
        correctThickLayout = []
        for value in quizzAnswerLayout:
            correctThickLayout.append(True if value == 'column' else False)

        quizzAnswerBeAguide = QuizzAval.objects.all().values_list('beAguide', flat=True)
        correctThickBeAguide = []
        for value in quizzAnswerBeAguide:
            correctThickBeAguide.append(True)

        quizzAnswerNumberOfApps = QuizzAval.objects.all().values_list('numberOfApps', flat=True)
        correctThickNumberOfApps = []
        for value in quizzAnswerNumberOfApps:
            correctThickNumberOfApps.append(True if value == 2 else False)

        quizzAnswerPercentageOfPay = QuizzAval.objects.all().values_list('percentageOfPay', flat=True)
        correctThickPercentageOfPay = []
        for value in quizzAnswerPercentageOfPay:
            correctThickPercentageOfPay.append(True if value == 30 else False)

        quizzAnswerAvailablePlataforms = QuizzAval.objects.all().values_list('availablePlataforms', flat=True)
        correctThickAvailablePlataforms = []
        for value in quizzAnswerAvailablePlataforms:
            correctThickAvailablePlataforms.append(True if value == True else False)

        quizzAnswerHowManyDevs = QuizzAval.objects.all().values_list('howManyDevs', flat=True)
        correctThickHowManyDevs = []
        for value in quizzAnswerHowManyDevs:
            correctThickHowManyDevs.append(True if value == 2 else False)

        quizzAnswerAnimations = QuizzAval.objects.all().values_list('animations', flat=True)
        correctThickAnimations = []
        for value in quizzAnswerAnimations:
            correctThickAnimations.append(True if value == 2 else False)

        quizzAnswerAudioQuestion = QuizzAval.objects.all().values_list('audioQuestion', flat=True)
        correctThickAudioQuestion = []
        for value in quizzAnswerAudioQuestion:
            correctThickAudioQuestion.append(True if value == True else False)

        quizzAnswerDisciplina = QuizzAval.objects.all().values_list('disciplina', flat=True)
        correctThickDisciplina = []
        for value in quizzAnswerDisciplina:
            correctThickDisciplina.append(True if value == 'trabalho final de curso' else False)

        quizzAnswerDiff = QuizzAval.objects.all().values_list('diff', flat=True)
        correctThickDiff = []
        for value in quizzAnswerDiff:
            correctThickDiff.append(True if value == 'trabalho final de curso' else False)

        y = [
            sum(x == True for x in correctThickLayout),
            sum(x == True for x in correctThickBeAguide),
            sum(x == True for x in correctThickNumberOfApps),
            sum(x == True for x in correctThickPercentageOfPay),
            sum(x == True for x in correctThickAvailablePlataforms),
            sum(x == True for x in correctThickHowManyDevs),
            sum(x == True for x in correctThickAnimations),
            sum(x == True for x in correctThickAudioQuestion),
            sum(x == True for x in correctThickDisciplina),
            sum(x == True for x in correctThickDiff),
        ]

        print(y)

        x = ['Q.1', 'Q.2', 'Q.3', 'Q.4', 'Q.5', 'Q.6', 'Q.7',
             'Q.8', 'Q.9', 'Q.10']

        fig = plt.figure()
        plt.bar(x, y, color='green')
        plt.xlabel("Question number")
        plt.ylabel("Sum. of right answers")
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data

    def comments_graph():
        # Data
        questions = ['Clareza', 'Rigor', 'Precisão', 'Profundidade', 'Amplitude', 'Lógica', 'Significância',
                     'Originalidade']
        marks = [sum(Comentarios.objects.all().values_list('clareza', flat=True)),
                 sum(Comentarios.objects.all().values_list('rigor', flat=True)),
                 sum(Comentarios.objects.all().values_list('precisao', flat=True)),
                 sum(Comentarios.objects.all().values_list('profundidade', flat=True)),
                 sum(Comentarios.objects.all().values_list('amplitude', flat=True)),
                 sum(Comentarios.objects.all().values_list('logica', flat=True)),
                 sum(Comentarios.objects.all().values_list('significancia', flat=True)),
                 sum(Comentarios.objects.all().values_list('originalidade', flat=True)), ]
        # Graph Creation
        fig = plt.figure(figsize=(11, 5))
        plt.bar(questions, marks)
        plt.xlabel("Questions")
        plt.ylabel("Sum. of marks given")

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data

    context = {'quizzGraph': quizz_graph(),
               'commentGraph': comments_graph()}

    return render(request, 'tarefas/graphs.html', context)


def spa_page_view(request):
    return render(request, 'tarefas/spa.html')


exampleToursData = [
    "Gerês:Nature Hike:For those who wanted to travel there with only limited time, we decided to come up with a more "
    "convenient way to maximize your trip as well as enjoy every minute of it. We have Gerês Tour - Hiking & "
    "Sightseeing where in, you can experience the amazing exquisiteness of nature, traditional culture and the "
    "friendly locals of the Peneda-Gerês National Park. Also, we included several interesting activities which will "
    "lead you to the mountains, rivers, waterfalls and magnificent settings.",
    "Coimbra:Sightseeing: RM Tour was born from the idea of transforming visits to the University of Coimbra into a "
    "unique experience, transforming the guided tour into a pleasant experience of knowledge and cultural enrichment "
    "in a way that is interesting. Therefore, we always seek in our company to join the beautiful history of the "
    "University of Coimbra with the present and its customs that still permeate our institution today. This was all "
    "made possible by the training we have in the areas of history, sociology and tourism. Our collaborators are "
    "former students of the University of Coimbra which brings to our services a great appreciation and knowledge of "
    "it.",
    "Lisboa:Tuk-Tuk Ride:Do you want to see it all? Do you have time for a 3 hour tour? Then do "
    "it. It is Alfama Tour + City Center Tour. A great overview of the city. Frequent travellers often choose this "
    "tour for the best input interest information. Once you ride with us, you get inside the Portuguese culture, "
    "the dynamic of the city and the useful tips that only the local guides can provide."]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(exampleToursData[num - 1])
    else:
        raise Http404("No such section")
