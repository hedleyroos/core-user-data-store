from user_data_store import mappings
from user_data_store import models
from user_data_store.models import db


def crud(model,api_model, action, data=None, query=None):
    model = getattr(models, model)
    return serializer(
        globals()["%s_entry" % action](
            model=model,
            **{"data": data, "query": query}
        ),
        api_model=api_model
    )


def create_entry(model, **kwargs):
    instance = model(**kwargs["data"])
    db.session.add(instance)
    db.session.commit()
    return instance


def read_entry(model, **kwargs):
    # Get query only takes PKs, no kwargs. Filter however is more flexible.
    instance = model.query.filter_by(**kwargs["query"]).first_or_404()
    return instance


def update_entry(model, **kwargs):
    instance = model.query.get(**kwargs["query"])
    for key, value in kwargs["data"]:
        setattr(instance, key, value)
    db.session.commit()
    return instance


def delete_entry(model, **kwargs):
    # Can not safely without explicit select on id.
    instance = model.query.get(kwargs["query"]["id"])
    db.session.delete(instance)
    db.session.commit()


def list_entry(model, **kwargs):
    query = model.query
    if kwargs["query"].get("ids"):
        query = query.filter(model.id.in_(kwargs["query"].get("ids")))
    return query.offset(
        kwargs["query"].get("offet", None)
    ).limit(
        kwargs["query"].get("limit", None)
    ).all()


def serializer(instance, api_model):
    """
    Translate model object into a dictionary, to assist with json
    serialization.
    :param instance: SQLAlchemy model instance
    :return: python dict
    """
    data = None
    model_name = instance.__class__.__name__ \
        if not isinstance(instance, list) else instance[0].__class__.__name__
    transformer = getattr(mappings,
                          "DB_TO_API_%s_TRANSFORMATION" % model_name.upper())

    # TODO look at instance.__dict__ later, seems to not always provide the
    # expected dict.
    if isinstance(instance, list):
        data = []
        for obj in instance:
            obj_data = {}
            for key in obj.__table__.columns.keys():
                obj_data[key] = getattr(obj, key)
            data.append(
                api_model.from_dict(transformer.apply(obj_data))
            )
    else:
        data = {}
        for key in instance.__table__.columns.keys():
            data[key] = getattr(instance, key)
        data = api_model.from_dict(transformer.apply(data))
    return data
