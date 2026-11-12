# from fastapi import FastAPI
# from pydantic import BaseModel
# class Item(BaseModel):
#     name:str
#     description:str | None = None
#     price:float
#     tax:float |None = None
# app = FastAPI()
# @app.post('/items/')
# async def create_item(item:Item):
#     return item

import random

from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Annotated
from pydantic import AfterValidator
class Item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float |None = None
app = FastAPI()
# @app.post('/items/')
# async def create_item(item:Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price+item.tax
#         item_dict.update({'price_with_tax':price_with_tax})
#     return item_dict
# @app.get('/items/{item_id}')
# async def update_item(item_id:int,item:Item,q:str | None = None):
#     result = {'item_id':item_id,**item.model_dump()}
#     if q:
#         result.update({'q':q})
#     return result
#查询参数
# @app.get('/items/')
# async def read_items(q:Annotated[str | None,Query(max_length=5)] = None):
#     results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
#     if q:
#         results.update({'q':q})
#     return results
# @app.get('/items/')
# async def read_items(q:Annotated[list[str],Query()] = ['foo','bar']):
#     query_items = {'q':q}
#     return query_items
# @app.get('/items/')
# async def read_items(
#     q:Annotated[str|None,Query(title='Query string',min_length=3,alias = 'item_query',deprecated=True)] = None
# ):
#     results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
#     if q:
#         results.update({'q':q})
#     return results
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}
def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id
@app.get('/items/')
async def read_items(
    id:Annotated[str|None,AfterValidator(check_valid_id)] = None
):
    if id:
        item = data.get(id)
    else:
        id,item = random.choice(list(data.items()))
    return {'id':id,'name':item}