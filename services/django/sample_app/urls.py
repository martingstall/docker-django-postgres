from django.urls import path
from . import views

urlpatterns = [
    path('', views.users.index, name='index'),
    path('create_users/', views.users.create_users, name='create_users'),
    path('list_users/', views.users.list_users, name='list_users'),
    path('create_perms/', views.users.create_perms, name='create_perms'),

    path('ae/', views.api_calls.test_ae, name='test_ae'),
    path('dc/', views.api_calls.test_dc, name='test_dc'),
    path('normalization_example/', views.api_calls.normalization_example, name='normalization_example'),

    path('pptx/', views.pptx.index, name='index'),
    path('save_pptx/', views.pptx.save_pptx, name='save_pptx'),

    path('lit_table_example/', views.campaign.lit_table_example, name='lit_table_example'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/', views.campaign.view_step, name='view_step'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/save/', views.campaign.save_step_data, name='save_step_data'),

    path('cf/create_example/', views.campaign_framework.create_example, name='create_example'),

    path('campaign/create_example/', views.campaign.create_example, name='create_example'),

    path('app_store/load_app/<int:app_id>/', views.app_store.load_app, name='load_app'),
    path('app_store/create_example/', views.app_store.create_example, name='create_example'),
]
