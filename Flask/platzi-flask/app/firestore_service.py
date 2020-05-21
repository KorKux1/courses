import os

import firebase_admin

from firebase_admin import  credentials, firestore


project_id = os.environ['PROJECT_ID']

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
    'projectId': project_id
})


db = firestore.client()


""""USERS METHODS"""

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})



""""TODO METHODS"""

def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()

def todo_put(user_id, description):
    todo_collection_ref = db.collection('users').document(user_id).collection('todos')
    todo_collection_ref.add({'description':description, 'done': False})

def todo_deleate(user_id, todo_id):
    todo_ref = db.document(f'users/{user_id}/todos/{todo_id}')
    todo_ref.delete()
    # todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
