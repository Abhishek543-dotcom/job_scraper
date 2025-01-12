import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from app.backend.resume_parsing import ResumeParser

class EmailAutomator:
    def __init__(self, resume_path, smtp_server, smtp_port, smtp_user, smtp_password):
        self.resume_path = resume_path
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.resume_parser = ResumeParser(resume_path)

    def send_email(self, to_email, job_title, company, job_url):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = to_email
        msg['Subject'] = f"Application for {job_title} at {company}"

        body = f"""
        Dear Hiring Manager,

        I am writing to express my interest in the {job_title} position at {company}, as advertised on {job_url}. I believe my skills and experience align well with the requirements of the role.

        Please find my resume attached for your consideration. I am excited about the opportunity to contribute to your team and would welcome the chance to discuss my application further.

        Thank you for considering my application.

        Best regards,
        [Your Name]
        """

        msg.attach(MIMEText(body, 'plain'))

        # Attach resume
        attachment = open(self.resume_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(self.resume_path)}")
        msg.attach(part)

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            text = msg.as_string()
            server.sendmail(self.smtp_user, to_email, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

# Example usage
if __name__ == "__main__":
    resume_path = "path/to/your/resume.pdf"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"
    to_email = "hr@example.com"
    job_title = "Software Engineer"
    company = "Example Inc."
    job_url = "https://example.com/job-posting"

    automator = EmailAutomator(resume_path, smtp_server, smtp_port, smtp_user, smtp_password)
    success = automator.send_email(to_email, job_title, company, job_url)
    if success:
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
