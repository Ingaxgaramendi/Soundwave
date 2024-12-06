from iu.menu import show_menu
from database.data import events
from models.event_models import create_event, read_event, update_event, delete_event, buy_ticket
from utils.validators import validate_name

def main():
    while True:
        show_menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            read_event(events)
        elif choice == '2':
            event_id = input("Ingrese el ID del evento para ver los detalles: ")
            read_event(events, event_id)
        elif choice == '3':
            event_id = input("Ingrese el ID del nuevo evento: ")
            name = input("Ingrese el nombre del evento: ")
            date = input("Ingrese la fecha del evento: ")
            price = input("Ingrese el precio del evento: ")
            new_event = {"id": event_id, "name": name, "date": date, "price": float(price)}
            create_event(events, new_event)
        elif choice == '4':
            event_id = input("Ingrese el ID del evento que desea actualizar: ")
            updated_name = input("Ingrese el nuevo nombre del evento: ")
            updated_date = input("Ingrese la nueva fecha del evento: ")
            updated_price = input("Ingrese el nuevo precio del evento: ")
            updated_data = {"name": updated_name, "date": updated_date, "price": float(updated_price)}
            update_event(events, event_id, updated_data)
        elif choice == '5':
            event_id = input("Ingrese el ID del evento a eliminar: ")
            delete_event(events, event_id)
        elif choice == '6':
            print("¡Gracias por usar SoundWave!")
            break
        elif choice == '7':
            event_id = input("Ingrese el ID del evento para comprar entradas: ")
            name = input("Ingrese su nombre: ")
            surname = input("Ingrese su apellido: ")
            try:
                if validate_name(name) and validate_name(surname):
                    buy_ticket(events, event_id, name, surname)
                else:
                    print("❌ Nombre o apellido inválido. Intente de nuevo.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
