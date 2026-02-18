from dataclasses import dataclass


@dataclass
class Client:
    id: int
    name: str
    age: int
    email: str
    isWalkIn: bool = False

    def __str__(self) -> str:
        client_type = "Walk-in" if self.isWalkIn else "Regular"
        return f"{self.name} (ID: {self.id}, {client_type})"


class HotelManager:
    def __init__(self) -> None:
        self.rooms: list[Client] = []
        self.restaurant_reservations: list[Client] = []

    def add_client(self, client: Client) -> None:
        self.rooms.append(client)

    def remove_client(self, client: Client) -> None:
        self.rooms = [current_client for current_client in self.rooms if current_client.id != client.id]

    def add_reservation(self, client: Client) -> list[Client]:
        total_reservations = len(self.restaurant_reservations)
        regular_reservations = sum(1 for reserved in self.restaurant_reservations if not reserved.isWalkIn)
        walk_in_reservations = sum(1 for reserved in self.restaurant_reservations if reserved.isWalkIn)

        if client.isWalkIn:
            if total_reservations < 6 and walk_in_reservations < 2:
                print(f"Adding walk-in reservation for client: {client}")
                self.restaurant_reservations.append(client)
            else:
                print(f"No available slots for walk-in reservations for client: {client}")
        else:
            if total_reservations < 6 and regular_reservations < 4:
                print(f"Adding reservation for client: {client}")
                self.restaurant_reservations.append(client)
            else:
                print(f"No available slots for reservations for client: {client}")

        return self.restaurant_reservations


def main() -> None:
    print("Hello from py-hotel-example!")

    hotel_manager = HotelManager()

    client1 = Client(id=1, name="John Doe", age=30, email="john.doe@example.com", isWalkIn=False)
    client2 = Client(id=2, name="Jane Smith", age=25, email="jane.smith@example.com", isWalkIn=False)
    client3 = Client(id=3, name="Bob Johnson", age=40, email="bob.johnson@example.com", isWalkIn=False)
    client4 = Client(id=4, name="Alice Brown", age=35, email="alice.brown@example.com", isWalkIn=False)
    client5 = Client(id=5, name="Charlie Davis", age=28, email="charlie.davis@example.com", isWalkIn=False)
    client6 = Client(id=6, name="Eve Wilson", age=22, email="eve.wilson@example.com", isWalkIn=True)
    client7 = Client(id=7, name="Frank Miller", age=45, email="frank.miller@example.com", isWalkIn=True)
    client8 = Client(id=8, name="Grace Lee", age=32, email="grace.lee@example.com", isWalkIn=True)

    hotel_manager.add_client(client1)
    hotel_manager.add_client(client2)
    hotel_manager.add_client(client3)
    hotel_manager.add_client(client4)
    hotel_manager.add_client(client5)

    print()
    print("Current clients in the hotel:")
    for client in hotel_manager.rooms:
        print(client)

    print()
    hotel_manager.remove_client(client1)

    print()
    print("Clients after removing one:")
    for client in hotel_manager.rooms:
        print(client)

    print()
    hotel_manager.add_reservation(client1)
    hotel_manager.add_reservation(client2)
    hotel_manager.add_reservation(client3)
    hotel_manager.add_reservation(client4)
    hotel_manager.add_reservation(client6)
    hotel_manager.add_reservation(client7)
    hotel_manager.add_reservation(client5)
    hotel_manager.add_reservation(client8)


if __name__ == "__main__":
    main()
