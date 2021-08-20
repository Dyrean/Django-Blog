from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hiking-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Dyrean",
        "date": date(2021, 8, 20),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est architecto
            quae quidem natus odio accusantium placeat eum eaque, quo tenetur
            consectetur sint unde non aspernatur, facere fuga labore quis sequi!
            '''
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Dyrean",
        "date": date(2021, 8, 18),
        "title": "Programming Is Great",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est architecto
            quae quidem natus odio accusantium placeat eum eaque, quo tenetur
            consectetur sint unde non aspernatur, facere fuga labore quis sequi!
            '''
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Dyrean",
        "date": date(2021, 8, 22),
        "title": "Nature At Its Best",
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "content": '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Est architecto
            quae quidem natus odio accusantium placeat eum eaque, quo tenetur
            consectetur sint unde non aspernatur, facere fuga labore quis sequi!
            '''
    }
]
# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key = lambda x: x['date'])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")