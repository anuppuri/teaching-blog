from django.shortcuts import render, redirect

from .models import Category, Blog


# Create your views here.

def homepage(request):
    context = {
        'categories': Category.objects.order_by('title'),
        'blogs': Blog.objects.order_by('pub_date')[:5]
    }
    return render(request, 'index.html', context)


def category(request, category_slug):
    cat = Category.objects.get(slug=category_slug)
    print(cat)
    context = {'categories': Category.objects.order_by('title'),
               'blogs': cat.blog_set.order_by('-pub_date'),
               'category': cat
               }

    return render(request, 'category.html', context)


def blog(request, blog_slug):
    blg = Blog.objects.get(slug=blog_slug)
    print(blg)
    context = {
        'categories': Category.objects.order_by('title'),
        'blog': blg
    }
    return render(request, 'blog.html', context)


def search(request):
    if request.GET.get('q'):
        context = {
            'categories': Category.objects.order_by('title'),
            'blogs': Blog.objects.filter(title__icontains=request.GET.get('q'))
        }
        return render(request, 'search.html', context)

    return redirect('/')
