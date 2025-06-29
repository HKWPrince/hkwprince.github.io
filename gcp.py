# functions-framework==3.*
# firebase-admin==6.0.1
# google-cloud-firestore==2.13.0
# Flask==2.3.2



import functions_framework
import smtplib
from flask import redirect, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



@functions_framework.http
def hello_http(request):
    if request.method == 'POST':

        photo={"https://hkwprince.github.io": "https://hkwprince.github.io/assets/img/profile-img.jpeg",
        "https://lennert1226.github.io": "https://lennert1226.github.io/assets/img/me.jpg",
        "https://yoshilinmc.github.io": "https://yoshilinmc.github.io/assets/img/passport2.jpg",
        "https://scofield0605.github.io": "https://scofield0605.github.io/assets/img/Scofield_tsai_Toronto%20.jpg",
        "https://lucas0932.github.io": "https://lucas0932.github.io/assets/img/me.jpg"}


        photoUrl = "https://github.com/HKWPrince/hkwprince.github.io/blob/master/assets/img/logo_tree.png?raw=true"
        name = ""
        email = ""
        phone = ""
        message = ""
        address = ""
        mailTo = ""

        name = request.values.get('name')
        email = request.values.get('email')
        phone = request.values.get('phone')
        message = request.values.get('message')
        address = request.values.get('address')
        mailTo = request.values.get('mailTo')
        sender=address.replace("https://","").replace(".github.io","")
        
        print("表單接收到的資料：")
        print("name:", name)
        print("email:", email)
        print("phone:", phone)
        print("message:", message)
        print("address:", address)
        print("mailTo:", mailTo)

        if photo.get(address):
            photoUrl = photo[address]

        text = "姓名:{}\n信箱:{}\n電話:{}\n\n內容:\n{}".format(name, email, phone, message)
        text = MIMEText(text)
        
        content = MIMEMultipart()
        content['subject'] = "有人要留言給你囉"
        content['from'] = "kubetech.academy0524@gmail.com"
        content['to'] = mailTo
        content.attach(text)

        text2 = "Dear {},\nThank you for reaching out to us through our message board.\n I have received your message and will get back to you as soon as possible.\nIf you have any further questions, please feel free to contact us again.\n\n Best regards,\n from {}\n\n\n\nThis is an automated E-mail from system.".format(name, mailTo)
        text2 = MIMEText(text2)
        
        contentToGuest = MIMEMultipart()
        contentToGuest['subject'] = "Thank you for your message — we’ve received it!"
        contentToGuest['from'] = "kubetech.academy0524@gmail.com"
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

                <h2>親愛的 {name}，您好：</h2>
                <p> ✨ 感謝您透過我的個人網站留言！<br>
                我已收到以下訊息，將會盡快回覆您，請稍候片刻 😊</p>
                <table>
                <tr>
                    <td>👤 <strong>姓名：</strong><br>{name}</td>
                </tr>
                <tr>
                    <td>📧 <strong>信箱：</strong><br>{email}</td>
                </tr>
                <tr>
                    <td>📞 <strong>電話：</strong><br>{phone}</td>
                </tr>
                <tr>
                    <td>📝 <strong>留言內容：</strong><br>
                    {message.replace('\n', '<br>')}</td>
                </tr>
                </table>

                <p> 如果您還有其他問題，歡迎隨時再次聯絡我🙌</p>
                <div style="text-align: center; margin: 24px 0;">
                <a href="{address}" style="display: inline-block; background: #d39fa5; color: white; padding: 12px 28px; border-radius: 10px; text-decoration: none; font-weight: 600;">
                    ✨ 前往留言表單
                </a>
                </div>

                <div class="footer">
                📮 此為系統自動寄送的通知信，請勿直接回覆。<br>
                💖 感謝您對 <a href="mailto:{mailTo}" style="color: #b76e79; text-decoration: none;">{mailTo}</a> 的支持與關注！
                </div>
                <p style="font-size: 16px; color: #b76e79; margin-top: 40px; text-align: right;">
                <strong style="font-size: 17px;">{sender} 敬上</strong>
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
            smtp.login("kubetech.academy0524@gmail.com", mailToken)
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