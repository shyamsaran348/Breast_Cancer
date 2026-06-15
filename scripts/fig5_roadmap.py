import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style_guide import COLORS, set_style

def draw_column(ax, x, y, width, height, title, items, bg_color, bullet_color=COLORS['black']):
    rect = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                  boxstyle="round,pad=0.2", ec='none', fc=bg_color, zorder=2)
    ax.add_patch(rect)
    
    # Title
    ax.text(x, y + height/2 - 0.6, title, ha='center', va='center', 
            color=COLORS['white'], fontweight='bold', fontsize=12)
            
    # Bullet points
    y_bullet = y + height/2 - 1.5
    for item in items:
        ax.text(x - width/2 + 0.4, y_bullet, f"• {item}", ha='left', va='center', 
                color=bullet_color, fontsize=11)
        y_bullet -= 0.8
        
    return x + width/2

def generate_fig5():
    set_style()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    plt.title("The Future Roadmap of Precision Oncology to 2030", fontsize=16, fontweight='bold', color=COLORS['navy'], y=0.95)
    
    width = 3.5
    height = 5.5
    y_center = 4
    
    # Column 1
    x1_right = draw_column(ax, 2.5, y_center, width, height, "CURRENT STATE\n(2026)", 
                ["AI-Assisted Diagnosis", "Static Liquid Biopsy", "ADCs", "HER2-Low Targeting"], COLORS['skyblue'])
                
    # Arrow 1
    ax.annotate('', xy=(x1_right + 0.8, y_center), xytext=(x1_right + 0.1, y_center),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=4, mutation_scale=20))
                
    # Column 2
    x2_right = draw_column(ax, x1_right + 2.5, y_center, width, height, "EMERGING\nINNOVATIONS", 
                ["Multiomics Integration", "Digital Twins", "Next-Generation ADCs", "Adaptive Clinical Trials", "Real-time ctDNA"], COLORS['teal'])
                
    # Arrow 2
    ax.annotate('', xy=(x2_right + 0.8, y_center), xytext=(x2_right + 0.1, y_center),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['navy'], lw=4, mutation_scale=20))
                
    # Column 3
    draw_column(ax, x2_right + 2.5, y_center, width, height, "2030 VISION\n(FUTURE)", 
                ["Fully Personalized Therapy", "Continuous Monitoring", "AI Decision Support", "Precision Survivorship"], COLORS['navy'], bullet_color=COLORS['white'])

    out_dir = "../figures"
    os.makedirs(out_dir, exist_ok=True)
    
    plt.savefig(f"{out_dir}/Figure5_Roadmap.png", dpi=600)
    plt.savefig(f"{out_dir}/Figure5_Roadmap.pdf")
    plt.savefig(f"{out_dir}/Figure5_Roadmap.svg")
    plt.close()

if __name__ == "__main__":
    generate_fig5()
    print("Figure 5 generated successfully.")
