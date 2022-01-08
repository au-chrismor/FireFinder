import os

import matplotlib.pyplot as plt
import scipy.io
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as ply

audio_file = 'purenvwh.wav'
# audio_file = '20210109_232215.wav'
dataset_path = 'E:\\Data\\audio\Lightning-Detection\\whistles'

wave_data = os.path.join(dataset_path, audio_file)

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
plt.savefig('{0}.png'.format(audio_file))
plt.show()

