from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.filter():
            reviews.append(review.review_text) 
            reviews.append(review.name_text) 
            reviews.append(review.email_text) 
            reviews.append(review.number_text)
        return Response({'reviews': reviews})
 

class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data['review']
        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        if review == '' or name == '' or email == '' or number == '':
            return Response(({'message': 'failure'}))

        else:
           new_database_entry = Review(review_text=review, name_text=name, email_text=email, number_text=number)
           new_database_entry.save()
           return Response(({'message': 'success'}))