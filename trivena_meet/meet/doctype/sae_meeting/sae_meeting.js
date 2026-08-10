// Copyright (c) 2025, Frappe and contributors
// For license information, please see license.txt

trivena.ui.form.on("Sae Meeting", {
	refresh(frm) {
		frm.add_web_link(`/meet/${frm.doc.name}`, __("Join Meeting"));
	},
});
