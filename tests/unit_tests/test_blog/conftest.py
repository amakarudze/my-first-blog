from datetime import datetime
import pytest

from blog.models import Category, Contact, Event, Post, Talk, Tip


@pytest.fixture
def category(db):
    return Category.objects.create(
        name="Test category", description="Test category description"
    )


@pytest.fixture
def event(db):
    return Event.objects.create(
        name="Test event",
        from_date="2016-02-16 09:00:00",
        to_date="2016-02-18 17:00:00",
        location="Windhoek, Namibia",
        website="https://test.com",
        comments="What a great event",
        is_displayed=True,
    )


@pytest.fixture
def talk(db, category, event):
    return Talk.objects.create(
        title="Test title",
        description="Test title description",
        category=category,
        level="Beginner",
        event=event,
        presenter="Jane Doe",
        slides="https://test.com/slides.pdf",
        date_presented=datetime.now(),
    )


@pytest.fixture
def tip(db, category):
    return Tip.objects.create(
        category=category,
        topic="Python-dotenv",
        tip="Managing environment variables with Python-dotenv",
    )


@pytest.fixture
def post(db, category, user):
    return Post.objects.create(
        user=user,
        title="Test article",
        category=category,
        level="Beginner",
        text="Another test post for beginners.",
    )


@pytest.fixture
def contact(db):
    return Contact.objects.create(
        name="Test User",
        phone="0948593756",
        email="test@test.com",
        subject="Test email",
        message="Test email works!",
    )


@pytest.fixture
def categories(db):
    return Category.objects.bulk_create(
        Category(name="Category 1", description="Test Category 1"),
        Category(name="Category 2", description="Test Category 2"),
        Category(name="Category 3", description="Test Category 3"),
        Category(name="Category 4", description="Test Category 4"),
    )


@pytest.fixture
def contact_form():
    return {
        "name": "Test User",
        "phone": "0172839490",
        "email": "test@test.com",
        "subject": "Test email",
        "message": "Testing email functionality.",
    }


@pytest.fixture
def contact_form_invalid():
    return {
        "name": "Test User",
        "phone": "0172839490",
        "email": "test@test.com",
        "subject": "Test email",
        "message": "Testing email functionality with links in the email https://test.com.",
    }
