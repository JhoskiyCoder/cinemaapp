from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Session, Viewer, Ticket
from .forms import BookingForm
from django.core.mail import send_mail
def movie_list(request):
    movies = Movie.objects.all()

    query = request.GET.get('q')
    genre = request.GET.get('genre')

    if query:
        movies = movies.filter(title__icontains=query)

    if genre:
        movies = movies.filter(genre=genre)

    # Получим список уникальных жанров для формы
    genres = Movie.objects.values_list('genre', flat=True).distinct()

    return render(request, 'cinemaapp/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'selected_genre': genre,
        'search_query': query,
    })

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    sessions = Session.objects.filter(movie=movie)
    return render(request, 'cinemaapp/movie_detail.html', {'movie': movie, 'sessions': sessions})

def session_list(request):
    sessions = Session.objects.select_related('movie').order_by('date', 'time')
    return render(request, 'cinemaapp/session_list.html', {'sessions': sessions})

def book_ticket(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    taken_seats = Ticket.objects.filter(session=session).values_list('seat_number', flat=True)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            viewer, created = Viewer.objects.get_or_create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email']
            )
            Ticket.objects.create(
                viewer=viewer,
                session=session,
                seat_number=form.cleaned_data['seat_number']
            )

            subject = 'Подтверждение бронирования'
            message = f"""
            Здравствуйте, {viewer.name}!

            Вы успешно забронировали билет:
            Фильм: {session.movie.title}
            Дата: {session.date}
            Время: {session.time}
            Место: {form.cleaned_data['seat_number']}

            Спасибо за бронирование!
            """
            send_mail(subject, message, None, [viewer.email])
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'cinemaapp/book_ticket.html', {
        'form': form,
        'session': session,
        'taken_seats': list(taken_seats)
    })

def booking_success(request):
    return render(request, 'cinemaapp/booking_success.html')

def movie_sessions(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    sessions = Session.objects.filter(movie=movie).order_by('date', 'time')
    return render(request, 'cinemaapp/movie_sessions.html', {'movie': movie, 'sessions': sessions})

# Create your views here.
