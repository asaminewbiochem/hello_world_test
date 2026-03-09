import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Re-creating the data
data = {
    "GPU Model": [
        "Nvidia T4", "Nvidia T4", "Nvidia T4", "Nvidia T4",
        "Nvidia L4", "Nvidia L4", "Nvidia L4", "Nvidia L4",
        "Nvidia V100", "Nvidia V100", "Nvidia V100", "Nvidia V100",
        "Nvidia A100 40GB", "Nvidia A100 40GB", "Nvidia A100 40GB", "Nvidia A100 40GB"
    ],
    "Performance (ns/day)": [
        660, 235, 180, 98, 1420, 490, 360, 200, 1190, 645, 510, 330, 1580, 870, 680, 460
    ],
    "Scaling Factor": [
        0.465, 0.480, 0.500, 0.490, 1.000, 1.000, 1.000, 1.000, 0.838, 1.316, 1.417, 1.650, 1.113, 1.776, 3.400, 2.300
    ],
    "Cost ($/hr)": [
        0.28, 0.28, 0.28, 0.28, 0.77, 0.77, 0.77, 0.77, 1.77, 1.77, 1.77, 1.77, 3.67, 3.67, 3.67, 3.67
    ],
    "Atoms": [19000, 62000, 75000, 145000, 19000, 62000, 75000, 145000, 19000, 62000, 75000, 145000, 19000, 62000, 75000, 145000],
    "Tokens/GPU": [8, 8, 8, 8, 16, 16, 16, 16, 16, 16, 16, 16, 22, 22, 22, 22],
    "Molecule Type": [
        "gRNA 11 base pairs", "gRNA 21 base pairs", "ADAR + RNA duplex", "gRNA 31 base pairs",
        "gRNA 11 base pairs", "gRNA 21 base pairs", "ADAR + RNA duplex", "gRNA 31 base pairs",
        "gRNA 11 base pairs", "gRNA 21 base pairs", "ADAR + RNA duplex", "gRNA 31 base pairs",
        "gRNA 11 base pairs", "gRNA 21 base pairs", "ADAR + RNA duplex", "gRNA 31 base pairs"
    ],
    "GPU Version": [
        "T4 Version: v68", "T4 Version: v68", "T4 Version: v68", "T4 Version: v68",
        "L4 Version: v68", "L4 Version: v68", "L4 Version: v68", "L4 Version: v68",
        "V100 Version: v68", "V100 Version: v68", "V100 Version: v68", "V100 Version: v68",
        "A100-40gb Version: v68", "A100-40gb Version: v68", "A100-40gb Version: v68", "A100-40gb Version: v68"
    ],
    "Processors": [32, 32, 32, 32, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 12, 12],
    "Machine Type": [
        "n1-standard-32", "n1-standard-32", "n1-standard-32", "n1-standard-32",
        "g2-standard-4", "g2-standard-4", "g2-standard-4", "g2-standard-4",
        "n1-standard-8", "n1-standard-8", "n1-standard-8", "n1-standard-8",
        "a2-highgpu-1g", "a2-highgpu-1g", "a2-highgpu-1g", "a2-highgpu-1g"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Adding Performance/Cost Ratio
df["Total Cost ($/hr)"] = df["Cost ($/hr)"] + (df["Tokens/GPU"] * 0.10)  # Assuming token cost is $0.10
df["Performance/Cost Ratio"] = (df["Performance (ns/day)"] / df["Total Cost ($/hr)"]).round(2)

# Plot: Cost vs. Performance (ns/day) with GPU Model Color-Coded
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=df,
    x="Performance (ns/day)",
    y="Total Cost ($/hr)",
    hue="GPU Model",
    palette="tab10",
    s=100,
    edgecolor="w"
)
plt.title("Cost vs. Performance (ns/day) by GPU Model", fontsize=14)
plt.xlabel("Performance (ns/day)", fontsize=12)
plt.ylabel("Total Cost ($/hr)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="GPU Model", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

# Plot: Trendlines for Cost vs. Performance by GPU Model
sns.lmplot(
    data=df,
    x="Performance (ns/day)",
    y="Total Cost ($/hr)",
    hue="GPU Model",
    palette="tab10",
    height=8,
    aspect=1.5,
    markers=["o", "s", "D", "^"],
    ci=None
)
plt.title("Cost vs. Performance Trendlines by GPU Model", fontsize=14)
plt.xlabel("Performance (ns/day)", fontsize=12)
plt.ylabel("Total Cost ($/hr)", fontsize=12)
plt.tight_layout()
plt.show()



# Create a bar plot for Performance/Cost Ratio by number of atoms
plt.figure(figsize=(12, 6))
sns.barplot(
    data=df,
    x="Atoms",
    y="Performance/Cost Ratio",
    hue="GPU Model",
    palette="tab10"
)
plt.title("Performance/Cost Ratio by Number of Atoms", fontsize=14)
plt.xlabel("Number of Atoms", fontsize=12)
plt.ylabel("Performance/Cost Ratio", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(title="GPU Model", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
