import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from model_bakery import baker
from students.models import Course, Student




@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def client():
    return APIClient()
@pytest.mark.django_db
def test_example(client, course_factory, student_factory):
    #arrange

    courses = course_factory(_quantity=10)
    students = student_factory(_quantity=10)



    #act

    responce = client.get('/courses/')


    #assert
    assert responce.status_code == 200
    data = responce.json()
    assert len(data)==len(courses)

    for i, item in enumerate(data):
        assert item['name']==courses[i].name

# проверка удаления курса
    total_before = len(courses)
    responce = client.delete('/courses/1/')
    assert responce.status_code == 204
    responce = client.get('/courses/')
    data = responce.json()
    assert total_before == (len(data)+1)







    #assert False, "Just test example"

@pytest.mark.django_db
def test_create_course(client):
    #User.objects.create_user('admin')
    responce = client.post('/courses/', data={'name': 'математика'})
    assert responce.status_code == 201


@pytest.mark.django_db
def test_create_student(client):
    #User.objects.create_user('admin')
    responce = client.post('/courses/', data={'name': 'петров'})
    assert responce.status_code == 201

