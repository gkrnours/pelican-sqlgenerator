from markdown import Markdown
from pelican import contents
from pelican.generators import Generator
from pelican.urlwrappers import Author, Category
from playhouse import db_url


from .models import database, Content


class SQLGenerator(Generator):
    def __init__(self, context, settings, path, theme, output_path):
        self.context = context
        self.md = Markdown()
        database.initialize(db_url.connect(settings["SQL_DATABASE"]))

    def generate_context(self):
        cts = self._gather_contents()
        self.context["pages"] += cts
        page = contents.Page("<h1>Hello, world!</h1>", dict(
            title="Hello, World!",
            category=Category("Misc", {})
        ))
        self.context["pages"].append(page)

    def _gather_contents(self):
        r = []
        for content in Content.select():
            page = contents.Page(self.md.convert(content.content), dict(
                author=Author(content.author.name, {}),
                title=content.title,
                date=content.date,
                status=content.status,
                # category=Category("Misc", {})
            ))
            r.append(page)
        return r
