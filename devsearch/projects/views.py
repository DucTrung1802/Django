from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        "userId": "101",
        "id": "1",
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
    },
    {
        "userId": "202",
        "id": "2",
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
    },
    {
        "userId": "303",
        "id": "3",
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
    },
]


def projects(request):
    page = "projects"
    number = 10
    context = {"page": page, "number": number, "projects": projectList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i["id"] == pk:
            projectObj = i
    return render(request, "projects/single_project.html", {"project": projectObj})
