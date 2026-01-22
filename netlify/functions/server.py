import os
import sys
from pathlib import Path

# Add the project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

def handler(event, context):
    """Netlify serverless function handler for Django"""
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as RunserverCommand
    
    # This is a simplified handler - for production, consider using a proper WSGI adapter
    # For now, we'll use a basic approach
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': 'Django app is running'
    }
