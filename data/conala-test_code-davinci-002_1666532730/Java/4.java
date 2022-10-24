// Create a new Spectrogram
Spectrogram spectrogram = new Spectrogram(data, sampleRate);

// Create a new Colorbar
Colorbar colorbar = new Colorbar(spectrogram);

// Add the Colorbar to the Spectrogram
spectrogram.addColorbar(colorbar);