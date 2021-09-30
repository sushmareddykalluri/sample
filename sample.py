from dash import html
import dash

app=dash.Dash(__name__)

app.layout=html.Div(
    children=("Hi This is my Dash")
)

if __name__=="__main__":
    app.run_server()