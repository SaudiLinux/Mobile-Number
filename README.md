# Phone Information Finder Tool

<p align="center">
  <img src="banner.svg" alt="Phone Information Finder Tool" width="600">
</p>

## 🔍 وصف الأداة

أداة بلغة البايثون تمكنك من البحث عن تفاصيل أرقام الهواتف المحمولة، حيث تقوم بجمع معلومات شاملة عن الرقم مثل:

- اسم صاحب الرقم (إذا كان متاحًا)
- المواقع المرتبطة بالرقم
- آخر ظهور للرقم
- أسماء المستخدم في مواقع التواصل الاجتماعي المرتبطة بالرقم
- البريد الإلكتروني المرتبط بالرقم
- معلومات الموقع الجغرافي
- معلومات شركة الاتصالات

## 🚀 المميزات

- ✅ واجهة سهلة الاستخدام مع ألوان جذابة
- ✅ تحليل شامل لأرقام الهواتف
- ✅ البحث في قواعد البيانات عبر الإنترنت
- ✅ البحث العميق عن المعلومات المرتبطة بالرقم
- ✅ حفظ النتائج بتنسيق JSON
- ✅ دعم الأرقام الدولية

## 📋 المتطلبات

```
python 3.6+
requests
phonenumbers
colorama
tabulate
```

## ⚙️ التثبيت

1. قم بتثبيت المتطلبات:

```bash
pip install -r requirements.txt
```

2. قم بتشغيل الأداة:

```bash
python phone_info_finder.py -n "+1234567890"
```

## 📝 طريقة الاستخدام

```
usage: phone_info_finder.py [-h] -n NUMBER [-o OUTPUT] [-d]

Phone Information Finder Tool

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Phone number in international format (e.g., +1234567890)
  -o OUTPUT, --output OUTPUT
                        Output file to save results (JSON format)
  -d, --deep            Perform deep search
```

### أمثلة:

1. البحث الأساسي عن رقم هاتف:

```bash
python phone_info_finder.py -n "+1234567890"
```

2. البحث وحفظ النتائج في ملف:

```bash
python phone_info_finder.py -n "+1234567890" -o results.json
```

3. إجراء بحث عميق:

```bash
python phone_info_finder.py -n "+1234567890" -d
```

## ⚠️ تنبيه

هذه الأداة مخصصة للأغراض التعليمية والبحثية فقط. يرجى استخدامها بشكل أخلاقي وقانوني. لا تستخدم هذه الأداة لأي أنشطة غير قانونية أو انتهاك خصوصية الآخرين.

## 👨‍💻 المطور

**Saudi Linux**

البريد الإلكتروني: SaudiLinux7@gmail.com

## 📜 الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف LICENSE للتفاصيل.