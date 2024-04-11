# Dokumentacja projektu "Lista zadań"

## 1. Temat projektu aplikacji:

Projekt Todo App to aplikacja webowa służąca do zarządzania listą zadań do wykonania.

## 2. Opis projektu:

Projekt ma na celu umożliwienie użytkownikom dodawania, edycji, usuwania oraz oznaczania zadań jako wykonane. Aplikacja
zapewnia prosty interfejs użytkownika, który umożliwia efektywne zarządzanie codziennymi obowiązkami.

## 3. Wymagania funkcjonalne i niefunkcjonalne:

- Funkcjonalności:
    - Dodawanie nowych zadań.
    - Edycja istniejących zadań.
    - Usuwanie zadań.
    - Oznaczanie zadań jako wykonane.
- Wymagania niefunkcjonalne:
    - Aplikacja powinna być szybka i responsywna.
    - Interfejs użytkownika powinien być intuicyjny i przyjazny dla użytkownika.
    - Aplikacja powinna być łatwa w utrzymaniu i rozbudowie.

## 4. Odbiorcy:

Docelową grupą użytkowników są osoby potrzebujące prostego narzędzia do zarządzania codziennymi zadaniami.

## 5. Schematy i modele:

W projekcie użyto architektury FastAPI do obsługi zapytań HTTP oraz szablonów HTML do prezentacji interfejsu
użytkownika. Dane przechowywane są w pamięci podręcznej w formie listy zadań.

## 6. Dokumentacja API, UI:

- API:
    - `POST /todos`: Endpoint do dodawania nowego zadania. Przyjmuje tytuł nowego zadania i zwraca dodane zadanie.
    - `PUT /todos/{todo_id}`: Endpoint do aktualizacji istniejącego zadania. Przyjmuje identyfikator zadania oraz stan
      wykonania, a następnie zwraca zaktualizowane zadanie.
    - `DELETE /todos/{todo_id}`: Endpoint do usuwania istniejącego zadania. Przyjmuje identyfikator zadania i usuwa je.
- UI:
    - Interfejs użytkownika umożliwia dodawanie, edycję, usuwanie oraz oznaczanie zadań jako wykonane.
    - Umożliwia wygodną interakcję użytkownika z aplikacją za pomocą przeglądarki internetowej.

## 7. Uzasadnienie wyboru technologii:

- FastAPI: Wybrano FastAPI ze względu na jego wydajność oraz łatwość tworzenia interfejsów API. FastAPI oferuje
  wbudowane wsparcie dla asynchroniczności, co pozwala na obsługę wielu żądań jednocześnie, co jest kluczowe dla
  aplikacji webowych.
- Jinja2Templates: Szablony HTML zostały wybrane ze względu na ich elastyczność i możliwość tworzenia dynamicznych stron
  internetowych. Jinja2Templates oferuje prostą i efektywną metodę tworzenia szablonów opartych na Pythonie.

## 8. Dodatkowe elementy:

- Wykorzystano bibliotekę Pydantic do walidacji danych
- Aplikacja korzysta z biblioteki Bootstrap do stylizacji interfejsu użytkownika
- Użyte biblioteki zewnętrzne obejmują FastAPI, pydantic, oraz fastapi_htmx do obsługi dynamicznych interakcji w
  interfejsie użytkownika.
