from user_data_store import models
from user_data_store.models import db


def crud(model, action, data=None, query=None):
    model = getattr(models, model)
    return serializer(globals()["%s_entry" % action](
        model=model,
        **{"data": data, "query": query}
    ))


def create_entry(model, **kwargs):
    instance = model(**kwargs["data"])
    db.session.add(instance)
    db.session.commit()
    return instance


def serializer(instance):
    """
    Translate model object into a dictionary, to assist with json
    serialization.

    :param instance: SQLAlchemy model instance
    :return: python dict
    """
    data = {}
    for prop in instance.__mapper__.iterate_properties:
        data[prop.key] = getattr(instance, prop.key)

    return data
