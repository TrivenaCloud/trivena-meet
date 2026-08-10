# Copyright (c) 2026, Frappe and contributors
# For license information, please see license.txt

import trivena_framework as trivena
from trivena_framework.tests.utils import whitelist_for_tests


@whitelist_for_tests()
def clear_create_rate_limit() -> None:
	"""Clear meeting creation, join meeting as guest rate limit cache."""
	keys = trivena.cache.get_keys("rl:meet.api.meeting.join_meeting_as_guest:*")
	keys += trivena.cache.get_keys("rl:meet.api.meeting.create:*")
	for key in keys:
		trivena.cache.set(key, 0)  # nosemgrep
