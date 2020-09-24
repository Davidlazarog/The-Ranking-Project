
from src.app import app
from src.config import PORT
import src.controller.lab_controller
import src.controller.student_controller


app.run("0.0.0.0", PORT, debug=True)