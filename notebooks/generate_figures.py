"""
Generates all research figures (Figures 2, 3, 4, 5, 6, 7) and saves them directly into the project's figures/ directory.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 1. DIRECTORY CONFIGURATION
# ==========================================
BASE_DIR = Path.cwd()
# Auto-detect project root whether run from root or notebooks folder
PROJECT_ROOT = BASE_DIR.parent if BASE_DIR.name == "notebooks" else BASE_DIR

DATA_DIR = PROJECT_ROOT / "data"
FIGURES_DIR = PROJECT_ROOT / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned survey data (N=39) if needed for ad-hoc validation
cleaned_data_path = DATA_DIR / "cleaned_survey.csv"
if cleaned_data_path.exists():
    df_cleaned = pd.read_csv(cleaned_data_path)

# ==========================================
# 2. GLOBAL STYLING & COLOR PALETTES
# ==========================================
plt.rcParams['font.family'] = 'sans-serif'
THEME_COLOR = '#83C5BE'
COLOR_3_WEEKS = '#83C5BE'
COLOR_1_2_DAYS = '#F4A261'
STACKED_COLORS = ['#E76F51', '#F4A261', '#83C5BE', '#E5E9E8']


# ==========================================
# FIGURE 2: Current Disposition Methods
# ==========================================
def plot_figure_2():
    data = {
        'Method': [
            'Give away to friends/housemates', 'Throw away', 'Sell', 
            'Give away online', 'Leave for next occupant', 'Recycle', 
            'Donate to charity/op shop', 'Sell online'
        ],
        'Percentage': [82.1, 71.8, 61.5, 33.3, 28.2, 17.9, 15.4, 2.6]
    }
    df2 = pd.DataFrame(data).sort_values('Percentage', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(df2['Method'], df2['Percentage'], color=THEME_COLOR)
    
    # Add percentage labels
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, 
                f"{bar.get_width()}%", va='center', ha='left', fontsize=10)

    ax.set_xlim(0, 100)
    ax.set_xlabel('Respondents (%)')
    ax.set_title('Reported methods used to clear unwanted items (n=39)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'figure_2_fixed.png', dpi=300)
    plt.close()
    print("[OK] Figure 2 saved: figure_2_fixed.png")


# ==========================================
# FIGURE 3: First-choice Option
# ==========================================
def plot_figure_3():
    data = {
        'Option': [
            'Sell', 'Give to friends/housemates', 'Leave for next occupant', 
            'Throw away', 'Give away online', 'Recycle'
        ],
        'Percentage': [43.6, 33.3, 10.3, 7.7, 2.6, 2.6]
    }
    df3 = pd.DataFrame(data).sort_values('Percentage', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(df3['Option'], df3['Percentage'], color=THEME_COLOR, height=0.7)
    
    # Add percentage labels
    for bar in bars:
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, 
                f"{bar.get_width():.1f}%", va='center', ha='left', fontsize=10)

    ax.set_xlim(0, 50)
    ax.set_xlabel('Respondents (%)', fontweight='bold')
    ax.set_title("Respondents' first-choice option for clearing an unwanted item (n=39)", 
                 fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'Figure_3_Modern.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figure 3 saved: Figure_3_Modern.png")


# ==========================================
# FIGURE 4: Awareness and Use of Channels
# ==========================================
def plot_figure_4():
    channels = [
        'Friends/students', 'Social media', 'University groups', 
        'Online marketplaces', 'Charity', 'Other'
    ]
    used = np.array([59.0, 51.3, 33.3, 20.5, 5.1, 2.6])
    considered = np.array([30.8, 25.6, 20.5, 35.9, 23.1, 7.7])
    heard = np.array([7.7, 20.5, 25.6, 33.3, 46.2, 23.1])
    never = np.array([2.6, 2.6, 20.5, 10.3, 25.6, 66.7])

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(channels, used, color=STACKED_COLORS[0], label='Used')
    ax.barh(channels, considered, left=used, color=STACKED_COLORS[1], label='Considered')
    ax.barh(channels, heard, left=used + considered, color=STACKED_COLORS[2], label='Heard of')
    ax.barh(channels, never, left=used + considered + heard, color=STACKED_COLORS[3], label='Never heard of')

    # Add text labels inside bars for readable sections (> 4%)
    for i in range(len(channels)):
        if used[i] > 4:
            ax.text(used[i] / 2, i, f"{used[i]}%", va='center', ha='center', color='white')
        if considered[i] > 4:
            ax.text(used[i] + considered[i] / 2, i, f"{considered[i]}%", va='center', ha='center', color='black')
        if heard[i] > 4:
            ax.text(used[i] + considered[i] + heard[i] / 2, i, f"{heard[i]}%", va='center', ha='center', color='black')
        if never[i] > 4:
            ax.text(used[i] + considered[i] + heard[i] + never[i] / 2, i, f"{never[i]}%", va='center', ha='center', color='black')

    ax.invert_yaxis()
    ax.set_xlabel('Respondents (%)')
    ax.set_title('Awareness and use of redistribution channels (n=39)')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=4, frameon=False)
    ax.set_xlim(0, 100)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'figure_4_fixed.png', dpi=300)
    plt.close()
    print("[OK] Figure 4 saved: figure_4_fixed.png")


# ==========================================
# FIGURE 5: Factors Contributing to Disposal
# ==========================================
def plot_figure_5():
    data = {
        'Factor': [
            'Not sure anyone will want it', 'Too much time to find someone', 
            'Too much effort to arrange', 'Pickup arrangements are inconvenient', 
            'Need to get rid of it quickly', 'Item has little or no monetary value', 
            'Too much messaging or coordination', 'Left it too late to arrange anything', 
            'Recipient is too far away', 'Most people I know were also moving out', 
            'Safety or privacy concern', 'Have never thrown away a usable item'
        ],
        'Percentage': [69.2, 66.7, 64.1, 51.3, 46.2, 41.0, 33.3, 15.4, 12.8, 12.8, 5.1, 2.6]
    }
    df5 = pd.DataFrame(data).sort_values('Percentage', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(df5['Factor'], df5['Percentage'], color=THEME_COLOR)
    
    # Add percentage labels
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, 
                f"{bar.get_width()}%", va='center', ha='left', fontsize=10)

    ax.set_xlim(0, 100)
    ax.set_xlabel('Respondents (%)')
    ax.set_title('Factors contributing to disposal of usable items (n=39)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'figure_5_fixed.png', dpi=300)
    plt.close()
    print("[OK] Figure 5 saved: figure_5_fixed.png")


# ==========================================
# FIGURE 6: Privacy and Safety Concerns
# ==========================================
def plot_figure_6():
    data = {
        'Concern': [
            'Sharing phone number or contact details', 'Sharing home address', 
            'Meeting in a private or unfamiliar location', 'Meeting someone they do not know', 
            'Would not feel uncomfortable'
        ],
        'Percentage': [66.7, 64.1, 64.1, 43.6, 10.3]
    }
    df6 = pd.DataFrame(data).sort_values('Percentage', ascending=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.barh(df6['Concern'], df6['Percentage'], color=THEME_COLOR, height=0.7)
    
    # Add percentage labels
    for bar in bars:
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2, 
                f"{bar.get_width():.1f}%", va='center', ha='left', fontsize=10)

    ax.set_xlim(0, 80)
    ax.set_xlabel('Respondents (%)', fontweight='bold')
    ax.set_title('Specific privacy and safety concerns with stranger handovers (n=39)', 
                 fontweight='bold', pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'Figure_6_Modern.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figure 6 saved: Figure_6_Modern.png")


# ==========================================
# FIGURE 7: Deadline Effect (3 Weeks vs 1-2 Days)
# ==========================================
def plot_figure_7():
    labels = ['Sell', 'Give away', 'Friend / housemate', 'Throw away', 
              'Leave next occupant', 'Recycle', 'Donate']
    three_weeks = [51.3, 15.4, 23.1, 5.1, 2.6, 2.6, 0.0]
    one_two_days = [2.6, 23.1, 15.4, 35.9, 12.8, 7.7, 2.6]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width / 2, three_weeks, width, label='Three weeks remaining', color=COLOR_3_WEEKS)
    rects2 = ax.bar(x + width / 2, one_two_days, width, label='1-2 days remaining', color=COLOR_1_2_DAYS)

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            if height > 0:
                ax.annotate(f"{height:.1f}%",
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=9)

    autolabel(rects1)
    autolabel(rects2)

    ax.set_ylabel('Respondents (%)', fontweight='bold')
    ax.set_title('Intended clearing action as the move-out deadline approaches (n=39)', 
                 fontweight='bold', pad=15)
    ax.set_xticks(x)
    formatted_labels = [label.replace(' ', '\n', 1) if ' ' in label else label for label in labels]
    ax.set_xticklabels(formatted_labels)
    ax.legend(frameon=False)
    ax.set_ylim(0, 60)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'Figure_7_Modern.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figure 7 saved: Figure_7_Modern.png")


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == '__main__':
    print(f"Generating figures into: {FIGURES_DIR.resolve()}\n" + "-" * 50)
    plot_figure_2()
    plot_figure_3()
    plot_figure_4()
    plot_figure_5()
    plot_figure_6()
    plot_figure_7()
    print("-" * 50 + "\nAll figures successfully generated and saved!")
