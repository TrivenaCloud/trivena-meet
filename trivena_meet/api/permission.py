import trivena_framework as trivena


def has_app_permission() -> bool:
	if trivena.session.user == "Administrator":
		return True

	roles = trivena.get_roles()
	meet_roles = ["Meet User"]
	if any(role in roles for role in meet_roles):
		return True

	return False
