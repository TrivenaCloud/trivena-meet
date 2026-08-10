import trivena_framework as trivena

no_cache = 1


def get_context():
	csrf_token = trivena.sessions.get_csrf_token()
	trivena.db.commit()
	context = trivena._dict()
	context.boot = get_boot()
	context.boot.csrf_token = csrf_token
	return context


@trivena.whitelist(methods=["POST"], allow_guest=True)
def get_context_for_dev():
	if not trivena.conf.developer_mode:
		trivena.throw("This method is only meant for developer mode")
	return get_boot()


def get_boot():
	return trivena._dict(
		frappe_version=trivena.__version__,
		site_name=trivena.local.site,
		is_system_user=trivena.session.data.user_type == "System User",
	)
