import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import yfinance as yf

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Evolución del Precio de Acciones'),
    html.Div([
        html.P("Ingresa el símbolo de la acción (ej. AAPL, MSFT, TSLA):"),
        dcc.Input(
            id='input-simbolo',
            type='text',
            value='AAPL',
            debounce=True # Espera a que el usuario presione "Enter" o cambie de foco para disparar el callback
        )
    ], style={'marginBottom': '20px'}),
    
    html.Div(id='mensaje-error', style={'color': 'red', 'fontWeight': 'bold', 'marginBottom': '10px'}),
    
    dcc.Graph(id='grafico-accion')
])

@app.callback(
    [Output('grafico-accion', 'figure'),
     Output('mensaje-error', 'children')],
    [Input('input-simbolo', 'value')]
)
def actualizar_grafico(simbolo):
    if not simbolo:
        return {}, "Por favor, ingresa un símbolo válido."
        
    simbolo = simbolo.upper().strip()
    
    try:
        # Descargamos los datos del último mes usando yfinance
        df = yf.download(simbolo, period='1mo')
        
        if df.empty:
            return {}, f"No se encontraron datos para el símbolo '{simbolo}'."
            
        # Usamos Plotly Express aislando solo la columna 'Close' (Precio de cierre)
        fig = px.line(df, x=df.index, y='Close', title=f'Precio de Cierre de {simbolo} (Último mes)')
        fig.update_layout(template='plotly_white', xaxis_title='Fecha', yaxis_title='Precio de Cierre (USD)')
        return fig, ""
    except Exception as e:
        return {}, f"Ocurrió un error al consultar la acción: {e}"

if __name__ == '__main__':
    app.run(debug=True)