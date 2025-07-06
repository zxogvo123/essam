import gspread
from oauth2client.service_account import ServiceAccountCredentials

# إعداد الصلاحيات
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# تحميل بيانات حساب الخدمة
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "/data/data/ru.iiec.pydroid3/files/credentials.json", scope
)
client = gspread.authorize(creds)

# روابط الشيتات كلها
sheet_urls = [
    "https://docs.google.com/spreadsheets/d/1zZ8Jt_bDPHnGGYjp7OeOoCQNBLHw__YIFFz1el6LlY0",
 "https://docs.google.com/spreadsheets/d/1UWqxbQ2icb4QmFr1oC1aP5ZzzQrEVvhR5xSt0s4AGzE/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1nWCfZXTPvdqtl6MBRfIJgwCItT11aMQESq3SbnWPdkU",
 "https://docs.google.com/spreadsheets/d/1zs1L5FQYvLlcU_yPjmKRiGhcJQvYu6UQzg8YD0K50lI/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1AbmZ2CpBdN1qhVw8YbOPeHg_9bCvRCGZOq-J2mWIwIg/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1bGHKfY7AMCmuBW7gBa5u1mrSiWlmAunaFzzF2Nbo1ag/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1SRgRfG-moek1jJFSQNE-Gujoc3G0mhPgEOZb_Z5uVz8/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1USib7uXX7pd34zBCeYU3cGH1jExfnxY17S2VcEX-haM/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1I-3o98Jd3U0ztoszx1v4qOLVeIn3nPeO-YXUaFJWdCw/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1TpkDy7pl9JU68csRhO7K088sLg_1ZwbRakOB26bR-LY/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1UoJBmtLUT1VjECZS1VN51sVNUtuffKSDkCc-f9A7ARc/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1f5G1YV989LvcbAKkcY7jEkzcSFVcr_AT-_RWpdz75aY/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1o73WfBvAKimJzqyT-44ZaKUy7y9aIgS6kNdgKZX07Q8/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1FRzHyBZTHf1jNL8ikCeyEPQZx-uJocOz1_gaEkMbp5U/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1-fhzvArK7sCJ7mBxoRMGi8PJEUnGs_9B_-6Hu-4DcLM/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1d1KxYiA89ujFiAjwBk2jposuoe6TKm3YDUbd3nLZssg/edit?usp=drivesdk",
 "https://docs.google.com/spreadsheets/d/1Olt3a8ldSpCpmeKpdem-UpAZUZgzeOiMplFDBH87nK0/edit?usp=drivesdk",
 
 
    # ضيف أي روابط شيتات إضافية هنا
]

# تحميل كل البيانات من كل الشيتات
def load_all_data():
    data = []
    for url in sheet_urls:
        try:
            sheet = client.open_by_url(url).sheet1
            rows = sheet.get_all_values()
            for row in rows[1:]:  # تخطي الصف الأول (رؤوس الأعمدة)
                data.append(row)
        except Exception as e:
            print("❌ خطأ في الشيت:", url)
            print("📄 تفاصيل الخطأ:", e)
    return data

# دالة البحث عن الفاتورة
def search_invoice(doc_number, data):
    for row in data:
        try:
            if str(row[3]).strip() == str(doc_number):  # العمود D
                date = row[2]      # العمود C
                tender = row[7]    # العمود H
                cashier = row[8]   # العمود I
                return f"📅 التاريخ: {date}\n💳 طريقة الدفع: {tender}\n👤 الكاشير: {cashier}"
        except:
            continue
    return "❌ رقم الفاتورة غير موجود في أي يوم."

# تشغيل البوت
all_data = load_all_data()

while True:
    print("\n📥 اكتب رقم الفاتورة (أو اكتب 'خروج' لإنهاء البرنامج):")
    invoice = input("➡️ رقم الفاتورة: ").strip()

    if invoice.lower() in ["خروج", "exit", "quit"]:
        print("👋 تم إنهاء البوت. إلى اللقاء!")
        break

    result = search_invoice(invoice, all_data)
    print(result)
