from django.shortcuts import render
# Create your views here.

# def index4(request):
#     name = request.GET.get('name') or "world"
#     return render(request, 'bookmodule/index.html', {'name': name})

# def index2(request, val1=0): 
#     return render(request, 'bookmodule/index.html', {'val1': val1})

# def viewbook5(request, bookID):
#     book1 = {'id':123, 'title':'Python Programming', 'author':'John Doe'}
#     book2 = {'id':456, 'title':'Django for Beginners', 'author':'Jane Smith'}
#     target_book = None
#     if book1['id'] == bookID:
#         target_book = book1
#     if book2['id'] == bookID:
#         target_book = book2
#     context = {'book': target_book}
#     return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookID):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')