#SOTO JONATAN DNI N° 41.118.434

import pytest
import re 
from datetime import datetime

resultados_suite = []

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Módulo que captura si cada test pasó o falló."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call":
        nombre_limpio = item.name.replace("test_", "").replace("_", " ")
        nombre_separado = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', nombre_limpio)
        nombre_test = nombre_separado.title()
        nombre_test = nombre_separado.title().replace(" Y ", " y ")
        
        descripcion = item.obj.__doc__ or "Sin descripción técnica."
        estado = "PASSED" if rep.passed else "FAILED"
        
        resultados_suite.append({
            "nombre": nombre_test,
            "descripcion": descripcion,
            "estado": estado,
            "duracion": round(rep.duration, 2)
        }) 

def pytest_sessionfinish(session, exitstatus):
    """
    Hook de cierre de Pytest. Cuando todos los tests terminan,
    toma los resultados y diseña el HTML hecho desde cero.
    """
    if not resultados_suite:
        return

    ahora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    total = len(resultados_suite)
    pasados = sum(1 for t in resultados_suite if t["estado"] == "PASSED")
    fallados = total - pasados
    
    color_status = "#10b981" if fallados == 0 else "#ef4444"
    texto_status = "EXITOSA" if fallados == 0 else "CON FALLAS"

    # Determinar el nombre de archivo y títulos dinámicamente según la suite ejecutada
    archivo_origen = session.items[0].fspath.basename if session.items else ""
    if "Sitio2" in archivo_origen or "api" in archivo_origen.lower():
        nombre_archivo = "reporte_sitio2.html"
        titulo_principal = "Reporte de Automatización de APIs - SOTO JONATAN"
        subtitulo_principal = "Ecosistema de Pruebas de Servicios - PokeAPI"
    else:
        nombre_archivo = "reporte_sitio1.html"
        titulo_principal = "Reporte de Automatización Web - SOTO JONATAN"
        subtitulo_principal = "Ecosistema de Pruebas - Sitio SauceDemo"

    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Automatización</title>
    <style>
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background-color: #f3f4f6;
            color: #1f2937;
            margin: 0;
            padding: 40px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            color: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }}
        .header h1 {{ margin: 0; font-size: 28px; font-weight: 700; }}
        .header p {{ margin: 5px 0 0 0; opacity: 0.9; font-size: 14px; }}
        
        .grid-stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            text-align: center;
        }}
        .card-title {{ font-size: 12px; text-transform: uppercase; color: #6b7280; font-weight: 600; letter-spacing: 0.5px; }}
        .card-value {{ font-size: 24px; font-weight: 700; margin-top: 5px; }}
        
        .status-badge-suite {{
            background-color: {color_status};
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }}
        
        .table-container {{
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}
        th {{
            background-color: #f8fafc;
            color: #475569;
            padding: 16px;
            font-size: 13px;
            font-weight: 600;
            border-bottom: 2px solid #e2e8f0;
        }}
        td {{
            padding: 18px 16px;
            font-size: 14px;
            border-bottom: 1px solid #f1f5f9;
        }}
        tr:hover td {{ background-color: #f8fafc; }}
        
        .badge-passed {{
            background-color: #d1fae5;
            color: #065f46;
            padding: 6px 12px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 12px;
            display: inline-block;
        }}
        .badge-failed {{
            background-color: #fee2e2;
            color: #991b1b;
            padding: 6px 12px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 12px;
            display: inline-block;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{titulo_principal}</h1>
            <p>{subtitulo_principal}</p>
        </div>
        
        <div class="grid-stats">
            <div class="card">
                <div class="card-title">Ejecución</div>
                <div class="card-value" style="font-size: 14px; color: #374151; margin-top: 12px;">{ahora}</div>
            </div>
            <div class="card">
                <div class="card-title">Tests Totales</div>
                <div class="card-value" style="color: #2563eb;">{total}</div>
            </div>
            <div class="card">
                <div class="card-title">Casos Pasados</div>
                <div class="card-value" style="color: #10b981;">{pasados}</div>
            </div>
            <div class="card">
                <div class="card-title">Estado Final</div>
                <div class="status-badge-suite">{texto_status}</div>
            </div>
        </div>

        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th style="width: 25%;">Caso de Prueba</th>
                        <th style="width: 45%;">Descripción del Escenario</th>
                        <th style="width: 15%;">Duración</th>
                        <th style="width: 15%;">Resultado</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for t in resultados_suite:
        badge = f'<span class="badge-passed">PASSED</span>' if t["estado"] == "PASSED" else f'<span class="badge-failed">FAILED</span>'
        html_content += f"""
                    <tr>
                        <td style="font-weight: 600; color: #1e3a8a;">{t["nombre"]}</td>
                        <td style="color: #4b5563;">{t["descripcion"]}</td>
                        <td style="color: #6b7280; font-family: monospace;">{t["duracion"]} seg</td>
                        <td>{badge}</td>
                    </tr>
        """
        
    html_content += f"""
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
    """
    
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"\nSe ha generado el archivo con diseño moderno: '{{nombre_archivo}}'")
    
    resultados_suite.clear()