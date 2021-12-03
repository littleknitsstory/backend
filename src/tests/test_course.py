import json

import pytest
from moneyed import Money, Currency

from src.apps.course.models import Course

pytestmark = pytest.mark.django_db

def test_course_model_str():
    course = Course(name='Test Course', price=Money(100, 'EUR'))
    assert str(course) == 'Test Course'
    
def test_course_model_json():
    course = Course(name='Test Course', price=Money(100, 'EUR'))
    assert json.loads(course.json()) == {
        'id': None,
        'name': 'Test Course',
        'price': 100,
        'currency': 'EUR',
        'created_at': None,
        'updated_at': None,
    }
    
def test_course_model_json_with_id():
    course = Course(name='Test Course', price=Money(100, 'EUR'))
    course.id = 1
    assert json.loads(course.json()) == {
        'id': 1,
        'name': 'Test Course',
        'price': 100,
        'currency': 'EUR',
        'created_at': None,
        'updated_at': None,
    }

def  test_step_model_json():
    course = Course(name='Test Course', price=Money(100, 'EUR'))
    assert json.loads(course.json()) == {
        'id': None,
        'name': 'Test Course',
        'price': 100,
        'currency': 'EUR',
        'created_at': None,
        'updated_at': None,
    }