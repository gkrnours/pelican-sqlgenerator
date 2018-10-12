from datetime import datetime
import peewee

database = peewee.Proxy()


class Author(peewee.Model):
    class Meta:
        database = database
    name = peewee.CharField(max_length=160)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Content(peewee.Model):
    class Meta:
        database = database
    HIDDEN  = 'hd'
    DRAFT   = 'df'
    PUBLISHED = 'pb'
    STATUS_CHOICES = (
        (HIDDEN, 'Hidden'),
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    PAGE    = 'pg'
    ARTICLE = 'ar'
    QUOTE   = 'qt'
    TYPE_CHOICES = (
        (PAGE, 'Page'),
        (ARTICLE, 'Article'),
        (DRAFT, 'Draft'),
        (QUOTE, 'Quote'),
    )

    author  = peewee.ForeignKeyField(Author, backref="publications")
    title   = peewee.CharField(max_length=160, unique=True)
    slug    = peewee.CharField(max_length=40)
    date    = peewee.DateTimeField(default=datetime.now)
    modified = peewee.DateTimeField(default=datetime.now)
    status  = peewee.CharField(max_length=2, choices=STATUS_CHOICES)
    content = peewee.TextField()


def init_db(db):
    if database.obj == None:
        database.initialize(db)
    db.connect()
    db.create_tables([Author, Content])
    Author.create(id=0, name="author")
    db.close()
