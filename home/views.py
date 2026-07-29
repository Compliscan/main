from django.shortcuts import render
from django.http import HttpResponse
import platform
from . import supabase_service

def home(req):    
    context={
        "os":platform.system()
    }
    return render(req,"home.html",context)

def about(req):
    return render(req,"about.html")


def instructions(req):
    context={
            "os":platform.system()
        }
    return render(req,"instructions.html",context)

def func():
    return supabase_service.fetch_todos().data


async def test(req):
    res= HttpResponse(func())
    return res