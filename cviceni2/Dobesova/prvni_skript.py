import geopandas as gpd # Import the Geopandas package
import matplotlib.pyplot as plt # Import the Matplotlib package
import matplotlib.patches as mpatches # Import the Matplotlib package (patches module)

# Set the population threshold values
thresholds = [100000000, 300000000, 500000000]

# Loop through the threshold values
for threshold in thresholds:
# Load the world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Assign colors to each continent for differentiation
    # Key: Continent name, Value: Assigned color
    continent_colors = {
        'Africa': '#ffcc99',
        'Europe': '#99ccff',
        'Asia': '#ff9999',
        'North America': '#99ff99',
        'South America': '#ffff99',
        'Oceania': '#cc99ff',
        'Antarctica': '#aaa'
    }

    # Plotting
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))

    # Plot each continent with its assigned color, one by one
    world[world['continent'] == 'Africa'].plot(ax=ax, color=continent_colors['Africa'])
    world[world['continent'] == 'Europe'].plot(ax=ax, color=continent_colors['Europe'])
    world[world['continent'] == 'Asia'].plot(ax=ax, color=continent_colors['Asia'])
    world[world['continent'] == 'North America'].plot(ax=ax, color=continent_colors['North America'])
    world[world['continent'] == 'South America'].plot(ax=ax, color=continent_colors['South America'])
    world[world['continent'] == 'Oceania'].plot(ax=ax, color=continent_colors['Oceania'])
    world[world['continent'] == 'Antarctica'].plot(ax=ax, color=continent_colors['Antarctica'])

    # Apply hatch pattern to countries with population >= threshold
    world[world['pop_est'] > threshold].plot(ax=ax, color='none', hatch='////', edgecolor='black')

    # Custom legend
    # Note: Hatch pattern in legend is a workaround since matplotlib legend does not support hatches directly
    legend_labels = [
        mpatches.Patch(facecolor='none', hatch='////', label=f'>= {threshold:,} obyvatel', edgecolor='black'),
        mpatches.Patch(facecolor='none', label=f'< {threshold:,} obyvatel', edgecolor='none')
    ]
    plt.legend(handles=legend_labels, title="Populace")

    # Set the title of the map
    ax.set_title('Populace států v roce 2023')

    # Show the map
    plt.show()

    # Print message with template string (f-string), which allows to insert variables into the string
    print(f"Mapa pro threshold {threshold} byla vykreslena.")

print("Všechny tři mapy byly vykresleny! Volejte sláva!")
