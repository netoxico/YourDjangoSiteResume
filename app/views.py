"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Ernesto Vargas',
    'bio' : 'Software Developer visitin from Mexico City :D',
    'email' : 'me@netoxico.com', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'netoxico', # No @ symbol, just the handle.
    'github_username' : "netoxico", 
    'headshot_url' : 'http://netoxico.com', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )