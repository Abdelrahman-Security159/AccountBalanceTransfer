from .models import Account
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    accounts = Account.objects.all()
    try:
        if len(accounts == 0):
            return render(request, '400.html')
    except Exception:
        return render(request, '400.html')
    accounts_sum = round(sum(Account.objects.values_list('balance', flat=True)))
    return render(request, 'index.html', {'accounts': accounts, 'accounts_sum': accounts_sum})

@csrf_exempt
def transfer(request):
    if request.method == 'POST':
        from_id = request.POST.get('source_account_id')
        account_id = request.POST.get('target_account_id')
        amount = float(request.POST.get('amount'))

        if round(amount) == 0:
            return JsonResponse({'success': False, 'message': 'You must enter a number.'})

        from_account = Account.objects.get(id=from_id)
        from_account_balance = from_account.balance
        if from_account_balance < amount:
            return JsonResponse({'success': False, 'message': 'Enter a valide balance.'})
        
        try:
            account = Account.objects.get(id=account_id)
            account.balance += amount
            account.save()

            from_account.balance -= amount
            from_account.save()

            return JsonResponse({'success': True, 'message': 'Transfer completed successfully.'})
        except Account.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Account not found.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    
def show(request, id):
    return render(request, 'show.html', {'account': Account.objects.get(account_id=id)})