from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=254, default='', blank=False)
    phone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=200, blank=False, default='')
    message = models.TextField(max_length=400, blank=False, default='')

    def __str__(self):
        return self.email[:50]


class Comment(models.Model):
    name = models.CharField(max_length=200, blank=False)
    rating = models.IntegerField(blank=False, default='5')
    comment = models.TextField(max_length=400, blank=False, default='')
    postedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:50]


class Quizz(models.Model):
    description = models.CharField(max_length=200, blank=False)
    satisfaction = models.IntegerField(blank=False, default='5')
    destination = models.CharField(max_length=200, blank=False)
    visitDate = models.DateField(null=True, blank=True)
    groupSize = models.IntegerField(blank=True, null=True)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    useAgain = models.BooleanField(choices=BOOL_CHOICES)

    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.description[:50]


class Networking(models.Model):
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=254, default='', blank=False)
    phone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)

    choices = ((True, 'Guide'), (False, 'Tourist'))
    typeOfUser = models.BooleanField(choices=choices, default=False)

    def __str__(self):
        return self.name[:50]


class QuizzAval(models.Model):
    layout = models.CharField(max_length=200, blank=False)

    beAguideChoices = ((True, 'Sim!'), (False, 'Siiiim!'))
    beAguide = models.BooleanField(choices=beAguideChoices, blank=False)

    numberOfApps = models.IntegerField(blank=False)
    percentageOfPay = models.IntegerField(blank=False)

    plataformChoices = ((True, 'Sim'), (False, 'Não'))
    availablePlataforms = models.BooleanField(choices=plataformChoices, blank=False)

    howManyDevs = models.IntegerField(blank=False)
    animations = models.IntegerField(blank=False)

    audioChoices = ((True, 'Sim'), (False, 'Não'))
    audioQuestion = models.BooleanField(choices=audioChoices, blank=False)

    disciplina = models.CharField(max_length=200, blank=False)
    diff = models.IntegerField(blank=False, default='12')


class Comentarios(models.Model):
    clareza = models.IntegerField(blank=False, default='12')
    rigor = models.IntegerField(blank=False, default='12')
    precisao = models.IntegerField(blank=False, default='12')
    profundidade = models.IntegerField(blank=False, default='12')
    amplitude = models.IntegerField(blank=False, default='12')
    logica = models.IntegerField(blank=False, default='12')
    significancia = models.IntegerField(blank=False, default='12')
    originalidade = models.IntegerField(blank=False, default='12')
    sugestao = models.TextField(max_length=400, blank=False, default='')


class CommonUser(models.Model):
    name = models.CharField(max_length=64)
    accessToken = models.CharField(max_length=64)


class Like(models.Model):
    liked = models.ForeignKey(CommonUser,
                              on_delete=models.CASCADE, )


class Post(models.Model):
    numberOfLikes = models.ManyToManyField(Like, blank=True, )
