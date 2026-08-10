# Copyright (c) 2025, Frappe and contributors
# For license information, please see license.txt

import trivena_framework as trivena
from trivena_framework.utils.caching import redis_cache


@trivena.whitelist()
def get_logged_in_user() -> dict | None:
	user = trivena.session.user
	if user == "Guest":
		return None

	user_doc = trivena.get_doc("User", user)
	return {
		"name": user_doc.name,
		"email": user_doc.email,
		"full_name": user_doc.full_name,
		"avatar": user_doc.user_image,
		"roles": [role.role for role in user_doc.roles],
	}


@trivena.whitelist(allow_guest=True)
@redis_cache(ttl=10 * 60)
def oauth_providers(redirect_url: str = "") -> list[dict]:
	from trivena_framework.utils.html_utils import get_icon_html
	from trivena_framework.utils.oauth import get_oauth2_authorize_url, get_oauth_keys
	from trivena_framework.utils.password import get_decrypted_password

	out = []
	providers = trivena.get_all(
		"Social Login Key",
		filters={"enable_social_login": 1},
		fields=["name", "client_id", "base_url", "provider_name", "icon"],
		order_by="name",
	)

	for provider in providers:
		client_secret = get_decrypted_password("Social Login Key", provider.name, "client_secret")
		if not client_secret:
			continue

		icon = None
		if provider.icon:
			if provider.provider_name == "Custom":
				icon = get_icon_html(provider.icon, small=True)
			else:
				icon = f"<img src='{provider.icon}' alt={provider.provider_name}>"

		if provider.client_id and provider.base_url and get_oauth_keys(provider.name):
			out.append(
				{
					"name": provider.name,
					"provider_name": provider.provider_name,
					"auth_url": get_oauth2_authorize_url(provider.name, f"/meet{redirect_url}"),
					"icon": icon,
				}
			)
	return out
