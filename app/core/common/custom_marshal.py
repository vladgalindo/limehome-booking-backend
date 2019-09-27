from flask_restplus import marshal
from app.core.common.date_tools import get_time
from flask_jwt_extended import get_jwt_identity


def custom_marshal(model, template, option='create'):
    user_id = get_jwt_identity()
    data = marshal(model, template)
    if option == 'create':
        data['metadata']['created_on'] = get_time()
        data['metadata']['updated_on'] = get_time()
        data['metadata']['created_by'] = user_id
        data['metadata']['updated_by'] = user_id
    elif option == 'update' or option == 'delete':
        data['metadata']['updated_on'] = get_time()
        data['metadata']['updated_by'] = user_id
    return data
