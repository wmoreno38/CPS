# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:02:24 2024

@author: yxg084228
"""

# test_app.py
import unittest
from app import app

class TitanicAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        response = self.app.post('/predict', json=[{
            'Pclass': 3,
            'Age': 22,
            'SibSp': 1,
            'Parch': 0
        }])
        print(response.data)  # Imprime el contenido de la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json[0], [0, 1])

    def test_batch_predict(self):
        response = self.app.post('/batch_predict', json=[
            {'Pclass': 3, 'Age': 22, 'SibSp': 1, 'Parch': 0},
            {'Pclass': 1, 'Age': 38, 'SibSp': 1, 'Parch': 0}
        ])
        print(response.data)  # Imprime el contenido de la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

if __name__ == '__main__':
    unittest.main()

