# -*- coding: utf-8 -*-
#Activity 1

#The domain classes
import json
class Product:
    def __init__(self,name,EAN_id,price=0,quantity=0,brand=None):
        self.Name=name
        self.Price=price    
        self.Quantity=quantity
        self.EAN_ID=EAN_id
        self.Brand=brand
    
    def to_json(self):
        product_dict={'Name':self.Name,'Price':self.Price,
                      'Quantity':self.Quantity,'EAN_identitfier':self.EAN_ID,
                      'Brand':self.Brand}
        product_json=json.loads(json.dumps(product_dict))
        return(product_json)
    
    def get_name(self):
        return(self.Name)
    def get_price(self):
        return(self.Price)
    def get_quantity(self):
        return(self.Quantity)
    def get_ean(self):
        return(self.EAN_ID)
    def get_brand(self):
        return(self.Brand)
    def set_quantity(self,quantity):
        self.Quantity=quantity
        
    
class Clothing(Product):
    def __init__(self,name,EAN_id,price=0,quantity=0,brand=None,size=None,material=None):
        super().__init__(name,EAN_id,price,quantity,brand)
        self.Size=size
        self.Material=material
        
    def to_json(self):
        product_dict={'Type':'Clothing','Name':self.Name,'Price':self.Price,
                      'Quantity':self.Quantity,'EAN_identitfier':self.EAN_ID,
                      'Brand':self.Brand,'Size':self.Size,'Material':self.Material}
        product_json=json.loads(json.dumps(product_dict))
        return(product_json)
    
    def get_size(self):
        return(self.Size)
    def get_material(self):
        return(self.Material)

class Food(Product):
    def __init__(self,name,EAN_id,price=0,quantity=0,brand=None,expiry_date=None,gluten_free=None,suitable_for_vegans=None):
        super().__init__(name,EAN_id,price,quantity,brand)
        self.Expiry_date=expiry_date
        self.Gluten_free=gluten_free
        self.Suitable_for_vegans=suitable_for_vegans
        
    def to_json(self):
        product_dict={'Type':'Food','Name':self.Name,'Price':self.Price,
                      'Quantity':self.Quantity,'EAN_identitfier':self.EAN_ID,
                      'Brand':self.Brand,'Expiry_date':self.Expiry_date,
                      'Gluten_free':self.Gluten_free,
                      'Suitable_for_vegans':self.Suitable_for_vegans}
        product_json=json.loads(json.dumps(product_dict))
        return(product_json)
    
    def get_expiry_date(self):
        return(self.Expiry_date)
    def get_gluten_free(self):
        return(self.Gluten_free)
    def get_suitable_for_vegans(self):
        return(self.Suitable_for_vegans)
        

class Cosmetics(Product):
    def __init__(self,name,EAN_id,price=0,quantity=0,brand=None,suitable_for_sensitive_skin=None,expiry_date=None,color=None):
        super().__init__(name,EAN_id,price,quantity,brand)
        self.Suitable_for_sensitive_skin=suitable_for_sensitive_skin
        self.Expiry_date=expiry_date
        self.Color=color
        
    def to_json(self):
        product_dict={'Type':'Cosmetics','Name':self.Name,'Price':self.Price,
                      'Quantity':self.Quantity,'EAN_identitfier':self.EAN_ID,
                      'Brand':self.Brand,'Suitable_for_sensitive_skin':self.Suitable_for_sensitive_skin,
                      'Expiry_date':self.Expiry_date,'Color':self.Color}
        product_json=json.loads(json.dumps(product_dict))
        return(product_json)
    
    def get_suitable_for_sensitive_skin(self):
        return(self.Suitable_for_sensitive_skin)
    def get_expiry_date(self):
        return(self.Expiry_date)
    def get_color(self):
        return(self.Color)
        

#Shopping system
class ShoppingCart:
    def __init__(self,*cart):
        #check every item in *cart valid
        #check no repeat item in *cart？
        self.__Cart=list(cart)
            
    def addProduct(self,p):
    #check p valid
    #check p not in cart,else invoke changeProductQuantity？
        self.__Cart.append(p)
    

    def removeProduct(self,p):
    #check p in the cart
        self.__Cart.remove(p)

    
    def showSummary(self):
        json_cart=map(lambda x: x.to_json(),self.__Cart)
        print(list(json_cart))
        
    
    def changeProductQuantity(self,p,q):
        #check q>=0
        #check p in cart, else invoke addProduct
        index=self.__Cart.index(p)
        self.__Cart[index].set_quantity(q)

    def get_cart(self):
        return(self.__Cart)
       
 
         
#Doing some shopping
#suppose all attributes cannot be none
#suppose all different items need different EAN (items can have the same name)
#suppose the same items(all attributes except EAN and quantity are the same) cannot have different EAN
#suppose the name of items and brand of items are unsensitive to the capitalization
#the following functions check whether the input is valid
def check_none(attribute):
    #check name, brand, size, material, color is not none
    #set the format of those attribute to title and no ' ' before and after
    '''
    there are many ways to specify those attributes, 
    so here do not restrict them to a specific format and take all string valid
    '''
    while True:
        p_attribute=input("Insert its {}:".format(attribute)).strip(' ').title()
        if p_attribute =='C': #'C' then break the loop and the outer loop
            print("The current operation is cancelled.")
            break #break this loop, no return, so the value of this function is none
        elif p_attribute not in ['','None']:
            return(p_attribute)
            break
        else:
            print("invalid {}, Insert its {}:".format(attribute,attribute))

def check_TF(attribute):
    #check gulten_free,suitable_for_vegans,suitable_for_sensitive_skin is True or False
    while True:
        p_attribute=input("Insert its {}:".format(attribute)).strip(' ').title()
        if p_attribute =='C':
            print("The current operation is cancelled.")
            break
        elif p_attribute in ['True','False']:
            return(p_attribute)
            break
        else:
            print("invalid {}, Insert True/False as its {}:".format(attribute,attribute))
           
    
def get_Price():
    #check whether price is a postive number 
    while True:
        p_price=input('Insert its price (£):').strip(' ')
        if p_price.title() =='C':
            print("The current operation is cancelled.")
            break
        else:
            try:
                float(p_price)#check number
                if float(p_price)>0:#check postive
                    return(p_price)
                    break
                else:
                    print('invalid price, Insert a postive number as its price (£)')
            except:
                print('invalid price, Insert a postive number as its price (£)')
 
def get_Quantity():
    #check whether quantity is a postive int
    while True:
        p_quantity=input('Insert its quantity:').strip(' ')
        if p_quantity.title() =='C':
            print("The current operation is cancelled.")
            break
        else:
            try:
                int(p_quantity)#check int
                if int(p_quantity)>0: #check positive
                    return(p_quantity)
                    break
                else:
                    print('invalid quantity, Insert a possitive int as its quantity')
            except:
                print('invalid quantity, Insert a positive int as its quantity')

def get_EAN(cart):
    #check whether EAN is 13-digit and unique!!
    #also the same item cannot have different EAN (this will be checked later when user invoke A)
    while True:
        p_EAN=input('Insert its EAN code:').strip(' ')
        if p_EAN.title()=='C':
            print("The current operation is cancelled.")
            break
        else:
            try:
                int(p_EAN)#check int
                check_cart=[x.get_ean() for x in cart.get_cart()]
                if len(p_EAN)==13 and p_EAN not in check_cart: #check 13 digit and unqiue
                    return(p_EAN)
                    break
                else:
                    print('invalid EAN code,Insert a unique 13 digit (EAN code) for differenet items:')
            except:
                print('invalid EAN code,Insert a unique 13 digit (EAN code) for differenet items:')

import time      
def get_Expiry_date():#test date is date format and is not before today
    while True:
        p_expiry_date=input('Insert its expiry date(YYYY-MM-DD):').strip(' ')
        if p_expiry_date.title() =='C':
            print("The current operation is cancelled.")
            break
        else:
            try:
                time.strptime(p_expiry_date, "%Y-%m-%d")#check time format
                present_time=time.strftime("%Y-%m-%d")
                if p_expiry_date>=present_time:#check the date is not before today
                    return(p_expiry_date)
                    break
                else:
                    print('invalid date, Insert YYYY-MM-DD not before today as its expiry date:')
            except:
                print('invalid date, Insert YYYY-MM-DD not before today as  its expiry date:')

    
#make a new object:
def make_objects(cart):
    while True:
        class_name=input('Insert its type:').strip(' ').title()
        if class_name =='C':
            print("The current operation is cancelled.")
            break
        
        elif class_name in ['Product','Clothing','Food','Cosmetics']:
            obj_name=check_none('name')
            if obj_name==None:#when input='C' no return,obj_name=None, then break the outer loop 
                break
            obj_EAN_id=get_EAN(cart)
            if obj_EAN_id==None:
                break
            obj_price=get_Price()
            if obj_price==None:
                break
            obj_quantity=get_Quantity()
            if obj_quantity==None:
                break
            obj_brand=check_none('brand')
            if obj_brand==None:
                break
            
            if class_name=='Product':
                obj=Product(obj_name,obj_EAN_id,obj_price,obj_quantity,obj_brand)
            elif class_name=='Clothing':
                obj_size=check_none('size')
                if obj_size==None:
                    break
                obj_material=check_none('material')
                if obj_material==None:
                    break
                obj=Clothing(obj_name,obj_EAN_id,obj_price,obj_quantity,obj_brand,obj_size,obj_material)
            elif class_name=='Food':
                obj_expiry_date=get_Expiry_date()
                if obj_expiry_date==None:
                    break
                obj_gluten_free=check_TF('gluten_free')
                if obj_gluten_free==None:
                    break
                obj_suitable_for_vegans=check_TF('suitable_for_vegans')
                if obj_suitable_for_vegans==None:
                    break 
                obj=Food(obj_name,obj_EAN_id,obj_price,obj_quantity,obj_brand,obj_expiry_date,obj_gluten_free,obj_suitable_for_vegans)
            else:
                obj_suitable_for_sensitive_skin=check_TF('suitable_for_sensitive_skin')
                if obj_suitable_for_sensitive_skin==None:
                    break 
                obj_expiry_date=get_Expiry_date()
                if obj_expiry_date==None:
                    break 
                obj_color=check_none('color')
                if obj_color==None:
                    break 
                obj=Cosmetics(obj_name,obj_EAN_id,obj_price,obj_quantity,obj_brand,obj_suitable_for_sensitive_skin,obj_expiry_date,obj_color)
            return(obj)
            break
        else:
            print('Please input a valid type: Clothing,Food,Cosmetics,Product(for other type of product)')
  
 
        

import re
print('The program has started.')
print('Insert your next command (H for help):')
terminated = False
your_cart=ShoppingCart()
while not terminated:
    c = input("Type your next command:").strip(' ').upper() 
    if c not in ['A','R','S','Q','E','C','T','H']:#test if c is valid
        print('Command not recognised. Please try again')
    else:
        if c =='T':
            terminated = True
        
        elif c=='H':
            print('The program supports the following commands:')
            print(' [A] - Add a new product to the cart')
            print(' [R] - Remove a product from the cart')
            print(' [S] - Print a summary of the cart')
            print(' [Q] - Change the quantity of a product')
            print(' [E] - Export a JSON version of the cart')
            print(' [C] - Cancel the current operation')
            print(' [T] - Terminate the program')
            print(' [H] - List the supported commands')
                
        elif c=='A': 
            print(' Adding a new product:')
            p=make_objects(your_cart)
            if p!=None:
                #check if the same product(all other attributes except EAN and quantity are the same) have different EAN
                #if true ask user invoke Q or invoke A and add a different item, else add
                pattern1=re.compile(r"'Quantity': '\d+',") #sub quantity:  with ' '
                pattern2=re.compile(r"'EAN_identitfier': '\d+',")#sub EAN_identitfier: with ' '
                p_check=re.sub(pattern1,"",str(p.to_json()))
                p_check=re.sub(pattern2,"",p_check)
                cart_check=[re.sub(pattern1,"",str(x.to_json())) for x in your_cart.get_cart()]
                cart_check=[re.sub(pattern2,"", x) for x in cart_check]
                if p_check in cart_check:
                    print("Invalid EAN code, the product is already in your cart and has different EAN code")
                    print("Please invoke Q function to change its quantity or A function to add a different item")
                else:
                    your_cart.addProduct(p)
                    print('The product {} has been added to the cart.'.format(p.get_name()))
                    cart_len=len(your_cart.get_cart())
                    if cart_len>1:
                        print('The cart contains {} products.'.format(cart_len))
                    else:
                        print('The cart contains {} product.'.format(cart_len))
              
        elif c=='R':
            obj_del=input('What is the name of the product you want to remove? ').strip(' ').title()
            if obj_del=='C':
                print("The current operation is cancelled.")
            else:
                obj_list=[x.get_name() for x in your_cart.get_cart()]
                #check if the obj is in the cart
                if obj_list.count(obj_del)==1: #when only one product has this name delete it
                    index=obj_list.index(obj_del)
                    your_cart.removeProduct(your_cart.get_cart()[index])
                    print('\'{}\' successfully removed from the cart.'.format(obj_del))
                    cart_len=len(your_cart.get_cart())
                    if cart_len>1:
                        print('The cart contains {} products.'.format(cart_len))
                    else:
                        print('The cart contains {} product.'.format(cart_len))
                elif obj_list.count(obj_del)>1:#when more than one product has this name ask for EAN_id
                    obj_del_choose=input('There are more than one product have this name, specify its EAN_id: ').strip(' ')
                    if obj_del_choose.title()=='C':
                        print("The current operation is cancelled.")
                    else:
                        obj_list_choose=[x.get_ean() for x in your_cart.get_cart()]
                        find=False
                        for x in your_cart.get_cart():
                            if x.get_name()==obj_del and x.get_ean()==obj_del_choose:
                                index=obj_list_choose.index(obj_del_choose)
                                your_cart.removeProduct(your_cart.get_cart()[index])
                                print('\'{}\' with EAN_id {} successfully removed from the cart.'.format(obj_del,obj_del_choose))
                                find=True
                                break
                        if find==False:
                            print('\'{}\' with EAN_id {} is not in the cart.'.format(obj_del,obj_del_choose))    
                else:
                    print('\'{}\' is not in the cart.'.format(obj_del))
        
        elif c=='S':
            print('This is the total of the expenses:')
            cart_list=your_cart.get_cart()
            total_price=0
            for i in range(1,len(cart_list)+1):
                obj=cart_list[i-1]
                price=int(obj.get_quantity())*float(obj.get_price())
                total_price+=price
                if int(obj.get_quantity())==1:
                    print(' {} - {} = £{}'.format(i,obj.get_name(),price))
                else:
                    print(' {} - {} * {} = £{}'.format(i,obj.get_quantity(),obj.get_name(),price)) 
            print(' Total = £{}'.format(total_price))
            
        elif c=='Q':
            obj_change=input('Insert the product you want to change quantity: ').strip(' ').title()
            if obj_change=='C':
                print("The current operation is cancelled.")
            else:
                obj_list=[x.get_name() for x in your_cart.get_cart()]
                #check if the obj is in the cart
                if obj_list.count(obj_change)==1: #when only one product has this name change its quantity
                    new_q=get_Quantity()#restrict the input value to positive int, if input=0, the customer should invoke remove
                    if new_q!=None:
                        new_q=int(new_q)
                        index=obj_list.index(obj_change)
                        your_cart.changeProductQuantity(your_cart.get_cart()[index],new_q)
                        print('Successfully change the quantity of {} to {}.'.format(obj_change,new_q))
                elif obj_list.count(obj_change)>1:#when more than one product has this name ask for EAN_id
                    obj_change_choose=input('There are more than one product have this name, specify its EAN_id: ').strip(' ')
                    if obj_change_choose.title()=='C':
                        print("The current operation is cancelled.")
                    else:
                        obj_list_choose=[x.get_ean() for x in your_cart.get_cart()]
                        find=False
                        for x in your_cart.get_cart():
                            if x.get_name()==obj_change and x.get_ean()==obj_change_choose:
                                new_q=get_Quantity()
                                if new_q!=None:
                                    new_q=int(new_q)
                                    index=obj_list_choose.index(obj_change_choose)
                                    your_cart.changeProductQuantity(your_cart.get_cart()[index],new_q)
                                    print('Successfully change the quantity of {} with EAN_id {} to {}.'.format(obj_change,obj_change_choose,new_q))
                                    find=True
                                    break
                        if find==False:
                            print('\'{}\' with EAN_id {} is not in the cart.'.format(obj_change,obj_change_choose))   
                else:
                    print('{} is not in the cart.'.format(obj_change))
            
        elif c=='E':
            your_cart.showSummary()
         
        elif c=='C':
            print("The current operation is cancelled.")
            
            
print( 'Goodbye.' )

