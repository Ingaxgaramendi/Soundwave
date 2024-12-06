def create_event(events, new_event):
    """Añade un nuevo evento."""
    events.append(new_event)
    print(f"✅ Evento {new_event['name']} agregado con éxito.")

def read_event(events, event_id=None):
    """Muestra todos los eventos o uno específico por ID."""
    if event_id:
        event = next((e for e in events if e["id"] == event_id), None)
        if event:
            print(f"🎟️ ID: {event['id']} | Nombre: {event['name']} | Fecha: {event['date']} | Precio: ${event['price']}")
            return event
        else:
            print("❌ No se encontró un evento con ese ID.")
            return None
    else:
        print("\n🎫 Lista de Eventos:")
        for event in events:
            print(f"- ID: {event['id']} | Nombre: {event['name']} | Fecha: {event['date']} | Precio: ${event['price']}")
        return events

def update_event(events, event_id, updated_data):
    """Actualiza un evento existente."""
    event = next((e for e in events if e["id"] == event_id), None)
    if event:
        event.update(updated_data)
        print(f"✅ Evento {event_id} actualizado con éxito.")
    else:
        print(f"❌ No se encontró el evento con ID {event_id}.")

def delete_event(events, event_id):
    """Elimina un evento por ID."""
    event = next((e for e in events if e["id"] == event_id), None)
    if event:
        events.remove(event)
        print(f"✅ Evento {event_id} eliminado con éxito.")
    else:
        print(f"❌ No se encontró el evento con ID {event_id}.")

def buy_ticket(events, event_id, name, surname):
    """Permite comprar entradas para un evento."""
    event = next((e for e in events if e["id"] == event_id), None)
    if event:
        print(f"🎫 ¡Compra exitosa para {name} {surname}!")
        print(f"Detalles del evento: {event['name']} - Fecha: {event['date']} - Precio: ${event['price']}")
    else:
        print(f"❌ No se encontró el evento con ID {event_id}.")