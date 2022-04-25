from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Branch, Agent, Transaction
from .forms import BranchForm, AgentForm, TransactionForm


def index(request):
    """The home page for widget international"""
    branches = Branch.objects.order_by('date_added')
    agents = Agent.objects.order_by('date_added')
    transactions = Transaction.objects.order_by('date_added')
    context = {'branches': branches, 'agents': agents, 'transactions': transactions}
    return render(request, 'index.html', context)


def branch(request, branch_id):
    """show branch and list agents"""
    branch = Branch.objects.get(id=branch_id)
    agents = branch.agent_set.order_by('-date_added')
    context = {'branch': branch, 'agents': agents}
    return render(request, 'branch.html', context)


def agent(request, agent_id):
    """show branch and list agents"""
    agent1 = Agent.objects.get(id=agent_id)
    transactions = agent1.transaction_set.order_by('-date_added')
    context = {'transactions': transactions, 'agent': agent1}
    return render(request, 'agent.html', context)


def transaction(request, transaction_id):
    """show branch and list agents"""
    tran = Transaction.objects.get(id=transaction_id)
    context = {'transaction': tran}
    return render(request, 'transaction.html', context)


def agents(request):
    """show branch and list agents"""
    agent1 = Agent.objects.order_by('date_added')
    context = {'agents': agent1}
    return render(request, 'agents.html', context)


def branches(request):
    """show branch and list agents"""
    branches = Branch.objects.order_by('date_added')
    context = {'branches': branches}
    return render(request, 'branches.html', context)


def transactions(request):
    """show branch and list agents"""
    transactions = Transaction.objects.order_by('date_added')
    context = {'transactions': transactions}
    return render(request, 'transactions.html', context)


def new_branch(request):
    """Add a new branch."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BranchForm()
    else:
        # POST data submitted; process data.
        form = BranchForm(request.POST)
        if form.is_valid():
            new_branch = form.save(commit=False)
            new_branch.owner = request.user
            new_branch.save()
            return HttpResponseRedirect(reverse('main_app:branches'))

    context = {'form': form}
    return render(request, 'new_branch.html', context)


def new_agent(request, branch_id):
    """add new agent"""
    branch = Branch.objects.get(id=branch_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = AgentForm()
    else:
        # POST data submitted; process data.
        form = AgentForm(data=request.POST)
        if form.is_valid():
            new_agent = form.save(commit=False)
            new_agent.branch = branch
            new_agent.save()
            return HttpResponseRedirect(reverse('main_app:branch', args=[branch_id]))

    context = {'branch': branch, 'form': form}
    return render(request, 'new_agent.html', context)


def new_transaction(request, agent_id):
    """add new trans"""
    agent = Agent.objects.get(id=agent_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TransactionForm()
    else:
        # POST data submitted; process data.
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.agent = agent
            new_transaction.save()
            return HttpResponseRedirect(reverse('main_app:agent', args=[agent_id]))

    context = {'agent': agent, 'form': form}
    return render(request, 'new_transaction.html', context)


def edit_branch(request, branch_id):
    """Edit an existing branchy."""
    branch = Branch.objects.get(id=branch_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BranchForm(instance=branch)
    else:
        # POST data submitted; process data.
        form = BranchForm(instance=branch, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:branch', args=[branch_id]))

    context = {'branch': branch, 'form': form}
    return render(request, 'edit_branch.html', context)


def edit_agent(request, agent_id):
    """Edit an existing agent."""
    agent = Agent.objects.get(id=agent_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = AgentForm(instance=agent)
    else:
        # POST data submitted; process data.
        form = AgentForm(instance=agent, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:agent', args=[agent_id]))

    context = {'agent': agent, 'form': form}
    return render(request, 'edit_agent.html', context)


def edit_transaction(request, transaction_id):
    """Edit an existing agent."""
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TransactionForm(instance=transaction)
    else:
        # POST data submitted; process data.
        form = TransactionForm(instance=transaction, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:transaction', args=[transaction_id]))

    context = {'transaction': transaction, 'form': form}
    return render(request, 'edit_transaction.html', context)


def destroy_branch(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    branch.delete()
    return redirect('/')


def destroy_agent(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    agent.delete()
    return redirect('/')


def destroy_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    transaction.delete()
    return redirect('/')




