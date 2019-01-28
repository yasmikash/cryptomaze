from cryptomaze.settings import discount_list
from cryptomaze.models import User


def ref_count(user_id):
    user = User.query.filter_by(referred_by=user_id)
    count = 0
    for ref in user:
        count += 1
    return count


def apply_discount(refs):
    for key, val in discount_list.items():
        if refs in range(key[0], key[1]):
            return val
    if not refs == 0:
        return 70
