# tasks/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from tasks.models import Priority, Category, Task, SubTask, Note
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **options):
        fake = Faker()

        # 1. Manually add record to Priority and Category
        default_priorities = ['high', 'medium', 'low', 'critical', 'optional']
        for name in default_priorities:
            Priority.objects.get_or_create(name=name)

        default_categories = ['Work', 'School', 'Personal', 'Finance', 'Projects']
        for name in default_categories:
            Category.objects.get_or_create(name=name)

        # Fetch existing priorities and categories for foreign key assignment
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        # 2. Generate fake Tasks
        num_tasks = 50 # Adjust as needed
        for _ in range(num_tasks):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5)[:-1], # Remove the trailing period
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]), # Use random_element
                deadline=timezone.make_aware(fake.date_time_this_month()), # Use timezone.make_aware
                priority=random.choice(priorities),
                category=random.choice(categories)
            )

            # 3. Generate fake SubTasks for each Task
            num_subtasks = random.randint(0, 5) # Each task gets 0 to 5 subtasks
            for _ in range(num_subtasks):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4)[:-1], # Remove the trailing period
                    description=fake.paragraph(nb_sentences=1),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]), # Use random_element
                    task=task # Assign the foreign key
                )

            # 4. Generate fake Notes for each Task
            num_notes = random.randint(0, 3) # Each task gets 0 to 3 notes
            for _ in range(num_notes):
                Note.objects.create(
                    content=fake.paragraph(nb_sentences=2),
                    task=task # Assign the foreign key
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {num_tasks} tasks, '
                               f'{SubTask.objects.count()} subtasks, and {Note.objects.count()} notes.')
        )
