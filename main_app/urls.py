from django.urls import path

from . import views

app_name = 'main_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('branches/<int:branch_id>/', views.branch, name='branch'),
    path('agents/<int:agent_id>/', views.agent, name='agent'),
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
    path('branches', views.branches, name='branches'),
    path('agents', views.agents, name='agents'),
    path('transactions', views.transactions, name='transactions'),

    # paths for adding new entries
    path('new_branch/', views.new_branch, name='new_branch'),
    path('new_agent/<int:branch_id>', views.new_agent, name='new_agent'),
    path('new_transaction/<int:agent_id>', views.new_transaction, name='new_transaction'),

    #paths for edits
    path('edit_branch/<int:branch_id>/', views.edit_branch, name='edit_branch'),
    path('edit_agent/<int:agent_id>/', views.edit_agent, name='edit_agent'),
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),

    #paths for delete
    path('destroy_branch/<int:branch_id>', views.destroy_branch, name='destroy_branch'),
    path('destroy_agent/<int:agent_id>', views.destroy_agent, name='destroy_agent'),
    path('destroy_transaction/<int:transaction_id>', views.destroy_transaction, name='destroy_transaction'),

]
