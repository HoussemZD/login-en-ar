import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# --- قاموس الترجمات ---
# هذا القاموس يحتوي على جميع النصوص المستخدمة في الواجهة
# لسهولة التبديل بين اللغتين.
translations = {
    'en': {
        'window_title': "Login Interface",
        'title_label': "Login",
        'username_placeholder': "Username",
        'password_placeholder': "Password",
        'show_password': "Show Password",
        'login_button': "Login",
        'forgot_password': "Forgot Password?",
        'login_error_title': "Login Error",
        'login_error_message': "Please enter a username and password",
        'credentials_error': "Incorrect username or password",
        'login_success_title': "Success",
        'login_success_message': "Welcome, {username}!",
        'lang_label': "Language:"
    },
    'ar': {
        'window_title': "واجهة تسجيل الدخول",
        'title_label': "تسجيل الدخول",
        'username_placeholder': "اسم المستخدم",
        'password_placeholder': "كلمة المرور",
        'show_password': "إظهار كلمة المرور",
        'login_button': "دخـــول",
        'forgot_password': "هل نسيت كلمة المرور؟",
        'login_error_title': "خطأ في الدخول",
        'login_error_message': "الرجاء إدخال اسم المستخدم وكلمة المرور",
        'credentials_error': "اسم المستخدم أو كلمة المرور غير صحيحة",
        'login_success_title': "نجاح",
        'login_success_message': "مرحباً بك، {username}!",
        'lang_label': "اللغة:"
    }
}
current_lang = 'en' # اللغة الافتراضية هي العربية

# --- الدوال الوظيفية ---

def set_language(lang):
    """
    تقوم هذه الدالة بتغيير لغة الواجهة بالكامل.
    """
    global current_lang
    current_lang = lang
    lang_texts = translations[lang]

    # تحديث نصوص عناصر الواجهة
    window.title(lang_texts['window_title'])
    title_label.config(text=lang_texts['title_label'])
    show_password_check.config(text=lang_texts['show_password'])
    login_button.config(text=lang_texts['login_button'])
    forgot_password_label.config(text=lang_texts['forgot_password'])
    lang_label.config(text=lang_texts['lang_label'])
    
    # تحديث النصوص المؤقتة في حقول الإدخال إذا لم يتم التعديل عليها من قبل المستخدم
    if username_entry.get() in [translations['en']['username_placeholder'], translations['ar']['username_placeholder']]:
        username_entry.delete(0, tk.END)
        username_entry.insert(0, lang_texts['username_placeholder'])
        username_entry.config(foreground='gray')
    if password_entry.get() in [translations['en']['password_placeholder'], translations['ar']['password_placeholder']]:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, lang_texts['password_placeholder'])
        password_entry.config(foreground='gray', show="")

    # تعديل المحاذاة للغة العربية
    if lang == 'ar':
        show_password_check.pack_configure(anchor="e")
    else:
        show_password_check.pack_configure(anchor="w")

def login():
    """
    يتم استدعاء هذه الدالة عند الضغط على زر "دخول".
    تقوم بالتحقق من اسم المستخدم وكلمة المرور وتظهر الرسائل المناسبة.
    """
    username = username_entry.get()
    password = password_entry.get()
    lang_texts = translations[current_lang]

    # التحقق من أن الحقول ليست فارغة أو تحتوي على النص المؤقت
    if (username == translations['ar']['username_placeholder'] or
        username == translations['en']['username_placeholder'] or
        password == translations['ar']['password_placeholder'] or
        password == translations['en']['password_placeholder'] or
        not username or not password):
        messagebox.showerror(lang_texts['login_error_title'], lang_texts['login_error_message'])
        return

    # هنا يمكنك وضع منطق التحقق الحقيقي
    if username == "admin" and password == "1234":
        messagebox.showinfo(lang_texts['login_success_title'], lang_texts['login_success_message'].format(username=username))
    else:
        messagebox.showerror(lang_texts['login_error_title'], lang_texts['credentials_error'])

def toggle_password_visibility():
    """
    تقوم هذه الدالة بإظهار أو إخفاء كلمة المرور بناءً على حالة مربع الاختيار.
    """
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# --- دوال النص المؤقت (Placeholder) ---

def on_username_focus_in(event):
    """عندما يتم التركيز على حقل اسم المستخدم، يتم حذف النص المؤقت."""
    if username_entry.get() == translations[current_lang]['username_placeholder']:
        username_entry.delete(0, tk.END)
        username_entry.config(foreground='black')

def on_username_focus_out(event):
    """عندما يتم الخروج من حقل اسم المستخدم وهو فارغ، يتم إعادة النص المؤقت."""
    if not username_entry.get():
        username_entry.insert(0, translations[current_lang]['username_placeholder'])
        username_entry.config(foreground='gray')

def on_password_focus_in(event):
    """عندما يتم التركيز على حقل كلمة المرور، يتم حذف النص المؤقت."""
    if password_entry.get() == translations[current_lang]['password_placeholder']:
        password_entry.delete(0, tk.END)
        password_entry.config(foreground='black', show="*")

def on_password_focus_out(event):
    """عندما يتم الخروج من حقل كلمة المرور وهو فارغ، يتم إعادة النص المؤقت."""
    if not password_entry.get():
        password_entry.insert(0, translations[current_lang]['password_placeholder'])
        password_entry.config(foreground='gray', show="")

# --- إعداد النافذة الرئيسية ---

window = ttk.Window(themename="litera")
window.iconbitmap("log-out_icon-icons.com_50106.ico")
window.resizable(False, False)

# توسيط النافذة على الشاشة
window_width = 400
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# --- إنشاء وتصميم الواجهة ---

# الإطار الرئيسي لتنظيم المحتوى
main_frame = ttk.Frame(window, padding="40 20 40 20")
main_frame.pack(fill=BOTH, expand=True)

# عنوان الواجهة
title_label = ttk.Label(main_frame, font=("Helvetica", 24, "bold"), bootstyle=PRIMARY)
title_label.pack(pady=(0, 30))

# حقل إدخال اسم المستخدم
username_entry = ttk.Entry(main_frame, font=("Helvetica", 12), width=30)
username_entry.pack(pady=10, ipady=8)
username_entry.bind("<FocusIn>", on_username_focus_in)
username_entry.bind("<FocusOut>", on_username_focus_out)

# حقل إدخال كلمة المرور
password_entry = ttk.Entry(main_frame, font=("Helvetica", 12), width=30)
password_entry.pack(pady=10, ipady=8)
password_entry.bind("<FocusIn>", on_password_focus_in)
password_entry.bind("<FocusOut>", on_password_focus_out)

# مربع اختيار لإظهار/إخفاء كلمة المرور
show_password_var = tk.BooleanVar()
show_password_check = ttk.Checkbutton(
    main_frame,
    variable=show_password_var,
    command=toggle_password_visibility,
    bootstyle="primary"
)
show_password_check.pack(pady=(5, 20))

# زر تسجيل الدخول
login_button = ttk.Button(
    main_frame,
    command=login,
    bootstyle=(SUCCESS, OUTLINE),
    width=20
)
login_button.pack(pady=(10, 20), ipady=10, fill=X)

# رابط "هل نسيت كلمة المرور؟"
forgot_password_label = ttk.Label(main_frame, font=("Helvetica", 10), bootstyle=SECONDARY)
forgot_password_label.pack()
forgot_password_label.bind("<Enter>", lambda e: forgot_password_label.config(cursor="hand2"))
forgot_password_label.bind("<Leave>", lambda e: forgot_password_label.config(cursor=""))

# إطار لاختيار اللغة
lang_frame = ttk.Frame(main_frame)
lang_frame.pack(pady=10)

lang_label = ttk.Label(lang_frame, font=("Helvetica", 10))
lang_label.pack(side=LEFT)

lang_combo = ttk.Combobox(
    lang_frame,
    values=['العربية', 'English'],
    state='readonly',
    width=10,
    font=("Helvetica", 10)
)
lang_combo.current(0) # تعيين اللغة الافتراضية
lang_combo.bind("<<ComboboxSelected>>", lambda e: set_language('ar' if lang_combo.get() == 'العربية' else 'en'))
lang_combo.pack(side=RIGHT)

# إعداد اللغة الأولية عند تشغيل التطبيق
set_language(current_lang)

# --- تشغيل التطبيق ---
window.mainloop()
