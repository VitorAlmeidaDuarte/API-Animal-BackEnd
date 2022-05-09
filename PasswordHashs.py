from passlib.hash import pbkdf2_sha512


def create_hash(password):
    pass_hash = pbkdf2_sha512.hash(password.encode("utf-8"))

    return pass_hash


def verify_hash(password, hash_password):
    if pbkdf2_sha512.verify(password, hash_password):
        return True

    else:
        return False
