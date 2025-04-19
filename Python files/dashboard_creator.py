import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

class CyberSecurityDashboard:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = pd.read_csv(self.data_file)
        self.industry_avg = self.data.groupby("TargetIndustry")["FinancialLoss"].mean()
        self.app = dash.Dash(__name__)
        self.setup_layout()
        self.setup_callbacks()
    
    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1("Cybersecurity Threats Dashboard"),

            html.Label("Select Industry for Benchmarking:"),
            dcc.Dropdown(
                id='industry-dropdown',
                options=[{'label': c, 'value': c} for c in self.data['TargetIndustry'].dropna().unique()],
                value=self.data['TargetIndustry'].dropna().unique()[0]
            ),
            dcc.Graph(id='benchmarking-treemap'),  

            html.Label("Adjust Attack Severity Impact (%):"),
            dcc.Slider(
                id='severity-slider',
                min=-50, max=100, step=5, value=0,
                marks={i: f"{i}%" for i in range(-50, 101, 25)}
            ),
            dcc.Graph(id='severity-area-chart'),  

            html.Label("Select Metrics to Display:"),
            dcc.Checklist(
                id='metrics-checklist',
                options=[
                    {'label': 'Financial Loss', 'value': 'FinancialLoss'},
                    {'label': 'Affected Users', 'value': 'NumberofAffectedUsers'},
                    {'label': 'Resolution Time', 'value': 'IncidentResolutionTime'}
                ],
                value=['FinancialLoss']
            ),
            dcc.Graph(id='metrics-heatmap'),  

            html.Label("Cybersecurity Incidents by Country:"),
            dcc.Graph(id='country-map'),  

            html.Label("Security Vulnerabilities Analysis:"),
            dcc.Graph(id='vulnerability-sunburst')  
        ])
    
    def setup_callbacks(self):
        @self.app.callback(
            Output('benchmarking-treemap', 'figure'),
            Input('industry-dropdown', 'value')
        )
        @self.app.callback(
    Output('benchmarking-plot', 'figure'),
    Input('industry-dropdown', 'value')
)
        def update_benchmarking_plot(selected_industry):
            industry_data = self.data[self.data['TargetIndustry'] == selected_industry]
            
            # Drop rows with missing values in Attack_Type
            industry_data = industry_data.dropna(subset=['AttackType'])
            
            if industry_data.empty:
                return px.treemap(title="No Data Available")
        
            fig = px.treemap(
                industry_data, 
                path=['TargetIndustry', 'AttackType'], 
                values='FinancialLoss', 
                title=f"Benchmarking: Financial Loss by Industry and Attack Type"
            )
            return fig

        
        @self.app.callback(
            Output('severity-area-chart', 'figure'),
            Input('severity-slider', 'value')
        )
        def update_severity_area_chart(severity_change):
            modified_data = self.data.copy()
            modified_data['Adjusted_Loss'] = modified_data['FinancialLoss'] * (1 + severity_change / 100)
            fig = px.area(modified_data, x='Year', y='Adjusted_Loss', color='TargetIndustry',
                          title="Impact of Attack Severity Over Time")
            return fig
        
        @self.app.callback(
            Output('metrics-heatmap', 'figure'),
            Input('metrics-checklist', 'value')
        )
        def update_metrics_heatmap(selected_metrics):
            if not selected_metrics:
                return px.imshow([[0]], title="No Metrics Selected")
            
            heatmap_data = self.data.pivot_table(index='Year', columns='TargetIndustry', values=selected_metrics, aggfunc='sum')
            fig = px.imshow(heatmap_data, aspect="auto", title="Cybersecurity Metrics Heatmap")
            fig.update_layout(width=500, height=400)

            return fig
        
        @self.app.callback(
            Output('country-map', 'figure'),
            Input('industry-dropdown', 'value')
        )
        def update_country_map(selected_industry):
            country_data = self.data.groupby('Country')['FinancialLoss'].sum().reset_index()
            fig = px.choropleth(country_data, locations='Country', locationmode='country names',
                                color='FinancialLoss', title="Cybersecurity Incidents by Country")
            return fig

        @self.app.callback(
    Output('vulnerability-sunburst', 'figure'),
    Input('industry-dropdown', 'value')
)
        def update_vulnerability_sunburst(selected_industry):
            # Filter data for the selected industry
            vulnerability_data = self.data[self.data['TargetIndustry'] == selected_industry].copy()
        
            # Handle missing values
            vulnerability_data['SecurityVulnerabilityType'] = vulnerability_data['SecurityVulnerabilityType'].fillna("Unknown")
            vulnerability_data['AttackType'] = vulnerability_data['AttackType'].fillna("Unknown")
        
            # Ensure no empty values
            vulnerability_data = vulnerability_data.dropna(subset=['FinancialLoss'])  # Drop rows where Financial_Loss_ is NaN
        
            # Create Sunburst Chart
            fig = px.sunburst(
                vulnerability_data, 
                path=['SecurityVulnerabilityType', 'AttackType'], 
                values='FinancialLoss', 
                title="Security Vulnerabilities Breakdown"
            )
            
            return fig


    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    dashboard = CyberSecurityDashboard("GCST - Python.csv")
    dashboard.run()
