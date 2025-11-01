#api helps in accessing  resources via HTTP requests that someone else created
#step2
from fastapi import FastAPI #import FastAPI class from fastapi module
#assign an instance of FastAPI to a variable called app and initialize it with a title
#step3
app = FastAPI(title ="Grocery Store API")
#make this avilable to the world via HTTP requests
#step4
#endpoint-specific location
# @app.get("/catalog/tomatoes") #decorator to define an endpoint that listens for GET requests at the specified path
# #function that will be executed when a GET request is made to the /catalog/tomatoes endpoint
# def load_truck(order_qty):
#     return{
#         #create a dictionary to represent the response
#         "product": "tomatoes",
#         "units": catalog["tomatoes"]["units"],
#         "order_qty": order_qty
#     }
#  async def load_truck(order_qty):
#         return{
#             #create a dictionary to represent the response
#             "product": "wine",
#             "units": catalog["wine"]["units"],
#             "order_qty": order_qty
#         } 

@app.get("/warehouse/{product}")   
async def load_truck(product, order_qty,color):
    return{
        #create a dictionary to represent the response
        "product": product,
        "units": catalog[product]["units"],
        "order_qty": order_qty,
        "color": color
    }     
#step1
catalog={
    "tomatoes": {
        "units": "kg",
        "qty": 100
    },
    "wine": {
        "units": "bottles",
        "qty": 50
    }
}
