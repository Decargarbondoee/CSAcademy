from datetime import datetime, timedelta
import json
from flask import request
from flask_jwt_extended import (
    get_jwt,
    get_jwt_identity,
    jwt_required
)
from flask_restful import Resource
from app.models import Tasks
from app.schemas.task import TaskSchema

task_schema = TaskSchema()

class TaskResource(Resource):
    @classmethod
    def post(cls):
        task = task_schema.load(request.get_json())
        
        task.save_to_db()

        return {"message": "Task created successfully."}, 201
