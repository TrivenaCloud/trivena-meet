# Copyright (c) 2025, Frappe and contributors
# For license information, please see license.txt

import trivena_framework as trivena
from trivena_framework.utils.caching import redis_cache


@redis_cache(ttl=5 * 60)
def get_sfu_config():
	"""Get SFU configuration from site config or defaults"""
	return {
		"sfu_server_url": trivena.conf.get("sfu_server_url", "http://localhost"),
		"sfu_server_port": trivena.conf.get("sfu_server_port", 3000),
		"sfu_secret": trivena.conf.get("sfu_secret", ""),
	}
