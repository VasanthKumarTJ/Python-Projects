from datetime import datetime
from django.db import models

class BlogPosts:
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    category : str
    