from django.shortcuts import render

from portfolio.models import Images, Info, Portfolio, Service, Skills

# Create your views here.
def index(request):
    personal_info=Info.objects.all().first()
    skills=Skills.objects.all()
    services=Service.objects.all()
    images_portfolio=Images.objects.all()
    portfolio=Portfolio.objects.all()
    context={
        "avatar_portfolio":portfolio,
        "images_portfolio":images_portfolio,
        "services":services,
        "skills":skills,
        "personal_info":personal_info,
    }
    return render(request,'pages/index.html',context)
def portfolio_detail(request,pk):
    portfolio=Portfolio.objects.get(id=pk)
    portfolio_img=Images.objects.filter(portfolio=portfolio)
    context={
        "portfolio_img":portfolio_img,
        "portfolio":portfolio,
    }
    return render(request,'pages/portfolio-details.html',context)