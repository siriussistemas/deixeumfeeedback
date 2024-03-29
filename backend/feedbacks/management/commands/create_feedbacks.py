from faker import Faker

from django.core.management.base import BaseCommand, CommandError, CommandParser

from feedbacks.models import Feedback
from django.contrib.auth import get_user_model

import random

User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = "Create fake feedbacks for a user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "user_email", type=str, help="User email to create feedbacks"
        )
        parser.add_argument(
            "--total", type=int, default=30, help="Total feedbacks to create"
        )

    def handle(self, *args, **options):
        email = options["user_email"]
        total = options["total"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise CommandError(f"User with {email} does not exists")

        feedbacks = [
            Feedback(
                user=user,
                text=fake.text(),
                type=Feedback.FeedbackType(
                    random.choice(["ISSUE", "IDEA", "OTHER"])
                ),  # TODO: get all availables options type from the model
                page=fake.url(),
                device=fake.user_agent(),
                fingersprint=fake.sha256(raw_output=False),
            )
            for _ in range(total)
        ]

        Feedback.objects.bulk_create(feedbacks)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created feedbacks for {email}")
        )
