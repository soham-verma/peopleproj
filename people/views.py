from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *

def index_view(request):
    return render(request, 'index.html')


def person_list_view(request):
    # Filtering and searching
    label_id = request.GET.get('label')
    query = request.GET.get('q', '')

    people = Person.objects.all()

    if label_id:
        people = people.filter(labels__id=label_id)
    
    if query:
        people = people.filter(name__icontains=query)
        
    # Optional: Add ordering, e.g. by name
    people = people.order_by('name')

    context = {
        'people': people,
        'query': query,
        'label_id': label_id,
        'labels': Label.objects.all()
    }
    return render(request, 'person_list.html', context)


def person_detail_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'person_detail.html', {'person': person})


def label_list_view(request):
    labels = Label.objects.all().order_by('name')
    form = LabelForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('label_list')

    return render(request, 'label_list.html', {'labels': labels, 'form': form})


def label_detail_view(request, pk):
    label = get_object_or_404(Label, pk=pk)
    people_with_label = label.people.all()  # Fetch people associated with the label

    return render(request, 'label_detail.html', {
        'label': label,
        'people_with_label': people_with_label
    })



def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        formset = LinkFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            person = form.save(commit=False)
            person.save()

            # Handle existing labels
            person.labels.set(form.cleaned_data['labels'])

            # Handle custom label
            custom_label = form.cleaned_data.get('custom_label')
            if custom_label:
                label, created = Label.objects.get_or_create(name=custom_label.strip())
                person.labels.add(label)

            links = formset.save(commit=False)
            for link in links:
                link.person = person
                link.save()
            formset.save()
            return redirect('person_list')
    else:
        form = PersonForm()
        formset = LinkFormSet()

    return render(request, 'person_form.html', {'form': form, 'formset': formset, 'title': 'Add Person'})



def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        formset = LinkFormSet(request.POST, instance=person)
        if form.is_valid() and formset.is_valid():
            person = form.save(commit=False)
            person.save()

            # Handle existing labels
            person.labels.set(form.cleaned_data['labels'])

            # Handle custom label
            custom_label = form.cleaned_data.get('custom_label')
            if custom_label:
                label, created = Label.objects.get_or_create(name=custom_label.strip())
                person.labels.add(label)

            links = formset.save(commit=False)
            for link in links:
                link.person = person
                link.save()
            formset.save()
            return redirect('person_detail', pk=pk)
    else:
        form = PersonForm(instance=person, initial={'labels': person.labels.all()})
        formset = LinkFormSet(instance=person)

    return render(request, 'person_form.html', {'form': form, 'formset': formset, 'title': f'Edit {person.name}'})



def person_delete_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_confirm_delete.html', {'person': person})
