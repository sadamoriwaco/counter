from django.shortcuts import render, redirect
from .models import Counter

def counter(request):
    counters = Counter.objects.all()
    return render(request, 'counter_app/counter.html', {'counters': counters})

def increment(request, counter_id):
    counter = Counter.objects.get(id=counter_id)
    if request.method == 'POST':
        if 'increment1' in request.POST:
            counter.count1 += 1
        elif 'increment2' in request.POST:
            counter.count2 += 1
        elif 'increment3' in request.POST:
            counter.count3 += 1
        elif 'increment4' in request.POST:
            counter.count4 += 1
        counter.save()
    return redirect('counter')

def reset(request, counter_id):
    counter = Counter.objects.get(id=counter_id)
    counter.count1 = 0
    counter.count2 = 0
    counter.count3 = 0
    counter.count4 = 0
    counter.save()
    return redirect('counter')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        new_counter = Counter(name=name)
        new_counter.save()
    return redirect('counter')

# counter_app/views.py

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Counter.objects.filter(name=name).exists():
            # 名前が既に存在する場合のエラー処理
            return redirect('counter')
        new_counter = Counter(name=name)
        new_counter.save()
    return redirect('counter')

# counter_app/views.py

def counter_detail(request, counter_id):
    counter = Counter.objects.get(id=counter_id)
    return render(request, 'counter_app/counter_detail.html', {'counter': counter})
