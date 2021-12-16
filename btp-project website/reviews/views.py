from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
from .models import Review
from django .utils import timezone

def search(request):
    if request.method == 'POST':
        if request.POST['search']:
            if request.POST['dropdown']=='Latest_reviews':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('-id')
                return render(request, 'reviews/allreviews.html',{'review':review})
            elif request.POST['dropdown']=='Oldest_reviews':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('id')
                return render(request, 'reviews/allreviews.html',{'review':review})
            elif request.POST['dropdown']=='Oldest_devices':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('-buy_date')
                return render(request, 'reviews/allreviews.html',{'review':review})
            elif request.POST['dropdown']=='Latest_devices':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('buy_date')
                return render(request, 'reviews/allreviews.html',{'review':review})
            elif request.POST['dropdown']=='Rating':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('-rating')
                return render(request, 'reviews/allreviews.html',{'review':review})
            elif request.POST['dropdown']=='Votes':
                review = Review.objects.filter(appliance=request.POST['search']).order_by('-votes_total')
                return render(request, 'reviews/allreviews.html',{'review':review})
        else:
            return render(request, 'reviews/allreviews.html')
    else:
        return render(request, 'reviews/allreviews.html')

def allreviews(request):
    review = Review.objects.order_by('-id')
    return render(request, 'reviews/allreviews.html',{'review':review})

@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        if request.POST['model'] and request.POST['body'] and request.POST['buy_date'] and request.POST['appliance'] and request.FILES['image'] and request.POST['rating']:
            review = Review()
            review.title = request.user.username
            review.body = request.POST['body']
            review.appliance = request.POST['appliance']
            review.buy_date = request.POST['buy_date']
            review.model = request.POST['model']
            review.image = request.FILES['image']
            review.pub_date = timezone.datetime.now()
            review.hunter = request.user
            review.rating=request.POST['rating']
            review.save()
            return redirect('/reviews/' + str(review.id))
        else:
            return render(request, 'reviews/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'reviews/create.html')

@login_required(login_url="/accounts/login")
def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/detail.html',{'review':review})

@login_required(login_url="/accounts/login")
def upvote(request, review_id):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=review_id)
        review.votes_total += 1
        review.save()
        return redirect('/reviews/' + str(review.id))
