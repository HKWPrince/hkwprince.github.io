import functions_framework
import smtplib
from flask import redirect, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



@functions_framework.http
def hello_http(request):
    if request.method == 'POST':

        address="https://hkwprince.github.io"
        photoUrl = "https://avatars.githubusercontent.com/u/70823007?v=4"
        name = ""
        email = ""
        subject = ""


        name = request.values.get('name')
        email = request.values.get('email')
        subject = request.values.get('subject')
        message = request.values.get('message')
        sender="HUANG KUO-WEI"
        
        

        text = "姓名:{}\n信箱:{}\n主旨:{}\n\n內容:\n{}".format(name, email, subject, message)
        text = MIMEText(text)
        
        content = MIMEMultipart()
        content['subject'] = "有人留言給你囉"
        content['from'] = "prince880211@gmail.com"
        content['to'] = "prince880211@gmail.com"
        content.attach(text)

        text2 = "Dear {},\nThank you for reaching out to us through our message board.\n I have received your message and will get back to you as soon as possible.\nIf you have any further questions, please feel free to contact us again.\n\n Best regards,\n from {}\n\n\n\nThis is an automated E-mail from system.".format(name, sender)
        text2 = MIMEText(text2)
        
        contentToGuest = MIMEMultipart()
        contentToGuest['subject'] = "Thank you for your message — we’ve received it!"
        contentToGuest['from'] = "prince880211@gmail.com"
        contentToGuest['to'] = email

        guest_html = """
            <!DOCTYPE html>
            <html lang="zh-Hant">

            <head>
            <meta charset="UTF-8">
            <title>留言回覆</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

                body {
                margin: 0;
                padding: 0;
                background: linear-gradient(180deg, #fff0f5 0%, #fbeef3 100%);
                font-family: 'Inter', Arial, sans-serif;
                }

                .container {
                max-width: 380px;
                margin: 0 auto;
                background: linear-gradient(180deg, #fff0f5 0%, #fbeef3 100%);
                border-radius: 18px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                padding: 24px;
                position: relative;

                background-image: repeating-linear-gradient(
                    to bottom,
                    transparent,
                    transparent 34px,
                    rgb(207, 79, 103) 35px
                );
                background-size: 100% 36px;
                }

                .container::before {
                content: "";
                position: absolute;
                top: 24px;
                bottom: 24px;
                left: -12px;
                width: 12px;
                background: repeating-radial-gradient(circle at center, #ccc 0px, #ccc 2px, transparent 3px, transparent 12px);
                background-size: 12px 36px;
                }

                .avatar {
                display: block;
                width: 80px;
                height: 80px;
                border-radius: 50%;
                object-fit: cover;
                margin: 0 auto 20px auto;
                border: 3px solid #e5b9c1;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }

                h2 {
                color: #c56c83;
                margin-top: 0;
                font-size: 22px;
                font-family: 'Georgia', serif;
                }

                p, td {
                font-size: 15px;
                color: #333333;
                }

                table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 12px;
                }

                td {
                padding: 12px 0;
                vertical-align: top;
                }

                .footer {
                font-size: 13px;
                color: #888;
                border-top: 1px solid #eee;
                padding-top: 16px;
                margin-top: 24px;
                }

                a {
                color: #c56c83;
                text-decoration: none;
                }
            </style>
            </head>""" + f"""
            <body>
            <div class="container">
                <img class="avatar" src="{photoUrl}" alt="avatar">

                <h2>Dear {name},：</h2>
                <p> ✨ nThank you for reaching out to us through our message board！<br>
                I have received your message and will get back to you as soon as possible. 😊</p>
                <table>
                <tr>
                    <td>👤 <strong>Name：</strong><br>{name}</td>
                </tr>
                <tr>
                    <td>📧 <strong>Email：</strong><br>{email}</td>
                </tr>

                <tr>
                    <td>📝 <strong>Content</strong><br>
                    {message.replace('\n', '<br>')}</td>
                </tr>
                </table>

                <p> If you have any further questions, please feel free to contact us again.<br>\n\n</p>
                <div style="text-align: center; margin: 24px 0;">
                <a href="{address}" style="display: inline-block; background: #d39fa5; color: white; padding: 12px 28px; border-radius: 10px; text-decoration: none; font-weight: 600;">
                    ✨ 前往留言表單
                </a>
                </div>

                <div class="footer">
                📮 This is an automated E-mail from system.<br>
                💖 Thank you for your support to<a href="mailto:prince880211@gmail.com" style="color: #b76e79; text-decoration: none;">{sender}</a> ！
                </div>
                <p style="font-size: 16px; color: #b76e79; margin-top: 40px; text-align: right;">
                <strong style="font-size: 17px;">{sender} Best regard</strong>
                </p>
            </div>
            </body>

            </html>
        """
        contentToGuest.attach(MIMEText(guest_html, 'html'))

        smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
        with open("./password.txt", "r") as f:
            mailToken = f.read().strip()
        
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("prince880211@gmail.com", mailToken)
            smtp.send_message(content)
            smtp.send_message(contentToGuest)
            print("Email is sent successfully!")
        except Exception as e:
            print("Error sending failed: ", e)
            return "Internal Server Error", 500
        finally:
            smtp.quit()

        return f'''
                <script>
                alert("留言已送出，即將導回頁面{sender}的網頁");
                window.location.href = "{address}";
                </script>
                '''

    return "Hi"