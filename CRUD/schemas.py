import pydantic
import datetime as dt
from typing import List

class PostBase(pydantic.BaseModel):
  title: str
  content: str

class PostCreate(PostBase):
  pass

class Post(PostBase):
  id: int
  owner_id: int
  date_created: dt.datetime
  date_last_updated: dt.datetime

  class Config:
    orm_mode= True

class UserBase(pydantic.BaseModel):
  email: str

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  is_active: bool
  posts: List[Post]= []

  class Config:
    orm_mode= True