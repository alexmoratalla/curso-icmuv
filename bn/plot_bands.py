import matplotlib.pyplot as plt

def read_bands_gnu(filename):
    with open(filename,'r') as file:
        lines = file.readlines()

    bands = []
    current_band = []
    for line in lines:
        if line.strip():
            current_band.append([float(x) for x in line.split()])

        else:
            if current_band:
                bands.append(current_band)
                current_band = []
    if current_band:
        bands.append(current_band)

    return bands

def process_bands(bands):
    processed_bands = []
    for band in bands:
        k_points = [point[0] for point in band]
        energies = [point[1] for point in band]
        processed_bands.append((k_points, energies))
    return processed_bands

def plot_bands(processed_bands):
    plt.figure(figsize=(8,6))

    for k_points, energies in processed_bands:
        plt.plot(k_points, energies, 'crimson', lw = 1.5)

    plt.ylabel('Energy (eV)')
    
    tick_positions = [0.0000, 0.5774, 0.9107, 1.5774]
    tick_labels = ['$\Gamma$', 'M', 'K', '$\Gamma$']

    plt.xticks(tick_positions, tick_labels)
    plt.xlim(0.0000, 1.5774)
    plt.ylim(-6.0, 10.0)

    plt.axvline(x = 0.5774, linestyle = 'dashed', dashes = (5,10), color = 'gray')
    plt.axvline(x = 0.9107, linestyle = 'dashed', dashes = (5,10), color = 'gray')

    plt.show()

filename = 'bn-bands.gnu'
bands = read_bands_gnu(filename)
processed_bands = process_bands(bands)
plot_bands(processed_bands)
