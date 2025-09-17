from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from tasks.models import Category, Priority, Task, SubTask, Note


class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Manually create Categories and Priorities
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        priorities = ["high", "medium", "low", "critical", "optional"]

        for cat_name in categories:
            Category.objects.get_or_create(name=cat_name)

        for pri_name in priorities:
            Priority.objects.get_or_create(name=pri_name)

        # Get the created objects for relationships
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        # Generate 20 fake tasks
        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=fake.random_element(elements=priorities),
                category=fake.random_element(elements=categories),
            )

            # Generate 1-3 notes for each task
            for _ in range(fake.random_int(min=1, max=3)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

            # Generate 0-5 subtasks for each task
            for _ in range(fake.random_int(min=0, max=5)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=3),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                    parent_task=task
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data.'))