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
    path('pptx/create/', views.pptx.create_pptx, name='create_pptx'),

    path('lit_table_example/', views.campaign.lit_table_example, name='lit_table_example'),

    path('cf/create_example/', views.campaign_framework.create_example, name='create_example'),
    path('cf/update_example/', views.campaign_framework.update_example, name='update_example'),

    path('campaign/<int:campaign_id>/', views.campaign.campaign_details, name='campaign_details'),
    path('campaign/<int:campaign_id>/pptx/create/', views.campaign.create_campaign_pptx, name='create_campaign_pptx'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/', views.campaign.view_step, name='view_step'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/save/', views.campaign.save_step_data, name='save_step_data'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/html_file/', views.campaign.upload_step_html_file, name='upload_step_html_file'),
    path('campaign/<int:campaign_id>/step/<int:cf_step_id>/api_call/', views.campaign.step_api_call, name='step_api_call'),

    path('app_store/load_app/<int:app_id>/', views.app_store.load_app, name='load_app'),
    path('app_store/create_example/', views.app_store.create_example, name='create_example'),
]
