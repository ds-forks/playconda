from django.db.models import Model, CharField, ManyToManyField, EmailField, \
    URLField


class Term(Model):
    text = CharField(max_length=64, unique=True)

    def __str__(self):
        return self.term

    def __repr__(self):
        return "<Term: %s>" % self.__str__()


class App(Model):
    terms = ManyToManyField(Term, related_name="apps")
    app_id = CharField(max_length=64, unique=True)
    app_name = CharField(max_length=256)
    developer_name = CharField(max_length=128)
    developer_email = EmailField(max_length=128, null=True)
    icon_url = URLField(max_length=256)

    def __str__(self):
        return self.app_id

    def __repr__(self):
        return "<App: %s>" % self.__str__()
