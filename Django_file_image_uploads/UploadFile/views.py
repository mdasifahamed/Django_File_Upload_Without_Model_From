from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from UploadFile.models import Uploads
import re



def home(request):
    h_temp = loader.get_template('home.html')

    return HttpResponse(h_temp.render())

@csrf_exempt
def uploads(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('image')
        photo_name = photo.name.replace(" ","")
        upload_handle = FileSystemStorage()
        uploaded_file = upload_handle.save(photo_name,photo)
        file_url = upload_handle.url(uploaded_file)
        print(name,photo)
        profile = Uploads(
            name = name,
            img_path = file_url,
        )
        profile.save()
        resp = {
            'status':"success",
        }
        return JsonResponse(resp)

    else:
        return HttpResponse("Make It Perfect")

def after_upload(request):

    s_temp = loader.get_template('success.html')
    data = Uploads.objects.order_by("id").last()

    context ={
        'data':data,
    }

    return HttpResponse(s_temp.render(context,request))

def all_data(request):



    all = Uploads.objects.all()
    a_temp = loader.get_template('all.html')
    context = {
        'datas':all,
    }

    return HttpResponse(a_temp.render(context,request))


@csrf_exempt
def search(request):
    d_temp = loader.get_template("search.html")
    check = 0
    if request.method =='POST':

        id = int(request.POST.get('id'))

        try:
            data = Uploads.objects.get(id=id)
            check = 1
            context = {
            'data':data,
            'check':check
        }
            return HttpResponse(d_temp.render(context,request))

        except Uploads.DoesNotExist:
            data = None
            check = 0
            context = {
            'data':data,
            'check':check
        }
            return HttpResponse(d_temp.render(context,request))
        
    else:
        return HttpResponse(d_temp.render())  



@csrf_exempt
def update(request):
    up_id = int(request.POST.get('up_id'))
    data = Uploads.objects.get(id=up_id)
    image_file = data.img_path
    image_file = image_file.removeprefix('/media/')
    print(image_file)
    up_temp = loader.get_template('update.html')
    contex ={
        'data':data,
    }
    return HttpResponse(up_temp.render(contex,request))

@csrf_exempt
def updated(request):
    a_f_u_temp = loader.get_template('after_delete_photo.html')
    up_id = int(request.POST.get('up_id'))
    img = request.FILES.get('update_pic')
    img_name = img.name.replace(" ","")
    data= Uploads.objects.get(id=up_id)
    file_handle = FileSystemStorage()
    delete_file = FileSystemStorage()
    file = file_handle.save(img_name,img)
    file_url = file_handle.url(file)
    old_img = data.img_path
    if old_img == "":
        data.img_path = file_url
        data.save()
        print(data.img_path)
    elif old_img != "":
        old_img = old_img.removeprefix('/media/')
        data.img_path = file_url
        data.save()
        delete_file.delete(old_img)
    else:
        data.img_path = old_img
        data.save()
        delete_file.delete(img.name)
        print(data.img_path)  

    context = {
        'data':data
    } 
    
    return HttpResponse(a_f_u_temp.render(context,request))

    
        

    




@csrf_exempt
def delete_photo_temp(request):
    del_t = loader.get_template('delete.html')
    if request.method == 'POST':
        delp_id = int(request.POST.get('delp_id'))
        
        data = Uploads.objects.get(id = delp_id)
        context  = {
            'data':data,
        }
        return HttpResponse(del_t.render(context,request))      

@csrf_exempt
def delete(request):
    a_d_temp = loader.get_template('after_delete_photo.html')
    file_h = FileSystemStorage()

    if request.method == 'POST':
        del_id = int(request.POST.get('delet_id'))
        print(type(del_id))
        data = Uploads.objects.get(id=del_id)
        print(data.img_path)
        old_img = data.img_path
        old_img = old_img.removeprefix('/media/')
        print(old_img)
        file_h.delete(old_img)
        data.img_path = ""
        print(data.img_path)
        data.save()
        context ={
            'data':data
        }
        return HttpResponse(a_d_temp.render(context,request))




@csrf_exempt
def delete_profile_temp(request):
    con_d_temp = loader.get_template('confirm_delete_profile.html')
    if request.method=='POST':
        dl_p_id = int(request.POST.get('del_id'))
        data = Uploads.objects.get(id=dl_p_id)
        context = {
            'data':data,
        }

        return HttpResponse(con_d_temp.render(context,request))

@csrf_exempt
def delete_profile(request):
    af_d_p_temp = loader.get_template('after_profile_delete.html')
    file_handle = FileSystemStorage()
    if request.method=='POST':
        p_id = int(request.POST.get('p_id'))
        data = Uploads.objects.get(id = p_id)
        check = data.img_path
        if check == "":
            data.delete()
            print("image path is empty")
        else:
            file_name = check.removeprefix('/media/')
            file_handle.delete(file_name)
            data.delete()

        return HttpResponse(af_d_p_temp.render())

def id(request):
    # latest_id = Uploads.objects.latest('id').id
    # data = Uploads.objects.get(id=latest_id) 
    # print(latest_id)

    # print('/n')
    
    # print(data.name)
    # print(data.img_path)
    # # fs = FileSystemStorage()
    # # name = '12_1fgn4u0.PNG'
    # # fs.delete(name)
    # # data.delete()
    # s = data.img_path
    # file_name = s.removeprefix('/media/')
    # print(file_name)
    # print(type(file_name))
    # fs = FileSystemStorage()
    # fs.delete(file_name)
    # data.delete()

    file_h = FileSystemStorage()

    file_h.delete('Photo of Md Asif Ahamed.jpg')
    return HttpResponse("check terminal")
