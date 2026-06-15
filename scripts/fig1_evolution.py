import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style_guide import COLORS, set_style

def generate_fig1():
    set_style()
    fig, ax = plt.subplots(figsize=(14, 3))
    ax.axis('off')
    
    eras = [
        {"year": "2000s", "title": "Chemotherapy Era"},
        {"year": "2005", "title": "Molecular\nClassification"},
        {"year": "2010", "title": "Genomic\nProfiling"},
        {"year": "2015", "title": "Targeted\nTherapy"},
        {"year": "2018", "title": "Immunotherapy"},
        {"year": "2020", "title": "ADC\nRevolution"},
        {"year": "2026+", "title": "Precision\nOncology"}
    ]
    
    n = len(eras)
    
    for i, era in enumerate(eras):
        # Draw box
        rect = patches.FancyBboxPatch((i*2.2 - 0.9, -0.6), 1.8, 1.2, 
                                      boxstyle="round,pad=0.1", ec=COLORS['navy'], fc=COLORS['lightgray'], lw=2, zorder=2)
        ax.add_patch(rect)
        
        ax.text(i*2.2, 0.2, era['year'], ha='center', va='center', fontweight='bold', fontsize=12, color=COLORS['navy'])
        ax.text(i*2.2, -0.2, era['title'], ha='center', va='center', fontsize=11, color=COLORS['black'])
        
        if i < n - 1:
            # Draw arrow
            ax.annotate('', xy=(i*2.2 + 1.2, 0), xytext=(i*2.2 + 0.9, 0),
                        arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=3, mutation_scale=15))
            
    ax.set_xlim(-1.5, n*2.2)
    ax.set_ylim(-1.5, 2.5)
    plt.title("Evolution of Breast Cancer Management", fontsize=16, fontweight='bold', color=COLORS['navy'], y=0.9)
    
    # Save outputs
    out_dir = "../figures"
    os.makedirs(out_dir, exist_ok=True)
    
    plt.savefig(f"{out_dir}/Figure1_Timeline.png", dpi=600)
    plt.savefig(f"{out_dir}/Figure1_Timeline.pdf")
    plt.savefig(f"{out_dir}/Figure1_Timeline.svg")
    plt.close()

if __name__ == "__main__":
    generate_fig1()
    print("Figure 1 generated successfully.")
