import os
import django
import random
from faker import Faker
from django.db.utils import IntegrityError

# Ensure Django settings are configured
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whistly.settings")
django.setup()

# Import models AFTER Django setup
from birds.models import Bird
from users.models import CustomUser

# Faker instance
fake = Faker()


def dummy_birds_multiply_users(n=10):
    """
    Populates the Bird's nest with data.
    1 User x 1 Bird
    """
    print(f"Generating {n} users, each with one bird...")
    for _ in range(n):
        user = fake.first_name()
        email = fake.email()
        pwd = fake.pystr()

        try:
            new_user = CustomUser.objects.create_user(
                username=user, email=email, password=pwd
            )
        except IntegrityError:  # In case of username collision
            user = f"{user}_{random.randint(1, 999)}"
            new_user = CustomUser.objects.create_user(
                username=user, email=email, password=pwd
            )

        # Generate bird data
        location = fake.country()
        comment = fake.paragraph()
        species = fake.last_name()
        picture = random.choice(
            [x for x in os.listdir(os.path.join("media", "test_birds"))]
        )

        new_bird = Bird(
            species=species,
            location=location,
            photographer=new_user,
            photographer_comment=comment,
            picture=os.path.join("test_birds", picture),
        )
        new_bird.save()
    print("Successfully populated users and birds!")


def dummy_birds_single_user(n=10):
    """
    Populates the Bird's nest with data.
    1 User x (n) Birds
    """
    print(f"Generating 1 user with {n} birds...")
    email = fake.email()
    pwd = fake.pystr()

    user, created = CustomUser.objects.get_or_create(
        username="SuperUser", email=email
    )
    if created:
        user.set_password(pwd)
        user.save()
        print(f"SuperUser created with email {email}")

    # Generate bird data
    for _ in range(n):
        location = fake.country()
        comment = fake.paragraph()
        species = fake.last_name()
        picture = random.choice(
            [x for x in os.listdir(os.path.join("media", "test_birds"))]
        )

        new_bird = Bird(
            species=species,
            location=location,
            photographer=user,
            photographer_comment=comment,
            picture=os.path.join("test_birds", picture),
        )
        new_bird.save()
    print("Birds successfully populated for SuperUser!")


if __name__ == "__main__":
    print("Populating database with dummy bird data...")

    # Read optional environment variable for number of birds/users
    num_users = int(os.getenv("NUM_USERS", 20))
    num_birds = int(os.getenv("NUM_BIRDS", 10))

    # For multiple users, each with 1 bird
    dummy_birds_multiply_users(num_users)

    # For single user with multiple birds
    dummy_birds_single_user(num_birds)

    print("Database population complete!")
