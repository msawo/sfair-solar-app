from django.template.defaultfilters import slugify
import datetime
from django.shortcuts import render, redirect
from collection.forms import ProfileForm
from collection.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    return render(request, 'index.html', {
        'profiles': profiles,
    })


@login_required
def profile_detail(request, slug):
    # grab the object...
    profile = Profile.objects.get(slug=slug)

    if profile.user != request.user:
        raise Http404
    # and pass to the template
    return render(request, 'profiles/profile_detail.html', {
        'profile': profile,
    })

@login_required
def edit_profile(request, slug):
    # grab the object...
    profile = Profile.objects.get(slug=slug)

    # make sure the logged in user is the owner of the panel
    if profile.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = ProfileForm

    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        # and apply to form
        form = form_class(data=request.POST, instance=profile)
        if form.is_valid():
            # save the new form
            form.save()
            return redirect('profile_detail', slug=profile.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=profile)

    # and render the template
    return render(request, 'profiles/edit_profile.html', {
        'profile': profile,
        'form': form,
    })

def create_my_solar(request):
    form_class = ProfileForm
    # if coming from a submitted form, do this
    if request.method == 'POST':
        # grab data submitted & apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            profile = form.save(commit=False)
            # set the additional details
            profile.user = request.user
            profile.slug = slugify(profile.name)
            # save the object
            profile.save()
            # redirect to the newly created panel
            return redirect('profile_detail', slug=profile.slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'profiles/create_my_solar.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        profiles = Profile.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        profiles = Profile.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'profiles': profiles,
        'initial': initial,
    })
