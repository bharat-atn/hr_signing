# # Copyright (c) 2024, Bharat and contributors
# # For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document


# class NewRecruitment(Document):
# 	pass






# import frappe
# from frappe.utils.pdf import get_pdf
# from frappe.utils import get_url
# from frappe.core.doctype.communication.email import make

# class NewRecruitment(Document):
#     pass

# @frappe.whitelist()
# def send_pdf_email(record_name):
#     # Fetch the record
#     record = frappe.get_doc("New Recruitment", record_name)

#     # Generate PDF
#     pdf_content = get_pdf(frappe.render_template("hr_signing/templates/pdf/new_recruitment.html", {"doc": record}))
    
#     if not pdf_content:
#         frappe.throw("Failed to generate PDF.")
    
#     # Create email subject and content
#     subject = f"New Recruitment Details - {record.first_name} {record.last_name}"
#     content = f"Please find attached the details for {record.first_name} {record.last_name}."

#     # Send email
#     recipients = [record.email]
    
#     try:
#         frappe.sendmail(
#             recipients=recipients,
#             subject=subject,
#             content=content,
#             attachments=[{
#                 "fname": f"New_Recruitment_{record.first_name}_{record.last_name}.pdf",
#                 "fcontent": pdf_content
#             }]
#         )
#         return "Success"
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "Email Sending Failed")
#         return f"Failed to send email: {str(e)}"










import frappe
from frappe.model.document import Document  
from frappe.utils.pdf import get_pdf
from frappe.utils import get_url
from frappe.core.doctype.communication.email import make

class NewRecruitment(Document):
    pass

@frappe.whitelist()
def send_pdf_email(record_name):
    # Fetch the record
    record = frappe.get_doc("New Recruitment", record_name)

    # Generate PDF
    pdf_content = get_pdf(frappe.render_template("hr_signing/templates/pdf/new_recruitment.html", {"doc": record}))
    
    if not pdf_content:
        frappe.throw("Failed to generate PDF.")
    
    # Create email subject and content
    subject = f"New Recruitment Details - {record.first_name} {record.last_name}"
    content = f"Please find attached the details on the below link for {record.first_name} {record.last_name}, Your Recruitment id is : {record.name}, Use this id during Document signiture.  LINK: http://hrstaff.local:8004/verification/new"

    # Send email
    recipients = [record.email]
    
    try:
        frappe.sendmail(
            recipients=recipients,
            subject=subject,
            content=content,
            attachments=[{
                "fname": f"New_Recruitment_{record.first_name}_{record.last_name}.pdf",
                "fcontent": pdf_content
            }],
            now=True
        )
        return "Success"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Email Sending Failed")
        return f"Failed to send email: {str(e)}"
