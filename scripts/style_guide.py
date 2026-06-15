import matplotlib.pyplot as plt

# Global color palette
COLORS = {
    'navy': '#1F3A5F',
    'teal': '#2A9D8F',
    'skyblue': '#7DB7D5',
    'orange': '#F4A261',
    'red': '#E76F51',
    'gray': '#6c757d',
    'lightgray': '#e9ecef',
    'white': '#ffffff',
    'black': '#000000'
}

def set_style():
    """Sets the global rcParams for matplotlib to ensure consistent typography and DPI."""
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'DejaVu Sans', 'Helvetica'],
        'font.size': 10,
        'axes.linewidth': 1.5,
        'figure.dpi': 600,
        'savefig.dpi': 600,
        'savefig.bbox': 'tight'
    })
