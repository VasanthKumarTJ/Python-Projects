from blog.models import Category
from django.core.management.base  import BaseCommand


class Command(BaseCommand):
    help = "Populate data for the category model"

    def handle(self, *args, **options):
        # Deleting existing data
        Category.objects.all().delete()
        categories = ['Sports', 'Technology', 'Science', 'Health', 'Business', 'Art', 'Travel', 'Food', 'Fashion', 'Music']

        for category_name in categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Data populated successfully!"))
       
# python manage.py populate_posts
# The above command will populate the Posts model with sample data for demonstration purposes. You can customize the titles, contents, and image URLs to suit your needs. After running the command, you should see a success message indicating that the data has been populated successfully. You can then view the populated data in the Django admin interface or query it using Django ORM methods.