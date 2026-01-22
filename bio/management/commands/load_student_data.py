from django.core.management.base import BaseCommand
from datetime import date, timedelta
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from projects.models import Project


class Command(BaseCommand):
    help = 'Loads student data: clears existing data and creates new student portfolio data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Clear existing data
        Bio.objects.all().delete()
        Education.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        
        # Create Bio
        self.stdout.write('Creating Bio...')
        bio = Bio.objects.create(
            name="Muhammed Rehan Atique",
            job_title="Web Developer & CS Student",
            professional_description="Aspiring developer with a passion for Django and Python."
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Created Bio: {bio.name}'))
        
        # Create Education
        self.stdout.write('Creating Education...')
        # Assuming BS started 4 years ago and is ongoing
        start_date = date.today() - timedelta(days=4*365)
        education = Education.objects.create(
            degree_title="BS Computer Science",
            institution="UMT",
            start_date=start_date,
            end_date=None,  # Ongoing
            description="Pursuing Bachelor's degree in Computer Science with focus on web development and software engineering."
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Created Education: {education.degree_title} at {education.institution}'))
        
        # Create Skills
        self.stdout.write('Creating Skills...')
        skills_data = [
            {"name": "Django", "proficiency": 85, "category": "Technical"},
            {"name": "Python", "proficiency": 90, "category": "Technical"},
            {"name": "HTML/CSS", "proficiency": 80, "category": "Technical"},
        ]
        
        for skill_data in skills_data:
            skill = Skill.objects.create(**skill_data)
            self.stdout.write(self.style.SUCCESS(f'✓ Created Skill: {skill.name} ({skill.proficiency}%)'))
        
        # Create Project
        self.stdout.write('Creating Project...')
        project = Project.objects.create(
            title="Term Project",
            description="Portfolio website using Django MVT.",
            technology_used="Django, SQLite",
            link=None  # Optional field
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Created Project: {project.title}'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ All student data loaded successfully!'))
        self.stdout.write(self.style.WARNING('\nNote: Image fields (profile_picture and project image) have been left blank.'))
        self.stdout.write(self.style.WARNING('You can add images through the Django admin panel.'))
