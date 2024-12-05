from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import housing,food,shopping,travelling,health,school,socialservice,entertainment,busines,bank,budgetplanning
from django.db.models import Sum
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def get_date_filter(from_date, to_date, field_name='date'):
    filters = Q()
    if from_date:
        filters &= Q(**{f"{field_name}__gte": from_date})
    if to_date:
        filters &= Q(**{f"{field_name}__lte": to_date})
    return filters

# Create your views here. 
def index(request):
    template = loader.get_template('Home/index.html')  # Manually load the template
    context = {}  # Optional: Add any context data if needed
    return HttpResponse(template.render(context, request))

@login_required
def Visualization(request):
    user = request.user

    from_date = request.GET.get('fromDate')
    to_date = request.GET.get('toDate')

    expense_filters = Q()
    if from_date:
        expense_filters &= Q(date__gte=from_date)
    if to_date:
        expense_filters &= Q(date__lte=to_date)
    # Calculate income and expenses
    housing_expenses = housing.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    food_expenses = food.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    shopping_expenses = shopping.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    travelling_expenses = travelling.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    entertainment_expenses = entertainment.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    healthcare_expenses = health.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    schooling_expenses = school.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    business_expenses = busines.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    socialservice_expenses=socialservice.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0

    total_expenses = business_expenses+healthcare_expenses+schooling_expenses+housing_expenses + food_expenses + shopping_expenses + travelling_expenses + entertainment_expenses
    income = 10000  # Replace with actual query for user income
    print("total_expenses : ",total_expenses)
    print("housing_expenses : ",housing_expenses)
    print("food_expenses : ",food_expenses)
    print("shopping_expenses : ",shopping_expenses)
    print("travelling_expenses : ",travelling_expenses)
    print("entertainment_expenses : ",entertainment_expenses)
    print("healthcare_expenses : ",healthcare_expenses)
    print("schooling_expenses : ",schooling_expenses)
    print("business_expenses : ",business_expenses)
    print("socialservice_expenses : ",socialservice_expenses)
    
    print("from_date : ",from_date)
    print("to_date : ",to_date)

    context = {
        'income': income,
        'expenses': total_expenses,
    }
    return render(request, 'Home/Visualization.html', context)


@login_required
def get_expenses(request):
    user = request.user
    from_date = request.GET.get('fromDate')
    to_date = request.GET.get('toDate')

    expense_filters = Q()
    if from_date:
        expense_filters &= Q(date__gte=from_date)
    if to_date:
        expense_filters &= Q(date__lte=to_date)

    # Calculate expenses
    data = {
        'housing_expenses': housing.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'food_expenses': food.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'shopping_expenses': shopping.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'travelling_expenses': travelling.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'entertainment_expenses': entertainment.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'healthcare_expenses': health.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'schooling_expenses': school.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'business_expenses': busines.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0,
        'socialservice_expenses':socialservice.objects.filter(expense_filters).aggregate(total=Sum('total'))['total'] or 0
    }
    return JsonResponse(data)


def Login(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect to index if user is already logged in
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        print(f"Username: {username}, Password: {password}")

        if username and password:
            user = authenticate(request, username=username, password=password)
            print(f"user:{user}")
            
            if user is not None:
                login(request, user)  # Logs the user in
                messages.success(request, 'successfully logined in')
                return redirect('index')  # Redirect to the homepage or another page after successful login
                
            else:
                messages.error(request, 'Invalid username or password')  # Display error message
                return render(request, 'Home/Login.html')
        else:
            messages.error(request, 'Please provide both username and password')  # Display error message
            return render(request, 'Home/Login.html')
    else:
        return render(request, 'Home/Login.html')


def Logout(request):
    list(messages.get_messages(request)) 
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')

def Register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 == password2:
            if User.objects.filter(username=fullname).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=fullname, email=email, password=password1)
                user.save()
                login(request, user)  # Automatically log the user in after registration
                messages.success(request, 'You have successfully registered')
                return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'Home/Registration.html')

def save_expense_data(model, user, data, request, template):
    if any(data.values()):  # Check if any value is not empty or zero
        instance = model(user=user, **data)
        try:
            instance.save()
            messages.success(request, 'Data saved successfully!')
        except Exception as e:
            messages.error(request, f'Error saving data: {e}')
    else:
        messages.warning(request, 'No data to save!')
    return render(request, template)


def house(request):
    if request.method == 'POST':
        try:
            data = {
                'rent' : float(request.POST.get('rent', 0) or 0.0),
                'electricity' : float(request.POST.get('electricity', 0) or 0.0),
                'water' : float(request.POST.get('water', 0) or 0.0),
                'gas' : float(request.POST.get('gas', 0) or 0.0),
                'sewage' : float(request.POST.get('sewage', 0) or 0.0),
                'internet' : float(request.POST.get('internet', 0) or 0.0),
                'insurance' : float(request.POST.get('insurance', 0) or 0.0),
                'tax' : float(request.POST.get('tax', 0) or 0.0),
                'repairs' : float(request.POST.get('repairs', 0) or 0.0),
                'furnishings' : float(request.POST.get('furnishings', 0) or 0.0),
                'security' : float(request.POST.get('security', 0) or 0.0),
                'other' : float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(housing, request.user, data, request, "Home/Housing.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")# Handle potential conversion errors
    return render(request, "Home/Housing.html")

def foodmodel(request):
    if request.method == 'POST':
        try:
            data={
                'fresh' : float(request.POST.get('fresh', 0) or 0.0),
                'meat' : float(request.POST.get('meat', 0) or 0.0),
                'sweets' : float(request.POST.get('sweets', 0) or 0.0),
                'fast' : float(request.POST.get('fast', 0) or 0.0),
                'dairy' : float(request.POST.get('dairy', 0) or 0.0),
                'beverages' : float(request.POST.get('beverages', 0) or 0.0),
                'restaurants' : float(request.POST.get('restaurants', 0) or 0.0),
                'pet' : float(request.POST.get('pet', 0) or 0.0),
                'other' : float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(food, request.user, data, request,"Home/food.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request, "Home/food.html")

def shoppingmod(request):
    if request.method == 'POST':
        try:
            data={
                'clothes' : float(request.POST.get('clothes', 0) or 0.0),
                'access' : float(request.POST.get('access', 0) or 0.0),
                'beauty' : float(request.POST.get('beauty', 0) or 0.0),
                'electronics' : float(request.POST.get('electronics', 0) or 0.0),
                'homeacs' : float(request.POST.get('homeacs', 0) or 0.0),
                'sports' : float(request.POST.get('sports', 0) or 0.0),
                'toys' : float(request.POST.get('toys', 0) or 0.0),
                'other' : float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(shopping, request.user, data, request, "Home/shopping.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request, "Home/shopping.html")

def travelmodel(request):
    if request.method == 'POST':
        try:
            data={
                'transportation' : float(request.POST.get('transportation', 0) or 0.0),
                'accommodation' : float(request.POST.get('accommodation', 0) or 0.0),
                'insurance' : float(request.POST.get('insurance', 0) or 0.0),
                'visa' : float(request.POST.get('visa', 0) or 0.0),
                'other' : float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(travelling, request.user, data, request, "Home/travelling.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request, "Home/travelling.html")

def healthmod(request):
    if request.method=='POST':
        try:
            data={
                'medicines' :float(request.POST.get('medicines', 0) or 0.0),
                'mental':float(request.POST.get('mental', 0) or 0.0),
                'physical':float(request.POST.get('physical', 0) or 0.0),
                'insurance':float(request.POST.get('insurance', 0) or 0.0),
                'other':float(request.POST.get('other', 0) or 0.0),
                }
            return save_expense_data(health, request.user, data, request, "Home/healthcare.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request,"Home/healthcare.html")

def schooling(request):
    if request.method=='POST':
        try:
            data={
                'fee':float(request.POST.get('fee', 0) or 0.0),
                'supplies':float(request.POST.get('supplies', 0) or 0.0),
                'uniforms':float(request.POST.get('uniforms', 0) or 0.0),
                'transportation':float(request.POST.get('transportation', 0) or 0.0),
                'enrichment':float(request.POST.get('enrichment', 0) or 0.0),
                'other':float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(school, request.user, data, request, "Home/schooling.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request,"Home/schooling.html")

def businesmod(request):
    if request.method=='POST':
        try:
            data={
                'operational':float(request.POST.get('operational', 0) or 0.0),
                'employ':float(request.POST.get('employ', 0) or 0.0),
                'adv':float(request.POST.get('adv', 0) or 0.0),
                'sales':float(request.POST.get('sales', 0) or 0.0),
                'other':float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(busines, request.user, data, request, "Home/busines.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request,"Home/busines.html")

def social(request):
    if request.method=='POST':
        try:
            data={
                'program':float(request.POST.get('program', 0) or 0.0),
                'staff':float(request.POST.get('staff', 0) or 0.0),
                'operational':float(request.POST.get('operational', 0) or 0.0),
                'donation':float(request.POST.get('donation', 0) or 0.0),
                'transportation':float(request.POST.get('transportation', 0) or 0.0),
                'legal':float(request.POST.get('employ', 0) or 0.0),
                'subsidies':float(request.POST.get('subsidies', 0) or 0.0),
                'health':float(request.POST.get('health', 0) or 0.0),
                'other':float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(socialservice, request.user, data, request, "Home/social.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request,"Home/social.html")

def enter(request):
    if request.method=='POST':
        try:
            data={
                'movie':float(request.POST.get('movie', 0) or 0.0),
                'music':float(request.POST.get('music', 0) or 0.0),
                'sports':float(request.POST.get('sports', 0) or 0.0),
                'gaming':float(request.POST.get('gaming', 0) or 0.0),
                'book':float(request.POST.get('book', 0) or 0.0),
                'hobby':float(request.POST.get('hobby', 0) or 0.0),
                'event':float(request.POST.get('event', 0) or 0.0),
                'other':float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(entertainment, request.user, data, request, "Home/entertainment.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request,"Home/entertainment.html")

def Budget(request):
    return render(request,"Home/Budget.html")

def sample(request):
    return render(request,"Home/sample.html")

def expense_tracking(request):
    return render(request,"Home/expense_tracking.html")

@login_required
def budget_planning(request):
    if request.method == 'POST':
        try:
            data={
                'income' : float(request.POST.get('income', 0) or 0.0),
                'housing' : float(request.POST.get('housing', 0) or 0.0),
                'food' : float(request.POST.get('food', 0) or 0.0),
                'shopping' : float(request.POST.get('shopping', 0) or 0.0),
                'travelling' : float(request.POST.get('travelling', 0) or 0.0),
                'entertainment' : float(request.POST.get('entertainment', 0) or 0.0),
                'health' : float(request.POST.get('health', 0) or 0.0),
                'school' : float(request.POST.get('school', 0) or 0.0),
                'busines' : float(request.POST.get('busines', 0) or 0.0),
                'socialservice' : float(request.POST.get('socialservice', 0) or 0.0),
                'other' : float(request.POST.get('other', 0) or 0.0),
            }
            return save_expense_data(budgetplanning, request.user, data, request, "Home/budget_panning.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
    return render(request, "Home/budget_panning.html")

def banking(request):
    if request.method=='POST':
        try:
            data={
                'bank_name':request.POST.get("bank_name",""),
                'account_number':request.POST.get("account_number",""),
                'ifsc_code':request.POST.get("ifsc_code",""),
                'userid':request.POST.get("userid",""),
                'account_type':request.POST.get("account_type",""),
                'branch_nam':request.POST.get("branch_name",""),
                'holder':request.POST.get("holder",""),
                'swift':request.POST.get("swift",""),
            }
            return save_expense_data(bank, request.user, data, request, "Home/Banking.html")
        except ValueError as e:
            messages.error(request, f"Error in data format: {e}")
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
    return render(request, "Home/Banking.html")