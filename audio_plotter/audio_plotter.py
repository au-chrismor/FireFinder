import os

import matplotlib.pyplot as plt
import scipy.io
import scipy.io.wavfile
import numpy as np

audio_file = 'purenvwh.wav'
# audio_file = '20210109_232215.wav'
dataset_path = '/data/audio/lightning-Detection'
output_path = '/data/audio/Lightning-Image-Format'

for dr in os.listdir(dataset_path):
    local_path = '{0}/{1}'.format(dataset_path, dr)
    for file in os.listdir(local_path):
        if file.endswith('.wav'):
            wave_data = '{0}/{1}/{2}'.format(dataset_path, dr, file)
            image_data = '{0}/{1}/{2}.png'.format(output_path, dr, file)

            print('Input File: {0}'.format(wave_data))
            print('Output File: {0}'.format(image_data))

            sample_rate, audio_buffer = scipy.io.wavfile.read(wave_data)
            duration = len(audio_buffer) / sample_rate

            print('Sample Rate: {0}'.format(sample_rate))
            print('Duration: {0}'.format(duration))

            time = np.arange(0, duration, 1 / sample_rate)

            plt.plot(time, audio_buffer)
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.axis("off")
            #plt.title(audio_file)
            plt.savefig(image_data)
            #plt.show()
            plt.
