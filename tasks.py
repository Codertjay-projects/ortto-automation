import json

new_task = {
    "automation_name": "Name Provided for the automation",
    "option_error_message": "welcome_new_subscriber or respond_to_subscriber_changes",
    "automation_choice": "autoresponder",
    "mail_type": "welcome_new_subscriber"
}


class SendMailTask():
    def __init__(self, option):
        self.option = option

    def verify_email_task(self):
        """
      it takes Autoresponder, ecommerce_and_marketing, Blank (Means None)
      If option is autoresponder then the (email option is to welcome new subscriber)
        """
        if self.option.get("automation_choice") == "autoresponder":
            with open("./autoresponder.json", "r") as content:
                if self.verify_json_passed(content):
                    return self.send_email_task()
        elif self.option.get("automation_choice") == "ecommerce_and_marketing":
            with open("./ecommerce_and_marketing.json", "r") as content:
                if self.verify_json_passed(content):
                    return self.send_email_task()
        elif self.option.get("automation_choice") == "blank" or "":
            with open("./blank.json", "r") as content:
                if self.verify_json_passed(content):
                    return self.send_email_task()
        return self.failed_mail_task()

    def verify_json_passed(self, content):
        for items in json.loads(content.read()):
            for key, value in items.items():
                if self.option.get("mail_type"):
                    if key.lower() == "mail_type" and value == self.option.get("mail_type").lower():
                        return True
        return False

    def send_email_task(self):
        print(f"""
            Sending email To {self.option.get("mail_type").replace("_", " ")}:
            Title of the automation is  {self.option.get("automation_name").replace("_", " ")}
            Automation choice is {self.option.get("automation_choice").replace("_", " ")}
            """)
        return True

    def failed_mail_task(self):
        print("""
        we were not able to validate your response please provide a valid mail_type and  automation_choice 
        you can choose the choices below
        """)
        with open("./autoresponder.json", "r") as content:
            print(content.read())
        with open("./ecommerce_and_marketing.json", "r") as content:
            print(content.read())
        with open("./blank.json", "r") as content:
            print(content.read())
        return False


run_task = SendMailTask(option=new_task)
run_task.verify_email_task()
