# VIBE
**V**ocal acoustic **I**nversion to **B**iomechanical **E**stimates

VIBE reconstructs the time-dependent control parameters of a biomechanical model of the zebra finch (Taeniopygia guttata) syrinx directly from recorded song, recovering the physiological instructions underlying vocal production:

- **α(t)** — air sac pressure
- **β(t)** — syringeal muscle tension

These parameters are the coupled inputs to a nonlinear oscillator model of the syrinx ([Perl et al. 2011](https://doi.org/10.1103/physreve.84.051909); [Amador et al. 2013](https://doi.org/10.1038/nature11967)).

## Installation

```bash
pip install git+https://github.com/laurenostrowski/VIBE.git
```

Or clone and install locally:

```bash
git clone https://github.com/laurenostrowski/VIBE.git
cd VIBE
pip install -e .
```

Dependencies: `numpy`, `scipy`, `torch`, `matplotlib`, `joblib`, `tqdm`. Pitch estimation in the example notebooks optionally uses [`noisereduce`](https://github.com/timsainb/noisereduce) and the segmentation step uses [`vocalization-segmentation`](https://github.com/timsainb/vocalization-segmentation).


## Usage

### Pitch extraction parameters

Pitch extraction is the one stage in the pipeline that benefits from per-bird tuning. 
`get_pitch` selects a fundamental ateach frame by Viterbi decoding over prominent 
spectral peaks, and the scoring termsthat resolve the fundamental against its 
harmonics depend on the frequency rangeand harmonic structure of the individual bird. 
Defaults are reasonable for most birds. Tune once per bird on a few representative 
songs, then hold the settings fixed across that bird's corpus.

Settings are passed to `song_to_parameters` through `pitch_kwargs` and forwarded
to `get_pitch`:

```python
pitch_kwargs = {
    'f0_min': 300.0,           # lower bound of the f0 search (Hz)
    'f0_max': 4000.0,          # upper bound of the f0 search (Hz)
    'freq_boost_exp': 5.0,     # raise to favor lower peaks (default 1.0)
    'harmonic_bonus': 5.0,     # raise when harmonic stacks are strong (default 5.0)
    'min_prominence_db': 1.0,  # lower when peaks are weak (default 5.0)
}
```


To tune, call `get_pitch` directly and plot the contour over the spectrogram:

```python
from vibe import get_pitch

pitch, mag_db, freqs, times = get_pitch(
    waveform, vmask, fs_audio, hop_length, win_length, n_fft, **pitch_kwargs)

ax.imshow(mag_db, aspect='auto', origin='lower', cmap='gray_r',
          extent=[times[0], times[-1], freqs[0], freqs[-1]],
          vmin=np.percentile(mag_db, 10), vmax=0.98 * np.max(mag_db))
ax.plot(times, pitch, 'magenta', lw=3, alpha=0.7)
```

`examples/fit_VIBE.ipynb` demonstrates this step for bird A.

### Fit a song

```python
from vibe import song_to_parameters

alpha, beta, fit_result = song_to_parameters(
    waveform,        # 1D audio waveform
    fs_audio,        # sample rate (Hz)
    vmask,           # boolean voicing mask, one value per STFT frame
    hop_length,      # STFT hop (samples)
    win_length,      # STFT window (samples)
    n_fft,           # FFT size
    pitch_kwargs=pitch_kwargs,   # optional per-bird pitch settings
)
```

`alpha` and `beta` are per-frame trajectories over the whole song. At voiced frames they are fit to the waveform; at unvoiced frames α follows a duration-dependent silence trajectory and β is held fixed. `fit_result` also contains the model amplitude, the optimizer positions, and the amplitude-fit correlation.

### Resynthesize from parameters

```python
from vibe import synthesize_song

rec_wav = synthesize_song(alpha, beta, fs_audio, len(waveform))
```

## Example notebooks

The `examples/` directory contains notebooks demonstrating segmentation, fitting, and resynthesis on example songs from three birds.

## Citation

If you use this code, please cite:

> Ostrowski LM, Méndez JM, Tostado-Marcos P, Cooper BG, Gentner TQ. Automated inference of respiratory and syringeal biomechanical trajectories from birdsong acoustics. *bioRxiv* 2026.08.03.742634 (2026). https://doi.org/10.64898/2026.08.03.742634

The underlying biomechanical model is described in:

> Perl YS, Arneodo EM, Amador A, Mindlin GB. Reconstruction of physiological instructions from zebra finch song. *Phys Rev E* 84, 051909 (2011).

> Amador A, Perl YS, Mindlin GB, Margoliash D. Elemental gesture dynamics are encoded by song premotor cortical neurons. *Nature* 495, 59–64 (2013).

## License

VIBE is released under the MIT License. See [LICENSE](LICENSE) for details.

Copyright (c) 2026 Lauren Ostrowski

