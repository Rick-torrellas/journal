from src.infrastructure.repositories import InMemoryActivityRepository
from src.application.ports import RegisterActivity


if __name__ == "__main__":
    # main.py
# Inyección de dependencias
    repo = InMemoryActivityRepository()
    use_case = RegisterActivity(repo)
# Ejecución
    new_activity = use_case.execute("Inception", "Movie")
    print(f"Registrado: {new_activity.title} con ID {new_activity.id}")
