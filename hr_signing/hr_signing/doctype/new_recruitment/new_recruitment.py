# # # Copyright (c) 2024, Bharat and contributors
# # # For license information, please see license.txt

# # # import frappe
# # from frappe.model.document import Document


# # class NewRecruitment(Document):
# # 	pass





# import frappe
# from frappe.model.document import Document


# class NewRecruitment(Document):

# 	def send_approval_email(doc, method):
# 		"""
# 		Send an email with a PDF attachment when the status changes to 'Approve'.
# 		"""
# 		print( "Email Notifcatio  is working properly ")
# 		if doc.status == "Approve":
# 			# Generate the PDF for the document
# 			pdf_data = frappe.get_print(doc.doctype, doc.name, print_format="Standard", as_pdf=True)

# 			# Define recipient, subject, and message
# 			recipient = doc.email or "default@example.com"  # Use the email field or a default
# 			subject = f"Approval Notification for {doc.first_name} {doc.last_name}"
# 			message = f"""
# 			Dear {doc.first_name} {doc.last_name},

# 			Your recruitment process has been approved. Please find the attached document for your reference.

# 			Regards,  
# 			HR Team
# 			"""

# 			# Send the email with the PDF attached
# 			frappe.sendmail(
# 				recipients=[recipient],
# 				subject=subject,
# 				message=message,
# 				attachments=[
# 					{
# 						"fname": f"{doc.name}.pdf",
# 						"fcontent": pdf_data
# 					}
# 				]
# 			)








import frappe
from frappe.model.document import Document

class NewRecruitment(Document):

    def send_approval_email(self, doc, method):
        """
        Send an email with a PDF attachment when the status changes to 'Approve'.
        """
        print("Email Notification is working properly")
        if doc.status == "Approve":
            # Generate the PDF for the document
            pdf_data = frappe.get_print(doc.doctype, doc.name, print_format="Standard", as_pdf=True)

            # Define recipient, subject, and message
            recipient = doc.email or "default@example.com"  # Use the email field or a default
            subject = f"Approval Notification for {doc.first_name} {doc.last_name}"
            message = f"""
            Dear {doc.first_name} {doc.last_name},

            Your recruitment process has been approved. Please find the attached document for your reference.

            Regards,  
            HR Team
            """

            # Send the email with the PDF attached
            frappe.sendmail(
                recipients=[recipient],
                subject=subject,
                message=message,
                attachments=[
                    {
                        "fname": f"{doc.name}.pdf",
                        "fcontent": pdf_data
                    }
                ]
            )
