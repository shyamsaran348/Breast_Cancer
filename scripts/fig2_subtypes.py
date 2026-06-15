import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from style_guide import COLORS, set_style

def draw_box(ax, x, y, width, height, text, bg_color, text_color=COLORS['white']):
    # Center x, y
    rect = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                  boxstyle="round,pad=0.2", ec='none', fc=bg_color, zorder=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', color=text_color, fontweight='bold', fontsize=10, zorder=3)
    return x, y - height/2

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=COLORS['gray'], lw=2, mutation_scale=15), zorder=1)

def generate_fig2():
    set_style()
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 11)
    ax.axis('off')
    
    plt.title("Molecular Subtypes and Precision Treatment Framework", fontsize=16, fontweight='bold', color=COLORS['navy'], pad=20)
    
    # Root
    rx, ry_bottom = draw_box(ax, 0, 10, 4, 1.2, "Breast Cancer", COLORS['navy'])
    
    # Subtypes
    subtypes = [
        {"x": -4.5, "name": "Luminal A\n(HR+, HER2-)", "color": COLORS['skyblue'], "tx": "Endocrine\nTherapy"},
        {"x": -2.25, "name": "Luminal B\n(HR+, HER2+/-)", "color": COLORS['teal'], "tx": "Endocrine +\nTargeted/Chemo"},
        {"x": 0, "name": "HER2-Enriched\n(HR-, HER2+)", "color": COLORS['orange'], "tx": "Anti-HER2\nTargeted Therapy"},
        {"x": 2.25, "name": "TNBC\n(HR-, HER2-)", "color": COLORS['red'], "tx": "Chemotherapy +\nImmunotherapy"},
        {"x": 4.5, "name": "HER2-Low\n(IHC 1+/2+, ISH-)", "color": COLORS['navy'], "tx": "Antibody-Drug\nConjugates (T-DXd)"}
    ]
    
    for st in subtypes:
        # Draw line from root to subtype
        draw_arrow(ax, 0, ry_bottom - 0.1, st['x'], 7.6)
        
        # Subtype box
        sx, sy_bottom = draw_box(ax, st['x'], 7, 2, 1.2, st['name'], st['color'])
        
        # Draw arrow to treatment
        draw_arrow(ax, st['x'], sy_bottom - 0.1, st['x'], 4.6)
        
        # Treatment box (lighter background)
        _, ty_bottom = draw_box(ax, st['x'], 4, 2, 1.2, st['tx'], COLORS['lightgray'], text_color=COLORS['black'])
        
        # Draw arrow to prognosis
        draw_arrow(ax, st['x'], ty_bottom - 0.1, st['x'], 1.6)

    # Prognosis boxes
    prognoses = [
        {"x": -4.5, "text": "Favorable Prognosis"},
        {"x": -2.25, "text": "Intermediate\nPrognosis"},
        {"x": 0, "text": "Improved Survival\n(with Anti-HER2)"},
        {"x": 2.25, "text": "Aggressive Disease"},
        {"x": 4.5, "text": "Emerging Category"}
    ]
    
    for prog in prognoses:
        draw_box(ax, prog['x'], 1, 2, 1.0, prog['text'], COLORS['navy'], text_color=COLORS['white'])

    out_dir = "../figures"
    os.makedirs(out_dir, exist_ok=True)
    
    plt.savefig(f"{out_dir}/Figure2_Subtypes.png", dpi=600)
    plt.savefig(f"{out_dir}/Figure2_Subtypes.pdf")
    plt.savefig(f"{out_dir}/Figure2_Subtypes.svg")
    plt.close()

if __name__ == "__main__":
    generate_fig2()
    print("Figure 2 generated successfully.")
