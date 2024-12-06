import unittest
from models.event_models import create_event, read_event, update_event, delete_event, buy_ticket
from database.data import events
from utils.validators import validate_name

class TestSoundWaveCRUD(unittest.TestCase):

    def test_create_event(self):
        """Prueba la creación de un nuevo evento."""
        new_event = {"id": "104", "name": "Concierto Pop", "date": "2024-12-15", "price": 20}
        create_event(events, new_event)
        self.assertEqual(len(events), 4)  # Debe haber 4 eventos después de agregar uno nuevo
        self.assertEqual(events[-1]['id'], "104")  # Verifica que el ID sea el mismo

    def test_read_event(self):
        """Prueba la lectura de un evento por ID."""
        event = read_event(events, "101")
        self.assertIsNotNone(event)  # Debe encontrar el evento con ID 101
        self.assertEqual(event['name'], "Concierto de Rock")  # Verifica que el nombre coincida

    def test_update_event(self):
        """Prueba la actualización de un evento."""
        updated_data = {"name": "Concierto de Metal", "date": "2024-12-20", "price": 28}
        update_event(events, "101", updated_data)
        updated_event = read_event(events, "101")
        self.assertEqual(updated_event['name'], "Concierto de Metal")  # El nombre debe haberse actualizado
        self.assertEqual(updated_event['date'], "2024-12-20")  # La fecha debe haberse actualizado

    def test_delete_event(self):
        """Prueba la eliminación de un evento."""
        delete_event(events, "102")
        event = read_event(events, "102")
        self.assertIsNone(event)  # El evento con ID 102 ya no debe existir

    def test_buy_ticket_valid(self):
        """Prueba la compra de un ticket con datos válidos."""
        name = "Juan"
        surname = "Perez"
        valid_name = validate_name(name)
        valid_surname = validate_name(surname)
        self.assertTrue(valid_name)  # El nombre debe ser válido
        self.assertTrue(valid_surname)  # El apellido debe ser válido
        buy_ticket(events, "103", name, surname)  # Simula la compra de un ticket para el evento con ID 103

    def test_buy_ticket_invalid(self):
        """Prueba la compra de un ticket con datos inválidos."""
        name = "Juan123"  # Nombre con números, no válido
        surname = "Perez!"
        invalid_name = validate_name(name)
        invalid_surname = validate_name(surname)
        self.assertFalse(invalid_name)  # El nombre debe ser inválido
        self.assertFalse(invalid_surname)  # El apellido debe ser inválido

if __name__ == "__main__":
    unittest.main()
