from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Session, Viewer, Ticket
from .forms import BookingForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinemaapp/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    sessions = Session.objects.filter(movie=movie)
    return render(request, 'cinemaapp/movie_detail.html', {'movie': movie, 'sessions': sessions})

def session_list(request):
    sessions = Session.objects.select_related('movie').order_by('date', 'time')
    return render(request, 'cinemaapp/session_list.html', {'sessions': sessions})

def book_ticket(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Сохраняем данные зрителя
            viewer, created = Viewer.objects.get_or_create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email']
            )
            # Создаем билет
            Ticket.objects.create(
                viewer=viewer,
                session=session,
                seat_number=form.cleaned_data['seat_number']
            )
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'cinemaapp/book_ticket.html', {'form': form, 'session': session})

def booking_success(request):
    return render(request, 'cinemaapp/booking_success.html')

# Create your views here.
