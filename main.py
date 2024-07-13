from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess, json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    if "application/json" in request.headers.get("accept", ""):
        return JSONResponse(status_code=404, content={"message": "Oops! The resource you are looking for is not found."},)
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.get("/report")
async def Repoert():
    return FileResponse("Parallelism_Report.pdf", media_type="application/pdf")

@app.get("/")
async def index(exercies_tag: str = None):
    if exercies_tag == None:
        return FileResponse("templates/menu.html")
    else:
        return RedirectResponse(f"/{exercies_tag}", status_code=303)

@app.get("/s1e1")
async def Exercise_S1_E2(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"

    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e1.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)

        description = [
                        "در این سناریو وجود join باعث می شود که ترد اجرایی ابتدا تکمیل شود و سپس ترد بعدی به اجرا برود پس با وجود join بلا فاصله پس از start ترتیب اجرای ترد ها را خواهیم داشت.",
                        "در صورت عدم استفاده از join نحو دیگر اجرای ترتیبی تردها به این صورت می باشد که از یه وقفه زمانی به اندازه حداقل مدت زمان مورد نیاز برای اجرای ترد های فعلی در حال اجرا بهره ببریم که در اینجا 0.3 ثانیه صبر می کنیم و سپس ترد بعدی start می شود.",
                        "نحوه دیگر تضمین ترتیب با وقفه زمانی به این گونه است که از یک زمان افزایشی استفاده کرد، با استفاده از شماره هر ترد و ضرب آن در یک زمان ثابت زمان های از مضرب پایه انتخابی خواهیم داشت که همزمان با هم اجرا شده و در ترد های با شماره کمتر زمان انتظار زودتر به اتمام می رسد.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e1.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 1})

@app.get("/s1e2")
async def Exercise_S1_E2(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e2.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)

        description = [
                        "در این سناریو هر ترد تابع مربوط به خودش را فرا می خواهد، نحوه چاپ ورود به تابع به هر ترتیبی می تواند صورت بگیرد اما معمولا چون در حد چند صدم ثانیه عمل start برای هر ترد تا ترد بعدی زمان می برد ترتیب اجرا را خواهیم داشت و برای ترتیب اجرا در خروجی از وقفه های زمانی تصاعدی بهره گرفته ایم.",
                        "در این سناریو ما اجرای دستور join بعد از هر start را خواهیم داشت که اجرای کامل هر ترد پیش از ارسال ترد بعدی برای اجرا را خواهیم داشت.",
                        "در این پیاده سازی ما از زمان های انتظار نزولی بهره گرفته ایم که با توجه به اجرای با فاصله هر ترد در حد چند صدم ثانیه اجرای معکوس ترد ها موقع ورود و هنگام خروج را خواهیم داشت اما این امر تضمین شده نمی باشد.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s1e2.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 2})

@app.get("/s1e3")
async def Exercise_S1_E3(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e3.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این سناریو به دلیل اجرای با فاصله در حد صدم ثانیه هر ترد ورود به ترتیب به متد های کلاس را خواهیم داشت و اما به هنگام خروج به دلیل وجود وقفه رندوم ترتیب خاصی وجود نخواهد داشت و در نهایت وجود join برای همه ترد ها موجب چاپ زمان اجرا در آخرین مرحله می شود.",
                        "در این سناریو به دلیل عدم وجود وقفه و join نحوه اجرا و خروج از هر ترد کاملا بسته به منابع سیستم دارد و ترتیب های ورود و خروج کاملا به هم ریخنه می باشند.",
                        "این سناریو با قرار دادن وقفه 1 هزارم ثانیه ای نشان می دهد که سرعت انجام یک دستور در ترد در حدود هزارم ثانیه می باشد چرا که این وقفه موجب اجرای کامل ورود ها و سپس اجرای کامل خروج ها شده است و اگر آن را کاهش دهیم مانند سناریو قبل درهم ریختگی را مجددا خواهیم داشت",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e3.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 3})

@app.get("/s1e4")
async def Exercise_S1_E4(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e4.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این سناریو که در واقع مشابه تمرین قبل می باشد مشاهده می شود که با یک زمان ثابت نیم ثانیه ای خروجی قبلی که ترتیب چاپ ورود ها و سپس چاپ خروج ها بود را نداریم و ورود خروج هر ترد پشت سر هم آمده که علت وجود lock می باشد و چون کل متد ما ناحیه بحرانی در نظر گرفته شده تا خروج کامل از ترد سایر ترد ها به حالت انتظار در خواهند آمد.",
                        "در این سناریو برای اثبات عملکرد lock زمان مابین چاپ ورود و خروج برداشته شده است و همانطور که می بینیم ترتیب اجرا با سناریو قبل یکسان خواهد بود.",
                        "در اینجا چون کل اجرای یک ترد ما ناحیه بحرانی اطلاق شده است می توان به جای استفاده از لاک از جوین بهره گرفت و مشاهده کرد که خروجی مشابه سناریوهای قبلی می باشد.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e4.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 4})


@app.get("/s1e5")
async def Exercise_S1_E5(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e5.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این تمرین نحوه کارکرد rlock به چشم می خورد که امکان دریافت چندباره توسط یک ترد را دارا می باشد و اما در این سناریو وجود وقفه 0.2 ثانیه ای موجب اجرای تقریبا یک در میان دو ترد می شود و در نهایت به دلیل بیشتر بودن تعداد اجرای افزایش در آخر فقط ترد افزودن اجرا می شود.",
                        "در اینجا زمان وقفه برداشته شده و می بینیم که به دلیل عدم وجود وقفه ترتیب اجرا تقریبا اجرای کامل یک ترد و سپس دیگری می باشد",
                        "برای اجرای کاملا به ترتیب این دو ترد از Join استفاده شده است در این حالت می توان از rlock نیز استفاده نکرد چرا که در هر واحد زمانی تنها یک ترد به متغیر ناحیه بحرانی ما دسترسی خواهد داشت همچنین به دلیل اینکه عملیات های ما تنها افزایش و کاهش هستند دسترسی همزمان ترد ها مشکلی اجاد نمیکند فقط ترتیب کاهش ها و افزایش ها است که ممکن است مسئله ساز شود.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s1e5.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 5})


@app.get("/s1e6")
async def Exercise_S1_E6(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e6.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا تعداد n جفت ترد به صورت همزمان اجرا شده اند که ترد ابتدایی مصرف کننده است و ترد ثانویه که مدت زمانی را برای اجرا نیاز دارد تولید کننده پس چون ابتدا آیتمی وجود ندارد تمامی ترد های مصرف کننده به حالت تعلیق در آمده و با تولید یک آیتم سمافور افزایش می یابد و یکی از ترد های معلق جهت اجرا آزاد می شود و به همین ترتیب اجرای یک در میان تولید و مصرف را داریم، در صورتی که تولیدی صورت نگیرد مصرف کننده تا ابد در حالت تعلیق می ماند.",
                        "در این حالت تولید کننده به زمان وابسته نمی باشد و میزان حالت هایی که کمبود آیتم داریم و نیاز است تا ترد مصرف کننده ای تعلیق شود کمتر است.",
                        "در این سناریو تولید کننده غیر وابسته به زمان را ابتدا اجرا کرده و سپس مضرف کننده ای را فرا میخوانیم اینگونه دیگر زمان انتظار و تعلیقی را نخواهیم داشت.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e6.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 6})


@app.get("/s1e7")
async def Exercise_S1_E7(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e7.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این تمرین ما به مفهوم مانع اشاره می کنیم که با برخورد 3 ترد با آن اجازه ادامه داده می شود اما در این سناریو نحوه اجرای زمان به این صورت است که رندوم یک زمان به هر ترد اختصاص داده می شود اما زمان تمامی این تردها با هم شروع می شود یعنی این زمان مدت زمان کل ترد از ابتدا تا انتها می باشد  و در اینجا هر ترد ممکن است زودتر به از سایرین به پایان برسد.",
                        "در این سناریو تردی که ابتدا اجرا شده با سپری کردن زمان خود نیز زود تر به پایان می رسد و این زمان ها همچنان رندوم می باشند",
                        "ترد ها با فاصله زمانی 1 ثانیه از یکدیگر به پایان می رسند یعنی زمان بندی به صورت 1، 2، 3 و ... می باشد.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s1e7.png", "description": description[scenario - 1] if scenario else "", "s": 1, "e": 7})

@app.get("/s2e1")
async def Exercise_S2_E1(request: Request, scenario: int = None, n_process: int = 5, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e1.py', str(scenario), str(n_process)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این سناریو شماره هر پراسس به تابع فراخوانی کننده اش ارسال و یک حلقه داخل تابع از صفر تا شماره پراسس چاپ می کند و دستور Join تضمین کننده اجرای ترتیبی است",
                        "در این سناریو به دلیل عدم وجود join تمامی پراسس ها همزمان اجرا شده پیام ورود را چاپ و 0.2 ثانیه انتظار می کشند سپس حلقه تکرار خود را اجرا میکنند که ترتیب اجرایی نخواهیم داشت",
                        "جهت برطرف سازی ضعف ایجاد شده در سناریو قبل می توان از سمافور بهره گرفت اما باید توجه داشت که سمافور به عنوان پارامتر به هر پراسس ارسال شود و حلقه را به عنوان ناحیه بحرانی در نظر گرفت تا چاپ های هر پراسس با دیگری ادغام نشود.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "processes", "type_value": n_process, "output": output, "img": "s2e1.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 1})

@app.get("/s2e2")
async def Exercise_S2_E2(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e2.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در این سناریو هر دو پراسس اجرا شده پیغام ورود را چاپ و سپس خارج می شوند، مشاهده می شود که یک پراسس دارای نام تعیین شده و دیگری دارای یک نام پیشفرض است",
                        "در اینجا ترتیب ورود و خروج ها برای اجرای کامل یک پراسس را با استفاده از join مشاهده می کنیم",
                        "در این سناریو ابتدا تابع با نام تعریف شده استارت شده است اما نام آن را ابتدا نمی بینیم چرا که پراسس فرزند پس از اجرا خود پراسسی را تحت نام insider فراخوانده در این مدت زمان پراسس با نام پیشفرض اجرا شده و پس از وارد شدن به پراسس insider دستور چاپ پراسس والد آن را داریم insider نیز پراسسی را فراخوانده که آرگومان آن None است و اگر مجدد آرگومان 3 ارسال شود فرایند اجرای پراسس های فرزند بی انتها می شد",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e2.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 2})

@app.get("/s2e3")
async def Exercise_S2_E3(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e3.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا 2 پراسس که یکی در حالت بکگراند و دیگری نرمال اجرا می شود داریم و پراسس اول اعداد زوج صفر تا نه و پراسس دوم اعداد فرد را چاپ می کند می بینیم که بکگراند پراسس تعاملی با خروجی ندارد",
                        "در اینجا شرایط بکگراند بودن را برای پراسس ابتدایی برداشته و مشاهده می شود که تمامی اعداد صفر تا نه ما بین یکدیگر و به صورت تقریبا ترتیبی چاپ می شوند  ( در FastAPI به دلیل اینکه اصل کد خود به عنوان پراسس فرزند اجرا می شود خروجی های هر پراسس تجمیع شده و سپس نمایش داده می شود )",
                        "جهت درک بهتر تعاملی بودن و اینکه کدام خروجی مربوط به کدام پراسس است از join استفاده می کنیم تا متوجه بشیم خروجی ای که در سناریو ابتدایی وجود نداشته است دقیقا چه مواردی بوده اند",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e3.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 3})

@app.get("/s2e4")
async def Exercise_S2_E4(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e4.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا مشاهده می شود که یک پراسس ما پیش از اجرا حالت اجرای False هنگام اجرا True موقع Terminate به دلیل اینکه کمی این امر زمانبر است همچنان True اما چون پراسس متوقف شده خروجی تابع را نخواهیم دید و پس از این امر با دستور جوین False خواهد بود همچنین کد خروج ما منفی می باشد به این دلیل که سیگنالی خارجی موجب توقف پراسس شده است",
                        "اینبار پیش از Terminate کردن پراسس کمی به اجرای پراسس زمان می دهیم تا مشاهده شود پراسس در حال اجرا و چاپ خروجی است سپس آن را Terminate می کنیم.",
                        "گفته شد هنگام تغییر وضعیت پراسس کمی زمانبر است تا حالت درست آن به نمایش در آید پس اینبار مقداری وقفه زمانی پیش از چاپ وضعیت Terminated اضافه کردیم می بینیم که پس از آن وضعیت اجرا False است.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e4.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 4})

@app.get("/s2e5")
async def Exercise_S2_E5(request: Request, scenario: int = None, n_process: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e5.py', str(scenario), str(n_process)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا پراسس های اجرا شده یک شی از کلاس مالتی پراسسینگ هستند که هرکدام نام خود را دارا می باشند و بخاطر وجود join ترتیب اجرای آنها قابل مشاهده است",
                        "در اینجا join برداشته شده است و ترتیب خروجی ها نیز تغییر امکان تغییر دارد",
                        "در این سناریو یک در میان برای هر پراسس جوین را خواهیم داشت که ترتیب در پراسس های زوج را به ارمغان می آورد و امکان اجرای متغیر در پراسس های فرد را خواهیم داشت",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "processes", "type_value": n_process, "output": output, "img": "s2e5.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 5})

@app.get("/s2e6")
async def Exercise_S2_E6(request: Request, scenario: int = None, n_products: int = 5, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e6.py', str(scenario), str(n_products)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا پراسس های تولید کننده و مصرف کننده با هم شروع به اجرا می کنند و چون تولید کننده کمی زود تر شروع به اجرا کرده روند تولید را داریم و از این پس زمان تولید مجدد 2 برابر کمتر از مصرف است پس تا انتها تولید و مصرف ترتیبی را خواهیم داشت",
                        "در اینجا ابتدا یک آیتم تولید می شود و مصرف کننده نیز آن را مصرف می کند اما چون مدت زمان انتظار مصرف کننده کوتاه است پیش از تولید آیتم بعدی اجرا شده و به دلیل عدم وجود آیتم متوقف می شود و از این پس تنها تولید بدون مصرف خواهیم داشت",
                        "در این سناریو تولید کننده زمان انتظار ندارد پس به محض اجرا تعداد آیتم های تعیین شده را تولید میکنید و سپس مصرف کننده می تواند به مصرف بپردازد",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "products", "type_value": n_products, "output": output, "img": "s2e6.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 6})

@app.get("/s2e7")
async def Exercise_S2_E7(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e7.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا 2 پراسس 1 و 2 به دلیل اینکه با مانع اجرا می شوند تا هر دو به مانع برسند کمی زمان می برد پس اپتدا پراسس 3 و 4 را خواهیم داشت و سپس 1 و 2",
                        "در اینجا مانع برداشته شده و امکان اجرا به هر ترتیبی امکان دارد و منطقا انتظار می رود پراسس 1 اول اجرا شود اما چون در تابع اجرایی این پراسس یک شرط اضافه به نسبت پراسس 3 و 4 وجود دارد ابتدا براسس 3 سپس 1 اجرا می شود اما چون در این حین پراسس 2 فرصت داشته ترتیب 2 و 4 به هر طریقی ممکن است",
                        "در اینجا جوین مابین جفت پراسس های 1،2 و 3،4 داریم که ترتیب اجرایی را تنها به 2 گروه تقسیم می کند ابتدا 1 و 2 اجرا می شوند و کاملا همزمان هستند پس ترتیبی ما بین 1 و 2 نیست سپس 3 و 4 که این دو نیز بدین شکل هستند.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e7.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 7})

@app.get("/s2e8")
async def Exercise_S2_E8(request: Request, scenario: int = None, n_inputs: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e8.py', str(scenario), str(n_inputs)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
        
        description = [
                        "در اینجا با تابع map به pool پردازنده ها مقادیر و تابع مد نظر را می فرستیم و خروجی را دریافت میکنیم و لیستی از مقادیر خروجی با همان ترتیب ورودی با اینکه یک وقفه رندوم ایجاد کرده ایم خواهیم داشت.",
                        "در این سناریو برسی می شود تا علت ترتیب آیتم ها با وجود وقفه رندوم مشخص گردد و قبل مشاهده است که تابع مپ نتایج خروجی را به صورت تصادفی جمع آوری و در نهایت همه را تجمیع و باز گردانی می کند و اگر پیش از تجمیع نتایج نمایش داده شوند بدون ترتیب خواهند بود",
                        "در این سناریو برسی می شود تاثیر join بر حالت نهایی و ترتیب گونه خروجی مپ چگونه است، با برداشتن این دستور مشاهده می شود که تاثیری در ترتیب خرجی حتی با وقفه های نا منظم نخواهیم داشت و تنها تاثیر join در اینجا موارد اجرایی پس از این دستور مپ می باشد.",
                    ]
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "products", "type_value": n_inputs, "output": output, "img": "s2e8.png", "description": description[scenario - 1] if scenario else "", "s": 2, "e": 8})

@app.get("/s3e1")
async def Exercise_S3_E1():
    return FileResponse("templates/404.html")

@app.get("/s3e2")
async def Exercise_S3_E2():
    return FileResponse("templates/404.html")

@app.get("/s3e3")
async def Exercise_S3_E3():
    return FileResponse("templates/404.html")