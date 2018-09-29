from email_lib import email_lib

def main():
  From=str(raw_input("From: "))
  Pass=str(raw_input("Password: "))
  To=str(raw_input("To: "))
  Subjet=str(raw_input("Subject: "))
  Text=str(raw_input("Text: "))
  con=email_lib(From,Pass,To,Subjet,Text)
  con.send_email()
if __name__=="__main__:
  main()
