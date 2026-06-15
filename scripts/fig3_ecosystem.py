import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style_guide import COLORS, set_style

def draw_layer_box(ax, x, y, width, height, title, items, bg_color):
    # Main container
    rect = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                  boxstyle="round,pad=0.2", ec=COLORS['navy'], fc=bg_color, lw=1.5, zorder=2)
    ax.add_patch(rect)
    
    # Title
    ax.text(x, y + height/2 - 0.4, title, ha='center', va='center', 
            color=COLORS['navy'], fontweight='bold', fontsize=12)
            
    # Items (separated by |)
    items_str = "  |  ".join(items)
    ax.text(x, y - 0.2, items_str, ha='center', va='center', 
            color=COLORS['black'], fontsize=10)
    
    return x, y - height/2

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=3, mutation_scale=20), zorder=1)

def generate_fig3():
    set_style()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    plt.title("Integrated Precision Oncology Ecosystem", fontsize=16, fontweight='bold', color=COLORS['navy'], y=0.95)
    
    center_x = 5
    width = 9
    height = 1.8
    gap = 1.2
    
    y = 12
    # Layer 1
    _, b1 = draw_layer_box(ax, center_x, y, width, height, "TECHNOLOGY LAYER", 
                   ["AI", "Radiomics", "Liquid Biopsy", "ctDNA", "Multiomics", "Digital Health"], COLORS['lightgray'])
                   
    draw_arrow(ax, center_x, b1 - 0.1, center_x, b1 - gap + 0.1)
    y -= (height + gap)
    
    # Layer 2
    _, b2 = draw_layer_box(ax, center_x, y, width, height, "CLINICAL INTELLIGENCE LAYER", 
                   ["Early Detection", "Risk Stratification", "Tumor Characterization", "Treatment Selection", "Response Monitoring"], COLORS['lightgray'])

    draw_arrow(ax, center_x, b2 - 0.1, center_x, b2 - gap + 0.1)
    y -= (height + gap)
    
    # Layer 3
    # Different background for the core concept
    rect = patches.FancyBboxPatch((center_x - width/2, y - height/2), width, height, 
                                  boxstyle="round,pad=0.2", ec='none', fc=COLORS['navy'], zorder=2)
    ax.add_patch(rect)
    ax.text(center_x, y, "PRECISION ONCOLOGY LAYER\n\nPersonalized Breast Cancer Management", 
            ha='center', va='center', color=COLORS['white'], fontweight='bold', fontsize=12)
    b3 = y - height/2
            
    draw_arrow(ax, center_x, b3 - 0.1, center_x, b3 - gap + 0.1)
    y -= (height + gap)
    
    # Layer 4
    _, b4 = draw_layer_box(ax, center_x, y, width, height, "CLINICAL OUTCOMES LAYER", 
                   ["Improved Survival", "Reduced Toxicity", "Better Quality of Life"], COLORS['lightgray'])

    out_dir = "../figures"
    os.makedirs(out_dir, exist_ok=True)
    
    plt.savefig(f"{out_dir}/Figure3_Ecosystem.png", dpi=600)
    plt.savefig(f"{out_dir}/Figure3_Ecosystem.pdf")
    plt.savefig(f"{out_dir}/Figure3_Ecosystem.svg")
    plt.close()

if __name__ == "__main__":
    generate_fig3()
    print("Figure 3 generated successfully.")
