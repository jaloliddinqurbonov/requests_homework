"""
Task 5: Create a Utility Module

Goal:
- Organize all your request functions into a reusable module.

Module requirements:
- Filename: api_client.py
- Contains all previous functions:
  - get_post_data(post_id)
  - safe_get_post(post_id)
  - create_post(title, body, user_id)
  - get_comments_by_post(post_id, limit=3)
- All functions should be properly documented with docstrings
- The module should handle imports appropriately

Your implementation below:
"""
import requests
import json

def get_post_data(post_id):
  post_id=int(input('idni kriting '))
  response=requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
  data=response.json()
  return data

def safe_get_post(post_id):
  post_id=int(input('id ni krit lanati '))
  post_data=requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
  response=post_data.status_code
  if response==200:
    return ({"success":True,"data":post_data.json()})
  else:
    return ({"succes":False,"massege":"Filed to get data"})


def create_post(title, body, user_id):
  dict={
  "title": title,
  "body": body,
  "userId": user_id,
  "id": 102
  }
  post_data=requests.post("https://jsonplaceholder.typicode.com/posts",json=dict)
  return post_data.json()

# Your implementation here
