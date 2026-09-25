"""Dummy users used to seed a local learning-project database."""

from src.models.user import User
from src.utils.constants import Role


DUMMY_USERS = [
    User(user_name="dr.mehta", password="doctor", roles=[Role.DOCTOR]),
    User(user_name="nurse.priya", password="nurse", roles=[Role.NURSE]),
    User(
        user_name="billing.ravi",
        password="billing_executive",
        roles=[Role.BILLING_EXECUTIVE],
    ),
    User(user_name="tech.anand", password="technician", roles=[Role.TECHNICIAN]),
    User(user_name="admin.sys", password="admin", roles=[Role.ADMIN]),
]
