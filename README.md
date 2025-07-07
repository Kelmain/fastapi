# FastAPI Task Manager

## Description
API REST pour la gestion d'une liste de tâches (CRUD) avec FastAPI et Pydantic.

## Fonctionnalités
- Afficher la liste des tâches (`GET /tasks/`)
- Ajouter une tâche (`POST /tasks/`)
- Modifier une tâche (`PUT /tasks/{id}`)
- Supprimer une tâche (`DELETE /tasks/{id}`)
- Marquer une tâche comme terminée (`PATCH /tasks/{id}/complete`)
- Trier les tâches par statut ou par titre

## Structure du projet
```
app/
  ├── __init__.py
  ├── main.py
  ├── routes/
  │   ├── __init__.py
  │   └── tasks.py
  ├── schemas.py
  └── database.py
```

## Installation et exécution
1. Installez les dépendances :
   ```sh
   pip install fastapi uvicorn
   ```
2. Lancez le serveur :
   ```sh
   uvicorn app.main:app --reload
   ```
3. Accédez à la documentation interactive :
   - Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)

## Exemple de requête
```json
{
  "title": "Acheter du pain",
  "description": "Aller à la boulangerie",
  "completed": false
}
```

## Dépôt GitLab
Publiez ce projet sur votre dépôt GitLab avec un historique de commits clair.
