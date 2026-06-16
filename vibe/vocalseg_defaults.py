def get_default_params():
    return {
        'n_fft': 512, # FFT window size
        'hop_length_ms': 1, # number audio of frames in ms between STFT columns
        'win_length_ms': 5, # size of fft window (ms)
        'ref_level_db': 10, # reference level dB of audio
        'pre': 0.97, # coefficient for preemphasis filter
        'min_level_db': -120, # default dB minimum of spectrogram (threshold anything below)
        'silence_threshold': 0.07, # threshold for spectrogram to consider noise as silence
        'spectral_range': [400, 6000], # spectral range to care about for spectrogram
        'mask_thresh_std': 1.0, # standard deviations above median to threshold out noise (higher = threshold more noise)
        'figsize': (30, 3), # size of figure for displaying output (default: {(20, 5)})
        'min_silence_for_spec': 0.01, # shortest expected length of silence in a song (used to set dynamic threshold)
        'neighborhood_thresh': 0.25, # threshold number of neighborhood time-frequency bins above 0 to consider a bin not noise
        'neighborhood_time_ms': 5, # size in ms of neighborhood-continuity filter
        'neighborhood_freq_hz': 2000, # size in Hz of neighborhood-continuity filter
        'temporal_neighbor_merge_distance_ms': 5, # longest distance at which two elements should be considered one
        'overlapping_element_merge_thresh': 0.25, # proportion of temporal overlap to consider two elements one
        'min_element_size_ms_hz': [10, 1000] # smallest expected element size (in ms and Hz): everything smaller is removed
    }
  
