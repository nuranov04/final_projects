from django.shortcuts import redirect, render
from comment.models import CommentUniversity, CommentCity


# def updateCityComment(request, id):
#     comment = CommentCity.objects.get(id=id)
#     if request.method == "POST":
#         text = request.POST.get('text')
#         comment.save()
#         return redirect('index')
#     return render(request, 'comment/city_update.html', locals())


def deleteCityComment(request, id):
    comment = CommentCity.objects.get(id=id)
    if request.method == "POST":
        comment.delete()
        return redirect("index")
    return render(request, 'comment/city_delete.html', locals())



def deleteUniversityComment(request, id):
    comment = CommentUniversity.objects.get(id=id)
    if request.method == "POST":
        comment.delete()
        return redirect('index')
    return render(request, 'comment/university_delete.html', locals())

# def updateUniversityComment(request, id):
#     comment = CommentUniversity.objects.get(id=id)
#     if request.method == "POST":
#         text = request.POST.get('text')
#         comment.save()
#         return redirect('index')
#     return render(request, 'comment/university_update.html', locals())

