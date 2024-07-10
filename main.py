from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(exercies_tag: str = None):
    if exercies_tag == None:
        return FileResponse("templates/menu.html")
    else:
        return RedirectResponse(f"/{exercies_tag}", status_code=303)

@app.get("/s1e1")
async def Exercise_S1_E1(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e1.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e1.png"})

@app.get("/s1e2")
async def Exercise_S1_E2(request: Request, scenario: int = None, n_threads: int = 3, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e2.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e2.png"})

@app.get("/s1e3")
async def Exercise_S1_E3(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e3.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e3.png"})

@app.get("/s1e4")
async def Exercise_S1_E4(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e4.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e4.png"})


@app.get("/s1e5")
async def Exercise_S1_E5(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e5.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s1e5.png"})


@app.get("/s1e6")
async def Exercise_S1_E6(request: Request, scenario: int = None, n_threads: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e6.py', str(scenario), str(n_threads)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "threads", "type_value": n_threads, "output": output, "img": "s1e6.png"})


@app.get("/s1e7")
async def Exercise_S1_E7(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s1e7.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s1e7.png"})

@app.get("/s2e1")
async def Exercise_S2_E1(request: Request, scenario: int = None, n_process: int = 5, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e1.py', str(scenario), str(n_process)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "processes", "type_value": n_process, "output": output, "img": "s2e1.png"})

@app.get("/s2e2")
async def Exercise_S2_E2(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e2.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e2.png"})

@app.get("/s2e3")
async def Exercise_S2_E3(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e3.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e3.png"})

@app.get("/s2e4")
async def Exercise_S2_E4(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e4.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e4.png"})

@app.get("/s2e5")
async def Exercise_S2_E5(request: Request, scenario: int = None, n_process: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e5.py', str(scenario), str(n_process)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "processes", "type_value": n_process, "output": output, "img": "s2e5.png"})

@app.get("/s2e6")
async def Exercise_S2_E6(request: Request, scenario: int = None, n_products: int = 5, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e6.py', str(scenario), str(n_products)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "products", "type_value": n_products, "output": output, "img": "s2e6.png"})

@app.get("/s2e7")
async def Exercise_S2_E7(request: Request, scenario: int = None, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e7.py', str(scenario)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "", "output": output, "img": "s2e7.png"})

@app.get("/s2e8")
async def Exercise_S2_E8(request: Request, scenario: int = None, n_inputs: int = 10, Json: int = 0):
    output = "There is nothing to show !!!"
    if scenario != None:
        result = subprocess.run(['python', 'codes/s2e8.py', str(scenario), str(n_inputs)], capture_output=True, text=True)
        output = json.dumps(result.stdout)
        output = eval(output)
    if Json:
        return result
    return templates.TemplateResponse("showcase.html",{"request": request, "scenario": scenario, "type_name": "products", "type_value": n_inputs, "output": output, "img": "s2e8.png"})

@app.get("/s3e1")
async def Exercise_S3_E1():
    return FileResponse("templates/exercises.html")

@app.get("/s3e2")
async def Exercise_S3_E2():
    return FileResponse("templates/exercises.html")

@app.get("/s3e3")
async def Exercise_S3_E3():
    return FileResponse("templates/exercises.html")