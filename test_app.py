import pytest
from app import app
from flask import url_for
from flask_wtf import csrf

def test_home():
    with app.test_client() as client, app.app_context():
        app.config['WTF_CSRF_ENABLED'] = False

        response = client.get(url_for('home'))
        assert response.status_code == 200
        assert b'Cannot calculate BMI' not in response.data
        assert b'Your BMI is' not in response.data

        response = client.post('/', data={
            'feet': '5', 
            'inches': '10', 
            'pounds': '150',
        })
        assert response.status_code == 200
        assert b'Cannot calculate BMI' not in response.data
        assert b'Your BMI is 22.0' in response.data
        assert b'Your BMI category is Normal weight' in response.data

        response = client.post('/', data={
            'feet': '6',
            'inches': '3',
            'pounds': '260',
        })
        assert response.status_code == 200
        assert b'Cannot calculate BMI' not in response.data
        assert b'Your BMI is 33.3' in response.data
        assert b'Your BMI category is Obese' in response.data

        response = client.post('/', data={
            'feet': '0', 
            'inches': '0', 
            'pounds': '0',
        })
        assert response.status_code == 200
        assert b'Height must be positive' in response.data
        assert b'Weight must be positive' in response.data
        assert b'Your BMI is' not in response.data

