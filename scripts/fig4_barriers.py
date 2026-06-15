import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style_guide import COLORS, set_style

def generate_fig4():
    set_style()
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    plt.title("Barriers to Optimal Breast Cancer Care", fontsize=16, fontweight='bold', color=COLORS['navy'], y=0.95)
    
    # Trapezoids
    # Top width = 6, Bottom width = 8, Height = 1.5
    layers = [
        {"y": 9, "w_top": 4, "w_bot": 6, "color": COLORS['orange'], "text": "HEALTHCARE SYSTEM BARRIERS\nLack of infrastructure, specialized workforce shortages"},
        {"y": 7, "w_top": 6, "w_bot": 8, "color": COLORS['red'], "text": "SOCIOECONOMIC BARRIERS\nFinancial toxicity, lack of insurance coverage"},
        {"y": 5, "w_top": 8, "w_bot": 10, "color": '#8B0000', "text": "PATIENT-LEVEL BARRIERS\nHealth literacy, stigma, logistical challenges"} # Dark red
    ]
    
    center_x = 5
    
    for l in layers:
        y_top = l['y'] + 0.75
        y_bot = l['y'] - 0.75
        
        x_tl = center_x - l['w_top']/2
        x_tr = center_x + l['w_top']/2
        x_bl = center_x - l['w_bot']/2
        x_br = center_x + l['w_bot']/2
        
        poly = patches.Polygon([[x_tl, y_top], [x_tr, y_top], [x_br, y_bot], [x_bl, y_bot]], 
                               closed=True, edgecolor='white', facecolor=l['color'], lw=2, zorder=2)
        ax.add_patch(poly)
        
        ax.text(center_x, l['y'], l['text'], ha='center', va='center', color=COLORS['white'], fontweight='bold', fontsize=11, zorder=3)
        
    # Draw arrow from pyramid to intermediate box
    ax.annotate('', xy=(center_x, 3.1), xytext=(center_x, 4.0),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=4, mutation_scale=20), zorder=1)
                
    # Intermediate box
    rect = patches.FancyBboxPatch((center_x - 3.5, 2.1), 7, 1.0, 
                                  boxstyle="round,pad=0.2", ec='none', fc=COLORS['gray'], zorder=2)
    ax.add_patch(rect)
    ax.text(center_x, 2.6, "Delayed Diagnosis & Suboptimal Adherence", ha='center', va='center', color=COLORS['white'], fontweight='bold', fontsize=11, zorder=3)
    
    # Draw arrow to Outcomes
    ax.annotate('', xy=(center_x, 1.1), xytext=(center_x, 1.9),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=4, mutation_scale=20), zorder=1)

    # Outcomes box
    rect2 = patches.FancyBboxPatch((center_x - 2, 0.1), 4, 1.0, 
                                  boxstyle="round,pad=0.2", ec='none', fc=COLORS['navy'], zorder=2)
    ax.add_patch(rect2)
    ax.text(center_x, 0.6, "NEGATIVE OUTCOMES", ha='center', va='center', color=COLORS['white'], fontweight='bold', fontsize=12, zorder=3)

    out_dir = "../figures"
    os.makedirs(out_dir, exist_ok=True)
    
    plt.savefig(f"{out_dir}/Figure4_Barriers.png", dpi=600)
    plt.savefig(f"{out_dir}/Figure4_Barriers.pdf")
    plt.savefig(f"{out_dir}/Figure4_Barriers.svg")
    plt.close()

if __name__ == "__main__":
    generate_fig4()
    print("Figure 4 generated successfully.")
