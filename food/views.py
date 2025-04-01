from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#anmysite
#class based view
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    context={
        'item_list':Item,
    }
#above method in class base of same
def index(request):
    item = Item.objects.all()
    template = loader.get_template('food/index.html')
    context={
        'item_list':item,
    } #will retuening this context to template it will contain variables for template in the from this json object
    return HttpResponse(template.render(context,request))
    #return HttpResponse('Hello world')



#class based view
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
#above method in class base of same
def detail(request,pass_data):
    #this pass_data is coming from web site web.com/pass_data 
    #we have configured this in url tab for food/<int:pass_data> pass dat will strored request vale in integer
    item = Item.objects.get(pk=pass_data)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context) #short cut responseve as above index fun

#class based view
class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'
 
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
#above method in class base of same
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    else:
        print("form is invalid")
    return render(request, 'food/item-form.html', {'form' : form})




#FUNTION BASED VIEW
def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    else:
        print("form is invalid")
    return render(request, 'food/item-form.html', {'form' : form ,'item' : item})
    

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item' : item})