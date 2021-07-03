from django.urls import path

from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('index/', views.index_page_view, name='index'),
    # Buddy Abroad
    path('contacts/', views.contacts_page_view, name='contacts'),
    path('aval/', views.aval_page_view, name='aval'),
    path('reviews/', views.reviews_page_view, name='reviews'),
    path('quizz/', views.quizz_page_view, name='quizz'),
    path('networking/', views.networking_page_view, name='networking'),
    path('networkingAddUser/', views.networkingAddUser_page_view, name='networkingAddUser'),
    path('quizzAval/', views.quizzAval_page_view, name='quizzAval'),
    path('quizzAvalResults/<int:quizzAval_id>', views.quizzAvalResults_page_view, name='quizzAvalResults'),
    path('comentarios/', views.comentarios_page_view, name='comentarios'),
    path('networkingEditUser/', views.networkingEditUser_page_view, name='networkingEditUser'),
    path('networkingRemoveUser/', views.networkingRemoveUser_page_view, name='networkingRemoveUser'),
    path('deleteConfirmation/<int:card_id>', views.deleteConfirmation_page_view, name='deleteConfirmation'),
    path('apagaCard/<int:card_id>', views.apaga_card_view, name='apagaCard'),
    path('editaCard/<int:card_id>', views.editUserCard_view, name='editaCard'),
    path('avalPt2/', views.avalPt2_page_view, name='avalPt2'),
    path('graphs/', views.graphs_page_view, name='graphs'),
    path('spa/', views.spa_page_view, name='spa'),
    path("sections/<int:num>", views.section, name="section")
]
