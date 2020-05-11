from django.http import HttpResponse
from app1.models import Article
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    return HttpResponse('Hello world,新的界面')

#内容
def acticle_content(request):
    article = Article.objects.all()[1]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s ,brief_content: %s ,content: %s ,article_id %s ,publish_date: %s ' % (
        '&nbsp' + title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)

#分页
def show_templates(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('page',page)
    article = Article.objects.all()
    pageinator = Paginator(article,8)
    page_num = pageinator.num_pages
    print('pageinator',pageinator.num_pages)
    pagelsit = pageinator.page(page)
    if pagelsit.has_next():
        next_page = page+1
    else:
        next_page = page
    if pagelsit.has_previous():
        previous_page = page-1
    else:
        previous_page = page
    return render(request, 'blog/show.html', {'articles': pagelsit,
                                              'page_num':range(1,page_num+1),
                                              'curr_page':page,
                                              'next_page':next_page,
                                              'previous_page':previous_page})


def show_bloginfo(request, article_id):
    all_article = Article.objects.all()  # 取出所有文章
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
    # for article in all_article:
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    # return render(request, 'blog/show_info.html', {'bloginfo': curr_article,
    #                                                'section_list': section_list
    #                                                })


    return render(request, 'blog/show_info.html', {'bloginfo': curr_article,
                                                   'section_list': section_list,
                                                   'previous_article': previous_article,
                                                   'next_article': next_article})
def image_info(request):
    return render(request,'blog/img.html')