from django.core.mail import send_mail
from django.http import JsonResponse

# htmlMessage = '<h1>This is my HTML test</h1>'

subject = 'Some subject'
from_email = 'nap3831@gmail.com'
message = 'This is my test message'
recipient_list = ['nap38318@gmail.com',]
html_message = '<h1>This is my HTML test</h1>  <br/> <a href="https://fb.com/nap2539">Contact Admin</a>'
def sendEmail(request):
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
    return JsonResponse({'status ': 200})


# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
# 		auth=("api", "YOUR_API_KEY"),
# 		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
# 			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})

# subject = "Hello, its me"
# text_content = "I was wondering if after all these years"
# sender = "from@localhost.com"
# recipient = "to@localhost.com"

# def send_simple_message():
#     msg = EmailMultiAlternatives(subject, text_content, sender, [recipient])
#     msg.send()
#     return JsonResponse({'status': 200})