// Copyright (c) 2024, Bharat and contributors
// For license information, please see license.txt

// frappe.ui.form.on("New Recruitment", {
// 	refresh(frm) {

// 	},
// });



frappe.ui.form.on('New Recruitment', {
    refresh(frm) {
        frm.add_custom_button(__('Send PDF Email'), function() {
            frappe.call({
                method: 'hr_signing.hr_signing.doctype.new_recruitment.new_recruitment.send_pdf_email',
                args: {
                    record_name: frm.doc.name
                },
                callback: function(response) {
                    if (response.message === 'Success') {
                        frappe.msgprint(__('Email sent successfully.'));
                    } else {
                        frappe.msgprint(__('Failed to send email.'));
                    }
                }
            });
        });
    }
});
